# v0.9.9-migration

# v0.3.5

本项目基于原作 weread.koplugin v0.2.1 继续开发，在保留书架浏览、书籍下载、划线和想法等基础功能的同时，重点增强了登录方式、阅读时间同步、OTA 更新、下载稳定性以及不同书籍内容格式的兼容性。
v0.3.5：功能增强与时间同步修复
v0.3.5 主要解决插件的基础使用体验和阅读时间上传问题。
相对于原作 v0.2.1，主要新增和改进如下：
1. 扫码登录
•	增加微信读书二维码登录流程。
•	登录后自动保存 Cookie、API Key 和账号信息。
•	普通用户不再需要手动编辑 config.lua 或复制 Cookie。
•	账号信息保存于 KOReader 设置目录，删除插件代码不会自动删除账号数据。
2. 自动阅读时间上传
•	修复原有阅读时间上传失败的问题。
•	扫码登录后自动初始化微信读书网页阅读会话。
•	自动获取并生成阅读上报需要的参数，不再要求用户手动导入 /web/book/read cURL。
•	根据 KOReader 当前阅读位置估算微信读书阅读进度。
•	支持定时上报、休眠暂停、唤醒恢复和关闭书籍时停止上报。
•	服务器返回 succ=1 即视为成功，不再错误要求必须返回 synckey。
•	阅读会话失效时自动尝试刷新。
3. OTA 在线更新
•	增加插件内 OTA 更新功能。
•	支持正式通道和测试通道清单。
•	下载更新包后进行 SHA-256 校验。
•	更新前自动备份旧插件。
•	更新失败时可恢复旧版本。
•	支持远程 update.json 管理版本、下载地址、更新说明和删除列表。
4. 书架功能增强
整合原作 v0.2.1 中较成熟的书架功能，并增加兼容性修正：
•	按最近阅读时间排序。
•	按最早阅读时间排序。
•	按书名正序或倒序排列。
•	筛选已读、未读、已下载和未下载书籍。
•	已缓存书籍显示下载状态。
•	下载或清除缓存后自动刷新书架状态。
•	公众号文章书架支持相同的排序入口。
5. 整书下载稳定性
•	整书下载改为分阶段处理。
•	单个章节失败时跳过该章节，继续下载其他章节。
•	下载完成后显示成功章节数和失败章节数。
•	划线和想法采用分批下载。
•	单批请求失败时自动重试。
•	评论下载失败不会影响正文 EPUB 生成。
•	保留“干净版”和“带划线及想法版”两个下载入口。
6. EPUB 打包优化
•	使用 KOReader 自带的 ffi/archiver 生成 EPUB。
•	EPUB 的 mimetype 按规范保持不压缩。
•	其他资源使用 deflate 压缩。
•	减少手写 ZIP 造成的文件结构和兼容性问题。
•	生成的 EPUB 文件通常更小、更符合标准。
7. 划线和评论显示改进
•	微信读书评论不再直接写入 EPUB 正文。
•	评论内容保存为独立 JSON 数据。
•	点击带评论的划线正文时，在 KOReader 内显示独立弹窗。
•	评论内容不会进入正文阅读流，也不会改变书籍分页。
•	使用内部锚点代替自定义外部协议，避免 KOReader 弹出无效链接提示。
•	保留原始 range 作为评论查找键。
8. 评论和划线错位修复
•	不再完全依赖微信读书返回的 HTML 字符范围。
•	使用评论中的 abstract 或 contextAbstract 在章节可见文字中重新定位。
•	优先在原始 range 附近寻找匹配内容。
•	附近无法匹配时再进行全章搜索。
•	兼容 UTF-8、多字节字符、BOM、HTML 实体、换行和连续空格。
•	修复部分评论星号落在错误段落或错误文字上的问题。
•	修复 range 落入 HTML 标签或实体内部时导致的结构错误。
9. 脚注与想法分离
•	原书脚注继续由脚注模块处理。
•	微信读书用户评论使用独立弹窗显示。
•	避免原书脚注与微信读书评论互相覆盖或共同进入正文分页。
10. 网络和隐私安全
•	跨域跳转时自动移除 Cookie、Authorization 和 Origin。
•	避免账号凭据跟随封面、公众号图片或外部链接发送到第三方域名。
•	正式发布包不包含 config.lua、Cookie、API Key、日志和用户缓存。
•	OTA 更新不会主动覆盖用户账号设置。

# v0.3.2

## WeRead KOReader Plugin v0.3.2

微信读书 KOReader 插件的非官方增强版 Fork。

本次对 v0.3.2 的项目说明、上游声明和插件元数据进行了整理。版本号和 OTA 配置保持不变，未修改下载、解码、扫码登录或更新核心逻辑。

### 主要功能

- 插件内微信扫码登录
- 手动 Cookie/cURL 导入备用方式
- 微信读书书架浏览与搜索
- clean EPUB 下载
- 带划线和想法版本下载
- 点击划线弹出想法窗口
- 微信读书原书脚注处理
- 插件内 OTA 更新
- SHA-256 完整性校验
- 更新前备份及账号数据保护

### 本次说明更新

- 重写 README
- 明确与上游项目的关系
- 补充扫码登录、划线、想法、脚注和 OTA 使用说明
- 更新 NOTICE、CHANGELOG 和发布安全说明
- 更新 config.example.lua
- 更新插件描述和“关于”页面

### 安装包

`weread-koreader-plugin-mod-v0.3.2-full-safe.zip`

用于首次安装或手动覆盖安装。

解压后应得到：

```text
weread.koplugin/
├── main.lua
├── _meta.lua
├── fonts/
└── lib/

将整个 weread.koplugin 文件夹复制到：
koreader/plugins/

然后重启 KOReader

# v0.3.1

## WeRead KOReader Plugin Modified Version v0.3.1

### Changes

* Improved account-data cleanup.
* Added cleanup handling for KOReader settings backup files.
* Prevented cleared account information from being restored from local backup settings.
* Improved handling of local `config.lua` account data.
* Updated the QR-code login and account-management logic.
* Updated the OTA package and release manifest.

### Security and privacy

The release packages do not contain:

* WeRead account information
* Cookies
* API keys
* User IDs
* Login tokens
* Local KOReader settings
* `config.lua`
* Downloaded books or cache data

Existing account information stored on a user's own KOReader device is preserved during normal installation and OTA updates. It is removed only when the user explicitly selects the account-data clearing function.

### Installation

Download:

`weread-koreader-plugin-mod-v0.3.1-full-safe.zip`

Extract the included `weread.koplugin` directory to:

`koreader/plugins/`

Then restart KOReader.

### OTA update

Existing users can update through the plugin's manual update checker.

### Important

Download the attached full installation package. Do not use GitHub's automatically generated “Source code” archives as the KOReader installation package.

This is an unofficial modified version based on the original WeRead KOReader plugin. It is intended for personal learning and technical research.

# v0.2.5-test-versionfix
