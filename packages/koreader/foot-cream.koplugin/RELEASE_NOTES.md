Thank you for all the errors/flags you've sent in! The conversion and filtering is now much improved thanks to that. Please keep doing that. 

### Footcream now speaks 30 languages

The plugin interface — menu entries, dialogs, notifications and the long-press
explainers — is translatable, and this release ships with 30 languages:

Arabic, Catalan, Chinese (Simplified and Traditional), Czech, Danish, Dutch,
Estonian, Finnish, French, German, Greek, Hebrew, Hungarian, Indonesian,
Italian, Japanese, Korean, Norwegian Bokmål, Polish, Portuguese (Brazil and
Portugal), Romanian, Russian, Slovak, Spanish, Swedish, Turkish, Ukrainian,
Vietnamese.

Footcream follows KOReader's own language setting — there is nothing to
configure. Anything not yet translated falls back to English.

**Only the interface changes. Your conversions do not.** The scanner, the
maths and the output are untouched by any of this: the same measurements are
found, the same values come out, and a measurement reads identically in every
language — `1.8 m`, `5 ft 11 in`, `°C`, decimal point and all. In the two
modes that rewrite the book's text, **not one translated word is written into
your book.** Switching KOReader to Japanese changes the menus and nothing
else.

**These are machine-assisted drafts awaiting native speakers.** If you read one
of these languages, corrections are very welcome and take a few minutes — see
[TRANSLATING.md](TRANSLATING.md).

### Fixed

- **Android: "Check for updates" crashed the reader outright.** KOReader's
  dismissable-subprocess helper forks, and Android's runtime can't safely fork
  a live process once network work has started. The update check now runs
  inline on Android. (#4)
- **"Rescan book" silently did nothing in the two in-text modes.** The scan ran
  and reported its matches, then never re-applied the conversion — no error, no
  prompt, indistinguishable from the plugin being broken.
- **Scanning no longer flashes or ghosts the screen.** The corner progress ring
  repaints only its own small region instead of forcing a full-screen refresh.
- **One rescan could produce up to five separate interruptions**, two of them
  reporting different counts ("Scan complete: 321 units found" immediately
  followed by "Converted 304 units in book"). The scan notice is now suppressed
  when a conversion is queued behind it; the mode that only underlines still
  always announces, since there the notice is the only feedback there is.

### Scanner

Cache version 59 → 64; already-scanned books rescan themselves once on open.

- **"2001's" and "the 90's" are no longer read as heights**
  A guard for this shipped in 1.6.0 but could never actually fire.
- **Height notation with curly quotes now works** — `6'2"` as typeset by most
  commercial EPUBs, not just the straight-quote form. (#2)
- **"ten degrees Celsius" is no longer converted as Fahrenheit** — an already
  metric figure was coming out as −12 °C.
- Bare **"degrees"** converts as Fahrenheit only when the surrounding sentence
  is about temperature; angles, proof and headings are left alone. "minus
  seventy degrees" now negates correctly.
- **"twenty-three square leagues"** and hyphenated compounds like
  **"250,000-square-foot"** now convert as areas rather than lengths.
- **"three-toed feet"** is no longer read as a distance