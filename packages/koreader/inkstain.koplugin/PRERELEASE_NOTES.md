# v3.9.0beta1

**新增设置项**：custom_output_path（自定义保存目录）、wallpaper_save_only_custom（仅用自定义路径开关）
**新增方法**：customOutputFile()（返回自定义目录的壁纸文件名）、setCustomWallpaperPath()（目录选择器，复用 KOReader PathChooser）
**改造函数**：
writeWallpaper()（2086 行）—— 生成壁纸时额外写入自定义目录（同名覆盖、不清理你的目录，防误删）
isUsingInkStainScreensaver()（2127 行）—— 识别自定义路径
applyScreensaverSettings()（2161 行）—— 支持「仅自定义路径」模式，原生屏保也指向自定义文件
**菜单新增 3 项**：「自定义壁纸保存路径」「仅使用自定义路径（关闭原生屏保）」「显示输出路径」（4271–4299 行）

# v3.3.0_beta

根据觅阅4.9.0 beta27优化了觅阅阅读记录的抓取逻辑

# 20260804-beta

墨痕壁纸 v2.0.1 更新
 
重新设计标题排版，「墨痕」二字采用大小分层布局，配以英文「ink stain」副标
​
修复统计数据库表名错误，v2.0.0 中数据读取异常的问题已解决
​
觅阅数据源改为从 KOReader 统计数据库查询真实阅读记录，经 MiuRead 作者确认数据存储方式后修正
 
感谢 @miumiupy98-art 协助确认觅阅数据结构。
