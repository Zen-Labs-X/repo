# pinyinplus.koplugin

KOReader 拼音输入法增强插件。启用后，在中文拼音键盘上方显示候选词栏，并在输入过程中保留当前拼音状态，方便直接点选候选词输入汉字。

本项目基于 [pinyin_enhancement.koplugin](https://github.com/gytwo/pinyin_enhancement.koplugin) 修改和重构，主要优化候选词栏界面与输入体验。

## 功能

- 在拼音输入过程中显示候选词栏。
- 点击候选词即可直接输入对应汉字。
- 支持候选词翻页。
- 在输入框中实时显示当前拼音。
- 可在 KOReader 设置菜单中启用或关闭插件。
- 兼容 KOReader Terminal，避免中文键盘 IME 包装导致终端无响应。

## 效果图

<img src="screenshots/example1.png" alt="拼音候选词栏示意图 1" width="360">

<img src="screenshots/example2.png" alt="拼音候选词栏示意图 2" width="360">

## 安装

1. 下载或克隆本仓库。
2. 将整个 `pinyinplus.koplugin` 文件夹放入 KOReader 的 `plugins` 目录。
3. 重启 KOReader。

目录结构示例：

```text
koreader/
└── plugins/
    └── pinyinplus.koplugin/
        ├── _meta.lua
        ├── main.lua
        └── candidate_bar.lua
```

## 使用

1. 打开 KOReader 的设置菜单。
2. 进入 `拼音输入法增强`。
3. 确认 `启用拼音候选词` 已勾选。
4. 在中文拼音输入法中输入拼音，候选词栏会显示在键盘上方。
5. 点击候选词输入汉字，或使用左右翻页按钮查看更多候选词。

插件默认启用。关闭后需要重启 KOReader 才能完全生效。

## 候选词数据

候选词来自 KOReader 内置拼音数据表：

```text
frontend/ui/data/keyboardlayouts/zh_pinyin_data
```

如果需要扩展词库或支持首字母输入，可以从 KOReader 的拼音数据表入手调整。

## 说明

本插件不包含在线检查更新或自动更新功能。更新插件时，请手动替换 `pinyinplus.koplugin` 文件夹并重启 KOReader。

Terminal 使用中文键盘布局时会自动绕过拼音 IME，按键将直接发送给终端；普通输入框中的拼音增强不受影响。
