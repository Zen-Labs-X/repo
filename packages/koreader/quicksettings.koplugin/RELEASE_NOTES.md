# v1.3.0

### Added
- Custom buttons: create, edit, and delete your own quick-settings buttons, with icon picker and action selector.
- Plugin icons are automatically imported into KOReader's icon folder on startup, need to restar koreader.

# v1.2.0

<html>
<body>
<!--StartFragment--><html><head></head><body><h1>Changelog</h1>
<h2>v1.2.0 - 2026-07-01</h2>
<h3>Bug Fixes</h3>
<ul>
<li><strong>Casual Chess label</strong>: The <code>casualchess</code> button was displaying <code>_("Chess")</code> instead of <code>_("Casual Chess")</code>, making it indistinguishable from the regular chess button. Fixed to show the correct label.</li>
<li><strong>Chess button removed</strong>: The <code>chess</code> button (<code>chess.koplugin</code> / internal name <code>kochess</code>) was consistently failing to appear due to a mismatch between the plugin's folder name (<code>chess.koplugin</code>) and its internal <code>name</code> field (<code>kochess</code>). After multiple fix attempts — including dual <code>hasPlugin</code> checks and a rewritten <code>hasPlugin</code> using KOReader's <code>plugins_disabled</code> list — the button was removed entirely to avoid instability. The <code>casualchess</code> button (<code>casualkochess.koplugin</code>) remains and works correctly.</li>
</ul>
<h3>Focus Mode</h3>
<ul>
<li>
<p><strong>Tab selection dialog</strong>: Added a visual tab selection dialog that opens when the Focus Mode button is clicked. Users can choose which tabs to hide before applying.</p>
</li>
<li>
<p><strong>Icons in dialog</strong>: Each tab in the selection list now shows its corresponding KOReader icon alongside the checkbox, making it easier to identify tabs visually. Icon map used:</p>

Tab | Icon
-- | --
File Browser Settings | appbar.filebrowser
Settings | appbar.settings
Tools | appbar.tools
Search | appbar.search
Main | appbar.menu
Navigation | appbar.navigation
Typesetting | appbar.typeset
Return to File Browser | appbar.filebrowser


</li>
<li>
<p><strong>Plus Menu removed</strong> from the tab list — it is not a real navigation tab.</p>
</li>
<li>
<p><strong>Main tab icon corrected</strong> from <code>home</code> to <code>appbar.menu</code>.</p>
</li>
<li>
<p><strong>Checkbox visual feedback</strong>: Clicking a checkbox now closes and rebuilds the dialog immediately, reflecting the updated state — fixing the issue where selections had no visible confirmation.</p>
</li>
<li>
<p><strong>Dialog centering</strong>: The dialog is now centered on screen using <code>CenterContainer</code>, replacing the previous <code>MovableContainer</code> that positioned it in the upper corner.</p>
</li>
<li>
<p><strong>Buttons</strong>: Dialog has two buttons — "Cancel" (closes without changes) and "Apply &amp; Restart" (saves selection and restarts KOReader). "Disable &amp; Restart" was removed; disabling Focus Mode is now done by applying with zero tabs selected.</p>
</li>
<li>
<p><strong>Focus mode state</strong>: <code>config.focus_mode</code> is automatically set to <code>false</code> when "Apply &amp; Restart" is confirmed with no tabs selected, and <code>true</code> when at least one tab is selected.</p>
</li>
<li>
<p><strong>Dynamic tab detection</strong>: Tabs installed by third-party plugins (not in the fixed list) are detected from the current <code>tab_item_table</code> at dialog open time and added to the selection list automatically.</p>
</li>
</ul></body></html><!--EndFragment-->
</body>
</html>
<img width="400" alt="FileManager_2026-07-01_194216" src="https://github.com/user-attachments/assets/56e22cb6-dd62-436c-ab23-4182ffa7c407" />



<img width="400" alt="FileManager_2026-07-01_194534" src="https://github.com/user-attachments/assets/6201a41e-0183-4324-a3fe-5495930481cc" />



