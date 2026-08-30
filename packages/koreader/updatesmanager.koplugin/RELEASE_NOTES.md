
### Added
- Runtime localization from `locale/<lang>.po` (no `.mo` compilation). To add a language, copy `locale/updatesmanager.pot` to `locale/<lang>.po` and fill in `msgstr`.
- Translations: Hungarian, Polish, Russian, Turkish, Ukrainian.

### Changed
- Flattened the Tools menu: **Check for Updates** (patches + plugins) and a single **Force Refresh** are on the first level. Separate Patches/Plugins submenus, Installed lists, and Clear Cache were removed.

### Fixed
- Crash on **Check for Updates**: `loadIgnoredPatches` was a `local function` defined after `checkForUpdates`, so Lua looked up a nil global.