# v1.2.2

## What's Changed
* fix: use POSIX arithmetic in start-syncthing by @Philantrop in https://github.com/d0nizam/kosyncthing_plus.koplugin/pull/8

## New Contributors
* @Philantrop made their first contribution in https://github.com/d0nizam/kosyncthing_plus.koplugin/pull/8

**Full Changelog**: https://github.com/d0nizam/kosyncthing_plus.koplugin/compare/v1.2.1...v1.2.2

# v1.2.1

## [v1.2.1] — 2026-07-23

### Fixed
- **Downloading the legacy binary could fail with "did not contain a valid Linux
  Syncthing binary".** A release archive holds three entries named `syncthing`,
  and the plugin picked whichever the filesystem happened to list first —
  sometimes one of the two helper scripts, which was then correctly rejected as
  not an executable. The legacy download was affected on every device; the
  ordinary binary update only when it fell back from system `tar`. The
  executable is now selected by its path inside the archive and extracted on its
  own. Verified against the v1.2.2, v1.27.12 and v2.x archives.
- **The old-kernel notice reappeared on almost every wake.** The hint pointing
  at Legacy mode was meant to show once, but nothing recorded that it had been
  shown, and `init()` runs on every plugin instantiation — each FileManager to
  Reader transition, and after resume. On an old-kernel device it therefore
  returned indefinitely, and being a delayed pop-up it landed on top of whatever
  was drawing at the time, including lock-screen plugins. It is now shown at
  most once, recorded only when it is actually displayed, and cleared by a
  factory reset. The standing information stays in the menu, which marks
  *Legacy Syncthing* whenever the kernel needs it.

### Changed
- Binary extraction now also falls back to system `tar` if `ffi/archiver` is
  unavailable, which keeps the legacy download working on older KOReader builds
  — the devices most likely to need it.
- Extraction failures now report the underlying reason, so a failed download can
  be diagnosed from the message instead of guessed at.

## What's Changed
* Enhance binary extraction by @d0nizam in https://github.com/d0nizam/kosyncthing_plus.koplugin/pull/6


**Full Changelog**: https://github.com/d0nizam/kosyncthing_plus.koplugin/compare/v1.2.0...v1.2.1

# v1.2.0

## [v1.2.0] — 2026-07-18

### Fixed
- KOReader commit 751b497 removed `Device:unpackArchive`, breaking plugin and binary updates on newer KOReader builds. Added `U.unpackArchive` with a direct `ffi/archiver` fallback so updates work on all KOReader versions.

**Full Changelog**: https://github.com/d0nizam/kosyncthing_plus.koplugin/compare/v1.1.9...v1.2.0

# v1.1.9

## [v1.1.9] — 2026-06-21

### Fixed
- **A successful pairing no longer shows a warning icon.** After accepting a
  pairing request in the wizard, the "Paired with … successfully" message was
  displayed with a ⚠ warning icon instead of the neutral info icon, making a
  success look like something had gone wrong. The icon now matches the outcome.
  (The failure message is unchanged - it still shows the warning icon.)

### Added
- **Windows test setup.** A one-command `spec/setup_windows.ps1` (installs
  MinGW-w64, LuaRocks and `luafilesystem`, then runs the suite) plus Windows
  path/command shims in `spec/run_tests.lua`, so the full 506-test suite runs
  on Windows as well as Linux/WSL. Dev tooling only - not part of the shipped
  plugin.

### Changed
- **The LICENSE is now bundled with the installed plugin.** It was previously
  excluded from the install package; it now ships alongside the runtime files.
- **Dropped the deprecated `name` field from `_meta.lua`.** KOReader derives the
  plugin name from its directory and logs a deprecation warning for a `name`
  key in `_meta.lua`; removing it silences that warning with no change to the
  plugin's identity.

# v1.1.8

## [v1.1.8] — 2026-06-15

### Fixed
- **"No devices online" while devices were actually connected.** The
  device-online count shown in the header and in *Status & conflicts* treated
  Syncthing's `isLocal` connection flag as "this entry is the local device" and
  excluded it. But `isLocal` actually marks a connection made over the **local
  network (LAN)** — so every peer on the same Wi-Fi was excluded, and the count
  read "no devices online" even though the device list showed them all
  connected. (A peer reached over the internet/relay reports `isLocal=false`, so
  it *was* counted — meaning the same device dropped in and out of the count as
  it moved between a LAN and a global connection.) The local device is now
  identified by its device ID only, so LAN and global peers are both counted.
- **The error header now takes you straight to the problem.** Tapping the
  "⚠ Error in N folders" header used to open *Status & conflicts* rendered as a
  bare list without the normal nested navigation. It now opens the erroring
  folder's dialog directly — or, when several folders have errors, a short list
  of just those folders — mirroring how tapping a conflict opens its resolver.

### Added
- **"Explain the error" button on folder errors.** When a folder has a
  non-transient error, its dialog now offers a plain-language explanation of
  what happened, why, and what to do, tailored to the kind of error: a remote
  deletion blocked by ignored files, out of disk space, no write permission, a
  missing path or `.stfolder` marker, or a generic fallback. The original
  Syncthing message is included. For the ignored-files case it points to
  deleting the folder from a file manager (warning that the files inside go
  too) and clarifies that *Remove folder* only stops tracking without deleting.

### Changed
- **Android: the plugin-update item is now labelled "Check for updates"** rather
  than "Check for plugin updates". Remote mode has no plugin-managed Syncthing
  binary, so there is nothing to disambiguate from. Kindle/Kobo keep "Check for
  plugin updates" (it sits next to the binary updater).
- **The device-connection count refreshes immediately after a sync,** so a peer
  that connected or dropped during the sync is reflected without waiting for the
  short connection cache to expire.
