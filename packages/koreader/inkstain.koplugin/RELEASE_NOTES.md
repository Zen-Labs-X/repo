## v3.0.2

【新增】
- 新增繁體中文（香港）语言包（zh-HK）
- 觅阅书架支持公众号/漫画（shelf_cache.mp）进度读取
- 觅阅进度新增云端回退：progress_remote_percent / progress_upload_percent / pending_progress.percent

【修复】
- 修复觅阅阅读记录同步率低的问题
  - 书名匹配升级为三级：精确匹配 → 规范化匹配（去空格/标点）→ 前缀/包含模糊匹配
  - stream 模式下从本地 library 补充书架进度
  - 增加详细调试日志，方便排查问题
- 修复 i18n 翻译条数统计一直显示 0 的 bug
- 补齐缺失的 async.lua / json.lua（OTA 异步更新依赖）

【优化】
- 壁纸语言菜单将「中文」改标为「简体中文」，新增「繁體中文（香港）」选项
- 觅阅进度读取增加容错，避免 sessions/library 为 nil 时崩溃