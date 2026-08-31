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
