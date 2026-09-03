# v0.1.1

# Changelog

## v0.1.1 - 2026-05-07

Source: https://github.com/iceyear/readeck.koplugin  
License: MIT

### English

This release is a maintenance and refactoring release focused on reliability, clearer sync behavior, Readeck 0.22.2 compatibility, and a more maintainable plugin structure.

#### Added

- Added plugin-provided i18n fallbacks with English and Simplified Chinese, while still reusing KOReader gettext strings when available.
- Added configurable log levels: `Info`, `Debug`, `Warnings`, and `Errors`.
- Added Readeck server feature detection through `/api/info`, with an automatic mode plus manual modern/legacy compatibility modes.
- Added bidirectional highlight sync for Readeck annotations and KOReader highlights, including note and color support for modern Readeck servers.
- Added highlight conflict strategies: merge changes, let Readeck overwrite KOReader, or let KOReader overwrite Readeck.
- Added a remote-deleted highlight policy so users can preserve local highlights or respect Readeck-side deletions.
- Added reading progress sync below 100% between KOReader and Readeck.
- Added file timestamp sync from Readeck metadata and estimated reading time as a KOReader keyword.
- Added periodic sync beta support.
- Added a dismissible, movable sync progress popup that can be reopened from the Readeck menu while sync is still running.
- Added KOReader runtime smoke tests and mock Readeck API network smoke tests for OAuth, article download, and highlight sync.

#### Changed

- Refactored the previous single-file implementation into smaller Lua modules; `main.lua` is now a compact plugin assembly entry point.
- Reorganized settings into clearer groups: server, authentication, client, article selection, article actions, highlights, periodic sync, and ratings/review tags.
- Reworked authentication around API token and OAuth device flow; username/password login is no longer exposed because current Readeck versions no longer support it.
- Improved sync status wording so archive/delete actions are reported accurately and less alarmingly.
- Improved article sync progress wording to show checked, downloaded, skipped, failed, and planned/completed local or remote actions.
- Made subprocess downloads experimental and explicit opt-in; failed or timed-out subprocess downloads now fall back to the stable blocking downloader.
- Reduced UI stalls by rendering status messages before slow work and by using async/cooperative paths only when KOReader runtime support is available.
- Updated development workflow with Stylua, Luacheck, Busted, KOReader runtime probes, and GitHub Actions CI.
- Documented the project as MIT-licensed open source at https://github.com/iceyear/readeck.koplugin and exposed this in the KOReader plugin About dialog.

#### Fixed

- Fixed misleading “Deleted” sync status text when articles were archived instead of deleted.
- Fixed repeated full-list redownload behavior by skipping already-downloaded articles by embedded Readeck ID.
- Fixed finished/read local actions being skipped incorrectly during sync in common archive workflows.
- Fixed Readeck 0.22.2 highlight payload compatibility for notes and transparent/none colors.
- Fixed progress popup behavior so dismissing it does not stop background sync progress tracking.
- Fixed saved experimental subprocess-download settings from old test builds being migrated back to stable defaults unless users explicitly opt in again.

#### Upgrade Notes

- Readeck username/password login is not supported. Use OAuth device flow or an API token.
- If upgrading from an early experimental build and sync/authentication behaves strangely, clear the old `readeck.lua` plugin settings and configure the plugin again.
- Experimental subprocess downloads are off by default. Keep them disabled unless you are testing that backend on your device/server.

### 中文

这是一个偏维护和重构的版本，重点是提高同步可靠性、理清同步行为、兼容 Readeck 0.22.2，并把插件结构整理到更容易长期维护的状态。

#### 新增

- 新增插件自带 i18n 回退，提供英文和简体中文，同时仍会优先复用 KOReader 已有 gettext 文本。
- 新增日志等级设置：`Info`、`Debug`、`Warnings`、`Errors`。
- 新增通过 `/api/info` 自动探测 Readeck 服务端能力，并支持手动固定新版/旧版兼容模式。
- 新增 Readeck annotations 与 KOReader highlights 的双向高亮同步，并支持新版 Readeck 的笔记和颜色字段。
- 新增高亮冲突策略：合并变更、Readeck 覆盖 KOReader、KOReader 覆盖 Readeck。
- 新增远端已删除高亮的处理策略：可保留本地高亮，也可尊重 Readeck 远端删除。
- 新增低于 100% 的阅读进度在 KOReader 与 Readeck 之间同步。
- 新增下载文件按 Readeck 元数据设置时间戳，并将预计阅读时间写入 KOReader 关键词。
- 新增周期同步 Beta。
- 新增可关闭、可移动的同步进度框；同步仍在进行时，可从 Readeck 菜单重新显示。
- 新增 KOReader runtime smoke 测试和 mock Readeck API 网络 smoke 测试，覆盖 OAuth、文章下载和高亮同步。

#### 变更

