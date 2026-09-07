# KoCharacters — KOReader Plugin

Automatically extract, track, and enrich character profiles from your books using the **Google Gemini AI API** (free tier). Generate AI portraits using **Google Imagen**. Runs on KOReader on Kindle and other supported devices.

---

## How to get API keys

### Gemini (character extraction — free)

1. Go to **aistudio.google.com** and sign in with your Google account
2. Click **"Get API key"** in the left sidebar
3. Click **"Create API key"** — choose "Create API key in new project"
4. Copy the key (it starts with `AIza…`)
5. No credit card required — free tier gives 500 requests/day and 1M tokens/day

### Imagen (portrait generation — paid)

Portrait generation uses the Google Imagen API, which requires a Google Cloud project with billing enabled. The same key format (`AIza…`) is used but must be created in Google AI Studio with Imagen access enabled. Imagen charges per image generated.

---

## Installation

1. Copy the `kocharacters.koplugin/` folder into your KOReader `plugins/` directory
2. Restart KOReader
3. Open any book, tap the menu → **KoCharacters** → **Settings...** → **AI Settings...**
4. Paste your Gemini Character Extraction key
5. Optionally paste your Gemini Image Generation key to enable portrait generation

---

## Menu overview

All actions live under the reader menu → **KoCharacters**:

| Menu item | What it does |
|---|---|
| **Extract characters from this page** | Sends the current page text to Gemini and saves any characters found or updated |
| **Scan current chapter** | Scans every page in the current chapter, 4 pages per Gemini call |
| **Scan specific chapter** | Shows a list of all chapters (with scan status) so you can pick one to scan |
| **View saved characters** | Browse the full character list; tap a name to see their profile and take actions |
| **Re-analyze character** | Pick a character and re-run Gemini against the current page to enrich their profile |
| **View relationship map** | Gemini reads all saved profiles and produces a text relationship map |
| **Cleanup all characters** | Batch-deduplicates redundant text in all character profiles via Gemini, then detects and offers to merge characters that are almost certainly the same person |
| **Generate portraits** | Select one or more characters to generate AI portraits via Imagen |
| **Export...** | Export character list (HTML), Export as ZIP (HTML + portraits), or Upload to server |
| **Settings...** | Configure keys, auto-extract, indicators, spoiler protection, and prompts |

### Character detail screen

Tapping a character in the list opens their profile with two rows of actions:

| Row | Buttons |
|---|---|
| **Row 1** | Generate Portrait — Merge into... — Delete Character |
| **Row 2** | Re-analyze — Clean up — Edit |

The same actions are available when using **Find character** by selecting text in the book.

---

## How it works

### Character extraction

1. The plugin reads the current page text by parsing the epub directly via `unzip` — this is the most reliable method on the supported KOReader build
2. It loads all already-known characters for this book from the local JSON database
3. Known characters whose name or alias appears in the page text are passed to Gemini as **full profiles to update**; the rest are passed as a **skip list**
4. Gemini returns a JSON object containing new/updated character profiles and an updated **book context** summary
5. New characters are inserted into the database; existing characters are fully updated in-place with enriched information
6. Scanned pages are tracked in a sidecar file so they are never re-processed

### Book context (auto-built)

Each extraction call asks Gemini to maintain a 2–3 sentence summary of the book's genre, setting, country/region, and historical era. This context is:

- Extracted from the **same Gemini call** as character data — no extra API calls
- Passed back to Gemini on every subsequent call so it builds cumulatively as you read
- Used automatically in portrait generation prompts to ensure historically accurate clothing, style, and setting
- Viewable and clearable from **Settings... → AI Settings... → View book context**

### Incremental enrichment

Every time a known character appears on a scanned page, their full current profile is sent to Gemini alongside the page text. Gemini merges any new details — additional appearance clues, personality traits inferred from actions, new relationships — into the existing profile. Profiles build up progressively as you read.

Gemini is instructed to write **synthesised descriptions, not event logs** — personality fields read as character traits ("reckless and fiercely loyal") rather than lists of actions.

There are two enrichment paths depending on how Gemini names the character:

- **Exact name match** — Gemini returns "John" and "John" already exists. The existing record is silently replaced with the updated version. This is the normal path.
- **Near-duplicate name** — Gemini returns "Jon" or "Mr. Smith" for an existing "John" or "Smith" (Levenshtein distance ≤ 2, or one name is a substring of the other). The plugin merges the new details into the existing record and sets the **"cleanup needed"** flag.

