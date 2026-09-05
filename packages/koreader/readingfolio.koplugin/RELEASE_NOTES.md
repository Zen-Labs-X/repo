# v1.8.0

# Release v1.8.0 - 字号动态比例联动缩放 & KOBO 原生风格全屏自适应优化

### 🚀 新特性与排版优化 (What's New)

#### 1. ✨ 字号随卡片比例平滑联动缩放 (Dynamic Font Ratio Scaling)
- **解决痛点**：彻底解决此前卡片在切换至「全屏」或自定义比例时，文字保持固定点数导致的画面视觉留白过多、全屏海报张力不足的问题。
- **平滑阻尼算法**：引入基于风格基准比例的平滑阻尼缩放算法（$\text{font\_scale} = \sqrt{\text{ratio} / \text{base\_ratio}}$）：
  - **全屏比例（1.00）下**：字号自适应放大约 **28% ~ 30%**（例如大标题由 24pt 增至 31~32pt），画面饱满大气，同时保证文字与封面在墨水屏物理高度下绝不溢出截断；
  - **调小卡片（如 0.35~0.50）下**：字号适度收缩紧凑，并保留安全下限保护，小字依然清晰可读；
  - **默认比例下**：保持 $1.00\times$，排版与原版完全一致。
- **双重微调兼容**：缩放机制与菜单中现有的「大/中/小号文字微调」（-20 至 +20）完美叠加生效。

#### 2. 🎨 KOBO 原生极简风格排版与全屏增强 (`kobo`)
- **全屏与默认比例自适应**：全屏模式下自动切换为无边框沉浸式全出血海报，非全屏模式下优雅保留圆角、边框与卡片投影。
- **封面自适应扩展**：封面组件支持等比放大（`allow_upscale`），针对不同尺寸与 DPI 屏幕重构顶部状态、居中大封面与底部进度的弹性留白比例，彻底消除紧凑屏下的挤压感。

---

### 🛡️ 代码健康与质量保证 (Quality & Invariants)
- **规范全覆盖**：全部 42 个 Lua 源码通过标准静态检查，无 `bit` 库等非标准环境依赖，完美向前兼容。
- **DPI 与字体纯净性**：所有样式 `Font:getFace` 调用严格保持纯点数规范，杜绝高分屏二次缩放失真。
- **多语言 1:1 对齐**：中英文字典 279 项键位严格镜像对齐。

---

### 📦 安装与升级方式 (Installation)

1. 下载下方附件中的 `readingfolio.koplugin.zip`。
2. 解压并将 `readingfolio.koplugin` 文件夹整体放入设备的 `koreader/plugins/` 目录（覆盖旧文件）。
3. 重启 KOReader 即可体验全新动态比例排版。

# v1.7.0

## 阅笺 (Reading Folio) v1.7.0

本版本带来了全新的 **KOBO 原生极简休眠海报风格**，并重构了屏幕物理尺寸/DPI 自适应检测与字体缩放机制，彻底解决了高分屏（如 300 DPI 7/8寸设备）下的字体膨胀与比例失真问题。

---

### 🌟 新增功能与亮点 / Highlights

1. **全新「KOBO」原生极简风格**：
   - 纯白原厂海报休眠质感，居中通透大尺寸图书封面，无边框全屏排版。
   - 顶部居中展示休眠/阅读状态与电量/充电状态（支持每分钟局部刷新）。
   - 底部居中展示阅读进度百分比与剩余时间（如「已阅读 4% · 还需 6 小时」），无估算时优雅降级为页码或章节。
2. **修复 300 DPI 高分屏及大屏设备字体重复缩放 Bug**：
   - 解决 KOReader 底层 `Font:getFace` 内部缩放与插件层 `layout.scaled` 重复缩放叠加导致的 4.5 倍字体膨胀问题（阅读票笺等风格在 300 DPI 设备上不再被撑爆失真）。
3. **多尺寸设备自适应与物理 DPI 动态检测**：
   - 动态识别屏幕物理 DPI 与对角线尺寸（英寸），精准计算逻辑分辨率。
   - 重构 `compact` 紧凑模式为依据物理尺寸与逻辑分辨率动态判定。
   - 智能自适应不同屏幕对角线（6寸、7~8寸、10+寸）的默认卡片比例。
4. **优化「典藏画廊」侧栏排版**：
   - 调优左右两侧数据列字号与侧栏宽度比例，彻底防止 `1:09` / `10%` / `40/419` 在窄栏下异常换行。

---

### 📦 安装方法 / Installation

