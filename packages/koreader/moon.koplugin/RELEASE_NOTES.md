# v0.0.8

## 月读 v0.0.8

KOReader 插件包：`book.koplugin-v0.0.8.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.0.7`：

#### 新功能

- :sparkles: (lockscreen): 使用 RGB 画布保留原始颜色 (c40628b)
- :sparkles: (plugin): 添加 KOReader 最低版本检查 (8dc3866)
- :sparkles: (copymanga): 支持已缓存章节直接打开 (8a8f305)
- :sparkles: (settings): 添加拷贝漫画配置支持 (7ae35f7)
- :sparkles: (book): 支持单书缓存清理与在线源同步删除 (3b4368f)
- :sparkles: (db): 已读标记同步进度至 100% (ab4e6ca)
- :sparkles: (copymanga): 添加后续章节后台预取 (251faa8)
- :sparkles: (copymanga): 添加后续章节后台预取 (3154f8a)
- :sparkles: (copymanga): 新增拷贝漫画数据源 (79642cb)
- :sparkles: (update): 展示月读更新日志并拆分安装流程 (e497af9)
- :sparkles: (store): 新增本地下载状态判断 (c27cecf)
- :sparkles: (catalog): 补充目录项的 path 字段 (12cfc3a)
- :sparkles: (update): 增加月读更新下载进度条 (4a747c8)

#### 修复

- :bug: (http): 修正连接状态探测逻辑 (6a30102)
- :bug: (lockscreen): 修正统计缓存并支持章节数 (b66ddac)
- :bug: (ui): 修正设置页分页高度计算 (c3c9200)
- :bug: (http): 避免离线时发起 HTTP 请求 (6ed9756)
- :bug: 修复失败 URL 缓存与离线连接失败处理 (f0f2497)
- :bug: (ui): 限制阅读器栏刷新区域 (7584742)
- :bug: (source): 限制缓存与待处理队列大小 (ac09eb3)
- :bug: (http): 修复 Turbo 连接失败导致离线崩溃 (c1529ce)
- :bug: (progress): 移除云端进度拉取失败弹窗 (aa98d62)
- :bug: (ui): 修正分页时当前页内容判断 (d03743b)
- :bug: (page_turn_animation): 修复日志模块引用 (57b40da)
- :bug: (page_turn_animation): 修复日志模块引用 (9566137)
- :bug: (reader_prefs): 修复插件字体冷启动回退默认字体 (8ad61c9)

#### 界面

- :lipstick: (copymanga): 将账户图标改为 account_circle (b09f8cb)
- :lipstick: (ui): 重构封面状态叠层并新增已读与下载标记 (1abb5af)

#### 重构

- :recycle: (ui): 重构图片解码为单任务后台队列 (fce986a)

#### 变更

- :white_check_mark: (tests): 为 reader bars 测试添加 ui/geometry 桩模块 (b4d033e)
- :white_check_mark: (tests): 添加拷贝漫画离线打开测试 (02a66fc)
- :white_check_mark: (tests): 重置网络管理模块缓存 (ad4280b)
- :white_check_mark: (tests): 重置网络管理模块缓存 (0ec8bd6)
- :globe_with_meridians: (l10n): 添加版本提示与未知版本翻译 (643b565)
- :white_check_mark: (tests): 增加拷贝漫画进度与目录缓存测试 (0802d98)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.0.7...v0.0.8

# v0.0.7

## 月读 v0.0.7

KOReader 插件包：`book.koplugin-v0.0.7.zip`

输入法词库（整库，手动 sideload）：`dictionary.sqlite3 dictionary-wubi.sqlite3 dictionary-cangjie.sqlite3 dictionary-zhuyin.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

词库 sideload：下载对应布局的词库，直接放入 KOReader 数据目录下的
`.moon/`（与 `book.sqlite3` 同级）。附件已使用最终文件名，无需重命名。

### 更新内容

相对上一版本 `v0.0.6`：

#### 新功能

- :sparkles: (update): 添加插件在线更新与校验安装 (caa3279)
- :sparkles: (ime): 支持大千注音 11 键候选栏布局 (73d2205)
- :sparkles: (remote): 新增月读数据目录配置 (cd1e987)
- :sparkles: (zlib): 调整镜像顺序并增加请求调试日志 (8a1f838)
- :sparkles: (jdread): 新增京东读书数据源 (17ad7d3)
- :sparkles: (book): 支持连续章节目录的章内锚点与原生目录适配 (443e35d)

#### 修复

- :bug: (xray): 修正标记点击手势处理 (581e095)
- :bug: (reader): 修复底栏手势劫持短按翻页 (db4266f)
- :bug: (ui): 修正原生面板菜单父级引用 (1f8a0e0)
- :bug: (ui): 修正原生面板菜单父级引用 (f56977e)
- :bug: (cache): 修复清缓存误删书籍元数据 (d096d5c)
- :bug: (http): 修复响应体读取的 Content-Length 解析与分块处理 (6a2827e)
- :bug: (progress): 修复阅读进度计算 (db44244)

#### 界面

- :lipstick: (l10n): 添加 X-Ray 刷新文案并更新缓存清理说明 (c7dc57a)
- :lipstick: (ui): 优化滑杆刷新并新增 xray 刷新动作 (3a343e2)
- :lipstick: (ui): 优化滑杆刷新并新增 xray 刷新动作 (744714f)
- :lipstick: (ui): 增加 show_status 控制封面状态显示 (8e7b883)
- :lipstick: (l10n): 新增阅读状态与京东登录文案 (954f716)

#### 重构

- :recycle: (settings): 重组桌面设置分类与文案 (efbb3bc)

#### 文档

- :memo: (docs): 更新图书馆设计说明 (242110f)
- :memo: (docs): 更新拼音词典手动安装说明 (a601290)

#### 变更

- :white_check_mark: (tests): 为 library 测试预加载 ui/geometry 桩模块 (59fc942)
- :white_check_mark: (tests): 更新下载、设置、阅读栏与标注测试 (6ac76fc)
- :white_check_mark: (tests): 添加注音、X-Ray、滑条与远程路径测试 (858f28c)
- :white_check_mark: (tests): 更新图书目录与词典可用性测试 (2bfefbe)
- :white_check_mark: (tests): 更新阅读状态、分类与自动标记测试 (2b6a6dd)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.0.6...v0.0.7

# v0.0.6

## 月读 v0.0.6

KOReader 插件包：`book.koplugin-v0.0.6.zip`

输入法词库（整库，手动 sideload）：`pinyin-dictionary-v0.0.6.sqlite3 wubi-dictionary-v0.0.6.sqlite3 cangjie-dictionary-v0.0.6.sqlite3 zhuyin-dictionary-v0.0.6.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

词库 sideload：拼音重命名为 `dictionary.sqlite3`；其他布局重命名为
`dictionary-wubi.sqlite3`、`dictionary-cangjie.sqlite3` 或 `dictionary-zhuyin.sqlite3`，
放入 KOReader 数据目录下的 `.moon/`（与 `book.sqlite3` 同级），然后重启。

### 更新内容

相对上一版本 `v0.0.5`：

#### 新功能

- :sparkles: (ime): 支持五笔、仓颉与注音输入法 (3d82b24)
- :sparkles: (settings): 支持选择中文输入法并统一词库管理 (c829485)
- :sparkles: (local): 未设置目录时引导用户设置 (0c090ad)
- :sparkles: (ui): 支持配置顶部状态栏项目显示 (21e6bd1)
- :sparkles: (ui): 支持配置顶部状态栏项目显示 (120ae45)

#### 修复

- :bug: 固定顶栏水平留白并记录字体加载 (5e670aa)
- :bug: (reader_prefs): 防止过期字体 id 覆盖原生菜单切换后的字体 (52cd77b)

