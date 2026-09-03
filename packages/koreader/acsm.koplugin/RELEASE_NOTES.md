# v0.0.13

**Full Changelog**: https://github.com/kaikozlov/acsm.koplugin/compare/v0.0.12...v0.0.13

- **Fixed: PDFs that use compressed cross-reference streams now process and open** — some ACSM PDFs (e.g. processed by qpdf or saved with Acrobat's Fast Web View/linearization) failed with a parsing error. The PDF parser now handles all five PNG prediction filter types used by these files. Fixes [#21](https://github.com/kaikozlov/acsm.koplugin/issues/21).
- **Internal cleanup of the PDF and fulfillment code** — consolidated duplicate parsing
paths. Processing is now verified end-to-end against Adobe's full public sample library (26 titles, both EPUB and PDF).

---

## Installation

1. Download `acsm-koplugin-v0.0.13.zip` below
2. Extract `acsm.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - Android: `/storage/emulated/0/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.

# v0.0.12

**Full Changelog**: https://github.com/kaikozlov/acsm.koplugin/compare/v0.0.11...v0.0.12

- **Fixed: ACSM processing crash on some Android devices (e.g. BOOX)** — resolves an "undefined symbol: CRYPTO_free" error caused by missing crypto symbols in vendor builds (https://github.com/kaikozlov/acsm.koplugin/issues/20).

---

## Installation

1. Download `acsm-koplugin-v0.0.12.zip` below
2. Extract `acsm.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - Android: `/storage/emulated/0/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.

# v0.0.11

**Full Changelog**: https://github.com/kaikozlov/acsm.koplugin/compare/v0.0.10...v0.0.11

- **ACSM PDFs open much faster**, especially on older or slower e-readers.
- **Various reliability fixes** for device activation and processing of EPUBs and PDFs.

---

## Installation

1. Download `acsm-koplugin-v0.0.11.zip` below
2. Extract `acsm.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - Android: `/storage/emulated/0/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.

# v0.0.10

**Full Changelog**: https://github.com/kaikozlov/acsm.koplugin/compare/v0.0.9...v0.0.10

- **Optional user patch**: open `.acsm` files launched from external apps (e.g. the PocketBook library). Only needed in specific cases — see [`patches/README.md`](https://github.com/kaikozlov/acsm.koplugin/blob/v0.0.10/patches/README.md).
- **Bug fixes** in Adobe activation and signing.

---

## Installation

1. Download `acsm-koplugin-v0.0.10.zip` below
2. Extract `acsm.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - Android: `/storage/emulated/0/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.

# v0.0.9

**Full Changelog**: https://github.com/kaikozlov/acsm.koplugin/compare/v0.0.8...v0.0.9

- **Book Information for .acsm files** — the Book Information screen now shows metadata parsed from the ACSM (title, author, publisher, language, target format, etc.) without needing to download the book first.
- **Fixed: ACSM appearing twice in "Open with"** — duplicate provider registration has been removed.
  
---

## Installation

1. Download `acsm.koplugin-v0.0.9.zip` below
2. Extract `acsm.koplugin` to your KOReader plugins directory:
   - Kindle: `/mnt/us/koreader/plugins/`
   - Kobo: `/.adds/koreader/plugins/`
   - Android: `/storage/emulated/0/koreader/plugins/`
   - reMarkable: `/home/root/koreader/plugins/`
3. Restart KOReader

See README for usage instructions.
