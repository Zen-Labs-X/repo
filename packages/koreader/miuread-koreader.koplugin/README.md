# MiuRead · WeRead Assistant

MiuRead（觅阅 · 微信读书助手）是面向 KOReader 的非官方微信读书客户端。本仓库为 **Stable / 正式版通道**。

## Current Release

当前正式版本：`4.3.5`。

完整版本记录见 [`CHANGELOG.md`](CHANGELOG.md)。

## Installation

1. 在 GitHub Releases 下载最新正式版 `miuread-vX.Y.Z-full.zip`。
2. 解压后将完整的 `miuread.koplugin` 目录放入 KOReader 的插件目录。
3. 完整重启 KOReader。
4. 后续正式版可使用 MiuRead 内置更新功能升级。

## OTA Update Channel

从 `4.3.0` 起，正式版更新清单由 GitHub Actions 在发布时自动生成，并发布到固定 `stable-channel` Release。

- 新版正式 OTA：`stable-channel/update.json`
- 仓库根目录 `update.json`：仅作为旧正式版桥接入口
- 发布 `4.3.0` 时，workflow 会把根目录 `update.json` 更新为 4.3.0 并保持冻结，使 4.1.2 等旧版先升级到 4.3.0，再自动切换到新 OTA 通道。

## Release Process

- Stable tag：`vX.Y.Z`
- Stable Release：GitHub 正式 Release
- 版本记录：统一维护 `CHANGELOG.md`
- 创建正式 tag 后，GitHub Actions 自动校验版本、执行 Lua 5.1 语法检查、构建 full.zip、校验 SHA-256 与公开下载地址，并更新固定正式 OTA 清单。
- tag、`miuread.koplugin/miuread/config.lua` 与 `miuread.koplugin/_meta.lua` 中的版本必须一致。

## Origin and License

MiuRead originated as a modified version of `finlater/weread.koplugin` v0.1.1 and has since undergone substantial restructuring, modification, and extension.

MiuRead is an unofficial community project and is not affiliated with or endorsed by WeRead, Tencent, KOReader, or their maintainers.

This project is distributed under the GNU Affero General Public License version 3 only (`AGPL-3.0-only`). See `LICENSE`, `NOTICE`, and `THIRD_PARTY_NOTICES` for details.
