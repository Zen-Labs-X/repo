# Pinyin IME v1.1.0

本版本将原“常用双拼”按标准方案名称显示为“自然码双拼”，并正式验证 KOReader v2026.07。

## 更新

- 菜单、状态页和方案数据统一显示“自然码双拼”。
- 保留内部方案标识 `common` 与原有键位，旧设置无需迁移。
- 全量校验自然码键位和零声母规则；`zirjma` 的首选候选为“自然码”。
- 将 KOReader v2026.07 加入固定验证版本表。
- 全拼、其他双拼方案、词库、个性化学习和后续词联想保持不变。

## 安装

1. 下载并解压 `pinyinime.koplugin-v1.1.0.zip`。
2. 将顶层 `pinyinime.koplugin/` 复制到 `koreader/plugins/`。
3. 重启 KOReader，并启用简体中文键盘。
4. 进入 `设置 → 设备 → 键盘 → 拼音输入法`，确认版本为 `v1.1.0`。

最低支持 KOReader v2025.10；v2025.10、v2026.03 与 v2026.07 已正式验证。

- [完整版本说明](https://github.com/Merpyzf/pinyinime.koplugin/blob/main/versions/v1.1.0.md)
- [安装与使用说明](https://github.com/Merpyzf/pinyinime.koplugin/blob/main/README.md)
- [故障反馈说明](https://github.com/Merpyzf/pinyinime.koplugin/blob/main/SUPPORT.md)

压缩包 SHA-256：`f5319ae0253dbab2f6e7f94ab204b3de8ca69634451294e33a3d037572ddee36`
