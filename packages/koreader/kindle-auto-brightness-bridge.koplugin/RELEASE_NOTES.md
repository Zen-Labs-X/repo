# v0.2.0

## What changed

- Added optional warmth synchronization for supported Kindles with warm frontlights.
  - Uses KOReader's public hardware warmth reader and existing conversion.
  - Reads the Kindle's currently applied hardware warmth only when KOReader asks.
  - Runs no background polling and writes no warmth merely to synchronize.
  - Has a separate setting and is disabled by default.
- Added native long-press help to the existing brightness synchronization menu item.
- Documented the interaction with KOReader AutoWarmth: the two schedulers remain independent.

## Validation

- 21 plugin tests pass against KOReader.
- Luacheck reports 0 warnings and 0 errors.
- Live-tested on the target Kindle running KOReader v2026.07.2.

Closes #1.
Closes #2.

# v0.1.0

Initial public release.

## What it does

- Keeps KOReader synchronized with brightness changes made by Amazon powerd.
- Fixes stale-cache jumps for relative brightness gestures.
- Uses zero polling and no custom lux-to-brightness algorithm.
- Preserves frontlight off/on remembered brightness.
- Supports Kindles whose native ALS is available even when KOReader model detection is incomplete.
- Places the opt-in checkbox under Tools → More tools without an orphaned NEW prefix.

## Verification

- 12 focused Busted specs passed against current KOReader DeviceListener code.
- LuaJIT syntax and Luacheck passed with zero warnings/errors.
- Physically verified on KOReader v2026.07.2 / KindlePaperWhite6: startup 11, external Amazon powerd change 20, real KOReader +1 gesture 21, matching notification.

## Install

Extract the archive and copy `kindleautobrightness.koplugin/` into KOReader’s `plugins/` directory, restart KOReader once, then enable **Synchronize with Kindle Auto Brightness** under **Tools → More tools**.

Enable Auto Brightness in the stock Kindle UI before starting KOReader.
