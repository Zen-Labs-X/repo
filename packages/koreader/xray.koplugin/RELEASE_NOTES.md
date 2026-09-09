# 26.9.9

### What's New
- **Image viewer**: Added a dedicated viewer to inspect and browse maps, diagrams, and illustrations directly within X-Ray.
- **Non-touch device support**: Full navigation support for e-readers without a touch screen using physical buttons and D-pads ([#115](https://github.com/ultimatejimmy/xray.koplugin/issues/115)).
- Overall UI updates to modernize

### Improvements
- **Unit converter**: Improved multi-language support to better handle non-English measurements and non-ASCII characters.
- **Performance & memory**: General optimizations to lower memory overhead and keep UI navigation snappy.
- Removed duplicate gesture registrations from the menu.

### Bug Fixes
- Fixed an issue affecting inline lookups.
- Fixed a crash under certain conditions ([#121](https://github.com/ultimatejimmy/xray.koplugin/issues/121)).
- Fixed a bug where in-text X-Ray wasn't matching properly in Cyrillic text ([#116](https://github.com/ultimatejimmy/xray.koplugin/issues/116)).
- Fixed a spoiler leak issue ([#118](https://github.com/ultimatejimmy/xray.koplugin/issues/118)).
- Fixed bug [#119](https://github.com/ultimatejimmy/xray.koplugin/issues/119).
* Fix italian translation by @blurryuma in https://github.com/ultimatejimmy/xray.koplugin/pull/123

## New Contributors
* @blurryuma made their first contribution in https://github.com/ultimatejimmy/xray.koplugin/pull/123

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.27...26.9.9

# 26.8.27

## What's Changed
- Fix AI request cancellation across suspend and timeout. Add cancel button to inline lookups.  by @billcstickers in https://github.com/ultimatejimmy/xray.koplugin/pull/113
- Refactored multiple similar functions for fetch cancelations
- Protect against app crashing. Thanks @tramch https://github.com/ultimatejimmy/xray.koplugin/issues/112
- some minor text/UI updates

## New Contributors
* @billcstickers made their first contribution in https://github.com/ultimatejimmy/xray.koplugin/pull/113

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.23...26.8.27

# 26.8.23

## What's Changed in 26.8.23

### Gemini Model Updates
- **New Gemini Models**: Added support for **Gemini 3.7 Flash** (now the primary default) and **Gemini 3.1 Pro Preview**.
- **Automatic Model Migration**: Any existing configurations using older or retired Gemini model names are now automatically updated to active equivalents.

### Smarter Series Handling & Offline Support
- **Improved Series Number Detection**: If a book has a series name but is missing an explicit index in its metadata, X-Ray can now extract book and volume numbers directly from the title (including numbers, written words, and Roman numerals) before falling back to AI.
- **Automatic Series Context Loading**: When opening a subsequent book in a series, X-Ray now automatically merges context from earlier books if they are already cached locally—no extra prompt or active internet connection required.
- **Series Cache Management**: Added a menu option to clear cached series data for the active book when needed.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.20...26.8.23

# 26.8.20

- Update to add new Gemini models

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.10...26.8.20

# 26.8.10

## What's Changed

- fix: keep PDF X-Ray context within current page by @giorgiobrullo in https://github.com/ultimatejimmy/xray.koplugin/pull/93
- fix: cancel active AI requests by @giorgiobrullo in https://github.com/ultimatejimmy/xray.koplugin/pull/94
- add safeguards to prevent crashing https://github.com/ultimatejimmy/xray.koplugin/issues/97
- Fix text splitting logic to prevent issues with Chinese text https://github.com/ultimatejimmy/xray.koplugin/issues/96
- fix bug with unit converter being disabled
- fix  bug with inline fetching

# New Contributors

- @giorgiobrullo made their first contribution in https://github.com/ultimatejimmy/xray.koplugin/pull/93

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.9...26.8.10