#### 性能

- :zap: (xray): 添加标记扫描防抖和任务取消 (cfb97ac)

#### 重构

- :recycle: (xray): 改用 Job 处理标记扫描 (6977dce)
- :recycle: (xray): 改用 Job 处理标记扫描 (13d61f6)
- :recycle: (ime): 简化字根编码与键帽显示 (fa17f29)

#### 文档

- :memo: (docs): 更新输入法特性说明 (18815d7)
- :memo: 更新中文输入法文档 (22e9448)

#### 其他

- :wrench: (assets): 添加注音输入法字典清单 (bf45f34)
- :wrench: (assets): 添加注音输入法字典清单 (0629128)
- :wrench: (license): 删除许可证声明文本 (f8003bf)

#### 变更

- :white_check_mark: (tests): 更新输入法测试并补充多词库覆盖 (b0a0209)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.0.5...v0.0.6

# v0.0.5

## 月读 v0.0.5

KOReader 插件包：`book.koplugin-v0.0.5.zip`

拼音词库（整库，手动 sideload）：`pinyin-dictionary-v0.0.5.sqlite3`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

拼音词库 sideload：从 Release 下载 `pinyin-dictionary-v0.0.5.sqlite3`，重命名为 `dictionary.sqlite3`，
放入 KOReader 数据目录下的 `.moon/`（与 `book.sqlite3` 同级），然后重启。

### 更新内容

相对上一版本 `v0.0.2`：

#### 新功能

