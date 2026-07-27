## 新功能与改进
- 划线想法优化
  - 展示界面使用原生UI显示
  - 大幅提升首次加载和显示速度，降低内存占用
  - 增加划线防误触
- 支持阅读进度同步
- 优化阅读时间上报逻辑，避免阻塞UI

⚠️注意：本地划线和想法机制升级，须重新下载想法和划线，且想法显示界面改为 koreader 原生 UI 渲染，不再支持 emoji 显示。

感谢 @shichen35 @MsReverie  @jqs7 的贡献🎉🎉🎉

## What's Changed
* fix(read_report): run reading-time report in a forked subprocess to unblock the UI loop by @shichen35 in https://github.com/finlater/weread.koplugin/pull/67
* feat: add SQLite-based thought storage with JSON fallback by @jqs7 in https://github.com/finlater/weread.koplugin/pull/66
* feat: ignore edge taps on thought underlines to reduce page-turn misfires by @MsReverie in https://github.com/finlater/weread.koplugin/pull/63

## New Contributors
* @MsReverie made their first contribution in https://github.com/finlater/weread.koplugin/pull/63

**Full Changelog**: https://github.com/finlater/weread.koplugin/compare/v0.4.0...v0.5.0