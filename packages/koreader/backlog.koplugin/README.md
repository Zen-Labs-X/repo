# Backlog

**Backlog helps KOReader remember which articles you have already read inside a magazine, anthology, newsletter, or other multi-article EPUB.**

Some EPUBs are not one story from start to finish. They are collections of separate pieces: articles, essays, blog posts, reference pages, or magazine sections. KOReader shows progress for the whole book, but it does not tell you which individual pieces are done.

Backlog adds that missing article-level memory. It shows every article in one list, marks articles as read when you finish them, lets you save pieces for later, and can fade links to articles you have already read.

## What Backlog Solves

Backlog is for books where you often ask:

> **"Have I already read this article?"**

This is common with:

- magazine EPUBs
- newsletter or RSS collections
- anthologies of essays or short stories
- research/reference EPUBs with many linked entries
- any reflowable book where the table of contents is really a list of separate pieces

Backlog treats each final table-of-contents entry as an article. In a flat anthology, those may be the top-level chapters. In a magazine with sections, those are usually the articles inside each section.

## Main Features

- **Article list:** see all articles in the current book with read, unread, current, and saved-for-later status.
- **Per-section counts:** sectioned magazines show counts like `3/8 read` for each section.
- **Automatic read marking:** when you turn past an article's last page, Backlog marks it read.
- **Manual marking:** long-press an article to mark it read/unread or save it for later.
- **Save for later:** keep a separate list of articles you want to return to.
- **Jump actions:** jump to the next unread article or the next saved article.
- **Faded read links:** links to articles you have already read can appear dimmed, like visited links in a browser.
- **Per-book tracking:** Backlog only tracks books where you open its article list, and it never changes the EPUB file itself.

## Screenshot

<p align="center">
  <img src="screenshots/articles-list.jpg" width="360" alt="Articles list"><br>
  <em>Articles list — ▶ current, ✓ read, running count</em>
</p>

## Install

Backlog needs KOReader and a book with a table of contents. It works best with EPUBs and other books whose text reflows, especially when the chapters are separate articles or entries.

### Easiest: App Store Plugin

If you have the [KOReader App Store plugin](https://github.com/omer-faruq/appstore.koplugin):

1. Open KOReader.
2. Go to Tools → App Store.
3. Search for **Backlog**.
4. Install it and restart KOReader.

### Manual Install

1. Download or clone this repository.
2. Make sure the plugin folder is named `backlog.koplugin`.
3. Copy that folder into KOReader's `plugins` directory.
4. Restart KOReader.

Common plugin locations:

| Device | Copy `backlog.koplugin` to |
| --- | --- |
| Kindle | `/mnt/us/koreader/plugins/` |
| Kobo | `.adds/koreader/plugins/` |
| PocketBook | `applications/koreader/plugins/` |
| Android | `koreader/plugins/` in KOReader's data directory |
| Linux / desktop | `~/.config/koreader/plugins/` |

## How To Use It

Open a book, then go to:

**Tools → Backlog (articles read) → Show articles**

The first time you open this list for a book, Backlog starts tracking that book. Books you never open in Backlog are left alone.

### The Article List

The list shows one row per article:

- blank = unread
- `▶` = the article you are currently reading
- `✓` = read
- `☆` = saved for later

Tap an article to jump to it. Tap a section header to jump to the first article in that section.

Long-press an article to mark it read/unread or save it for later. Long-press a section header to mark the whole section read, or unread if the whole section was already read.

### Reading Articles

With the default settings, Backlog marks an article read when you turn past its last page.

If you prefer to control everything yourself, turn off **Auto-mark articles read** and use long-press actions in the article list.

### Save For Later

Use save for later when you notice an article you want to come back to.

You can save articles in three ways:

- In the article list: long-press an article → Save for later.
- From the current article: assign **Backlog: save current for later** to a gesture.
- From a link in the text: long-press the link until KOReader's selection menu opens, then tap **Save for later**.

Saved articles show `☆` and appear together in a **Saved** group at the top of the article list. You can also assign **Backlog: next saved** to a gesture to move through saved articles quickly.

The three states are exclusive — an article is unread, saved, *or* read, never two at once. Saving a read article clears its read mark (it moves to Saved); finishing a saved article marks it read (and drops it from Saved).

### Jump To The Next Article

Backlog adds two actions you can use from the menu or assign to gestures:

- **Backlog: next unread**
- **Backlog: next saved**

These are useful when you are reading a magazine or collection out of order.

### Faded Links

When a link points to an article you have already read, Backlog can dim that link in the page text. This makes cross-references easier to scan because already-read destinations look different from unread ones.

You can turn this off or adjust the strength in settings.

## Settings

Settings are under **Tools → Backlog (articles read)**.

- **Auto-mark articles read** *(default: on)* — mark an article read when you turn past its last page.
- **Show read notifications** *(default: on)* — show a short message when an article is automatically marked read.
- **Fade links to read articles** *(default: Medium)* — choose Off, Subtle, Medium, or Strong.

## FAQ

**Does Backlog change my EPUB?**

No. Backlog stores read/saved status in KOReader's per-book settings next to the book, keyed by each article's location in the document — so your marks survive font changes (re-pagination) and restarts. The EPUB file is never changed.

**Why do I not see Backlog on the home screen?**

Backlog only appears while a book is open. Open a book, then go to Tools → Backlog (articles read).

**What counts as an article?**

Backlog uses the book's table of contents. It tracks the final entries: entries with no smaller entries underneath them. In a simple anthology, that is usually each chapter. In a sectioned magazine, that is usually each article inside a section.

**Why are links not fading?**

Check that the book is being tracked, the linked article is marked read, and **Fade links to read articles** is not set to Off. On e-ink screens, try Strong if the default is too subtle.

**Why does holding a link sometimes open the dictionary instead of Save for later?**

KOReader treats a short hold as dictionary lookup. Hold until the long hold marker appears on the top left of the screen and then release to get the correct menu.

## Development

The decision logic lives in `lib/model.lua` with no KOReader dependencies, so it is unit-tested in isolation:

```sh
busted spec/unit/model_spec.lua   # with the busted framework
luajit spec/run.lua               # or zero-install, with just LuaJIT
```

Linting mirrors KOReader's own config: `luacheck .`. The KOReader-coupled glue (`main.lua`, `ui/articles_view.lua`, `ui/reflinks_overlay.lua`) is verified in the KOReader emulator.

## License

Released under the [MIT License](LICENSE). Built on [KOReader](https://github.com/koreader/koreader)'s plugin API.
