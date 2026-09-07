# v1.3.0

- Shortcut/Dispatcher action added
- Auto-close on device suspend

# v1.2.0

# Slide Puzzle 1.2.0

## Highlights

- **Localization**: built-in translations for English, Português, Español,
  Français, Deutsch, 한국어 and Türkçe. An in-plugin self-contained Lua
  table is used (no gettext toolchain required). *Default* auto-follows
  KOReader's UI language when possible and falls back to English.
- **New Settings sub-menu** regrouping all preferences under a single
  entry (**Tools → Slide puzzle → Settings**).
- **Redesigned Stats dialog**: aligned monospace table with *Size /
  Time / Moves / Plays* columns and a per-size games-played counter.
  CJK-aware column widths keep the layout aligned in every language.

## New settings

- **Font** — choose the face used for the tile digits. First choice is
  *Default*, which inherits KOReader's UI font (so any custom system
  font you've set carries over). Five bundled fallbacks are included
  (Sans, Sans Bold, Serif, FreeSans, Monospace) so the plugin works on
  every device without depending on user-installed fonts.
- **Font size** — explicit override of the auto-computed digit size.
  The spinner pre-fills with the *actual* auto pixel value for the
  current board, so you can nudge it up or down without having to
  guess where *Auto* lives. Keeping the value untouched saves it as
  `Auto` so future board / screen changes keep adapting. The upper
  bound was raised from 96 to 200 so the spinner can always reach the
  auto value on high-DPI devices. Confirmation button now reads
  *OK* / *Tamam* / *확인* / … instead of re-printing the title.
- **Language** — explicit language picker; independent of the KOReader
  UI language so you can keep the rest of the UI in one language and
  the puzzle in another.
- **Reset best results** — moved into Settings and now asks for
  confirmation before deleting anything. Also clears the new *Plays*
  counters.

## UI & behaviour

- Main menu simplified to **Play** + **Settings**.
- Board renderer now accepts a caller-supplied font face and pixel size
  with a per-cell safety clamp (`cell × 0.78`) so picking a very large
  size never makes digits overflow a tile.
- Preference changes are applied live while the puzzle screen is open.
- Solved overlay, size dialog, stats and all in-game buttons fully
  translated.

## Internals

- New modules: [slidepuzzle_i18n.lua](cci:7://file:///c:/Users/Lenovo/source/Lua/koreader/plugins/slidepuzzle.koplugin/slidepuzzle_i18n.lua:0:0-0:0), [slidepuzzle_settings.lua](cci:7://file:///c:/Users/Lenovo/source/Lua/koreader/plugins/slidepuzzle.koplugin/slidepuzzle_settings.lua:0:0-0:0).
- Board exposes `setFontPrefs(face_name, size_override)` with nil /
  zero semantics that map to "use KOReader default" / "auto size".
- README documents the new menu, the font-size behaviour and a
  step-by-step guide for contributing new translations.
- Version bumped to **1.2.0**.

## Migration notes

- Previously saved best times and move counts are preserved; the new
  `plays` field starts at `0` and is filled in as you solve puzzles.
- Users who had never changed the font implicitly get the new
  *Default* font (inherits KOReader UI font). Pick *Sans (Noto)* in
  **Settings → Font** to restore the previous look.

# v1.1.0

- tiles drawn inverted when in the correct position for visual feedback
- fix: correctly record the last movement

# v1.0.0

- initial release
