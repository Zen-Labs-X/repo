# AnnotationSync v2.0.0 🎉

The biggest release yet — new sync capabilities, a major internal
refactor, a hardened end-to-end test suite, and a new translation.

## ✨ New Features

- **Full Library Sync** — scan your entire library for books with
  annotations that were never synced (not just the currently dirty
  ones) and sync them all in one pass.
- **Device Purging** — remove a stale or retired device's entries from
  reading progress sync, with a one-click undo.

## 🌍 Localization

- Added **Simplified Chinese (zh_CN)** translation.
- Refreshed and completed existing translations.

## 🐛 Fixes

- Fixed a WebDAV `sync_server` reference bug that could corrupt state
  when handed to the storage provider.
- Bounded retries on persistent sync conflicts to prevent runaway
  loops.
- No-op resyncs no longer trigger a broadcast, keeping sync idempotent.
- Settings exclusion filters are now enforced at the push boundary.

## 🏗️ Under the Hood

- Major refactor of the sync orchestration: extracted dedicated modules
  for settings sync, the changed-documents queue, UI suppression, and
  provider adaptation — smaller, more testable, more maintainable code.
- A sprawling new **real-WebDAV end-to-end test harness** covering
  two-device sync, progress sync, merge conflicts, bookmark restore,
  highlight resizing, the pending queue, network reconnects, and more —
  dozens of new scenarios guarding against regressions.
- CI bumped to KOReader v2026.07.2.

## 📖 Docs

- README now documents Full Library Sync and Device Purging.
- Added a from-scratch guide for setting up a KOReader dev environment.

---

**Full Changelog**: https://github.com/dani84bs/AnnotationSync.koplugin/compare/v1.9.9999...v2.0.0
