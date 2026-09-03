# v2.0.2

# **V2.0.2**
- Completely rewritten codebase and modernized folder structure to improve maintainability and facilitate easier open-source contributions

- The issues in issues #8 and #2 were completely and finally fixed !!



The issue were causing the user installed plugins to be labeled "NEW:", while it was not a NEW plugin.
Also on some devices it caused the plugins to change it's location randomly and appear in weird places.

Special thanks to @sparklerfish for their contribution and massive help to this release.

# v2.0.1

Release Notes: Version 2.0.1 (Patch)

This minor patch addresses several quality-of-life improvements and resolves a critical file management issue reported by a community user (bosislermuduruyum).

## What's New & Improved
- Dependency Management: The core meta package version has been updated.
- Documentation Clarity: The primary README file has been revised to provide more accurate and less ambiguous information regarding installation and usage.

## Bug Fixes

- External Plugin Management: Resolved an issue where external user-installed plugins were incorrectly moved from their original locations to the MORE TOOLS directory. User plugins now remain intact in their initial directory, ensuring configuration stability and predictable file paths.

Now the plugins 
Zlibrary, Telegram Downloader, Sudoku, Web browser, RSS reader etc. Works properly.

Fixed issue #7

# v2.0.0

This update rewrites the codebase from the ground up to improve stability, modernize the user interface, and prevent system crashes.


- Implemented a profile system to save, load, and delete custom menu layouts.
- Switched UI to a native category-based view instead of the legacy flat list.
- Added search functionality to quickly find menu items.
- "Apply FM Layout" now uses smart merging to preserve Reader-specific tabs, fixing the bug where items were incorrectly labeled as "NEW".
- Introduced a global safety wrapper to catch Lua errors without crashing the application.
- Added logic to disable Reader menu customization while a book is open to prevent engine instability.
- Hardened the backend by locking critical system tabs (Navigation, Tools, Search) to prevent accidental disabling that could cause boot loops.
- Removed hardcoded lists; menus are now loaded dynamically from the system.
- Added visual checkmarks and lock indicators for better clarity.
- Added a global "Reset All" button to restore defaults.
- Removed forced reboots; the plugin now prompts for a manual restart.
- Fixed variable scoping issues in the profile naming dialog.

Fixed issues: 
https://github.com/JoeBumm/Koreader-Menu-customizer/issues/2
https://github.com/JoeBumm/Koreader-Menu-customizer/issues/5
https://github.com/JoeBumm/Koreader-Menu-customizer/issues/3

# v1.0.0

Community contributions and feedback are very welcome. If you experience crashes or instability, please refer to the installation tutorial or open an issue on GitHub — I’ll be happy to help.

 Happy reading !!
