# v4.6.0

- On-hold and finished books now show their badge and fade on list-view covers, following the same settings as the cover view (#365)
- OPDS downloads use the server's filename when that option is on (#354)
- Pinching to fit more rows fills them again, and redraws faster than before
- The line editor no longer closes when a tap in the Tokens or Icons picker misses a row (#364)
- Swipe to change pages in the token picker

# v4.5.1

- Stack folder tiles no longer show a white corner when the cover drop shadow is off (#362)
- Toggling rotation from a start menu action redraws the shelf straight away, instead of on the next tap
- With a custom chip colour, the currently-reading chip keeps its outline and the divider beside it stays visible
- Calibre custom columns are now read from metadata files up to 64 MB (#357)
- Calibre number columns above a million show in full, rather than as 1.2e+06
- Some English/American spelling inconsistency caught and corrected (#358)

# v4.5.0

**Kindle library**

- On a Kindle, your own Kindle books can now be a shelf alongside the ones you side-load: long-press any chip, **+ Add new chip**, then pick **Kindle Virtual Library**
- It needs [kindle.koplugin](https://github.com/kaikozlov/kindle.koplugin) installed, and only appears where it is. That plugin does all the work of reading and converting your Kindle library; Bookshelf just shows you what it finds, so anything about the conversion itself belongs on its issue tracker rather than this one
- Sorted, filtered and searched like any other shelf, with their own cover art, and they count towards Shelf size
- Titles the Kindle took from a filename are tidied up: an author's name is removed only where the catalogue credits that name, so an unrecognised subtitle or translator is left alone
- The first time you open a Kindle book, kindle.koplugin has to convert it. That takes a few minutes and cannot be interrupted, so Bookshelf asks first, and only once per book
- A new Kindle chip filters out the formats KOReader cannot open, so the shelf is not padded with books that can only refuse. Older MOBI and AZW purchases and `.azw3` files are the usual ones. Show them from the chip's **Filters** if you would rather see everything: tapping one then says why it cannot be opened, instead of dropping you into the file browser
- Move, Delete and Reset are left out for these books, since the files belong to your Kindle's library rather than to you
- Searching your library includes your Kindle books, and searching from an OPDS catalogue now offers **Search my library** alongside the catalogue's own search

**Chips**

- Creating a chip opens the source picker straight away: the source is what the chip is for, and what gives it its name

**Covers and list lines**

- Two new options under Settings > Cover display: **Square cover corners** and **No cover drop shadow**, for a flatter, crisper grid. They work independently, so you can square the corners and keep the shadow, or the other way round. Dropping the shadow gives its reserved pixels back to the cover, so covers grow slightly (#353)
- New `%genres` and `%genre` tokens for list lines and hero text: every genre comma-separated, or just the first where there is no room for more. These are what calibre calls tags, and `[if:genres]...[/if]` gates them like any other token (#346)
- `%sysused` uses a short "M" suffix, matching `%ram`

**Faster**

- The shelf opens faster, and the bigger your library the more it saves. On a Paperwhite 5 with around 250 books, the default shelf went from 2.4 seconds to 0.9, and a grouped Series shelf from 2.3 to 1.4
- Covers stay ready between launches instead of being rebuilt every time the shelf opens. The first launch after updating still has to build that cache, so the speed-up starts from the second one
- Shelf page turns are quicker, and the page-turn animation now defaults to Fast. Medium, Slow and Off are all still there, under Advanced settings > Page turn animation, if Fast still feels slow on your device
- The start menu opens and closes faster
- The book details popup opens quicker, and pinching to change how many covers fit settles in one pass rather than two

**Fixes**

- Two small micro-modules share a hero row instead of each taking a full one (#359)
- Filters set on a Kobo shelf are applied
- Kobo shelves sort by progress and by last opened correctly
- Reopening Bookshelf puts you back inside a Format or Rating group you had drilled into, rather than at the top of the chip

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
