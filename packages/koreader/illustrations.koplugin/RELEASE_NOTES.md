## Critical Memory Leak & Disable Fixes


### Fixed
- **Critical Memory Leak**: Fixed an issue where images were not properly released from memory during pagination and gallery viewing, causing "high memory usage" warnings and crashes on low-RAM devices.
- **Plugin Management**: Fixed a bug where the plugin could not be disabled in KOReader settings (KOReader would restart but the plugin would remain enabled) due to an ID casing mismatch.
