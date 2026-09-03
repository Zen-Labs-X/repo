# v1.8.0

- KOReader's *Delete plugin and settings* / *Disable plugin and delete settings* menu entries now work for FileSync: the plugin's settings are removed along with it, and the file server is stopped cleanly before the restart. (#25)
- Stopping the file server no longer quits KOReader on Android (and macOS/SDL), where the app cannot restart itself. The screen is refreshed instead. The updater's *Restart now* button had the same problem and now asks you to reopen KOReader manually. (#34)

# v1.7.0

- File server toggle is now available as a Simple UI quick action, so the server can be started and stopped without opening the plugin menu. (#36)
- Hidden files and folders are now shown in the web UI when safe mode is off. (#32)
- Default port is now 80, so the server can be reached by typing just the device IP with no ':port' suffix. Existing users keep their saved port. (#27)
- Ports below 1024 are now accepted, with automatic fallback to 8080 when the privileged bind fails (Android/desktop, where KOReader isn't root). (#27)
- QR code screen now works on non-touch devices: The screen is fully keyboard-navigable. (#31)
- README is now more generic about supported devices. (#30)
- Synced all translation catalogs with the codebase. (#38)

# v1.6.0

- Start server flow now triggers KOReader's standard "Turn on Wi-Fi?" prompt instead of bailing with a warning when WiFi is off; server starts automatically once connected. Same flow applies to the update check. (#23)
- Web UI now opens in the KOReader home folder by default. (#22)

# v1.5.0

## What's New

### Streaming Uploads (up to 1 GB)
- File uploads now stream directly to disk in 64 KB chunks instead of loading the entire file into memory
- Upload limit raised from 50 MB to **1 GB** -- supports large comic compilations, graphic novels, and PDF collections
- Memory usage during uploads stays constant (~128 KB) regardless of file size
- Client-side file size validation with instant feedback before upload begins
- Warning toast for files over 100 MB about potential UI slowdown

### Code Quality & Maintainability
- Extracted shared json.lua module -- eliminated ~300 lines of duplicated JSON parser code
- Extracted shared utils.lua module -- consolidated plugin directory resolution and shell escaping across 5 files
- Extracted mobi.lua module -- MOBI/AZW3 binary parser moved out of fileops.lua (~300 lines)
- Consolidated EPUB OPF parsing into a single helper, eliminating ~120 lines of duplication
- Removed dead code: qrcode.lua (145 lines, never used), unused _httpsRequest function

### Security & Robustness
- Added HTTP request body size limit (1 MB for API calls) with 413 response
- Added HTTP header count limit (100 max) to prevent resource exhaustion
- Fixed nil-safety crash in QR code icon path resolution
- Added pcall protection for lfs.dir in recursive delete
- Check f:write() return value on uploads -- partial files are now cleaned up on disk-full errors
- Added tonumber guard on port before iptables commands (Kindle)
- Check backup move return value before plugin update install

### UI Responsiveness
- E-reader UI stays responsive during large uploads and downloads (yields to UIManager every ~2 MB)
- Reduced HTTP connection timeout from 5s to 2s with 3s per-poll-cycle time budget
- Forced garbage collection after large uploads to prevent memory pressure on directory reload

### Testing
- Added busted test framework with **195 unit tests**
- Test coverage for JSON encode/decode, path validation, filename validation, version parsing, URL decoding, query parsing, boundary extraction, and upload filename handling
- Added constructors to FileOps and FileSyncManager for testability
- Decoupled FileOps from HTTP transport layer

### Documentation & i18n
- Added "Running Tests" section to Contributing guide in all 10 languages
- Added large file upload warning to troubleshooting in all 10 languages
- Added module-level documentation and @param/@return annotations throughout
- New web UI toast strings translated in all 10 .po files
- Updated directory tree in all READMEs to reflect new module structure

# v1.4.0

## What's New

- Add 6 new language translations: Arabic, Hindi, Japanese, Korean, Russian, and Turkish (#21)
- Modularize monolithic web UI and unify i18n with .po files (#20)

**Full Changelog**: https://github.com/abrahamnm/filesync.koplugin/compare/v1.3.1...v1.4.0

### Contributions
- @abrahamnm: New language translations and web UI modularization.
