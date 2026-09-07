# v1.5.6

#v1.5.6 — Change in the Mihon hash extraction method

# v1.5.5

#v1.5.5 — Change in the Mihon hash extraction method

# v1.5.4

#v1.5.4 — Extract Preview & UX Improvements

## What's new

### Extract Metadata From Filenames — preview before extracting
Following a report of unformatted filenames losing book titles on extraction, the **Extract Metadata From Filenames** flow now shows a paginated preview of all parsed metadata before writing anything to disk. You can browse every file and verify what will be extracted, then confirm or cancel.

Preview format:
```
Death Note - Tsugumi Ohba - Death Note #1.cbz
  Title:  Death Note
  Author: Tsugumi Ohba
  Series: Death Note #1
```

Fields are only shown if present — files with just a title won't show empty Author/Series lines.

### Rename All Files in Folder — same preview layout + Preview-only flow
- The **Rename All Files in Folder** preview now uses the same field-per-line layout as the Extract preview, making it easier to spot parsing issues at a glance.
- The **"Rename All"** button has been removed from the form. Renaming now requires going through Preview first — the "Rename All" action only appears on the last preview page, after reviewing the full file list.

### Navigation
Both previews use the same consistent navigation pattern:
- **← Back** / **Cancel** on the left
- **Next →** / **Extract All** (or **Rename All**) on the right

# v1.5.3

## MetaFileExtract v1.5.3

**MENU**

* Now in Tools --> MetaFile Extraction

### New Features

**Decimal chapter support**

* `6.5.cbz` or `6,5.cbz` → Title `#6.5`, Series `#6.5`
* `Capítulo 6.5` and `Chapter 6.5` recognized
* Ignores Mihon/Tachiyomi hashes (`_c56fba`)

**Smart skipping**

* Files without changes are skipped
* Existing destination files are skipped
* Non-standard files left untouched

### Examples

**Title Before:** `6.5.cbz` → `7` (wrong order)  
**Series Number Before:** `6.5.cbz` → `7` (wrong order)  
**Title After:** `6.5.cbz` → `6.5`  
**Series Number After:** `6.5.cbz` → `6.5`

# v1.5.2

## MetaFileExtract v1.52

**New menu**
- Now in Tools --> MetaFile Extract

### New Features
**Decimal chapter support**
- `6.5.cbz` or `6,5.cbz` → Title `#6.5`, Series `#6`
- `Capítulo 6.5` and `Chapter 6.5` recognized
- Ignores Mihon/Tachiyomi hashes (`_c56fba`)

**Smart batch auto-fill**
- Scans folder for properly formatted files first
- Pre-populates Title, Authors, Keywords, Series
- Consistent results (alphabetical order)

**Full title control (context menu)**
- Title field = exact filename title (no auto `#number`)
- Separate series number field for sorting only

**Batch rename defaults**
- `#number` enabled by default (toggle on/off)

**Stability**
- Fixed ordering mode crashes
- Safe rename across filesystems (internal ↔ sdcard)

**Smart skipping**
- Files without changes are skipped
- Existing destination files are skipped
- Non-standard files left untouched

### Examples

**Before:** `ArinVale_Capítulo 58_92cb1b.cbz` → `#1`  
**After:**  `ArinVale_Capítulo 58_92cb1b.cbz` → `58`

**Before:** `6.5.cbz` → `7` (wrong order)  
**After:**  `6.5.cbz` → `6.5` (between 6 and 7)

**Batch rename:**
- `Mangá 6 - Author - Keyword - Series #6.cbz` → auto-fills all fields
- `chapter_extra.cbz` → ignored (no auto-fill, no changes)

### Supported formats
`cbz`, `cbr`, `epub`, `pdf`, `mobi`, `azw`, `fb2`, `djvu`, `zip`