- :sparkles: (translate): 翻译弹窗支持可滚动全页显示 (95bcf49)
- :sparkles: (remote): 添加锁屏壁纸目录及公共目录访问控制 (29468e9)
- :sparkles: (db): 将书籍封面 URL 持久化到数据库 (96c7861)
- :sparkles: (lockscreen): 新增阅读票根组件 (2e2b567)
- :sparkles: (dictionary): 升级词典下载为实时进度条并支持桌面模式 (d64118a)
- :sparkles: (remote): 添加设备状态接口与首页状态展示 (ecea9be)
- :sparkles: (remote): 新增共享剪贴板页面及设备状态接口 (b062ca1)
- :sparkles: (remote): 重构文件管理页为资源管理器布局并新增拖拽上传与 ZIP 解压 (74a0a32)
- :sparkles: (remote): 重构文件管理页为资源管理器布局并新增拖拽上传与 ZIP 解压 (3aeaa71)
- :sparkles: (wechat): 微信读书日历支持按周展示阅读书目 (99bb832)
- :sparkles: (sync): 支持源侧注解清洗与串行同步 (dbb4135)
- :sparkles: (book): 添加独立文件日志模块 (4a7a777)
- :sparkles: (dictionary): 将字典下载入口移到查词菜单之后 (30f9572)
- :sparkles: (dictionary): 将字典下载入口移到查词菜单之后 (480fea7)
- :sparkles: (dictionary): 新增 Book 词典管理并接管原生词典菜单 (2f7af14)
- :sparkles: (dict): 添加多语言词典支持 (abbeb31)
- :sparkles: (dict): 添加多语言词典支持 (0b9d9f9)
- :sparkles: (lockscreen): 新增组合锁屏设置接口 (abc05e3)
- :sparkles: (ui): 添加弱化文字控件辅助函数 (37ae23a)
- :sparkles: (lockscreen): 新增本地化位置选项，并重构位置定义 (90f5371)
- :sparkles: (db): 添加 chapters 表 schema 初始化并修正模块路径 (9da1adc)
- :sparkles: (workers): 新增通用 Job 与 SQLite 常驻执行域 (463fa3e)
- :sparkles: (workers): 新增常驻 Worker 双向 IPC 基础设施 (340b92d)
- :sparkles: (reader): 新增阅读结束对话框 (b136348)
- :sparkles: 支持删除书籍并新增缓存任务列表 (660195d)
- :sparkles: (source): 新增全本缓存后台队列并加固写入失败处理 (17bbe28)
- :sparkles: (book): 新增章节缓存完整性判断 (4263227)
- :sparkles: (remote): 增加图片预览与上传冲突处理 (bad6662)
- :sparkles: (ui): 新增截图远程分享按钮 (076ac43)
- :sparkles: (ui): 在顶栏添加全本缓存状态显示 (fb0e30b)
- :sparkles: (zlib): 添加新的 Z-Library 镜像域名 (00e91ec)
- :sparkles: (chapter): 缓存章节时统计失败并返回部分完成结果 (db007ba)
- :sparkles: (book): 新增章节模式全本缓存 (36abb05)
- :sparkles: (reader): 将划词弹窗改为可配置工具栏并支持排序 (fe5d0da)
- :sparkles: (baike): 新增百度百科查询与 Edge 翻译开关 (b95c2f0)
- :sparkles: (book): 升级后首次启动时启用脚注弹窗链接 (7d0d2ff)
- :sparkles: (db): 新增书库增量迁移与批量取书 (9d544d0)
- :sparkles: (wechat): 新增 Skills Agent 网关以支持阅读统计 (0e2f444)
- :sparkles: (book_source): 新增 edit 能力标记以区分可编辑元信息的书源 (d9531a2)
- :sparkles: (wechat): 实现微信读书 Web 书城、笔记同步与阅读时长上报 (c89723e)
- :sparkles: (ui): 顶栏点击源名切换数据源 (c611dc9)
- :sparkles: (translate): 添加常用翻译语言并重构翻译弹窗 (9f0d785)
- :sparkles: (ui): 新增翻译弹窗与阅读设置页面，重构顶底栏偏好 (8fd72df)
- :sparkles: (ui): 在面板标题中显示当前章节标题 (2a4d852)
- :sparkles: (book): 新增全书阅读排版偏好持久化与自动应用 (0b2ebea)
- :sparkles: (ui): 重构首页为可配置组件布局并支持阅读字体切换 (aa8ec79)
- :sparkles: (reflow): 为本地 TXT/MOBI 排版添加章节预览与确认替换流程 (9818ccd)
- :sparkles: (xray): 重构 X-Ray 为原文实体抽取并新增页内标记 (aeb3e96)
- :sparkles: 添加海报墙锁屏组件，移除 WebDAV 与拷贝漫画源 (dd4a0dc)
- :sparkles: (ui): 新增截屏快捷动作并更新多语言文案 (4b9f80f)
- :sparkles: (source): 新增拷贝漫画源，移除 RSS 订阅 (3c2a360)
- :sparkles: (panel): 新增远程管理快捷动作及动作列表工具 (0bb3194)
- :sparkles: (ui): 在设置中添加翻页动画开关 (bed3baf)
- :sparkles: (patch): 翻页动画期间强制完全刷新为从不以避免闪烁 (3a2e18a)
- :sparkles: (utils): 新增通用网络图片目录及初始化函数 (d8aa09f)
- :sparkles: (koplugin): 添加补丁备份与启动打开功能，更新快捷面板配置 (e2ae45b)
- :sparkles: (patch): 添加补丁管理器与翻页动画补丁功能 (d9f2568)
- :sparkles: (ui): 为进度条组件添加动态设置百分比能力 (a13d503)
- :sparkles: (remote): 添加连接配置页面与 API (8a4b797)
- :sparkles: (remote): 添加连接配置页面与 API (32cd0c2)
- :sparkles: (ai): 添加 AI 连接测试功能 (6ef4ffb)
- :sparkles: (pinyin): 添加拼音整库 Release 分发与手动 sideload 提示 (b36e8d7)
- :sparkles: (ui): 优化词库下载对话框的进度显示逻辑 (b3b6830)
- :sparkles: (ui): 字体选择器支持系统字库并改为三栏切换 (31e3724)
- :sparkles: (reader): 新增阅读风格预设 (63690cf)
- :sparkles: (progress): 在阅读进度中记录章节标题与页码 (52a1d93)
- :sparkles: (db): 在进度记录中新增章节标题与页码信息 (0eef874)
- :sparkles: (lockscreen): 重构锁屏设置并新增自定义留言 (b62fb5c)
- :sparkles: (settings): 更新锁屏默认组件并添加自定义文案 (6009a12)
- :sparkles: (lockscreen): add reading stats layouts and cover background (f809d95)
- :sparkles: (lockscreen): 重构锁屏样式并新增阅读统计柱图 (37ec132)
- :sparkles: (lockscreen): 重构锁屏样式并新增阅读统计柱图 (17cd6c2)
- :sparkles: (ai): 添加可复用的AI门面并重构设置UI (86151d9)
- :sparkles: (dict): 添加词典清单文件 (ee21831)
- :sparkles: (ui): 新增 AI 总结与字典管理，重构统计页为三页 (c36a31e)
- :sparkles: (dictionary): 新增 StarDict 词典管理模块 (ca3c1c0)
- :sparkles: (db): 数据库层重构为向前迁移并支持同步状态持久化 (39a3eb5)
- :sparkles: (convert): 添加 MOBI 转 EPUB 功能 (8f61b84)
- :sparkles: (xray): add AI-powered X-Ray reader plugin (fbf25d7)
- :sparkles: (sync): 启动时异步重试未完成的数据同步 (589312a)
- :sparkles: (lockscreen): 新增书架锁屏样式 (4f2c86c)
- :sparkles: (ai): 添加 AI 阅读分析与图谱模块 (4f8a16c)
- :sparkles: (pinyin): 支持词库断点续传并按构建版本标识 (751457e)
- :sparkles: (ui): 为书库界面增加仅搜索模式与自定义回调 (5042333)
- :sparkles: (utils): 新增 Text.truncateUtf8 按字节截取 UTF-8 字符串 (991b55e)
- :sparkles: (ui): 支持 popup 保持菜单打开 (47da30a)
- :sparkles: (translate): 添加 Microsoft Edge 翻译服务适配 (2e5fa13)
- :sparkles: (book): 新增阅读统计模块 (fbd576e)
- :sparkles: (http): 添加流式HTTP请求支持并修复headers处理 (58fd5da)
- :sparkles: (book): 新增阅读注解的保存、导入与同步功能 (96ad737)
- :sparkles: (convert): 改进 TXT 转 EPUB 章节识别与元数据提取 (d749f3e)
- :sparkles: (utils): 添加章节路径与 UTF-8 校验，扩展阅读设置 (918ecf7)
- :sparkles: (ui): 重构锁屏设置，支持自定义背景壁纸、一言与阅读统计 (95dabf9)
- :sparkles: (ui): 添加居中弹窗选项支持 (d596e12)
- :sparkles: (lockscreen): 新增阅读统计、阅读账单和一言锁屏样式 (742699f)
- :sparkles: (utils): 新增锁屏资源目录管理 (37f388c)
- :sparkles: (ui): 增强列表选择组件并新增目录选择器 (5d6164d)
- :sparkles: (lockscreen): 添加新样式并简化锁屏配置处理 (0c945c3)
- :sparkles: (lockscreen): 添加新样式并简化锁屏配置处理 (e9c4bda)
- :sparkles: (lockscreen): 优化锁屏预生成逻辑，新增高亮变化触发 (bc50168)
- :sparkles: (pinyin): 以候选栏取代原生 IME 候选包装 (47e738b)
- :sparkles: (settings): 新增拼音词库下载增强与调试日志开关 (e18969e)
- :sparkles: (ui): 重构桌面设置页并新增语言、锁屏等子页 (b4e632d)
- :sparkles: (book): 实现进度冲突提示与拼音词库增强 (56cbe26)
- :sparkles: (db): 新增 toc 目录缓存与书籍身份反查 (7ec6989)
- :sparkles: (pinyin): add pinyin dictionary support (1392a42)
- :sparkles: (remote): 添加共享剪贴板功能 (3184142)
- :sparkles: (pinyin): 新增中文键盘入口插件模块 (a4ee9ff)
- :sparkles: (pinyin): 新增中文键盘入口插件模块 (55eefa5)
- :sparkles: (remote): 新增远程文件管理与远程输入服务 (3792953)
- :sparkles: (settings): 新增远程传书与拼音候选输入设置 (f776760)
- :sparkles: (remote): 添加远程传书服务，并在休眠/唤醒/退出时管理 (3a4328e)
- :sparkles: (lockscreen): 新增锁屏显示功能，支持跟随 KOReader 或摸鱼日报 (5e201ac)
- : :sparkles: (local): 新增编辑分类/系列时物理移动书籍文件 (338c720)
- :sparkles: (ui): 重做书籍详情页并加入阅读统计与编辑功能 (00147be)
- :sparkles: (local): 支持二级子目录系列并重构扫描为子进程任务 (1b7028d)
- :sparkles: (ui): 添加网格最大列数设置 (e971047)
- :sparkles: (utils): 添加基于 UIManager 调度的防抖与节流工具 (ad953eb)
- :sparkles: (setting): 显示配置的实际路径 (caf450a)
- :sparkles: (ui): 为列表控件增加单选/多选支持 (0ace0ef)
- :sparkles: (annotations): 新增注解快照同步功能 (ae8bd2c)
- :sparkles: (source): 添加书城下载导入并修复微信会话逻辑 (adb0948)
- :sparkles: (zlib): 接入 Z-Library 书库与加入书库流程 (a5ce5d8)
- :sparkles: (zlib): 实现多镜像故障转移与重定向处理 (de46d97)
- :sparkles: (http): 添加 allow_redirects 选项控制重定向跟随 (944fcac)
- :sparkles: (zlib): 新增 Z-Library 书城客户端及相关模块 (3023f6c)
- :sparkles: (zlib): 新增 Z-Library 书城客户端及相关模块 (6eccab1)
- :sparkles: (zlib): 新增 Z-Library 书城客户端及相关模块 (6eb18b4)
- :sparkles: (webdav): 新增异步文件上传方法 putFileAsync (dafab1c)
- :sparkles: (cache): 新增书籍缓存管理模块 (8e7fe16)
- :sparkles: (rss): add RSS subscription source support (9da5d7e)
- :sparkles: (koplugin): 桌面打开时通知源进行后台维护 (faca7b1)
- :sparkles: (scrape): add book metadata scraping feature (436344c)
- :sparkles: (stats): 添加异步阅读统计同步与追踪模块 (b7025fa)
- :sparkles: (book): 添加 html2epub 功能模块 (fb58411)
- :sparkles: (ui): 添加 Material Icons 图标组件 (60cb4e5)
- :sparkles: (http): 添加 Turbo ioloop 支持以确保 HTTP 请求正常工作 (d94d312)
- :sparkles: (db): 添加完整的 SQLite 数据库访问层 (d5bc4ad)
- :sparkles: (tests): 增加 async api 和 utils task 的测试用例 (9a28bb0)
- :sparkles: (book): 添加子进程任务管理模块 (3ec87d3)
- :sparkles: (book): 添加子进程任务管理模块 (d0df2c2)
- :sparkles: (db): 引入 SQLite 缓存层并迁移旧存储数据 (c12bf0b)
- :sparkles: (http): 新增 HTTP 响应缓存模块及清理接口 (25b8463)
- :sparkles: (utils): 优化目录结构并引入设置持久化模块 (c18bb3a)
- :sparkles: (types): 添加书籍管理、阅读进度与统计洞察的类型定义 (3ed8b15)
- :sparkles: (utils): 添加 UI 线程 Promise 与防抖节流工具 (a1f3b5c)
- :sparkles: (wechat): 实现微信读书 Web 扫码登录与会话管理 (aa21169)
- :sparkles: (ui): 扩展 Popup 组件支持自定义控件与动态尺寸 (834105d)
- :sparkles: (book): 新增插件界面字体选择与动态加载功能 (abedc1b)
- :sparkles: (http): 新增内部 HTTP 客户端与 WebDAV 工具模块 (f5e0218)
- :sparkles: (ui): 支持列表项图文渲染，新增数值增减弹窗组件 (a986998)
- :sparkles: (ui): 添加设置行组件 (3d9dada)
- :sparkles: (moon, ui): 添加单飞异步协调器与图片组件 (f8dba4d)
- :sparkles: (ui): 重构统计页为双分页布局并清理冗余组件 (f602269)
- :sparkles: (ui): 新增底部统一分页导航组件 (2cdc5e5)
- :sparkles: (ui): 新增书籍信息共用组件 (d6249e6)
- :sparkles: (moon): 添加异步任务调度器，防止 UI 阻塞 (2af3066)
- :sparkles: (ui): 新增桌面端底部导航栏组件 (a9d2508)
- :sparkles: (ui): 新增桌面顶部状态栏组件 (8e70f64)
- :sparkles: (book): 实现多数据源架构、国际化支持与核心基础模块 (e6e638a)

