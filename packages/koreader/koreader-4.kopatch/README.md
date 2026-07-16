# patchs-plugins-for-koreader

# KOReader Screensaver - Kobo Style

A highly customizable Lua patch for KOReader that replaces the default screensaver with a modern, Kobo-inspired design. It displays rich book information, reading statistics, and random highlights from your current book.

**[Download the Patch (2-kobo-style-screensaver.lua)](https://github.com/PedroMachado1/patches-plugins-for-koreader/blob/e5501edb17c2115425ae12c51ab466286f18d69f/2-kobo-style-screensaver.lua)**

<p align="center">
  <img src="./images/IMG_20260128_163932674.jpg" width="60%" alt="Kobo Style Screensaver Preview">
</p>

## ✨ Features

### Visual Design
*   **Modern Aesthetics**: Clean typography and spacing inspired by the native Kobo UI.
*   **Rounded Corners**: Configurable `Border Radius` for info boxes (0px to 50px).
*   **Dark Mode**: Full support for night mode/inverted screens.
*   **UI Scaling**: Global scale setting to adjust perfectly to any screen DPI (Kobo, Kindle).

### Information Display
*   **Book Details**: Displays the current Book Title and Chapter Name.
*   **Reading Statistics**:
    *   Percentage read.
    *   Time left in book (based on reading speed).
    *   Time read today.
    *   Current page / Total pages.
*   **Book Cover**: Option to display the current book's cover as the background.

### 💬 Random Quotes Feature
Automatically fetches and displays a random quote from your book's annotations on the screensaver.
*   **Smart Layout**: Quotes are displayed in a separate, elegant box below the main info.
*   **Long Text Support**: Automatic word-wrapping handles long paragraphs perfectly without cutting off text.
*   **Source Filtering**: Choose to display quotes from **Highlights**, **Bookmarks**, or both.
*   **Metadata**: Displays the chapter and page number of the quote.

### ⚙️ Customization Menu
A dedicated "Kobo Style" menu is added to your KOReader Screensaver settings, allowing you to tweak everything:
*   **Toggle Elements**: Show/Hide any element (Title, Chapter, Progress, Time Left, etc.).
*   **Font Sizes**: Adjust the size of Titles, Chapter text, Status info, and Quotes independently.
*   **Text Limits**: Configure maximum character counts for titles and quotes.
*   **Language**: Support for English (default) and Portuguese.

## 🚀 How to Install

1.  Download the `2-kobo-style-screensaver.lua` file from the link above.
2.  Navigate to the KOReader directory on your device: `koreader/patches/` (create the `patches` folder if it doesn't exist).
3.  Copy the lua file into the `patches` folder.
4.  Go to **Settings** (Gear icon) -> **Screen** -> **Screensaver/Sleep Screen** -> **Wallpaper** -> **Kobo Style (cover + progress) or Estilo Kobo (capa + progresso)**.

## 🛠️ Configuration
After installation, you can customize the look and feel by going to:
`Settings (Gear icon) -> Screen -> Screensaver/Sleep Screen -> Wallpaper -> Kobo Style (cover + progress) or Estilo Kobo (capa + progresso)`

Enjoy your beautiful new screensaver!

---

# KOReader Custom Bottom Navigation Bar

A fork of [qewer33/koreader-patches](https://github.com/qewer33/koreader-patches) that adds a fully customizable tab bar at the bottom of the KOReader File Manager, with added support for **Z-Library**, **Anna's Archive**, **AppStore**, **OPDS** and **custom tabs** powered by any installed plugin.

**[Download the Patch (2-custom-navbar.lua)](https://github.com/PedroMachado1/patches-plugins-for-koreader/blob/main/2-custom-navbar.lua)**

<p align="center">
  <img src="./images/FileManager_2026-03-08_123608.png" width="60%" alt="Custom Navigation Bar Preview">
</p>

## ✨ Features

- **Tab Bar**: Adds a bottom navigation bar to the File Manager with icons and labels.
- **Configurable Tabs**: Show or hide any tab individually via the settings menu.
- **Tab Order**: Reorder tabs to your preference.
- **Active Tab Styling**: Highlights the active tab with bold text, underline, and optional color.
- **Color Support**: Full RGB color support for active tab indicators on color screens.
- **Custom Tabs**: Create your own tabs linked to any action or plugin method installed on your device.

## 📑 Available Tabs

| Tab | Description |
|---|---|
| **Books** | Navigate to your home/books folder |
| **Manga** | Open Rakuyomi plugin or a custom folder |
| **News** | Open QuickRSS plugin or a custom folder |
| **Continue** | Reopen the last read book |
| **History** | Open reading history |
| **Favorites** | Open favorites list |
| **Collections** | Open collections list |
| **Z-Lib** | Open the Z-Library plugin *(requires zlibrary.koplugin)* |
| **Anna's** | Open the Anna's Archive plugin *(requires annas.koplugin)* |
| **AppStore** | Open the AppStore plugin *(requires appstore.koplugin)* |
| **OPDS** | Browse your OPDS catalogs *(requires opds.koplugin, enabled by default in KOReader)* |
| **Exit** | Close KOReader |

## 🚀 How to Install

1. Download the `2-custom-navbar.lua` file from the link above.
2. Download the [icons for Navbar](https://github.com/PedroMachado1/Koreader.patches/blob/main/icons%20for%20NavBar.zip) file from the repository and extract the icons into `koreader/icons/`.
3. Navigate to the KOReader directory on your device: `koreader/patches/` (create the `patches` folder if it doesn't exist).
4. Copy the lua file into the `patches` folder.
5. Restart KOReader.

## ⚙️ Configuration

After installation, access the settings via the **≡ (hamburger) menu** in the File Manager:

`File Manager Menu → Navbar settings`

From there you can toggle individual tabs on/off, change the active tab color, toggle labels, and more.

## 🔌 Plugin Tabs (Z-Lib, Anna's Archive, AppStore & OPDS)

These tabs are disabled by default. To enable them:

1. Make sure the corresponding plugin is installed in your `koreader/plugins/` directory.
2. Go to `File Manager Menu → Navbar settings → Tabs`.
3. Enable the desired toggle.

| Tab | Plugin required |
|---|---|
| Z-Lib | `zlibrary.koplugin` |
| Anna's | `annas.koplugin` |
| AppStore | `appstore.koplugin` |
| OPDS | `opds.koplugin` *(ships with KOReader, just needs to be enabled)* |

> These tabs were added in this fork and are not present in the original patch.

### 📚 OPDS Tab behavior

When you tap the OPDS tab:

- **No catalogs configured** — opens the catalog browser so you can add your first server.
- **One catalog** — opens it directly, no extra tap needed.
- **Two or more catalogs** — shows a quick picker with all your saved catalogs, plus an "All catalogs" option at the bottom.

<p align="center">
  <img src="./images/IMG_20260308_123659736.jpg" width="60%" alt="OPDS catalog picker">
</p>

Your OPDS catalogs are managed inside the native OPDS plugin (`File Manager Menu → Search → OPDS catalog`). Any catalog you add or remove there is automatically reflected in the tab picker.

## ➕ Custom Tabs

You can create your own tabs linked to any action or plugin installed on your device. This is useful for plugins not covered by the built-in tabs, such as a personal Calibre server, a custom script, or any community plugin.

### How to add a custom tab

1. Go to `File Manager Menu → Navbar settings → Custom tabs`.
2. Tap **+ Add custom tab**.
3. Browse the list of available actions. It has two sources:
   - **Native KOReader actions** registered in the Dispatcher (adjust brightness, open history, etc.).
   - **Plugin methods** auto-discovered from all plugins currently loaded in the File Manager — listed as `pluginName → methodName`.
4. Choose the action, then pick an icon.
5. Give the tab a label and tap **Add tab**.
6. Go back to `Navbar settings` and tap **Refresh navbar** to apply.

### Managing custom tabs

In `Navbar settings → Custom tabs`, each existing custom tab has two interactions:

- **Tap** — toggle the tab on/off without removing it.
- **Hold** — shows a confirmation dialog to permanently delete the tab.

> Custom tabs added in this fork are saved in KOReader's settings file and persist across restarts.
> 
