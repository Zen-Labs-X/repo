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
