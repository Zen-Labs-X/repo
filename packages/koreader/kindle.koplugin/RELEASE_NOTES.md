# v0.0.8

**Full Changelog**: https://github.com/kaikozlov/kindle.koplugin/compare/v0.0.5...v0.0.8

This release mostly focuses on reading position sync and support for newer Kindle firmware.

Reading position sync is now much more faithful to the native Kindle state. Automatic KOReader -> Kindle sync now runs when a book closes, supports exact kfx/pdoc positions, targets the correct downloaded book entry for catalog updates, and no longer stomps on Kindle's separate read/unread state. The catalog integration was also reworked to use Kindle's real locale/collation behavior while remaining self-contained and working in no framework mode.

Newer Java 21-based Kindle firmware is now supported by the integrated extraction path, and the native extractor fallback has a more reliable runtime environment. The Kindle library menu is also available while reading, unsafe maintenance actions are gated while a book is open, and there's now a dispatcher action for opening the Kindle library.

still very much a work in progress.

python remains slow

please make github issues for any problems you run into

# v0.0.5

**Full Changelog**: https://github.com/kaikozlov/kindle.koplugin/compare/v0.0.4...v0.0.5

major rewrite of the library and reading position sync

the plugin now integrates with koreader using normal file paths instead of the old virtual filesystem hacks. reading position sync is now exact where supported, book access is fully just-in-time, covers work properly in the kindle library, and there are a bunch of fixes for older kindle firmware, cold starts, drm fallback, cache handling, and sidecars.

also updated the bundled kfx converter and did a pretty significant cleanup of the old implementation.

still very much a work in progress, but this should be substantially more reliable than v0.0.4.

python remains slow

please make github issues for any problems you run into

# v0.0.4

v0.0.4 - Processing now works on older Kindle firmware

still very much a work in progress and python is very slow for this task. should be mostly functional, at least

tested on PW6 running 5.18.5.0.1

please make github issues for any problems you run into

# v0.0.3

v0.0.3 - fix: keep Kindle Library menu visible when virtual library is disabled

still very much a work in progress and python is very slow for this task. should be mostly functional, at least

tested on PW6 running 5.18.5.0.1

please make github issues for any problems you run into
