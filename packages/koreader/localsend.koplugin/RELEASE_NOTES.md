# v1.4.5

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

# v1.4.4

## KOReader Plugin

### New Features

- **Portuguese (Portugal) translation**: LocalSend's UI is now available in Portuguese (Portugal) — the first community-contributed translation. The plugin follows KOReader's **Language** setting automatically, with untranslated strings falling back to English. Thanks @CookieCaptainD! (https://github.com/kaikozlov/localsend.koplugin/pull/16)

  > **Updating from v1.4.2 or earlier?** The translation system debuted in v1.4.3, so your first update won't include the locale files. After updating and restarting, open **Check for updates** again and tap **Reinstall** so they're installed.

### Bug Fixes

- **Older Kindle kernel support**: 32-bit ARM builds now run on Linux 2.6.22 kernels (such as the Kindle DX Graphite) that predate `epoll_create1`, `eventfd2`, `accept4`, `pipe2`, and `dup3`. The receiver can start, show up in LocalSend, and complete transfers on these older devices, extending the Linux 2.6.31 support added in v1.4.2 even further back.

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

# v1.4.3

## KOReader Plugin

### New Features

- **Send with LocalSend from the file menu**: Long-press a file or folder in File Manager, History, Collections, or File Search and tap **Send with LocalSend** to send it straight to a nearby device — no need to open the plugin menu first. A new setting lets you show or hide this context-menu button.
- **Translation support (foundation)**: LocalSend now has its own translation system that follows KOReader's **Language** setting automatically, independent of the core language packs. This release lays the groundwork; the first community translations are on the way, and contributors can add a language as a `.po` file — see the Translations guide in the repo.

### Bug Fixes

- **Settings menu stays open**: Opening **About** or **Recent transfers** from the settings menu no longer dismisses the menu behind it.

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

# v1.4.2

## KOReader Plugin

### Bug Fixes

- **Older Kindle receiver support**: 32-bit ARM builds now work on Amazon Linux 2.6.31 kernels (such as Paperwhite 1 / firmware 5.6.1.1) that lack `epoll_pwait` and `accept4`. The receiver can start, show up in LocalSend, and complete transfers again.
- **Update checks on older Kindles**: "Check for updates" no longer fails with `HTTP status: 000` when the firmware certificate bundle is too old to validate GitHub. Requests use KOReader's CA bundle when available.
- **Legacy iptables support**: Firewall setup works on older firmware that lacks `iptables -C`, or only ships iptables under common sbin paths.

### Improvements

- **Legacy Kindle compatibility docs**: Documented the verified firmware and syscall boundary, plus the release overlay and audit workflow used for older Amazon kernels.

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

# v1.4.1

## KOReader Plugin

### New Features

- **Built-in troubleshooting**: A new "Troubleshooting" menu walks you through common problems. "Check LocalSend" inspects Wi-Fi, the receiver, your save folder, and network access, then suggests a next step. Additional guided helpers cover "Can't find a device?" and "Transfer failed?" — plus a one-tap **support report** generator to make filing useful bug reports easier.
- **Quick actions and gestures**: "Send file" and "Send current book" can now be assigned to KOReader gestures, profiles, and quick-menu actions.
- **About menu**: A dedicated "About LocalSend" dialog shows the installed version, device architecture, and project link.
- **Compound extension routing**: Route tagged files such as `document.safari.pdf` separately from ordinary `.pdf` files. When no compound rule exists, routing falls back to the normal file extension.

### Improvements

- **Better update experience**: Updates now have a dedicated menu with full release notes, an available-update indicator, optional background checks, and the ability to reinstall the current version when recovering a damaged installation.
- **Scan again from the device picker**: Refresh nearby devices without leaving the selection dialog or restarting the send flow.
- **Graceful server shutdown**: The receiver stops more cleanly during KOReader exit and suspend, reducing leftover processes and port conflicts.
- **Cleaner uninstall**: KOReader's plugin management can now remove LocalSend settings, certificates, routing configuration, and temporary state when deleting the plugin.

---

## CLI Changes

### New Features

- **Discovery self-test**: The new `nettest` command checks multicast loopback, LocalSend announcements, HTTP registration responses, and visible network interfaces. Human-readable and JSON output are available.

### Improvements

- **Updated networking stack**: Updated Fiber, Pion WebRTC, DTLS, FastHTTP, and other Go dependencies to their latest compatible releases.

### Bug Fixes

- **Reliable LAN discovery**: The `scan` and `recv` discovery backend now listens across all eligible network interfaces, improving discovery on e-readers, constrained hardware, and multi-interface networks.
- **Stable WebRTC transfers**: Hardened the WebRTC send queue, file pipeline, and shutdown synchronization to prevent transfer desynchronization, partial-file handling errors, and shutdown hangs.

### Security

- **Atomic session admission**: Receive-session checks and creation are now performed atomically, preventing concurrent transfers from bypassing the single-session limit.
- **Mandatory V3 nonce exchange**: V3 HTTP uploads must complete the nonce exchange before preparing a transfer, preventing replay of stale handshake state.
- **Hardened WebRTC validation**: Incoming file headers, tokens, declared sizes, checksums, control messages, and signaling payloads now receive stricter validation.
- **Bounded request handling**: File uploads are streamed instead of buffered in memory, while JSON metadata and control messages have explicit size limits to reduce denial-of-service risk.

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
