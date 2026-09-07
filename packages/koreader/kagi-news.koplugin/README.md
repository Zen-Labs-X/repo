# Kagi News for KOReader

A [KOReader](https://github.com/koreader/koreader) plugin that brings curated news from [Kagi Kite](https://kite.kagi.com/) to your e-ink device. Browse 100+ news categories, read AI-summarized article clusters with multiple perspectives, and view images — all optimized for e-ink displays.

**No API key required.** Kagi Kite is a free, public news API.

## Features

- 📂 **100+ Categories** — World, Tech, Science, Sports, Business, and many more
- 📰 **AI Summaries** — Detailed clusters with key points, perspectives, and quotes
- 🖼 **In-line Images** — Rich HTML rendering with article images embedded directly in the text via MuPDF
- 💾 **Organized Offline Cache** — Structured storage (`meta/`, `articles/`, `images/`) with MD5 hashing for safety
- ⚡ **Step-wise Sync** — Download categories first, select what to follow, then bulk sync
- 🔄 **Bulk Synchronization** — Download text and images for all followed categories with a single tap and `Trapper` progress UI
- 📱 **E-ink Optimized** — Hardware screen refresh, offline-first architecture, paginated menus, and neutral grayscale UI

## Screenshots

![Screenshot 1](img/screenshot-1.png)
![Screenshot 2](img/screenshot-2.png)
![Screenshot 3](img/screenshot-3.png)
![Screenshot 4](img/screenshot-4.png)
![Screenshot 5](img/screenshot-5.png)

## Installation

### From Source

1. Clone or download this repository
2. Copy the `kagi-news.koplugin` folder to your KOReader plugins directory:

   ```bash
   # Linux / macOS (AppImage or installed)
   cp -r kagi-news.koplugin ~/.config/koreader/plugins/

   # Kindle
   cp -r kagi-news.koplugin /mnt/us/koreader/plugins/

   # Kobo
   cp -r kagi-news.koplugin /mnt/onboard/.adds/koreader/plugins/

   # PocketBook
   cp -r kagi-news.koplugin /mnt/ext1/applications/koreader/plugins/
   ```

3. Restart KOReader

## Usage

1. Open the **hamburger menu** (☰) in KOReader
2. Navigate to **More tools → Kagi News**
3. Select your workflow:
   - **Followed categories** — Choose which news topics you want to track
   - **Sync / Download news** — Bulk fetch all content for offline reading
   - **Browse news** — Read your synced news strictly from local cache (offline-first)
   - **Clear cache** — Manually remove all cached data

> **Note:** On first run, select "Sync" to fetch the category list.

## Project Structure

```
kagi-news.koplugin/
├── _meta.lua            # Plugin metadata
├── main.lua             # Entry point, menu registration, WiFi gating
├── api.lua              # Kagi Kite HTTPS API client
├── storage.lua          # Organized cache management (MD5 hashing)
├── ui.lua               # Main UI screens & Browse news logic
├── category_select.lua  # Followed categories (TouchMenu)
├── htmlviewer.lua       # Custom rich-text viewer (ScrollHtmlWidget)
└── .gitignore           # Ignores local kagi-news/ cache
```

## Architecture

| Module | Responsibility |
|---|---|
| `main.lua` | Plugin lifecycle, menu integration, WiFi connectivity check |
| `api.lua` | HTTPS (`ssl.https`) to `kite.kagi.com`, JSON decoding, error handling |
| `storage.lua` | Local file cache (`meta/`, `articles/`, `images/`), MD5 hashing (`ffi/sha2`) |
| `ui.lua` | Navigation, bulk sync progress via `Trapper:wrap`, offline reading |
| `htmlviewer.lua` | Rich HTML rendering using `ScrollHtmlWidget` (MuPDF engine) |
| `category_select.lua` | Native KOReader `TouchMenu` for category management |

## Cache & Sync Strategy

### Offline-First
The plugin is designed for e-readers. Network calls are only made during explicit **Sync** actions. "Browse news" reads strictly from the local cache to preserve battery and ensure a fast experience.

### Auto-Clear
To ensure news stays fresh, the plugin automatically clears its article and image cache when starting a sync on a new calendar day.

## API

This plugin uses the [Kagi Kite](https://kite.kagi.com/) public API:
- `GET https://kite.kagi.com/kite.json` — list of all news categories
- `GET https://kite.kagi.com/<category>.json` — article clusters for a category

Consult the [official API docs](https://news.kagi.com/api-docs) for technical details.

## License

MIT
