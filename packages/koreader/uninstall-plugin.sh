#!/bin/sh
set -eu
# Generic KOReader plugin uninstaller for Zen Package Manager
# Auto-detects KOReader installation across devices.
# Usage: uninstall-plugin.sh DISPLAY_NAME
#   DISPLAY_NAME - name used during install (matches tracking file)

DISPLAY_NAME="${1:-${ZENPM_PLUGIN_NAME:-${ZENPM_PACKAGE_DISPLAY_NAME:-}}}"

if [ -z "$DISPLAY_NAME" ]; then
    SOURCE_ASSET="${ZENPM_PACKAGE_SOURCE_ASSET:-${ZENPM_SOURCE_ASSET:-${PACKAGE_SOURCE_ASSET:-}}}"
    case "$SOURCE_ASSET" in
        *.koplugin.zip)
            DISPLAY_NAME="${SOURCE_ASSET%.zip}"
            ;;
    esac
fi

if [ -z "$DISPLAY_NAME" ]; then
    SOURCE_REF="${ZENPM_PACKAGE_SOURCE:-${ZENPM_SOURCE:-${PACKAGE_SOURCE:-}}}"
    if [ -n "$SOURCE_REF" ]; then
        clean=$(printf '%s\n' "$SOURCE_REF" | sed 's|^https://api\.github\.com/repos/||;s|^http://api\.github\.com/repos/||;s|^https://github\.com/||;s|^http://github\.com/||')
        clean="${clean%@*}"
        DISPLAY_NAME="${clean##*/}"
    fi
fi

if [ -z "$DISPLAY_NAME" ]; then
    DISPLAY_NAME="${ZENPM_PACKAGE_ID:-${PACKAGE_ID:-}}"
fi

if [ -z "$DISPLAY_NAME" ]; then
    echo "Usage: uninstall-plugin.sh DISPLAY_NAME"
    echo "  DISPLAY_NAME - name used when the plugin was installed"
    echo "Or set ZENPM_PACKAGE_SOURCE_ASSET, ZENPM_PACKAGE_SOURCE, or ZENPM_PACKAGE_ID."
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

# Installer appends .koplugin to the tracking name when the source ref lacks it.
# If the bare name has no tracking file, fall back to the .koplugin variant.
if [ ! -f "$TRACKING_FILE" ]; then
    case "$DISPLAY_NAME" in
        *.koplugin) ;;
        *)
            if [ -f "$TRACKING_DIR/$DISPLAY_NAME.koplugin" ]; then
                DISPLAY_NAME="$DISPLAY_NAME.koplugin"
                TRACKING_FILE="$TRACKING_DIR/$DISPLAY_NAME"
            fi
            ;;
    esac
fi

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
