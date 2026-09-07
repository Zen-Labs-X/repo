# v0.3.0

**Mythos v0.3.0**
---

**What's new:**

<!--himythos-->
- ↺ button on every tab title bar — tap to clear e-ink ghosting instantly
- Smarter screen refreshes — page turns no longer trigger a full flash
- Library Refresh now warns before running (scales with tracked novel count)
- Check for Updates enabled — tap in the menu to check and install on device
- Rapid nav taps no longer stack duplicate fetch calls
<!--/himythos-->

---

**What changed in detail:**
- Main tab panel (Library/Browse/Sources) is now kept alive across rebuilds. Page turns use a partial e-ink repaint, tab switches use a clean non-flashing refresh — no more full screen flash on every navigation
- Ghost-clearing counter added: every 6 page turns, a flash repaint runs automatically to clear accumulated ghosting
- ↺ button added to the top-left of all three main tab title bars for manual ghosting clear on demand
- About dialog and hamburger dropdown now use properly scoped dirty calls, fixing ghosting on open
- Library Refresh shows a confirmation dialog explaining that refresh time scales with how many novels you have tracked, and suggests opening novels individually for targeted updates
- OTA updater fully enabled — Check for Updates in the hamburger menu now triggers on tap. Downloads and installs the update on device, then prompts to restart KOReader
- Updater reads only the `<!-- himythos -->` section from release notes for the on-device update summary
- Rapid taps on Browse page turns and Library Refresh no longer stack multiple concurrent fetch calls
- Browse source picker title simplified to "Browse"

**Installation:**
Download `mythos.koplugin.zip`, extract, and copy the folder into your KOReader plugins directory. If updating, replace the existing `mythos.koplugin` folder, or just use the OTA updater.

# v0.2.0

**Mythos v0.2.0**
---

**What's new:**
- **Update badge** — installed extensions with a newer version available now show a bold update indicator in the Sources list
- **Bug fix** — tapping outside the hamburger menu now correctly closes it instead of opening the About dialog

**Installation:**
Download `mythos.koplugin.zip`, extract, and copy the folder into your KOReader plugins directory. If updating from 0.1.0, replace the existing `mythos.koplugin` folder.

# v0.1.0

**Mythos v0.1.0 — Initial Release**
---

The first public release of Mythos, a web novel library plugin for KOReader.

**What's included:**
- Browse popular titles and search by name directly on your e-reader
- Track novels in your library and refresh to catch new chapters
- Select individual chapters or entire series for export
- Export as a single EPUB, one per chapter, or split into volumes
- EPUBs include cover art and are saved to `Mythos/Series/` on your device
- Extension system — install sources from a GitHub repo without updating the plugin

**Installation:**
Download `mythos.koplugin.zip`, extract, and copy the folder into your KOReader plugins directory.
