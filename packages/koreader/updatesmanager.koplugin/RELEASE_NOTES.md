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

# v1.4.10


### Fixed
- Fixed crash when updating plugins on KOReader nightly: `Device:unpackArchive` was removed upstream; plugin updates now unpack via `ffi/archiver` ([#36](https://github.com/advokatb/updatesmanager.koplugin/issues/36)).
