# v0.5.2

## 新功能与改进

- 优化升级说明页面：标题直接显示“旧版本 → 新版本”，正文只展示新版本更新内容，避免版本归属混淆。

**Full Changelog**: https://github.com/finlater/one.koplugin/compare/v0.5.1...v0.5.2

# v0.5.1

## 新功能与改进

- 优化菜单层级，将“关于（版本号）”移入“设置”菜单。

**Full Changelog**: https://github.com/finlater/one.koplugin/compare/v0.5.0...v0.5.1

# v0.5.0

## 新功能与改进

- 支持在插件内手动检查更新、查看更新说明并在线安装。
- 支持每天自动检查一次更新，发现新版本后在更新管理菜单中提示。
- 更新默认优先使用 GitHub 代理；代理不可用时自动回退 GitHub 直连。
- 安装前校验发布包 SHA-256、文件路径、插件结构和版本号。
- 更新时保留上一版插件目录，安装激活失败时自动回滚。
- 增加自动发布流程：修改 `_meta.lua` 版本号并推送到主分支后，自动测试、打包并创建 GitHub Release。

## What's Changed
* feat: add OTA updates by @finlater in https://github.com/finlater/one.koplugin/pull/2

## New Contributors
* @finlater made their first contribution in https://github.com/finlater/one.koplugin/pull/2

**Full Changelog**: https://github.com/finlater/one.koplugin/compare/0.4.3...v0.5.0

# 0.4.3

- 支持 SimpleUI 和 Zen_UI 集成快捷方式

**Full Changelog**: https://github.com/finlater/one.koplugin/compare/0.4.2...0.4.3

# 0.4.2

- 已缓存列表中支持长按清理单期缓存

**Full Changelog**: https://github.com/finlater/one.koplugin/compare/0.4.1...0.4.2
