# 2.2

### Enhancement by @jmanoj0905 

- Fix foundation card selection so foundation cards can move back to tableau as documented
- Prevent completed games from being saved again on close
- Reject malformed saved-game data before it can corrupt runtime state
- Polish the board UI with clearer status text, adaptive tableau spacing, improved card rendering, cleaner empty slots, and a less crowded action bar

# 2.1

Enhancement by [TomasDiLeo](https://github.com/TomasDiLeo)

- Adjust font sizes based on screen DPI to keep consistency between devices
- Changed all fonts to the default monospace font in KoReader for consistent alignment
- Refine card drawing logic: center the suits correctly, draw a corner suit on partially drawn cards (piles and stock), enhanced pattern rendering.
- Improve refresh behavior for Eink devices, avoid partial refreshes when unnecessary

# 2.0

**v2.0**

- Draw-3 Mode: Toggle between Draw-1 and Draw-3 with fanned waste pile display
- Game Timer: Tracks elapsed time per game, shown in status bar
- Statistics: Full game stats tracking (wins, losses, streaks, averages, per-mode breakdown)
- Leaderboard: Top 10 best scores with score, moves, time, mode, and date
- Stats & Top buttons: Direct access to statistics and leaderboard from button bar
- Enhanced win message: Shows time, draw mode, new-best indicators, and win streak

# 1.1.1

# 🐛 Bug Fix

- Removed stock card count that was overlapping with tableau cards

**Full Changelog**: https://github.com/Lalocaballero/solitaire.koplugin/compare/v1.1.0...v1.1.1

# 1.1.0

# 🃏 Solitaire v1.1.0 - Undo & Auto-Save

The two most requested features are here!

## ✨ What's New

### ↩️ Undo
- Undo button in the button bar
- Up to 100 moves of history
- Undo count shown in status bar

### 💾 Auto-Save
- Game saves automatically after every move
- Resume your game when reopening
- Save deleted on win or new game

## 📥 Upgrade

1. Delete old `solitaire.koplugin` folder
2. Extract new version to `/koreader/plugins/`
3. Restart KOReader

## 🎮 Buttons

New | Undo | Hint | Auto | Close

---

**Full Changelog**: https://github.com/Lalocaballero/solitaire.koplugin/compare/v1.0.0...v1.1.0
