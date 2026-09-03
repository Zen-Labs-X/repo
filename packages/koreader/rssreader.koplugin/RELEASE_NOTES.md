# v1.16.0

## Better book metadata for saved EPUBs

Articles you save as EPUB now arrive with proper metadata, so they look like real books in your library instead of untitled files. Everything is read from data the plugin already downloads — no article takes any longer to save.

### Author
The article's own byline now appears as the author, with the feed name on a second line beneath it. Previously the feed name was shown in the author field and the byline was discarded, even though CommaFeed, Fever, FreshRSS, Miniflux and NewsBlur all provide one. Feeds that omit a byline fall back to the article page's own markup; anything that doesn't look like a name is left out rather than guessed at.

### Description
Books now have a description — the entry's summary from the feed, or, when the feed provides none, a short excerpt taken from the article's opening paragraphs. Visible under **Book information** and in the file manager.

### Cover image
Saved articles now get a cover. The plugin prefers the thumbnail the feed itself nominates, which is the same image you see while browsing stories. If the feed offers none, it picks the article's lead image by measuring the pictures it has already downloaded, skipping icons and banner strips. Requires image downloads to be enabled.

Previously a cover was only used if the article's HTML happened to declare the image size *and* the image was taller than it was wide — a rule that almost never matched real feed content, so most saved articles had no cover at all.

### Chapters
Long articles now have a real table of contents built from their headings, with subheadings nested under their parent sections. Tap the middle of the screen and open the TOC to jump between sections. Articles without headings keep the previous single-entry behaviour.

## Get back to your feeds from an open article

Opening a story hands it to KOReader as a normal book, and until now finding your
way back to the feed list meant digging through the main menu. There are now
several quicker ways back:

- **A floating RSS button** in the corner of every page. One tap returns you to
  the list you came from, at the position you left it — and closing the list
  drops you straight back into the article, right where you were reading.
- **Corner tap.** The same corner works as a tap target even with the button
  hidden, if you would rather have nothing drawn over your page.
- **End of article.** When you finish reading, the end-of-document prompt now
  offers **Back to RSS list** alongside *Go to beginning* and *File browser*.
- **The Back key.** On devices with a Back button, pressing it inside an article
  returns you to your feeds instead of asking whether you want to quit KOReader.
  Links inside the article still work the way they always did — Back only
  returns to RSS once there is nowhere left to go back to in the article itself.

All of these are optional and can be switched on or off separately under
**Settings → Return to RSS from an article**, including which corner the button
sits in. It defaults to the bottom right, where it is least likely to get in the
way of page turns, the menu strip or your bookmarks, and it keeps clear of the
status bar. On devices without a touchscreen the button and corner tap are off
by default, since there is nothing to tap.

This covers stories you open from a feed or from your reading list. Articles you
*save* to your library stay ordinary books, and pages opened with *Open
Sanitized* from a link are left alone as well.

## Full hardware-key navigation

RSS Reader can now be driven entirely with physical buttons on Kindle 3/4 and
key-based Kobo/PocketBook models:

- **Up / Down** move through the list, wrapping onto the Back button below the
  last item
- **Press** (5-way centre) opens the selected entry
- **ScreenKB + Press** on Kindle 4, **Shift + Press** on keyboard devices, or
  **Right** on few-key devices opens an entry's context menu
- **Page turn buttons** page through lists and scroll the story preview
- **Back** steps up one level — feed → category → account list — and closes the
  story preview

If you would rather have a dedicated shortcut, the **RSS Reader** action can be
bound to a key combination with the Hotkeys plugin.

# v1.14.1

- Fix non-Latin titles (Cyrillic, etc.) being sanitized to underscores in filenames

    Filename sanitization used a whitelist of ASCII word chars, so any
    non-ASCII letter was stripped, turning archived titles into
    all-underscore filenames. Switch to a blacklist of characters actually
    illegal in filenames, and make title truncation UTF-8 boundary aware
    so it can't cut a multi-byte character in half.

# v1.14.0

- Add CommaFeed tag browsing and per-story tag editing

    Adds a virtual "Tags" folder under CommaFeed accounts that lists all
    tags and lets you drill into a tag's stories. Also adds an "Edit Tags" 
    action on stories  and shows a story's current tags in its long-press
    popup.

# v1.13.0

- Add article starring support for CommaFeed accounts
    Wire CommaFeed's /entry/star API into the story viewer toolbar and the
    story long-press menu (next to Add to List), show a star marker in
    story titles, and add a ★ Starred virtual feed at the root level that
    aggregates all starred articles. 

- Fix Miniflux feed state restore , pr by philvernon

# v1.12.0

- "open sanitized " and "save sanitized" buttons on link popup
- add api support for the webbrowser plugin
