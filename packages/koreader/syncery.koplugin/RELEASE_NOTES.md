## [v1.2.4] — 2026-08-14

### Fixed
- Cloud credentials now execute only through a private, session-scoped server
  copy. Dropbox access-token mutation can no longer overwrite Syncery or Cloud
  storage+ settings, and one bounded runtime is reused across Sync All instead
  of refreshing OAuth once per book.
- Cloud destinations selected below an account root now match the live server
  by routing identity (`type`, `name`, `address`) while preserving the selected
  folder as the runtime `url` override.
- Manifest listing, upload, download, and prefetch now use a narrow Cloud I/O
  facade that brackets `provider.base`, restores `show_unsupported`, validates
  remote Syncery filenames, and keeps raw provider objects out of sync logic.
- Reading Statistics and Vocabulary Builder now receive a pristine Dropbox
  refresh-token descriptor immediately before every periodic or manual DB sync.
  KOReader's in-place access-token mutation is no longer persisted and reused
  after expiry; repairing credentials for the same destination preserves the
  existing three-way-merge `.sync` state.

## What's Changed
* Dropbox fix by @d0nizam in https://github.com/d0nizam/syncery.koplugin/pull/22


**Full Changelog**: https://github.com/d0nizam/syncery.koplugin/compare/v1.2.3...v1.2.4