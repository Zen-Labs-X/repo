<p align="center">
  <img src="assets/koocomic-social-preview.jpg" alt="KooComic / koo漫画 — KOReader 漫画书架" width="100%">
</p>

# koo漫画（KooComic）

[![CI](https://github.com/jackchensky/KooComic/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jackchensky/KooComic/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/jackchensky/KooComic?label=release)](https://github.com/jackchensky/KooComic/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/jackchensky/KooComic?style=flat&label=stars)](https://github.com/jackchensky/KooComic/stargazers)
[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue.svg)](LICENSE)

一个连接用户个人 KOOBONE 漫画书库的非官方 KOReader 插件，让你可以在 Kindle/KOReader 上浏览封面书架、下载 EPUB 并直接阅读。

> ⭐ 如果 koo漫画对你有帮助，欢迎为项目点亮一个 **Star**。你的支持能帮助更多 KOReader 用户发现它，也能让我们知道这个插件值得继续维护。想及时收到新版通知，可以选择 GitHub 的 **Watch → Custom → Releases**，或在插件内使用版本检查。

## 功能亮点

- 墨水屏友好的封面书架，自适应横竖屏并可调整行列数和文字大小。
- 搜索、排序和下载/阅读状态筛选，支持书籍详情与分页浏览。
- 流式下载 EPUB，显示百分比、大小、速度和预计剩余时间。
- 自动恢复登录状态；“记住密码”默认关闭，可随时清除密码或退出账号。
- 封面本地缓存、下载记录，以及旧版 KOReader 的列表界面回退。
- 通过 GitHub Release 在线更新，安装前校验文件大小和 SHA-256，失败时尝试回滚。
- 每天最多提醒一次新版本；连续三次选择“稍后更新”后停止自动弹窗，仍可手动检查。

当前公开版本为 **v0.4.0**。插件已在 Kindle/KOReader 真机上持续迭代，但设备型号、KOReader 版本和 KOOBONE 网页接口都可能影响兼容性，欢迎提交脱敏后的测试反馈。

## 安装

### 通过 Storefront

1. 打开 KOReader 的 Storefront，使用默认的 **Storefront** 目录来源。
2. 刷新插件目录。
3. 搜索 `KooComic`、`KOOBONE` 或“漫画”并安装。

如果 Direct GitHub API 模式暂时搜不到，请切回默认 Storefront 目录。GitHub Topic 搜索存在分页、缓存和未认证请求限速，可能漏掉少量仓库。

### 手动安装

1. 从 [Releases](https://github.com/jackchensky/KooComic/releases/latest) 下载最新版 ZIP。
2. 解压后，将整个 `koocomic.koplugin` 文件夹复制到 `koreader/plugins/`。
3. 完全重启 KOReader，然后打开 `工具 → koo漫画`。

从 v0.3.1 或更早版本升级时，只删除旧的 `plugins/koobone.koplugin` **插件代码目录**；不要删除 `settings/koobone.lua` 和原有漫画下载目录，以便迁移登录状态与本地文件。升级前建议先备份这两处数据。

## 在线更新

插件从 GitHub Pages 读取固定版本清单，并通过 GitHub Release 下载更新包。发现新版本后，会先询问是否更新；只有确认后才会下载、校验和安装。

在线更新地址、更新提醒规则和完整功能说明见 [`koocomic.koplugin/README.md`](koocomic.koplugin/README.md)。开发与真机验证进度见 [`PROJECT_STATUS.md`](PROJECT_STATUS.md)。

## 隐私与安全

- 插件不包含安装量、设备型号或其他遥测统计。
- 只有主动勾选“记住密码”时，密码才会保存在 Kindle 本机设置文件中。
- 退出账号会清除会话和保存的密码，不删除已下载漫画。
- 请勿在 Issue 中上传密码、Cookie、完整签名下载地址或未脱敏日志。
- 提交截图前，请遮盖账号、邮箱和其他个人信息。

KOOBONE 没有提供面向本插件的公开 API，其网页端接口变化可能导致部分功能暂时失效。如果遇到问题，请在 [Issues](https://github.com/jackchensky/KooComic/issues) 中说明 Kindle 型号、KOReader 版本、插件版本和已脱敏的错误信息。

参与开发前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。涉及账号、会话、更新校验或其他安全问题时，请不要公开细节，改按 [`SECURITY.md`](SECURITY.md) 私密报告。

## English

**KooComic** is an unofficial KOReader connector for your personal KOOBONE comic library. It provides an e-ink-friendly cover shelf, search and filters, EPUB downloads with progress, local cover caching, account controls, adaptive layouts, and verified in-app updates.

Install it from KOReader Storefront, or download the latest package from [GitHub Releases](https://github.com/jackchensky/KooComic/releases/latest). Device compatibility may vary; privacy-safe reports are welcome in [Issues](https://github.com/jackchensky/KooComic/issues).

## 许可证与声明

本项目采用 [GNU Affero General Public License v3.0 only](LICENSE)，SPDX 标识为 `AGPL-3.0-only`。

本项目与 KOOBONE、Bookof.hk 及其开发者不存在隶属、赞助或官方合作关系。KOOBONE 名称仅用于说明兼容服务。
