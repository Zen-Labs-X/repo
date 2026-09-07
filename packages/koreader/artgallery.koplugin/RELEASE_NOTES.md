# v1.0.22

## v1.0.22 (2026-08-29)

Adopted from Glimpse v1.5.1 (based on real source diff):
- Phase 47: shared decoded-bitmap LRU (_bbCacheGet/_Put/_Free, max=3)
- Phase 48: selective-corner make_corner_stencil + hold-release full-flash suppression
- Phase 49: zoom/switch light update path (_updateImageOnly, _repaintOverlayFast, FAST_SWITCH_KEY toggle)
- Phase 50: audit of bookmark cache + max-zoom config (already in v1.0.21)
- Phase 51: doc sync (README, compare.html, About dialog, CHANGELOG.html) — three-version consistency
- Phase 52: hotfix for hold-release panning regression (guard moved inside branch)

Self-check: PASS=17 FAIL=0 WARN=0. KPW3 on-device verified.
README + Compare doc now reflect v1.5.1 absorption (not just v1.3.0).
Version bumped: 1.0.21 → 1.0.22.

# v1.0.21

美术馆 / ArtGallery v1.0.21

KPW3 实机验证通过的增量，统一随本版发布（此前 v1.0.20 发行包未含阶段四十/四一）：

- 阶段四十 / 四一（hotfix）：修复点画廊「返回」致 KOReader 崩溃，以及图库仅一张书签删除后点「返回」无反应（主池空即回阅读页）。
- 阶段四二：吸收 Glimpse v1.3.0 的菜单图标缓存——弹出菜单行图标按「路径:尺寸」全会话复用，菜单打开更跟手。
- 阶段四三：吸收 Glimpse v1.3.0 的圆角渲染快填——make_rounded_stencil 内部矩形一次填，像素一致、更省。
- 阶段四四：吸收 Glimpse v1.3.0 的弹出菜单自动旋转修复——菜单开着时旋转屏幕会先关菜单、再交还查看器按新方向重排。
- 阶段四五：「关于 美术馆」对话框严格审阅——footer 标注已采纳 v1.3.0 部分内部优化，与 README / 独立对比件三版一致。

ArtGallery = Glimpse + Illustrations 合并增强（自包含，无 require 上游）。目标设备仅装本插件即可，勿与 glimpse / illustrations 并存。

安装：下载 artgallery.koplugin-v1.0.21.zip，解压得 artgallery.koplugin 文件夹，复制到 koreader/plugins/ 后重启 KOReader。

# v1.0.20

## 美术馆 / ArtGallery v1.0.20

阶段三十八「书签入画廊」经多轮 KPW3 真机复验与根因定位，书签删除 / 收藏 / 跳转 / 缓存清理全链路确认稳定，特此发版。

### 主要变更
- **书签删除修复（关键）**：经多轮真机取证定位三类根因并逐一修复——
  1. 删除后未落盘（KOReader `ReaderAnnotation:onSaveSettings` 自身不 flush）→ 显式 `saveSetting + flush` 强制落盘；
  2. 菜单回调同步弹确认框被同一点按「穿透」→ `UIManager:nextTick` 推迟到下一 UI 帧；
  3. 确认框「确定」字段名误用 `callback`（KOReader 实际调用 `ok_callback`）→ 改为 `ok_callback`。
  - 另含兜底 `table.remove` + `updatePageNumbers` 与落盘解耦 + 诊断日志清理。KPW3 实机确认删除生效（crash.log 取证 `flush ok=true left=0`）。
- **版本 1.0.19 → 1.0.20**。
- **文档同步**：CHANGELOG.md 补齐轮7/8/9 与发版说明；README.md 新增 §11 书签入画廊、下载链接更新至 v1.0.20。

### 安装
下载 `artgallery.koplugin-v1.0.20.zip`，解压得 `artgallery.koplugin/` 复制到 KOReader 插件目录 `koreader/plugins/`，重启即可。

---
## ArtGallery v1.0.20

Phase 38 "bookmarks into gallery" is now stabilized on-device (KPW3) after multiple rounds of real-device debugging; bookmark delete / favorite / jump / cache-clear all confirmed working. Released as v1.0.20.

### Highlights
- **Bookmark delete fix (critical)**: three root causes found via on-device forensics and fixed — disk flush, input-penetration (nextTick), and ConfirmBox `ok_callback` field name. On-device confirmed (`flush ok=true left=0`).
- Version 1.0.19 → 1.0.20; docs (CHANGELOG.md / README.md) synced.

