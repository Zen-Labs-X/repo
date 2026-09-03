# v1.4.0


### Added
- Optional toast notifications for streak achievements (Settings → Tracking → **Use toast notifications**). When enabled, notifications appear at the top of the screen and dismiss automatically instead of requiring a tap ([#9](https://github.com/advokatb/readingstreak.koplugin/issues/9)).

### Changed
- Removed dead code and unused translations left over from the old modal settings dialog.
- Translations load directly from `locale/*.po` at runtime — no `.mo` compilation required. Ukrainian locale code is now `uk`.

### Fixed
- Skip Project Title footer integration when Project Title is missing, so uninstalling or renaming it no longer crash-loops KOReader ([#14](https://github.com/advokatb/readingstreak.koplugin/issues/14)).

# v1.3.7


### Fixed
- Fixed reading time continuing to run when the device was suspended (thanks to @jandamm, #17).

# v1.3.6


### Added
- Added KOReader uninstall hook `deletePluginSettings()` to remove plugin settings when users check **"Also delete plugin settings"** in plugin management ([#15](https://github.com/advokatb/readingstreak.koplugin/issues/15)).

# v1.3.5


### Fixed
- Improve dateDiffDays function to use Julian day calculation

# v1.3.4


### Fixed
- Fixed day-to-day streak calculation around daylight saving time transitions by using a DST-safe day difference method.
