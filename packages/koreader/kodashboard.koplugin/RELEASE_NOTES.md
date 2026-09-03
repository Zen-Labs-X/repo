# v1.2.5

KoDashboard v1.2.5 (retry release)

Asset is minimal and includes only: _meta.lua, main.lua, dataloader.lua, api.lua, and web/.

# v1.2.4

KoDashboard v1.2.4

- Add Disconnect button in web UI to stop KoDashboard server remotely
- Fix Last open sorting stability after pull covers
- Restore calendar book cover mapping

Release asset includes only: _meta.lua, main.lua, dataloader.lua, api.lua, and web/.

# v1.2.3

KoDashboard v1.2.3

Performance and stability improvements focused on mobile stats loading:

- Reduced `/api/dashboard` compute cost to lower crash risk on large libraries.
- Added short-term dashboard caching to avoid repeated heavy recomputation.
- Limited expensive day-by-book aggregation to the recent 365-day window.
- Reworked hourly/monthly/weekday/top-book range calculations to reduce repeated SQL scans.
- Removed extra `books` fetch from Stats and Calendar views to reduce payload and memory pressure.

Packaging:
- Minimal release zip excludes screenshots.

# v1.2.2

README clarification, optional Pull Covers workflow, WebP cover storage, skipped-no-upload fix, and non-GIF upload restriction.

# v1.2.1

Add QR menu shortcut and remove auto-start
