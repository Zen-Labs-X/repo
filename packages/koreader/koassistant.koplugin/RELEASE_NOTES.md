# KOAssistant v0.21.1 Release Notes

⚠ You may have to install this fix manually ⚠

This is a maintenance release to v0.21.0 that fixes the broken updater. Release notes for v0.21.0 below.

You can update manually or by using one of the functioning Store plugins, like StoreFront or AppStore.

## Hotfix (v0.21.1)

- **One-tap update crashed with a luajit error on current KOReader builds** (`attempt to call method 'unpackArchive'`). KOReader removed that API in its mid-2026 releases; the updater now uses KOReader's current extraction API and falls back to the old one on older KOReader versions, so both work.
- **If tapping "Update Now" gives you that luajit error** (updating from v0.21.0 or earlier on a recent KOReader): the crash is in the previously installed updater, so update manually this once — download `koassistant.koplugin.zip` from the release page, extract, and manually copy it over `plugins/koassistant.koplugin`, replacing existing files (you will not lose any settings or user files). One-tap updates work again from then on. On older KOReader versions, one-tap update works as before.

---

# KOAssistant v0.21.0 Release Notes

> **Defaults changed in this release.** Spoiler protection is now **on by default** (details below). X-Ray entity marking in the book text and exact-match lookup routing are on by default; short answers from a few quick actions now open in a small anchored popup by default; AI Book Tools is now **off** by default (the Tools chip turns it on per chat). The highlight menu and input dialogs were re-curated for fresh installs — existing users keep their configured lists; to pick up the new menu defaults use **Settings → Backup & Reset → Reset Settings → Custom reset** and tick only the action menus (note: the "Actions only" quick reset also deletes custom actions you created). API keys, notebooks, chats, and cached artifacts are not affected by any of this.

---

## OpenAI Subscription 

You can now use a ChatGPT plan without an API key, via device login — verified working on free accounts too. Web search and book tools included. Thanks to @bmanturner.

## Spoiler Protection (On by Default)

Spoiler protection is now ON by default: chats are told not to reveal events past your reading position, and X-Ray checkpoint updates follow your position instead of installing the newest version. Turn it off globally in Settings > Chat & Export > Spoiler Protection, per book in Book Settings, or per chat with the Spoiler chip. With protection off, a new Book Settings row ("X-Ray updates: Follow my position") still keeps X-Ray updates position-bound if you prefer.

