# v1.4.2

## 新功能与改进

- 优化划线和想法的拉取速度与进度显示，减少网络请求。
- 提升显示划线和想法时的翻页流畅度。
- 修复清理想法不彻底，以及重新打开书籍后重复匹配的问题。

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.4.1...v1.4.2

# v1.4.1

## 新功能与改进

- 修复划线和想法的显示状态及章节匹配问题，兼容本地书与微信读书章节编号不一致的情况。
- 降低后台预下载和匹配的内存要求，并修复清理书籍缓存后旧划线想法自动恢复的问题。

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.4.0...v1.4.1

# v1.4.0

## 新功能与改进

- 统一本地书与微信下载书的划线和想法管理，支持按章匹配、中断续传和同书数据复用。
- 下一章正文及划线想法改为后台预下载，减少阅读时的等待和卡顿。
- 优化公众号图片下载，降低内存占用。
- 修复部分书籍正文不显示、脚注识别异常的问题。

感谢 @baily-zhang、@szey 和 @q107580018 的贡献。

## What's Changed
* fix(footnotes): stop ancestor blocks from poisoning note definitions by @baily-zhang in https://github.com/finlater/weread.koplugin/pull/133
* fix(content): sanitize hostile font-size:0 in server book css by @baily-zhang in https://github.com/finlater/weread.koplugin/pull/137
* refactor(annotations): unify matching and resumable sync by @finlater in https://github.com/finlater/weread.koplugin/pull/150
* fix(mp): stream public-account article images to disk by @szey in https://github.com/finlater/weread.koplugin/pull/132

## New Contributors
* @szey made their first contribution in https://github.com/finlater/weread.koplugin/pull/132

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v1.3.1...v1.4.0

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
