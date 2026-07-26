# KOAssistant v0.20.0 Release Notes

> **Settings reset recommended**. After updating, go to **Settings → Backup & Reset** and reset the Quick Actions panel, Quick Settings panel, and Input Dialog actions to pick up new defaults. Custom actions, API keys, notebooks, chats, and cached artifacts are not affected. Old reasoning settings are cleared on first launch (everything starts at the new "Default" stance; re-apply per-model preferences if you had custom setups); the chapter-quiz trigger level is reset once to the new default because the option meanings changed.

---

## Per-Book Settings

A single **Book Settings** screen collects every per-book override in one place, reachable from the file-browser long-press, the Quick Actions panel, and the input-dialog gear menu.

- **Per book:** domain, research mode, spoiler-free chat, book-info level (None / Title & author / + position), AI title & author (use real metadata, set a custom value, or send none), quiz behavior, and translation / dictionary / response languages.
- **"(N customized)"** indicator and a one-tap **Reset** so you can always see and clear what's been changed.
- Settings resolve **action > book > global**, so a book's preferences quietly override your defaults.

---

## Interactive Chapter Quizzes

Comprehension quizzes that trigger automatically at the end of each chapter, with a dedicated viewer.

- **Smart trigger:** fires on finishing a chapter, with substance gates (minimum chapter length and reading time) so short front-matter and tiny sections don't interrupt you. Configurable depth; per-book "Not for this book" / "Quiz settings…" controls.
- **Quiz viewer:** one question at a time: multiple-choice (auto-graded), short-answer and discussion (self-graded), score tracking, and a question picker. Answers persist: reopen to **Review** or **Take Again**.
- Robust against malformed model output (JSON repair), and cached as a reusable artifact (Copy / Export / Save to Notebook).

---

## Library & Reading Insights

Recommendations grounded in your actual library and reading habits, computed on-device.

- **Folder scanning:** point KOAssistant at your book folders to build a private catalog (title, author, status, series, progress). Triple-gated for privacy; raw data never leaves the device.
- **Library actions:** *Next Read*, *Discover New*, *Analyze Library*, and *Suggest from Library* (with an optional end-of-book suggestion popup).
- **Reading-stats engagement groups:** "deep reads", "recently finished", "stalled", and "briefly started" lists, computed locally from KOReader's statistics; only curated book lists are ever used, never raw stats.
- **Redesigned library dialog:** opens to actions (not a book picker), with a multi-book picker that switches between reading history and folders, plus search and filters. Cross-book **Notes Analysis** across your library.
- **File-browser actions read closed books:** actions run from the file browser can now use a book's highlights, annotations, notebook, and reading progress straight from its sidecar, no need to open the book first. The same privacy gating applies.

---

## Spoiler-Free Mode

Keep the AI from revealing anything past your current page. A global toggle plus an optional per-session checkbox; injects a spoiler-aware instruction (with your reading progress) into book/highlight chat. Also respected by the new AI Book Tools when reading the text.

---

## Reasoning, Reworked

Reasoning is now controlled **per model** instead of one global on/off switch.

- **Global stance dial:** Minimal / Default / Maximum, applied to each model as far as it allows.
- **Per-model overrides:** set effort/budget, on/off, or pin a model to its own **API default** regardless of the global stance; the per-model list shows both your setting and the effective state, and a Quick Settings chip shows the effective state at a glance.
- The Quick Settings reasoning popup can now reach **every model** (not just the active one) via its "Other models…" browser.
- Full support for adaptive thinking on **Claude Sonnet 5** and **Claude Opus 4.7 / 4.8** (including the sampling-parameter constraints those models require).
- Old reasoning settings are cleared on first launch; everything starts at the new "Default" stance, so re-apply per-model preferences if you had custom setups.

---

## AI Book Tools (Experimental)

Opt-in **`enable_tool_workflows`** lets the AI call local tools (search the text, read a page, view the table of contents) to ground its answers in what the book actually says. Works on **Gemini** and **Claude**; spoiler-free mode bounds what it can read. Off by default; behavior may still change. Requires "Allow Text Extraction"; responses don't stream while tools are running.

---

## New Provider & Model Updates

- **Requesty** added as a new OpenAI-compatible provider (now **19 built-in providers**).
- **Claude Sonnet 5** added as the new Anthropic default (Sonnet 4.6 remains available).
- Across-the-board mid-2026 model refresh (new OpenAI, Kimi, GLM, and Gemini entries; retired deprecated models). Custom models now appear at the top of the model list.

---

## Translations

