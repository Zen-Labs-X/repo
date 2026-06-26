#!/bin/sh
set -eu

target=/mnt/us/documents/ZenKOReader.sh
rm -f "$target"
[ ! -e "$target" ] || { echo "Failed to remove $target" >&2; exit 1; }

echo "ZenKOReader uninstall complete"
exit 0
