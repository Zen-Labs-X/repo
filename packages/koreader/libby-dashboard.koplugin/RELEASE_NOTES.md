# v0.2.8.1

## Version 0.2.8.1

### Added
- Added dedicated **Magazine Rack** and **Audiobooks** views.
- Magazine Rack now includes both checked-out issues and magazines followed through Libby subscriptions / Notify Me.
- Added automatic magazine cover retrieval for subscription-only issues.
- Added magazine frequency labels such as **Weekly** and **Monthly**.
- Added persistent **NEW ISSUE** indicators when a subscribed magazine receives a newer issue.
- Added library-name sections inside Magazine Rack and Audiobooks when items come from multiple libraries.

### Changed
- Replaced the old dashboard/book-card home screen with the full **Library Browser** as the main plugin interface.
- The browser now remembers the last selected library/rack and Grid/List view, while reopening on page 1.
- Reorganized the browser header to **Swap · Library/Rack · Holds · Refresh · Settings · Grid/List · Close**.
- **Close** now exits Libby Dashboard directly.
- Audiobooks now display **Listen on Libby** instead of Read on Libby.
- Magazine list rows now show **Edition** or **Published date** instead of an `N/A` author.
- Cleaned up the old `expanded` browser architecture and migrated existing settings automatically.

### Fixed
- Fixed Kindle and other non-touch D-pad navigation, including a key-dispatch conflict that could cause every D-pad button to activate the currently selected control.
- Fixed initial D-pad focus so navigation begins on library items rather than becoming trapped in Settings.
- Fixed D-pad navigation across library sections in Magazine and Audiobook racks.
- Fixed Libby magazine subscription discovery for accounts where Notify Me stores current issue IDs instead of parent magazine IDs.
- Fixed magazine subscription refresh so tag-based subscriptions are fetched during normal Refresh.
- Fixed missing covers for magazines that are subscribed to but not currently checked out.

### Tested on
KOReader emulator and **Kindle 4th Generation non-touch**, including D-pad navigation, Settings, account-backup restore, Libby library restoration, and ByteBooks authorization restoration.

# v0.2.8

### Version 0.2.8

**Added**
- Added full **D-pad navigation** for library grids, lists, book details, actions, and actionable header icons.
- Added persistent **Book Notes** for all titles. Notes remain attached to a book as it moves from Hold → Borrowed → Downloaded/Open.
- Added direct **Borrow** support for available holds.
- Borrowing from the plugin now automatically **downloads the newly borrowed book** when possible.
- Added expanded Hold details including queue position, estimated wait, copies, suspension state, and availability.
- Added the new **Swap Library** action in expanded view to cycle through individual libraries and **All Libraries**.

**Changed**
- Redesigned book detail cards with compact metadata, properly aligned covers, a dedicated Book Notes section, and cleaner action spacing.
- Expanded-library header now uses **Swap** in place of Settings and supports D-pad focus for every actionable icon.
- Cover labels now describe the book current state instead of the next action: loan time remaining, **Expires Today**, **Extended Loan**, **Ready to borrow**, queue position and estimated wait, **Suspended**, or **Read on Libby**.
- Expanded List view now dynamically reserves enough space for longer status labels such as **#1000 in line · 365 days**.
- Improved Hold and loan layouts across grid and list views.
- Improved update/version handling in preparation for future four-part releases.

**Fixed**
- Fixed clipped Hold/status labels in expanded List view.
- Fixed excessive whitespace and inconsistent spacing in book detail cards.
- Fixed cover alignment and top-padding issues in Hold and non-Hold detail cards.
- Fixed header separator artifacts introduced by D-pad focus borders.
- Fixed several fulfillment and state-handling edge cases for EPUB/PDF downloads.

**Versioning**
- **0.2.8 is the final three-part release.**
- Future releases will use four-part versions such as **0.2.8.0**.

# v0.2.7

# Libby Dashboard v0.2.7

## Compatibility Bridge Release

This release republishes the v0.2.6.1 code as **v0.2.7** so users still running **v0.2.6** can update successfully through the built-in updater.

The updater shipped in v0.2.6 only accepted three-part GitHub release tags (`x.y.z`) and therefore rejected `v0.2.6.1` with **“Latest GitHub release has an invalid version tag.”** After updating to v0.2.7, the plugin supports both three-part (`x.y.z`) and four-part (`x.y.z.w`) version formats for future releases.

## Highlights

- Added full **Grid** and **List** expanded library views.
- Added **Holds** support, including filtering held titles and cancelling holds.
- Added **Extended Loan Time** support and made it enabled by default.
- Added a redesigned **Library / Shelves** settings page with live layout preview.
- Updated the header toolbar with a consistent icon set and uniform icon sizing.
- Added support for four-part plugin versions such as `0.2.6.1`.

## Library and Shelf Views

- Added expanded **Grid View** for browsing book cards.
- Added expanded **List View** for a denser book listing.
- Added configurable layout controls for:
  - Main UI shelf columns and rows.
  - Expanded Grid columns and rows.
  - Expanded List rows per page.
- Layout changes preview immediately while editing settings.
- The **Save** button is now disabled and gray until a change is pending.
- Saving settings immediately returns the Save button to its disabled state.
- Improved library selector sizing and truncation so book counts remain visible.
- Improved long library-name fitting in expanded headers.
- Refined book-card spacing, typography, expiry information, and expanded-view layout.

## Holds

