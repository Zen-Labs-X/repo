# v3.1.0

# Release v3.1.0

## What's Changed / 变更说明

### 中文 (Simplified Chinese)
- **自定义底部页脚与状态栏**：新增基于 ViewModule 与 Blitbuffer 的独立绘制页脚，突破原生 ReaderFooter 限制，支持两端对齐、居中、古典页码与微型阅读进度条。
- **9 组精选设备与状态栏预设**：涵盖 Kindle、Kobo、Kobo 双端、掌阅、汉王、文石、微信读书、极简纯页码与现代全功能风格。
- **丰富插槽类型与分割线**：支持 12h/24h 时钟、章节名、书名、作者、动态电池图标与电量、组合进度、预计剩余时间、普通/古典页码、实线/虚线/点线/微型进度条等。
- **原生状态栏智能联动**：支持在插件内一键切换隐藏/显示 KOReader 原生顶部与底部状态栏，避免双重状态栏重叠。
- **菜单交互优化**：新增改动后实时预览机制（无缝接管层），优化关闭文档时的常驻窗口清理。
- **规范与工程化完善**：新增根目录 AGPL-3.0 LICENSE 文件，完善测试用例与打包过滤规则。

### English
- **Custom Bottom Footer & Status Bar**: Added standalone ViewModule and Blitbuffer rendering for footers, supporting justified/centered text, classical page numbering, and micro progress bars.
- **9 Curated Device & Status Bar Presets**: Includes Kindle, Kobo, Kobo Dual, iReader, Hanvon, BOOX, WeChat Read, Minimalist, and Modern layouts.
- **Rich Slot Items & Dividers**: Supports 12h/24h clocks, chapter title, book title, author, dynamic battery icons, combined progress, estimated reading time, classical page numbers, and custom divider lines/progress bars.
- **Native Status Bar Integration**: Seamlessly toggle native KOReader top/bottom status bars directly within the plugin to prevent overlap.
- **Menu Preview & Lifecycle Enhancements**: Added full-screen live preview with touch dismissal and improved window cleanup on document close.
- **Packaging & Compliance**: Added root AGPL-3.0 LICENSE file, expanded test specifications, and improved build packaging filters.

# v3.0.5

# Release v3.0.5

## What's Changed / 变更说明

### 中文 (Simplified Chinese)
- **内置预设保护**：修复套用内置预设（如研读笔记）时静默关闭对话高亮、强调点与跳过引用块绘制器的问题。现在仅覆盖预设声明的字段，读者已调好的绘制器与个性化设置完整保留。
- **预设导入导出健壮性**：修复首字下沉倍数（`drop_caps.scale`）因浮点数被整数规则误拒导致无法跨设备导入的缺陷；补充标题边框居中与章节分页规则；加入显式 NaN 防护。
- **排版体检可视化标记**：修复体检问题标记画笔空转的问题。开启后可直接在页面上高亮标出「首字下沉首段全角空格」与「未开启跳过时的居中段落」。
- **跨页段落对话精准着色**：修复从上一页跨页续接的段落因偏移叠加导致引号着色错位的问题；改用语义索引清洗后的文本基准，彻底杜绝着色漂移。
- **对话高亮引擎与性能优化**：段落引号扫描改为单次执行多处共用；优化整句连续引号的快速着色通道；明确「有引号即高亮」的判定原则，真机实测对话召回率达 100%。
- **全页 HTML 预检与引用块跳过**：统一整页与逐行引用判定规则；引入整页结构化 HTML 预检机制，普通页面翻页原生调用开销降低约 95%，且对旧版 KOReader 自动兼容降级。
- **工程化与自动化测试**：新增 6 项针对预设套用、编解码校验、体检标记、跨页对话着色的自动化回归测试；提供标准的 Python 自动化打包脚本。

---

### English
- **Built-in Presets Protection**: Fixed an issue where applying built-in presets (e.g. Study Notes) inadvertently disabled dialogue highlights, emphasis marks, and blockquote skip painters. Presets now clone the current configuration and only override explicitly defined fields.
- **Preset Import/Export Robustness**: Fixed drop caps scale (`drop_caps.scale`) float rejection during import; added missing validation rules for centered heading borders and chapter page breaks; added explicit NaN guards.
- **Visual Health Check Markings**: Fixed non-rendering health check findings overlay. Visual markers now accurately flag leading full-width spaces under drop caps and unskipped centered paragraphs on the visible page.
- **Cross-page Dialogue Alignment**: Fixed highlighting offsets on paragraphs continued from previous pages caused by overlapping coordinate baselines; now references sanitized semantic index text.
- **Dialogue Highlighting Optimization**: Quote scanning is now performed once per paragraph; optimized fast-path rendering for single contiguous quotes; standardized full quote recall policy (100% recall on tested books).
- **Full-page HTML Precheck & Blockquote Skipping**: Unified page-level and line-level blockquote tag matching; introduced full-page HTML precheck to reduce native engine calls by ~95% on non-quote pages with graceful fallback for older KOReader versions.
- **Testing & Packaging**: Added 6 automated regression specs covering preset application, codec schemas, health check diagnostics, and dialogue offsets; included automated Python packaging script.

# v2.1.2

# Release v2.1.2

## What's Changed / 变更说明

