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