#### 修复

- :bug: (remote): 修正壁纸目录路径拼接 (a52d875)
- :bug: (ui): 修复面板切换时序及底栏模式切换逻辑 (b326489)
- :bug: (ui): 修复面板切换时序及底栏模式切换逻辑 (d0b25a4)
- :bug: (pinyin): 网络不可用时改为立即提示而非静默等待 (12f68eb)
- :bug: (book): 使用 HTTP 响应头改进下载进度与校验 (849d94d)
- :bug: (lockscreen): 修复固定形态组件污染共享宽窄屏偏好 (1a57e59)
- :bug: (lockscreen): 修复固定形态组件污染共享宽窄屏偏好 (07fb91c)
- :bug: (reader): 导航到目标章节时关闭过渡提示 (f841ff7)
- :bug: (book): 修复稀疏远端行清空已有元数据的问题 (d10e09c)
- :bug: (ui): 修复弹窗关闭、首页刷新竞态及底栏几何计算 (10270d0)
- :bug: (log): 同一天内重启时保留已有日志 (f7f596b)
- :bug: (wechat): 修复划线与想法同步坐标 (7b85fc5)
- :bug: (reader): 关书时仅上推脏进度，避免回拉覆盖 (4ba99ac)
- :bug: (pinyin): 修复下载校验与键盘关闭时的查询残留 (ca73801)
- :bug: (library): 修复封面路径使用错误的 source_id (e74b5ce)
- :bug: (library): 修复封面路径使用错误的 source_id (84913b8)
- :bug: (db): 修正 http.lua 对非字符串参数的处理 (ab073bf)
- :bug: (pinyin): 加固 manifest 校验与文件写入 (4aef97b)
- :bug: (http): 修复 HTTP 请求异常与取消路径下输入超时未释放 (01b7720)
- :bug: (lockscreen): fix narrow canvas dropping poster columns (3095909)
- :bug: (local): 扫描后保留失效书籍的封面缓存 (0247bfc)
- :bug: 修复注解同步与数据保留的多个问题 (787d343)
- :bug: (stats): 修复 saveSource 整表覆盖丢失 token 的问题 (03ac49b)
- :bug: (ui): 修复数据源不支持编辑时仍可编辑元信息的问题 (a8d4878)
- :bug: (reader): 修复连续章节关闭时字体偏好被空值覆盖 (444888b)
- :bug: (db): 修复最近阅读进度与图书馆不一致 (ce2152f)
- :bug: (progress): 修复章内进度冲突检测与冷打开恢复 (15c930b)
- :bug: (remote): 修复本地IP获取并重命名服务为远程管理 (e453011)
- :bug: 修复锁屏刷新背景调用 (cf9de26)
- :bug: (ui): 重置商店状态变量 (a01f488)
- :bug: (store): 添加异步操作后文档一致性校验 (206e184)
- :bug: (lockscreen): 修复 KOReader 未初始化时锁屏设置默认值处理 (d1bbf60)
- :bug: (ui): 修复详情修改后关闭时桌面未正确刷新 (b56e8a4)
- :bug: (scrape): 修复豆瓣年份识别与微信读书分隔符解析 (634f99e)
- :bug: (chapters): 修复无目录时预取章节可能越界的问题 (4b58009)
- :bug: (paths): 修复 slugFor 对空 stable_id 生成固定哈希的问题 (78a9f30)
- :bug: (book): 修复缓存目录删除失败时的误判 (b588f29)
- :bug: (rss): 修复属性值中的 > 导致 XML 标签结束判断错误 (17ec895)
- :bug: (queue): 隔离队列回调异常避免卡死队列 (5bc2289)
- :bug: 为书库更新添加事务并修复 http 删除的 LIKE 转义 (d09e267)
- : :bug: (parser): 修复 Rss URL scheme 白名单校验顺序 (63885eb)
- :bug: (scrape): 修复豆瓣抓取失败并完善结果选择页 (bceab5b)
- :bug: (ui): 修复图标尺寸计算错误导致 DPI 缩放异常的问题 (a6873a2)
- :bug: (moon): 初始化时安全应用当前字体设置 (b8febe0)
- :bug: (plugin): 修复菜单项文本返回 nil 并支持开机自启提示 (b7268af)
- :bug: (ui): 增加桌面端 UI 的异步请求取消与清理逻辑 (1cc31d5)

#### 界面

- :lipstick: (lockscreen): 修复账单与收据头部布局对齐 (a70d535)
- :lipstick: (lockscreen): 重构锁屏组件布局并支持品牌 Logo 与图片渲染 (af7b793)
- :lipstick: (lockscreen): 将阅读账单重构为热敏小票风格 (2311893)
- :lipstick: (lockscreen): 为锁屏收据组件添加左右列间距 (36124ed)
- :lipstick: (ui): 使首页封面格子与图书馆一致 (003a84f)
- :lipstick: (ui): 调整书籍网格列数范围 (59719a2)
- :lipstick: (translate): 调整翻译弹窗布局，移除译文嵌套边框 (1334154)
- :lipstick: (settings): 将本地源设置移至列表底部 (bbc22e3)
- :lipstick: (remote) 重构远程管理页面灰色系设计 (aeda5f9)
- :lipstick: (ui): 支持设置行背景可配置 (024f3e6)
- :lipstick: (lockscreen): refine stats card layout and spacing (ebaf2bc)
- :lipstick: (lockscreen): 调整白卡高度贴合 hero 内容，减少上下留白 (d4ca8ac)
- :lipstick: (lockscreen): 对齐 DESIGN.md 重设计锁屏样式与账单柱图 (757c9b6)
- :lipstick: (ui): 重构顶栏布局并替换电池图标 (3ba8529)
- :lipstick: (ui): 调整TopBar显示顺序并修正source_id引用 (88164ff)
- :lipstick: (ui): 优化底部标签栏选中态样式，适配墨水屏显示 (5e8f46c)
- :lipstick: (ui): 修复高分辨率下分页控件溢出并自适应间距 (b755d54)
- :lipstick: (ui): 调整书籍信息界面文本为加粗样式 (4cc0003)
- :lipstick: (ui): 添加统一的页面边距、间距与顶部状态栏高度配置 (ac8e7ff)

