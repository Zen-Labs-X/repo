# v1.6.0


### Added
- Optional background check for **installed plugins** only (off by default). Runs on File Manager resume / Wi-Fi already connected, at most every 12 or 24 hours. Does not scan patches, does not turn Wi-Fi on, and yields between GitHub requests so the UI stays usable. A dialog offers **View** (existing update list) or **Later** (snooze until the next interval).

### Fixed
- Background prompt no longer snoozes if it never appeared: `last_check` is written only after the dialog is shown (or when GitHub answered and there are no updates). Failed/rate-limited runs retry. Enabling the setting clears the snooze. The dialog waits until the Tools menu is closed so it is not buried.
- Background update prompt is no longer dismissed by a tap outside it or by a leftover tap after the Tools menu closes. Close it with **View** or **Later**.

# v1.5.1


### Added
- Added charart.koplugin to repositories list

# v1.5.0


### Added
- Runtime localization from `locale/<lang>.po` (no `.mo` compilation). To add a language, copy `locale/updatesmanager.pot` to `locale/<lang>.po` and fill in `msgstr`.
- Translations: Hungarian, Polish, Russian, Turkish, Ukrainian.

### Changed
- Flattened the Tools menu: **Check for Updates** (patches + plugins) and a single **Force Refresh** are on the first level. Separate Patches/Plugins submenus, Installed lists, and Clear Cache were removed.

### Fixed
- Crash on **Check for Updates**: `loadIgnoredPatches` was a `local function` defined after `checkForUpdates`, so Lua looked up a nil global.

# v1.4.12


### Added
- Added new patch and plugin repositories

# v1.4.11


### Added
- Added new patch and plugin repositories
