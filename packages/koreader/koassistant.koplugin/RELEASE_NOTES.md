# v0.22.1

# KOAssistant v0.22.1 Release Notes

Maintenance release for v0.22.0: two small fixes and one changed default. Notes for v0.22.0 below, since they came in quick succession.

## Maintenance (v0.22.1)

- **New X-Rays default to the Reference preset** (characters, places, themes and terms; no timeline or argument development) instead of all categories. Builds finish noticeably faster on every model, everything you can tap on in the book is still tracked, and Recap covers what happened. Pick All categories under Settings > X-Ray > Categories for New X-Rays (or per book) to get the timeline back. Existing X-Rays keep the categories they were built with. Note: if you had picked All categories globally before this version, that pick was stored as "no preference" and now reads as Reference; pick All categories once more to restore it.
- **Group Hub and Book Hub show real titles and authors for books you have never opened.** They used to fall back to the file name with no author until the book was opened once. The book picker's collection and folder lists do the same when KOReader's cover browser has already cached the metadata.
- **The KOAssistant row now sits at the top of the Tools menu**, in both the reader and the file browser, instead of at the very end after "More tools".

---

# KOAssistant v0.22.0 Release Notes

> **SHIPPED 2026-09-07** as tag `v0.22.0` (108 commits since v0.21.2). The GitHub release body is this file minus the trailer; the recipe is [release_recipe.md](release_recipe.md).

> **Behavior changed in this release.** Nothing starts a book's X-Ray on its own any more, and every first build asks first. Three settings were removed with that change: "Also Start X-Rays Automatically", "First Build for New Books" and "Offer Automatic X-Ray for New Books". If you had them on, see the first two bullets below. Existing X-Rays, chats, notebooks and API keys are not affected.

> **Your per-book data moved.** Chats and per-book settings now live in the book's own `.sdr` folder in plugin files instead of inside KOReader's `metadata.lua`. The move happens automatically on first start and nothing is lost; details under Storage.

---

## Spoiler Protection and X-Ray

**Automation only continues what you started.**

- **Nothing starts an X-Ray on its own.** "Automatic X-Ray (all books)" now only keeps up to date the X-Rays you have already started; a book with no X-Ray is left alone. The settings that used to start one ("Also Start X-Rays Automatically", "First Build for New Books" and its coverage question, "Offer Automatic X-Ray for New Books") are gone. Stale values are ignored, nothing needs migrating.
- **Every first build asks first.** The two ways to start a background X-Ray are the creation form's "In checkpoints, as I read (automatic)" pick and the per-book "Automatic X-Ray: On" switch. Both now say how many background requests they need right now and wait for **Start**; **Cancel** puts the switch back the way it was and nothing runs. (When nothing needs building right now, the switch just turns on.) A book left On while it was closed gets the same question the moment the first build would start, with "Cancel (turn Automatic X-Ray off)" as the way out. Books that already have an X-Ray keep being extended silently, which is what Automatic means.
- **Deleting an X-Ray now quiets automation for that book**, so nothing re-asks or restarts behind you after a delete.
- The Automatic X-Ray cooldown is cleared when a build chain finishes; a completed chain used to silently decline page-turn triggers for a whole cooldown.

**New: depth.**

- **Depth of New X-Rays: Light / Standard / Deep.** Light is one line per entry and only recurring figures and turning points; Standard (the default, unchanged from before) is a few sentences per entry; Deep is longer entries with richer connections. Set the default in **Settings > Reading & Library > X-Ray > Depth of New X-Rays**, per book in **Book Settings > X-Ray > New X-Ray depth**, or from the creation form. It applies to creates and rebuilds; checkpoints and updates keep the depth the X-Ray was started with.

**Categories.**

- **Presets renamed and re-cut**: **All categories**, **Characters and story (people, timeline)**, **Reference (everything except the timeline)**, **Characters only**. The timeline turned out to be the single heaviest block of an X-Ray, so "Reference" is now the cheap pick and cost lives on the depth dial instead. The picker separates presets from picking categories one by one.

**Creation form and checkpoints.**

- Spacing, categories and depth sit on one small options row above the action buttons, each button showing its current value, and the categories and depth pickers open on the book tab from there and from Book Settings. On a plain extend the categories and depth buttons show what the X-Ray was started with (they are locked to it), not the current default.
- A one-step checkpoint plan stays pickable instead of disappearing, and the 100%-covered "Rebuild X-Ray..." row opens the rebuild form directly (no more deleting first).
- A build that only covers up to your position no longer spends a request on a separate introduction it would immediately supersede.
- The next checkpoint starts building only after the current one installs, and builds from the live copy, so entity renames and merges you made carry forward.
- A checkpoint installs only once you actually reach its coverage (it used to install a hair early).

**Entity cards and marking.**

- **Upcoming entities reveal in stages.** An entity known only from the checkpoint built ahead of you now shows name and category first, one tap adds the first sentence, and another opens the full entry behind the usual spoiler confirmation. Two new settings: **Upcoming Entity Cards** (name only / first sentence right away) and **Card Shows** (first sentence only / full entry, for entities already in your installed X-Ray). Both can be overridden per book. When the tap landed on an alias, the card stays at name only even with "first sentence right away", since the sentence would give away which entry the alias belongs to.
- **The peek reads one checkpoint, never a later one**: the ahead card now uses the lowest built checkpoint that reaches your position, so an alias folded in at 100% cannot reveal itself on sight.
- Tapping a marked alias opens the card on the words you tapped, not on the entry name (which gave the link away).
- A name inside another entity's longer name now counts as the longer entity's mention everywhere: marks, mention lists, chapter appearances and counts.
- Names whose own edge is punctuation ("D.B.", "Jr.") are marked again.
- The first-sentence cut on cards handles initials, titles, CJK sentence ends and the Arabic question mark instead of stopping at the first period.
- The card no longer shows the whole entry when the first sentence ends in a non-breaking space, or when the next word starts lowercase after an ordinary word (a name like "van" or "de"); only short abbreviations such as "vs." still hold the sentence open. This is why some cards were cut and others were not.

