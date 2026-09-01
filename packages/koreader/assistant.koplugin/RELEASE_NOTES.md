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
