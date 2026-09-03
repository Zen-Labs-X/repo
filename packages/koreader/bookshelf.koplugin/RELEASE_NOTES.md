# v4.4.1

Patch for v4.4.0. See those notes for the full feature list.

- List lines using `%spacer` now wrap across the space available instead of truncating, and the first line breaks at a balanced point
- Covers and folder stacks sit at the top of a row that is taller than the artwork, rather than floating in the middle of it
- Folder and series stacks draw the same size covers whatever the stack holds
- Installing a development branch by name now only installs from the Bookshelf repository

# v4.4.0

**Bookends token parity**

- Tokens mean the same thing in Bookshelf and Bookends now, so a line copied from one reads the same in the other (#348, #62)
- %warmth uses the device's own scale (0-24 on Kindle) and the frontlight shows OFF rather than 0, matching Bookends
- New tokens: %highlights, %notes, %bookmarks and %annotations for a book's annotation counts; %pages_today, %time_today, %total_read_time, %books_finished and %book_pct_read for reading statistics; %avg_page_time for this book's pace; %warmth_pct and %warmth_icon
- %<token> marks where a token's name ends, so ordinary text can follow it: %<author>s gives the author followed by an s

**Status line in the reader**

- The status line can sit across the top of the reader as well as the shelf, drawn by the same code so it reads the same in both: menu > Settings > Advanced > While reading > Show status line
- If you also use Bookends, its top row and any top-anchored progress bar move down to make room
- The in-reader launcher button settings live in that same section now

- Calibre custom columns survive a wireless calibre sync on books that have a publisher, publication date or rating; before, only books with none of the three kept them
- The Recent shelf no longer offers a page it cannot fill

# v4.3.5

- The hero card shows a book's description again when a two-line title left only a little room - it now fills whatever space remains, down to a single line, instead of vanishing (#349)
- Generated covers for books without artwork no longer cut short titles off with "…" when the last word only just fit; the same fix stops uppercase hero titles doing the odd early wrap (thanks for the Reddit report)
- Swiping between pages of an overflowing chip bar no longer leaves a ghost line from the previously selected chip (#352)
- On a series shelf, the series filter dialog now marks the option that is actually in effect, instead of showing "standalone and books in series" as active before it was (#350)

# v4.3.4

- A shelf pinned to a specific author now finds its books in every "Author name formatting" setting (#347)
- Folder names like "Locked Tomb, The" read as "The Locked Tomb", the way book titles already do (#341)

# v4.3.3

- A line break inside a line's template counts as a space now, instead of swallowing everything after it the moment the line needed shortening (#345)
- A shortened line ends in one "…", not two (#345)
