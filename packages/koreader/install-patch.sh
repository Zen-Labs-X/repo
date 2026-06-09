#!/bin/sh
set -eu
# Generic KOReader patch installer for Zen Package Manager
# Auto-detects KOReader installation across Kobo, Kindle, Android, Linux.
# Usage: install-patch.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]
#   REPO          - "owner/repo" or "owner/repo@tag" or full API URL
#   ASSET_PATTERN - substring to match asset name (default: first .zip)
#   DISPLAY_NAME  - name for tracking file (default: derived from repo name)

# --- arg parsing ---
REPO_REF="${1:-}"
ASSET_PATTERN="${2:-}"
DISPLAY_NAME="${3:-}"

if [ -z "$REPO_REF" ]; then
    echo "Usage: install-patch.sh REPO [ASSET_PATTERN] [DISPLAY_NAME]"
    echo "  REPO          - 'owner/repo' or 'owner/repo@tag' or full API URL"
    echo "  ASSET_PATTERN - substring to match asset name (default: first .zip)"
    echo "  DISPLAY_NAME  - name for tracking (default: repo name)"
    exit 1
fi

# --- find KOReader root directory ---
find_koreader_root() {
    candidates="
        /mnt/onboard/.adds/koreader
        /mnt/us/koreader
        /mnt/us/extensions/koreader
        /sdcard/koreader
        /mnt/sd/koreader
        $HOME/koreader
    "
    for dir in $candidates; do
        if [ -d "$dir" ] && [ -f "$dir/koreader.sh" ]; then
            printf '%s\n' "$dir"
            return 0
        fi
    done

    kosh=$(find /mnt /sdcard "$HOME" -maxdepth 4 -name 'koreader.sh' -type f 2>/dev/null | head -n 1)
    if [ -n "$kosh" ]; then
        dirname "$kosh"
        return 0
    fi

    return 1
}

KO_ROOT=$(find_koreader_root)

if [ -z "$KO_ROOT" ]; then
    echo "KOReader installation not found."
    echo "Searched: /mnt/onboard/.adds/koreader, /mnt/us/koreader, /sdcard/koreader, ..."
    exit 1
fi

KO_PATCHES_DIR="$KO_ROOT/patches"
TRACKING_DIR="$KO_ROOT/.zenpm-patches"
TMP_DIR="/tmp/kopatch-install-$$"

if [ ! -d "$KO_PATCHES_DIR" ]; then
    echo "KOReader patches directory not found at $KO_PATCHES_DIR"
    echo "KOReader found at $KO_ROOT but missing patches/ subdirectory."
    exit 1
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
    clean=$(printf '%s\n' "$ref" | sed 's|https\?://api\.github\.com/repos/||')
    clean="${clean%@*}"
    printf '%s\n' "${clean##*/}"
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

API_URL=$(resolve_api_url "$REPO_REF")
echo "Resolving release: $API_URL"

RELEASE_JSON=$(fetch_json "$API_URL")

# Extract asset download URL matching the pattern
if [ -n "$ASSET_PATTERN" ]; then
    ASSET_URL=$(printf '%s\n' "$RELEASE_JSON" \
        | grep -oE '"browser_download_url":\s*"[^"]*"' \
        | cut -d'"' -f4 \
        | grep -iF "$ASSET_PATTERN" \
        | head -n 1 || true)
else
    ASSET_URL=$(printf '%s\n' "$RELEASE_JSON" \
        | grep -oE '"browser_download_url":\s*"[^"]*"' \
        | cut -d'"' -f4 \
        | grep -iE '\.zip$' \
        | head -n 1 || true)
fi

if [ -z "$ASSET_URL" ]; then
    echo "No matching asset found in release"
    if [ -n "$ASSET_PATTERN" ]; then
        echo "  pattern: $ASSET_PATTERN"
    fi
    exit 1
fi

ASSET_FILENAME=$(printf '%s\n' "$ASSET_URL" | sed 's|.*/||')
echo "Found asset: $ASSET_FILENAME"

# Derive display name
[ -z "$DISPLAY_NAME" ] && DISPLAY_NAME=$(derive_name "$REPO_REF")
PATCH_DIR="$KO_PATCHES_DIR/$DISPLAY_NAME"

# Download
ARCHIVE_PATH="$TMP_DIR/$ASSET_FILENAME"
echo "Downloading $ASSET_URL ..."
download_file "$ASSET_URL" "$ARCHIVE_PATH"

# Validate SHA from release body
RELEASE_BODY=$(printf '%s\n' "$RELEASE_JSON" | grep -oE '"body":\s*"[^"]*"' | head -n 1 | sed 's/^"body":\s*"//;s/"$//')
RELEASE_BODY=$(printf '%s\n' "$RELEASE_BODY" | sed 's/\\n/\n/g; s/\\r/\r/g; s/\\t/\t/g; s/\\"/"/g; s/\\\\/\\/g')
validate_sha "$ARCHIVE_PATH" "$RELEASE_BODY" "$ASSET_FILENAME"

# Extract
echo "Extracting..."
EXTRACT_DIR="$TMP_DIR/extracted"
mkdir -p "$EXTRACT_DIR"
extract_zip "$ARCHIVE_PATH" "$EXTRACT_DIR"

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
