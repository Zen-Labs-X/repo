**List view**

- Any shelf can be a text list instead of covers: long-press its chip and pick List, or hold the page number in the footer to flip the shelf you are on
- Rows are built from the same editable lines as the hero card - up to six per row, each with its own template, font, size, weight, slant, case and alignment
- Each shelf picks its own rows (1 to 12) and columns (1 to 3); pinching the shelf fits one more or one fewer row
- Progress bars can sit inside a line, fixed width or sized to how long the book is
- Folders, series and collections draw as a fan of their members' covers
- A layout you like can be saved as a named preset and other shelves pinned to it
- Swiping up to expand a shelf can switch it to a list automatically (a setting)
- New tokens to put in lines: %size, %added, %opened, %favourite and %status_label

**Status line**

- %books_read counts the books in your library marked Finished, and %books_started counts those with reading time recorded by the statistics plugin - both work anywhere tokens do, like the hero status line

**Calibre metadata (beta)**

- A calibre custom series column gives a book a second series stack, so one book can sit in more than one series (#299)
- %calibre{name} shows any calibre column in a line: %calibre{pubdate} for the publication year, %calibre{publisher}, or a custom column by its lookup name
- Custom columns and author sort no longer vanish after a wireless calibre sync: Bookshelf keeps its own copy of the fields KOReader's sync drops, saved automatically whenever it reads a calibre-written metadata file

**Fixes**

- Book details: swipe down closes the popup, Close and Open swapped places, and descriptions no longer open with a stray blank line (#338)
- The bulk "Best guess" Hardcover link searches the way the manual picker does, so it finds the matches the picker finds (#310, with thanks to bmanturner's #311)

**Languages**

- Traditional Chinese, contributed by edison4uk (#308)
- Ukrainian, contributed by advokatb (#332)
