## v1.9.9999

  ### Fixes
  - Stop false-positive same-page deletions in annotation sync — highlights sharing a page could be wrongly marked deleted; the scan now uses fine-grained position ranges instead of page numbers.
  (#87)
  - Eliminate O(n²) scan in annotation sync — syncing books with hundreds of annotations could take up to ~20 minutes; the scan is now linear. (#69)

  ### Features
  - Make plugin menu location configurable, with a new Menu location settings submenu.
  - Add user-defined directory exclude list for automatic progress sync (manual push/pull unaffected).

  ### Other
  - Test suite hardening (real XPointers in bookmark deletion tests, flushed nested sync schedules in integration tests) — no user-facing changes.