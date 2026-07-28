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