## KOReader Plugin

### Improvements

* **Better compatibility with current LocalSend apps**: Updated sending, receiving, and device discovery to match LocalSend 1.18.2. Transfers between KOReader and current LocalSend versions should be more reliable, especially when HTTPS is enabled.
* **Faster file transfers**: Sending multiple files now makes better use of parallel transfers, while file reading and writing has been optimized to reduce overhead on slower e-readers.
* **More reliable device discovery**: Nearby devices are less likely to disappear or become unreachable after network changes, and compatibility with older LocalSend clients has also been improved.
* **Better sleep and WiFi handling**: LocalSend now shuts down and comes back more reliably when your e-reader sleeps, wakes up, disconnects from WiFi, or reconnects quickly.
* **Keeps the device awake during transfers**: KOReader temporarily prevents standby while scanning or actively transferring a file, then returns to normal power-saving behavior when the operation finishes.
* **Better default receive folder**: If you haven't chosen a save folder yet, LocalSend now uses your KOReader home folder instead of the filesystem root.

### Bug Fixes

* **Receiver automatically recovers if it stops**: If the LocalSend receiver unexpectedly exits while it should be running, the plugin now tries to restart it automatically instead of quietly becoming unavailable.
* **More reliable HTTPS transfers**: Fixed several compatibility problems that could prevent discovery or transfers when encryption was enabled.
* **Large transfers no longer time out after 30 seconds**: File uploads can now continue for as long as the transfer itself is making progress.
* **File checksums and timestamps**: Received files now preserve timestamps supplied by the sender, and corrupted transfers can be retried cleanly without leaving the failed partial file behind.
* **LocalSend Web compatibility**: Fixed several PIN, connection, and transfer issues when sending to or receiving from LocalSend Web over WebRTC.

---

## Installation

1. Download the zip for your device's architecture:
   - **armv7** — Kindle (all models), Kobo, reMarkable 2, PocketBook
   - **arm64** — reMarkable Paper Pro
   - **arm-legacy** — Kindle 3, Kindle DX, older 32-bit ARM devices

   > **Not sure?** Try armv7 first. Use arm-legacy only if armv7 doesn't work on older hardware.

2. Extract `localsend.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.

