# v1.8.0

### What’s new

Sync now ends with a short reading recap showing today’s minutes and pages, the chapter reached, and your current progress. Automatic syncs stay quiet. Open Today’s reading to see the recap again, or Today in Seekquel to refresh your daily targets and current streak.

When Seekquel has a later place logged from a hardcover, audiobook, another edition or another app, opening the linked book now asks before moving KOReader to the closest percentage in the local file. The move is approximate and never adds pages or reading time.

### Install

Download the zip, extract it, copy the seekquel.koplugin folder into koreader/plugins, then restart KOReader.

Existing installations can update from Tools, Seekquel. KOReader versions older than v2025.08 still require the manual file copy.

# v1.7.1


### Fixed

- **Seekquel now works on older KOReader builds, where it used to be missing entirely.**
  On any KOReader released before v2025.08, the add-on failed to load and showed nothing
  at all: no menu, no pairing screen, and no message saying why. It loaded a part of
  KOReader that only exists in newer builds, and KOReader skipped the whole add-on when
  it could not find it.

  Everything works on those builds now except the add-on updating itself, which needs
  that same missing part. The menu says a new version is ready and that it needs a
  computer to install, and tapping it explains to copy the files across rather than
  turning on wifi and failing at the end of a download.

  Found and fixed by [joelstitch](https://github.com/joelstitch).

# v1.7.0


### Added

- **Seekquel can now show you which part of the day you read in, and your device is the
  only thing that knows.** KOReader writes down the moment of every page turn, so the
  add-on now reports the hours a day's reading fell in alongside the minutes it already
  sent. Your reading stats gain a morning, afternoon, evening and night breakdown that is
  filled in from the history already on your reader, going back as far as your statistics
  do, rather than starting from empty on the day you update.

  The hours are read on your device's own clock and shifted by the timezone offset the
  add-on already uses for dating a day, so a chapter finished after midnight counts as
  night rather than as the following morning.

  Nothing else changes. The daily minutes, pages and chapter are the same numbers as
  before, and a day whose hours do not add up to it is sent without them rather than
  putting a correct total at risk.

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