#### 性能

- :zap: (ui): 串行化图片解码并支持字体安装对话框取消 (8ec9c87)
- :zap: (xray): 将全书文本扫描迁移至子进程执行 (ff66214)
- :zap: (remote): 将远程文件服务改为异步 worker 执行，避免阻塞 UI (45b92c9)
- :zap: (book): 移除本地导入并接入调试性能日志 (4eea280)
- :zap: (book): 合并首页后台刷新并补充 worker 任务名 (2094de3)
- :zap: (book): 合并首页后台刷新并补充 worker 任务名 (8b1b3a2)
- :zap: (book): 移除本地导入并接入调试性能日志 (31d29ef)
- :zap: (cache): 优化缓存写入与变更通知调度 (1b5f0f8)
- :zap: (koplugin): 优化书架同步与章节切换性能 (45f7506)
- :zap: (ui): 优化阅读器绘制热路径并简化本地章节打开 (06f9fac)
- :zap: (ui): 重构图片加载，子进程异步解码并新增 sync 模式 (43b0688)
- :zap: (chapter): 添加本地章节快开与后台刷新 (5b506d7)
- :zap: (pinyin): 优化候选查询与候选栏渲染 (e3a7eb9)
- :zap: (pinyin): 优化拼音查询使用 GLOB 前缀匹配 (d2e4544)
- :zap: (pinyin): 优化候选查询并调整键盘布局 (1509ad1)
- :zap: (ui): 优化输入超时设置并新增设置缓存测试 (51572f5)

#### 重构

