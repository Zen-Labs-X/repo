> "Just as a gnomish-forged Gwyhyr blade hones the edge of a witcher’s craft with razor-sharp precision, this update sharpens the connection between your library and your digital archives."

Welcome to the **v0.2.0 "Gwyhyr"** release. While Alzur gave us life, Gwyhyr brings the refinement. This version focuses on precision—sharpening the sync logic, expanding the metadata gathered from your tomes, and smoothing out the user interface.

### ⚠️ Important: Action Required
To upgrade to Gwyhyr, you must perform a small ritual in your **Notion Database**:
* Change the **Type** of the `Last Sync` column from **Date** to **Text**. 
* *Why?* Notion’s date precision is limited to the minute; switching to text allows us to track your syncs with the second accuracy required for a flawless experience.

### ⚔️ New Features

- **The Great Archive Sync:** A new feature to sync all highlights from every book in your KOReader history at once. Perfect for those moving their entire library to Notion for the first time.
- **Expanded Tome Metadata:** Your Notion entries are now richer. Thanks to @johnbarraza, the plugin now populates columns for **Author, Reading Progress, ISBN, and Total Pages**.
- **Automatic Connection:** No more manual toggling. The plugin will now automatically enable Wi-Fi if it detects it is disabled when you initiate a sync.

### 🛡️ Refinements & Fixes

- **Honed Sync Logic:** Fixed a bug where the last highlight would unnecessarily update even when no changes were detected. Your sync is now as efficient as a silver blade.
- **Menu Polishing:** Refined the NotionSync menus within KOReader for a more intuitive navigation experience.
- **Improved Tracking:** Internal architectural changes to how sync times are recorded (the move to Text format) ensure no quote is ever left behind.

### 📦 Installation & Update

1. Download `notionsync.koplugin.zip` from the Assets section below.
2. Connect your device and extract the zip into the `koreader/plugins/` directory, overwriting existing files.
3. **Remember to update your Notion column type (Date → Text) before your first sync!**
4. Restart KOReader.

**Full Changelog**: https://github.com/CezaryPukownik/koreader-notion-sync/commits/v0.2.0