#!/bin/sh
set -eu
# Generic KOReader plugin installer for Zen Package Manager
# Auto-detects KOReader installation across Kobo, Kindle, Android, Linux.
# Usage: install-plugin.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]
#   REPO          - "owner/repo" or "owner/repo@tag" or full API URL
#   ASSET_PATTERN - substring to match asset name (default: first .zip)
#   DISPLAY_NAME  - name for tracking file (default: derived from repo name)

# --- arg parsing ---
REPO_REF="${1:-${ZENPM_PACKAGE_SOURCE:-${ZENPM_SOURCE:-${PACKAGE_SOURCE:-}}}}"
ASSET_PATTERN="${2:-${ZENPM_PACKAGE_SOURCE_ASSET:-${ZENPM_SOURCE_ASSET:-${PACKAGE_SOURCE_ASSET:-}}}}"
DISPLAY_NAME="${3:-${ZENPM_PLUGIN_NAME:-${ZENPM_PACKAGE_DISPLAY_NAME:-}}}"

if [ -z "$REPO_REF" ]; then
    echo "Usage: install-plugin.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]"
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
    script_dir=$(CDPATH= cd "$(dirname "$0")" 2>/dev/null && pwd -P) || script_dir=""
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

KO_PLUGINS_DIR="$KO_ROOT/plugins"
TRACKING_DIR="$KO_ROOT/.zenpm-plugins"
TMP_DIR="/tmp/koplugin-install-$$"

if [ ! -d "$KO_PLUGINS_DIR" ]; then
    echo "KOReader plugins directory not found at $KO_PLUGINS_DIR"
    echo "KOReader found at $KO_ROOT but missing plugins/ subdirectory."
    exit 1
fi

mkdir -p "$TMP_DIR" "$TRACKING_DIR"

# --- utility: download file ---
download_file() {
    url="$1"
    output="$2"

    if command -v curl >/dev/null 2>&1; then
        if curl -fL "$url" -o "$output" 2>&1; then
            return 0
        fi
        echo "curl failed; trying wget..."
    fi

    if command -v wget >/dev/null 2>&1; then
        if wget -O "$output" "$url" 2>&1; then
            return 0
        fi
        echo "wget failed"
    fi

    if command -v busybox >/dev/null 2>&1; then
        if busybox wget -O "$output" "$url" 2>&1; then
            return 0
        fi
        echo "BusyBox wget failed"
    fi

    echo "Unable to download $url"
    return 1
}

# --- utility: extract zip ---
extract_zip() {
    archive="$1"
    destination="$2"

    if command -v unzip >/dev/null 2>&1; then
        unzip "$archive" -d "$destination"
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
    output="$2"

    if command -v curl >/dev/null 2>&1; then
        if curl -fL "$url" -o "$output" 2>&1; then
            return 0
        fi
        echo "curl failed; trying wget..."
    fi

    if command -v wget >/dev/null 2>&1; then
        if wget -O "$output" "$url" 2>&1; then
            return 0
        fi
        echo "wget failed"
    fi

    if command -v busybox >/dev/null 2>&1; then
        if busybox wget -O "$output" "$url" 2>&1; then
            return 0
        fi
        echo "BusyBox wget failed"
    fi

    echo "Unable to fetch release metadata from $url"
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

derive_name_from_asset() {
    asset_filename="$1"
    case "$asset_filename" in
        *.koplugin.zip)
            printf '%s\n' "${asset_filename%.zip}"
            ;;
        *)
            return 1
            ;;
    esac
}