- 将原本单文件为主的实现重构为多个较小的 Lua 模块；`main.lua` 现在只负责插件装配。
- 重新整理设置菜单分组：服务器、认证、客户端、文章选择、文章动作、高亮、周期同步、评分/评论标签。
- 认证流程改为围绕 API token 和 OAuth 设备授权；当前 Readeck 已不支持用户名/密码登录，因此插件不再暴露该方式。
- 改进同步状态文案，归档和删除会分别显示，避免“明明归档却显示删除”的惊吓感。
- 改进文章同步进度文案，会显示已检查、已下载、已跳过、失败，以及本地/远端即将或已经执行的动作。
- 子进程下载改为实验性显式开启；如果失败或超时，会回退到稳定的阻塞下载路径。
- 减少 UI 卡顿：慢操作前先渲染状态提示，并且只在 KOReader runtime 支持时使用异步/协作式路径。
- 更新开发流程，加入 Stylua、Luacheck、Busted、KOReader runtime probe 和 GitHub Actions CI。
- 明确项目以 MIT 协议开源，源码仓库为 https://github.com/iceyear/readeck.koplugin，并在 KOReader 插件“关于”弹窗中显示。

#### 修复

- 修复设置为归档时，状态消息仍显示 “Deleted” 的误导性问题。
- 修复同步时可能重复处理整批已下载文章的问题，现在会通过文件名内嵌的 Readeck ID 跳过已存在文章。
- 修复常见归档流程中，同步时本地已完成/已读动作可能被错误跳过的问题。
- 修复 Readeck 0.22.2 高亮 payload 对笔记和透明/none 颜色字段的兼容性。
- 修复进度框被关闭后影响后台同步进度追踪的问题。
- 修复早期测试版本保存过的实验性子进程下载设置：升级后会回到稳定默认值，除非用户再次显式开启。

#### 升级提示

- 不再支持 Readeck 用户名/密码登录，请使用 OAuth 设备授权或 API token。
- 如果从很早期实验版本升级后，同步或认证表现异常，请清除旧的 `readeck.lua` 插件配置并重新配置。
- 实验性子进程下载默认关闭。除非你正在专门测试该后端在自己设备/服务器上的表现，否则建议保持关闭。

# v0.1.0

## Changelog

### ⚠️ Upgrade Notice: Incompatible Configuration

`0.1.0` is a major refactor. The plugin settings schema is not fully compatible with early experimental builds.

After upgrading, if you see authentication failures, broken sync behavior, inconsistent menu state, or OAuth refresh issues, please clear the old plugin settings and configure Readeck again:

* Delete the old `readeck.lua` plugin settings file from KOReader’s settings directory; or
* Use **Readeck > Settings > Restore default settings**;
* Then reconfigure the server URL, OAuth / API token, download folder, and sync options.

Username / password login is no longer supported. Please use **OAuth Device Flow** or an **API Token**.

### Major Refactor

* Split the previous large `main.lua` implementation into smaller modules organized by responsibility: `auth`, `net`, `sync`, `annotations`, `storage`, `ui`, and `core`.
* Added centralized defaults, state loading, settings storage, API path helpers, logging, and status message handling.
* Added English / Simplified Chinese i18n fallback support, with optional language override inside the plugin.
* Updated plugin version to `0.1.0`.

### New Features

* **Reading Progress Sync (Beta)**

  * Sync KOReader local reading progress below 100% back to Readeck.
  * Apply newer incomplete Readeck progress back to KOReader sidecars.
  * Keep 100% progress handled by completion actions instead of regular progress sync.

* **Bidirectional Highlight Sync**

  * Import Readeck annotations into KOReader highlights.
  * Export KOReader highlights, notes, and mapped colors back to Readeck.
  * Store returned Readeck annotation IDs to reduce duplicate uploads.
  * Detect overlapping highlights to avoid duplicate annotations.
  * Adapt annotation payloads to server capabilities, including newer annotation notes and transparent color support.
  * Added highlight conflict policies:

    * **Preserve local highlights**: remote-deleted highlights may be restored from KOReader;
    * **Respect remote deletions**: remote-deleted highlights remain local-only and are not re-uploaded.

* **Completion Action Improvements**

  * Process finished / 100%-read local articles during sync.
  * Archive or delete Readeck entries according to user settings.
  * Remove KOReader local files only after the Readeck action succeeds.
  * Sync highlights before completion actions to reduce data loss risk.
  * Prevent articles already archived / deleted during the same sync from being downloaded again.

* **Sync and Download Improvements**

  * Detect existing local files by Readeck article ID to avoid duplicate downloads.
  * Apply Readeck metadata to local file timestamps.
  * Add estimated reading time as a KOReader keyword.
  * Add configurable download concurrency with experimental async downloads; failures fall back to blocking downloads.
  * Add an option to remove local files missing from Readeck.
  * Keep offline “Add to Readeck” queue behavior and retry queued links on the next sync.

* **OAuth and Authentication Improvements**

  * Reworked OAuth Device Flow handling.
  * Added OAuth client registration, device code polling, token refresh, and cached token management.
  * Added actions to open the authorization link or show a QR code.
  * Added reset access token and clear cached tokens actions.
  * Detect server capabilities through `/api/info`; servers without OAuth support now prompt users to use an API token instead.