1. 下载下方附件中的 `readingfolio.koplugin.zip`。
2. 解压并将 `readingfolio.koplugin` 文件夹复制到电子书设备的 `koreader/plugins/` 目录下。
3. 重启 KOReader，在阅读界面顶部菜单栏 **“工具 (Tools)”** 中即可找到 **“阅笺”**。

---

### 🛠️ 完整更新日志 / Changelog

- **feat**: add new `KOBO` native minimalist sleep style (`kobo`).
- **fix**: eliminate font double-scaling bug on 300 DPI high-density screens by passing raw unscaled points to `Font:getFace`.
- **feat**: add dynamic DPI, physical diagonal (inches), and logical resolution detection.
- **refactor**: overhaul `compact` mode and adaptive default card ratios based on physical device diagonal.
- **style**: refine metric font sizes and column widths in `gallery` style to prevent line wrapping.
- **i18n**: sync 279 strings across `zh_CN` and `en` with 100% parity.
- **test**: add `test_font_face_unscaled` invariant check to release verification toolchain.

# v1.6.1

# Release v1.6.1

## What's Changed / 变更说明

### 中文 (Simplified Chinese)
- **时钟局刷重构**：修复定时器叠加泄漏问题；引入 FrameContainer 底色区域重绘，杜绝字迹残留；针对多状态行风格（瑞士网格、梅兰竹菊）提供整行状态重建，避免电量与状态文字被覆盖。
- **电量显示开关**：修复梅、兰、竹、菊四款风格在电量开关关闭时依然显示电量的问题。
- **国际化补全**：补齐预设应用成功的双语提示文案，清理语言包冗余键。
- **回归测试套件**：新增 `style_render_spec.lua` 与 `clock_refresh_spec.lua` 自动化回归测试。

### English
- **Minute Clock Refresh**：Fixed timer stacking on repeated suspends; introduced proper region repaint with background fill; added formatter rebuilds for compound status rows so battery readings and page counts survive refreshes.
- **Battery Toggle**：Fixed battery level display in Plum, Orchid, Bamboo, and Chrysanthemum styles to respect the show-battery toggle.
- **i18n Completion**：Added missing translations for applied preset notifications and cleaned up duplicate keys.
- **Regression Specs**：Added `style_render_spec.lua` and `clock_refresh_spec.lua`.

# v1.3.0

# Release v1.3.0

## What's Changed / 变更说明

### 中文 (Simplified Chinese)
- **随机风格模式 (Random Style)**：在显示风格菜单最后添加「随机风格」选项，开启后每次预览或生成休眠屏保时从内置 15 种排版风格中随机挑选呈现。
- **语言设置独立解耦 (i18n Decoupling)**：菜单中的「语言」选项调整为仅控制阅读卡片/海报显示的语言（如英文或中文），插件自身的菜单语言恒定保持与 KOReader 系统语言一致。
- **透明屏保背景修复 (Transparent Background Fix)**：修复屏保托管中调用 `Screen:clear()` 清屏导致透明背景失效变白的问题，确保透明背景下底层阅读页面完美透出。
- **即时预览与保持菜单开启 (Live Preview & Keep Menu Open)**：所有样式选择、背景模式、字号微调及卡片外观调整在菜单中更改时均自动刷新全屏预览，并保持菜单开启状态。
- **输入参数弹窗校验与反馈 (Input Validation)**：为字号偏移（`-20` 至 `+20`）、封面缩放（`0.00` – `1.00`）、卡片比例等自定义输入增加边界校验与 `Notification` 错误提示，防止非法数值。
- **规范与标准对齐 (Spec Alignment)**：`_meta.lua` 补全 `name` 和 `version` 标注，建立项目开发与审查规范（`DEVELOPMENT_SPEC.md`）及 AI Agent 规范。

### English
- **Random Style Mode**: Added a "Random style" option to the style menu to automatically pick from the 15 built-in layout styles for each preview or sleep screen generation.
- **i18n Language Decoupling**: Updated the "Language" setting to only control the rendered card/poster display language, while the plugin menu strictly matches the KOReader system language.
- **Transparent Screensaver Fix**: Fixed an issue where `Screen:clear()` turned transparent screensaver backgrounds white, ensuring the active reading book page shows seamlessly underneath.
- **Live Preview & Keep Menu Open**: Improved live preview across all settings adjustments while maintaining an open menu state (`keep_menu_open`).
- **Input Validation & Feedback**: Added bounds checking and `Notification` error messages for custom inputs (font size deltas `-20` to `+20`, cover scale `0.00`–`1.00`, and card ratios).
- **Metadata & Development Spec Alignment**: Completed `_meta.lua` tags and standardized development review specs (`DEVELOPMENT_SPEC.md`).

# v1.2.0

删除手势中多余项目
