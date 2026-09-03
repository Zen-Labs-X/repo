# v1.2.0

# OPDS Plus v1.2.0

This release includes merged PRs, issue resolutions, and new user-facing settings since v1.1.0.

> [!IMPORTANT]
> **Upgrade method for existing users:** This release is based on a complete plugin rewrite.
> To avoid stale files and update issues, **remove the old `opds_plus.koplugin` directory entirely**, then install the new release fresh.

### Added
- Book Info Dialog for at-a-glance book metadata with improved cover handling.
- Direct dispatcher actions for:
  - OPDS Plus: Sync all catalogs
  - OPDS Plus: Force sync all catalogs
- Cover pipeline improvements with disk-backed cache and lifecycle-safe image loading.
- New Cover Settings:
  - Prefer Large Covers (quality-first source selection)
  - Enable Cover Cache toggle
  - Advanced cache controls: max size, TTL, and manual cache clear

### Changed
- Refactored debug architecture to standardize logging through shared utilities.
- Extended state-manager usage across UI menu components.
- Removed obsolete/dead code and simplified some loader internals.
- Updated GitHub Actions dependencies for checkout and artifact workflows.

### Fixed
- Gesture registration failures (Issue #58).
- Duplicate PDF entries in results (Issue #57).
- Book info dialog stability issues, including filename capture timing and cover widget behavior.

### Thanks
Special thanks to these contributors for their work in this release cycle:
- Michael Cummings (@kodermike)
- Gavin Mogan (@halkeye)

### Documentation
- Added KOReader installation/upgrade path reference:
  https://github.com/koreader/koreader/wiki\#installationupgrading
- Updated README and CHANGELOG to cover major additions and settings for 1.2.0.

Full changelog:
https://github.com/greywolf1499/opds_plus.koplugin/blob/main/CHANGELOG.md

# v1.1.0

# OPDS Plus v1.1.0 - Polish & Performance Release

This release focuses on polishing the user experience, fixing bugs discovered during real-world testing, and optimizing space utilization across all device sizes.

## 🎯 Highlights

### ✨ Better Text Display
- Titles and authors now show **ellipsis (…)** when truncated
- Smart word-aware truncation for cleaner breaks
- UTF-8 safe for international characters

### 📐 Optimized Layouts
- **List View**: Dynamically fits maximum items with minimal whitespace
- **Grid View**: Automatically maximizes rows based on screen height
- Works perfectly on small e-readers, tablets, and large desktop displays
- No more wasted space at the bottom of pages!

### 🐛 Bug Fixes
- Fixed release package containing nested directories
- Fixed crashes in Grid Layout and Border settings menus
- Fixed `%%` appearing in confirmation messages
- Fixed version display in About dialog
- Fixed text truncation crashes

### 🔧 Developer Features
- **Debug Mode Toggle**: Enable verbose logging when troubleshooting
- **Version Display**: Now shown in settings menu
- Cleaned up excessive logging for better performance

## 📦 Installation

1. Download `opds_plus.koplugin.zip` from assets below
2. Extract to your KOReader plugins directory:
   - **Linux/Mac**: `~/.config/koreader/plugins/`
   - **Android**: `/sdcard/koreader/plugins/`
   - **Kindle**: `/mnt/us/koreader/plugins/`
3. Restart KOReader
4. Access via: **File Manager → Menu → OPDS Plus Catalog**

## ⚙️ Settings

All settings accessible via: **OPDS Plus Catalog → Settings**

- **Display Mode**: Switch between List and Grid views
- **List View Settings**: Cover size presets (Compact/Regular/Large/Extra Large)
- **Grid View Settings**: Layout presets, borders, and styling
- **Font & Text**: Customize fonts, sizes, colors
- **Developer**: Toggle debug mode for troubleshooting

## 🔄 Upgrading from v1.0.0

Simply replace the plugin directory with the new version. All your settings and catalogs will be preserved.

## 🙏 Acknowledgments

Thanks to everyone (myself, so far) who tested v1.0.0 and provided feedback! This release addresses all reported issues and includes several UX improvements based on real-world usage.

---

**Full Changelog**: https://github.com/greywolf1499/opds_plus.koplugin/blob/main/CHANGELOG.md

# v1.0.0