- Added retrieval and display of held titles alongside loans.
- Held books are identified with an **On Hold** status.
- Added a dedicated **Holds** filter in Grid/List mode.
- Added **Cancel Hold** support.
- Added a dedicated calendar-style Holds icon to the expanded header.

## Extended Loan Time

- Added **Extended Loan Time** handling for eligible downloaded titles.
- Extended Loan Time is now **enabled by default**.
- Existing saved user settings are still respected.
- Kept explicit **Return Early** behavior separate from extended-loan handling.

## Header and Icon Improvements

- Added a consistent plugin-local SVG toolbar icon set for:
  - Settings
  - Holds
  - Refresh
  - List
  - Grid
  - Close
- Added the **Settings** icon to Grid/List headers for consistency with the Main UI.
- Replaced the previous text-based Holds control with the new Holds icon.
- Updated the Refresh icon to the new reload-style artwork.
- Replaced the previous Grid artwork with the new matching Grid icon.
- Added a matching List icon.
- Main UI Settings, Refresh, and Close icons now use the same uniform size as Grid/List mode.

## Settings UI

- Added the dedicated two-column settings layout.
- Improved Library / Shelves organization and controls.
- Child settings flows now return to the settings dialog instead of closing it unexpectedly.
- Shelf and expanded-view configuration can be previewed before being saved.

## Versioning and Updates

- Plugin version updated to **0.2.7**.
- v0.2.7 is a compatibility bridge for users on v0.2.6 whose older updater cannot parse four-part GitHub release tags.
- Added four-part version parsing and comparison (`x.y.z.w`) while retaining support for three-part versions.
- Updated the in-plugin updater to recognize four-part GitHub release tags.
- Updated the GitHub release workflow to validate either `x.y.z` or `x.y.z.w`.
- Updated README version synchronization to support both formats.
- Release tags must exactly match the version in `_meta.lua`, e.g. `v0.2.7` or a future `v0.2.7.1`.

## Validation

- Added regression coverage for:
  - Four-part version handling.
  - Holds.
  - Extended Loan Time.
  - Protected EPUB extended-loan behavior.
- Full Lua 5.1 test suite passes for this release.

# v0.2.6.1

# Libby Dashboard v0.2.6.1

## Highlights

- Added full **Grid** and **List** expanded library views.
- Added **Holds** support, including filtering held titles and cancelling holds.
- Added **Extended Loan Time** support and made it enabled by default.
- Added a redesigned **Library / Shelves** settings page with live layout preview.
- Updated the header toolbar with a consistent icon set and uniform icon sizing.
- Added support for four-part plugin versions such as `0.2.6.1`.

## Library and Shelf Views

- Added expanded **Grid View** for browsing book cards.
- Added expanded **List View** for a denser book listing.
- Added configurable layout controls for:
  - Main UI shelf columns and rows.
  - Expanded Grid columns and rows.
  - Expanded List rows per page.
- Layout changes preview immediately while editing settings.
- The **Save** button is now disabled and gray until a change is pending.
- Saving settings immediately returns the Save button to its disabled state.
- Improved library selector sizing and truncation so book counts remain visible.
- Improved long library-name fitting in expanded headers.
- Refined book-card spacing, typography, expiry information, and expanded-view layout.

## Holds

- Added retrieval and display of held titles alongside loans.
- Held books are identified with an **On Hold** status.
- Added a dedicated **Holds** filter in Grid/List mode.
- Added **Cancel Hold** support.
- Added a dedicated calendar-style Holds icon to the expanded header.

## Extended Loan Time

- Added **Extended Loan Time** handling for eligible downloaded titles.
- Extended Loan Time is now **enabled by default**.
- Existing saved user settings are still respected.
- Kept explicit **Return Early** behavior separate from extended-loan handling.

## Header and Icon Improvements

- Added a consistent plugin-local SVG toolbar icon set for:
  - Settings
  - Holds
  - Refresh
  - List
  - Grid
  - Close
- Added the **Settings** icon to Grid/List headers for consistency with the Main UI.
- Replaced the previous text-based Holds control with the new Holds icon.
- Updated the Refresh icon to the new reload-style artwork.
- Replaced the previous Grid artwork with the new matching Grid icon.
- Added a matching List icon.
- Main UI Settings, Refresh, and Close icons now use the same uniform size as Grid/List mode.

## Settings UI

- Added the dedicated two-column settings layout.
- Improved Library / Shelves organization and controls.
- Child settings flows now return to the settings dialog instead of closing it unexpectedly.
- Shelf and expanded-view configuration can be previewed before being saved.

## Versioning and Updates

- Plugin version updated to **0.2.6.1**.
- Added four-part version parsing and comparison (`x.y.z.w`) while retaining support for three-part versions.
- Updated the in-plugin updater to recognize four-part GitHub release tags.
- Updated the GitHub release workflow to validate either `x.y.z` or `x.y.z.w`.
- Updated README version synchronization to support four-part versions.
- Release tags must exactly match the version in `_meta.lua`, e.g. `v0.2.6.1`.

## Validation

- Added regression coverage for:
  - Four-part version handling.
  - Holds.
  - Extended Loan Time.
  - Protected EPUB extended-loan behavior.
- Full Lua 5.1 test suite passes for this release.

# v0.2.6

**Full Changelog**: https://github.com/jadehawk/libby-dashboard.koplugin/compare/v0.2.5...v0.2.6
