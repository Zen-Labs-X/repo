#!/bin/sh
set -eu
# Generic KOReader patch installer for Zen Package Manager
# Auto-detects KOReader installation across Kobo, Kindle, Android, Linux.
# Usage: install-patch.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]
#   REPO          - "owner/repo", "owner/repo@tag", full API URL, or direct .lua/.zip URL
#   ASSET_PATTERN - substring to match asset name (default: first .zip)
#   DISPLAY_NAME  - name for tracking file (default: derived from repo name)

# --- arg parsing ---
REPO_REF="${1:-${ZENPM_PACKAGE_SOURCE:-${ZENPM_SOURCE:-${PACKAGE_SOURCE:-}}}}"
ASSET_PATTERN="${2:-${ZENPM_PACKAGE_SOURCE_ASSET:-${ZENPM_SOURCE_ASSET:-${PACKAGE_SOURCE_ASSET:-}}}}"
DISPLAY_NAME="${3:-${ZENPM_PATCH_NAME:-${ZENPM_PACKAGE_DISPLAY_NAME:-}}}"

if [ -z "$REPO_REF" ]; then
    echo "Usage: install-patch.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]"
    echo "  REPO          - 'owner/repo' or 'owner/repo@tag' or full API URL"
    echo "  ASSET_PATTERN - substring to match asset name (default: first .zip)"
    echo "  DISPLAY_NAME  - name for tracking (default: repo name)"
    echo "Or set ZENPM_PACKAGE_SOURCE and optional ZENPM_PACKAGE_SOURCE_ASSET."
    exit 1
fi

# --- find KOReader root directory ---
is_koreader_root() {
    [ -d "$1" ] && { [ -f "$1/koreader.sh" ] || [ -f "$1/reader.lua" ]; }
}

find_koreader_root() {
    # 1. Explicit override from the ZenPM client.
    if [ -n "${ZENPM_KOREADER_ROOT:-}" ] && is_koreader_root "$ZENPM_KOREADER_ROOT"; then
        printf '%s\n' "$ZENPM_KOREADER_ROOT"
        return 0
    fi

    # 2. Anchor to the running install: the client runs inside the active
    # KOReader tree, so walk up from CWD and this script's dir.
    script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd -P) || script_dir=""
    for start in "$PWD" "$script_dir"; do
        [ -n "$start" ] || continue
        dir="$start"
        while [ -n "$dir" ] && [ "$dir" != "/" ]; do
            if is_koreader_root "$dir"; then
                printf '%s\n' "$dir"
                return 0
            fi
            dir=$(dirname "$dir")
        done
    done

    # 3. Fall back to common install locations across devices.
    candidates="
        /mnt/onboard/.adds/koreader
        /mnt/us/koreader
        /mnt/us/extensions/koreader
        /mnt/us/kmc/kpm/packages/koreader/koreader
        /sdcard/koreader
        /mnt/sd/koreader
        $HOME/koreader
    "
    for dir in $candidates; do
        if is_koreader_root "$dir"; then
            printf '%s\n' "$dir"
            return 0
        fi
    done

    return 1
}

KO_ROOT=$(find_koreader_root)

if [ -z "$KO_ROOT" ]; then
    echo "KOReader installation not found."
    echo "Searched: /mnt/onboard/.adds/koreader, /mnt/us/koreader, /mnt/us/kmc/kpm/packages/koreader/koreader, /sdcard/koreader, ..."
    exit 1
fi

KO_PATCHES_DIR="$KO_ROOT/patches"
TRACKING_DIR="$KO_ROOT/.zenpm-patches"
TMP_DIR="/tmp/kopatch-install-$$"

if [ ! -d "$KO_PATCHES_DIR" ]; then
    echo "Creating KOReader patches directory at $KO_PATCHES_DIR"
    mkdir -p "$KO_PATCHES_DIR"
fi

mkdir -p "$TMP_DIR" "$TRACKING_DIR"

# --- utility: download file ---
download_file() {
    url="$1"
    output="$2"

    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$url" -o "$output"
        return 0
    fi

    if command -v wget >/dev/null 2>&1; then
        wget -qO "$output" "$url"
        return 0
    fi

    echo "Neither curl nor wget is available"
    return 1
}

# --- utility: extract zip ---
extract_zip() {
    archive="$1"
    destination="$2"

    if command -v unzip >/dev/null 2>&1; then
        unzip -q "$archive" -d "$destination"
        return 0
    fi

    if command -v bsdtar >/dev/null 2>&1; then
        bsdtar -xf "$archive" -C "$destination"
        return 0
    fi

    echo "No zip extractor found (need unzip or bsdtar)"
    return 1
}

# --- utility: fetch JSON from URL ---
fetch_json() {
    url="$1"

    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$url"
        return 0
    fi

    if command -v wget >/dev/null 2>&1; then
        wget -qO- "$url"
        return 0
    fi

    echo "Neither curl nor wget is available"
    return 1
}

