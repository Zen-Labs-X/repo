# v0.3.4


### Fixed
- Auto-track sets **Currently reading** as soon as the book is linked (and on the first pages). It no longer waits for 1% progress.
  Opening an unlinked book no longer burns the 2s ensure before search/link finishes.

# v0.3.3


First public release: sync reading status and ratings with livelib.ru
(classic site or Beta API), auto-tracking, English / Russian / Ukrainian UI.

### Fixed
- Stale collection id after the book is removed on the website (beta `PATCH`/`DELETE` 404 → recreate or treat delete as success).
- Sidecar rating stores the value accepted by the server; a failed rating PATCH can be retried.
- Opening a book no longer double-sends «Currently reading».

### Changed
- GitHub Release zip includes `livelib_config.example.lua` and `README.md`. The `docs/` folder and maintainer tooling stay out of the zip.

### Removed
- Unused Livelib username setting (never used to build profile links).
- Dead code: unused sidecar helpers, unread `last_page` state, unused `ngettext` / `getLang` exports.
