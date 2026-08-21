## Changes
- Match manifest-tracked books by stable server ID before comparing titles and filenames.
- Prevent title, subtitle, volume-formatting, and source-filename changes from downloading the same BookOrbit book again.
- Keep metadata refresh replacements on the existing local path.
- Extend Mirror selected sync source to move older manifest-tracked duplicates of the same server book to `.library-sync-trash`.
- Keep the copy matching the current download profile when available; otherwise keep the most recently tracked copy.
- Continue skipping open books and never touch untracked local files during mirror cleanup.

## Verification
- Regression coverage for `Vol. 01` to `Vol. 1`
- Regression coverage for moving subtitle text into BookOrbit’s subtitle field
- Regression coverage for tracked duplicate cleanup
- Lua and LuaJIT contract tests
- Full Lua syntax validation
- ZIP integrity and directory-layout validation for both OTA assets