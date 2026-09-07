# v1.3.0

What's new in 1.3.0:

- **Save for later** — flag an article as *to-read* the moment you spot it, then come back to it. Save from the articles list (long-press → Save for later), from a link in the text (hold until the selection menu opens → Save for later), or with the new **Backlog: save current for later** action. Saved articles show a ☆ and gather in a **Saved** group at the top of the list.
- **Jump to next saved** — a new bindable action that walks you through your saved articles, alongside the existing jump-to-next-unread.
- **Exclusive states** — every article is exactly one of unread, ☆ saved, or ✓ read: saving an already-read article moves it back to your to-read list, and finishing a saved article marks it read.
- **README** rewritten around an article-level model and de-duplicated.

**Install:** download `backlog.koplugin-v1.3.0.zip`, extract into your device's `koreader/plugins/` directory, and restart KOReader. Or update in place via the App Store plugin.

# v1.2.0

What's new in 1.2.0:

- **Section-grouped magazines** — for EPUBs whose table of contents nests articles under sections (e.g. The Economist), Backlog now tracks the individual articles and groups them under a header per section, each with its own read count. Tap a section header to jump to its first article, or long-press it to mark the whole section read. Flat anthologies are unchanged. (#1)
- **Smarter auto-mark** — an article is marked read when you turn *past* its last page (i.e. when you finish it and move on), not the instant its last page appears; the final article is marked when you reach the end of the book. (#2)
- **Notification toggle** — a new **Show read notifications** option (under **Tools → Backlog**) silences the "marked read" popup; the ✓ still shows in the articles list. The previous four auto-mark modes are replaced by a single on/off **Auto-mark articles read** toggle. (#2)

**Install:** download `backlog.koplugin-v1.2.0.zip`, extract into your device's `koreader/plugins/` directory, and restart KOReader. Or update in place via the App Store plugin.

# v1.1.0

What's new in 1.1.0:

- **Faded cross-references** — in-text links to articles you've already read are now dimmed, like visited web links, so you can see at a glance which references you've been through. Strength is configurable (Off / Subtle / Medium / Strong) under **Tools → Backlog → Fade links to read articles**. No reflow — it's painted over the page.
- **Articles list** now shows the current (▶) and read (✓) markers in separate columns, so a current article that's also read shows both.
- **Moved to the Tools menu** (from More tools) for quicker access.

**Install:** download `backlog.koplugin-v1.1.0.zip`, extract into your device's `koreader/plugins/` directory, restart KOReader. Or update in place via the App Store plugin.

# v1.0.0

Per-chapter read tracking for anthology EPUBs in KOReader — collections of standalone, cross-linked articles you read in any order (blog archives, essay collections). Shows which articles you've read, jumps to the next unread, and auto-marks as you finish reading one.

**Install:** download `backlog.koplugin-v1.0.0.zip`, extract it into your device's `koreader/plugins/` directory, then restart KOReader. The zip extracts to a correctly-named `backlog.koplugin/` folder.

See the README for usage and settings.
