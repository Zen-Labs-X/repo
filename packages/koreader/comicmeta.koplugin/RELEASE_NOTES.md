# v2.0

## 📢 What's Changed

### ✨ New Features 
- Support for `.cbr` files has been added, as well as switching to the new `ffi/Archiver` module.
- Extraction is now done in the background.
- Extraction progress is now displayed to the user, and can be aborted.

### 👩🏻‍💻 Backend
- Comic parsing logic has been migrated to [KORComic/comiclib](https://github.com/KORComic/comiclib/), allowing its use in multiple plugins.

### 🔧 Fixes
- Support for uppercase, lowercase, and mixed-case files has been added.
- Change language to be more exact, using `Extract Comic Meta` instead of `Get Comic Meta`.

📜 **Full Changelog**: https://github.com/KORComic/comicmeta.koplugin/compare/v1.2...v2.0

![kusuriya-no-hitorigoto-apothecary](https://github.com/user-attachments/assets/d1ee0ca5-bd83-409b-b70c-a34e90740f40)

# v1.2

## What's Changed
* feat(comicmeta): add recursive .cbz file processing and tests by @OGKevin in https://github.com/NightQuest/comicmeta.koplugin/pull/10
* feat(comicmeta): add custom ToC generation from ComicInfo.xml pages by @OGKevin in https://github.com/NightQuest/comicmeta.koplugin/pull/11


**Full Changelog**: https://github.com/NightQuest/comicmeta.koplugin/compare/v1.1...v1.2

# v1.1

## What's Changed
* fix: rename xml to comicxml by @OGKevin in https://github.com/NightQuest/comicmeta.koplugin/pull/9


**Full Changelog**: https://github.com/NightQuest/comicmeta.koplugin/compare/v1.0...v1.1

# v1.0

Initial Release.

Special thanks goes to @OGKevin for #3 and #4
