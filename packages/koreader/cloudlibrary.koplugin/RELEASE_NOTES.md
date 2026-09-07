# v1.4.5

## What's Changed

- Integrate with Bookshelf: batch operations now auto-enter Bookshelf selection mode and retrieve selected books
- Fix garbled text when truncating Chinese folder paths in cloud book dialog navigation
- Improved Chinese translations

# v1.4.4

## 更新说明 

- 云端书籍列表添加目录切换按钮，可快捷切换云端书籍目录
- 优化上传/下载/删除进度对话框，显示书名和进度计数
- 无网络时自动提示开启 WiFi，连接后自动重试
- 优化云端书籍列表刷新逻辑，改善 K3/e-ink 设备体验 #12 #14 
- 为云端书籍列表增加循环翻页导航支持，改善 K3/e-ink 设备体验 #13 
- 检查更新时显示更新说明 #11 
- 完善中文翻译

感谢 @iav  对提升K3设备体验的贡献.

## What's Changed 

- Added quick folder navigation to cloud book dialog for switching cloud directories
- Optimized upload/download/delete progress dialogs with book name and progress counter display
- Add auto WiFi prompt and retry for network-dependent operations
- Optimize cloud book dialog refresh logic for better K3/e-ink experience #12 #14 
- Wrap page navigation for K3/e-ink devices #13 
- Display release notes when new version is found
- Improved Chinese translations #11 

Thanks to @iav  for contributions to improving the K3 device experience.

# v1.4.3

## What's Changed

- Added Auto Sync Exclude Directories feature #9  #10 
- Optimized gesture registration: merged reader/filemanager paired gestures into unified general gestures
- Remove logger.info

# v1.4.2

## What's Changed

- Fix: support all KOReader formats in book validation (including .fb2.zip)
- Non-touch navigation for the cloud book dialog

# v1.4.1

## What's Changed

- Added changelog.lua to track version history
- Optimize plugin module loading path and fix naming conflict with other plugins