# --- resolve API URL ---
resolve_api_url() {
    ref="$1"
    case "$ref" in
        https://github.com/*/releases/tag/*|http://github.com/*/releases/tag/*)
            repo=$(printf '%s\n' "$ref" | sed 's|^https://github\.com/||;s|^http://github\.com/||;s|/releases/tag/.*$||')
            tag="${ref##*/releases/tag/}"
            printf 'https://api.github.com/repos/%s/releases/tags/%s\n' "$repo" "$tag"
            ;;
        https://github.com/*|http://github.com/*)
            repo=$(printf '%s\n' "$ref" | sed 's|^https://github\.com/||;s|^http://github\.com/||;s|/$||')
            printf 'https://api.github.com/repos/%s/releases/latest\n' "$repo"
            ;;
        https://api.github.com/*|http://api.github.com/*)
            printf '%s\n' "$ref"
            ;;
        http*)
            printf '%s\n' "$ref"
            ;;
        *@*)
            repo="${ref%@*}"
            tag="${ref#*@}"
            printf 'https://api.github.com/repos/%s/releases/tags/%s\n' "$repo" "$tag"
            ;;
        *)
            printf 'https://api.github.com/repos/%s/releases/latest\n' "$ref"
            ;;
    esac
}

# --- derive display name from repo ref ---
derive_name() {
    ref="$1"
    clean=$(printf '%s\n' "$ref" | sed 's|^https://api\.github\.com/repos/||;s|^http://api\.github\.com/repos/||;s|^https://github\.com/||;s|^http://github\.com/||')
    clean="${clean%@*}"
    printf '%s\n' "${clean##*/}"
}

github_repo_from_ref() {
    ref="$1"
    clean=$(printf '%s\n' "$ref" | sed 's|^https://api\.github\.com/repos/||;s|^http://api\.github\.com/repos/||;s|^https://github\.com/||;s|^http://github\.com/||;s|/$||')
    clean="${clean%@*}"
    owner=$(printf '%s\n' "$clean" | cut -d/ -f1)
    repo=$(printf '%s\n' "$clean" | cut -d/ -f2)
    if [ -n "$owner" ] && [ -n "$repo" ] && [ "$owner" != "$repo" ]; then
        printf '%s/%s\n' "$owner" "$repo"
        return 0
    fi
    return 1
}

# --- validate sha256 from release body ---
validate_sha() {
    archive_path="$1"
    release_body="$2"
    asset_filename="$3"

    if ! command -v sha256sum >/dev/null 2>&1; then
        echo "(no sha256sum command — skipping verification)"
        return 0
    fi

    computed=$(sha256sum "$archive_path" | awk '{print $1}')

    expected=$(printf '%s\n' "$release_body" \
        | grep -iF "$asset_filename" \
        | grep -oE '[a-fA-F0-9]{64}' \
        | head -n 1)

    if [ -z "$expected" ]; then
        echo "(no SHA256 found in release body for $asset_filename — skipping verification)"
        return 0
    fi

    if [ "$computed" = "$expected" ]; then
        echo "SHA256 verified: $computed"
        return 0
    else
        echo "SHA256 MISMATCH!"
        echo "  expected: $expected"
        echo "  got:      $computed"
        return 1
    fi
}

# --- main ---

echo "KOReader root: $KO_ROOT"

RELEASE_JSON=""
ASSET_URL=""

case "$ASSET_PATTERN" in
    http://*.lua|https://*.lua|http://*.zip|https://*.zip)
        ASSET_URL="$ASSET_PATTERN"
        echo "Direct asset: $ASSET_URL"
        ;;
    *.lua)
        if repo_path=$(github_repo_from_ref "$REPO_REF"); then
            ASSET_URL="https://raw.githubusercontent.com/$repo_path/HEAD/$ASSET_PATTERN"
            echo "Source patch asset: $ASSET_URL"
        fi
        ;;
esac

case "$REPO_REF" in
    *.lua|*.zip|https://codeload.github.com/*|http://codeload.github.com/*)
        ASSET_URL="$REPO_REF"
        echo "Direct asset: $ASSET_URL"
        ;;
    *)
        if [ -z "$ASSET_URL" ]; then
            API_URL=$(resolve_api_url "$REPO_REF")
            echo "Resolving release: $API_URL"

            RELEASE_JSON=$(fetch_json "$API_URL")

            ASSET_LIST=$(printf '%s\n' "$RELEASE_JSON" \
                | grep -oE '"browser_download_url":\s*"[^"]*"' \
                | cut -d'"' -f4 \
                | grep -iE '\.zip$' || true)

            if [ -n "$ASSET_PATTERN" ]; then
                ASSET_URL=$(printf '%s\n' "$ASSET_LIST" | grep -iF "$ASSET_PATTERN" | head -n 1 || true)
            fi

            if [ -z "$ASSET_URL" ]; then
                ASSET_URL=$(printf '%s\n' "$ASSET_LIST" | head -n 1 || true)
            fi

            if [ -z "$ASSET_URL" ]; then
                echo "No matching asset found in release"
                [ -n "$ASSET_PATTERN" ] && echo "  pattern: $ASSET_PATTERN"
                exit 1
            fi
        fi
        ;;
