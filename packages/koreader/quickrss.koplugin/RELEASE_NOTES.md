# v0.2.1

**QuickRSS v0.2.1-beta-hotfix**

- Reverted back to using LuaSec for fetching instead of wget as it caused hard to track issues

# v0.2.0

**QuickRSS v0.2.0-beta**

A fast, standalone RSS reader plugin for KOReader. Browse and read articles from your favorite feeds without leaving your e-reader.

**Highlights**

- Paginated feed view with thumbnail cards
- Full HTML article reader with banner images, bold, lists, and inline images
- Full-text extraction for truncated RSS summaries (via FiveFilters, configurable)
- Offline-first: articles and images cached to disk
- OPML feed management (edit on device or from your computer)
- Customizable reader font, size, and line spacing

**Installation**

- Download `quickrss.koplugin.zip` from this release
- Unzip it into your KOReader plugins directory (e.g. `.adds/koreader/plugins/` on Kobo, `/mnt/us/extensions/koreader/plugins/` on Kindle)
- Restart KOReader
- Open the search menu and tap QuickRSS

**Looking for beta testers**

This is the first public release and there will be rough edges. If you run into bugs, crashes, or have feedback on the workflow, please open an issue, it's incredibly helpful at this stage. Tested on Kobo and desktop Linux KOReader so far; reports from Kindle, PocketBook or other platforms are especially welcome.

Thanks for giving it a spin!

---

**What's New in v0.2.0**

- **Filter by feed** — new button in the footer lets you view articles from a single feed or all feeds at once
- **Opening indicator** — shows which article is loading when you tap on it
- **Full screen refresh** — diagonal swipe clears e-ink ghosting, just like in KOReader
- **RSS icon in the main menu** for easier spotting
- **Faster & more reliable image downloads** — smarter handling of flaky network connections on e-readers, automatically skips broken hosts instead of waiting for timeouts
- **Dedicated data folder** — plugin data now lives in its own quickrss/ directory instead of cluttering KOReader's settings folder (note: you'll need to re-fetch articles after updating)

# v0.1.0

**QuickRSS v0.1.0-beta**

A fast, standalone RSS reader plugin for KOReader. Browse and read articles from your favorite feeds without leaving your e-reader.

**Highlights**

- Paginated feed view with thumbnail cards
- Full HTML article reader with banner images, bold, lists, and inline images
- Full-text extraction for truncated RSS summaries (via FiveFilters, configurable)
- Offline-first: articles and images cached to disk
- OPML feed management (edit on device or from your computer)
- Customizable reader font, size, and line spacing

**Installation**

- Download `quickrss.koplugin.zip` from this release
- Unzip it into your KOReader plugins directory (e.g. `.adds/koreader/plugins/` on Kobo, `/mnt/us/extensions/koreader/plugins/` on Kindle)
- Restart KOReader
- Open the search menu and tap QuickRSS

**Looking for beta testers**

This is the first public release and there will be rough edges. If you run into bugs, crashes, or have feedback on the workflow, please open an issue, it's incredibly helpful at this stage. Tested on Kobo and desktop Linux KOReader so far; reports from Kindle, PocketBook or other platforms are especially welcome.

Thanks for giving it a spin!
