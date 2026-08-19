Two fixes, both about Footcream doing things you didn't ask for.

### Leaving a book now stops its scan

Starting a scan and going back to your home screen left the scan running. In the two in-text modes it would then convert the book anyway — rewriting it and reopening it on top of whatever you were looking at, several seconds after you'd walked away.

Leaving a book now cancels its scan, and cancels the conversion queued behind it. Nothing is rewritten, and nothing reopens itself. This works whichever home screen you use, including replacements like the Bookshelf plugin.

### Old conversions are left alone unless you asked for automatic ones

A book converted by an earlier version was interrupted on opening with a question about updating its conversions — a question about an internal version number, asked while you were trying to start reading.

That now only happens with **Auto-convert when opening a new book** switched on, which is the setting that says "rewrite my books without asking". With it off, an already-converted book simply opens, keeping the conversions it has. "Rescan book" still refreshes one whenever you want.
