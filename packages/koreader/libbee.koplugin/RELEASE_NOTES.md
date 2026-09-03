# 26.8.27

- Handle long folder names in the folder picker
- Add toggle for grouping when multiple accounts/library cards are active

**Full Changelog**: https://github.com/ultimatejimmy/libbee/compare/26.8.23...26.8.27

# 26.8.23

## What's New in v26.8.23

This release brings some much-requested features, including early book returns, automatic cleanup for expired loans, and a lot of polish across different screen sizes and Android devices.

### New Features & Enhancements

- **Direct Book Returns:** You can now return book loans early directly from Libbee without having to open the Libby app or website.
- **Auto-Expire Loans:** Added an automatic cleanup option for loans that have reached their due date.
- **Screen-Adaptive Layout:** The loan list now dynamically adjusts row counts based on your device's screen size and resolution, making things look much cleaner on smaller e-ink readers as well as larger screens.
- **Multi-Library & Multi-Account Polish:** Improved the interface and switching flow when managing multiple library cards and accounts.
- **Reverse-Order Log Viewer:** The in-app log viewer now displays the newest events first so you can quickly see recent sync activity or troubleshoot issues.
- **Preserved Reading Data:** Libbee now ensures KOReader *sidecar* files (bookmarks, highlights, and reading progress) are protected during book management actions.

### Bug Fixes & Stability

- **Download Stability:** Fixed a crash that could occur while downloading books or processing book covers.
- **Android Compatibility:** Resolved Android-specific file handling and network transport issues.
- **Pagination Fixes:** Fixed an issue where pagination could get out of sync when navigating larger loan lists.
- **Cache Refresh:** Fixed display issues where cached loan status didn't immediately update after changes.
- **Localization:** Updated and synchronized translations across all supported languages.

**Full Changelog**: https://github.com/ultimatejimmy/libbee/compare/26.8.21.7...26.8.23

# 26.8.21.7

- add detection for kindle/libby only books

**Full Changelog**: https://github.com/ultimatejimmy/libbee/compare/26.8.21.6...26.8.21.7

# 26.8.21.6

- Restore toast message when downloading.

**Full Changelog**: https://github.com/ultimatejimmy/libbee/compare/26.8.21.5...26.8.21.6

# 26.8.21.5

- fix network bug affecting android only
**Full Changelog**: https://github.com/ultimatejimmy/libbee/compare/26.8.21.4...26.8.21.5
