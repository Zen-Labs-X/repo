# v1.9.2


- Other issue identified in issue #77 - the old restore where you left off code assumed there were only two options - in the reader or in the filebrowser. But with the use of new plugins to override the filebrowser (simpleui, etc.) that is no longer the fallback if not in reader. Fixed.

# v1.9.1


- Issue identified in #77 - old plugin schema wasn't migrating correctly resulting in plugin lists being reset and never unset.

# v1.9.0


### Added 🚀

- Broke builtin and user added plugins into separate spaces (#64)
- Added `About` box, as well as more information for use when submitting bug reports

### Housekeeping 🏠

- Heavy initial refactor, breaking the monolithic lua file into components
- Moved all settings management that is AirPlaneMode specific to the AirPlaneMode config file
- Added a hook for `stopPlugin` calls (#68)
- Added a hook to delete configs when being disabled by KOReader the plugin manager (#65)
- Improved linting and tests for pre-release checks

### Experimental 💣

- Developer mode added - disable/enable features that are still in progress
- Debug logging - enables/disables debug logging, only available when devmode is on
- Update manager - now you can update AirPlaneMode from directly inside the plugin (#71). Currently gated with dev mode

# v1.2.2

## Version v1.2.2

See [CHANGELOG.md](CHANGELOG.md) for details.

# v1.2.1

## Version v1.2.1

See [CHANGELOG.md](CHANGELOG.md) for details.
