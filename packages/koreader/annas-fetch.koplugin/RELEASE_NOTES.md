# v1.1.0

## v1.1.0

### New Features
- **Custom Mirror URL**: Set a specific Anna's Archive domain/mirror from Settings -> e-reading -> Anna's Archive, useful for regions where the default domain is blocked

### Security
- Fixed shell injection vulnerabilities in scraper and OTA modules (proper shell_quote for all shell commands)
- Domain cache moved to KOReader's data directory instead of plugin install path

### Bug Fixes
- Restored reliable book metadata extraction (title, author, format, description) with proper CSS-class selectors
- Fixed cache directory creation (broken mkdir quote character)
- Fixed blank widget when refreshing mirror list - now shows a simple info message
- Fixed dead src/update.lua import in OTA module

### Cleanup
- Plugin display name changed to **Annas Fetch** throughout the UI
- All debug print() calls replaced with proper logger calls
- Removed commented-out dead code from OTA module

# v1.0.0
