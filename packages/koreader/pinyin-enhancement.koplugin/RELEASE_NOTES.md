# v1.5.3

## What's Changed

- 对调拼音键功能：单击上屏拼音、长按清空拼音
- 添加换行键上屏拼音/候选词功能
- 修复单字母无法上屏拼音的问题

# v1.5.2

## What's Changed

- 添加扩展码表（可额外添加自定义码表）
- 注意：启用扩展码表前请先备份完整koreader文件
- 添加更新日志

# v1.5.1

- Fixed issue with unstable candidate word ordering (traditional Chinese characters appearing first)  #5 #7 
- Added control menu for enabling word frequency sorting
- Clearing candidate word usage records now takes effect immediately instead of after restart
- Optimized update channels: three options available - GitHub (latest), GitHub (pre-release), Gitee (latest)

# v1.5

添加首字母拼音码表，支持首字母匹配#4
添加词频统计，候选词按词频排序
菜单中清空候选词记录并重启koreader，则恢复原始排序
优化更新来源：支持 Gitee + GitHub 双源

#### 首字母拼音码表说明

- 根据 KOReader 源码 `ui/data/keyboardlayouts/zh_pinyin_data.lua` 生成
- 生成工具：`Node.js`
- 辅助模块：[pinyin-pro](https://github.com/zh-lx/pinyin-pro)
- 格式说明：`["aa"]={"啊啊"}`、`["bb"]={"爸爸","八百"}`
- 可按照相同格式增加映射，或替换整个码表内容

# v1.4

修复多个输入框时键盘指向问题 #3
