# v1.5.3

### Fixed

- **A Kindle Paperwhite could not tell Seekquel what it was.** Every time the add-on
  introduced itself, the server refused the whole message because the device's model name
  was one character too long for the field holding it. Nothing looked wrong: your pages,
  reading time and highlights all synced normally. But the reply to that message is what
  carries your time zone, the settings you change from the app, and the news that a newer
  add-on exists, so none of those reached the device, and the app showed it as a nameless
  reader with no version and no settings. The fix is on the server, so an affected device
  names itself the next time you open a book, with nothing to install.
- **Sending your reading history no longer holds the screen for half a minute.** One device
  reported a single send taking 25 seconds, and the screen is frozen for the whole of it.
  Sends are now given fifteen seconds, and anything that does not fit goes with the next
  sync instead of keeping you waiting.

### Changed

- **Reading time is only sent when it has changed.** The add-on rebuilt and re-sent the
  same day totals on every sync whether or not you had turned a page, which on the way out
  of a book could push your highlights out of the same trip. Nearly half of all reading
  time sends were crediting nothing. It now compares what it is about to send against what
  it last sent and skips the trip entirely when nothing has moved, which leaves room for
  your highlights.

# v1.5.2

### Added

- **Get the Seekquel app from the device itself.** Under Seekquel, tap **Get the Seekquel
  app** for a QR code that opens Seekquel's links page on your phone, where the right app
  store is one tap away. It is offered before you connect a device, since you need the app
  before you have anything to pair with, and again under Settings for a second phone or
  tablet.

# v1.5.1

### Fixed

- **Looking something up at the back of a book is no longer recorded as reading it.** Jump
  to an index, an endnote, a glossary or an appendix and your place went with you: one
  reader 7% into a book was recorded at 94%, that leap was counted as pages read that
  afternoon, and it was announced to their followers as three quarters of a book. Worse,
  it stayed the furthest point of the read, so everything they genuinely read afterwards
  counted for nothing. Your place now only moves once you have actually read from where
  you landed, so a look at the index is never sent at all. Skipping ahead and reading on
  still follows you there, after a few pages.
- **A day is only credited with the pages you turned.** Skip an introduction and your place
  moves without the skipped pages being added to your day. The add-on now reports how much
  of the book you crossed a page at a time, and that is the most a sync can be credited
  with, so nothing you did not read reaches your streak, your goals or your badges.

# v1.5.0

### Added

- **Syncing now also happens on a timer, every fifteen minutes by default.** Until now the
  only thing that brought a sitting across while you were still in the book was turning
  twenty pages, so reading slowly, or reading a few pages and putting the book down
  without closing it, left everything waiting. Set it to five, thirty or sixty minutes, or
  off, under **Settings > Sync on a timer**, or from Seekquel under Settings, Integrations,
  KOReader, like the other switches. A tick with nothing new to send does nothing, so it
  costs you no pauses, and it follows **Sync while reading** like the page count does.

### Fixed

- **A highlight made and then left behind now catches up.** Two things were against it.
  Switching away from KOReader allows five seconds for the whole send and each request
  can take two, so with your place and your reading time ahead of it in the queue, a
  passage was routinely the one that ran out of time. And reopening the book sent only
  your place, so nothing tried again until twenty pages had turned, you closed the book,
  or you tapped Sync now. Passages now go ahead of reading time on the way out, since
  reading time is a daily total that is complete whenever it arrives, and reopening a
  book sends anything still waiting.
- **Sleeping the device and picking it back up now syncs.** A message that fails leaves
  the server alone for two minutes so one unreachable server cannot cost one wait after
  another. Sleeping a reader turns its Wi-Fi off, so the send on the way out usually
  failed, and that failure then swallowed the catch-up send when you came back: you slept
  the reader, woke it, and nothing had moved. Waking up and finding a network both end
  that wait now, because both are reasons to think the answer has changed.
- **Update status and Rate this book show which one the book is on.** Both were lists of
  every option with no mark on the current one, so all four statuses looked equally wrong.
- **Send status changes from this device can be set from the app.** It has been on the
  reader since 1.4.0 and the server did not recognise it, so it was the one switch you had
  to go and find the e-reader to change.
- **The slowest call the add-on reports is the slowest since it last reported.** It used to
  be the slowest ever, kept for the life of the install, so one bad afternoon was re-sent
  unchanged on every version after it and a reader whose problem was fixed still looked
  slow.

# v1.4.5

### Fixed

- **Switching away from KOReader now syncs properly, not just your place in the book.**
  Closing a book has always sent everything; backgrounding the app sent only your page, so
  reading time and highlights waited until you came back to the book. That is exactly
  backwards: the moment you leave KOReader is the moment you open Seekquel. It now sends
  your place, your reading time and your highlights on the way out, with a five second
  ceiling on the whole thing and two seconds on any single request, so it cannot hold the
  screen the way the old version did. Anything that does not fit still goes when you
  return.
