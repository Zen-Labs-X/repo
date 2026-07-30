# 觅阅 · 微信读书助手

KOReader 的微信读书插件。

## 发布 3.0.1 正式版

1. 将本仓库包中的全部文件上传或覆盖到仓库 `main` 分支。
2. 打开 GitHub 仓库的 **Actions** 页面。
3. 选择 **Release full package**。
4. 点击 **Run workflow**，输入 `v3.0.1`。

workflow 会自动完成：

- 检查 `_meta.lua`、`config.lua` 与发布标签的版本号是否一致；
- 读取 `CHANGELOG-3.0.1.txt` 作为更新说明；
- 生成 `miuread-v3.0.1-full.zip`；
- 创建或更新 GitHub Release；
- 校验公开下载地址与安装包 SHA-256；
- 将新的 `update.json` 写入 `main` 分支，供插件在线更新。

## 仓库结构

- `miuread.koplugin/`：插件源码；
- `.github/workflows/release.yml`：正式版发布；
- `.github/workflows/release-beta.yml`：内测版发布；
- `CHANGELOG-3.0.1.txt`：3.0.1 更新说明。