* **Settings and Menu Improvements**

  * Added “Configure Readeck client” for sync limit and download concurrency.
  * Added Periodic Sync (Beta) settings.
  * Added a dedicated Highlights settings group.
  * Added language selection.
  * Added Restore Default Settings to clear server, authentication, queue, and sync options.
  * Sync progress and result messages now include download, skipped, failed, highlight, reading progress, archive, and delete counts.

### Development and Testing

* Added `Makefile`, LuaRocks development rockspec, Stylua, Luacheck, and Busted tests.
* Added KOReader stub smoke tests, runtime smoke tests, and network smoke tests.
* Added a mock Readeck server covering API token auth, OAuth, bookmark listing, EPUB download, and highlight sync.
* Added GitHub Actions CI with manual `workflow_dispatch` support.

---

## 更新日志

### ⚠️ 升级前必读：配置不兼容

本次 `0.1.0` 是一次大规模重构，插件配置结构与早期实验版本不完全兼容。

升级后如遇到认证失败、同步异常、菜单状态不一致、OAuth 无法刷新等问题，请先清除旧配置再重新配置插件：

* 删除 KOReader 设置目录中的旧 `readeck.lua` 插件配置；或
* 进入 **Readeck > 设置 > 恢复默认设置** 清空插件配置；
* 然后重新配置服务器地址、OAuth / API Token、下载目录和同步选项。

另外，用户名 / 密码登录已不再支持，请改用 **OAuth 设备授权** 或 **API Token**。

### 重大重构

* 将原本集中在 `main.lua` 中的大型实现拆分为模块化架构，按职责拆分为 `auth`、`net`、`sync`、`annotations`、`storage`、`ui`、`core` 等模块。
* 新增统一的默认配置、状态加载、设置存储、API 路径封装、日志和状态消息处理。
* 新增中英文 i18n 回退机制，可跟随 KOReader 语言，也可在插件内强制选择 English / 简体中文。
* 插件版本更新为 `0.1.0`。

### 新增功能

* **阅读进度同步（Beta）**

  * 支持将 KOReader 中低于 100% 的本地阅读进度同步回 Readeck。
  * 支持把 Readeck 中更新的未完成阅读进度写回 KOReader sidecar。
  * 100% 阅读进度仍交由完成动作处理，避免误触发普通进度同步。

* **高亮双向同步**

  * 支持将 Readeck annotations 导入为 KOReader 高亮。
  * 支持将 KOReader 本地高亮、笔记和颜色映射后导出到 Readeck。
  * 支持保存 Readeck annotation ID，减少重复上传。
  * 支持重叠检测，避免重复创建相同高亮。
  * 支持根据 Readeck 服务端能力调整 payload，例如新版 annotation notes / transparent color 字段。
  * 新增高亮冲突策略：

    * **保留本地高亮**：远端删除的高亮可能会被 KOReader 重新上传；
    * **尊重远端删除**：远端已删除的高亮保留在 KOReader 本地，但不会再次上传。

* **完成动作改进**

  * 支持在同步过程中自动处理已完成 / 已读 100% 的本地文章。
  * 支持归档或删除 Readeck 文章。
  * 仅在 Readeck 端动作成功后才删除 KOReader 本地文件。
  * 处理完成动作前会先尝试同步高亮，降低数据丢失风险。
  * 已在本轮同步中被归档 / 删除的文章不会再次进入下载列表。

* **同步与下载改进**

  * 支持按 Readeck 文章 ID 检测已存在的本地文件，减少重复下载。
  * 支持同步 Readeck 元数据到本地文件时间戳。
  * 支持把预计阅读时间写入 KOReader 关键词。
  * 新增可配置的下载并发数，支持实验性异步下载；失败时会回退到阻塞下载。
  * 支持删除 Readeck 中已不存在的本地文件，可通过设置开关控制。
  * 离线添加文章时继续写入队列，并在下次同步时重试。

* **OAuth 与认证改进**

  * 重写 OAuth 设备授权流程。
  * 支持 OAuth client 注册、device code、轮询、刷新 token。
  * 支持打开授权链接和显示 QR Code。
  * 新增访问令牌重置与清除所有缓存 token 的入口。
  * 根据 `/api/info` 检测服务器能力；不支持 OAuth 的服务端会提示改用 API Token。

* **设置与菜单改进**

  * 新增“配置 Readeck 客户端”，可设置每次同步文章数和并发下载数。
  * 新增周期同步（Beta）设置。
  * 新增高亮同步设置组。
  * 新增语言选择。
  * 新增恢复默认设置入口，可清除服务器、认证、队列和同步选项。
  * 同步进度和处理结果现在会显示下载、跳过、失败、高亮、阅读进度、归档 / 删除等统计。

### 开发与测试

* 新增 `Makefile`、LuaRocks 开发依赖 rockspec、Stylua、Luacheck 和 Busted 测试。
* 新增 KOReader stub smoke test、runtime smoke test 和 network smoke test。
* 新增 mock Readeck server，用于测试 API Token、OAuth、文章列表、EPUB 下载和高亮同步。
* 新增 GitHub Actions CI，并支持手动触发 `workflow_dispatch`。

---
