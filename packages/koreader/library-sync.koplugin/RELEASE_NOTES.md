# v0.7.0

## What's new

- Add first-class CBZ manga/comic support for Grimmory and BookOrbit OPDS libraries.
- Preserve CBZ extensions across folder routing and every file-naming profile.
- Support CBZ files in missing-book sync, metadata refresh, Mirror cleanup and restore, and BookOrbit local registration.
- Prevent EPUB and CBZ files from being mistaken for one another during matching or replacement.
- Update the README and installation guide for EPUB/CBZ libraries.

Both ZIP assets are included for new and legacy OTA installations.

# v0.6.12

Fixes the BookOrbit reconciliation confirmation crash caused by a Lua gettext name collision. Also adds a regression guard preventing ignored return values from shadowing the translation function. Existing batched registration and reading-status protection remain unchanged.

# v0.6.11

## BookOrbit reconciliation crash hotfix
- Limit BookOrbit state transactions to batches of 100 files to avoid large transient allocations on Android.
- Add guarded UI stages so ordinary reconciliation errors are logged and reported without crashing KOReader.
- Requeue uncommitted files safely after a failed state batch.

## Verification
- Regression test confirms 205 links are committed as 100 + 100 + 5.
- Lua and LuaJIT provider contract tests.
- Full Lua syntax validation and both OTA ZIP integrity checks.

# v0.6.10

## BookOrbit file registration
- Automatically register verified EPUB downloads and metadata replacements in the BookOrbit plugin state.
- Add **BookOrbit integration -> Register existing Library Sync books** for previously downloaded files.
- Preserve exact BookOrbit book and file/edition IDs from OPDS, with match API fallback for older manifests.
- Reconciliation does not open books or change reading status.

## Verification
- Lua and LuaJIT provider contract tests.
- Full Lua syntax validation.
- OTA ZIP integrity and directory-layout validation for both current and legacy plugin names.

# v0.6.9

## Metadata refresh safety hotfix
- Stop metadata refresh before replacing files when configured BookOrbit/Grimmory API metadata cannot be loaded.
- Reject incomplete paginated BookOrbit API responses and unexpectedly low OPDS-to-API match coverage.
- Require a second confirmation before an unusually large manual metadata refresh.
- Stop unusually large automatic refresh queues and direct the user to review them manually.
- Keep `Sync missing books` able to continue without optional API metadata.

## Verification
- Regression coverage for API failure, incomplete API pagination, low metadata match coverage, and large queue detection.
- Lua and LuaJIT contract tests.
- Full Lua syntax validation.
- ZIP integrity and directory-layout validation for both OTA assets.
