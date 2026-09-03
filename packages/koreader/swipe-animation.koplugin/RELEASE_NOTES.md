# v4.2

## What's Changed
* feat: Fix first-refresh stutter on Kobo MTK devices by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/20
* feat: Provide ultra-fast UI refresh mode when delay is set to 0 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/21
* docs: replace generic issue templates with plugin-specific forms by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/22
## 更新内容
* feat: 修复 Kobo MTK 设备首刷卡顿问题 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/20
* feat: 提供延迟设置为0时UI疾速刷新模式 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/21
* docs: 提供专用 issue 模板以提升反馈效率  by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/22

**Full Changelog**: https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/compare/v4.1...v4.2

# v4.1

## What's Changed
* feat: pt-BR translation by @caiojares in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/15
* feat: add post-resume display warm-up for MTK Kobo devices by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/16
* add: restore-files for users upgrading from pre-v4.0 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/17
## 更新内容
* feat: 支持葡萄牙语（pt-BR），by @caiojares in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/15  
* feat: 为 MTK Kobo 设备休眠后预热，解决休眠后第一次翻页动画卡顿问题 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/16
* add: 添加 restore-files，供从 v4.0 之前版本升级的用户使用 by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/17
## New Contributors
* @caiojares made their first contribution in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/15

**Full Changelog**: https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/compare/v4.0...v4.1

# v4.0

## 升级注意

从旧版覆盖升级的设备，在升级完成后以后，最好手动删除 `koreader/patches/` 下的旧补丁文件：
- `1-mtk-swipe-direction.lua`
- `2-mtk-swipe-direction.lua`
- `2-swipe-full-refresh-judgment.lua`

> （旧文件已替换成墓碑，无害但建议删除。）

另外，v4.0 起插件不再依赖或修改 `ffi/framebuffer.lua`。release 中附带的 `ffi/` 目录是 KOReader 原版源文件，用于从旧版升级、之前被旧版覆盖过的用户还原系统文件（直接覆盖即可）。

## 更新说明
* refactor: 重构动画核心、接入 gettext、修复稳定性（减少系统文件覆盖 + 单一 core 补丁） by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/13

## Upgrade Notes

For devices upgrading by overwriting from an older version, after the upgrade it's best to manually delete the old patch files under `koreader/patches/`:

- `1-mtk-swipe-direction.lua`
- `2-mtk-swipe-direction.lua`
- `2-swipe-full-refresh-judgment.lua`

> (The old files have been replaced with tombstones. They're harmless, but deletion is recommended.)

Since v4.0, the plugin no longer depends on or modifies `ffi/framebuffer.lua`. The `ffi/` directory included in the release contains KOReader's original source files — it's only there so users upgrading from older versions can restore the system file that was previously overwritten (just copy it over). 
## Changelog
* refactor: reworked the animation core, integrated gettext, and fixed stability (reduce overwrites of system files + a single core patch) by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/13

**Full Changelog**: https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/compare/v3.7...v4.0%E7%A8%B3%E5%AE%9A%E7%89%88

# v3.7

## What's Changed
* Merge device.lua functionality into settings and sync with latest KOReader by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/6
* fix: restore stock full-refresh on chapter boundaries and image pages by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/7
* feat: skip animation on clearing pages + mild global refresh option by @MsReverie in https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/pull/8


**Full Changelog**: https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/compare/v3.6...v3.7

## 更新内容

* 将 device.lua 功能合并进设置，并同步最新 KOReader（#6）
* 修复：恢复章节边界与图片页的原版全刷逻辑（#7）
* 新增：刷新页跳过动画 + 轻度全局刷新选项（#8）
* 完整更新日志：https://github.com/koplugin-swipe-animation/Swipe_Animation.koplugin/compare/v3.6...v3.7

# v3.6

## 新增功能
- 新增：KINDLE 2022 及以上机型的完全支持
## New Features
- Added full support for Kindle 2022 and newer models.