# --- validate sha256 from release body ---
validate_sha() {
    archive_path="$1"
    release_body="$2"
    asset_filename="$3"
    asset_digest="$4"

    if ! command -v sha256sum >/dev/null 2>&1; then
        echo "(no sha256sum command — skipping verification)"
        return 0
    fi

    computed=$(sha256sum "$archive_path" | awk '{print $1}')

    # Look for a line in the release body that mentions this asset filename
    # and contains a 64-char hex string (SHA256).
    expected=$(printf '%s\n' "$release_body" \
        | grep -iF "$asset_filename" \
        | grep -oE '[a-fA-F0-9]{64}' \
        | head -n 1)

    if [ -z "$expected" ] && [ -n "$asset_digest" ]; then
        expected="$asset_digest"
    fi

    if [ -z "$expected" ]; then
        echo "(no SHA256 found in release body or asset digest for $asset_filename — skipping verification)"
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

extract_asset_digest() {
    release_json="$1"
    asset_filename="$2"

    printf '%s\n' "$release_json" \
        | awk -v name="$asset_filename" '
            index($0, "\"name\"") && index($0, "\"" name "\"") { found=1 }
            found && index($0, "\"digest\"") { print; exit }
        ' \
        | grep -oE 'sha256:[a-fA-F0-9]{64}' \
        | head -n 1 \
        | sed 's/^sha256://'
}

# --- main ---

echo "KOReader root: $KO_ROOT"

# Architecture supplied by the ZenPM client to pick a matching release asset.
TARGET_ARCH="${ZENPM_PACKAGE_ARCH:-${ZENPM_ARCH:-}}"

RELEASE_JSON=""
ASSET_URL=""
ASSET_DIGEST=""

case "$REPO_REF" in
    # Direct zip URL (e.g. codeload source archive or a specific release asset).
    # Skip the release API entirely and download it as-is.
    *.zip|https://codeload.github.com/*|http://codeload.github.com/*)
        ASSET_URL="$REPO_REF"
        echo "Direct archive: $ASSET_URL"
        ;;
    *)
        API_URL=$(resolve_api_url "$REPO_REF")
        echo "Resolving release: $API_URL"
        RELEASE_PATH="$TMP_DIR/release.json"
        if ! fetch_json "$API_URL" "$RELEASE_PATH"; then
            exit 1
        fi
        RELEASE_JSON=$(cat "$RELEASE_PATH")

        # Build the candidate asset list once (all .zip browser_download_urls).
        ASSET_LIST=$(printf '%s\n' "$RELEASE_JSON" \
            | grep -oE '"browser_download_url":\s*"[^"]*"' \
            | cut -d'"' -f4 \
            | grep -iE '\.zip$' || true)

        if [ -n "$ASSET_PATTERN" ]; then
            ASSET_URL=$(printf '%s\n' "$ASSET_LIST" | grep -iF "$ASSET_PATTERN" | head -n 1 || true)
        fi

        # No explicit pattern match yet: try the client arch token.
        if [ -z "$ASSET_URL" ] && [ -n "$TARGET_ARCH" ]; then
            ASSET_URL=$(printf '%s\n' "$ASSET_LIST" | grep -iF "$TARGET_ARCH" | head -n 1 || true)
            [ -n "$ASSET_URL" ] && echo "Selected asset for arch '$TARGET_ARCH'"
        fi

        # Fall back to the first zip asset.
        if [ -z "$ASSET_URL" ]; then
            ASSET_URL=$(printf '%s\n' "$ASSET_LIST" | head -n 1 || true)
        fi

        if [ -z "$ASSET_URL" ]; then
            echo "No matching asset found in release"
            [ -n "$ASSET_PATTERN" ] && echo "  pattern: $ASSET_PATTERN"
            exit 1
        fi
        ;;
esac

ASSET_FILENAME=$(printf '%s\n' "$ASSET_URL" | sed 's|.*/||')
echo "Found asset: $ASSET_FILENAME"
if [ -n "$RELEASE_JSON" ]; then
    ASSET_DIGEST=$(extract_asset_digest "$RELEASE_JSON" "$ASSET_FILENAME")
fi

# Derive display name
if [ -z "$DISPLAY_NAME" ]; then
    case "$REPO_REF" in
        https://codeload.github.com/*|http://codeload.github.com/*)
            # codeload.github.com/<owner>/<repo>/zip/... -> repo name
            DISPLAY_NAME=$(printf '%s\n' "$REPO_REF" \
                | sed 's|^https://codeload\.github\.com/||;s|^http://codeload\.github\.com/||' \
                | cut -d/ -f2)
            ;;
        *)
            DISPLAY_NAME=$(derive_name_from_asset "$ASSET_FILENAME" || derive_name "$REPO_REF")
            ;;
    esac
