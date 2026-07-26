**v1.3.1 (2026-03-05)**

**Bug Fixes**

- Fixed ProjectTitle footer integration (#11): The previous patch-based approach for PT footer didn't work reliably because patches load before plugins, causing timing issues. Replaced with a modified covermenu_readmastery.lua that users copy directly into ProjectTitle's plugin folder. This adds ReadMastery stats directly into PT's footer rendering pipeline, ensuring it works on every page load, pagination, and folder navigation.

**Changes**

- Removed deprecated 2-projecttitle-footer-readmastery.lua patch file
- PT footer integration now uses a modified covermenu.lua approach (more reliable)
- Updated installation instructions for PT footer setup