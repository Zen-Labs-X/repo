#!/bin/sh
set -eu
# Generic KOReader patch uninstaller for Zen Package Manager
# Auto-detects KOReader installation across devices.
# Usage: uninstall-patch.sh DISPLAY_NAME
#   DISPLAY_NAME - name used during install (matches tracking file)

DISPLAY_NAME="${1:-}"

if [ -z "$DISPLAY_NAME" ]; then
    echo "Usage: uninstall-patch.sh DISPLAY_NAME"
    echo "  DISPLAY_NAME - name used when the patch was installed"
    exit 1
fi

# --- find KOReader root directory ---
find_koreader_root() {
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
        if [ -d "$dir" ] && [ -f "$dir/koreader.sh" ]; then
            printf '%s\n' "$dir"
            return 0
        fi
    done

    kosh=$(find /mnt /sdcard "$HOME" -maxdepth 7 -name 'koreader.sh' -type f 2>/dev/null | head -n 1)
    if [ -n "$kosh" ]; then
        dirname "$kosh"
        return 0
    fi

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

TRACKING_FILE="$TRACKING_DIR/$DISPLAY_NAME"

if [ ! -f "$TRACKING_FILE" ]; then
    echo "Tracking file not found: $TRACKING_FILE"
    echo "Patch may have been manually removed or never installed."
    # Still try to remove the patch directory
    PATCH_DIR="$KO_PATCHES_DIR/$DISPLAY_NAME"
    if [ -d "$PATCH_DIR" ]; then
        echo "Removing patch directory $PATCH_DIR ..."
        rm -rf "$PATCH_DIR"
    fi
    exit 0
fi

# Read patch dir from tracking file
PATCH_DIR=$(grep -E '^patch_dir=' "$TRACKING_FILE" | cut -d= -f2-)

if [ ! -d "$PATCH_DIR" ]; then
    echo "Patch directory $PATCH_DIR not found (already removed)."
else
    echo "Removing $PATCH_DIR ..."
    rm -rf "$PATCH_DIR"
fi

rm -f "$TRACKING_FILE"

# Clean up tracking dir if empty
if [ -d "$TRACKING_DIR" ] && [ -z "$(ls -A "$TRACKING_DIR" 2>/dev/null)" ]; then
    rmdir "$TRACKING_DIR" 2>/dev/null || true
fi

sync
echo "Patch '$DISPLAY_NAME' uninstalled"
