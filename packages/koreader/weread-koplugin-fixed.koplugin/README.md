# WeRead KOReader Plugin — 非官方增强版 Fork

> **版本 0.3.5**：修复自动阅读时长上报，合并上游 0.2.1 的书架筛选、下载容错、EPUB 打包和请求安全改进，并改善部分评论与划线错位。


[![Upstream](https://img.shields.io/badge/upstream-QiuYukang%2Fweread.koplugin-555)](https://github.com/QiuYukang/weread.koplugin)
[![Maintained fork](https://img.shields.io/badge/fork-miumiupy98--art%2Fweread.koplugin--fixed-555)](https://github.com/miumiupy98-art/weread.koplugin-fixed)

本项目是 [`QiuYukang/weread.koplugin`](https://github.com/QiuYukang/weread.koplugin) 的公开增强版 Fork，用于在 KOReader 中浏览、下载和阅读微信读书书籍及公众号文章。

本分支保留上游项目的基础微信读书访问、内容解析和 KOReader 集成能力，并继续维护扫码登录、账号凭据管理、划线与想法弹窗、原书脚注处理、OTA 更新及安全发布等增强功能。

> 本项目不是上游项目的官方版本。上游来源、提交历史及代码差异均通过 GitHub Fork 关系公开保留。

## 本 Fork 的主要增强

- **插件内微信扫码登录**：可直接在 KOReader 中显示二维码，并支持登录确认和四位验证码。
- **账号凭据持久化**：登录成功后保存 Cookie、API Key 和账号信息；`config.lua` 仅作为高级或备用配置方式。
- **双版本整书下载**：可分别生成干净 EPUB，或生成带微信读书划线和想法的 EPUB。
- **想法独立存储与弹窗显示**：想法数据保存在本地 JSON 中，不写入 EPUB 正文分页；点击划线后由插件弹窗显示。
- **划线显示控制**：阅读缓存书籍时可显示或隐藏已嵌入的划线标记。
- **原书脚注处理**：将部分图片注脚和跨文件脚注转换为更适合 KOReader 的 EPUB3 内联脚注。
- **手动 OTA 更新**：支持检查更新、下载更新包、SHA-256 校验、安装前备份和成功启动后的备份清理。
- **账号安全清理**：清除账号时同步删除持久化凭据、设置备份和本地 `config.lua` 凭据文件，已下载书籍不会被删除。
- **安全发布包**：完整包不包含用户 Cookie、API Key、Token、二维码状态、运行设置、缓存书籍或日志。
- **书架筛选与下载标记**：支持按阅读状态、下载状态筛选，并在书架中标记已缓存书籍。
- **分阶段下载与失败续跑**：章节、划线、想法和图片分阶段处理；单章失败不会中断整本书，想法批次支持重试。
- **请求凭据隔离**：跨域跳转时移除 Cookie、Authorization 和 Origin，外部图片请求不携带微信读书 Cookie。
- **标准 EPUB 打包**：使用 KOReader 自带归档器生成 EPUB，并压缩除 `mimetype` 外的内容。
- **评论位置校正**：当微信读书 range 与下载章节 HTML 不一致时，使用评论引用文字重新定位，同时保留原始 range 绑定评论弹窗。

## 功能概览

### 书籍

- 浏览微信读书书架并搜索书籍。
- 查看书籍信息和章节列表。
- 下载单章或整本书为 EPUB。
- 处理章节内容、CSS、封面和图片资源。
- 自动生成目录。
- 下载干净 EPUB，或下载带划线和想法的 EPUB。
- 阅读时显示或隐藏划线，点击划线查看想法。

### 公众号

- 浏览微信读书书架中的公众号。
- 获取公众号文章列表。
- 下载文章为适合 KOReader 阅读的 HTML。
- 可选择是否下载并内嵌文章图片。
- 文章列表和已下载文章保存在本地缓存中。

### 阅读时间上报

- 可选择是否向微信读书上报阅读时长。
- 上报任务只在 Reader 实际打开书籍时运行，返回文件管理器、关闭文档或设备休眠后立即停止。
- 从插件书架、KOReader 文件管理器或最近阅读打开已下载的微信读书 EPUB，均可自动识别书籍。
- 连续 10 分钟无翻页活动后暂停上报；再次翻页或恢复阅读时自动启动。
- 无网络时跳过当前请求，不主动打开 Wi-Fi，也不把网络错误误当作 Cookie 失效。
- 可查看当前状态、成功次数、失败次数、最近阅读活动和停止原因。

> 阅读进度双向同步和当前书籍详情仍处于开发状态，相关菜单目前禁用。

## 环境要求

- 已安装 KOReader 的 Kindle 或其他兼容设备。
- 建议使用较新的 KOReader 版本。过旧版本可能无法加载插件，表现为“工具”菜单中没有“微信读书”。
- 使用在线功能时需要设备联网。

## 安装完整包

1. 下载名称包含 `full-safe` 的完整安装包。
2. 解压后确认目录结构只有一层插件目录：

   ```text
   koreader/plugins/weread.koplugin/
   ├── _meta.lua
   ├── main.lua
   └── lib/
   ```

3. 将整个 `weread.koplugin` 文件夹复制到 KOReader 的 `plugins` 目录。
4. 完全退出并重新启动 KOReader。
5. 打开：

   ```text
   工具 → 微信读书
   ```

### 常见安装错误

错误结构：

```text
koreader/plugins/weread.koplugin/weread.koplugin/main.lua
```

正确结构：

```text
koreader/plugins/weread.koplugin/main.lua
```

## 首次登录

### 推荐：插件内扫码登录

1. 打开 `工具 → 微信读书 → 设置 → 账号管理 → 微信扫码登录`。
2. 使用微信扫描设备上的二维码。
3. 在手机端确认登录。
4. 如手机页面显示四位验证码，在 KOReader 中输入验证码。
5. 登录成功后，插件会保存账号 Cookie、官方 API Key 和账号信息。

可通过以下位置检查状态：

```text
工具 → 微信读书 → 设置 → 账号管理 → 账号状态
```

### 备用：手动导入 Cookie 或 cURL

扫码登录不可用时，可进入：

```text
工具 → 微信读书 → 设置 → 账号管理 → 手动导入 Cookie/cURL（备用）
```

支持粘贴：

- 浏览器中的原始 Cookie header；或
- 从 `https://weread.qq.com/web/book/read` 请求复制的完整 cURL。

### 高级方式：`config.lua`

普通用户不需要创建 `config.lua`。该文件仅用于：

- 手动配置或调试；
- 导入公众号所需的浏览器凭据；
- 配置缓存、阅读时间上报等高级选项；
- 扫码登录不可用时恢复账号配置。

使用方法：

```bash
cp config.example.lua config.lua
```

填写后，在 KOReader 中选择：

```text
工具 → 微信读书 → 设置 → 重新加载 config.lua
```

> `config.lua` 可能包含敏感凭据，不应提交到 GitHub、放入 Release 压缩包或发送给其他人。

## 下载书籍

打开书籍详情后，可选择：

### 下载完整书籍

生成文件名带 `full` 的干净 EPUB：

- 不请求微信读书划线和想法；
- 下载速度通常更快；
- 适合只阅读正文。

### 下载完整书籍（带划线和想法）

生成文件名带 `with-thoughts` 的 EPUB：

- 在正文中嵌入划线定位标记；
- 将想法数据独立保存到本地缓存；
- 点击划线时由插件弹窗显示想法；
- 想法内容不会作为普通正文进入分页。

打开已缓存的微信读书书籍时，还可使用：

```text
显示/隐藏划线和想法
重新下载当前书（带划线和想法）
```

如果当前打开的是干净 EPUB，切换“显示划线和想法”不会自动添加标注，需要重新下载带标注版本。

## 脚注处理

插件会尝试识别微信读书 EPUB 中的：

- 图片形式的注脚引用；
- 指向其他 `Text/*.xhtml` 文件的脚注链接；
- 可解析的脚注锚点和脚注正文。

识别成功后，将其转换为 EPUB3 内联脚注，以改善 KOReader 中的点击和显示体验。无法可靠识别的链接会保留原样，避免错误改写正文。

## 公众号文章

公众号文章列表可能需要浏览器请求中的 `x-wr-ticket` 或 `x-wrpa-0`。扫码登录后如果文章列表仍无法加载，可在插件提示框中粘贴：

- `x-wr-ticket` 的值；或
- 从 `/web/mp/articles` 请求复制的完整 cURL。

也可在 `config.lua` 中填写 `mp_curl`、`wr_ticket` 或 `wr_wrpa`，然后重新加载配置。

默认不下载公众号文章图片。启用图片下载可能显著增加下载时间和文件大小。

## OTA 更新

插件只在用户主动选择时检查更新：

```text
工具 → 微信读书 → 检查更新
```

更新流程包括：

1. 获取远程更新清单；
2. 比较版本号；
3. 下载 OTA 更新包；
4. 校验 SHA-256；
5. 在插件目录外创建备份；
6. 安装新文件并重启 KOReader；
7. 新版本成功启动后清理备份。

OTA 更新不会使用完整安装包，也不应覆盖用户运行设置。首次安装、插件损坏或跨越不兼容版本时，应使用 `full-safe` 完整包手动覆盖安装。

## 账号数据和隐私

账号凭据通常保存在 KOReader 的运行设置中，而不是发布包中。执行“清除账号数据”时会清除：

- 微信读书 Cookie；
- API Key；
- 账号名称及登录方式；
- 公众号验证凭据；
- 阅读上报请求参数；
- `weread.lua.old` 和 `weread.lua.new` 中可能残留的凭据；
- 插件目录中的 `config.lua` 及常见备份文件。

已下载书籍和文章缓存会保留。如需删除缓存，请使用“缓存管理”。

发布包必须排除：

```text
config.lua
config.lua.old
config.lua.new
config.lua.bak
settings/weread.lua
settings/weread.lua.old
settings/weread.lua.new
缓存书籍、文章、日志和 OTA 临时文件
```

## 菜单结构

```text
微信读书
├── 同步进度（阅读时显示，开发中）
├── 书籍详情（阅读时显示，开发中）
├── 显示/隐藏划线和想法（阅读微信读书缓存书籍时显示）
├── 重新下载当前书（带划线和想法）（阅读时显示）
├── 书架
├── 搜索
├── 阅读时间上报
│   ├── 启用阅读时间上报
│   ├── 连续 10 分钟无翻页后暂停
│   ├── 选择目标书籍
│   └── 上报状态
├── 设置
│   ├── 缓存管理
│   │   ├── 缓存清理
│   │   └── 缓存目录
│   ├── 重新加载 config.lua
│   ├── 立即续期 Cookie
│   ├── 进度管理（开发中）
│   ├── 下载内容
│   │   ├── 书籍图片
│   │   └── 公众号文章图片
│   ├── 书架排序
│   └── 账号管理
│       ├── 微信扫码登录
│       ├── 账号状态
│       ├── 手动导入 Cookie/cURL（备用）
│       └── 清除账号数据
├── 检查更新
└── 关于
```

## 文件结构

```text
weread.koplugin/
├── _meta.lua                  插件元数据
├── main.lua                   插件入口、菜单和主要业务流程
├── config.example.lua         高级配置模板，不包含真实凭据
├── README.md                  使用说明
├── NOTICE.md                  上游关系和项目声明
├── CHANGELOG.md               修改版更新记录
├── RELEASE-SAFETY.md          发布包安全检查说明
├── fonts/
│   └── NotoEmoji-Regular.ttf  想法弹窗 Emoji 字体
└── lib/
    ├── annotations.lua        划线标记生成和处理
    ├── client.lua             微信读书 HTTP/API 客户端与扫码登录
    ├── content.lua            内容解码、资源处理和 EPUB/HTML 生成
    ├── cookie.lua             Cookie 与 cURL 解析
    ├── crypto.lua             哈希与签名工具
    ├── download_dialog.lua    下载进度界面
    ├── footnotes.lua          原书脚注识别和转换
    ├── i18n.lua               界面翻译
    ├── settings.lua           KOReader 设置持久化
    ├── thought_popup.lua      想法弹窗
    ├── thoughts.lua           想法下载、缓存与划线注入
    ├── updater.lua            OTA 更新
    └── weread.lua             微信读书协议工具
```

## 故障排查

### 插件没有出现在菜单中

1. 检查目录是否为 `koreader/plugins/weread.koplugin/main.lua`。
2. 确认完整包没有多套一层目录。
3. 确认 `lib/weread.lua` 等依赖文件完整。
4. 确认 `fonts/NotoEmoji-Regular.ttf` 存在。
5. 升级 KOReader 后重试。
6. 查看 KOReader 的 `crash.log`，搜索 `weread.koplugin`、`module not found`、`unfinished string` 或 Lua 语法错误。

### 能打开插件，但书架无法加载

- 检查网络；
- 打开“账号状态”确认 Cookie 和 API Key 均已配置；
- 重新扫码登录；
- 或手动导入新的 Cookie/cURL。

### 公众号列表无法加载

- 公众号接口可能需要新的 `x-wr-ticket`；
- 根据插件提示粘贴该值或完整 `/web/mp/articles` cURL；
- 必要时更新 `config.lua` 并重新加载。

### 划线或想法没有显示

- 确认下载的是 `with-thoughts` 版本；
- 确认“显示/隐藏划线和想法”处于开启状态；
- 微信读书接口可能没有返回对应章节的想法数据；
- 重新下载当前书的带标注版本。

## 上游关系与贡献说明

本 Fork 基于上游项目继续开发。基础的微信读书访问、内容解析和 KOReader 插件结构来源于上游项目；本分支增加和维护的功能通过公开提交记录保留差异。

- 上游项目：<https://github.com/QiuYukang/weread.koplugin>
- 上游作者：<https://github.com/QiuYukang>
- 本增强分支：<https://github.com/miumiupy98-art/weread.koplugin-fixed>

借鉴或合并上游后续修复时，应保留可追踪的提交说明，不通过改名或打乱代码结构隐藏来源。

## 使用声明

本项目仅用于个人学习和技术研究，不代表微信读书或上游项目的官方立场。使用者应自行确认适用的授权条件，遵守微信读书用户协议及相关法律法规，并自行承担账号、数据和设备操作风险。
