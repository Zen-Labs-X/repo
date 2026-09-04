# v5.25.0

**Fixes**

- Fixed a crash when turning the top or bottom status bar on while another plugin is hosting the Bookends menu. The settings dialog now opens over the menu instead of replacing it in that case.
- `%sysused` now reports correctly on older Kindles such as the Paperwhite 3, where it was counting reclaimable disk cache as used memory and sitting close to full. Thanks to @ksaMask123 for tracking this down and fixing it.

**Changes**

- `%sysused` renders as `84M` rather than `84 MiB`, matching `%ram` and the Bookshelf plugin. Lines using it will be a little shorter.

# v5.24.0

**Calibre columns in your status bar**

If your library is managed by Calibre, `%calibre{name}` now shows any column from it, using the column's lookup name: a custom column `#mood` renders with `%calibre{mood}`. Text, list, number, date, yes/no and multi-value columns all work. Three standard fields come through the same way: `%calibre{pubdate}`, `%calibre{publisher}` and `%calibre{rating}`. Conditionals work too, so `[if:calibre{mood}="cosy"]` does what you would expect.

Nothing is read unless one of your lines actually uses the token.

**Fourteen new tokens**

Book details that were only available on the Bookshelf home screen now work in the reader as well: `%status` and `%status_label`, `%rating` and `%rating_number`, `%description`, `%size`, `%added`, `%opened`, `%favourite`, `%author_count`, `%authors_short`, `%quote` and `%quote_source`, plus `%sysused` for memory.

**`%spacer`**

A new elastic gap that pushes everything after it to the far edge of the line, so `%author%spacer%book_pct` puts the author hard left and the percentage hard right without any fiddling with widths.

**Fixes**

