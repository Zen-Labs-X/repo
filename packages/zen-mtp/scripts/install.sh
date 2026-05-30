#!/bin/sh

set -e

TMPDIR=/mnt/us/ZenPM-Temporary
mkdir -p "$TMPDIR"

# Download + Extract
curl -fSL --progress-bar -o "$TMPDIR/zenmtp.zip" \
  https://github.com/AnthonyGress/ZenKindleMTP/releases/latest/download/ZenMTP.zip
unzip -oq "$TMPDIR/zenmtp.zip" -d "$TMPDIR"

# Copy contents
mkdir -p /mnt/us/documents/zenmtp
cp -r "$TMPDIR"/* /mnt/us/documents/zenmtp/

# Cleanup
rm -rf "$TMPDIR"

exit 0
