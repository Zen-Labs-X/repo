# 0.4.0

## 0.4.0 (2026-04-26)

### Added

* Added option to show a confirmation when changing a book's currently read status to reduce misclick issues

# 0.3.1

## 0.3.1 (2026-02-18)

### Added

* Added support for [Updates Manager Plugin](https://github.com/advokatb/updatesmanager.koplugin) (min: v1.4.0)

### Fixes

* Fix page change gestures causing a refresh (even when there are no pages to navigate to) of the suggest a book, and
  book/edition linking dialogs

# 0.3.0

## 0.3.0 (2026-01-24)

This release restores a previously removed feature, 'suggest a book', with some new functionality. This displays a list of up to 10 books in random order from your Hardcover Want to Read list.

This was removed previously because of the lack of integration with KOReader. Now, tapping one of the suggested books will also start a file search for that book.

<img width="369" height="292" alt="Hardcover menu in KOReader, including the new option: Suggest a book" src="https://github.com/user-attachments/assets/9a6bdb42-953a-4935-9703-1477cd7bd60e" />
<img width="369" height="292" alt="Suggest a book dialog displaying several books from a to-read list. There is a refresh icon in the upper left corner" src="https://github.com/user-attachments/assets/486d955f-6d55-4bdb-aab0-8113a56748bc" />

### Added

* Added "suggest a book" to hardcover menu. Displays 10 books from your to-read list at random.
* Plugin will now consider the `hardcover-slug` ebook identifier in addition to `hardcover` identifier (
  by [@yd4dev](https://github.com/yd4dev))

## Fixes

* Fix page map crash when loading document formats that don't support page maps (like CBR)
* Fix page map crash when document is out of range of the active page map

# 0.2.0

## 0.2.0 (2025-11-22)

The 0.2  release changes the way publisher page numbers (if available) are used when updating reading progress. Previously, publisher page numbers were used to estimate a progress percentage, which was compared to the number of pages in the selected edition, and the resulting page number was sent to Hardcover. This was done to solve issues with non-numeric and non-linear page numbers in publisher page maps.

For books with page maps that closely matched the selected edition, this resulted in sometimes surprising progress updates that didn't match the current page at all, but the result could be even worse if the selected edition's page count was very different from the page map's.

In 0.2, when a book has publisher page numbers available and enabled, the plugin will do its best to use those page numbers directly when updating. This has some caveats:

* Pages read before "page 1" of the book (typically prologues and introductions) will be treated as page 1 when updating.
* Epilogue pages after the end of the book (which also may be non-numeric) will be treated as the number of pages in the edition.
* If the page map has fewer or more pages than the edition, reading progress in Hardcover may not have the most desirable page.
* There may be some odd page maps with no or limited _numeric_ page numbers which will probably not have good results.

This can mean that finished books don't reach 100%, or reach it too soon.

This is a compromise approach and has some negative tradeoffs compared to the previous implementation, but should be an overall improvement for most users.

However, if you don't like this behavior, you can disable publisher page numbers in KOReader (`Bookmark>Settings>Stable page numbers>Use stable page numbers` in 2025.10, or `Bookmark>Reference pages>Use reference page numbers` in previous versions), and the plugin will use the old system instead.

_Note: KOReader 2025.10 also adds stable page numbers based on a number of characters per page. These are ignored by the plugin._

---

### Added

* Publisher page labels will now be used for reading progress without translation
* Percentage calculation used to determine when to create new journal entries now uses the page
  label divided by edition page count. This is weird but ensures that journal reading percentage is close to the
  selected interval
* Plugin will now ignore page mapping if publisher page labels are disabled in KOReader 

### Fixes

* Switch to `socket.http` implementation to better support proxy usage

### Chores

* Fix zip release directory structure

# 0.0.13

## 0.1.3 (2025-09-10)

### 🚀 Added

* Register action to immediately update reading
  progress [#19](https://github.com/Billiam/hardcoverapp.koplugin/issues/19)
* Add event to open journal entry dialog [#27](https://github.com/Billiam/hardcoverapp.koplugin/issues/27)
