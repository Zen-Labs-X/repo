## v0.9.5

### Added

- Split the plugin runtime into focused `http`, `network`, `menu`,
  `interaction`, and `updater` modules.
- Added idle-timeout shutdown handling in the server and exposed
  `idle_timeout_seconds_remaining` to the web UI.
- Added a persistent Idle Stop card in the web UI with a short explanation,
  live countdown, and info icon.
- Added diagnostic logging/export plumbing in the runtime.
- Added a temporary `30 seconds` test value via the legacy `0.5` minute
  setting.

### Changed

- Moved `Idle stop` from the KOReader plugin menu into the web UI and made it
  persistent.
- Moved `Full screen refresh` above `Idle stop` in Device settings.
- Simplified the Device settings help text.
- Reworked Idle Stop to use the visible minute choices `2`, `5`, `10`, and
  `30`.
- Removed the `Session log` panel from the web UI.
- Prevented passive web polling from keeping the server awake.
- Kept the `Test connection` menu entry for now.

### Fixed

- Idle Stop now stops the server even when Auto-start is enabled; Auto-start
  only resumes after standby/resume.
- Idle Stop now resets only on real page-turn and control actions.
- Legacy `0.5` minute values remain compatible for saved settings.
- Hardened the release workflow markers for the new device-settings layout.

Build channel: stable
Build ID: stable
Commit: 946545f4c3474d26247409c56c65c7ece64facdc
