## v1.15 Release Notes

### Changes since v1.14

This is a usability-focused iteration around provider setup, web search, and prompt context.

#### Highlights

- **UI-managed Provider Keys — zero-config start** — After installing from the KOReader Plugin Store, you can configure everything directly in the UI. No `configuration.lua` editing required. Add, edit, and delete custom providers in Settings, with `display_name`, built-in presets, and per-handler **Browse Models** (fetches via the handler's own `FetchModels`). The plugin also starts cleanly with no file-based config at all.
- **Web search configuration UI** — Web search moves from config file to UI: manage multiple search APIs, long-press to edit/delete, and see configured state at a glance via menu icons. The Ask dialog now has a dedicated **Use web search** checkbox.
- **Notebook & context improvements** — Multiple general notebooks with a folder picker and dedicated settings submenu. Prompts can now optionally include **book metadata** and **nearby page text** as context, with related settings regrouped for clarity.
- **Settings & menu polish** — Reorganized menus, unified Title Case labels, dynamic navigation, and conditional display of Custom Prompts.

#### Fixes & Improvements

- Fixed ~20s delay before the Wi-Fi prompt on every AI action; consolidated `runWhenOnline` handling across 21 call sites.
- Fixed forwarding of the `thinking` parameter to OpenAI-compatible handlers, `null tool_calls` crashes, Gemini OpenAI-compat response tolerance, and OpenRouter model filtering via `/models/user`.
- Improved stream error handling (surface server messages), auto-scroll behavior, and Responses API `reasoning_summary` handling.
- Hardened `ai_translate.py` and `l10n/Makefile` (now fails on `.po` syntax errors).
- Added headless test framework and `wbuilder` UI preview tooling.

#### Thanks

Special thanks to contributors in this cycle:

- @SUBHAM-ROY — web search toggle for Ask, OpenRouter guardrail-aware model filtering
- @jdbway — Wi-Fi delay fix (#197)
- @anhnn2010 — multiple general notebooks (#192)
- @Craftwork2720 — `thinking` parameter forwarding (#188)

And everyone who helped with translations, feedback, and testing.
