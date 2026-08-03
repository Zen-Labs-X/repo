# 觅阅 · 微信读书助手

KOReader 的微信读书插件，支持 Kindle、Kobo 与 Android 等 KOReader 设备。

## 当前版本

当前源码为 `4.0.0` 正式版，应提交到 `main` 分支。

详细变更见 `CHANGELOG-4.0.0.txt`。

## 分支与发布

- `main`：正式版源码，使用 `.github/workflows/release.yml` 发布并更新 `update.json`。
- `beta`：内测版源码，使用 `.github/workflows/release-beta.yml` 发布并更新 `update-beta.json`。

两个 workflow 都保留在默认分支，GitHub Actions 才会同时显示正式版与内测版入口。

## 安装

将完整安装包中的 `miuread.koplugin` 文件夹放入 KOReader 的 `plugins` 目录，然后完整重启 KOReader。
