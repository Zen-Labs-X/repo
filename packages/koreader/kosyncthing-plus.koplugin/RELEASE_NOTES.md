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