<img width="400" alt="FileManager_2026-07-01_194755" src="https://github.com/user-attachments/assets/dcbaaa17-d2fb-47b9-9ad3-7b979c6454ee" />

# v1.1.0

<img width="400" alt="FileManager_2026-06-28_155701" src="https://github.com/user-attachments/assets/fd81fe93-760e-42f4-a835-bb36ac002dcd" />
# Changelog

## Version 1.1 - 2026-06-28

### New Buttons Added

Nine new optional quick-settings buttons have been added, all disabled by default and only visible when the corresponding plugin is installed:

| Button | Plugin | Detection |
|---|---|---|
| **QuickRSS** | `quickrss.koplugin` | Opens feed view directly via `modules/ui/feed_view` |
| **OPDS** | `opds.koplugin` | Broadcasts `ShowOPDSCatalog` event |
| **Puzzle** | `slidepuzzle.koplugin` | Broadcasts `SlidePuzzleOpen` event |
| **Crossword** | `crossword.koplugin` | Broadcasts `CrosswordMenu` event |
| **Connections** | `connections.koplugin` | Calls `nytconnections:addToMainMenu` callback |
| **Chess** | `chess.koplugin` | Broadcasts `KochessStart` event |
| **Casual Chess** | `casualkochess.koplugin` | Broadcasts `CasualChessStart` event |
| **KOSync** | `kosync.koplugin` | Calls sync directly via plugin instance |
| **FileBrowser+** | `filebrowserplus.koplugin` | Toggles server on/off via `ToggleFilebrowserPlusServer` event; shows active state by reading PID file |

### Removed

- Removed the built-in **Filebrowser** button (`filebrowser.koplugin`) — superseded by **FileBrowser+**.

### Icon System Overhaul

- All button icons now load from `plugins/quicksettings.koplugin/icons/` instead of KOReader's internal icon cache.
- `makeActionButton` now auto-detects the icon type: if the name contains `/` it uses `file =` (external file); otherwise falls back to `icon =` (internal cache).
- Added PNG → SVG fallback: if the `.png` file is not found, the loader automatically tries the `.svg` variant at the same path.

### Bug Fixes

- **Syntax error**: Fixed a missing closing brace `}` on the `button_defs` table that prevented the plugin from loading entirely.
- **QuickRSS**: Was incorrectly using a `broadcastEvent("ShowQuickRSS")` call that does not exist in the plugin. Now opens the feed view directly via `require("modules/ui/feed_view")`, matching what the plugin does internally.
- **Crossword**: Was calling `ui.crossword:showLibraryView()` which does not exist in `omer-faruq/crossword.koplugin`. Fixed to use the `CrosswordMenu` event registered by the plugin's Dispatcher.
- **Connections**: Plugin folder is `connections.koplugin` but internal slot name is `nytconnections`. Detection now uses `hasPlugin("connections")` (folder name) while the callback accesses `ui.nytconnections` (slot name).
- **Chess**: `hasPlugin` was looking for `kochess.koplugin` but the actual folder is `chess.koplugin`. Fixed to use `hasPlugin("chess")`.
- **FileBrowser+**: Was sending a non-existent `ShowFileBrowserPlus` event. Now uses `ToggleFilebrowserPlusServer` (the event registered by the plugin) and shows active/inactive state by checking the PID file at `/tmp/filebrowserplus_koreader.pid`.

### Internals

- **`hasPlugin` robustness**: Now tries both a relative path (`plugins/<name>.koplugin/main.lua`) and an absolute path via `DataStorage:getDataDir()`, fixing detection failures on Kindle where the working directory differs from the KOReader root.
- **Config backfill**: New button IDs are automatically added to existing saved configs on first load, so users upgrading from a previous version do not need to reset their settings.

**Full Changelog**: https://github.com/renandeivison/quicksettings/compare/v1.1.0...v1.1.0

# v1.0.0

This is the first public release of the Quick Settings Plugin for KOReader, a hybrid rework that combines two excellent community projects into a single, cohesive menu panel.

Built using AI assistance for personal use and shared by community request!