### Duplicate and conflict detection

When Gemini returns characters that look like existing ones (Levenshtein distance ≤ 2, or one name is a substring of another), the plugin detects the conflict and enriches the existing character rather than creating a duplicate. Within a single Gemini response, near-duplicates are collapsed before insertion.

### Auto-extract

When enabled, the plugin automatically scans each new page as you turn to it, after a configurable debounce delay (default 10 seconds). A small **scanning icon** appears in the top-left corner while the Gemini call is in progress. When the call completes, the icon is replaced by a **character count badge** showing how many characters were found or updated, which fades after 4 seconds. Both indicators can be disabled in Settings.

### Offline / pending pages

When a page scan fails due to a network error (e.g. the Kindle is in flight mode), the page number is saved to a `pending_pages.json` sidecar. The next time auto-extract successfully completes a scan while connected, you are prompted: "N page(s) couldn't be scanned while offline — scan them now?" Accepting replays the failed pages in the same batched, rate-limited manner as chapter scan.

### Chapter scan

Scans every page in a chapter in batches of 4 pages per Gemini call, sleeping 3 seconds between batches to stay within the free-tier rate limit (15 RPM). The "Scan specific chapter" option shows all TOC chapters with their page ranges and a scan status indicator (`[✓ done]`, `[~ N/M pages]`, or unseen).

### Cleanup needed

The **KoCharacters** menu title shows **"— cleanup needed"** when auto-extract has enriched one or more existing characters but skipped the Gemini deduplication pass to avoid blocking. Over multiple page scans, enriched fields can accumulate redundant phrases (e.g. "brave; brave" or "tall with dark hair; tall, dark hair").

Run **"Cleanup all characters"** to send all affected profiles to Gemini for a single deduplication pass. The flag also clears automatically at the end of a chapter scan.

After the text cleanup pass, the plugin runs a second Gemini call across all character profiles to detect characters that are almost certainly the same person (e.g. a character referred to by their first name in some chapters and by a title or surname in others). Gemini requires strong evidence across multiple fields before suggesting a merge — name similarity alone is not enough. For each high-confidence match found, a confirmation dialog shows the two names and the reason for the suggestion; you can merge or skip each one individually. Merging combines aliases, relationships, physical description, and personality into the kept record.

### Portrait generation

Portraits are generated via the **Google Imagen API** and saved as PNG files inside the book's data folder. The portrait prompt is built automatically from the character's appearance, personality, occupation, and the book context, and is styled to match the era and setting of the book.

- **Batch generation** — select any number of characters from a list; characters that already have a portrait are marked with `[img]`
- **Portrait filename** is stored on the character record so the image link survives name renames
- **Model selection** — choose between fast, standard, or ultra Imagen models in AI Settings
- Portraits are embedded in the HTML export with a **lightbox** (click to enlarge)

### Spoiler protection

Characters have an `unlocked` field. When spoiler protection is enabled in Settings, characters first seen beyond your current page are shown as `[SPOILER]` in the browser. Tapping a spoiler entry unlocks it.

### Relationship map

Sends all saved character profiles to Gemini in one call and asks it to produce a text-based relationship map, listing each character's connections with short relationship labels.

### Gesture and hardware button shortcuts

The plugin registers six actions with KOReader's **Dispatcher**, which means any of them can be bound to a swipe gesture or hardware button in KOReader's gesture/button settings:

| Action name | What it does |
|---|---|
| KoCharacters: Extract from page | Runs extraction on the current page |
| KoCharacters: Scan chapter | Scans the current chapter |
| KoCharacters: View characters | Opens the character browser |
| KoCharacters: Re-analyze character… | Opens the character picker for re-analysis |
| KoCharacters: View API usage | Shows the usage log |
| KoCharacters: View relationship map | Generates and shows the relationship map |

### Export

**Export character list** produces a styled HTML file with all characters, their profiles, and any generated portraits. Portraits appear on the left with character info on the right; clicking a portrait opens a full-screen lightbox.

**Export as ZIP** bundles the HTML file and the portraits folder into a single `.zip` file, ready to copy to another device.

Both exports are saved inside the book's data folder (`kocharacters/<book_id>/`).

**Upload to server** packages the character database, book metadata, and portraits into a `.tar.gz` archive and POSTs it to a configurable HTTP endpoint (e.g. a personal web app or home server) via `curl`. The endpoint URL and optional API key (`X-Api-Key` header) are set under **Settings... → Export settings**. The archive is deleted from the device after upload completes.

