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