- A long chapter title in a centred or right-hand region could run off the left edge of the screen with its first words missing. This happened when that region had no neighbour in the same row, so nothing forced it to truncate. It now truncates against your Bookends margins (#108)
- Updates could fail on a slow connection. The download was capped at 60 seconds regardless of how it was progressing, so a download that was merely slow failed the same way a dead one does
- When an update does fail, the message now says why (timed out, no response, or the actual error), instead of just "Download failed." A partly downloaded file can also no longer be left behind to confuse the next attempt
- `%wifi_icon` now works as another name for `%wifi`, so a line copied from Bookshelf no longer shows the token's own name

**If you use Bookshelf too**

Bookshelf can now show its status line across the top of the reader. When it does, your top row and any top-anchored progress bar shift down to make room. The switch is in Bookshelf; there is nothing to set up here.

# v5.23.1

**Fixes the in-app updater**

Installing an update crashed KOReader before it could finish. Bookends unpacked the downloaded file using a KOReader helper that was removed from KOReader itself in mid-2026, so on current versions that call failed and took the reader down with it. It now unpacks using the same library KOReader uses internally.

The download was never the problem, so nothing was left half-installed — the previous version stayed in place and came back on restart.

**If you're on v5.23.0 or earlier you'll need to install this one by hand.** The updater is the thing that was broken, so it can't update itself. Download the zip below, unzip it, and copy the `bookends.koplugin` folder over the existing one in your KOReader `plugins` directory. Updates after this one work normally again.

Everything in [v5.23.0](https://github.com/AndyHazz/bookends.koplugin/releases/tag/v5.23.0) is included — auto preset by file type, the progress-marker fix, the new tokens, and Ukrainian and European Portuguese translations.

# v5.23.0

> [!IMPORTANT]
> **Don't install this one with the in-app updater — use [v5.23.1](https://github.com/AndyHazz/bookends.koplugin/releases/tag/v5.23.1) instead.**
>
> Updating crashes KOReader on v2026.07 and newer. Bookends unpacked the download using `Device:unpackArchive`, which KOReader removed in [751b497](https://github.com/koreader/koreader/commit/751b49784878fa749f8c06cffbeeb43031ea5202) (5 July 2026). v5.23.1 fixes it and contains everything below, but has to be installed by hand the first time, since the updater is the broken part. See #109.

**Auto preset by file type**

Bookends can now switch preset, or hide itself entirely, based on the file you open. Under **Bookends settings > Auto preset by file type**, add a rule for a file extension and pick either a preset or **Hidden (no overlay)**. The picker previews each preset live on the page before you commit.

Comics and manga were the motivating case: a rule that hides the overlay for CBZ keeps the artwork clear, and going back to an EPUB restores your normal preset with nothing to toggle by hand. The same works the other way, e.g. a plainer preset for PDFs.

Rules key off the extension, so one rule covers every file of that type. Your normal preset is remembered separately from whatever a rule switches you to, so removing a rule puts you back where you were.

**Progress markers stay put when you change font size**

The Today, session and book-opened markers on progress bars were anchored to a page number. Changing font size re-paginates the book, so that number stopped pointing at the same place and the marker drifted away from where you had actually read to. They're now anchored to the text itself and hold their position through font, margin and line-spacing changes.

**Hours and minutes in conditionals**

`chap_time_left_h`, `chap_time_left_m`, `book_time_left_h` and `book_time_left_m` now work inside `[if:…]`, matching the tokens of the same names. That makes the stock-Kindle phrasing possible, where the hours only appear when there are any:

```
[if:chap_time_left_h>0]%chap_time_left_h hr(s) [/if]%chap_time_left_m min(s) left in chapter
```

giving "2 hrs 5 mins left in chapter", then "42 mins left in chapter" once under an hour. Both the chapter and book versions are in the token picker under **Templates**.

**Tokens that sit flush against text**

A token name runs until the next non-letter, so anything typed straight after it gets read as part of the name. Wrapping the name in angle brackets marks where it ends:

```
%<book_time_left_h>h%<book_time_left_m>m
```

gives `4h40m`. Width limits still work inside, e.g. `%<author{200}>`.

**Position in the folder**

`%file_num` and `%file_count` give the open file's place among the documents in its folder, so `File %file_num/%file_count` shows "File 5/10". Ordering follows your file manager sort settings. Aimed at comics and manga kept as one file per chapter, where the page and chapter tokens can only describe the chapter you're in.

**Weekday and month names follow your language**

`%weekday`, `%weekday_short`, `%date_long` and `%datetime{}` were rendering English day and month names regardless of your KOReader language. They now use KOReader's own translations, which covers every language KOReader ships rather than only the ones Bookends has a translation file for.

**Presets folder in Folder shortcuts**

The presets folder now appears in KOReader's **Folder shortcuts**, so you can reach it from the file manager without typing the path. Useful for copying preset files on or off the device by hand.

**Gallery**

Install counts load faster and no longer stop working on busy days. The counts endpoint was doing one lookup per preset in the gallery, which grew slower as the gallery grew and was hitting a daily quota; it's now a single lookup regardless of size.

**Memory token on older Kindles**

`%mem` rendered as nothing on older devices, because it read a field that only exists on newer Linux kernels. It now falls back to the equivalent older fields. Thanks to ksaMask123 for the fix and the diagnosis, in #106.

**New languages**

Ukrainian (uk) and European Portuguese (pt_PT), thanks to the contributors in #105 and #93.

# v5.22.0

**Chapter progress at any TOC depth**

The chapter progress tokens now take a depth suffix, the same way `%chap_title_1`…`%chap_title_9` already do: `%chap_read_N`, `%chap_pages_N`, `%chap_pages_left_N`, `%chap_pct_N`, `%chap_pct_left_N`, plus `%chap_time_left_N` and `%chap_time_left_N_eta`.

Without a number they track the deepest chapter, as before. With a depth, e.g. `%chap_read_1`, they measure against the top-level chapter instead. Useful for books with a very fine table of contents, where a plain `%chap_read` shows a tiny sub-section's length next to a top-level `%chap_title_1`.

Type them manually (they're not in the token picker). The README token reference lists the full set.