- **Four new languages: Finnish, Bengali, Urdu, and Persian (Farsi)**, bringing the total to 24.
- Full refresh across all languages for this release's ~330 new and changed strings.
- Fixed translations silently falling back to English for strings containing newlines or quotes.
- As always, machine translations are marked "needs review"; corrections are very welcome on [Weblate](https://hosted.weblate.org/engage/koassistant/). Thanks to **Seruschl** (German) and **ferdinanlima** (Brazilian Portuguese) for their review contributions.

---

## Other Improvements

- **Data, Backup & Reset:** a single internal registry now tracks every file and setting the plugin owns, so resets and backups are consistent. New **"Validate Data Indexes"** tool under Backup & Reset repairs stale chat/artifact/notebook/pinned indexes on demand.
- **Long-press any action button** (input dialog, Quick Actions, highlight menu, file browser) to see what it does.
- **Research mode** can now be toggled manually from the Domain & Research picker (resolution: action > book > DOI auto-detection > global).
- New **"Re-run Setup Wizard"** under Backup & Reset; fixed the wizard stalling when the language picker was dismissed.
- **Enhanced text selection** in KOReader's dictionary and text-viewer popups (opt-in).
- New context placeholders for custom actions: **`{page_text}`** (current visible page) and **`{page_number}`**.
- New **"Up to current position (NN%)"** scope in the source/scope picker for whole-document actions.
- **Dictionary popup** updated for KOReader's new button API (works on current and older KOReader).
- Web-search controls are now shown only for providers that actually support it, with honest on/off state.

---

## Stability & Performance

- **No more UI freezes on slow/flaky Wi-Fi:** removed blocking DNS checks from every interaction; dialogs now open instantly offline, with the Wi-Fi prompt deferred to send time.
- **Faster startup:** removed eager module loading and chat-index validation from the launch path.
- **Lighter update checks:** the auto update check now runs at most once a day (instead of every start), fetches a much smaller payload, waits until startup rendering is done, and reports clearer errors when GitHub is unreachable.
- Fixed **macOS** subprocess networking hangs (DNS-after-fork).
- Fixed a **crash when deleting a book** that had KOAssistant data.
- **Boox / Snapdragon (Adreno) devices:** worked around a GPU-driver crash on background requests. The durable fix is in recent KOReader builds; updating KOReader is recommended.

---

## Action Changes

- New built-in **News Update** action (general chat): fetches today's top stories via web search, with headlines, summaries, and links.
- **Explain** no longer performs web search by default (#75).
- Domain context enabled for six reading-analysis actions; the `reader_assistant` behavior override was removed from seven built-ins (they now follow your selected behavior).
- Renames: "Library Actions" → **"Library Chat/Action"**; quiz "Essay" → **"Discussion"**.
- Prompt-quality improvements across several built-in actions.

---

## Bug Fixes

- **Fixed a serious data-loss race** where saving a response to a note (or saving a chat) while the book was open could revert the book's highlights, annotations, and reading progress (#72).
- Fixed library chats silently losing messages on resume, and manual library-chat saves misrouting into general storage.
- Fixed pinned artifacts being permanently lost when a pinned result ended in a tricky bracket sequence.
- Fixed a crash in the starred-chats browser menu.
- **Privacy hardening:** cached artifacts now remember whether your highlights went into them and stop re-sending that data once you revoke sharing, including on incremental "Update to X%" runs; the trusted-provider bypass is now evaluated against the provider an action *actually* sends to (not the global one) when an action pins its own provider.
- Local providers set up via Quick Setup (LM Studio, llama.cpp, …) no longer wrongly require an API key.
- Fixed a fresh-install crash that silently disabled the plugin when `configuration.lua` had no `features` table.
- Spoiler-free mode no longer leaks its instruction into predefined actions or artifact chats.
- A missing or unplugged scan folder (e.g. a removed SD card) no longer crashes library actions.
- Fixed X-Ray highlight search crashing on recent KOReader nightlies.
- Streaming errors from local providers are now shown as errors instead of being saved into the chat as the AI's answer.
- Fixed continue-chat sending the placeholder API key instead of your configured key (401 errors).
- Fixed `configuration.lua` overrides not always taking effect, and added an error notice when `configuration.lua` fails to parse.
- Fixed Groq HTTP 400/413 on X-Ray/Recap: output-token clamps for Groq models plus a clear size-limit hint when a provider rejects an oversized request (#89).
- Fixed a crash in the trusted-providers dialog.
- Fixed HTTP 400 when enabling reasoning on GPT-5.4 (missing temperature constraint).
- Fixed garbled (non-JSON) API error messages on e-ink / non-macOS devices, and mid-stream error detection.
- Fixed subprocess networking on dual-stack (IPv4/IPv6) networks.
- API keys entered in the GUI are now trimmed of accidental whitespace.
- Copying a book (not just moving it) now brings its KOAssistant sidecar data along.
- Hardened X-Ray and quiz JSON parsing against malformed model output.
- Numerous smaller fixes across chat, artifacts, and providers.

---

## For Custom Action Users

- New **`{page_text}`** / **`{page_text_section}`** and **`{page_number}`** placeholders are available in any action.
- New library placeholders: **`{library}`** / **`{library_section}`** and the engagement groups (**`{deep_reads_section}`**, **`{recently_finished_section}`**, **`{stalled_section}`**, **`{briefly_started_section}`**), gated by the new `use_library` / `use_advanced_stats` flags; plus **`{spoiler_free_nudge}`** for spoiler-aware prompts.
- The action-creator wizard is now **3 steps** (domain selector built in; behavior moved to Advanced); the confusing "both" compound context was removed from the wizard.
- The new **"Up to current position"** scope works for whole-document actions in the source picker.

---

## What's Changed
* Library redo by @zeeyado in https://github.com/zeeyado/koassistant.koplugin/pull/60
* Disable web search for Explain action by @LK4D4 in https://github.com/zeeyado/koassistant.koplugin/pull/75
* Add Requesty as an OpenAI-compatible provider by @Thibaultjaigu in https://github.com/zeeyado/koassistant.koplugin/pull/88

## New Contributors
* @LK4D4 made their first contribution in https://github.com/zeeyado/koassistant.koplugin/pull/75
* @Thibaultjaigu made their first contribution in https://github.com/zeeyado/koassistant.koplugin/pull/88
* @schuay made their first contribution in https://github.com/zeeyado/koassistant.koplugin/issues/79

**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.19.1...v0.20.0
