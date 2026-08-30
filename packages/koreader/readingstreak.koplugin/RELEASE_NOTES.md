
### Added
- Optional toast notifications for streak achievements (Settings → Tracking → **Use toast notifications**). When enabled, notifications appear at the top of the screen and dismiss automatically instead of requiring a tap ([#9](https://github.com/advokatb/readingstreak.koplugin/issues/9)).

### Changed
- Removed dead code and unused translations left over from the old modal settings dialog.
- Translations load directly from `locale/*.po` at runtime — no `.mo` compilation required. Ukrainian locale code is now `uk`.

### Fixed
- Skip Project Title footer integration when Project Title is missing, so uninstalling or renaming it no longer crash-loops KOReader ([#14](https://github.com/advokatb/readingstreak.koplugin/issues/14)).