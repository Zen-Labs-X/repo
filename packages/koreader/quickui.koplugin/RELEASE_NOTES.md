# v1.0.4

## What's Changed
- Fix crash when removing last bottom bar tab (empty tab list handling)
- Fix residual touch handler when removing the rightmost bottom bar tab
- Fix Deselect All not showing when bottom bar tab count reaches max limit
- Move Remove button next to Save in built-in action edit dialog
- Adjust title and author font size in list view
- Fix placeholder cover dim effect not showing when selected in filemanager
- Add 'Hide in PDF' option for bottom bar
- Improve Chinese translations
- 修复底部栏移除最后一个按钮时崩溃闪退的问题（无按钮时显示提示性文字）
- 修复底部栏移除最右边按钮后触摸区域仍为旧按钮的问题
- 修复底部栏因达数量限制而无法批量移除所有按钮的问题
- 将内置动作编辑框的移除按钮放至保存按钮左侧（保持与自定义动作编辑框相同布局）
- 调整显示模式列表视图下标题及作者字体大小（解决字体过大的问题）
- 修复无封面书籍的占位封面及列表视图下的书籍封面无选中效果的问题
- 添加在PDF中隐藏底部栏选项
- 完善中文翻译

# v1.0.3

## What's Changed

- Expose QuickUI bottom bar height globally for SimpleUI compatibility
- Ddisable auto-keyboard popup on action edit dialogs to prevent accidental triggers
- Display release notes when new version is found
- Remove the name field to be compatible with KOReader v2026.07

# v1.0.2

## What's Changed

- feat(bottombar): add overlap toggle for reader view
- fix(qa_settings): hide Remove button when creating new custom action
- fix(main): read plugin version from _meta.lua dynamically
- i18n: add translations for overlap mode

# v1.0.1

## What's Changed

- fix(bottombar): clean up old instance before rebuild to fix overlap #2

# v1.0.0

## What's Changed

- Quick Actions: Built-in actions (WiFi, night mode, rotate, screenshot, continue reading, search, restart, quit, power, HTTP server, font list, etc.)
- Quick Actions: Custom actions (folders, collections, plugins, system actions, recorded menu actions)
- Quick Actions: Icon picker with Nerd Font and SVG/PNG support
- Quick Actions: System icon override and UI font switcher
- Quick Actions: Interface filter to show/hide actions based on current view (File Manager/Reader)
- Quick Actions: Customizable panel with button shapes, sizes, labels, and sliders (frontlight/warmth)
- Quick Actions: Bottom navigation bar with configurable tabs, styles, and colors
- Cover Visuals: Placeholder covers (simple/gradient) with title/author
- Cover Visuals: Badges (favorite, progress, NEW, page count, format)
- Cover Visuals: Rounded corners and unified aspect ratio (3:4/2:3)
- Cover Visuals: Folder cover previews (Gallery/Stack/Normal/None)
- Cover Visuals: Title/author below cover, title banner on cover
- Cloze Mode: Mask annotations (highlights, underlines, strikeouts, inversions)
- Cloze Mode: Three toggle modes (double-tap, single-tap block menu, single-tap show menu)
- Header & Footer: Display time, page numbers, progress, chapter info, author, title, battery
- Header & Footer: Customizable positions, font face/size/bold, padding, offsets
- Unified settings management with configuration stored in quickui.lua
- Gesture support: Quick Actions Panel, Settings, Cover Settings, Toggle Cloze Mode
- Online update: Check for updates from GitHub (Latest/Pre-release) and Gitee
- i18n support: Chinese translation included
- Inspired by SimpleUI, ZenUI, and ShortcutsToolbar
