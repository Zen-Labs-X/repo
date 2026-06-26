#!/bin/sh
set -e

LOG_FILE="/mnt/us/ZenKOReader.log"
LOG_PIPE="/tmp/zen-koreader-install.$$"

mkfifo "$LOG_PIPE"
tee "$LOG_FILE" < "$LOG_PIPE" &
TEE_PID=$!
exec > "$LOG_PIPE" 2>&1
rm -f "$LOG_PIPE"

finish_logging() {
  status=$?
  set +e
  exec 1>&- 2>&-
  wait "$TEE_PID"
  exit "$status"
}

trap finish_logging EXIT HUP INT TERM

echo "ZenKOReader install started: $(date)"
echo "Downloading ZenKOReader launcher..."
curl -fSL --progress-bar -o /mnt/us/documents/ZenKOReader.sh \
  https://github.com/xZenLabs/ZenKOReaderKindle/releases/latest/download/ZenKOReader.sh
echo "Installed /mnt/us/documents/ZenKOReader.sh"
echo "ZenKOReader install complete: $(date)"

exit 0
