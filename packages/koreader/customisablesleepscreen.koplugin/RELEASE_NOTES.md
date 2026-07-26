## New Features

* **Sleep screen image export** - Saves the generated sleep screen as an image when closing a book. Android users can then use the image with their device's screensaver feature. Also useful for sharing setups.
* **Rounded corners** - Configurable corner radius on the infobox, from small rounding to full pill shape.
* **Inline progress bars** - Progress bars can now sit within the text column rather than spanning the full section width.
* **Cover image in book section** - Add your book cover inline with reading stats as an alternative to the full background option.
* **Infobox layout tweaks** - Added an offset option to move the infobox slightly off-screen (useful for rounded corners), and per-side padding control.
* **Spin widgets** - All numeric settings now use spin widgets for precise control over values.
* **Hide message section header** - The message section title can now be hidden.

## Fixes

* Bold titles now apply to all section titles, not just the book title.
* Daily goal reset time and week start now follow KOReader's own reading statistics settings.
* Background folder picker defaults to classic file view and allows full directory navigation.
* Removed compiled language files, only `.po` source files are now used. Turkish po added.
* Plugin settings now moved out from `settings.reader.lua` and stored in two files within `koreader/settings`.
* Updated to support settings removal with KOReader’s new feature for on-device plugin removal (currently in the nightly builds).
* Replaced `Terminal` preset option with `Capsule` preset as shown in the screenshot.
* Renamed several Lua files to avoid potential filename conflicts.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).