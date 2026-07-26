# KOReader Assistant Plugin: v1.11 Release 

This release focuses on optimizing performance, expanding model provider support, improving UI responsiveness, and fixing several edge-case bugs.

## Key Highlights

### 🤖 New Providers & Model Options

* **OpenRouter Model Picker:** Introduced a fully dynamic on-device UI model picker for OpenRouter with responsive sizing, page-forward shortcuts, and better model ID visibility.
* **DeepSeek:** Added official support for DeepSeek's **Thinking Mode** parameter.
* **Google Gemma:** Added a dedicated Gemma handler featuring automatic API detection and dynamic `<thought>` tag filtering for Gemma 4 models.
* **New APIs:** Added integrated support for **Perplexity**, **GigaChat**, and Anthropic web search capabilities.

### 🚀 Performance & Network Optimizations

* **Gzip Compression:** Implemented gzip compression across model fetching, update checking, and OpenRouter api workflows (leveraging `libz`), significantly decreasing data payload sizes and accelerating model list loading times.
* **Parallel API Requests:** Improved localization/makefile processing with parallelized API calls.
* **Algorithm Upgrades:** Integrated major optimizations for **Lexrank** to improve text summarizing efficiency.

### 🎨 UI & UX Improvements

* **KOReader Compatibility:** Refactored the dictionary popup buttons to support the latest KOReader API (PR #15184+) while maintaining seamless backward compatibility with older versions.
* **Dialog Enhancements:** Added a dedicated close button (top-right cross) to the "Ask Another" dialog and resolved query animation flashing issues.
* **Clipboard Sync:** Added support for copying inputs to the clipboard for built-in system prompts.

### 🐛 Bug Fixes & Stability

* **Encoding Robustness:** Fixed UTF-8 encoding issues post-text truncation by cleaning up orphaned continuation bytes via `util.fixUtf8()`.
* **Reliability:** Resolved a critical application crash that occurred when `configuration.lua` was missing.
* **Flow Correctness:** Fixed a bug where follow-up questions were dropped after running X-Ray or Recap operations.

---
## What's Changed
* Optimize Lexrank by @michael-kucek in https://github.com/omer-faruq/assistant.koplugin/pull/154
* Add supports for GigaChat API by @wellWINeo in https://github.com/omer-faruq/assistant.koplugin/pull/158
* Add model picker UI for OpenRouter model selection by @Agnesor in https://github.com/omer-faruq/assistant.koplugin/pull/169
* Update configuration.sample.lua by @stevesbrain in https://github.com/omer-faruq/assistant.koplugin/pull/166
* fix: remove query animation that caused flashing by @dreamtigers in https://github.com/omer-faruq/assistant.koplugin/pull/175

## New Contributors
* @wellWINeo made their first contribution in https://github.com/omer-faruq/assistant.koplugin/pull/158
* @stevesbrain made their first contribution in https://github.com/omer-faruq/assistant.koplugin/pull/166
* @dreamtigers made their first contribution in https://github.com/omer-faruq/assistant.koplugin/pull/175

**Full Changelog**: https://github.com/omer-faruq/assistant.koplugin/compare/v1.10...v1.11