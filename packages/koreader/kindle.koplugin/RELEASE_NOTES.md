**Full Changelog**: https://github.com/kaikozlov/kindle.koplugin/compare/v0.0.4...v0.0.5

major rewrite of the library and reading position sync

the plugin now integrates with koreader using normal file paths instead of the old virtual filesystem hacks. reading position sync is now exact where supported, book access is fully just-in-time, covers work properly in the kindle library, and there are a bunch of fixes for older kindle firmware, cold starts, drm fallback, cache handling, and sidecars.

also updated the bundled kfx converter and did a pretty significant cleanup of the old implementation.

still very much a work in progress, but this should be substantially more reliable than v0.0.4.

python remains slow

please make github issues for any problems you run into