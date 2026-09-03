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

# v0.2.5

**Full Changelog**: https://github.com/jadehawk/libby-dashboard.koplugin/compare/v0.2.4...v0.2.5

# v0.2.4

**Full Changelog**: https://github.com/jadehawk/libby-dashboard.koplugin/compare/v0.2.3...v0.2.4

# v0.2.3

**Full Changelog**: https://github.com/jadehawk/libby-dashboard.koplugin/compare/v0.2.2...v0.2.3

- HOTFIX. Error 502 was preventing ACSM download on certain internet connections.