- :recycle: (ui): 抽取设置子页导航到桌面方法 (dfcb581)
- :recycle: (sync): 重构同步与统计存储以降低内存占用 (e3ad1fb)
- :recycle: (xray): 将实体标记扫描从全书后台 Job 改为仅当前可见页 (0165df5)
- :recycle: (ui): 重构图片下载为有限并发队列模式 (f84d528)
- :recycle: (book): 重构阅读进度百分比解析逻辑 (966f6de)
- :recycle: (book): 简化书籍下载逻辑并移除最近阅读列表 (fad0cf3)
- :recycle: (book): 简化书籍下载逻辑并移除最近阅读列表 (9fb277c)
- :recycle: (stats): 重构阅读统计为单次全量拉取，移除阅读洞察 (8fc3a2e)
- :recycle: (sync): 重构统计同步为全量快照模式并优化进度/日志处理 (b30d6b1)
- :recycle: (stats): 重构统计同步流程：支持双向同步、总量聚合与请求取消 (5650898)
- :recycle: (ui): 优化封面与最近阅读组件的动态尺寸计算 (d270f35)
- :recycle: (ui): 重构首页弹性布局并拆分当前阅读组件 (8b5442a)
- :recycle: (note): 重构注解合并与快照兼容 (7cfa128)
- :recycle: (ci): 将发布标题由 Book 改为月读 (36cf06a)
- :recycle: (plugin): 重命名 Book 插件为月读并完善日志 (782161d)
- :recycle: (book): 重构数据库持久化为同步写库并迁移模块路径 (ef57f36)
- :recycle: (reader): 重构章节会话导航与目录加载 (a7038eb)
- :recycle: (reader): 重构章节会话导航与目录加载 (7dae28a)
- :recycle: (dictionary): 迁移词典 UI 模块并更新引用 (236562d)
- :recycle: (dictionary): 迁移词典 UI 模块并更新引用 (2580a15)
- :recycle: (desktop): 重构 UI 与设置模块并新增词典设置 (045a4a9)
- :recycle: (desktop): 重构首页组件与唤醒刷新流程 (24d2a9f)
- :recycle: (lua): 重构休眠前流程，完善锁屏刷新与词典初始化 (bcb3b13)
- :recycle: (convert): 改用 workers.job 打包 epub (6e48d6d)
- :recycle: (scrape): 重构刮削流程并修复搜索与元数据保存问题 (dd726be)
- :recycle: (http): 重构缓存与请求模块，增强健壮性 (a634114)
- :recycle: (lockscreen): 重构锁屏组件，抽取公共书库辅助模块 (fec9000)
- :recycle: (ui): 更新设置界面引用的锁屏模块 (731ee92)
- :recycle: (lockscreen): 重构锁屏组合图生成与设置管理 (7fce65a)
- :recycle: (ui): 将图片加载逻辑迁移到 workers.job (ccd44e8)
- :recycle: (types): 更新书籍类型注解 (d4b9a6d)
- :recycle: (xray): 重构实体存储与标记刷新流程 (6056ba4)
- :recycle: 用 workers.job 替换 utils.task，重构拼音候选条查询 (88abd1c)
- :recycle: (font): 改用 Job 子进程扫描与解压字体 (99ab257)
- :recycle: (db): 重构书籍数据库层，移除 favorite 与 last_chapter_idx 字段 (e9f9828)
- :recycle: (db): 用 record_type 区分阅读统计记录类型 (9dc7ad7)
- :recycle: (db): 重构 progress 查询，source_id 改为必填参数 (ff2ea0e)
- :recycle: (db): 重构进度模块并新增待同步进度表 (487c4c4)
- :recycle: (db): 重构笔记数据库模块并抽取建表逻辑 (7687098)
- :recycle: (db): 移除重复的 Base.ensure() 调用 (a0c9909)
- :recycle: (db): 用 Base.ensure() 替换 assertMainProcess() (da5b26f)
- :recycle: (db): 重构 X-Ray 数据层并支持原子替换 (0465363)
- :recycle: (db): 重构 http 缓存模块并新增建表初始化 (be08f8c)
- :recycle: (db): 将建表逻辑拆分为 schema 模块并禁止子进程访问数据库 (6692055)
- :recycle: (workers): 重构为一次性 Job 与轻量 SimpleJob (fcb6208)
- :recycle: (lockscreen): 优先使用 MoonSettings.activeSourceId() 获取当前源 (e9c00e0)
- :recycle: (lockscreen): 优先使用 MoonSettings.activeSourceId() 获取当前源 (458475b)
- :recycle: 重构首页书架同步逻辑并更新网格列数文案 (3047ae1)
- :recycle: (ui): 重构首页刷新逻辑并将全本缓存改为后台队列 (96a26a9)
- :recycle: (book): 重构封面提取流程并精简文档 (555e3a3)
- :recycle: 抽取注解归一化与阅读位置纯计算并拆分远程管理 UI (69a6e8d)
- :recycle: (sync): 重构阅读同步：注解原生定位、进度精确恢复、统计支持拉取 (de6562e)
- :recycle: (ui): 重构最近列表网格并统一卡片间距 (63f9839)
- :recycle: (ui): 重构主页布局与组件注册 (1bb3e10)
- :recycle: (home): 重构首页组件与设置分组 (5d5776d)
- :recycle: (reader): 重构阅读会话为整书/连续章节双模式 (5ca5190)
- :recycle: (ui): 重构状态栏为原生栏叠加层并移除阅读风格预设 (2e475e2)
- :recycle: (reader): 将剩余阅读时间估算逻辑迁移至 session 模块 (655b816)
- :recycle: (ai): 重构 AI 响应处理并默认禁用推理 (298bc09)
- :recycle: (ui): 统一桌面与阅读快捷面板到共享动作注册表 (4a68241)
- : :recycle: (ui): 重构设置界面快捷面板，支持多个部分 (20aaecb)
- :recycle: 重命名图片缓存目录接口并更新测试 (9171e6f)
- :recycle: (koplugin): 重构初始化并添加补丁管理 (ce55b8b)
- :recycle: (remote): 重构文本 body 处理并修复端口规则泄漏 (862a4ab)
- :recycle: (pinyin): 重构候选条为自研 Strip 组件 (2f2b3a3)
- :recycle: (pinyin): 重构候选条为自研 Strip 组件 (13e5e2d)
- :recycle: (lockscreen): refactor lock screen subjects and background assets (6e8f5dd)
- :recycle: (lockscreen): 重构锁屏组件注册为清单驱动 (b95e220)
- :recycle: (lockscreen): 精简布局返回值并补充注释 (2984c60)
- :recycle: (ui): 移除图表的 track_empty 选项 (25c6584)
- :recycle: (lockscreen): 重构锁屏测试以适配组合壁纸 (be94f63)
- :recycle: (lockscreen): 重构锁屏为背景 × 主体 × 九宫格的组合式架构 (61ffa01)
- :recycle: (chart): 抽取柱状图渲染为共用组件 (c8267cf)
- :recycle: (chart): 抽取柱状图渲染为共用组件 (d1aa727)
- :recycle: (settings): 拆分配置存储并重构字体选择器 (0eb29aa)
- :recycle: (ui): 引入 surface 组件统一卡片与胶囊样式 (19354c1)
- :recycle: (translate): 重构 Edge 翻译传输并添加语言检测 (752b2d0)
- :recycle: (translate): 重构 Edge 翻译传输并添加语言检测 (1e90b95)
- :recycle: (source): 重构数据源为本地目录+对账模型，新增整本/按章打开流程 (137f049)
- :recycle: (sync): 重构同步流程为统一编排并新增书库读取模块 (0f03097)
- :recycle: (types): 更新书架同步 API 类型定义 (676ba0c)
- :recycle: (store): 重构书城搜索与分页 (e1afe73)
- :recycle: (zlib): 重构客户端并在请求缓存与镜像迁移处理上增强 (d2e719e)
- :recycle: (types): 重构书籍源接口类型定义 (dc0c8a3)
- :recycle: (ui): 更新 bookinfo 组件中 stable_id 的访问方式 (83f68b7)
- :recycle: (book): 重构阅读插件事件处理与模块架构 (d8d03d4)
- : :recycle: (db): 重构数据库 schema 并加入版本管理 (4f19d32)
- : :recycle: (db): 重构数据库 schema 并加入版本管理 (5f3a904)
- :recycle: (book): 重构书籍身份类型，将 BookRef 改为 BookIdentity (671fb9b)
- :recycle: (lockscreen): 重构上下文获取逻辑并优化章节计数 (1a6d1e5)
- :recycle: (reader): 重构书籍阅读会话生命周期与章节切换逻辑 (90db301)
- :recycle: (progress): 重构进度模块以使用阅读会话快照 (74ae51f)
- :recycle: (scrape): 重命名参数以使用 BookIdentity (619cd05)
- :recycle: (cache): 改用 books/chapters 路径登记管理缓存清理 (92cb65d)
- :recycle: (progress): 重构进度保存与同步流程 (e05397a)
- :recycle: (book): 重构书籍身份解析与异步落库 (dc13a97)
- :recycle: (book): 重构打开流程为源驱动并移除 opens 表 (418919b)
- :recycle: (desktop): 重构设置拆分架构并新增快捷面板原生菜单入口 (955c047)
- :recycle: (reader): 重构阅读控制台为顶部/底部工具栏 (e200e5e)
- :recycle: (convert): 重构TXT/HTML转EPUB的分章与目录逻辑 (c810538)
- :recycle: (lockscreen): refactor myrl style and fix image path (237ba8a)
- :recycle: (setting): 重构书库目录选择流程 (792ec00)
- :recycle: (lua): 重命名循环变量 (3a0ef4a)
- :recycle: (lockscreen): 重构锁屏插件并抽象样式接口 (b6c5168)
- :recycle: (ui): 重构文件管理界面和交互逻辑 (6bf1fdb)
- :recycle: (ui): 重构设置页为二级子菜单并增强源管理 (cfb3929)
- :recycle: (local): 将单本导入抽取到客户端并移除整库重扫 (132bb11)
- :recycle: (utils): 抽取公共文本处理工具到 utils.text (3e70a34)
- :recycle: 统一缓存目录初始化并适配子进程扫描测试 (a3cc800)
- :recycle: (utils): 将节流实现改为墙钟时间判断 (f2e413d)
- :recycle: (utils): 将节流实现改为墙钟时间判断 (21675b1)
- :recycle: (source): 重构数据源契约并以 type 分类替代 capabilities (ad9c780)
- :recycle: (tests): 移除已下线 API 的测试并迁移到新接口 (63c59a1)
- :recycle: (ui): 重构底栏为通用组件 (49a997c)
- :recycle: (ui): 重构底栏为通用组件 (8a20e06)
- :recycle: (book): 将缓存管理拆分为 book.cache 并移除旧 chapter 入口 (86befd7)
- :recycle: (rss): 用select代替哑变量获取feeds的第二返回值 (49d0c99)
- :recycle: (reader): move reader modules under ui/reader namespace (a0b2e56)
- :recycle: (reader): 移除Session.emit间接调用，直接分发page_changed事件 (0e0b68f)
- :recycle: (plugin): 简化返回逻辑并移除未使用的函数 (d2c9647)
- :recycle: (core): 以 (source_id, stable_id) 重建书籍身份并迁移按章阅读 (07b30e6)
- :recycle: (core): 以 (source_id, stable_id) 重建书籍身份并迁移按章阅读 (28b9430)
- :recycle: (source): 重构数据同步为全异步并新增本地书库支持 (8c04f43)
- :recycle: (source): 重构书源类型定义，增加异步接口与错误处理 (826c389)
- :recycle: (ui): 重构图标系统并移除阅读悬浮菜单 (4d97f87)
- :recycle: (ui): 将桌面端同步 API 调用重构为异步回调 (2338ff9)
- :recycle: (ui): 重构 tab 检查并新增 sourceChanged 处理 (ecb12a5)
- :recycle: (db): 重构数据库并发访问并新增阅读统计 (b67dbf0)
- :recycle: (book plugin): 用 Tracker 和事件通知重构生命周期 (218ad3a)
- :recycle: (settings): 缓存 LuaSettings 实例，首次打开即填充默认键并写回 (7ee2020)
- :recycle: 移除 book.l10n 中的调试日志 (b00acc3)
- :recycle: (http): 用 DbQueue 替代 Task 处理缓存读写 (b870151)
- :recycle: (db): 重构 source_id 校验并将 book_key 生成移至 BookRef.keyOf (80f3e59)
- :recycle: (tests): 重构书籍模块路径并更新测试 (8097083)
- :recycle: (types): 重构书籍类型定义，优化数据结构 (d5476d4)
- :recycle: (db): 使用参数化查询替换字符串格式化以提高安全性 (f94407d)
- :recycle: (ui): 重构图片组件以支持网络图和本地路径，优化下载逻辑 (39522f8)
- :recycle: (http): 重构缓存模块以支持异步操作和子进程数据库访问 (3652512)
- :recycle: (utils): 重构缓存目录确保逻辑 (6bcf58a)
- :recycle: (book): 重构书库插件架构，拆分存储、章节与进度模块 (78c8a79)
- :recycle: (api): 重构网络请求层并集成内置缓存 (7fca50a)
- :recycle: (ui): 重构字体选择器异步逻辑，迁移至 Promise 模式 (a8c5e12)
- :recycle: (desktop): 重构设置界面，提取通用组件并优化布局结构 (cdc73a6)
- :recycle: (settings): 按数据源拆分配置模块并重构设置 UI (caa7026)
- :recycle: (ui): 重构桌面端模块路径并简化重建逻辑 (e37f4bf)
- :recycle: (book): 重构 Book 插件初始化流程与设置接口 (373975d)
- :recycle: (l10n): 移除废弃的书籍状态本地化词条 (878c2b4)
- :recycle: (i18n): 清理废弃本地化字符串并优化错误提示文案 (e60d14f)
- :recycle: (utils): 重构 promise 与 timing 模块，完善 Luadoc 注释并修复 Lua 5.1 兼容问题 (414bb7c)
- :recycle: (http): 捕获 HTTP 响应头变量 (3a93b86)
- :recycle: (paths): 重构目录结构与路径管理，支持多源隔离 (4a96b1c)
- :recycle: (font): 重构字体模块与选择器，分离配置写入与应用逻辑 (12c7786)
- :recycle: (ui): 优化设置行布局计算逻辑 (3f0466d)
- :recycle: (ui): 重构图片下载逻辑，采用统一 HTTP 客户端 (f9402e4)
- :recycle: (plugin): 重构宿主初始化流程并增强异步任务日志与容错 (763ec0f)
- :recycle: (ui): 重构图片组件，统一封面渲染并修复嵌套刷新问题 (548ca2a)
- :recycle: (ui/source): 重构面板为分页模式，补充 EmmyLua 类型注解 (1e463a2)
- :recycle: (ui/library): 重构图书馆网格布局并引入异步分页与搜索 (0b71f15)
- :recycle: (ui): 重构书籍详情布局并修复关闭残影 (eb94255)
- :recycle: (book): 重构首页 UI 并改用异步分页加载 (f05068f)
- :recycle: (host): 重构桌面接管逻辑，改用显式状态机替代异步待定标记 (590dc18)
- :recycle: (book): 重构插件架构，拆分核心逻辑并清理遗留代码 (171135e)

