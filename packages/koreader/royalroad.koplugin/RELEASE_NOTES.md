# v0.21.0

## 🚀 Features
- feat(ui): show the reading-progress bar in list view too

## 🐛 Bug Fixes
- fix(epub): stop chapter titles accumulating HTML entities
- fix(ui): repaint the screen when the chapter-range dialog closes
- fix(ui): make the mosaic reading-progress bar actually show progress

# v0.20.1

## 🐛 Bug Fixes
- fix(epub): keep the contents out of the spine so reading positions survive

# v0.20.0

## 🚀 Features
- feat(epub): add an in-book contents page

## 🐛 Bug Fixes
- fix(epub): put the contents page ahead of the chapters
- fix(ui): rebuild the downloads list when the new-chapters badge is cleared

## 🧰 Maintenance
- docs: track CLAUDE.md pointing at AGENTS.md

# v0.19.0

## 🚀 Features
- feat: add a manual "clear new-chapters badge" action per story
- feat: remove the "Refresh cover" action

## 🐛 Bug Fixes
- fix(ui): label the badge-clear button "Clear new status"
- fix: clear the new-chapters ribbon at the start of every update check
- fix(parser): pick up chapters that belong to no volume

## 🧰 Maintenance
- docs(site): restyle landing page and fix walkthrough layout bugs
- docs: refresh README screenshots and note reading progress

# v0.18.8

## 🚀 Features
- feat: show reading progress on manage-downloads page

## 🐛 Bug Fixes
- fix(parser): strip hidden watermark elements from chapter content
