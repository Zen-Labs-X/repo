## Modifications via PR 16,17,20 by [iav](https://github.com/iav)
### Browser & installed-list navigation improvements

- Added pagination to the Installed Plugins and Installed Patches screens, with a configurable items-per-page setting.
- Added a compact toolbar (Switch tab / Refresh / Installed) to the plugin and patch browser.
- Added an installed checkmark next to plugins you already have in the browse list.
- Added a direct switch between Installed Plugins and Installed Patches without returning to the browser.
- Added hardware-keyboard shortcuts (R/F/S/T) and a Menu-key shortcut for refresh, filter, sort, and switch-tab actions.
- Cursor position and sort/filter selection are now preserved across page flips and list rebuilds on keyboard/D-pad devices.
- Fixed stale/ghosted screen content when switching between AppStore dialogs on e-ink screens.
- Reduced screen flashing when simply flipping pages, keeping the full-screen flash only for tab/filter/sort changes.

### Install message fix

- Fixed install/update success messages sometimes showing "nil" instead of the plugin's name.

### Update detection fix

- Fixed plugins with a "v"-prefixed version number (e.g. v1.4.2) being incorrectly flagged as needing an update.