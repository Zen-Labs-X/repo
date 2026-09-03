# webapp/v2026.07.10.1

New release because a few DNS issues with the KOReader plugin have been resolved + Web E-Reader and Hardcover progress sync.

## What's Changed
* feat: added option to disable various automatic syncs by @Sudashiii in https://github.com/Sudashiii/Sake/pull/62
* feat: silently not doing syncs if no wifi connection enabled by @Sudashiii in https://github.com/Sudashiii/Sake/pull/63
* feat: added contributingmd and fixed koreader plugin version bump by @Sudashiii in https://github.com/Sudashiii/Sake/pull/65
* feat(api): implement OPDS 1.2 catalog with basic auth and navigation by @ananyatimalsina in https://github.com/Sudashiii/Sake/pull/61
* feat: changed dav to basic auth and added docs by @Sudashiii in https://github.com/Sudashiii/Sake/pull/67
* feat: added option to have seperate password for basic auth by @Sudashiii in https://github.com/Sudashiii/Sake/pull/68
* fix: fixed auth for http by @Sudashiii in https://github.com/Sudashiii/Sake/pull/71
* feat: restructured metadata provider by @Sudashiii in https://github.com/Sudashiii/Sake/pull/72
* providers by @Sudashiii in https://github.com/Sudashiii/Sake/pull/73
* feat: extended metadata downloader by @Sudashiii in https://github.com/Sudashiii/Sake/pull/75
* feat: using networkmanager for wakeup progress sync now by @Sudashiii in https://github.com/Sudashiii/Sake/pull/76
* feat: added plugin list and version checker in webapp by @Sudashiii in https://github.com/Sudashiii/Sake/pull/77
* feat: web based e-reader by @Sudashiii in https://github.com/Sudashiii/Sake/pull/78
* feat: hardcover progress sync by @Sudashiii in https://github.com/Sudashiii/Sake/pull/79
* feat: keep screen awake on e-reader by @Sudashiii in https://github.com/Sudashiii/Sake/pull/81
* fix: s3 pagination by @Sudashiii in https://github.com/Sudashiii/Sake/pull/82

## New Contributors
* @ananyatimalsina made their first contribution in https://github.com/Sudashiii/Sake/pull/61

**Full Changelog**: https://github.com/Sudashiii/Sake/compare/webapp/v2026.04.04.4...webapp/v2026.07.10.1

# webapp/v2026.04.04.4

I've added quite a lot of stuff the last weeks. Thanks for everyone who created an issue and reported bugs or suggested features!

The KOReader plugin finally has all the feature I originally wanted but were not that straight forward to Implement. Syncs are now downloaded seamlessly in the background - no need to manually press the sync button anymore! Also some other improvements to fix DNS Issues and upload progress on book exit, Menu restructure and more!
