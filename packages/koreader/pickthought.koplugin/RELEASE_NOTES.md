## 本次更新

性能优化：
持久化正文 spine 缓存（PR #12/#19）
SQLite 句柄 LRU 与关书释放（PR #11/#18）
EPUB 大文件磁盘中转（PR #10）

新功能：
统一文件管理器与阅读器菜单
恢复想法弹窗按键翻页（Issue #16）
增加运行时划线样式切换（Issue #14）

问题修复：
修复大文件磁盘中转误报失败（PR #10）
限制想法弹窗切换重绘范围（Issue #16）
修正 addPath 调用语义（PR #10）
保留想法正文颜色（PR #9）
低内存 HTML/CSS 注入优化（PR #9）

---

## Contributors（本次更新的贡献者）

- @Mr54233
- @ksaMask123

---

## 安装

1. 下载 `pickthought.koplugin.zip` 并解压
2. 把 `pickthought.koplugin` 目录放到 KOReader 插件目录:
   `koreader/plugins/pickthought.koplugin`
3. 完全重启 KOReader,在「工具」菜单找到「撷思」

## 环境要求

KOReader ≥ v2026.03（需要内建的 `ffi/archiver` 与 `lua-ljsqlite3`）。

---

本插件衍生自 [miuread-koreader](https://github.com/miumiupy98-art/miuread-koreader) 与 [weread.koplugin](https://github.com/finlater/weread.koplugin),基于 AGPL-3.0 许可证发布。