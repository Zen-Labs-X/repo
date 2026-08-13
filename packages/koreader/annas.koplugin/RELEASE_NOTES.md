This update separates the underlying code forked from the ZLibrary KOReader plugin and fixes issues with invalid server response handling:


Fixes compatibility issues when both ZLibrary and Annas plugin are installed.
Fixes issue where language filter is ignored. Thanks to @LaiKash
Fixes issue where format filter is ignored.
Fixes issue where format of search result is not shown.


Please note that the associated plugins dispatcher action was renamed in this process, which might lead to your saved gestures / shortcuts connected to this plugin to be silently deleted. Please check and rebind them to this plugin.

**Full Changelog**: https://github.com/fischer-hub/annas.koplugin/compare/v0.1.8...v0.2.0