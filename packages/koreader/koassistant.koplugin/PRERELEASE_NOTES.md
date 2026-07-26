## v0.8.1-beta

New features added to extended thinking and streaming. 

### Bug Fixes
- Fixed model constraints not being applied for Anthropic (undefined variable)
- Fixed per-action reasoning config not being used when set in action editor
- Fixed model capability matching for versioned model names (e.g., claude-sonnet-4-5)
- Fixed reasoning indicator appearing in debug mode when setting was disabled
- Fixed Gemini thinking API format (now uses correct camelCase REST format)

### Improvements
- Simplified streaming reasoning display for better e-ink compatibility
- OpenAI reasoning models now show indicator with effort level (e.g., "Reasoning requested (medium)")
- Debug info stored per-message - shows config that was actually used, not current settings

### Code Quality
- Removed duplicate request body building code in API handlers
- Centralized reasoning default values
- Consolidated duplicate UI helper functions


**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.8.0...v.0.8.1-beta