**Other X-Ray.**

- **One more JSON repair**: a key that arrives missing its opening quote is restored, so a long build is not lost to it (the same family of fixes as v0.21.2).
- Artifact caches now record the request's token usage, shown on the artifact viewer's Info button.
- Section runs of **Counterarguments** now cache and browse like the other section artifacts.
- The X-Ray browser's root Mentions view defaults to the whole book once the book is marked Finished.
- A typeless non-fiction X-Ray is no longer read as a fiction one (it used to render every category empty).

## Book Groups and Cross-Book X-Ray (#90)

The headline of this cycle: in a group, an X-Ray lookup answers from the whole group, not just the open book, and every group now has its own page and its own settings.

- **Lookups reach the group.** Tapping a marked word, an exact dictionary or highlight match, an entity card, and the X-Ray browser's search all fall back, in order, to this book's carried list and then to the group's other X-Rays, nearest book first. Cards and rows name their source ("Carried from *Title*", "From *Title*'s X-Ray"), and a hit from another book offers **"Open in *Title*'s X-Ray"** and **"Add to this book's carried list"**.
- **The browser's search results fold the group in** as "From *Title*" groups, under the carried entries, with a plain "Nothing in the earlier books either" (or "Nothing in the other books of the group either") when there is nothing anywhere. No second tap.
- **Carried lists keep themselves up to date.** Editing a group (adding, removing, reordering, changing its kind) or writing any of its X-Rays re-seeds the members' carried lists in the background. Removing a carried entry is remembered, so it does not come back.
- **Later volumes stay closed.** In an ordered series a lookup only looks past a book once that book is read (marked **Finished**, or read to its last page) or its own spoiler protection is off. Volume 1 unread and protected keeps volumes 2 and 3 out of reach, whatever their own settings say. Passive marking, entity cards and matching selections never reach past that chain.
- **The reveal is one book at a time.** When something is held back, the results list and the no-results dialog carry a row naming the next volume ("Search *Title* too (may contain spoilers)..."), the confirmation names it too, and each confirmation opens exactly one more book. Nothing sticks: every search starts from the chain again.
- Project groups share in every direction between all members; plain groups share nothing.
- The "add this as an alias of an existing entry" offer now also appears on books that have section X-Rays (it used to fall back to a bare message there).
- **Series suggestion sees edited metadata**: a series typed into KOReader's own Book information editor now counts like one read from the file.
- Installing a checkpoint no longer drops carried entries and aliases that existed only in the live copy.
- **The group jump is spoiler-safe.** From an X-Ray entry, the "→ Group" popup lists a later volume that is still behind the spoiler chain as "(later in the series)" without checking whether the entity appears in it (knowing that a character returns is already a spoiler), and opens it only after the same confirmation the search reveal uses. From an entity page, the other book's entry opens as a read-only view over the page instead of switching X-Rays. Entity cards and pages also say where else in the group the entity appears ("Also in *Title*'s X-Ray"), never naming a later volume the spoiler chain still holds back.

**Group Hub and group settings.**

- **Every group has a page.** Main menu > Groups opens the Groups list: one row per group with its kind icon and "Kind · N books"; tap for the group's hub, hold to move, rename, change the kind or delete it, and the title-bar menu creates groups (blank, from a folder, from a collection, or with the open book) and sorts the list by name or by kind (a one-shot sort; you can still move groups by hand). The list itself also offers "New group from series ..." when the open book carries a series tag.
- **The Group Hub** shows a group's action rows first (Group Settings, the X-Ray fold row, and a Series/Project/Group Chat/Action row that opens the library dialog with the members pre-selected), then the members in order (tap for a book's Book Hub, hold to move, open or remove it), then the add rows. Its title-bar menu carries the add flows, Kind, Rename and Delete; the up-arrow returns to the list. The Book Hub's Group row, the artifact viewers' "→ Group" button and the Quick Actions "Group Hub" utility all land on the book's hub (a chooser when it is in several groups); the X-Ray browser's own "→ Group" keeps opening the members popup, which has a "Group hub..." row. A Book Hub opened from a group gets an up-arrow back to it.
- **Group settings.** A group can set the same settings a book can: domain, research mode, Background, spoiler protection, automatic X-Ray, new X-Ray categories and depth, and the three languages, through the same pickers ("For this group"). Setting a value offers to apply it to every member; members then follow the group ("Follow group X (value)" on their Book Settings rows and in every picker) until they pick their own value, which the Group Settings screen lists as "not following" with "Re-apply to all". Books added to a group that sets values are asked once; leaving or deleting a group returns its books to the global settings, and a book whose group no longer exists (a groups file restored from an older backup, say) simply follows the global settings again.
- **Collections as a source.** The book picker browses KOReader collections beside history and folders; groups can be created from a collection or filled with one, and the series scan can look in a collection.
- A closed book's chat opened beside another open book (from a group hub, for instance) gets its own dialog again instead of the open book's actions and title.
- Crossing the next built checkpoint installs it at any spacing; a spacing above 25% used to refuse the install (for good with automatic X-Ray off).

## Chat Viewer

