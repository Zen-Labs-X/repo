# v1.1.1

## Email to KOReader v1.1.1

### Fixes
- Added version field to manifest.lua for KOReader Updates Manager compatibility
- Improved fallback path logic using a cleaner preference chain
- Fixed crash in Settings dialog caused by calling MultiInputDialog:getFields() on the class instead of the instance (now uses settings_dialog:getFields())
- Fixed issue where settings sometimes did not save due to incorrect field retrieval
- Improved reliability of download path validation with clearer logging
- General stability improvements for saving configuration and writing files

### Improvements
- Removed unnecessary pcall() wrappers for modules always available in KOReader
- Cleaner and more consistent fallback path assignment
- Improved settings persistence code
- Minor code cleanup, formatting fixes, and internal optimizations

# v1.1.0

## Email to KOReader v1.1.0

### New
- Cyrillic and Unicode filename support (RFC 2047/2231 decoding)
- Automatic Cyrillic→Latin transliteration for filename compatibility
- Smart fallback path (user home → KOReader home directory)
- "View Download Path" menu item

### Fixes
- Write error handling and detailed error messages
- Directory creation on-demand
- Path validation improvements

### Improvements
- Multi-line email header support
- Enhanced logging and user notifications

# v1.0.0

### Initial release with:

- IMAP email integration
- Multi-file download support
- Large file handling (up to 3.5MB)
- In-app configuration
- Debug mode
- Auto-refresh file browser
- Gmail app password support