- Renamed everywhere from "spoiler-free chat" to **Spoiler Protection**; one posture now drives both the chat layer and the X-Ray install layer.
- A book marked **Finished** in KOReader stands protection down automatically; research mode does too (both are labelled in Book Settings, never hidden).
- The protection follows you live: it re-checks your position and posture at every reply, so a running chat respects where you are now, not where you started it — and your position is only disclosed when Basic Stats sharing allows it.
- Scope popups pre-select "Up to current position" under protection, and running a scope that covers unread text always asks first.
- Surrounding context for highlights is clamped under protection (nothing past your selection's paragraph by default, configurable).

## X-Ray, Reworked

The largest feature block of the release. X-Ray grows from a static artifact into a system that follows your reading.

**Automatic checkpoints (#73).** X-Rays can now build in the background as you read: a ladder of versions at configurable spacing (global formula, per-book override, snapped to chapter ends). Under spoiler protection the installed version follows your reading position; with protection off it installs newest-first. Extend, rebuild, or one-shot to a target coverage; interrupted builds resume; archived versions are browsable and restorable, and rebuilds carry forward cross-book knowledge instead of destroying it.

**Entities marked in the book text (#78).** Known entity names get a dotted underline as you read (configurable density ladder, people/places family filter, per-book overrides). Tapping a mark opens an **entity card**: a one-line identification in a footnote panel or a small popup anchored at the word, with the full entry one tap away. Entities known only to a checkpoint built ahead of you mark as dashes and carry a spoiler warning on their card.

**Selections open entries (#63).** Selecting or dictionary-looking-up text that exactly matches an entity's name or alias opens its X-Ray entry instead of the dictionary (on by default; opt out globally or per book; a very long press always gets you the normal menus). No-hit lookups can add the selection as an alias of an existing entry.

**Mentions and appearances.** Every entity gets a chapter-by-chapter appearance tree in the shape of your table of contents, with counts and comparison bars, plus mention lists that jump straight into the book at each occurrence via KOReader's native search session, with a floating button back to the X-Ray.

**Entity management.** Rename entries, merge duplicates (with a duplicate scan), mark pairs never-merge, link an entry with a group member's entry across books, browse a per-entity history across checkpoint versions, and manage entities carried in from earlier books.

**Category presets.** New X-Rays can be narrowed to what you care about: people / places / ideas / terms / events, as a global default and per book, with the prompt assembled to match ("Character tracking" makes a much cheaper X-Ray for long novels).

Plus: an X-Ray chats row in the browser, honest update-size trimming for long books, alias-aware merges, and a long tail of prompt-quality work (identity bridges, staleness rules, naming consistency across a series).

## Book Groups & Series (#90)

- Create named, **ordered** book groups: reading order is spoiler order, and it drives everything downstream. Groups can be created from a folder in one step, or suggested from a book's series metadata with a "find the rest" scan of a folder or collection.
- **Cross-book knowledge:** merge or fold X-Rays along the series; entities carry forward and wait in a "Carried from earlier books" list, waking automatically when they appear in the new book; shared naming keeps recurring entities under one name from birth.
- Group kinds (series / project / plain) tune what carries; per-group ordering toggle; group navigation from viewers and member popups.

## Book Hub

One full-screen page per book: every artifact with live status, chat, chat history, notebook, group, and book settings in one place. Reachable from the file-browser long-press, the main menu, a gesture, the Quick Actions panel, and every View Artifacts popup.

## Image Generation (#96)

Turn a highlight into an image: a new **Generate Image** action renders your selection via OpenAI, xAI, or Gemini image models (independent of your chat provider). By default the prompt is framed with the book's title/author and a slice of surrounding text so illustrations match the work's setting; both framing toggles and a prompt-template preview are in Settings. Images are kept on-device in a browsable **Generated Images** gallery, associated with the book they came from, and surfaced on the Book Hub and artifact browser. Thanks to @savvasdalkitsis for the feature.

## Chat Toolbar & Sessions

The input dialog's chip row grows into a full session toolbar: **Domain, Web, Tools, Quick, Scope/Ctx, Attach, Spoiler**. The binary chips (Web, Tools, Quick, Spoiler) tap-toggle for the current chat and hold-open their per-book/global defaults picker; Domain, Scope/Ctx, and Attach open their pickers on tap. Choose which chips appear via the gear menu.

- **Quick Answer:** one tap for a fast, brief answer. The preset bundle is configurable: brevity nudge, reasoning off, web/tools off, and optionally a fastest-model swap, a terse-behavior swap, or skipping domain/background for the answer. Direct entries (highlight menu, gestures) follow a per-book/global default.
- **Scope:** attach a text range to any question: current page, current chapter, a section span, or everything read so far.
- **Ctx:** the surrounding-context dial for highlight chats (sentence / paragraph / character amounts, clamped under spoiler protection), including "also send" book scopes. Paragraph windows now snap to sentence boundaries.
- **Attach:** bring notebook pages, artifacts, earlier chats, files, and one-off notes into a chat as labeled context.
- **Per-book Background:** a standing note about what YOU bring to a book ("reading this critically for a class"), injected alongside behavior and domain in every request for that book.
- Research mode now shows on the Domain chip, and the input dialog titles itself by context (Book / Highlight / X-Ray Chat).

## Response Viewing

- **Minimal popup:** short answers from quick actions (Translate, Quick Define, Quick Explain by default; configurable) land in a chrome-less popup anchored at your selection instead of a full-screen viewer, when they fit. Tap to expand to the full viewer. On by default ("When it fits").
- **Streaming keeps your place:** scrolling up mid-stream no longer yanks you to the bottom, and opening the finished response lands you on the exact line you were reading.
- Text alignment now defaults to **auto** (follows the text direction, so RTL answers align right); reply page breaks and scroll-to-newest-reply are also on by default now.
- Quote blocks in replies can be hidden per chat, with the global defaults (hide by default / auto-hide long quotes) now reachable from the button's hold menu.
- Text selection now works in the quiz viewer too (copy, dictionary, translate, add to notebook).

## Providers & Models

- **28 built-in providers**: 9 community additions this cycle (Cerebras, MiniMax, DeepInfra, Novita, Hyperbolic, Nebius, Chutes, Featherless, Vercel), plus custom OpenAI-compatible providers. Universal "Fetch models" / "Test provider" for every provider.
- **OpenAI Subscription (#103):** use a ChatGPT plan without an API key, via device login — verified working on free accounts too. Web search and book tools included. Thanks to @bmanturner for the groundwork.
- **Multiple API keys per provider**, with a manager to switch between them (tap to use, hold to manage).
- **Model tiers, in the GUI:** a 5-tier speed ladder editable per provider, global tier pins, and per-action speed hints (e.g. Translate prefers a fast model of your current provider).
- **Self-healing output limits:** when a provider rejects a request for exceeding a model's output cap, the plugin parses the stated limit, retries once at it, and remembers it for that model.
- **Prompt caching actually engages now:** Anthropic caching covers message history (it was silently missing the minimum cacheable size before), and OpenRouter-routed Claude/Gemini models get caching too — roughly 90% off repeated content.
- **Responses API** routing for OpenAI and xAI (web search and book tools on their current wire), a web-search depth dial with per-book override, a sources viewer for provenance, Z.AI search-engine choice (the default now returns international-quality sources), an Ollama server manager with per-request context sizing (no more silent truncation), and Perplexity search that can genuinely be turned off.
- Model refresh across the board (GPT-5.6 family, Gemini 3.6/3.7 Flash, Claude Opus 5 / Fable 5, and more); the GitHub Models preset was removed after the host retired its API.

## AI Book Tools

- Ollama joins the tools providers (local models, capabilities derived per model), alongside Gemini, Claude, OpenAI (API + Subscription), OpenRouter, DeepSeek, Mistral, Groq, xAI, Fireworks, Qwen, and Kimi.
- The three-way posture was simplified to a plain on/off, and the default is now **off** while retrieval quality matures (see Work in Progress). "Smart retrieval" now also works on the "Up to current position" scope, clamping the tools to where you are.

## Privacy

- **Per-book privacy overrides:** allow or deny highlights / annotations / notebook / text extraction for a single book; deny beats everything, including trusted providers.
- Your reading position is only disclosed to the AI when Basic Stats sharing allows it; spoiler reminders no longer leak position when it does not.

## Translations

- **Two new languages: Norwegian Bokmål and Swedish**, bringing the total to 26.
- Full refresh across all languages for this release's strings.
- As always, machine translations are marked "needs review"; corrections are very welcome on [Weblate](https://hosted.weblate.org/engage/koassistant/).

## Other Improvements

- Provider, model, and API-key menus refresh in place after adding/editing/removing entries (no more closing and reopening submenus).
- Error handling: rate-limit (429) errors show the provider's actual quota details with a retry option; server-overload (503) errors get the same persistent retry dialog; long decorated error messages scroll instead of pushing buttons off-screen; incomplete responses report their actual cause.
- File-browser long-press buttons now update live (no restart), and the input-dialog action lists have per-context managers (Book, Closed Book, Highlight, X-Ray Chat, Library, General) with a shared chooser.
- Chapter-end quizzes gained a minimum-reading-time gate, and quizzes now group multiple-choice questions together (asked for at generation time).
- `{previous_results}` placeholder: general-context actions can see their own recent saved runs, so recurring actions (news digests, journals) stop repeating themselves.

## Action Changes

- The highlight menu's fresh defaults were re-curated: Translate, Look up in X-Ray, Explain, Quick Explain, Summarize, Quick Define, Dictionary, Generate Image. Existing users keep their configured list (new entries inject at their positions; nothing is removed).
- New **Quick Explain** action: a two-or-three-sentence explanation designed for the minimal popup.
- The dictionary bypass default action is now **Quick Define** (was the full Dictionary entry; existing explicit picks are respected).
- book_info is now the only file-browser long-press default action (everything else remains available to add).
- The Grammar action returns in a simplified form (plain-language breakdown; manager-pickable, not a default).
- The "Add to notebook" highlight-menu row is now opt-in (Settings → Menus & Buttons).
- Recap no longer offers "Pick section range…" (arbitrary spans don't fit a catch-up action); "From section…" stays.

## Stability & Performance

- **Fixed a crash that silently killed local/self-hosted provider requests (Ollama and similar) on macOS**, caused by a background process crashing during network setup.
- **Fixed Ollama silently truncating long prompts** (X-Ray builds, recaps, book-text requests) at a fixed 4096-token window; the context size now scales with the request.
- Fixed an O(n^2) slowdown in stream parsing that dragged on long streaming responses, and streaming breaking on a JSON null in the wire data.
- Fixed mid-stream provider errors going undetected on every provider except Gemini — a response that failed partway through used to complete silently as if it had succeeded.
- Fixed update checks hanging on macOS (DNS is now pre-resolved).
- Fixed long-press file-browser popups (and some other dialogs) leaking as invisible windows that could survive into the reader and block KOReader from closing.

## Bug Fixes

- **Fixed empty "No response received" failures on reasoning models** (#98): reasoning could consume the entire output budget. Output defaults are now raised per model, reasoning gets guaranteed headroom, and a budget-exhausted answer reports honestly instead of dumping raw data. Also fixed Anthropic responses being capped at 16K output tokens instead of the intended 32K, and truncated answers on several community providers with too-low output caps.
- **Fixed "Look up in X-Ray" from chat and viewer surfaces sometimes targeting the wrong book** — including a case where it could delete another book's X-Ray.
- Quiz fixes: correct answers were statistically biased toward option B (the plugin now assigns answer letters itself); scores counted only answered questions; quiz exports and notebook copies dropped answer content.
- Fixed per-book setting overrides leaking into general and library chats, highlight-triggered actions not resolving the open book's per-book overrides, and per-book AI title/author not applying to freeform Send and artifact chat.
- Fixed the "reasoning off" toggle only minimizing (not disabling) reasoning for some OpenRouter/Requesty model families.
- Fixed the Perplexity web-search toggle having no effect, and retry dialogs silently re-enabling web search or book tools you had just turned off.
- Fixed wide markdown tables overflowing the chat viewer, markdown links misbehaving, and chat viewer alignment/font size resetting on every open instead of persisting.
- Streaming fixes: pausing autoscroll no longer yanks the view; in-flight replies now appear when the viewer changes mid-stream; opening a reply no longer flashes the top of the document or leaves a stray search highlight.
- Fixed expanding a dictionary popup into the full viewer silently re-enabling streaming you had turned off.
- Fixed text selected in dictionary/viewer popups incorrectly picking up the open book's context, and `{highlighted_text}` not resolving in every message context.
- Fixed Save-to-Note ignoring your configured default highlight color.
- Fixed Quick Settings popups graying out valid options (e.g. the last language in the Translate picker), and language-picker entries not appearing until the submenu was reopened.
- Fixed "reset input dialog actions" only resetting four hardcoded contexts instead of all of them.
- Fixed several settings whose reading code didn't match their declared default, several resolvers that folded an explicit "off" back to the default, buttons that were tappable with unmet prerequisites, crashes in Quick Edit on custom actions, a provider connection-test crash, and editing a custom action stripping its dictionary-view setting.
- Numerous smaller fixes across chat, artifacts, X-Ray, and providers.

## For Custom Action Users

- New placeholders: **`{previous_results}`** / **`{previous_results_section}`** (general-context actions; injects that action's recent saved runs), **`{response_language}`**, and `{page_number}` / `{page_text}` / `{page_text_section}` are now in the placeholder picker (#71).
- New action fields: `accept_quick_answer` (opt into the Quick Answer posture), `model_tier` (prefer a faster model of the same provider), `skip_background` (per-book Background gate), `smart_retrieval` (offer targeted passage retrieval as a source).
- `custom_models.lua` can now grant/deny capabilities, declare reasoning profiles (including for custom providers), set output caps, and place models into speed tiers.
- Actions with `source_selection` now offer the scope rows to highlight actions too (read so far, from a section, a section range).

## Work in Progress

Setting expectations for the new surfaces:

- **Groups and management surfaces:** functional but early; UI consolidation lands in v0.22.
- **AI Book Tools:** off by default while retrieval quality matures; turn tools on per chat with the Tools chip, per book in Book Settings, or globally. (Users who had chosen the old "auto" posture keep tools on.)
- **Minimal popup routing:** fit rules may still change.
- **Setup Wizard v2:** built but deferred to v0.22; the existing first-run wizard still serves.
- Reasoning across 28 providers is configured per model from empirical probing; report misbehaving models.

## How You Can Help

- **Device reports**,  especially on the new write paths (groups, cross-book merges, checkpoint installs).
- **Translations:** review passes on [Weblate](https://hosted.weblate.org/engage/koassistant/) help a lot.
- **Feedback on the new surfaces** (entity cards, marking, Book Hub, chips): what feels wrong, what you turned off first, what you want more of.
- **Bug reports and Feature Requests**

## What's Changed

* Image generation from highlights by @savvasdalkitsis in https://github.com/zeeyado/koassistant.koplugin/pull/96
* OpenAI Subscription device auth by @bmanturner in https://github.com/zeeyado/koassistant.koplugin/pull/101

## New Contributors

* @savvasdalkitsis made their first contribution in https://github.com/zeeyado/koassistant.koplugin/pull/96
* @bmanturner made their first contribution in https://github.com/zeeyado/koassistant.koplugin/pull/101

**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.20.0...v0.21.1
