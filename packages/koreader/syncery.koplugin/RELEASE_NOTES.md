## [v1.2.3] — 2026-07-24

### Changed
- **The "point out this book" prompts now say *which* book they mean.**
  When migrating storage modes, Syncery picks the book it wants you to
  locate — so it now names it ("Can't find *Title*. Point it out…")
  instead of asking you to point out one of N unnamed books and leaving
  you to guess. The "that file doesn't match" message names the book too,
  in every place the picker is used, since by then you've been through a
  file browser and the title is no longer on screen. Where *you* picked
  the book a moment earlier (Progress Browser, Annotation Browser), the
  opening prompt is unchanged — repeating the title there would just be
  noise.
