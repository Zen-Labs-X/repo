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
