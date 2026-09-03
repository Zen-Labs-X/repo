# v0.21.2

# KOAssistant v0.21.2 Release Notes

Maintenance release for v0.21.0, focused on X-Ray reliability. Notes for v0.21.1 and v0.21.0 below, since they came in quick succession.

If updating OTA from v0.21.0 or earlier gives you a luajit error, see the manual-install note under v0.21.1 below (one-time; updating from v0.21.1 works normally).

## Maintenance (v0.21.2)

- **Intermittent X-Ray build failures fixed** ("response is not valid JSON"): malformed JSON from the model is now repaired before parsing. Quiz parsing got the same hardening.
- **Long requests are no longer killed at 3 minutes** (limit now 15; you can still cancel from the loading dialog).
- **Connections cleaned up**: every connection must name its relationship (no more bare name-drops), rows show the relationship text in full, wrong-entity resolution and duplicate accumulation fixed, entity pages no longer drown in connection lists, and a crash in the overflow list is fixed.
- **Category narrowing survives updates** (a "Characters only" X-Ray no longer regrows all categories), and update requests are slimmer on long books.
- **Timeline reliability on updates.** Two defects fixed: v0.21.0's "Shorter Update Requests" trimming could freeze the timeline (updates stopped recording new events entirely; the trimming and its setting are removed, updates send the full lists again), and the update instructions now explicitly forbid re-sending existing timeline events (re-sends were appended as duplicates, in the worst case replaying the whole story from the start). If an affected book's timeline has gaps or duplicated stretches, a rebuild restores it.
- **Archived versions keep your most complete builds** instead of just the most recent, with honest labels in the versions list.
- **Reader engagement removed from X-Ray**: it never worked as designed, and highlights/annotations are no longer sent with X-Ray builds at all. Existing X-Rays are unaffected; Recap and highlight analysis keep their highlight use.
- New **Light (characters and story arc)** preset in the X-Ray categories picker.
- The "Global (use setting)" reasoning option now works on built-in actions that pin reasoning; it was silently inert.

---

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

**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.20.0...v0.21.2

# v0.21.1

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

# v0.21.0

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

**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.20.0...v0.21.0

# v0.20.0

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

# v0.19.1

## KOAssistant v0.19.1 Release Notes

This is a maintenance and bugfix release to v0.19.0 (release notes below), addressing a long-standing issue with subprocess hanging.

Fixed a bug where API requests, connection tests, and update checks could hang indefinitely on some devices. The plugin now detects subprocess completion via pipe EOF instead of relying solely on `waitpid`, which can be unreliable on certain OS kernels. Also fixed: Connection test now correctly uses API keys entered through the GUI settings.

**Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.19.0...v0.19.1

# KOAssistant v0.19.0 Release Notes

> **Settings reset recommended.** After updating, go to **Settings → Backup & Reset**
> and reset Quick Actions panel, Quick Settings panel, and Input Dialog actions to pick up new defaults.
> Or do a full Reset. Custom actions, API keys, notebooks, chats, and cached artifacts are not affected.

---

## Section Artifacts & Source Selection

Artifacts are no longer limited to the full document. You can now generate X-Rays, summaries, analyses, and other artifacts for specific chapters or sections.

- **Section picker**: Choose any chapter or section from the book's table of contents.
- **Source selection popup**: Before running, choose scope (full document or section) and source (full text, cached summary, or AI knowledge only). Remembers your last choice per action.
- **Section summaries**: Generate section-specific summaries on the fly — cached and reusable by other actions.
- **Smart X-Ray lookup**: Automatically selects the most relevant X-Ray for your current page (section > main > prompt to choose).
- **Cross-section search**: "Look up in X-Ray" searches across all section and main X-Rays simultaneously.
- **Artifact unification**: All artifact actions now use the same View/Update/Regenerate workflow. Previously, some cached silently in the background.
- **→ Chat button**: Available in all artifact viewers — ask follow-up questions with the artifact as context.

Applies to: X-Ray, Recap, Summary, Analysis, Analyze Notes, Key Arguments, Discussion Questions, Quiz, Extract Insights, X-Ray Simple, and Reading Guide.

---

## Pinned Artifacts & Starred Chats

- **Pin any AI response** as a named artifact (hold → "Pin to Artifacts"). Appears in Artifacts browser and popups.
- **Star conversations** to mark important chats. Starred chats appear in a virtual "Starred" folder in Chat History.

---

## Research Mode

Automatic academic paper detection and adaptation.

- **DOI detection** from document metadata and first-page text.
- **Academic prompt tracks**: X-Ray uses research categories (Key Concepts, Methodology, Findings, Referenced Works), About becomes a structured overview, Find Similar focuses on related literature.
- **Auto web search**: DOI-detected documents enable web search for relevant actions.

---

## Notebook Vault Storage

Notebooks can now be stored in a central folder or a custom location (e.g., an Obsidian vault), not just alongside the book.

- Three save locations: alongside book (default), central folder, or custom path.
- Vault/central modes use `Author — Title.md` filenames with YAML frontmatter.
- Switching location auto-migrates existing notebooks with collision handling.
- Notebook button now opens a popup: Add to Notebook / View / Edit.

