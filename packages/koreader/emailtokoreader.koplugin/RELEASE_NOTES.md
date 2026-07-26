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