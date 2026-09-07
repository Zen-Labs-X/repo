# KoStats – KOReader Statistics Analyzer

A free web-based statistics dashboard for [KOReader](https://koreader.rocks/) hosted at [thepixelpro.de/KoStatsMulti](https://thepixelpro.de/KoStatsMulti/). Upload your KOReader database via a KOReader plugin and get detailed insights into your reading habits.

---

## Installation

### 1. Create your personal dashboard

Go to [thepixelpro.de/KoStatsMulti](https://thepixelpro.de/KoStatsMulti/) and either:
- Enter your own 8-digit key, or
- Use a pre-generated key

**Write this key down — you will need it later.**

You will be redirected to your personal dashboard. It will show "no data" until you upload your statistics.

### 2. Install the KOReader plugin

- Download the plugin from the [releases page](https://github.com/ThePixelPro/KoStatsMulti/releases)
- Extract the zip and place the folder into `koreader/plugins/`
- Restart KOReader

### 3. Configure the plugin

Open a book or the file browser, then open the first menu — you should see an **Upload Statistic** option. Go to **Settings** and configure:

- **Server URL:** Your dashboard URL with `index.html` replaced by `upload.php`
  - Example: `https://thepixelpro.de/KoStatsMulti/12345678/index.html`
  - Becomes: `https://thepixelpro.de/KoStatsMulti/12345678/upload.php`
- **Secret Key:** Your 8-digit access code

### 4. Upload your statistics

Go back and click **Upload Statistic**. Your reading statistics will now appear in the dashboard.

---

## Troubleshooting

| Error | Likely Cause |
|---|---|
| **404** | Wrong server URL — double check it |
| **403** | Wrong secret key |
| **Host/Service Unknown** | Network issue — try again |
| **500** | Internal server error — make sure the KOReader statistics plugin is enabled. If the problem persists, please comment below |

---

## Features

### 📚 Books
- Grid and list view of all books
- Search by title, filter by minimum pages read
- Sort by title or reading time
- Automatic cover fetching via Google Books API
- Manual cover search override
- Progress bars per book

### 📖 Book Detail
- Total pages, reading time, active days, avg speed
- Per-book reading calendar
- Reading milestones timeline (First Open, Halfway, Completed, and more)
- Annotations panel (highlights & notes)
- **Page Activity Chart** — time spent per page visualized as a bar chart

### 📊 Reading Statistics
- Total reading time, pages, longest day stats
- Reading heatmap (last 52 weeks, color-coded by book)
- Weekly stats with prev/next navigation
- Day-of-week and monthly reading time charts
- Books overview table

### 🧾 Yearly Recap
- Active days with animated progress ring
- Books finished, longest streak, best month
- Total reading time, avg session, longest session
- Month-by-month breakdown with book covers
- Year selector and JSON export

### 📖 Insights
- Reading streaks (current, longest, total days)
- Reading speed (pages/hour, estimated words/minute)
- Time-of-day and day-of-week reading patterns
- Author diversity tracking

### ✨ Highlights
- Browse all highlights from your KOReader annotations
- Filter by book, color, language
- Sort by date or book
- Group by book toggle

### ⚖️ Compare
- Book vs Book
- Month vs Month
- Year vs Year

### 🎯 Goals & Achievements
- Set daily/weekly/monthly/yearly page goals
- Achievement badges
- Reading challenges (30-day streak, genre diversity, book marathon)

---

## Themes

8 built-in themes — Light (Default), Light Sand, Light Mint, Light Rose, Dark (Default), Dark Ocean, Dark Grape, Dark Slate. Your theme is saved and persists across sessions.

---

## Privacy Notice

Reading statistics are uploaded voluntarily by the user and stored on the server solely to display personal reading statistics. If you would like your data deleted, send a direct message with your access code.

---

## Tech Stack

- **Frontend:** Vanilla JavaScript, HTML, CSS
- **Database:** [sql.js](https://github.com/sql-js/sql.js) — SQLite processed client-side in the browser via WebAssembly
- **Charts:** [Chart.js](https://www.chartjs.org/)
- **Backend:** PHP (upload & access code management)
