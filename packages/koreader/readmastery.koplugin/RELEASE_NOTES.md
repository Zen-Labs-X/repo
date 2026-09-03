# v1.3.1

**v1.3.1 (2026-03-05)**

**Bug Fixes**

- Fixed ProjectTitle footer integration (#11): The previous patch-based approach for PT footer didn't work reliably because patches load before plugins, causing timing issues. Replaced with a modified covermenu_readmastery.lua that users copy directly into ProjectTitle's plugin folder. This adds ReadMastery stats directly into PT's footer rendering pipeline, ensuring it works on every page load, pagination, and folder navigation.

**Changes**

- Removed deprecated 2-projecttitle-footer-readmastery.lua patch file
- PT footer integration now uses a modified covermenu.lua approach (more reliable)
- Updated installation instructions for PT footer setup

# v1.3.0

v1.3.0 (2026-03-02)

**Bug Fixes**

- Fixed crash with CBZ/comic files (#8, #3): The plugin no longer crashes when opening CBZ or other document types that don't support getCurrentPage(). All page-related calls are now safely wrapped with error handling, enabling full tracking support for comic book archives and other formats.
- Fixed Random Page triggering multiple achievements (#5): Using the "Random Page" feature (or any large page jump via TOC, bookmarks, etc.) no longer falsely counts hundreds of pages as read. Large jumps (>5 pages) are detected and excluded from page tracking. Additionally, time-based achievements (Early Bird, Night Owl, Weekend Warrior) now only count once per day, and session achievements (Centurion, Marathon, Sprint) only trigger once per session.
- Fixed streak reset on book finish (#7): Finishing a book no longer incorrectly resets the reading streak. The streak logic now properly handles midnight crossover sessions (starting a book before midnight and finishing after) and correctly calculates missed days.
- Fixed ASCII art distortion in landscape mode (#10): Achievement and tier-up popups now use the dedicated AsciiPopup widget with monospace font rendering. The popup automatically detects screen orientation and adjusts its width (60% in landscape vs 85% in portrait) and font size to keep ASCII art properly aligned on all screen orientations.
- Fixed streak reset on orientation change (#10): Changing device orientation (portrait ↔ landscape) no longer triggers a session restart. The plugin now detects when onReaderReady is called for an already-active session on the same document and skips re-initialization.

**Improvements**

- Added safe page detection for all document types using pcall wrappers
- Achievement notifications now use the AsciiPopup widget for better rendering
- Daily deduplication for time-based achievement progress tracking
- Session-level deduplication for continuous reading achievements
- More robust streak continuation logic with freeze token awareness
- File extension parsing is now nil-safe for documents without extensions

**New Features**

- ProjectTitle Footer Support (#9): ReadMastery stats can now be displayed in the Project: Title plugin's footer bar. Includes a dedicated patch file (2-projecttitle-footer-readmastery.lua) and a new "Level + XP" display format (e.g., Lv11 XP 514/687). Configure via ReadMastery → Display → ProjectTitle Footer.

# v1.2.1

Quick fix:

Cleaned the code to remove the integration with Project:Title, work in progress this integration

# v1.2.0

# v1.2.0 - Gestures & Streak Overlay

## New Features

### Gesture Support
- Assign ReadMastery actions to any gesture
- Available actions:
  - Show Stats
  - Show Streak Info
  - Show Achievements
  - Toggle Streak Overlay
  - Quick Stats Popup

### Streak Display in Title Bar
- Modified the title bar patch to support readmastery injection of data
- Customizable text (streak, level, streak + level, full)
- Toggle via menu

## Menu Changes
- New "Display" submenu
- New Title Bar options under Display submenu
- Info about gestures

## Bug Fixes
- Fixed streak lost when reading across midnight

# v1.1.0

# v1.1.0 - Badge Tier System

## New Features
- **Badge Tiers**: All 11 achievements now have 4 tiers
  - 🥉 Bronze - First unlock
  - 🥈 Silver - Repeated accomplishment
  - 🥇 Gold - Dedicated reader
  - 💎 Platinum - Master level
- **Progress Tracking**: See your progress toward the next tier
- **Tier XP Bonuses**: Earn extra XP for tier upgrades
- **Tier Up Notifications**: Celebrate when you reach a new tier

## Bug Fixes
- Fixed: Large page jumps (random page, TOC) no longer count as read
- Fixed: Achievement view crash on some devices
- Fixed: UI layout issues on larger screens

## Improvements
- Better ASCII art centering
- Smoother data migration for existing users
