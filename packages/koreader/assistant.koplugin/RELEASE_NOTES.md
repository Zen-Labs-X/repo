# v1.16

> ⚠️ **OTA Users: Please update twice — the first OTA loses translations, the second restores them.** Details below.

#### Highlights
Smarter context control, per-model tuning, and more resilient API handling.

#### What's New

**Context Management — New "Current Chapter Only" Option**
Context management in the Ask dialog now includes `Current Chapter Only`. When `Include Text Read So Far` is checked, you can limit context to the current chapter only (auto-detected via the book's Table of Contents). Great for focusing answers on the chapter you're reading. Hidden automatically if the book has no TOC. Thanks to @Vilhelm-Ian (#205).

**Per-Model Parameter Presets**
Configure separate `additional_parameters` (e.g. `temperature`, `max_tokens`, `reasoning`) for each model under the same provider via `model_parameters` in `configuration.lua`. Switching models via Settings → Browse Models applies the matching preset automatically; models without a preset keep the shared defaults. See `configuration.sample.lua` for examples. Thanks to @SUBHAM-ROY (#200).

**Automatic Retry on API 429 (Rate Limit)**
When the provider returns **HTTP 429 Too Many Requests** (rate limit / quota exceeded), the plugin now retries automatically — up to 8 times — respecting `Retry-After` headers, with exponential backoff and jitter. Works for both streaming and non-streaming requests. During streaming, a cancellable countdown `API Busy (429) — Attempts N/M` is shown.

#### Improvements & Fixes
- **Web Search compatibility** — Search tool renamed to `assistant_web_search` to avoid 400 errors on gateways (e.g. OneAPI) that filter the generic `web_search` name.
- **Dictionary accuracy** — Dictionary and Term X-Ray prompts now include book title/author and handle word forms better.
- **More robust streaming** — Ignore SSE `id:` fields to fix stray `id:0 id:1...` text with Qwen and other OpenAI-compatible models.
- **Settings dialog** — Browse Models failures no longer close the settings window.
- **Ask dialog polish** — Improved checkbox layout, separator, input height; reasoning blocks now wrap correctly.

#### Translations & Details
All 42+ languages updated. The plugin now reuses KOReader's native translation module directly instead of bundling a stale copy of `gettext` — only the adapter entry is customized — with translations shipped as compiled `.mo` files for faster loading. This format change is why OTA requires two passes; fresh installs via zip are not affected.

# v1.15

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

# v1.14

## v1.14 Release Notes

### Changes since v1.13

#### New Features
- **Bold dialog labels and status verbs via PTF** — Error dialogs, OTA update dialogs, and search info dialogs now use bold formatting for key labels, making them easier to scan at a glance.
- **Gemini 3 thinking budget auto-conversion** — The `thinking_budget` setting now automatically converts to Gemini 3's expected format. Disabled by default in the sample config.

#### Bug Fixes
- **Dictionary popup AI buttons** — AI buttons in the dictionary popup no longer disappear after customizing the dict button layout (#187).
- **Gemini thinking config** — Fixed `thinkingConfig` to use camelCase (required by Gemini API), and fixed a bug where `thinking_budget=0` was silently ignored instead of disabling thinking.
- **Server error messages** — Non-200 HTTP responses now surface the server's actual error message instead of a generic "fetchJSON: failed to parse" message.
- **Error dialog polish** — Error messages are now formatted with bold labels and clearer structure.
- **Silenced noise logs** — Unprocessed SSE event logs for `web_search_call` lifecycle events and Responses API annotation events are now suppressed.
- **OTA and search info dialogs** — Polished the layout and text of OTA update and search tool info dialogs.
- **PO file format** — Normalized `.po` file format to 1-space alignment, eliminating diff noise from `msgattrib -i` misuse.

#### Internal Improvements
- `assistant_utils` is now imported as `ASUtils` consistently across the codebase.
- String concatenation loops replaced with `string.buffer` / `table.concat` for better performance.
- OTA updater path construction routed through `FFIUtil.joinPath` for cross-platform safety.
- Gemini `thinking_budget` handling consolidated into a single handler.
- Bold formatting centralized through `bold_format` helper, keeping translatable strings contiguous.
- Removed unused shell translation script.

# v1.13

# v1.13 Release Notes

## Stream Response Performance

Streaming responses previously caused noticeable UI lag, especially on e-ink devices with limited refresh capabilities. Each token triggered a separate screen update, leading to choppy rendering and slow perceived response times.

This release introduces two performance improvements:

- **Coalesced UI updates**: Incoming stream content is now buffered and flushed to the screen at 500ms intervals instead of on every token. This dramatically reduces the number of screen redraws, making the reading experience much smoother and more responsive.
- **Cleaner reasoning separation**: When a model outputs its internal reasoning before the final answer, the UI now clears the reasoning content and starts the answer fresh, avoiding visual clutter and making the response easier to read.

## Cleanup

- Removed a long-unused plain-text rendering code path and the associated `render_markdown` configuration option (which was always effectively enabled). This simplifies the viewer code and eliminates dead code.

## Other Improvements

- Built-in prompt section headers (e.g. "What It Is", "Role & Function", "Evolution & Connections" in Term X-Ray, and similar headers in Grammar, ELI5, Key Points, and Historical Context prompts) are now localized. Users in supported languages will see these headers in their own language. All 40+ language translations have been updated.
- Fixed the Azure OpenAI sample endpoint URL in the configuration template.
- Internal naming improvements to reduce confusion between built-in and user-defined prompts.

---

**Stats**: 70 files changed, +41,440 / -32,086 lines (mostly translation updates).

# v1.12

# v1.12 Release Notes

We're excited to announce v1.12! This release brings web search tool calling, native Markdown rendering, over-the-air updates, and much more.

## Web Search Tool Calling (#180)

The assistant can now search the web to enrich its responses—especially useful for web novels, current events, and factual queries. It supports multiple search backends (SerpAPI, Tavily, SearXNG, and Exa), multi-round tool-call loops (up to 3 rounds), and works across all three wire formats (OpenAI, Anthropic, and Gemini).

When web search is configured, prompts that support web-powered queries will display a small globe icon (🌐) in the prompt menu, so you can tell at a glance which features benefit from live web access. Tasks like translation that don't need web search remain unaffected, so response speed is never compromised.

## Native Markdown Rendering with libhoedown

A bundled `libhoedown` native library now handles Markdown-to-HTML conversion, providing full support for tables, code blocks, and other advanced formatting. The plugin automatically detects the target architecture and falls back to KOReader's pure-Lua parser when the native library is unavailable.

## Over-the-Air Updates

The plugin can now check for and install updates directly from GitHub Repo. Head to the settings menu to check for new versions—no manual downloads needed.

## OpenAI Responses API

Support for OpenAI's `/v1/responses` endpoint has been added, enabling built-in web search, file search, and function-calling tools natively through the OpenAI API.

## Model Picker

A paginated, searchable model picker is now available for most API providers (OpenAI, Anthropic, Gemini, and compatible providers). You can browse and switch between available models directly from the UI without manually editing configuration files—just pick and go.

## Other Improvements

- **OpenAI thinking budget**: `enable_thinking` and `thinking_budget` options are now whitelisted for OpenAI-compatible providers (#182)
- **Handler architecture refactored**: provider handlers now use object-oriented settings, with a `SyncOptions` hook for per-request configuration
- **Gigachat** has been refactored to inherit from the OpenAI handler. Note: this change is untested by the maintainers due to lack of platform access; feedback from Gigachat users is welcome.
- **Performance**: optimized line processing in the streaming querier and adopted `string.buffer` for string concatenation
- **Reasoning text** support for models that emit thinking/reasoning content
- **Korean localization** synced with upstream KOReader translations

## Configuration: `base_url` Now Uses the True Base URL

The `base_url` field in `configuration.lua` now expects the actual API base URL (e.g., `https://api.openai.com/v1`) instead of the full `/chat/completions` endpoint. Existing configurations are still handled with backward compatibility—no immediate migration required—but updating to the new format is recommended for clarity.

## Bug Fixes

- Fixed crashes caused by config-only custom prompts (#183)
- Fixed pipe table rendering when libhoedown is unavailable (#176)
- Fixed markdown list bullets to use filled discs (#184)
- Fixed variable errors in the Gigachat handler
- Fixed Gemma handler metatable caching and dynamic inheritance
- Fixed model name overriding in the settings dialog
- Fixed prompt button updates when web search tools change

## Contributors

Thanks to everyone who contributed to this release:

- **boypt** — web search tool calling, OTA updates, libhoedown, Responses API, model picker, architecture refactoring, and many fixes
- **Charles Han** — markdown list bullet fix (#184) and custom prompt crash fix (#183)
- **Dávid Szakállas** — OpenAI thinking budget whitelist (#182)
- **Balmisjutas** — pipe table rendering fix (#176)

---

[Full changelog](https://github.com/boypt/assistant.koplugin/compare/v1.11...v1.12)
