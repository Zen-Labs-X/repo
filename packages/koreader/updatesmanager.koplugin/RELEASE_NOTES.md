
### Fixed
- Fixed crash when updating plugins on KOReader nightly: `Device:unpackArchive` was removed upstream; plugin updates now unpack via `ffi/archiver` ([#36](https://github.com/advokatb/updatesmanager.koplugin/issues/36)).