---
> **2026-08-16 文档刷新（版本仍为 v1.0.20，无运行行为变化）**：README §相比上游的改进 对比段校正为 Glimpse 最新稳定版 **v1.3.0**（原写 v1.2.5），并补记与美术馆的差异（书签独立实现／未采用屏上缩放控件与全局总开关）；Illustrations 仍为 v0.5.2。插件内「关于 美术馆」文本与独立对比件同步，做到三版统一。本次重新打包 zip 以使下载包内含更新后的文档。

# v1.0.19

# 美术馆 / ArtGallery v1.0.19

在 v1.0.16（最大放大倍数可配置）基础上，按用户指定顺序 **③→①→②** 吸收母插件 glimpse v1.2.5 的可借鉴项，三项改进全部完成并通过彻底核验（语法 / 类顺序 / 代理加载 / local_ 遮蔽 / 单元测试），且经 **KPW3 实机复测确认**。

## 本次新增（v1.0.17 → v1.0.19）

### ③ 手势独立开关（v1.0.17）
插件菜单新增「手势」子菜单，可**单独开启 / 关闭**「双击放大 / 滑动翻页 / 捏合缩放」任一手势——按手感或防误触自由定制，关闭后对应手势立即失效、其余不受影响。纯配置 + wiring，零新增渲染路径。

### ① 更聪明的图片相关性过滤（v1.0.18）
扫描层智能判断图片是否值得入图库，减少装饰性留白 / 页眉页脚噪声：
- **参考图识别**：按文件名识别 map / family-tree / pedigree / diagram / chart / graph / timeline / schematic / infographic（词边界匹配，避免 remap / photo / logo 误命中），小尺寸或异形地图、族谱、图表不再被当作"太小"误杀；
- **图文书自动放宽**：全书"强参考信号"密度足够高（≥4 且占 ≥40%）时判定为图文书，对无说明小图放宽尺寸下限，但**长宽比测试保持严格**，高瘦装饰留白仍丢弃；
- 升级后首次打开自动重扫（扫描层版本号自增，旧缓存失效）。

### ② 双池带实时计数的分段切换器（v1.0.19）
图库（抽屉）底部由旧「三态循环按钮」升级为**三段式分段控件**，直达切换三个图片池并实时显示计数：
- **全部 [N]** / **收藏 [F]** / **忽略 [M]**；点按分段直接跳转（无需循环），当前池反相（黑底白字）高亮；
- 仅当确有忽略项时才显示「忽略」段——无忽略时只有 全部 / 收藏 两段，外观与旧版一致；处于「忽略」视图但已无忽略项时自动回退「全部」，避免空画廊；
- 收藏计数走缓存，频繁切换无性能压力。

## 实机（KPW3）复测确认项
- 冷启动速度快、无卡顿；
- 飞行模式下触发「检查更新」不冻结，正确提示「是否打开 WIFI」；
- 逐段点「全部 / 收藏 / 忽略」命中正确、实时计数准确；无忽略项时不显示「忽略」段；
- 菜单关闭某手势后对应手势确失效；
- 退出再进，收藏 / 过滤偏好 / 手势开关均保持。

## 安装 / 更新
- **新增安装**：下载下方 `artgallery.koplugin-v1.0.19.zip`，解压得到 `artgallery.koplugin` 文件夹，复制到 `koreader/plugins/` 后重启 KOReader。
- **已装用户**：插件菜单「检查更新」会自动从本仓库 Release 拉取并安装。

> 完整逐次改动时间线见仓库 `audit/CHANGELOG.html`（中文）；部署前验收报告见 `audit/ACCEPTANCE_v1.0.19.html`。

# v1.0.16

v1.0.16 更新（最大放大倍数可配置，吸收母插件 glimpse v1.2.2）：

- 新增「最大放大倍数」设置（插件菜单）：可在 1.5× / 2.0× / 2.5× / 3.0× / 4.0× 之间选择，对齐母插件 glimpse 的 150%–400% 区间；默认 1.5× 保持此前行为——抽屉态取该上限，全屏态自动 ×2。
- 设置即时生效（下次打开 viewer / 进入全屏即应用），无需重启 KOReader。
- 此前版本已含的关键加固（v1.0.15）：init / 网络更新检查起止 / 配置持久化处补 logger.dbg 关键路径日志；全屏 viewer 拆除与完整扫描结束两处安全点主动 collectgarbage，缓解 KPW3 低内存压力。
- 实机（KPW3）测试通过。

完整改动时间线见仓库 audit/CHANGELOG.html（阶段三十二）。
