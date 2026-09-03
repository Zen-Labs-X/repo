# v0.9.5

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

# v0.9.4

## v0.9.4

### Fixed

- Hardened platform-aware network recovery and local IP detection.
- Added safer Kindle firewall chain management with verified cleanup.

Build channel: stable
Build ID: stable
Commit: 7b8bf97824f46357a485cb432777507f2db49c3d

# v0.9.3

## v0.9.3

### Fixed

- Reduced unnecessary note polling during connection failures and paused
  retries when the web interface is hidden.
- Limited manual session recovery after standby to short sleeps while keeping
  autostart recovery available.
- Added global HTTP error handling and safer automatic note-sync retries with
  stale-response protection.

Build channel: stable
Build ID: stable
Commit: 6cdc3f00e2602d47d277affe86068ea3dfaec124

# v0.9.2

## v0.9.2

### Added

- Added Stable and Beta update channels with a persistent channel selection.
- Added build metadata containing channel, release version, build ID, and
  commit identity to every packaged plugin.
- Added Beta prerelease packaging from the `dev` branch with checksum-verified
  ZIP artifacts.

### Changed

- The updater now displays and validates the selected channel and exact build
  identity before installation.
- Plugin status and the local API now expose the installed build identity.

Build channel: stable
Build ID: stable
Commit: d6e728c5c262131a6281417a9bbb5e11ddedc17e

# v0.9.1

## v0.9.1

### Changed

- Removed automatic OLED inactivity dimming; OLED mode now stays at its normal
  brightness until the user changes or disables it.
