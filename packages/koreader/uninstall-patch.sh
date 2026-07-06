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

# Read patch file or patch dir from tracking file.
PATCH_FILE=$(grep -E '^patch_file=' "$TRACKING_FILE" | cut -d= -f2- || true)
PATCH_DIR=$(grep -E '^patch_dir=' "$TRACKING_FILE" | cut -d= -f2- || true)

if [ -n "$PATCH_FILE" ]; then
    if [ ! -f "$PATCH_FILE" ]; then
        echo "Patch file $PATCH_FILE not found (already removed)."
    else
        echo "Removing $PATCH_FILE ..."
        rm -f "$PATCH_FILE"
    fi
elif [ -n "$PATCH_DIR" ]; then
    if [ ! -d "$PATCH_DIR" ]; then
        echo "Patch directory $PATCH_DIR not found (already removed)."
    else
        echo "Removing $PATCH_DIR ..."
        rm -rf "$PATCH_DIR"
    fi
else
    echo "Tracking file has no patch_file or patch_dir entry."
fi

rm -f "$TRACKING_FILE"

# Clean up tracking dir if empty
if [ -d "$TRACKING_DIR" ] && [ -z "$(ls -A "$TRACKING_DIR" 2>/dev/null)" ]; then
    rmdir "$TRACKING_DIR" 2>/dev/null || true
fi

sync
echo "Patch '$DISPLAY_NAME' uninstalled"