### 中文 (Simplified Chinese)
- **目录/章节跳转绘制崩溃修复**：直接绘制模式下对 `crengine` 行框及双页 `xpointer` 查询增加 `pcall` 护栏机制并校验指针有序性。跳转瞬间若原生侧无法提供稳态行框，自动跳过当前帧画线，彻底解决崩进 `ReaderView.paintTo` 渲染循环引发闪退的问题。
- **开书按书重写 CSS 状态**：在 `onReaderReady` 钩子中按当前书 `typefolio_config` 自动重写与同步 `99_typefolio.css`，避免多书切换导致样式相互污染；并在文档中补充单文件机制限制说明。
- **模式切换与参数校验优化**：切换至直接绘制模式时，若选中仅 CSS 支持的样式（如段落底线/强调词下划线）自动重置为无；自定义粗细弹窗增加正数与范围校验（上限 20px）。
- **菜单交互与文档/翻译补全**：所有子菜单弹窗、预设管理及使用指南完成后保持菜单打开状态（`keep_menu_open`）；完善 README 功能全景表与英文说明；补齐 `Save`/`Rename`/`Delete` 等双语翻译。

### English
- **Directory & Chapter Jump Crash Fix**: Added `pcall` safety guards and box boundary validations for `crengine` line boxes and dual-page `xpointer` queries in direct drawing mode. Silently skips invalid frames during chapter transitions to prevent crashes in `ReaderView.paintTo` loop.
- **Per-Book CSS Synchronization**: Rewrites and synchronizes `99_typefolio.css` using current book's `typefolio_config` in `onReaderReady`, preventing style cross-contamination across books. Updated README with single-file CSS limitations.
- **Mode Switching & Input Validation**: Automatically resets CSS-only underline styles when switching to direct paint mode. Added positive number range validation (max 20px) for custom line thickness input dialogs.
- **Menu Interaction & i18n Completion**: Preserved menu open state (`keep_menu_open`) across popup dialogs, preset management, and help guides. Fully updated README feature matrix and filled missing bilingual translation keys for UI buttons.

# v2.1.1

# Release v2.1.1

## What's Changed / 变更说明

### 中文 (Simplified Chinese)

* **菜单交互体验优化**：所有子菜单弹窗、使用指南及预设操作完成后保持菜单打开状态（`keep_menu_open`），避免频繁重新进入菜单。
* **Calibre 正则兼容性增强**：更新「使用指南」中的标题匹配正则，完美穿透 `<span>`、`<font>`、`<b>` 等多层标签嵌套与换行，适配各种复杂源书排版。

---

### English

* **Menu Navigation & State Persistence**: Preserved menu open state (`keep_menu_open`) across all popup dialogs, help guides, and custom preset actions for smoother e-ink interactions.
* **Enhanced Calibre Regex Compatibility**: Improved heading matching regex in the in-reader guide and docs to handle multi-layer nested tags (`<span>`, `<font>`, `<b>`) and line breaks.

---

## Detailed Changes / 详细变更分类

### Changed / 优化
* `_meta.lua`: Bumped plugin version to `2.1.1`.
* `main.lua`: Added `keep_menu_open = true` across all preset callbacks, help topics, and input dialog triggers.
* `locales/` & `README.md`: Synchronized robust multi-nesting Calibre title matching regex across `zh_CN.lua`, `en.lua`, and `README.md`.

# v2.1.0

# Release v2.1.0

## What's Changed / 变更说明

### 🇨🇳 中文

* **对话高亮 (Dialogue Highlight)**：新增对话样式微调，支持背景底色（浅/中/深 3 档）、加粗、斜体独立组合，兼容 `.dialogue` 等 class。
* **自定义预设 (Custom Presets)**：支持将当前排版快照保存为自定义预设，提供套用、重命名及删除功能。
* **内置使用指南 (In-Reader User Guide)**：主菜单顶部新增「使用指南」入口，弹窗提供功能原理、Calibre 正则标记教程及手势绑定说明。
* **菜单交互与状态指示 (UI Improvements)**：子菜单首行统一显示 `功能名：已开启/已关闭` 实时状态，提升墨水屏可读性。
* **双语与文档更新 (i18n & Docs)**：补充中英文语言包 (`locales/en.lua`, `locales/zh_CN.lua`)，同步更新 README 架构与 Changelog。

---

### 🇬🇧 English

* **Dialogue Highlight**: Added dialogue text styling supporting background tint (Light/Medium/Strong), bold, and italic, compatible with `.dialogue` and related CSS classes.
* **Custom Presets**: Added ability to save current settings as named custom presets with options to apply, rename, and delete.
* **In-Reader User Guide**: Added a Help entry at the top of the main menu explaining rendering modes, Calibre regex tagging, and gesture shortcuts.
* **UI & Submenu Status Labels**: Updated first-row submenu toggles to display live state (`<Feature>: Enabled/Disabled`) for better legibility on e-ink screens.
* **i18n & Documentation**: Updated English and Simplified Chinese locale dictionaries (`en.lua`, `zh_CN.lua`) and updated README project guidelines.

---

## Detailed Changes / 详细变更分类

### Added / 新增
* `css_templates.lua`: Added `dialogue_style` CSS template with configurable tint, tint level, bold, and italic parameters.
* `main.lua`: Added `Custom presets` submenu logic allowing preset saving, loading, renaming, and deletion.
* `main.lua`: Added `Help / user guide` menu entry and `InfoMessage` modal with usage instructions.
* `locales/`: Added dictionary strings for Dialogue Highlight, Custom Presets, and User Guide in both `en.lua` and `zh_CN.lua`.

### Changed / 优化
* `main.lua`: Standardized submenu header toggles via `_tweakEnableItem` to render `<Title>: Enabled/Disabled`.
* `README.md`: Updated plugin architecture description, settings key definitions, and changelog section.
