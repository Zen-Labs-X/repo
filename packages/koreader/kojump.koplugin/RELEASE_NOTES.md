# v1.0.0

# 🧭 Kojump v1.0.0 — Initial Release

We are excited to announce the initial release of **Kojump** (v1.0.0), a lightweight plugin for [KOReader](https://github.com/koreader/koreader) that brings modern web-browser-style navigation history to your e-reading experience. 

Never lose your place again when jumping to footnotes, chapters, indexes, or custom locations. With Kojump, you can seamlessly navigate back and forward through your reading history, view a visual map of your jumps, and resume reading instantly.

---

## 🌟 Key Features

### 🧭 Browser-Style Back & Forward Navigation
Navigate through your jump history just like a web browser. Easily move **Back** to where you were and **Forward** to your newest position. If you navigate back and perform a new jump, Kojump handles branching and prunes forward history automatically.

### 📊 Smart Jump Detection
Kojump automatically detects and records page jumps (where the page changes by more than 1 page, such as clicking footnotes, links, search results, or TOC items), while intelligently ignoring normal consecutive page turns so your history remains clean.

### 🔄 Source Page Retention
If you turn pages manually and then perform a jump, Kojump records your last read page as the source. This ensures that going back returns you exactly to the manual page turn sequence starting point rather than missing it.

### 📜 Rich, Interactive History Menu
View a clear, chronological map of your navigation history in a custom menu containing:
- **Directional indicators** (`←` for previous jumps, `→` for forward jumps, and `•` for the current page).
- **Reading percentages** (e.g., `(15%)`) showing exactly where in the document each jump occurred.
- **Chapter & Section Titles** automatically retrieved from the Table of Contents and safely formatted.

### 💾 Per-Document Persistence
Your jump history and index are saved directly inside KOReader's document settings. Your navigation history is fully preserved across reader restarts, so you can pick up exactly where you left off.

### ⚙️ User-Configurable Capacity
Adjust the maximum history capacity to your preference (from 5 to 100 jumps, default is 20) via the Kojump submenu in the plugins configuration. Reducing the limit immediately prunes older entries and frees up settings storage.

### ⚡ Keybindings & Dispatcher Support
Fully integrated with KOReader's action dispatcher. You can map Kojump actions to gestures, edge swipes, double taps, physical keys, or multiswipes:
- `Kojump: Go Back` (`kojump_back`)
- `Kojump: Go Forward` (`kojump_forward`)
- `Kojump: Show History` (`kojump_show_history`)

---

## 📖 Installation & Usage

For detailed instructions on installation, key gesture mapping, and developer setups, please refer to the project's README.md file.
