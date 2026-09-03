# v1.3.1

## 新功能与改进

- 整本下载的 EPUB 新增书籍简介，可在 KOReader 的书籍信息中查看。
- 优化自适应封面书架布局，修复部分屏幕上的内容溢出和滚动条问题，并用封面折角标记已下载书籍。

## What's Changed
* fix(library): refine adaptive cover shelf by @finlater in https://github.com/finlater/weread.koplugin/pull/143
* feat(epub): include book description metadata by @finlater in https://github.com/finlater/weread.koplugin/pull/144


**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.3.0...v1.3.1

# v1.3.0

## 新功能与改进

- 新增自适应封面书架（设置-书架视图-封面模式），并默认启用分页，提升大书架的加载速度。
- 重做想法弹窗，支持 Emoji、长内容滚动、物理按键操作和显示样式调整，支持长按复制想法。
- 下载设置新增脚注弹窗选项，可隐藏正文中的脚注文本。
- 移除划线末尾的星号，避免影响正文排版。
- 修复阅读进度自动同步偶尔失败、封面书架显示不稳定等问题。

感谢 @lostanother、@jqs7 和 @baily-zhang 的贡献。

## What's Changed
* perf(library): paginate bookshelf views by @lostanother in https://github.com/finlater/weread.koplugin/pull/121
* feat(library): add adaptive cover shelf by @lostanother in https://github.com/finlater/weread.koplugin/pull/128
* fix(progress-sync): retry automatic pull when the link is not ready by @baily-zhang in https://github.com/finlater/weread.koplugin/pull/130

## New Contributors
* @baily-zhang made their first contribution in https://github.com/finlater/weread.koplugin/pull/130

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.2.0...v1.3.0

# v1.2.0

## 新功能与改进

### 新功能

- 本地书支持同步微信读书的划线与想法，无需重新生成 EPUB。
- 同步划线想法支持取消和断点续传，并可一键显示或隐藏划线。

### 优化与修复

- 整本下载失败时自动重试，不再保存残缺 EPUB。
- weread 主菜单简化和重构。

感谢 @lostanother、@Mr54233 的贡献。

本地书划线与想法功能参考了 https://github.com/Mr54233/pickthought.koplugin 的实现。

## What's Changed
* fix(download): avoid incomplete full-book EPUBs by @lostanother in https://github.com/finlater/weread.koplugin/pull/118
* feat: sync local-book underlines and thoughts by @finlater in https://github.com/finlater/weread.koplugin/pull/117

## New Contributors
* @lostanother made their first contribution in https://github.com/finlater/weread.koplugin/pull/118

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.1.0...v1.2.0

# v1.1.0

## 新功能与改进

### 新功能

- 支持使用方向键、翻页键和确认键操作书架、书籍详情、章节列表、书评与阅读统计，方便无触屏或主要依赖物理按键的设备使用。
- 新增可绑定到手势或按键的“微信读书·书架”“微信读书·本地书架”“微信读书·阅读统计”和“微信读书·搜索”动作；阅读界面继续提供快捷菜单。

### 优化与问题修复

- 优化大书和图片较多书籍的下载方式，显著降低内存占用，并在完成、失败或取消后自动清理临时文件。
- 脚注改为按 KOReader 默认方式显示在页面底部，解决脚注看不到或点击后跳错位置的问题。
- 改进划线与想法显示：长标题可以换行，想法标记不再被划线遮住。
- 修复空书架、空书评以及快速切换书籍时可能导致的闪退。
- 修复从微信读书书架打开图书后，书架残留并阻挡 KOReader 退出的问题。

> **升级提示：** 脚注显示方式会写入下载的书籍，已经下载的旧书需要重新下载才能使用新的脚注效果。

感谢 @SuzyZhang-Dev、@MsReverie、@jsfaint、@jqs7 和 @ViggoC 的贡献。

# v1.0.0

## 新功能与改进

### 新功能

- 全面重构书架、书籍详情和章节列表界面，优化书籍与公众号的浏览、缓存状态和操作入口。
- 支持 SimpleUI 和 ZenUI 快速启动，并增加专用图标与稳定的第三方调用入口。
- 支持将已下载书籍添加到 KOReader 本地书架，无网络时也可快速访问。
- 支持插件内手动或每日自动检查更新，查看更新日志、下载进度并在线安装。
- 更新下载默认优先使用 GitHub 代理，失败后自动回退直连。

### 优化与问题修复

- 增加章节目录的文件缓存与 SQLite 双重存储、自动回填和联网修复，解决目录缺失后阅读进度同步、阅读时长上报及章节识别失败的问题。
- 整理“关于”与更新选项的菜单层级，并优化菜单交互；关闭弹框或临时页面后保留原来的菜单位置。
- 恢复书架页的文字操作栏，改进小屏设备上的标题和操作区布局。
- 加强在线升级安全性：校验 SHA-256，限制更新包最大为 10 MiB，下载过程超限时立即终止，并在新版本成功启动后自动清理上一版备份。

感谢 @MsReverie 的贡献。

## What's Changed
* feat: refactor bookshelf and book details UI by @finlater in https://github.com/finlater/weread.koplugin/pull/86
* feat: refactor the bookshelf view to support custom options and callbacks by @finlater in https://github.com/finlater/weread.koplugin/pull/92
* feat: add local weread collection as offline bookshelf by @MsReverie in https://github.com/finlater/weread.koplugin/pull/83
* feat: support OTA updates by @finlater in https://github.com/finlater/weread.koplugin/pull/85


**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v0.6.0...v1.0.0
