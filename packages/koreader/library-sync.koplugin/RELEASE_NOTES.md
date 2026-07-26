## Changes
- Add a manual Bookshelf integration action for uploading local author images to BookOrbit.
- Match exact author names, BookOrbit sort names, reversed name order, and Bookshelf slugs.
- Upload only when the BookOrbit author has no image; existing server images are never overwritten.
- Skip ambiguous author matches and report them in the completion summary.
- Stream multipart image uploads to keep memory use low on e-readers.
- Document the migration workflow from Grimmory author images to BookOrbit.

## Requirements
- The configured BookOrbit account must have permission to edit metadata.

## Verification
- luajit tests/provider_contract_spec.lua
- lua tests/provider_contract_spec.lua
- luac syntax validation for plugin and test files
- git diff --check
- ZIP integrity and directory-layout checks for both OTA assets