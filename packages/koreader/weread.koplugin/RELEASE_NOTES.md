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