# v2.2.0

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

# v2.1.0

This release fixes reported issues from v2 and adds user suggested features. 
## New Features
- **Time-based goal type.** Users can now choose between page/time goal. Pages read today has been moved to the section title line, which can be set to display pages read, time read, or both.
- **Orientation lock.** Force the sleep screen into portrait/landscape independent of the book’s orientation. Option added to advanced menu.
- **Cover image alignment.** If stretch to fill is disabled, the book cover can now be aligned left, centre or right. Also, the letterbox fill can now be any user-chosen colour.
- **Custom quote option** added to the message section. Quotes are saved in `custom_quotes.lua` for easy editing.
- **Series display option.** Enable series name (and series # if available) in the book section.
- **Hidden flow support.** Book time remaining, page numbers and percentage read now work with hidden flow (if activated).
## Fixes
- **Expanded document format support.** Fixed a crash when using plugin with `cbz` or `pdf` files. These often lack chapter metadata, so it’s recommended to disable the chapter section when reading these formats (chose not to program this to be disabled outright on the off-chance that they contain chapter information).
- **Power off stability.** Fixed a crash when powering down from within KOReader. Sleep screen will now also correctly remain as the last image on display when powered off.
- **Silent failure fix.**  If the plugin is opened from the file manager before being run in a book, it will now show a notification explaining why nothing is displayed, rather than silently not loading.
- **Plugin version metadata fix.** Fixed a crash where plugins version metadata was being read incorrectly by other plugins.
- **File manager sleep screen update.** Sleep screen contents are now updated on book closure, so the file manager sleep screen always shows the most up-to-date information.
- **Comic icons updated.** Jpeg icons changed to svgs so they can be recoloured with progress bar colours. The comic preset has been updated to use new features and is now suited for reading comics in landscape.
- **Menu and display adjustments.** Section gap options moved into a submenu, standardised section names and slightly modified goal section strings.

For installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v2.0.0

Customisable Sleep Screen is now available as a KOReader plugin. This release replaces the original patch version with a plugin rewrite, making installation simpler and adding new features and fixes based on feedback from v1.

## New Features
- Simpler installation: fonts and icons are now bundled, so no manual folder setup is required
- Two new presets based on the Catppuccin and Nord colour palettes, with matching wallpapers and two new icon sets
- Added language support for 12 languages: `de`, `es`, `fr`, `it`, `ja`, `ko`, `nl`, `pl`, `pt_BR`, `ru`, `vi`, `zh_CN`
- Info-box background and text colour options
- Daily stats scope option: choose between all books or current book only
- Stretch cover to fill toggle: disable to preserve cover aspect ratio with black/white fill
- Cosmetic-only progress bar option for the message section
- Long-press help text added to most menu items
- Reset options now restore from the active preset instead of factory defaults

## Fixes
- Book/chapter time remaining can now be disabled
- Message section visibility is no longer tied to KOReader’s built-in sleep screen message setting
- Book highlights now work across all metadata locations
- Exit sleep screen gesture is now respected within books
- Sleep screen now loads up-to-date details on first load
- Daily stats now read from the correct KOReader stats table
- Various calculation improvements, including weekly goal and chapter count handling

## Plugin Rewrite
The main menu has been moved and is now registered using the proper KOReader plugin method. v1 was a large single `.lua` patch that modified KOReader internals. v2 is a plugin rewrite that utilises more of KOReader’s own modules.

## Upgrading from v1
If you are upgrading from the original patch version, delete the old patch file and folders first: `2-customisable-sleep-screen.lua`, `customisable-sleep-screen-fonts`, and `customisable-sleep-screen-iconsets`. Presets carry over, but any personally added icons or fonts will need to be copied into the new plugin folder.

For full installation instructions, see the [README](https://github.com/pxlflux/customisablesleepscreen.koplugin/blob/main/README.md).

# v1.0.0

Original patch release of Customisable Sleep Screen for KOReader.

Displays reading stats & book info on your sleep screen with extensive customisation options in the settings menu and the ability to save/load your own configurations to quickly switch between designs.

This release has been superseded by v2.0.0, which converts the patch to a 
native .koplugin with additional features, fixes, and simpler installation. See the latest release.
