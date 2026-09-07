# 2.1.0

### Added
- **Multi-Chapter Background Pre-Downloading**:
  - Configurable setting under options to auto-download the next N chapters/books in the background (setting to `0` disables it).
  - Runs sequentially in a background subprocess to avoid any UI lag or blocking during reading.
  - Added cooperative polling (1-second check interval) and standby lock management to prevent the device from entering sleep mode mid-download.
- **Skip End-of-Book Prompt**:
  - Added a setting to skip the end-of-book prompt and directly open the next book if it has already been pre-downloaded locally.
- **KOReader Action Registration**:
  - Registered the Komga Library Browser as a global KOReader action (`komga_browse`), enabling users to bind gesture shortcuts, key presses, or profiles to launch the browser directly from both the file manager and the reader.

### Fixed
- **Dispatcher Actions**:
  - Fixed the manual sync action (`komga_sync_now`) which had an incorrect `"none"` category and missing event method, ensuring it now correctly dispatches and triggers manual synchronization.
- **Home Screen Return Behavior**:
  - Aligned browser window stack properties and resolved settings menu stack retention to ensure closing the browser correctly returns to launcher/homescreen plugins (e.g. Simple UI) instead of showing the book file manager.

# 2.0.1

### Fixed
- **File Extension Handling**:
  - Fixed an issue where books ending with decimal volume or chapter numbers (e.g., `xxx-vol-12.5`) would be downloaded without their extensions, preventing KOReader from recognizing them.
  - Refined extension validation to check specifically for the expected extension when the media type is known, ensuring even mismatched metadata extensions are corrected (e.g., ensuring a `.cbz` file is always saved as `.cbz` even if named `.pdf` on the server).
  - Maintained general non-numeric extension validation for fallback cases when the media type is unknown.

# 2.0.0

### Added
- **Manual Book Matching & Side-loading**:
  - Added support to manually match side-loaded books to Komga IDs with local fallback metadata support.
- **Bulk Download in Browser**:
  - Selection gesture on book items (tap to toggle selection with checkmark overlays directly on cover images).
  - Contextual menu triggered by holding any book item to view download options (long-press is ignored for non-book entries).
  - Clear, simplified options to download selected books, download all books on the current page, or cancel (excluding duplicate/already downloaded books seamlessly).
- **Aesthetic Cover Indicators**:
  - Added visual indicators for local download status ("↓") on both list and grid item covers.
  - Implemented real-time reading progress indicators ("New", "Done", page/total pages, or raw page count) for list and grid views in the browser catalog.
- **Series Title Omission**:
  - Omitted prepending the series name from book titles when browsing books within a specific series since the series title is already displayed as the main title bar header.
  - Retained the series name prefix in multi-series lists (e.g. "Keep Reading", "On Deck", "Recently Added Books") for proper context.
- **Series Cover Image Download**:
  - Automatically downloads the series cover art (`.cover.<ext>`) to the series subdirectory on successful book download if no series cover is present, enabling folder-level cover previews in KOReader's coverbrowser.
- **Improved List Mode UI Layout**:
  - Made the list-mode separator lines significantly more distinct by changing the color to a darker mid-gray (`COLOR_GRAY`) and dynamically scaling the line height (`delimiter_h`) based on the device's screen scale factor.
  - Added wider, more balanced horizontal padding (left and right) on list view rows to give them elegant margins and breathe better on a wider variety of display devices.
- **Multi-language Localization**:
  - Added complete localization dictionaries for Traditional Chinese (`zh_TW`/`zh_HK`), Japanese (`ja`), and Spanish (`es`).

### Fixed
- **Memory Safety & Mutex Crash Prevention**:
  - Re-architected item layout rendering to avoid calling native `:getSize()` on un-parented `TextWidget` instances, eliminating the intermittent Freetype-related "pthread_mutex_lock called on a destroyed mutex" crash in KOReader.
  - Eliminated custom manual memory/badge tracking and destruction logic in favor of KOReader's native garbage collector and widget parenting lifecycle.
- **Robust Type Checking**:
  - Added defensive type verification (`type(...) == "table"`) on both `book` entries and `readProgress` objects to prevent the runtime error "attempt to index local 'readProgress' (a function value)".
- **KOSync Settings Integration**:
  - Aligned syncing actions to depend purely on native KOSync configuration state. Removed redundant custom sync interval options, background progress push loops, and offline Wi-Fi connection prompt warnings.
- **Dead Code & Import Cleanup**:
  - Removed multiple unused local variables, duplicate imports, and obsolete helper functions (`sanitize_for_settings`, custom recursive folder creation, etc.) to optimize the plugin's memory footprint.

# 1.0.0

First release. 

#### Highlights

1. **Browse Komga Catalog:** View libraries, series, recently added, and on-deck books with cover thumbnails, layout adjustments (list/grid modes), read status filters, and direct downloads.
2. **Metadata Extraction:** Upon downloading, automatically retrieves comic and book metadata (title, summary, authors, series index) from the Komga server and populates KOReader's document settings.
3. **Next Chapter Flow:** Prompts at the end of a book to check the server for the next chapter. If it is already downloaded, it opens it; if not, it automatically downloads and opens it.
4. **Integrated Progress Sync:** Integrations into the default KOReader sync (`kosync`) to intercept get/update progress events and sync directly with the Komga server for matched books.
5. **Auto RTL:** An option to automatically toggle reading direction to Right-to-Left (RTL) upon opening any book that are from Komga.
