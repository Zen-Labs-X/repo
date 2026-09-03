# v0.0.30

## What's Changed
* chore: drop asc from Grimmory books API call by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/191
* fix: stop refereencing the CFI column in repository code by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/192
* fix: corrected sql for fetching book events by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/193
* fix: resolve plugin path using plugin loader if required by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/194


**Full Changelog**: https://github.com/grimmory-tools/grimmory.koplugin/compare/v0.0.29...v0.0.30

# v0.0.29

## What's Changed
* fix: resolve _meta from local plugin path by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/190


**Full Changelog**: https://github.com/grimmory-tools/grimmory.koplugin/compare/v0.0.28...v0.0.29

# v0.0.28

## What's Changed
* chore: remove CFI migration by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/184
* fix: avoid android SIGABRT during sync by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/183
* fix: properly fail requests for get books on error by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/187


**Full Changelog**: https://github.com/grimmory-tools/grimmory.koplugin/compare/v0.0.27...v0.0.28

# v0.0.27

## What's Changed
* refactor: make `withDatabase` a helper by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/168
* chore: prevent wifi toggle when no wifi by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/172
* fix: show new cover when individual book is reloaded by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/174
* feat: end session when adopting progress by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/173
* chore: drop writing CFI when recording session events by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/181
* fix: handle CFI for nodes that have no space between them by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/182


**Full Changelog**: https://github.com/grimmory-tools/grimmory.koplugin/compare/v0.0.26...v0.0.27

# v0.0.26

## What's Changed
* fix: properly wait for automatic wifi without breaking executor by @sabrina553 in https://github.com/grimmory-tools/grimmory.koplugin/pull/149
* fix: proper toggle of `syncReadingSessions()` by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/150
* refactor: drop unused fields from sync by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/151
* refactor: simplify executor and combine with wifi manager by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/154
* fix: only send progress when needed by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/155
* fix: only emit dismiss callback when not external by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/157
* fix: handle self-closing tags in CFI resolver by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/156
* feat: add session events for annotations by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/160
* refactor: move UI refresh helper into doc_metadata by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/161
* fix: move refresh UI to only when required by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/162
* refactor: set grimmory ID when associating a book by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/163
* fix: use `step` rather than `exec` when executing statement by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/166
* feat: sync annotations with grimmory by @imnotjames in https://github.com/grimmory-tools/grimmory.koplugin/pull/123

## New Contributors
* @sabrina553 made their first contribution in https://github.com/grimmory-tools/grimmory.koplugin/pull/149

**Full Changelog**: https://github.com/grimmory-tools/grimmory.koplugin/compare/v0.0.25...v0.0.26
