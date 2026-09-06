# v1.1.2

Fixes for module loading, gestures, and split-page navigation on KOReader.

- Fix settings crashes and duplicate menus caused by module-name collisions with Maximum or other plugins.
- Make two-finger tap, spread, pinch, and tap-to-collapse take priority while enabled, with normal gesture fallback when disabled.
- Fix split-page navigation using taps, swipes, and physical buttons, including RTL and backward navigation between spreads.
- Apply landscape modes immediately and on the opening page; keep auto-rotate and split defaults mutually exclusive.
- Cancel stale pan callbacks and restore previous zoom, pan, reading direction, and continuous-view settings after temporary zooming.
- Retain the v1.1.1 physical-button fix and correct layout updates when restoring portrait orientation.

Installation: download **leadingmangazoom.koplugin.zip**, extract it into KOReader's **plugins/** directory, replace the existing **leadingmangazoom.koplugin** folder, and restart KOReader. Disable Reflow for the document.

Validation: regression tests pass on Lua 5.1 and LuaJIT, with touch-dispatch integration checks against KOReader 2026.03 and 2026.07. Physical-device testing was not available.

Changes: https://github.com/Auri3l/leadingmangazoom.koplugin/pull/6

# v1.1.1

v1.1.1 Release: Fix physical page-turn button remapping bug on Kobo Sage, Kobo Libra 2, Kobo Forma, PocketBook, and Kindle Oasis devices when auto-rotating landscape pages.

# v1.1.0

v1.1.0 release: Add CZB support, fix zoom coordinates, pinch gesture, and RTL split-page navigation

# v1.0.0

Initial release of LeadingMangaZoom for KOReader.

Two-finger tap to zoom into any quadrant. Tap to zoom back out. Spread/pinch for page zoom. Auto-rotate and page split for landscape pages.

**Installation:** Extract the zip and copy the `leadingmangazoom.koplugin` folder into KOReader's `plugins/` directory. Restart KOReader.

Supports CBZ, CBR, and PDF files. Requires touch-enabled device.
