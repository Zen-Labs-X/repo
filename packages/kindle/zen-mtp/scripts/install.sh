#!/bin/sh

set -e

TMPDIR=/mnt/us/ZenPM-Temporary
mkdir -p "$TMPDIR"

# Download + Extract
curl -fSL --progress-bar -o "$TMPDIR/zenmtp.zip" \
  https://github.com/AnthonyGress/ZenKindleMTP/releases/latest/download/ZenMTP.zip
unzip -oq "$TMPDIR/zenmtp.zip" -d "$TMPDIR"

# Copy contents
cp -r "$TMPDIR"/* /mnt/us/

# Cleanup
rm -rf "$TMPDIR"

exit 0
