#!/bin/sh
set -eu

target=/mnt/us/documents/KOReader.sh
rm -f "$target"
[ ! -e "$target" ] || { echo "Failed to remove $target" >&2; exit 1; }

echo "KOReader uninstall complete"
exit 0
