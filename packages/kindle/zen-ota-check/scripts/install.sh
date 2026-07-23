#!/bin/sh
set -e

curl -fSL --progress-bar -o /mnt/us/documents/zen-ota-check.sh \
  https://github.com/xZenLabs/check-ota-status-scriptlet/releases/latest/download/zen-ota-check.sh

exit 0
