# splitread - Translation Panel for KOReader

A KOReader plugin that displays real-time translations in a split panel, designed for language learners reading foreign-language books.

---

## Screenshots

| Reading View | Settings |
|---|---|
| ![Reading View](screenshots/readingview.png) | ![Settings](screenshots/settings.png) |

---

## What It Does

Splitread divides your reading screen into two halves:
- **Top** - the original text, as normal
- **Bottom** - a live translation of the visible page, updating automatically as you turn pages

Translation is powered by KOReader's built-in Google Translate integration - no API key required. An active internet connection is needed for translations to work.

---

## Who Is It For?

It works best for readers who:
- Are at an intermediate level and can partially understand the original text
- Want to read authentic foreign-language books rather than graded readers

---

## Installation

1. Download the latest release from the [releases page](https://github.com/sadatdaniel/splitread.koplugin/releases) or clone this repository.
2. Copy the `splitread.koplugin` folder to your KOReader plugins directory:
   - **Kobo/Kindle:** `koreader/plugins/`
   - **Android:** `/sdcard/koreader/plugins/`
   - **Desktop (Linux):** `~/.config/koreader/plugins/`
3. Restart KOReader.

---

## Usage

### Enabling for a book

Splitread is disabled by default and must be enabled per book:

1. Open a book
2. Tap the top of the screen to open the reader menu
3. Tap the **NAVIGATION** menu (the menu that shows bookmarks, table of contents, and skim document)
4. Scroll to find **splitread** (maybe on the second page of options)
5. Tap **Enable for this book**

### Settings

While splitread is enabled, tap the **⚙** icon in the bottom-right corner of the translation panel to open settings:

- **Source language** - language of the book (default: Auto detect)
- **Target language** - language to translate into (default: English)
- **Auto-translate** - toggle automatic translation on page turns
- **Provider** - allows you to switch between translation providers. (To learn how to obtain a Gemini Translation API key, see the section further down this page)
- **Font size** - adjust the translation panel font size

Settings are saved globally across all books.

### Disabling for a book

Go back to the same **NAVIGATION** menu -> **splitread** -> **Disable for this book**. The screen returns to normal.

### Getting a Gemini API Key

1. Sign in to your Google account.

   > **Recommendation:** Use a separate Google account that does **not** have a payment method attached. This helps ensure you stay within the free tier and prevents accidental charges.

2. Go to **Google AI Studio**: https://aistudio.google.com/apikey

3. If prompted, create a new project.

4. Click **Create API Key** and copy the generated key.

5. **Keep your API key private.**
   - Never share it with anyone.

6. Create a file named `keys.lua`.

7. Add your API key following the template in `keys.lua.sample`:

   ```lua
   return {
       gemini = "your-gemini-api-key-here",
   }
   ```

8. Save the file and restart KOReader.

The Gemini translation provider is now ready to use.

---

## Requirements

- KOReader (tested on v2026.03)
- Active internet connection (uses Google Translate via KOReader's built-in translator)
- EPUB or other text-based formats (PDF not supported)

---

## Tested On

- Kobo Libra H2O
- Linux (KOReader AppImage)

---

## Known Limitations

- The first and last lines of each page may be partially cut off at page boundaries - SplitRead stitches sentences across pages to compensate in the translation panel
- Very large font sizes in the translation panel may cause text to be clipped
- Requires WiFi/internet for every page translation

---

## Contributing

The project started as a personal solution, but I decided to share it in case others find it useful as well. I plan to continue developing and improving the plugin as new needs arise during my language learning journey.

Feature requests, bug reports, and pull requests are welcome.
