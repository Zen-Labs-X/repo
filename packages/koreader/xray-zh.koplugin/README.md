# X-Ray（中文版）— KOReader 插件

> 基于 [koreader-xray-plugin](https://github.com/0zd3m1r/koreader-xray-plugin)（v2.0.0，MIT）的中文本地化分支，为中文用户和中文书籍做了深度优化，并新增 **DeepSeek** 大模型支持。

像亚马逊 Kindle X-Ray 一样，用 AI 自动分析你正在读的书：**人物、本章人物、时间线、历史人物、地点、主题、内容简介、作者信息**，全程无剧透，数据缓存后离线可用。

- 🌐 **默认简体中文界面**，并自动跟随 KOReader 界面语言
- 🧠 **内置 DeepSeek 支持**（`deepseek-v4-flash` / `deepseek-v4-pro`，官方最新模型），对中文书籍分析效果出色
- 🆓 也支持 Google Gemini（免费额度）与 ChatGPT

---

## ✨ 功能特性

| 功能 | 说明 |
|---|---|
| 👥 人物 | 自动提取全书人物（长篇 30-50+ 个，分段获取可累积上百个），含角色、性别、职业、详细描述；支持模糊搜索与个人笔记 |
| 📖 本章人物 | 即时分析当前章节出现的人物及出现次数；自动识别全名/昵称/简称等称呼变体 |
| ⏱️ 时间线 | 关键事件按时间顺序排列，关联章节与人物 |
| 📜 历史人物 | 识别书中出现的真实历史人物，附传记、生卒年份与书内背景 |
| 📍 地点 | 重要地点及在故事中的意义 |
| 🎨 主题 & 📝 简介 | 主要主题列表、无剧透全书简介、作者传记 |
| 🔒 无剧透模式 | 按当前阅读进度生成数据，绝不提前剧透（首次获取数据时可选） |
| ✂️ 分段获取 | 超长书籍（几百上千章）按段读取正文分析，覆盖全书所有章节，完全基于原文 |
| 📋 诊断日志 | 每次请求/成功/失败自动记录到 `xray.log`（含错误原因、HTTP 状态码），菜单内可直接查看 |
| 💾 缓存系统 | 每本书独立缓存、永久有效、首次获取后完全离线可用 |
| 🌍 语言 | 简体中文（默认）/ 英语 |
| ⌨️ 快捷键 | `Alt + X` 快捷菜单 |

---

## 📸 截图

（发布前在此补充设备实拍截图，建议 2-4 张：主菜单、人物列表、时间线、AI 设置）

---

## 📦 安装

### 方式一：直接拷贝（推荐）

1. 下载本仓库，将 **`xray-zh.koplugin`** 文件夹整体拷贝到 KOReader 的插件目录：

   | 设备 | 插件目录 |
   |---|---|
   | Kindle | `koreader/plugins/` |
   | 其他设备（Kobo / Boox / 手机等） | `~/.config/koreader/plugins/`（即 KOReader 安装目录下的 `plugins/`） |

2. **完全退出并重启 KOReader**（不是返回主页，是彻底退出进程）。
3. 打开任意一本书，菜单 → **X-Ray** 即可使用。

> ⚠️ 若之前安装过原版 `xray` 或旧版本，请先删除旧插件文件夹，避免菜单重复。

### 方式二：OPDS / 其他

（如后续提供打包发布，可补充 OPDS 源地址）

---

## 🚀 快速开始

### 第 1 步：获取 API 密钥

| 提供商 | 地址 | 费用 | 建议 |
|---|---|---|---|
| **DeepSeek** ⭐ | https://platform.deepseek.com/api_keys | 极低（约 ¥1-3/百万 tokens 输入） | **中文书籍首选** |
| Google Gemini | https://makersuite.google.com/app/apikey | 有免费额度 | 免费 |
| ChatGPT | https://platform.openai.com/api-keys | 付费 | — |

> 密钥推荐在插件菜单里设置（会保存到 `settings/xray/*_api_key.txt`，不写入插件文件）；也可以直接编辑 `config.lua`。

### 第 2 步：设置密钥（二选一）

**在插件内设置（推荐）：**
```
菜单 → X-Ray → AI 设置 → DeepSeek API 密钥
```
输入 `sk-...` 开头的密钥即可，保存后自动切换为 DeepSeek。

**或编辑 `config.lua`：**
```lua
deepseek_api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
default_provider = "deepseek",
```

### 第 3 步：选择模型

```
菜单 → X-Ray → AI 设置 → 选择 DeepSeek 模型
```

| 模型 | 定位 | 特点 |
|---|---|---|
| `deepseek-v4-flash`（默认） | 快速、性价比高 | 响应快，日常分析足够 |
| `deepseek-v4-pro` | 旗舰 | 推理更强、分析更深入，稍慢 |

> **思考模式默认关闭**：KOReader 的 HTTPS 层强制 60 秒超时，而 DeepSeek V4 思考模式分析大本书通常超过 60 秒，会导致 `请求失败: wantread` 错误。关闭思考后响应只需几秒，对 X-Ray 结构化分析完全够用。
>
> 如需深度推理，可在 `config.lua` 中设置 `deepseek_thinking = true`（插件会自动临时调高超时以支持思考模式，但单次请求可能耗时 1 分钟以上）。

### 第 4 步：获取 AI 数据

```
菜单 → X-Ray → 获取 AI 数据
```

- 首次会询问剧透偏好：🔒 **无剧透模式**（只分析已读部分）或 📖 **完整模式**
- 等待 10-30 秒，之后数据**永久缓存**在本机，无需再次联网

#### 超长书籍：分段获取

普通"获取 AI 数据"只把**书名和作者**发给 AI（AI 基于自身知识分析，输出长度有限），对于几百上千章的长篇（如长篇网文），时间线可能只覆盖前几十章。

```
菜单 → X-Ray → 获取 AI 数据（分段·基于原文）
```

分段获取会**读取书籍正文**，切成若干段（默认每段 20 万字符，可在 `config.lua` 的 `settings.segment_size_chars` 调整），逐段发给 AI 分析，最后自动合并——**覆盖全书所有章节，且完全基于原文**（AI 不认识的书也能准确分析）。

- 优点：完整覆盖、准确（不依赖 AI 对这本书的了解）、人物称呼直接取自原文（"本章人物"匹配更好）
- 缺点：耗时较长（视书长度，数分钟到几十分钟）、消耗更多 token
- 仅支持可提取文本的格式（EPUB/TXT/FB2 等；PDF 扫描件无法提取）
- 过程中屏幕会显示"正在分析第 N/M 段…"，请保持联网、不要关闭 KOReader

---

## 🧭 菜单结构

```
X-Ray
├── 人物 (N)              ← 全部人物，可搜索
├── 本章人物              ← 当前章节出现的人物
├── 我的角色笔记          ← 给人物添加/编辑/删除笔记
├── 时间线 (N 个事件)
├── 历史人物 (N)
├── 地点 (N)
├── 作者信息
├── 内容简介
├── 主题 (N)
├── 获取 AI 数据
├── 获取 AI 数据（分段·基于原文）
├── AI 设置
│   ├── Google Gemini API 密钥
│   ├── 选择 Gemini 模型
│   ├── ChatGPT API 密钥
│   ├── DeepSeek API 密钥
│   ├── 选择 DeepSeek 模型
│   └── 选择 AI 提供商
├── 清除缓存
├── X-Ray 模式：已启用/已停用
├── 语言
├── 关于
└── 查看日志              ← 查看 xray.log 诊断日志（报错排查用）
```

快捷键：**`Alt + X`** 呼出快捷菜单；长按菜单项可查看完整菜单。

---

## 🌍 语言支持

插件**默认使用简体中文**，并做了智能语言切换：

- 首次使用且未手动设置过语言时，自动跟随 KOReader 界面语言（中文界面 → 中文，其他界面 → 中文默认）
- 手动切换：`菜单 → X-Ray → 语言`（中文 / English）
- 中文提示词会要求 AI **用简体中文输出分析结果**

---

## ⚙️ 配置说明

### 文件位置

| 内容 | 路径 |
|---|---|
| 插件本体 | `plugins/xray-zh.koplugin/` |
| 数据缓存 | `~/.config/koreader/cache/xray/` |
| 设置（密钥/模型/语言） | `~/.config/koreader/settings/xray/` |
| 诊断日志 | `~/.config/koreader/settings/xray/xray.log` |

### config.lua 可选配置

```lua
return {
    -- API 密钥（也可以不填，在插件菜单里设置）
    gemini_api_key = "",
    chatgpt_api_key = "",
    deepseek_api_key = "",

    -- 模型
    gemini_model = "gemini-2.5-flash",
    deepseek_model = "deepseek-v4-flash",   -- 或 "deepseek-v4-pro"

    -- DeepSeek API 地址（一般无需修改）
    deepseek_endpoint = "https://api.deepseek.com/chat/completions",

    -- DeepSeek 思考模式（默认关闭，响应快、稳定）
    -- 设为 true 开启深度推理（分析更深入，但单次请求可能超过 1 分钟；
    -- 插件会自动调高超时以支持思考模式）
    deepseek_thinking = false,

    -- 默认提供商: "gemini" / "chatgpt" / "deepseek"
    default_provider = "deepseek",

    settings = {
        auto_fetch_on_open = false,  -- 打开书时自动获取数据
        cache_duration_days = -1,    -- 缓存有效期（-1 = 永久）
        -- 分段获取时每段正文的字符数（默认 200000，可调到 300000 减少段数）
        segment_size_chars = 200000,
    }
}
```

---

## ❓ 常见问题

**Q：需要一直联网吗？**
A：不需要。只有**首次获取**某本书的数据时需要联网，之后全部离线。

**Q：会剧透吗？**
A：不会。获取数据时可选择"无剧透模式"，AI 只分析你已经读到的部分；即使是完整模式，AI 也被要求避免剧透关键情节。

**Q：缓存怎么清理？**
A：`菜单 → X-Ray → 清除缓存`，然后重新获取即可。

**Q：数据存在哪里？**
A：每本书的 AI 分析结果以 JSON 形式缓存在 `~/.config/koreader/cache/xray/`，不会上传到任何地方（除了一次性的 AI 请求本身）。

**Q：密钥安全吗？**
A：密钥保存在你设备本地的 `settings/xray/*_api_key.txt`，仅用于向对应 AI 服务发起请求，插件不会把密钥发给任何第三方。

**Q：AI 分析结果不准？**
A：试试 `deepseek-v4-pro` 或 Gemini Pro 模型；另外书名/作者信息完整的话效果更好（可在书籍信息中确认）。对超长书籍或冷门书，用"获取 AI 数据（分段·基于原文）"效果最好——它基于原文分析，不依赖 AI 对这本书的了解。

**Q：获取数据时报"请求失败: wantread"？**
A：这是 KOReader 的 HTTPS 层强制 60 秒超时导致的（DeepSeek 思考模式分析大本书超过 60 秒）。新版已默认关闭思考模式，响应只需几秒。若仍遇到，请检查网络，并打开 `菜单 → X-Ray → 查看日志` 查看 `xray.log` 中的具体原因。

**Q：本章人物提示"本章未找到人物"？**
A：通常是 AI 返回的人名（全名）与书中的称呼（昵称/简称）不一致。新版会自动拆分全名匹配（如"德米特里·费奥多罗维奇"会匹配"德米特里"），并让 AI 使用书中常用称呼。建议 `菜单 → X-Ray → 清除缓存` 后重新获取数据。

**Q：报错了怎么排查？**
A：插件会把每次请求的详细信息（书名、提供商、模型、端点、错误原因、HTTP 状态码）写入 `settings/xray/xray.log`，报错弹窗底部也有提示。打开 `菜单 → X-Ray → 查看日志` 即可查看；反馈问题时附上日志内容能快速定位。

---

## 🛠️ 与原版的关系

本项目是 [koreader-xray-plugin](https://github.com/0zd3m1r/koreader-xray-plugin)（v2.0.0，MIT 协议）的分支，在原版基础上：

- ✅ 新增完整简体中文界面翻译（`languages/zh.po`）
- ✅ 新增中文 AI 提示词（`prompts/zh.lua`），AI 分析结果以中文输出
- ✅ 新增 DeepSeek 提供商（官方最新 V4 模型，支持思考模式开关）
- ✅ 默认语言改为中文 + 自动跟随 KOReader 界面语言
- ✅ 修复原版对 LuaJIT 不兼容的语法（`goto`）
- ✅ 插件目录改为动态识别（文件夹可任意命名，如 `xray-zh.koplugin`）
- ✅ 界面错误消息本地化（消除原版残留的土耳其语硬编码）
- ✅ 新增"分段获取"：读取书籍正文分段分析，覆盖超长书籍全部章节
- ✅ 新增诊断日志（`xray.log` + 菜单内"查看日志"入口）
- ✅ 修复 KOReader HTTPS 层 60 秒超时导致的 `wantread` 错误
- ✅ 本章人物匹配改进：自动识别全名/昵称/简称等称呼变体

感谢原作者 [0zd3m1r](https://github.com/0zd3m1r) 的出色工作。

---

## 📄 许可证

MIT License — 与原版一致。详见 [LICENSE](LICENSE)。

---

## ⭐ 支持与反馈

- 遇到问题请提交 [Issue](https://github.com/你的用户名/xray-zh.koplugin/issues)
- 觉得好用欢迎 ⭐ Star

**免责声明**：本项目为个人学习交流用途，与 DeepSeek / Google / OpenAI 等公司无任何关联。使用 AI 服务产生的费用由用户自行承担。
