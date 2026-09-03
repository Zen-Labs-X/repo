# v1.10.1

Session Cleaner v1.10.1 is the recommended public baseline.

This release keeps the trusted database/session engine and replaces the old UI with a stable native KOReader menu-based interface.

## Highlights
- stable fullscreen native-menu rewrite
- preserved DB/session engine
- exact session inspection before deletion
- multi-select session deletion
- UI scale presets
- cleaner typography and safer row presentation
- faster post-delete navigation through in-memory hot-path updates

## Compared with the old version
The old version already had the core idea and working database/session logic, but its UI was flatter, less native-feeling, and less efficient for heavy cleanup. v1.10.1 keeps the trusted engine while improving navigation, inspection clarity, batch deletion, and responsiveness.

## Safety
Session Cleaner deletes the real underlying rows from KOReader’s statistics database only after explicit confirmation. Backup-before-delete is supported.
