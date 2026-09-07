# v2.0.1-zh

## X-Ray（中文版）v2.0.1-zh

### 本次更新
- 完善"关于"页面：加入项目主页、原版致谢、MIT 许可证、免责声明
- 关于页底部自动显示版本号

### 安装
下载 `xray-zh.koplugin.zip`，解压得到 `xray-zh.koplugin/` 文件夹，拷贝到 KOReader 的 `plugins/` 目录，彻底重启 KOReader 即可。

### 主要特性
- 简体中文界面（默认），自动跟随 KOReader 界面语言
- DeepSeek V4 支持（deepseek-v4-flash / deepseek-v4-pro，思考模式可配）
- 分段获取：读取书籍正文逐段分析，覆盖超长书籍全部章节
- 本章人物：自动识别全名/昵称/简称等称呼变体
- 诊断日志（xray.log，菜单内可查看）
- 内置 Google Gemini / ChatGPT 支持

# v2.0.0-zh

## X-Ray（中文版）v2.0.0-zh

中文本地化 + DeepSeek 支持的分段获取插件。

### 安装
下载 `xray-zh.koplugin.zip`，解压得到 `xray-zh.koplugin/` 文件夹，拷贝到 KOReader 的 `plugins/` 目录，彻底重启 KOReader 即可。

### 主要特性
- 简体中文界面（默认），自动跟随 KOReader 界面语言
- DeepSeek V4 支持（deepseek-v4-flash / deepseek-v4-pro，思考模式可配）
- 分段获取：读取书籍正文逐段分析，覆盖超长书籍全部章节
- 本章人物：自动识别全名/昵称/简称等称呼变体
- 诊断日志（xray.log，菜单内可查看）
- 内置 Google Gemini / ChatGPT 支持

### 说明
- 首次使用请在 X-Ray → AI 设置 中填入 DeepSeek/Gemini API 密钥
- 打包内 config.lua 密钥为空，请自行配置
