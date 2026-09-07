# v1.2.5

- Group dictionary actions in one row.
- Keep separate dictionary actions as the default.
- Add the optional VD Definition unified dictionary action.
- Apply dictionary-button setting changes immediately.
- Refresh update checks from the menu.
- Match definition previews with card details.
- Hide empty language tabs after card changes.

SHA-256: `28d7db29d091bcdcdb66c149f2234cc17a5a0f79bbe0f3adcae64ee078122771`

# v1.2.4

## KOReader compatibility

- Restores **Add to VD**, **VD +AI**, and **Define (VD)** in dictionary popups on KOReader 2026.07.
- Uses KOReader 2026.07's supported archive reader for OTA extraction while retaining the legacy paths needed by KOReader 2026.03.
- Installs the published release ZIP, reports detailed extraction/install errors, and preserves local `vocabdeck_apikeys.lua` and `vocabdeck_configuration.lua` files during OTA updates.

## Study and network fixes

- Includes manually defined and non-AI-enriched cards in study by default. **Study only enriched cards** remains available as an opt-in setting.
- Updates the manual to point to the Dashboard and language deck entries instead of the removed top-level Study item.
- Opens KOReader's Wi-Fi prompt immediately when the radio is off, avoiding the long DNS timeout before single-card or bulk AI enrichment.

## One-time recovery for KOReader 2026.07

If KOReader 2026.07 is running a VocabDeck version older than 1.2.3, **Check for updates cannot install this release** because that installed updater calls an archive API removed by KOReader.

1. Download `vocabdeck.koplugin.zip` from this release.
2. Keep copies of `vocabdeck_apikeys.lua` and `vocabdeck_configuration.lua` if you use them.
3. Manually replace the VocabDeck plugin files, restore those two private files if necessary, and restart KOReader.
4. Future updates can use **Check for updates** normally.

Users on KOReader 2026.03 do not need this recovery. Existing VocabDeck 1.2.3 installations already have the repaired updater and can update normally.

SHA-256: `584457dff11eabba0ea80030d006ed1e474d9eada8c87a5807d546e3ec33c64c`

# v1.2.2

- Restored **Add to VD**, **VD +AI**, and **Define (VD)** in the dictionary popup on KOReader 2026.07 and newer.
- Preserved the legacy dictionary-button integration for older KOReader releases.

# v1.2.1

- Improved update flow: concise update prompt, clearer install progress, and restart request after install.
- Removed the unnecessary post-restart update message.

# v1.2.0

### 🆕 New Features

- **Dashboard** — Deck overview screen with language/book breakdowns, search, and tappable navigation headers.
- **Grammar Helper** — AI grammar explanations for selected text, with translation and e-ink-optimized output.
- **Diagnostics Module** — Troubleshooting screen showing provider, model, API key status, and DB stats.
- **Reverse Study** — Quiz from *meaning → phrase* instead of the default *phrase → meaning*.
- **Auto-Rating** — Cards self-rate based on recall time, with a passive timer on flip and configurable thresholds.
- **Anki Text Import** — Import cards from Anki-formatted text exports.
- **Study History** — View past sessions from your review history log.
- **Move Cards** — Reassign cards between language decks.
- **Lapses Filter** — Sort and filter cards by lapse count.

### 🔧 Improvements

- **Codebase refactoring** — Card list split from a ~1,400-line monolith into four focused modules; shared text utilities extracted.
- **Better error messages** — Clear, specific messages for network failures, timeouts, auth, rate limits, and response errors.
- **Card-state filters** moved into database queries for accurate pagination counts.
- **Clear filters** now resets *all* active card-list filters in one action.
- **Settings** gains submenu navigation (with back button) and an Import option.
- **AI** message construction DRY'd up; define cache added to reduce redundant API calls.
- **Updater** uses a single confirm dialog, shows post-update release notes, and rejects invalid archives.

### 🐛 Fixes

- Source language detection fixes for AI definitions and card listings.
- Grammar highlight properly cleared on AI fetch failure.
- `moveCardToLanguage` INSERT column count fix after schema change.
- Update check menu item no longer keeps menu open after use.
- Database user version now set at initialization for cleaner migration tracking.
- Various dashboard submenu interaction and visual layout fixes.
- AI loader, DB migrations, and grammar cache hardening.
