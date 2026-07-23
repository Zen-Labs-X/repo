#!/bin/sh
set -e

curl -fSL --progress-bar -o /mnt/us/documents/koreader-installer.sh \
  https://github.com/xZenLabs/koreader-installer/releases/latest/download/KOReader.sh

exit 0
