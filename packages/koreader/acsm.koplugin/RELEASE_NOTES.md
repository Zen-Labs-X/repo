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