---

## Multi-Book Action Launcher

Multi-book actions (Compare, Find Common Themes, Analyze Collection, Quick Summaries, Reading Order, Recommend) now use a dedicated book picker with search and filtering, instead of requiring navigation to each book. New action: **Recommend Books**.

---

## Action Changes

- **AI Wiki**: Encyclopedia-style entries from highlights or from the X-Ray browser (per-item, cached as artifacts).
- **Reading Guide**: Spoiler-free guidance for what to watch for as you read. Adapts to genre.
- **Grammar**: Sentence-level grammatical breakdown — word-by-word with optional constituency parse. Language-aware.
- **Smart actions removed**: Explain/Analyze in Context Smart replaced by the source selection popup on the standard actions.
- **Action names shortened**: "Book Info" → "About", "Analyze My Notes" → "Analyze Notes", etc.
- **In-context trio clarified**: Explain (comprehension), Analyze (reader-focused), Thematic Connection (craft analysis) — less overlap.
- **Deep Analysis**: Restructured for dense, scannable output.

---

## New Providers

### Z.AI

17th built-in provider. GLM models (GLM-4.5-Flash free tier) with regional endpoints (international/China) and toggleable thinking for GLM-4.5+ models.

### Perplexity

18th built-in provider. Sonar models with always-on web search, citations as clickable footnotes, and reasoning extraction for `sonar-reasoning-pro`.

Streaming `<think>` tag extraction (also benefits Groq, Together, Fireworks, SambaNova, and Ollama).

### Local Provider Presets

Quick setup for LM Studio, llama.cpp, Jan, vLLM, KoboldCpp, LocalAI. Pre-fills name and URL, no API key required.

---

## Reasoning & Model Updates

### Reasoning Expansion

New effort-level controls for always-on reasoning providers:

| Provider | Models |
|----------|--------|
| Groq | gpt-oss-120b, gpt-oss-20b, qwen3-32b |
| Together | DeepSeek-R1, Qwen3-235B, Qwen3-32B |
| Fireworks | deepseek-r1, qwen3-235b |
| SambaNova | DeepSeek-R1, Qwen3-32B |

**Gemini 2.5**: Thinking now controlled via master toggle with configurable budget (dynamic/low/medium/high/max). Previously always-on with no user control.

**Mistral**: Magistral models now always think — reasoning extracted automatically.

### Model Updates

- **OpenAI**: GPT-5.4 (new default) and GPT-5.4 Pro added. Reasoning is gated (controlled by master toggle, same as GPT-5.1/5.2).
- **Gemini**: Gemini 3.1 Pro Preview replaces 3 Pro Preview. Gemini 3 Flash Preview (free tier) and 3.1 Flash Lite Preview added. Gemini 2.0 models removed.
- **Z.AI**: GLM-5 (flagship) and GLM-4.7 family added.

---

## Other Improvements

- **Text selection popup** in all KOAssistant viewers: 1 word → dictionary, 2+ words → Copy/Dictionary/Translate/Notebook popup.
- **Recap reminder**: Optional prompt to run AI Recap when opening a book after configurable days of inactivity.
- **KOReader storage modes**: All metadata modes now fully supported (previously only default mode was reliable).
- **Chat viewer**: Button layout streamlined. Dictionary view mode for highlight actions. Export saves to file (Copy handles clipboard).
- **API errors**: Now shown as readable text instead of raw JSON.
- **Quiz**: Answer Key moved to separate section to prevent spoilers.
- **Kobo**: No longer crashes without Wi-Fi at startup.
- **"Use Primary" → "Follow Primary"**: Language picker wording standardized.

---

## Bug Fixes

### X-Ray & Artifacts

- Fixed cross-book browser/viewer showing wrong book's data.
- Fixed section X-Ray surfacing, scope matching, and popup labels.
- Fixed AI Wiki placeholders, detail refresh, and cross-navigation.
- Fixed X-Ray lookup skipping description matches.
- Fixed TOC ghost entries in section artifact pickers.
- Fixed XPointer hidden flows in page display.

### Chat & Conversations

- Fixed chat titles, section scope labels, and starred status persistence.
- Fixed v2 chat delete and navigation gaps.
- Fixed group popups layering and multi-book context routing.

### Providers & Reasoning

- Fixed Perplexity citation formatting and message merging.
- Fixed default thinking preservation for Gemini 2.5, DeepSeek, and Z.AI when master toggle is off.
- Fixed Anthropic 4.6 adaptive thinking not suppressed when reasoning config is "off".

### Other

- Fixed UTF-8 context truncation for non-ASCII text (Arabic, CJK).
- Fixed notebook vault migration, collision handling, and export paths.
- Fixed action flag preservation when duplicating actions.
- Fixed "Keep English" not saving for non-English users.
- Fixed markdown link formatting in AI responses.

---

## For Custom Action Users

- **Smart actions removed**: Recreate using standard versions with `source_selection` enabled.
- The `source_selection` flag is available for custom actions — add it to any text-extraction action.

---

**Full Changelog**: https://github.com/zeeyado/koassistant.koplugin/compare/v0.18.2...v0.19.0
