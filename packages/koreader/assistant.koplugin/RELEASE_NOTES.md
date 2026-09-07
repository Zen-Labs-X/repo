# v1.17

> 📦 **Android users:** this release repairs the accelerated text renderer that was silently broken on Android — AI answers and dictionary results will render noticeably faster after updating.

#### Highlights
Do more from the screen: tune your AI providers, test them, and update the plugin — without opening a configuration file.

#### What's New

**Provider Setup, Now Fully On-Screen**
- **Reasoning Option** — dial back (or off) a model's "thinking" in one tap. The dialog shows only the choices your selected provider understands, applies immediately, and never touches your config file.
- **Test Connection** — probe a new provider right from the add/edit form; tells you instantly if the address, key, or model name is wrong, with the provider's own explanation (your key is never shown).
- **Cleaner provider management** — Add moved to the presets menu, Delete now lives inside Edit with a confirmation, simplified button row.
- **Better model picker** — title names the provider, "Manual" renamed to **Custom**, explicit **OK** to confirm.

**OTA Updates You Can Trust**
- The update dialog now pre-fills the right target for you: stable installs upgrade to the latest stable release by default, development installs stay on the bleeding edge — unless you explicitly type a different branch or tag to switch.
- New releases are checked quietly in the background (at most once per 48 hours) with a toast when one is out.
- Failed downloads are reported persistently instead of flashing by, Android installs are far more robust, and only the files the plugin actually needs are installed.

#### Improvements & Fixes
- **Your Ask dialog choices stick** — Web Search and Copy-to-Clipboard now keep their state after a restart instead of resetting.
- **Consistent dialog buttons** — confirm buttons are now uniformly **OK** across all dialogs instead of a mix of Save/OK.
- **Errors in plain language** — see what the provider actually said ("invalid API key", "model not found") instead of a raw data blob.
- **Quicker recovery from rate limits** — retries now wait at most 5 seconds (was up to a minute) and show the reason.
- **Follow-up suggestions per prompt** — each prompt decides whether the model offers follow-up questions, instead of one global switch.
- **Simpler config template** — fresh setups are built around four clearly-labelled service types; existing configs unaffected.
- **Cleaner debug logs** — verbose request data trimmed, so logs attached to bug reports stay readable.

#### Translations
All languages refreshed with the new on-screen settings.

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
