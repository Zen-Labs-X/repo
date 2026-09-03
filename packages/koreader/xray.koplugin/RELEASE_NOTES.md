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

# 26.7.27

- Fix duplicate detection logic to prevent spoilers https://github.com/ultimatejimmy/xray.koplugin/issues/92
- Fix one bug with timeline
- Update logic to accommodate non-standard TOC formatting

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.7.23...26.7.27
