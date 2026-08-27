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