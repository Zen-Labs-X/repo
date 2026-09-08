# v0.3.0

## What's new

- **Chinese localization** — the plugin now follows KOReader's UI language. Switch KOReader to 简体中文 / 繁體中文 and the whole plugin (menus, break screens, settings, help) shows in Chinese; other languages stay English.
- The status-bar countdown adapts: `5分钟后☕` in Chinese, `☕in 5min` in English.
- Added a [Simplified Chinese README](README.zh-CN.md) with a language switcher.

Translations live in `l10n_zh.lua` — easy to review or extend.

## Install

Download `eyerest.koplugin.zip` below, unzip, and drop the `eyerest.koplugin` folder into KOReader's `plugins/` directory. See the README for details.

# v0.2.0

## What's new

- **Sleep timer** — a one-shot countdown (e.g. read for one hour) that ends with a full-screen "time to sleep" reminder. Independent of the eye breaks; survives sleep/wake.
- **Pause removed** — it overlapped with Skip / *Read a bit more* and the main enable switch, so it's gone in favour of the Sleep timer.
- **Clearer time displays** — the next break shows in minutes in the menu title and status line (e.g. *Eye Rest (next break in ~18 min)*); break durations read as "20 s" / "5 min" instead of ambiguous MM:SS.
- Header countdown no longer needs KOReader's external-content toggle (footer still does).
- Fixed an unrenderable glyph in the *How Eye Rest works* diagram.

## Fixes carried from 0.1.x
- Postpone now honours durations longer than the break interval.
- Status bar refreshes correctly after a break closes.

# v0.1.0

First public release.

A Stretchly-style break reminder for KOReader. It nudges you to rest your eyes with **mini breaks** and periodic **long breaks**, timed by how long you actually read.

## Features
- One **Enable breaks** switch — no alarm/interval juggling.
- Timing follows the **20-20-20 rule** by default (20 min reading → 20 s break; a 5 min long break every 2 mini breaks).
- Counting pauses when you **close the book** or the **device sleeps**.
- Full-screen **countdown break screen** that ignores stray taps; **Skip** / **Read a bit more** on normal breaks, unskippable in **Strict mode**.
- E-ink-friendly segmented countdown (~5 refreshes per break).
- Optional countdown in the **header / footer** status bar.
- All durations adjustable down to seconds.

## Install
Copy the `eyerest.koplugin` folder into KOReader's `plugins/` directory, disable the built-in *Read timer* (they share a menu slot), and restart. See the README for details.