#### 文档

- :memo: (docs): 重写月读系统设计文档 (d118f5f)
- :memo: (docs): 完善月读项目 README (69640b3)
- :memo: (docs): 全面重写 README，补充功能详解、安装指引与安全说明 (72a285c)
- :memo: (types): 补充 BookChapter 与 BookSource 的类型注解 (9a83bf6)
- :memo: (types): 为进度类型补充章节标题与页码字段 (52d53e5)
- :memo: (docs): 重写 Book 设计规范为 UI 实现规范 (f447029)
- :memo: 补充锁屏账单柱图设计说明 (f8b008b)
- :memo: (docs): add Book 设计风格与 UI 规范 (7f79c1e)
- :memo: (docs): 更新许可证为 GPLv3 并修订 README (2e66468)
- :memo: (cache): 更新缓存注释说明 (1f0b35e)
- :memo: (convert): 修正 html 模块注释 (be47f96)
- :memo: (l10n): 添加数据源选择相关翻译 (28801ad)
- :memo: (book-source): 完善 BookSource 类型注释与能力表定义 (a2b8dc4)
- :memo: (types): 添加 importBookAsync 字段类型注解 (ad016b4)
- :memo: 添加架构文档梳理插件整体流程 (817ed04)
- :memo: (ui): add layout diagrams as code comments (2078b76)
- :memo: (l10n): 添加“刷新”的英文和繁體中文翻譯 (54b85b5)
- :memo: (l10n): 更新本地化文本，新增书库配置翻译并移除旧文案 (23ef63f)
- :memo: (types): 更新 book.lua 字段注释与身份键说明 (b86fea3)
- :memo: (types): 补充 EmmyLua 类型注释并整合数据源定义 (9de96f6)
- :memo: (types): 细化书籍数据模型类型定义与契约注释 (46687f6)
- :memo: (webdav): 添加 WebDAV 客户端类型注解 (2572e30)
- :memo: (utils): 完善 Promise 与 Timing 模块的 Lua 类型注释 (cc6f5cb)
- :memo: (async): 翻译异步模块注释为中文并添加调试日志 (95876e7)
- :memo: (l10n): 更新微信读书与字体功能翻译 (cd363ac)
- :memo: (doc): 更新开发文档以反映新架构与依赖管理 (03d7102)
- :memo: (ui): 移除 home.lua 中过时的布局注释说明 (88f8941)
- :memo: (docs): 新增 Book 插件开发指南与架构文档 (99ea9e3)

#### 其他

- :wrench: (settings): 调整快捷面板配置并新增字典开关 (6ecd7ad)
- :wrench: (settings): 将默认锁屏方式改为 ko (06ebf36)
- :wrench: update files (15ec5d2)
- :wrench: (lockscreen): 为组件启用同步 (db28c04)
- :wrench: 适配 CMake 4 并自动修复陈旧的第三方源码 (88d96df)
- :wrench: (tests): 更新测试以匹配屏保语义与 Material 图标变更 (bfaa1fa)
- :wrench: (assets): 为拼音切片清单添加 SHA-256 校验字段 (d0dd0c8)
- :wrench: (tools): 移除词典分片的 gzip 压缩，输出原始 SQLite 分片 (bf16208)
- :wrench: (tools): 移除词典分片的 gzip 压缩，输出原始 SQLite 分片 (d918a8d)
- :wrench: (tools): 移除词典分片的 gzip 压缩，输出原始 SQLite 分片 (b07713e)
- :wrench: (build): 忽略本地代理指令文件 AGENTS.md (af9f3f0)
- :wrench: (http): 修复 Turbo/LuaSec 在 verify_ca=false 时的 CA 加载问题 (b302125)
- :wrench: (host): 添加图标组件依赖检查 (86ef146)
- :wrench: (utils): 改进子进程任务执行逻辑 (b0adc83)
- :wrench: (http): 将 WebDAV 和 HTTP 请求改为非阻塞异步模式 (ce7576a)
- :wrench: (gitignore): 更新忽略规则，排除环境变量与模拟器配置目录 (d2a700e)

#### 变更

