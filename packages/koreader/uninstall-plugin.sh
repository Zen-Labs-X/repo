#!/bin/sh
set -eu
# Generic KOReader plugin uninstaller for Zen Package Manager
# Auto-detects KOReader installation across devices.
# Usage: uninstall-plugin.sh DISPLAY_NAME
#   DISPLAY_NAME - name used during install (matches tracking file)

DISPLAY_NAME="${1:-}"

if [ -z "$DISPLAY_NAME" ]; then
    echo "Usage: uninstall-plugin.sh DISPLAY_NAME"
    echo "  DISPLAY_NAME - name used when the plugin was installed"
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

KO_PLUGINS_DIR="$KO_ROOT/plugins"
TRACKING_DIR="$KO_ROOT/.zenpm-plugins"

TRACKING_FILE="$TRACKING_DIR/$DISPLAY_NAME"

if [ ! -f "$TRACKING_FILE" ]; then
    echo "Tracking file not found: $TRACKING_FILE"
    echo "Plugin may have been manually removed or never installed."
    # Still try to remove the plugin directory
    PLUGIN_DIR="$KO_PLUGINS_DIR/$DISPLAY_NAME"
    if [ -d "$PLUGIN_DIR" ]; then
        echo "Removing plugin directory $PLUGIN_DIR ..."
        rm -rf "$PLUGIN_DIR"
    fi
    exit 0
fi

# Read plugin dir from tracking file
PLUGIN_DIR=$(grep -E '^plugin_dir=' "$TRACKING_FILE" | cut -d= -f2-)

if [ ! -d "$PLUGIN_DIR" ]; then
    echo "Plugin directory $PLUGIN_DIR not found (already removed)."
else
    echo "Removing $PLUGIN_DIR ..."
    rm -rf "$PLUGIN_DIR"
fi

rm -f "$TRACKING_FILE"

# Clean up tracking dir if empty
if [ -d "$TRACKING_DIR" ] && [ -z "$(ls -A "$TRACKING_DIR" 2>/dev/null)" ]; then
    rmdir "$TRACKING_DIR" 2>/dev/null || true
fi

sync
echo "Plugin '$DISPLAY_NAME' uninstalled"