---

## Data storage

All files for a book are stored together in a single subdirectory named after the book title:

| Path | Contents |
|---|---|
| `<koreader_data>/kocharacters/<book_id>/characters.json` | Per-book character database |
| `<koreader_data>/kocharacters/<book_id>/scanned.json` | Scanned page index |
| `<koreader_data>/kocharacters/<book_id>/book_context.txt` | Auto-built genre/era/setting summary |
| `<koreader_data>/kocharacters/<book_id>/portraits/` | Generated portrait images |
| `<koreader_data>/kocharacters/<book_id>/pending_pages.json` | Page numbers that failed to scan while offline |
| `<koreader_data>/kocharacters/<book_id>/pending_cleanup` | Flag file: present when one or more characters need cleanup |
| `<koreader_data>/kocharacters/<book_id>/characters.html` | Exported character list |
| `<koreader_data>/kocharacters/<book_id>/characters.zip` | Exported ZIP (HTML + portraits) |
| `<koreader_data>/kocharacters/usage_stats.json` | Daily API usage log (shared across books) |

The book ID is derived from the sanitized book title and a byte-sum hash of the file path — no MD5, no document API calls required.

---

## Character profile fields

| Field | Description |
|---|---|
| **Name** | Full name or best available name |
| **Aliases** | Nicknames, titles, alternate names |
| **Role** | protagonist / antagonist / supporting / unknown |
| **Occupation** | Job title or role in society (e.g. blacksmith, spy, physician) |
| **Physical description** | Appearance details from explicit descriptions |
| **Personality** | Stable traits synthesised from behaviour |
| **Relationships** | Connections to other named characters |
| **First appearance quote** | Short verbatim quote from the text |
| **Notes** | User-editable free text field |
| **Last updated** | Page number of the most recent update |

---

## Settings

### AI Settings (submenu)

| Setting | Description |
|---|---|
| **Gemini Character Extraction key** | API key used for character extraction, cleanup, and relationship mapping |
| **Gemini Image Generation key** | API key used for portrait generation via Imagen |
| **Imagen model** | Choose between `imagen-4.0-fast-generate-001`, `imagen-4.0-generate-001`, or `imagen-4.0-ultra-generate-001` |
| **Edit extraction prompt** | Customise the prompt sent to Gemini for character extraction |
| **Edit cleanup prompt** | Customise the deduplication prompt |
| **Edit re-analyze prompt** | Customise the re-analysis prompt |
| **Edit relationship map prompt** | Customise the relationship map prompt |
| **Edit portrait prompt** | Customise the Imagen portrait generation prompt |
| **Edit merge detection prompt** | Customise the prompt used to detect duplicate characters during cleanup |
| **View book context** | View the auto-built genre/era/setting summary; option to clear it |

### General settings

| Setting | Description |
|---|---|
| **Auto-extract on page turn** | Automatically scan each page as you read |
| **Auto-extract delay** | Seconds to wait after a page turn before calling Gemini (default 10s) |
| **Cleanup batch size** | Characters sent to Gemini per cleanup request (default 5); lower values use more API calls but stay safely under the rate limit |
| **Detect duplicates after cleanup** | When ON, automatically runs merge-detection after each cleanup pass |
| **Scan indicator icon** | Show/hide the scanning and count icons in the top-left corner |
| **Auto-accept enrichments** | Silently enrich existing characters when near-duplicates are detected, instead of prompting |
| **Spoiler protection** | Hide characters first seen beyond your current page |
| **Character detail view** | **Text** — plain scrollable viewer; **HTML (with portrait)** — richer layout with the AI-generated portrait image embedded |
| **View API usage** | Daily log of Gemini text calls and Imagen image generations |
| **Export settings** | Configure the upload endpoint URL and optional API key for "Upload to server" |
| **Clear character database** | Delete all saved characters for the current book |
| **Reset prompts to default** | Restore all prompts to their built-in defaults |

---

## Requirements

- KOReader with `ssl.https` / `ltn12` support (standard on Kindle builds)
- A free Google Gemini API key from aistudio.google.com (for character extraction)
- A Google Imagen API key (optional, for portrait generation)
- `unzip` available on the device (standard on Kindle)
- `base64` and `curl` available on the device (standard on Kindle, required for portrait generation and server upload)
- `zip` available on the device (required for ZIP export — standard on Kindle via BusyBox)
- `tar` available on the device (required for "Upload to server" — standard on Kindle via BusyBox)
