# 0.7.2

Refactor HighlightSync logic for better performance

# 0.7.1

- Update user notifications for clarity during sync and document reload.
- Ensure 'silent' mode properly don't suppresses UI messages during auto-sync.

# 0.7

This release introduces automatic synchronization and major stability improvements.

✨ Automatic Synchronization: Implemented full support for automatic syncing. Highlights can now be synced automatically when opening, closing, or resuming a book (configurable in settings).

✨ Gesture Support: Added the SyncBookHighlights action to the Dispatcher. You can now assign gestures (swipes/taps) to trigger a sync manually.

🛡️ Filename Sanitization: Fixed a critical issue where filenames containing special characters (like $) caused sync failures.

📂 Smart Sidecar Location: The plugin now respects KOReader's global metadata settings, supporting both local and Hash-based storage directories.

# 0.6

🛠️ Bug Fixes
Fixed Cross-Device Sync Duplication: Addressed an issue where syncing between devices (e.g., Kindle and Android) caused duplicate highlights due to differing page numbers. The sync logic now uses stable XPath positions as the unique identifier, ensuring highlights are correctly merged regardless of font size or screen layout.

Resolved Multi-Page PDF Crash: Fixed a crash that occurred when loading highlights spanning multiple pages in PDF documents. This was caused by an issue with JSON serialization of the ext table; keys are now correctly stringified to ensure data integrity and stability.

📦 Update Manager Support
OTA Updates Integration: The plugin is now compatible with KOReader's native Update Manager. This allows for easier updates directly within the device.

# 0.5

Previously, the plugin was incorrectly using the settings key from the KOReader "Statistics" plugin (statistics) to store its sync configuration.

This commit fixes that by introducing a dedicated settings key (highlight_sync_settings) specifically for the Highlight Sync plugin. This avoids potential conflicts or data overwriting, and keeps plugin settings properly separated.

Users' existing configurations will now be stored and loaded independently, improving stability and maintainability.