- **Math renders as readable formulas** (#105). LaTeX in a response is shown with Greek letters, real operators, superscripts and subscripts, accents, roots, and fractions as `a/b`, with display formulas centered. Markdown view only, and display only: saved chats, copies and exports keep the original notation, which Obsidian and similar apps render fully. Toggle in **Settings > Display Settings > Rendering > Render Math Formulas** (on by default).
- **New Window Size setting** (Standard / Expanded) in **Settings > Display Settings > Window Size** for chat, artifact, translate, dictionary and quiz windows, also on each window's gear menu. Expanded leaves only a hairline around the window; compact dictionary popups are unaffected.
- Indented continuation lines under a list item render as part of that item instead of an empty bullet.
- A response whose markdown is cut short mid-code-fence renders instead of falling back to plain text, and emphasis characters inside math no longer scramble the rest of the answer.
- **Exports no longer fail on Kindle** ("Invalid argument"): filenames built from a title are cut on a character boundary.
- **Hold Close to get back to the page.** A long press on the Close button closes the chat window, any dictionary windows under it and the highlight menu in one gesture, instead of tapping through them one at a time.
- A reply that arrives while you have scrolled back to reread lands where you were reading, not on the last question marker (from the second reply on, the marker used to win).
- Pressing Stop or closing the window in the moment after a streamed answer has finished, while the plugin is still reading the provider's trailing rate-limit information, no longer reports the complete answer as cancelled.

## Providers and Models

- **NVIDIA is a new built-in provider**: free developer program, email only, no card and no identity check. Curated model list from a live catalog probe, reasoning profile, book tools on the models where forced tool use actually worked, no web search. Models retired by the host on 2026-08-26 are pruned, response parsing (including reasoning content) is fixed, and speed tiers are placed from measured latency.
- **Test provider** now shows the server's own error detail when a reachability check fails, instead of a bare failure.
- **OpenCode Zen and OpenCode Go are two new providers on one account** (#107): Zen is the pay-as-you-go catalog of open-weight models, Go the subscription with its own model list. Zen's built-in list grew by nine models (GLM 5, 5.1 and 5.2, MiniMax M2.5, Kimi K2.5, Qwen 3.5 Plus and 3.6 Plus, and two experimental ids), each with its own reasoning and output profile. Each has its own key entry (the same key string under `opencode` and `opencode_go`), both send the conversation header OpenCode requires, and reasoning effort is one setting for both. GPT, Claude and Gemini through OpenCode are not supported yet (they use other endpoints).
- **One conversation id per chat.** The id a chat is saved under is the id the wire saw, and it rides to the hosts that use one (OpenCode's session header, OpenRouter's session id, OpenAI's prompt cache key). No other host receives it.
- **Gemini's content filter is relaxed for books by default.** Google's own filter blocks answers about violent or sexual passages, and the reply used to arrive empty and unexplained. The plugin now turns the four adjustable filter categories off for its own requests. **Settings > Advanced > Provider Settings > Gemini Content Filter** ("Relaxed for books" by default, "Google default" restores Google's), also on the Gemini model menu.
- **When a provider cuts a response short, it says so.** A finish reason outside the normal set (a safety or content filter, a recitation block, a refusal) used to surface as "Unexpected response format" when nothing came back, or as a silently shortened answer. The reason is now named: as the error when there is no text, and as a line under a partial answer, which also keeps that answer from being cached as if it were complete. Streamed replies included.
- **Groq is now a tested provider.** A reader's free key (the #106 report) let the maintainer's model audit run against Groq itself: the live model list, and the full capability battery on every built-in Groq model. The gpt-oss models reason by default with low, medium or high effort, answer up to 65,536 tokens and take the book tools; the compound models take no reasoning setting and no tools, and answer up to 8,192 tokens. Everything the plugin had assumed from Groq's documentation held, so Groq loses its community marker in the provider list.

**Requests that fit your plan (#106).**

Some providers count the answer budget a request *asks for* against a per-minute token allowance, before running anything. Since v0.21.0 the plugin asks for a large budget by default, so on Groq's free plan (8,000 tokens a minute) every request was refused, including one-word dictionary lookups, and the error text blamed book size.

- The plugin now learns your plan's per-minute allowance from the provider's own rate-limit headers (Groq, Cerebras, OpenAI) and sizes the answer budget to fit it before sending. It learns on the first real answer, streamed ones included, and from "Test provider".
- If a request is refused all the same, a refusal that names its numbers teaches the plan's allowance: one whose answer budget was the problem is sent once more at a budget those numbers allow, and every later request in that session is sized to fit the allowance. A burst refusal (your minute's allowance is already spent) is not resent, because it refills with time.
- **One honest tip per refusal.** A burst refusal ("you used your minute") says to wait; an admission refusal explains what actually happened, and when the request itself is bigger than the allowance it names the lever for the surface you are on (scope and a new chat in a book chat, folders in the library, the artifact itself in artifact chat). A small one-word lookup refused this way no longer gets the old "lower Max Text Characters" advice, which could not have helped.
- If the prompt alone cannot fit your plan or the model's context window, a notice says so before sending, and the request is sent anyway rather than blocked locally.
- A background X-Ray build stopped this way now reports "request too large" instead of "unusable response", and does not retry on a 60-second timer for something deterministic. A per-minute refusal that states no numbers (Anthropic, Gemini, Cerebras) or one the bucket will admit once it refills counts as a burst: the wait tip, and the build retries once after a minute.
- A pinned answer budget cut to fit the plan tells you it was cut.
- The self-heal also recognizes OpenRouter's context-window wording, pre-caps the next request from it, and explains the window instead of blaming book text.
- **The provider's own wait, as a number.** When a refusal names how long to wait (Groq's and OpenAI's "try again in 5s", Gemini's retry delay, or the retry-after header Anthropic and OpenRouter send), the wait tip says "about N seconds" instead of "wait", and a background X-Ray build waits exactly that long before its one retry instead of a fixed minute (a wait past ten minutes stops the build instead, with the resume rows).
- **Account walls are named as such.** Used-up credits, an empty balance or a spending cap (OpenAI's insufficient_quota, Anthropic's "credit balance is too low" and monthly spend cap, DeepSeek's "Insufficient Balance", OpenRouter's "insufficient credits") get a tip that points at the account instead of "wait and try again", the error stays on screen with a Try again button for after you top up, and a background X-Ray build stops with "account credits or billing" instead of retrying. OpenRouter's "can only afford N tokens" refusal (its credit check counts the whole answer budget, so a low-credit key failed a one-line question) is resent once with that answer budget when N is worth an answer.
- Error messages now carry the provider's own error code in parentheses, such as "(insufficient_quota)" or "(rate_limit_exceeded)", which is what tells two providers' identical sentences apart.
- Checked on a real free Groq key (2026-09-07): the plugin learned the 8,000-token allowance from Groq's headers on the first answer and sized the next request to fit. Groq has since changed its limiter: the gpt-oss models now admit the old 32,768 budget (the photographed refusal did not reproduce), while some models carry a separate output-tokens-per-minute bucket (1,000 a minute on the preview Qwen models of that account). Both of Groq's new wordings are in the plugin's corpus: one that can never fit is resent once with a budget under the output limit, a spent bucket gets the wait tip with Groq's own seconds.

**Ollama**

- The plugin asks the server how big the loaded model's context window actually is before sending a prompt that will not fit, warns with the real number, and says afterwards when only part of the request reached the model (Ollama silently cuts the earliest book text to fit its window). New "Context window" row in the Ollama model menu.

**API keys**

- Keys are cleaned to printable characters when read, which heals a key pasted with an invisible character or an interior line break (the Kindle case where a key copied out of a wrapped text file kept returning 401). Saving a key reports how many stray characters were removed.

## Storage

**Per-book plugin data left KOReader's metadata.lua** (#72).

- Chats now live in `<book>.sdr/koassistant_chats.lua`, and every per-book plugin setting in `<book>.sdr/koassistant_book_settings.lua`, next to the cache and notebook files the plugin already kept there.
- **The move is automatic**: a bulk pass runs once at start-up, with catch-up passes when a book is opened or first touched, and it copies and verifies before removing anything.
- Consequences: KOReader's **"Reset this document"** no longer wipes your chats and per-book settings, and KOReader's optional metadata archive no longer carries chats.
- A book store now follows a mid-session change of KOReader's "Book metadata location" instead of leaving its file behind.

**Backup and restore**

- **Book groups are included in backups** (and per-book settings ride along as well).
- **Restoring a backup made before the chat storage change now imports its chats** instead of restoring them where nothing reads them.
- "Quick: Fresh start" also clears the leftover chat-import backup folder once migration is complete.
- Deleting a notebook now also clears the book's pointer to it, so the book no longer refers to a notebook that is gone.

## Other

- **Console Debug is scoped to the plugin**: turning it on brings back the plugin's own tracing without raising KOReader's global log level (which used to bury it under core's per-paint output). Routine tracing is no longer written to `crash.log` when debug is off, and plugin tracing is also emitted when KOReader's own verbose logging is on. A few per-page-turn lines that Console Debug used to write at the info level moved to the debug level too, and the marking line no longer lists entity names.
- **One long-press menu on every action button.** Holding an action in the highlight menu, the dictionary popup, Quick Actions, an input dialog or the file browser menu now opens the same small menu instead of a description on some surfaces and nothing on others: the description at the top, "Add to" or "Remove from" this menu, "Other placements..." for the rest of its menus, and "Edit...", "Duplicate as custom action..." or "Reset to default". Adding or removing takes effect where you are standing, without a trip to Settings.
- **New `{user_input}` placeholder for custom actions.** Text typed in the input dialog can be placed inside a prompt where you want it, instead of only being appended at the end. It is in the editor's placeholder list as "Typed Input"; before this the placeholder was offered but never filled in, so the braces were sent to the model as they were.
- **The update check reads version tags correctly.** Two-part tags (v0.22) are no longer skipped when looking for the newest release, and pre-release tags sort the way they should: rc.11 is newer than rc.9, alpha comes before beta before rc, and a final release beats its own release candidate.
- The Domain & Research picker opens on the book tab whenever a book is open, from the input dialog's Domain chip and from holding the Quick Settings Domain tile; it used to open on Global until the book had an override of its own.
- Settings rows that open a picker or a manager (Categories and Depth of New X-Rays, the action and domain managers, the menu ordering managers, backups, the index tools, Test Connection, Check for Updates, About) now leave the settings menu open behind them instead of closing the whole menu.
- Section-scoped artifacts are back on the Book Hub (only the X-Ray versions group is filtered out there, since the X-Ray browser owns it).
- **Highlight menu defaults reordered** so the two conditional rows sit last: Translate, Explain, Quick Explain, Summarize, Quick Define, Dictionary, then Look up in X-Ray and Generate Image. Existing users keep their configured list.
- **Edited book metadata is honored everywhere**: a title or author changed in KOReader's Book information now shows and is sent in artifact and notebook pickers, groups, merge labels, the library scan, notebook filenames, backup labels and the chat history browser. The chat history index carries it and refreshes the moment you edit it.
- The chat history browser opens without reading each book's sidecar, which is noticeably faster on a large library.
- The per-book Quick Answer default now resolves the book the action targets, not whichever book is open.
- Quiz generation asks for answer options of comparable length, specificity and style.
- Text extraction reaches the document's last page (whole-document builds used to stop at the start of it), SSE `id:` and `retry:` lines from a streaming server are ignored instead of read as data, nested list bullets are drawn as filled dots at every depth instead of hollow circles and squares, and long code lines wrap in the chat viewer instead of being cut off at the right edge.

## Work in Progress

- **Cross-book lookups, the Group Hub and group settings** are new and touch a lot of surfaces. Device reports welcome; the group settings for chat behavior (tools, web search, effort dials, contexts) are planned for the next version.
- **Request sizing** is verified against a local stub and, for the header path, on a real free Groq key. A live Groq refusal has not been reproduced (Groq admitted the old budget on 2026-09-07), so the refusal path stands on Groq's own wording from the report.
- **AI Book Tools** stays off by default while retrieval quality matures.
- **Setup Wizard v2** is still built but not switched on.

## How You Can Help

- **Device reports**, especially on the X-Ray first-build confirmations, cross-book lookups in a series, and the storage move.
- **Translations**: review passes on [Weblate](https://hosted.weblate.org/engage/koassistant/).
- **Bug reports and feature requests.**

# v0.22.0

# KOAssistant v0.22.0 Release Notes

> **Behavior changed in this release.** Nothing starts a book's X-Ray on its own any more, and every first build asks first. Three settings were removed with that change: "Also Start X-Rays Automatically", "First Build for New Books" and "Offer Automatic X-Ray for New Books". If you had them on, see the first two bullets below. Existing X-Rays, chats, notebooks and API keys are not affected.

> **Your per-book data moved.** Chats and per-book settings now live in the book's own `.sdr` folder in plugin files instead of inside KOReader's `metadata.lua`. The move happens automatically on first start and nothing is lost; details under Storage.

---

## Spoiler Protection and X-Ray

**Automation only continues what you started.**

- **Nothing starts an X-Ray on its own.** "Automatic X-Ray (all books)" now only keeps up to date the X-Rays you have already started; a book with no X-Ray is left alone. The settings that used to start one ("Also Start X-Rays Automatically", "First Build for New Books" and its coverage question, "Offer Automatic X-Ray for New Books") are gone. Stale values are ignored, nothing needs migrating.
- **Every first build asks first.** The two ways to start a background X-Ray are the creation form's "In checkpoints, as I read (automatic)" pick and the per-book "Automatic X-Ray: On" switch. Both now say how many background requests they need right now and wait for **Start**; **Cancel** puts the switch back the way it was and nothing runs. (When nothing needs building right now, the switch just turns on.) A book left On while it was closed gets the same question the moment the first build would start, with "Cancel (turn Automatic X-Ray off)" as the way out. Books that already have an X-Ray keep being extended silently, which is what Automatic means.
- **Deleting an X-Ray now quiets automation for that book**, so nothing re-asks or restarts behind you after a delete.
- The Automatic X-Ray cooldown is cleared when a build chain finishes; a completed chain used to silently decline page-turn triggers for a whole cooldown.

**New: depth.**

- **Depth of New X-Rays: Light / Standard / Deep.** Light is one line per entry and only recurring figures and turning points; Standard (the default, unchanged from before) is a few sentences per entry; Deep is longer entries with richer connections. Set the default in **Settings > Reading & Library > X-Ray > Depth of New X-Rays**, per book in **Book Settings > X-Ray > New X-Ray depth**, or from the creation form. It applies to creates and rebuilds; checkpoints and updates keep the depth the X-Ray was started with.

**Categories.**

- **Presets renamed and re-cut**: **All categories**, **Characters and story (people, timeline)**, **Reference (everything except the timeline)**, **Characters only**. The timeline turned out to be the single heaviest block of an X-Ray, so "Reference" is now the cheap pick and cost lives on the depth dial instead. The picker separates presets from picking categories one by one.

**Creation form and checkpoints.**

- Spacing, categories and depth sit on one small options row above the action buttons, each button showing its current value, and the categories and depth pickers open on the book tab from there and from Book Settings. On a plain extend the categories and depth buttons show what the X-Ray was started with (they are locked to it), not the current default.
- A one-step checkpoint plan stays pickable instead of disappearing, and the 100%-covered "Rebuild X-Ray..." row opens the rebuild form directly (no more deleting first).
- A build that only covers up to your position no longer spends a request on a separate introduction it would immediately supersede.
- The next checkpoint starts building only after the current one installs, and builds from the live copy, so entity renames and merges you made carry forward.
- A checkpoint installs only once you actually reach its coverage (it used to install a hair early).

**Entity cards and marking.**

- **Upcoming entities reveal in stages.** An entity known only from the checkpoint built ahead of you now shows name and category first, one tap adds the first sentence, and another opens the full entry behind the usual spoiler confirmation. Two new settings: **Upcoming Entity Cards** (name only / first sentence right away) and **Card Shows** (first sentence only / full entry, for entities already in your installed X-Ray). Both can be overridden per book. When the tap landed on an alias, the card stays at name only even with "first sentence right away", since the sentence would give away which entry the alias belongs to.
- **The peek reads one checkpoint, never a later one**: the ahead card now uses the lowest built checkpoint that reaches your position, so an alias folded in at 100% cannot reveal itself on sight.
- Tapping a marked alias opens the card on the words you tapped, not on the entry name (which gave the link away).
- A name inside another entity's longer name now counts as the longer entity's mention everywhere: marks, mention lists, chapter appearances and counts.
- Names whose own edge is punctuation ("D.B.", "Jr.") are marked again.
- The first-sentence cut on cards handles initials, titles, CJK sentence ends and the Arabic question mark instead of stopping at the first period.
- The card no longer shows the whole entry when the first sentence ends in a non-breaking space, or when the next word starts lowercase after an ordinary word (a name like "van" or "de"); only short abbreviations such as "vs." still hold the sentence open. This is why some cards were cut and others were not.

**Other X-Ray.**

- **One more JSON repair**: a key that arrives missing its opening quote is restored, so a long build is not lost to it (the same family of fixes as v0.21.2).
- Artifact caches now record the request's token usage, shown on the artifact viewer's Info button.
- Section runs of **Counterarguments** now cache and browse like the other section artifacts.
- The X-Ray browser's root Mentions view defaults to the whole book once the book is marked Finished.
- A typeless non-fiction X-Ray is no longer read as a fiction one (it used to render every category empty).

## Book Groups and Cross-Book X-Ray (#90)

The headline of this cycle: in a group, an X-Ray lookup answers from the whole group, not just the open book, and every group now has its own page and its own settings.

- **Lookups reach the group.** Tapping a marked word, an exact dictionary or highlight match, an entity card, and the X-Ray browser's search all fall back, in order, to this book's carried list and then to the group's other X-Rays, nearest book first. Cards and rows name their source ("Carried from *Title*", "From *Title*'s X-Ray"), and a hit from another book offers **"Open in *Title*'s X-Ray"** and **"Add to this book's carried list"**.
- **The browser's search results fold the group in** as "From *Title*" groups, under the carried entries, with a plain "Nothing in the earlier books either" (or "Nothing in the other books of the group either") when there is nothing anywhere. No second tap.
- **Carried lists keep themselves up to date.** Editing a group (adding, removing, reordering, changing its kind) or writing any of its X-Rays re-seeds the members' carried lists in the background. Removing a carried entry is remembered, so it does not come back.
- **Later volumes stay closed.** In an ordered series a lookup only looks past a book once that book is read (marked **Finished**, or read to its last page) or its own spoiler protection is off. Volume 1 unread and protected keeps volumes 2 and 3 out of reach, whatever their own settings say. Passive marking, entity cards and matching selections never reach past that chain.
- **The reveal is one book at a time.** When something is held back, the results list and the no-results dialog carry a row naming the next volume ("Search *Title* too (may contain spoilers)..."), the confirmation names it too, and each confirmation opens exactly one more book. Nothing sticks: every search starts from the chain again.
- Project groups share in every direction between all members; plain groups share nothing.
- The "add this as an alias of an existing entry" offer now also appears on books that have section X-Rays (it used to fall back to a bare message there).
- **Series suggestion sees edited metadata**: a series typed into KOReader's own Book information editor now counts like one read from the file.
- Installing a checkpoint no longer drops carried entries and aliases that existed only in the live copy.
- **The group jump is spoiler-safe.** From an X-Ray entry, the "→ Group" popup lists a later volume that is still behind the spoiler chain as "(later in the series)" without checking whether the entity appears in it (knowing that a character returns is already a spoiler), and opens it only after the same confirmation the search reveal uses. From an entity page, the other book's entry opens as a read-only view over the page instead of switching X-Rays. Entity cards and pages also say where else in the group the entity appears ("Also in *Title*'s X-Ray"), never naming a later volume the spoiler chain still holds back.

**Group Hub and group settings.**

- **Every group has a page.** Main menu > Groups opens the Groups list: one row per group with its kind icon and "Kind · N books"; tap for the group's hub, hold to move, rename, change the kind or delete it, and the title-bar menu creates groups (blank, from a folder, from a collection, or with the open book) and sorts the list by name or by kind (a one-shot sort; you can still move groups by hand). The list itself also offers "New group from series ..." when the open book carries a series tag.
- **The Group Hub** shows a group's action rows first (Group Settings, the X-Ray fold row, and a Series/Project/Group Chat/Action row that opens the library dialog with the members pre-selected), then the members in order (tap for a book's Book Hub, hold to move, open or remove it), then the add rows. Its title-bar menu carries the add flows, Kind, Rename and Delete; the up-arrow returns to the list. The Book Hub's Group row, the artifact viewers' "→ Group" button and the Quick Actions "Group Hub" utility all land on the book's hub (a chooser when it is in several groups); the X-Ray browser's own "→ Group" keeps opening the members popup, which has a "Group hub..." row. A Book Hub opened from a group gets an up-arrow back to it.
- **Group settings.** A group can set the same settings a book can: domain, research mode, Background, spoiler protection, automatic X-Ray, new X-Ray categories and depth, and the three languages, through the same pickers ("For this group"). Setting a value offers to apply it to every member; members then follow the group ("Follow group X (value)" on their Book Settings rows and in every picker) until they pick their own value, which the Group Settings screen lists as "not following" with "Re-apply to all". Books added to a group that sets values are asked once; leaving or deleting a group returns its books to the global settings, and a book whose group no longer exists (a groups file restored from an older backup, say) simply follows the global settings again.
- **Collections as a source.** The book picker browses KOReader collections beside history and folders; groups can be created from a collection or filled with one, and the series scan can look in a collection.
- A closed book's chat opened beside another open book (from a group hub, for instance) gets its own dialog again instead of the open book's actions and title.
- Crossing the next built checkpoint installs it at any spacing; a spacing above 25% used to refuse the install (for good with automatic X-Ray off).

## Chat Viewer

- **Math renders as readable formulas** (#105). LaTeX in a response is shown with Greek letters, real operators, superscripts and subscripts, accents, roots, and fractions as `a/b`, with display formulas centered. Markdown view only, and display only: saved chats, copies and exports keep the original notation, which Obsidian and similar apps render fully. Toggle in **Settings > Display Settings > Rendering > Render Math Formulas** (on by default).
- **New Window Size setting** (Standard / Expanded) in **Settings > Display Settings > Window Size** for chat, artifact, translate, dictionary and quiz windows, also on each window's gear menu. Expanded leaves only a hairline around the window; compact dictionary popups are unaffected.
- Indented continuation lines under a list item render as part of that item instead of an empty bullet.
- A response whose markdown is cut short mid-code-fence renders instead of falling back to plain text, and emphasis characters inside math no longer scramble the rest of the answer.
- **Exports no longer fail on Kindle** ("Invalid argument"): filenames built from a title are cut on a character boundary.
- **Hold Close to get back to the page.** A long press on the Close button closes the chat window, any dictionary windows under it and the highlight menu in one gesture, instead of tapping through them one at a time.
- A reply that arrives while you have scrolled back to reread lands where you were reading, not on the last question marker (from the second reply on, the marker used to win).
- Pressing Stop or closing the window in the moment after a streamed answer has finished, while the plugin is still reading the provider's trailing rate-limit information, no longer reports the complete answer as cancelled.

## Providers and Models

- **NVIDIA is a new built-in provider**: free developer program, email only, no card and no identity check. Curated model list from a live catalog probe, reasoning profile, book tools on the models where forced tool use actually worked, no web search. Models retired by the host on 2026-08-26 are pruned, response parsing (including reasoning content) is fixed, and speed tiers are placed from measured latency.
- **Test provider** now shows the server's own error detail when a reachability check fails, instead of a bare failure.
- **OpenCode Zen and OpenCode Go are two new providers on one account** (#107): Zen is the pay-as-you-go catalog of open-weight models, Go the subscription with its own model list. Zen's built-in list grew by nine models (GLM 5, 5.1 and 5.2, MiniMax M2.5, Kimi K2.5, Qwen 3.5 Plus and 3.6 Plus, and two experimental ids), each with its own reasoning and output profile. Each has its own key entry (the same key string under `opencode` and `opencode_go`), both send the conversation header OpenCode requires, and reasoning effort is one setting for both. GPT, Claude and Gemini through OpenCode are not supported yet (they use other endpoints).
- **One conversation id per chat.** The id a chat is saved under is the id the wire saw, and it rides to the hosts that use one (OpenCode's session header, OpenRouter's session id, OpenAI's prompt cache key). No other host receives it.
- **Gemini's content filter is relaxed for books by default.** Google's own filter blocks answers about violent or sexual passages, and the reply used to arrive empty and unexplained. The plugin now turns the four adjustable filter categories off for its own requests. **Settings > Advanced > Provider Settings > Gemini Content Filter** ("Relaxed for books" by default, "Google default" restores Google's), also on the Gemini model menu.
- **When a provider cuts a response short, it says so.** A finish reason outside the normal set (a safety or content filter, a recitation block, a refusal) used to surface as "Unexpected response format" when nothing came back, or as a silently shortened answer. The reason is now named: as the error when there is no text, and as a line under a partial answer, which also keeps that answer from being cached as if it were complete. Streamed replies included.
- **Groq is now a tested provider.** A reader's free key (the #106 report) let the maintainer's model audit run against Groq itself: the live model list, and the full capability battery on every built-in Groq model. The gpt-oss models reason by default with low, medium or high effort, answer up to 65,536 tokens and take the book tools; the compound models take no reasoning setting and no tools, and answer up to 8,192 tokens. Everything the plugin had assumed from Groq's documentation held, so Groq loses its community marker in the provider list.

**Requests that fit your plan (#106).**

Some providers count the answer budget a request *asks for* against a per-minute token allowance, before running anything. Since v0.21.0 the plugin asks for a large budget by default, so on Groq's free plan (8,000 tokens a minute) every request was refused, including one-word dictionary lookups, and the error text blamed book size.

- The plugin now learns your plan's per-minute allowance from the provider's own rate-limit headers (Groq, Cerebras, OpenAI) and sizes the answer budget to fit it before sending. It learns on the first real answer, streamed ones included, and from "Test provider".
- If a request is refused all the same, a refusal that names its numbers teaches the plan's allowance: one whose answer budget was the problem is sent once more at a budget those numbers allow, and every later request in that session is sized to fit the allowance. A burst refusal (your minute's allowance is already spent) is not resent, because it refills with time.
- **One honest tip per refusal.** A burst refusal ("you used your minute") says to wait; an admission refusal explains what actually happened, and when the request itself is bigger than the allowance it names the lever for the surface you are on (scope and a new chat in a book chat, folders in the library, the artifact itself in artifact chat). A small one-word lookup refused this way no longer gets the old "lower Max Text Characters" advice, which could not have helped.
- If the prompt alone cannot fit your plan or the model's context window, a notice says so before sending, and the request is sent anyway rather than blocked locally.
- A background X-Ray build stopped this way now reports "request too large" instead of "unusable response", and does not retry on a 60-second timer for something deterministic. A per-minute refusal that states no numbers (Anthropic, Gemini, Cerebras) or one the bucket will admit once it refills counts as a burst: the wait tip, and the build retries once after a minute.
- A pinned answer budget cut to fit the plan tells you it was cut.
- The self-heal also recognizes OpenRouter's context-window wording, pre-caps the next request from it, and explains the window instead of blaming book text.
- **The provider's own wait, as a number.** When a refusal names how long to wait (Groq's and OpenAI's "try again in 5s", Gemini's retry delay, or the retry-after header Anthropic and OpenRouter send), the wait tip says "about N seconds" instead of "wait", and a background X-Ray build waits exactly that long before its one retry instead of a fixed minute (a wait past ten minutes stops the build instead, with the resume rows).
- **Account walls are named as such.** Used-up credits, an empty balance or a spending cap (OpenAI's insufficient_quota, Anthropic's "credit balance is too low" and monthly spend cap, DeepSeek's "Insufficient Balance", OpenRouter's "insufficient credits") get a tip that points at the account instead of "wait and try again", the error stays on screen with a Try again button for after you top up, and a background X-Ray build stops with "account credits or billing" instead of retrying. OpenRouter's "can only afford N tokens" refusal (its credit check counts the whole answer budget, so a low-credit key failed a one-line question) is resent once with that answer budget when N is worth an answer.
- Error messages now carry the provider's own error code in parentheses, such as "(insufficient_quota)" or "(rate_limit_exceeded)", which is what tells two providers' identical sentences apart.
- Checked on a real free Groq key (2026-09-07): the plugin learned the 8,000-token allowance from Groq's headers on the first answer and sized the next request to fit. Groq has since changed its limiter: the gpt-oss models now admit the old 32,768 budget (the photographed refusal did not reproduce), while some models carry a separate output-tokens-per-minute bucket (1,000 a minute on the preview Qwen models of that account). Both of Groq's new wordings are in the plugin's corpus: one that can never fit is resent once with a budget under the output limit, a spent bucket gets the wait tip with Groq's own seconds.

**Ollama**

- The plugin asks the server how big the loaded model's context window actually is before sending a prompt that will not fit, warns with the real number, and says afterwards when only part of the request reached the model (Ollama silently cuts the earliest book text to fit its window). New "Context window" row in the Ollama model menu.

**API keys**

- Keys are cleaned to printable characters when read, which heals a key pasted with an invisible character or an interior line break (the Kindle case where a key copied out of a wrapped text file kept returning 401). Saving a key reports how many stray characters were removed.

## Storage

**Per-book plugin data left KOReader's metadata.lua** (#72).

- Chats now live in `<book>.sdr/koassistant_chats.lua`, and every per-book plugin setting in `<book>.sdr/koassistant_book_settings.lua`, next to the cache and notebook files the plugin already kept there.
- **The move is automatic**: a bulk pass runs once at start-up, with catch-up passes when a book is opened or first touched, and it copies and verifies before removing anything.
- Consequences: KOReader's **"Reset this document"** no longer wipes your chats and per-book settings, and KOReader's optional metadata archive no longer carries chats.
- A book store now follows a mid-session change of KOReader's "Book metadata location" instead of leaving its file behind.

**Backup and restore**

- **Book groups are included in backups** (and per-book settings ride along as well).
- **Restoring a backup made before the chat storage change now imports its chats** instead of restoring them where nothing reads them.
- "Quick: Fresh start" also clears the leftover chat-import backup folder once migration is complete.
- Deleting a notebook now also clears the book's pointer to it, so the book no longer refers to a notebook that is gone.

## Other

- **Console Debug is scoped to the plugin**: turning it on brings back the plugin's own tracing without raising KOReader's global log level (which used to bury it under core's per-paint output). Routine tracing is no longer written to `crash.log` when debug is off, and plugin tracing is also emitted when KOReader's own verbose logging is on. A few per-page-turn lines that Console Debug used to write at the info level moved to the debug level too, and the marking line no longer lists entity names.
- **One long-press menu on every action button.** Holding an action in the highlight menu, the dictionary popup, Quick Actions, an input dialog or the file browser menu now opens the same small menu instead of a description on some surfaces and nothing on others: the description at the top, "Add to" or "Remove from" this menu, "Other placements..." for the rest of its menus, and "Edit...", "Duplicate as custom action..." or "Reset to default". Adding or removing takes effect where you are standing, without a trip to Settings.
- **New `{user_input}` placeholder for custom actions.** Text typed in the input dialog can be placed inside a prompt where you want it, instead of only being appended at the end. It is in the editor's placeholder list as "Typed Input"; before this the placeholder was offered but never filled in, so the braces were sent to the model as they were.
- **The update check reads version tags correctly.** Two-part tags (v0.22) are no longer skipped when looking for the newest release, and pre-release tags sort the way they should: rc.11 is newer than rc.9, alpha comes before beta before rc, and a final release beats its own release candidate.
- The Domain & Research picker opens on the book tab whenever a book is open, from the input dialog's Domain chip and from holding the Quick Settings Domain tile; it used to open on Global until the book had an override of its own.
- Settings rows that open a picker or a manager (Categories and Depth of New X-Rays, the action and domain managers, the menu ordering managers, backups, the index tools, Test Connection, Check for Updates, About) now leave the settings menu open behind them instead of closing the whole menu.
- Section-scoped artifacts are back on the Book Hub (only the X-Ray versions group is filtered out there, since the X-Ray browser owns it).
- **Highlight menu defaults reordered** so the two conditional rows sit last: Translate, Explain, Quick Explain, Summarize, Quick Define, Dictionary, then Look up in X-Ray and Generate Image. Existing users keep their configured list.
- **Edited book metadata is honored everywhere**: a title or author changed in KOReader's Book information now shows and is sent in artifact and notebook pickers, groups, merge labels, the library scan, notebook filenames, backup labels and the chat history browser. The chat history index carries it and refreshes the moment you edit it.
- The chat history browser opens without reading each book's sidecar, which is noticeably faster on a large library.
- The per-book Quick Answer default now resolves the book the action targets, not whichever book is open.
- Quiz generation asks for answer options of comparable length, specificity and style.
- Text extraction reaches the document's last page (whole-document builds used to stop at the start of it), SSE `id:` and `retry:` lines from a streaming server are ignored instead of read as data, nested list bullets are drawn as filled dots at every depth instead of hollow circles and squares, and long code lines wrap in the chat viewer instead of being cut off at the right edge.

## Work in Progress

- **Cross-book lookups, the Group Hub and group settings** are new and touch a lot of surfaces. Device reports welcome; the group settings for chat behavior (tools, web search, effort dials, contexts) are planned for the next version.
- **Request sizing** is verified against a local stub and, for the header path, on a real free Groq key. A live Groq refusal has not been reproduced (Groq admitted the old budget on 2026-09-07), so the refusal path stands on Groq's own wording from the report.
- **AI Book Tools** stays off by default while retrieval quality matures.
- **Setup Wizard v2** is still built but not switched on.

## How You Can Help

- **Device reports**, especially on the X-Ray first-build confirmations, cross-book lookups in a series, and the storage move.
- **Translations**: review passes on [Weblate](https://hosted.weblate.org/engage/koassistant/).
- **Bug reports and feature requests.**

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