fi
[ -z "$DISPLAY_NAME" ] && DISPLAY_NAME="${ZENPM_PACKAGE_ID:-${PACKAGE_ID:-}}"
PLUGIN_DIR="$KO_PLUGINS_DIR/$DISPLAY_NAME"

# Download
ARCHIVE_PATH="$TMP_DIR/$ASSET_FILENAME"
echo "Downloading $ASSET_URL ..."
download_file "$ASSET_URL" "$ARCHIVE_PATH"

# Validate SHA from release body
RELEASE_BODY=$(printf '%s\n' "$RELEASE_JSON" | grep -oE '"body":\s*"[^"]*"' | head -n 1 | sed 's/^"body":\s*"//;s/"$//' || true)
# Unescape JSON: \n, \r, \t, \", \\
RELEASE_BODY=$(printf '%s\n' "$RELEASE_BODY" | sed 's/\\n/\n/g; s/\\r/\r/g; s/\\t/\t/g; s/\\"/"/g; s/\\\\/\\/g')
validate_sha "$ARCHIVE_PATH" "$RELEASE_BODY" "$ASSET_FILENAME" "$ASSET_DIGEST"

# Extract
echo "Extracting..."
EXTRACT_DIR="$TMP_DIR/extracted"
mkdir -p "$EXTRACT_DIR"
extract_zip "$ARCHIVE_PATH" "$EXTRACT_DIR"

# Determine the plugin root inside the extracted contents.
# If there's a single top-level directory, use its contents as the plugin.
CONTENTS=$(ls -A "$EXTRACT_DIR")
ENTRY_COUNT=$(printf '%s\n' "$CONTENTS" | wc -l | tr -d ' ')
if [ "$ENTRY_COUNT" = "1" ] && [ -d "$EXTRACT_DIR/$CONTENTS" ]; then
    SRC_DIR="$EXTRACT_DIR/$CONTENTS"
    # If the single top-level dir is already a .koplugin bundle, preserve its
    # name as the install dir. KOReader only loads dirs ending in .koplugin.
    case "$CONTENTS" in
        *.koplugin)
            DISPLAY_NAME="$CONTENTS"
            PLUGIN_DIR="$KO_PLUGINS_DIR/$DISPLAY_NAME"
            ;;
    esac
else
    SRC_DIR="$EXTRACT_DIR"
fi

# Ensure the install dir ends in .koplugin so KOReader will load it.
case "$PLUGIN_DIR" in
    *.koplugin) ;;
    *)
        DISPLAY_NAME="$DISPLAY_NAME.koplugin"
        PLUGIN_DIR="$KO_PLUGINS_DIR/$DISPLAY_NAME"
        ;;
esac

# Install
echo "Installing to $PLUGIN_DIR ..."
rm -rf "$PLUGIN_DIR"
mkdir -p "$PLUGIN_DIR"
cp -r "$SRC_DIR"/* "$PLUGIN_DIR"/ 2>/dev/null || true

# Remove macOS metadata if present
rm -rf "$PLUGIN_DIR/__MACOSX" 2>/dev/null || true

# Run custom install script if present
if [ -x "$PLUGIN_DIR/install.sh" ]; then
    echo "Running plugin install script..."
    ( cd "$PLUGIN_DIR" && sh ./install.sh ) || {
        echo "Warning: plugin install.sh returned non-zero"
    }
fi

# Create tracking file
cat > "$TRACKING_DIR/$DISPLAY_NAME" <<EOF
name=$DISPLAY_NAME
plugin_dir=$PLUGIN_DIR
asset_url=$ASSET_URL
asset_filename=$ASSET_FILENAME
repo_ref=$REPO_REF
installed_at=$(date '+%Y-%m-%dT%H:%M:%S%z' 2>/dev/null || date)
EOF

# Clean up
rm -rf "$TMP_DIR"
sync

echo "Plugin '$DISPLAY_NAME' installed to $PLUGIN_DIR"
