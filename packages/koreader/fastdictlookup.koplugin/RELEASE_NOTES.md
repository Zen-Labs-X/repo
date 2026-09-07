# v1.5.0

Fix compatibility issues with new KOReader version 2026.07.

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.4.0...v1.5.0

# v1.4.0

* New Full Definition Lookup menu
* Put all settings in sub menu
* Add new settings
    * **Enable Highlighting** - if enabled, first tap on "ok" button will go into highlighting mode
    * **Override Default Lookup Menu** - if enabled, tapping the word will open full definition instead of opening the default KOReader's context menu

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.3.1...v1.4.0

# v1.3.1

Fix Footnote Lookup issues:
* Footnotes with h1..h6 headers were ignored due to excessive flag
* Plugin crashes on looking up HTTP/HTTPs links (now they are ignored)

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.3.0...v1.3.1

# v1.3.0

Features:
* Text Highlighting Mode: pressing the button now enables highliting mode, pressing it again opens context menu for the selected text

Fixes:
* Optimize page redraws by only repainting parts of the screen where the cursor is
* Avoid reading dictionary file twice when it has required metadata

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.2.0...v1.3.0

# v1.2.0

Features:
* Lookup footnotes when moving cursor over them

Fixes:
* Cursor and underline position for words with line breaks
* Don't render lookup widget when no definition found

**Full Changelog**: https://github.com/Sirozha1337/fastdictlookup.koplugin/compare/v1.1.1...v1.2.0
