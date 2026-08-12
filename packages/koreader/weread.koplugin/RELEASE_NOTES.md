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