esac

ASSET_FILENAME=$(printf '%s\n' "$ASSET_URL" | sed 's|.*/||')
echo "Found asset: $ASSET_FILENAME"

# Derive display name
if [ -z "$DISPLAY_NAME" ]; then
    case "$REPO_REF" in
        https://codeload.github.com/*|http://codeload.github.com/*)
            DISPLAY_NAME=$(printf '%s\n' "$REPO_REF" \
                | sed 's|^https://codeload\.github\.com/||;s|^http://codeload\.github\.com/||' \
                | cut -d/ -f2)
            ;;
        *)
            DISPLAY_NAME=$(derive_name "$REPO_REF")
            ;;
    esac
fi
[ -z "$DISPLAY_NAME" ] && DISPLAY_NAME="${ZENPM_PACKAGE_ID:-${PACKAGE_ID:-}}"
PATCH_DIR="$KO_PATCHES_DIR/$DISPLAY_NAME"

# Download
ASSET_PATH="$TMP_DIR/$ASSET_FILENAME"
echo "Downloading $ASSET_URL ..."
download_file "$ASSET_URL" "$ASSET_PATH"

case "$ASSET_FILENAME" in
    *.lua)
        if [ -z "${ZENPM_PATCH_NAME:-}" ]; then
            DISPLAY_NAME="$ASSET_FILENAME"
        fi
        PATCH_FILE="$KO_PATCHES_DIR/$DISPLAY_NAME"
        case "$PATCH_FILE" in
            *.lua) ;;
            *) PATCH_FILE="$PATCH_FILE.lua" ;;
        esac

        echo "Installing to $PATCH_FILE ..."
        cp "$ASSET_PATH" "$PATCH_FILE"

        cat > "$TRACKING_DIR/$DISPLAY_NAME" <<EOF
name=$DISPLAY_NAME
patch_file=$PATCH_FILE
asset_url=$ASSET_URL
asset_filename=$ASSET_FILENAME
repo_ref=$REPO_REF
installed_at=$(date '+%Y-%m-%dT%H:%M:%S%z' 2>/dev/null || date)
EOF

        rm -rf "$TMP_DIR"
        sync

        echo "Patch '$DISPLAY_NAME' installed to $PATCH_FILE"
        exit 0
        ;;
esac

# Validate SHA from release body
RELEASE_BODY=$(printf '%s\n' "$RELEASE_JSON" | grep -oE '"body":\s*"[^"]*"' | head -n 1 | sed 's/^"body":\s*"//;s/"$//' || true)
RELEASE_BODY=$(printf '%s\n' "$RELEASE_BODY" | sed 's/\\n/\n/g; s/\\r/\r/g; s/\\t/\t/g; s/\\"/"/g; s/\\\\/\\/g')
validate_sha "$ASSET_PATH" "$RELEASE_BODY" "$ASSET_FILENAME"

# Extract
echo "Extracting..."
EXTRACT_DIR="$TMP_DIR/extracted"
mkdir -p "$EXTRACT_DIR"
extract_zip "$ASSET_PATH" "$EXTRACT_DIR"

# Determine the patch root inside the extracted contents.
CONTENTS=$(ls -A "$EXTRACT_DIR")
if [ "$(printf '%s\n' "$CONTENTS" | wc -l)" = "1" ] && [ -d "$EXTRACT_DIR/$CONTENTS" ]; then
    SRC_DIR="$EXTRACT_DIR/$CONTENTS"
else
    SRC_DIR="$EXTRACT_DIR"
fi

# Install
echo "Installing to $PATCH_DIR ..."
rm -rf "$PATCH_DIR"
mkdir -p "$PATCH_DIR"
cp -r "$SRC_DIR"/* "$PATCH_DIR"/ 2>/dev/null || true

# Remove macOS metadata if present
rm -rf "$PATCH_DIR/__MACOSX" 2>/dev/null || true

# Run custom install script if present
if [ -x "$PATCH_DIR/install.sh" ]; then
    echo "Running patch install script..."
    ( cd "$PATCH_DIR" && sh ./install.sh ) || {
        echo "Warning: patch install.sh returned non-zero"
    }
fi

# Create tracking file
cat > "$TRACKING_DIR/$DISPLAY_NAME" <<EOF
name=$DISPLAY_NAME
patch_dir=$PATCH_DIR
asset_url=$ASSET_URL
asset_filename=$ASSET_FILENAME
repo_ref=$REPO_REF
installed_at=$(date '+%Y-%m-%dT%H:%M:%S%z' 2>/dev/null || date)
EOF

# Clean up
rm -rf "$TMP_DIR"
sync

echo "Patch '$DISPLAY_NAME' installed to $PATCH_DIR"
