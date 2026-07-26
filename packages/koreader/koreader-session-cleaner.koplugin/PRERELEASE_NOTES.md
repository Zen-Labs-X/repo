Session Cleaner v2.0.0-beta1

This is the first frozen beta of the new v2 line.

Session Cleaner is a standalone KOReader plugin for browsing books with reading statistics, reconstructing sessions from raw page_stat_data rows, filtering suspicious sessions, inspecting exact raw rows, and deleting the real underlying rows from statistics.sqlite3 safely, with backup support.

What is included in this beta

- Stabilized v2 browser structure
- Grouped book cards with unified press feedback
- Atomic book-card pagination
- Cleaner book view hierarchy
- Live settings visibility in Book view and Session view
- Additional UI scale preset: Very Large
- Preserved trusted engine for DB access, session reconstruction, backup creation, and safe deletion

Important

This is a beta release of the v2 branch.
The stable v1 line remains separate.
This beta is intended for real-world testing on different KOReader devices and screen sizes.

Please report

- screenshots
- device model
- UI scale used
- what you were doing when the issue appeared

Especially useful:
- layout issues on different screens
- pagination/card-splitting problems
- navigation regressions
- delete/backup workflow issues

Current status

This build is the frozen v2.0.0-beta1 baseline and will only receive targeted fixes or polish before a final v2.0.0 release.