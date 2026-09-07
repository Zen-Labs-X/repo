# v1.0.8

Fixes stale entity footnotes surviving Clear Cache. That action wipes self.characters/historical_figures/locations/terms - the entity lists our scan is built from - but our overlay had no way to know it happened, so the underline overlay and tap targets kept showing entity mentions from the book's now-discarded data until something unrelated (a settings toggle, opening the menu on the next book) happened to trigger a rescan.

Hooked Clear Cache the same way the existing init/getSubMenuItems hooks work: it now also clears our in-memory scan state (underlines, tap targets, matched-by-page buckets) and deletes the on-disk entity cache file, so a stale signature can't get reused later if a fresh fetch happens to reproduce the same entity names.

Scope: this only affected the explicit "Clear Cache" menu action. Normal book close/reopen and settings-toggle rescans were already correct.

# v1.0.7

Fixes false-positive underlines: common lowercase words that share spelling with a proper noun (e.g. "black" the color vs "Black" the character) and lowercase substrings inside unrelated words (e.g. "than" containing "han") were being underlined as entity mentions.

Entity matching now runs case-sensitively: names and aliases only match their original (proper-noun) capitalization, instead of matching any case. This is a tighter filter than `\b` word boundaries alone, since word boundaries don't protect against a short name legitimately appearing, lowercase, as a substring inside a longer unrelated word's letters.

Trade-off: text in ALL-CAPS (some chapter headers or title pages) will no longer be underlined, since it won't case-match. Noted in the README's Known limitations.

# v1.0.6

Fixes the 0-entities-found bug. The new checkRegex diagnostic from v1.0.5 returned error code 102 (error_escape in crengine's own error table) - an invalid escape sequence. escape_pattern was backslash-escaping "-" and "%", neither of which is special in ECMAScript regex outside a character class; "\%" specifically isn't a recognized escape and made the whole search engine (SRELL) reject the pattern, silently returning zero hits for that entity category. With 84 glossary "term" entries in the test book, a hyphen or percent sign somewhere in there was very plausible.

Restricted escaping to the actual ECMAScript special characters. Verified the fix against sample inputs (including a term with a percent sign and one with a hyphen) in an isolated sandbox before shipping.

If this still doesn't find anything, the scan failure log now includes the full pattern text, not just its length - please share that line from crash.log if so.

# v1.0.5

Fixes the actual cause of the still-raw strings: userpatch.registerPatchPluginFunc runs the plugin's own init() before calling our patch function, so wrapping init() from inside the patch is already too late for the first book opened each session - confirmed by pulling the on-device log, where our setup code never ran at all despite the class-table patch succeeding.

Setup (localization injection + mounting the underline/tap overlays) now also runs from the X-Ray menu hook, which is guaranteed to fire correctly regardless of which book opens first.

Also adds diagnostics (doc:checkRegex probe, pattern length/chunk index) around the "findAllText pcall failed: nil" scan failure, which is still unresolved - if scanning still finds 0 after this update, please pull crash.log again and share lines containing "EntityFootnotesPatch: scanBookForEntities: findAllText failed".

# v1.0.4

Fixes scanning finding 0 matches. The v1.0.1 boundary-matching change (replacing \b with a hand-built boundary pattern) was based on an incorrect diagnosis - crengine's regex engine (SRELL) is a real ECMAScript-compliant library that supports \b correctly, confirmed by reading its C++ source. The replacement pattern most likely failed to compile, which makes the search silently return zero hits. Reverted to the original \b(...)\b matching.

Also adds diagnostic logging (term counts at scan start, and separate log lines for each init step) so if something still doesn't work, we can actually see why from the KOReader log instead of guessing again.

The localization-injection fix from v1.0.3 is unchanged and still needs verification - if strings are still showing as raw keys after this update, please check the KOReader log for lines starting with "EntityFootnotesPatch:" and share what they say.
