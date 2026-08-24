## What's Changed in 26.8.23

### Gemini Model Updates
- **New Gemini Models**: Added support for **Gemini 3.7 Flash** (now the primary default) and **Gemini 3.1 Pro Preview**.
- **Automatic Model Migration**: Any existing configurations using older or retired Gemini model names are now automatically updated to active equivalents.

### Smarter Series Handling & Offline Support
- **Improved Series Number Detection**: If a book has a series name but is missing an explicit index in its metadata, X-Ray can now extract book and volume numbers directly from the title (including numbers, written words, and Roman numerals) before falling back to AI.
- **Automatic Series Context Loading**: When opening a subsequent book in a series, X-Ray now automatically merges context from earlier books if they are already cached locally—no extra prompt or active internet connection required.
- **Series Cache Management**: Added a menu option to clear cached series data for the active book when needed.

**Full Changelog**: https://github.com/ultimatejimmy/xray.koplugin/compare/26.8.20...26.8.23