- :white_check_mark: (tests): 保留 loader 基线并改用 Assert.skip (a5af601)
- :white_check_mark: (ci): 在 release 工作流中运行离线测试 (ff8dfca)
- :fire: (ui): 移除源设置中的立即同步入口 (b800b16)
- :white_check_mark: (tests): 补充锁屏组件与进度拉取测试 (b558215)
- :white_check_mark: (tests): 添加远程服务状态接口与书签模块测试 (07ed468)
- :adhesive_bandage: (stats): push 失败时不再阻断 pull 流程 (dcb3151)
- :white_check_mark: (tests): 补充微信笔记同步与锁屏行为测试 (4fa43c9)
- :fire: (ui): 移除字典快捷动作并调整锁屏刷新 (8e886f4)
- :fire: (ui): 移除字典快捷动作并调整锁屏刷新 (6028d83)
- :white_check_mark: (tests): 补充桌面唤醒与统计同步的测试覆盖 (961f0d6)
- :fire: (ui): 移除阅读器中锁屏后台刷新调用 (ebe7aa3)
- :white_check_mark: (tests): 补充百科查询、拼音候选栏和词库下载的回归测试 (f474b71)
- :white_check_mark: (tests): 新增 HTTP 与抓取模块回归测试 (3677cad)
- :globe_with_meridians: (l10n): 更新本地化字符串 (2b0b854)
- :white_check_mark: (lockscreen): 添加 library 组件源边界测试 (efdc483)
- :fire: (tools): 删除 check_annotations.lua 注释体检脚本 (14059c1)
- :white_check_mark: (lockscreen): 添加锁屏组件测试 (e35716c)
- :white_check_mark: (tests): 更新测试以匹配重构后的 API (25feccd)
- :bulb: (lockscreen): 更新九宫格位置设置的注释 (fcaae9d)
- :fire: (text): 移除 cleanChapterTitle 函数 (38ef39a)
- :fire: (db): 清理 XrayDB 冗余代码 (07c4b2d)
- :fire:(db): 移除数据库队列与目录缓存模块 (22a4cb0)
- :white_check_mark: (tests): 更新测试以适配 DB 模块重构与同步落库 (bf49dfa)
- :fire: (db): 移除冗余的 source_id/stable_id 校验 (ef72e09)
- :white_check_mark: (tests): 新增 base 事件、缓存队列与首页加载规格测试 (dee60f4)
- :white_check_mark: (tests): 补充边界条件与失败路径测试 (5f25f11)
- :lock: 加固远程服务鉴权并修复同步/统计问题 (f3b8c79)
- :fire: (reader): 移除底条进度中的页码显示 (a6e43cb)
- :white_check_mark: (tests): 更新测试以适配 chapter 源类型与阅读进度调整 (4934d1f)
- :truck: (xray): 将阅读页 AI 分析迁移至 xray 模块 (825b96e)
- :fire: (remote): 移除远程设置中的 RSS 订阅功能 (8d33889)
- :white_check_mark: (tests): 精简离线测试并对齐当前功能集 (9150610)
- :white_check_mark: (tests): 精简离线测试并对齐当前功能集 (93a4d78)
- :white_check_mark: (tests): 添加 copymanga 客户端与阅读器文件浏览器重定向的离线用例 (b11ece1)
- :white_check_mark: (tests): 更新测试适配新实现并修复隔离 (3198226)
- :fire: (ui): 删除快捷面板设置模块 (7ee1ebe)
- :fire: (ui): 删除快捷面板设置模块 (3d7d917)
- :globe_with_meridians: (l10n): 添加布局预设与翻页动画补丁的翻译 (8505a96)
- :white_check_mark: (tests): 在 topbar 测试中保存并恢复全局设置 (a3263ea)
- :white_check_mark: (tests): 调整面板测试并新增 copymanga 离线用例 (38d2c5f)
- :white_check_mark: (tests) 补充本地章节已存在时的快开路径测试 (a82acbe)
- :white_check_mark: (tests): 添加 AI 设置“测试连接”行的离线用例 (f6f0388)
- :adhesive_bandage: (ui): 修复语言设置中提示文本布局错位 (28f3b34)
- :white_check_mark: (tests): 更新远程服务的 CSS 断言 (4bed075)
- :white_check_mark: (tests): 更新锁屏与阅读布局测试以匹配新接口 (1cee5d2)
- :white_check_mark: (lockscreen): 添加组件测试并完善背景下载失败用例 (ef9a04e)
- :globe_with_meridians: (l10n): 补充“时均”翻译并兼容旧字段名 (635e954)
- :label: (types): 添加 KOReader UI 类型桩 (7605e03)
- :hammer: (tools): 新增词典构建脚本 (a6d3af2)
- :globe_with_meridians: (l10n): 补充英文与繁体中文翻译 (6713dcd)
- :white_check_mark: (tests): 更新测试覆盖同步 API 重构与书架/锁屏新行为 (101657d)
- :fire: (paths): 删除 splitBookWorkPath 函数 (097992c)
- :arrow_up: (ui): 更新图标字体为 Material Symbols 并重构加载逻辑 (b13536f)
- :fire: (stats): 移除阅读统计上报与采集模块 (a0986c9)
- :fire: (book): 移除书籍内容校验与下载合并模块 (4d0f83e)
- :fire: (book.koplugin): 移除按章阅读相关模块 (4bcdc5e)
- :fire: 移除调试日志插件 (f41dbf8)
- :white_check_mark: (tests): add lockscreen and pinyin test coverage (21785b2)
- :white_check_mark: (tests): 补充进度冲突、身份识别、目录缓存与属主源路由等测试 (bac014d)
- :white_check_mark: (server): 补全远程输入与剪贴板测试并新增键盘中文文案 (eafa1e5)
- :white_check_mark: (tests): add remote input API tests and fix config stub serialization (a770005)
- :globe_with_meridians: (l10n): add file manager service translations (9a5841a)
- :white_check_mark: (tests): 添加远程文件服务器离线测试 (7cc4803)
- :globe_with_meridians: (l10n): 添加英文与繁体中文翻译 (7799ea3)
- :globe_with_meridians: (l10n): 添加英文与繁体中文翻译 (68e33c6)
- :white_check_mark: (tests): 添加 partialMD5 模拟实现并更新注释 (a578ed9)
- :white_check_mark: (tests): 更新测试以匹配系列筛选与来源契约 (9f2f95a)
- :white_check_mark: (tests): 新增 popup 组件离线测试 (b9adcd9)
- :white_check_mark: (tests): 重写 zlib 客户端测试并补齐离线测试桩 (470f883)
- :globe_with_meridians: (l10n): 添加 Z-Library 相关文案的英文与繁体中文翻译 (4bf127a)
- :white_check_mark: (tests): 新增离线单元测试并加强隔离与断言计数 (5b4ddb0)
- :fire: (ui): 移除未使用的桌面尺寸获取函数 (ca40087)
- :white_check_mark: (tests): 更新测试以覆盖新的客户端查询与数据库行为 (62a1481)
- :globe_with_meridians: (l10n): 添加英文和繁体中文翻译 (df3ebc7)
- :fire: (utils): 移除 paths.lua 中的调试日志 (d81e609)
- :fire: (settings): 移除 reader_float_menu 设置 (27ea68e)
- : :fire: (font): 移除调试日志并更新调用方注释 (738e847)
- :white_check_mark: (test): 添加本地客户端、注册中心、统计同步及追踪的完整单元测试并扩展 reading_stats CRUD 测试 (eb17645)
- :coffin: 移除 host.lua 中的调试日志 (827f70a)
- :white_check_mark: (tests): 调整测试以匹配新的数据库与队列行为 (a7d464d)
- :adhesive_bandage: (convert): 修复html2epub中任务回调参数与资源释放 (2cf6252)
- :truck: (book.koplugin): 移动并重命名 html2epub 模块，新增 text2epub 模块 (17d063c)
- :fire: (db): 移除数据库相关代码 (69e10c9)
- :white_check_mark: (test): 重构测试环境接线并补充微信源离线用例 (f92b6e7)
- :fire: (moon): 移除异步调度与请求合并模块 (d12187d)
- :white_check_mark: (test): 添加离线单元测试框架与初始用例 (dcc2d45)
- :fire: (config): 移除 koreader 子模块并更新忽略配置 (b0e0550)
- :fire: (book-plugin): 移除 book.koplugin 插件模块 (c4c4a08)
- :arrow_up: (submodule): 添加 koreader 子模块配置 (45a4d28)

- （无提交记录）

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.0.2...v0.0.5

# v0.0.2

## Book v0.0.2

KOReader 插件包：`book.koplugin-v0.0.2.zip`

安装：解压后将 `book.koplugin` 复制到 KOReader 的 `plugins` 目录，然后重启。

### 更新内容

相对上一版本 `v0.0.1`：

#### 新功能

- :sparkles: (book): 优化书籍详情打开流程，支持缓存查询与网络拉取 (4ac30fc)
- :sparkles: (book): 新增阅读统计上报功能 (e35466a)
- :sparkles: (book): 新增阅读统计上报功能 (eb70c31)

#### 性能

- :zap: (api): 添加统计接口缓存并优化状态管理 (f0a68e3)

#### 文档

- :memo: 添加 MIT 许可证并更新 README (d601c55)
- :memo: 添加 MIT 许可证并更新 README (e10eaa0)
- :memo: (docs): 补充配套服务说明与项目截图 (d684e99)

### 完整对比

https://github.com/AnkioTomas/moon/compare/v0.0.1...v0.0.2
