# v1.0.1

## Summary
This is a crash fix coming from recent versions of muPDF, you'll likely have seen this if you updated KOReader/Rakuyomi recently.
- Handled removal of `fz_close_device` in newer MuPDF versions.
- Added `pcall` blocks around device cleanup to silently catch missing symbols.
- Preserved memory leak protections for older app versions.

**Full Changelog**: https://github.com/mgrimace/stretch.koplugin/compare/v1.0.0...v1.0.1

# v1.0.0

## Summary

Initial release of the plugin for [KOReader](https://koreader.rocks/) to enable Manga and comic book pages to stretch to fill the screen width without adding extra scrolling. Two-page spreads are automatically rotated.

**Full Changelog**: https://github.com/mgrimace/stretch.koplugin/commits/v1.0.0
