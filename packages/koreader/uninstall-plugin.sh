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
