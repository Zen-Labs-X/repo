# v6.4.1

### Changed
- Book progress → chapter bar: when a book has fewer chapters than the
  "Chapters per page" setting (default 25), the paging arrows no longer
  appear at all (previously shown greyed-out). Instead, the chapter
  columns stretch to use the freed-up width.

# v6.4.0

### Added
- Reading streak popup can now be assigned to a gesture/shortcut
  (Dispatcher action: "Reading insights: reading streak"). 
- Reading heatmap popup can now be opened directly, without going
  through the main insights popup first — via a new Tools menu entry
  ("Show Reading heatmap") and a new gesture/shortcut action
  ("Reading insights: reading heatmap").
- Translations for both new actions/menu entry in all supported
  languages (en, de, hu, pt_PT, uk, zh_CN).
#74

# v6.3.0

**Fixed**

Landscape layout for the monthly chart, Last week section, and both calendars so everything fits on screen.

# v6.2.9

**Fixed**

- Removed dead code: the unused "today, all books" full-table-scan query. A bit faster book progress popup open.

# v6.2.8

**Changed**

Book progress calendar: start-day marker changed from a hollow flag to a ▷ triangle; projected finish-day marker changed from a solid black flag to a hollow white flag.
