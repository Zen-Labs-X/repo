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
