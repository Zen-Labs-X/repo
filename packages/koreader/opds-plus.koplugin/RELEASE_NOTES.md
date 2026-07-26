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
