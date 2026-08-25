# Changelog · 墨痕壁纸（InkStain）

> **当前版本：v3.5.7（官方版）** — 觅阅（MiuRead）5.1.0 免改动直接兼容

## 🙏 代码提供者

本版本（`inkstain-v3.5.7.zip`）代码由 **miumiupy98-art** 提供：

- GitHub：<https://github.com/miumiupy98-art>
- 觅阅 MiuRead 项目：<https://github.com/miumiupy98-art/miuread-koreader>

> 说明：v3.5.7 已在墨痕插件内**原生实现**觅阅所需的外部设置接口（Public API v2），
> 不再依赖本地补丁。此前本地制作的 v3.5.6 过渡适配版已被官方版本取代，可弃用。

---

## v3.5.7（2026-08-25）官方版

### ✨ Public API v2（面向外部插件完整开放）

| 接口 | 说明 |
|---|---|
| `getApiVersion()` | 返回 `api_version = 2`，供调用方做能力探测 |
| `isEnabled()` / `isActive()` / `getStatus()` | 状态查询；`getStatus()` 同时返回 `api_version` 与 `version` |
| `enable(opts)` / `disable(opts)` / `refresh(opts)` | 开启 / 关闭 / 刷新，支持 `quiet` 静默模式 |
| `getSettingsMenuItems()` | 返回 InkStain 自己维护的完整设置树，调用方无需复制任何选项 |
| `getSettingsMenu()` | 兼容别名（保留给使用旧命名方式的外部调用方） |
| `openSettings(opts)` | 由 InkStain 自己打开**原生 TouchMenu 设置界面**，支持 `on_close` 回调与防重入 |

### 🔌 MiuRead 集成

- ✅ 觅阅 5.1.0 点击「墨痕设置」直接进入墨痕原生设置界面，**不再弹出「请更新到 InkStain 3.5.7 或更高版本」提示**
- ✅ 觅阅关闭墨痕后真正解除锁屏接管并恢复原屏保
- ✅ 关闭「自动设置 KOReader 休眠屏幕」时同步解除当前墨痕锁屏
- ✅ 检查更新、文件选择、多级菜单不再由觅阅转发，全部由 InkStain 自己显示

### 🛠 OTA 与稳定性

- ✅ 恢复「软件更新」入口，接入安全的自动更新检查
- ✅ 自动检查延迟到主页、仅在联网时执行，并限制检查超时，避免启动阶段触发更新逻辑
- ✅ OTA 继续使用 stable-channel、SHA-256 校验、安装前备份与失败回滚
- ✅ 修复休眠兜底路径调用错误函数的问题

### 📦 文件变更（相对 v3.5.5）

| 文件 | 变更 |
|---|---|
| `main.lua` | 新增 Public API v2 全部接口、`_stopPeriodicRefresh`、OTA 自动检查调度（`_scheduleAutoUpdateCheck` / `_cancelAutoUpdateCheck`）、`external_quiet` 辅助函数，重写 `disableWallpaper`；版本号 → 3.5.7 |
| `_meta.lua` | 版本号 → 3.5.7 |
| `README.md` / `README_en.md` | 更新日志追加 v3.5.7 条目 |
| `README.txt` | **新增**（分发说明） |
| `scripts/build_release.py` | **新增**（发布构建脚本） |
| `scripts/verify_release.py` | **新增**（发布校验脚本） |

其余文件（`pluginota/`、`locales/`、`assets/`、`ota_config.lua` 等）相对 v3.5.5 无结构性变化。

### ⚙️ 兼容性

- 觅阅 5.1.0 零改动：其 `openSettings` 检测为**方法存在性判断**，官方 3.5.7 原生提供该接口，直接命中。
- KOReader 原生「墨痕壁纸」主菜单路径（`addToMainMenu`）保持不变。
- 本地 3.5.6 过渡适配版（为墨痕 3.5.5 手工补 `openSettings` 的版本）已被本官方版取代，**建议直接改用 v3.5.7**。

### 🔄 安装方式

1. 将 `inkstain-v3.5.7.zip` 解压，得到 `inkstain.koplugin` 文件夹
2. 替换 KOReader 插件目录中的同名文件夹
3. 重启 KOReader；墨痕与觅阅版本均无需其他调整

---

## 版本沿革（简表）

| 版本 | 说明 |
|---|---|
| v3.5.7（2026.08） | Public API v2 + 觅阅原生集成 + OTA 恢复（本文件主版本） |
| v3.5.6（2026.08） | 本地过渡适配（非官方；为 3.5.5 手工补设置入口，**已弃用**） |
| v3.5.5（2026.08） | 修复 Top 书单同书重复（按书名去重聚合）；补全 `last_time` 字段 |
| v3.5.4（2026.08） | 移除主菜单「检查更新」入口与启动自动检查（OTA 兼容性保护） |
| v3.5.3（2026.08） | 修复「检查更新」子菜单闪退；自动检查默认关闭；新增「手动下载地址」 |
| v3.0.0（2026.08） | 重构本地化为 .po 语言包系统；修复觅阅数据源多处问题 |
| v2.0.9 / v2.0.8 / v2.0.7 / v2.0.0（2026.08） | 壁纸语言切换、进度模式、字体自定义、多数据源、OTA 等 |
| v1.0.0（2026.08） | 首个稳定版本 |

完整历史条目见插件包内 `README.md`「📝 更新日志」章节。
