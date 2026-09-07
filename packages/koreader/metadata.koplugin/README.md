# Metadata for KOReader

Search online book metadata from KOReader, preview the result, and apply supported metadata and cover images to local KOReader custom metadata.

> [!NOTE]
> This plugin writes KOReader custom metadata for local use. It does not rewrite the book file itself or update a Calibre library database.

## What it does

- Searches book metadata from online providers.
- Shows detailed metadata and cover images before applying changes.
- Applies supported fields such as title, authors, series, language, tags, description, and identifiers.
- Can apply the selected cover image together with metadata.
- Lets you choose which providers are enabled.
- Searches one enabled provider at a time from the search dialog.

## Installation

1. Place the plugin directory under KOReader's `plugins/` directory:
   `plugins/metadata.koplugin`
2. Restart KOReader.
3. Enable the plugin if your KOReader setup requires manual plugin activation.

## How to access it

- File browser action: open a book file's actions and choose `Search metadata`.
- Settings menu: `More tools` -> `Metadata`.

```text
File Browser
└─ Book file
   └─ Search metadata

More tools
└─ Metadata
   ├─ Sources
   │  ├─ 豆瓣
   │  ├─ Google Books
   │  └─ Bangumi
   └─ Configuration
      ├─ Apply cover with metadata
      ├─ Cover width
      └─ Detail font size
```

## Configuration / Usage

- `Sources`: enable or disable providers. At least one provider must remain enabled.
- Long-press `Google Books` in `Sources` to set or clear a Google Books API key.
- `Apply cover with metadata`: choose whether `Apply` also writes the selected cover.
- `Cover width`: adjust the cover preview width in the detail view.
- `Detail font size`: adjust the metadata detail text size.

The search dialog prefills the query from the original document title when available, otherwise from the current title or the filename. It shows only currently enabled providers, and each search runs against the selected provider only.

Search results open directly in the detail view. Use the result menu or the `Previous page` and `Next page` buttons to switch results, then choose `Apply` to write metadata. When a search fails, returns no results, or you close the detail view, the search dialog is restored with the previous query and selected provider.

```text
┌────────────────────────────────────┐
│ Search metadata                    │
├────────────────────────────────────┤
│ One Hundred Years of Solitude      │
├────────────────────────────────────┤
│ (●) 豆瓣                           │
│ ( ) Google Books                   │
│ ( ) Bangumi                        │
├────────────────────────────────────┤
│ [Cancel]                  [Search] │
└────────────────────────────────────┘
```

```text
┌──────────────────────────────────────────────┐
│ ☰  One Hundred Years of Solitude (1/10)    × │
├──────────────────────────────────────────────┤
│ Title: One Hundred Years of Solitude         │
│ Authors: Gabriel Garcia Marquez              │
│ Publisher: HarperCollins                     │
│ Published: 2006                              │
│ ISBN: 9780060883287                          │
│ Tags: Fiction                                │
│                                              │
│ Description                                  │
│ One Hundred Years of Solitude tells the      │
│ story of the rise and fall of Macondo.       │
├──────────────────────────────────────────────┤
│ [Previous page]      [Apply]      [Next page]│
└──────────────────────────────────────────────┘
```

## Limits / Notes

- Metadata quality depends on the selected upstream provider and the query.
- Some provider-specific fields are displayed for review but are not written to KOReader metadata.
- Network, search, and cover download failures can happen when providers change their APIs or pages.
- Already running provider requests are not cancelled immediately when the UI closes; stale callbacks are discarded when they return.

## Credits / Upstream

- Douban Books: <https://book.douban.com/>
- Google Books API: <https://developers.google.com/books>
- Bangumi API: <https://bangumi.github.io/api/>
