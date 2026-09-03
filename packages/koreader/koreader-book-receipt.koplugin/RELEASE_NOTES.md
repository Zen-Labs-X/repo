# v2.3

后缀修改

# 20260801

# 📖 Release Notes · v2.2

## 🎉 阅读收据屏保插件 · 中文增强版 (KOReader Patch)

<img width="127.9" height="177.5" alt="b66d2edb99edea36948853b7c031a8c2" src="https://github.com/user-attachments/assets/f51899c2-35a5-4e6a-82d0-63c6b035c32d" />
<img width="128.0" height="182.9" alt="6144ea3d628270c365572feb9077dece" src="https://github.com/user-attachments/assets/e54da7ba-400d-440e-8a85-d1af810afb1a" />



### 📌 版本概述

v2.2 在原有阅读收据的基础上，引入了**智能日期切换**和**随机高亮标注**两大核心功能，同时优化了视觉呈现与布局稳定性。票据风格的齿孔边框与右下阴影效果，让收据更具质感。


### ✨ 核心新特性

#### 🔀 智能标注/日期切换

屏保顶部区域会根据书籍中是否有标注（高亮/划线）自动切换显示内容：

| 场景 | 顶部显示 | 底部状态栏 |
|------|----------|-----------|
| **有标注** | 封面 + 随机高亮内容（带竖线装饰） | 电量 \| 日期 \| 时间 |
| **无标注** | 封面 + 大日期（年月 / 日 / 星期） | 电量 \| 时间（日期不重复） |
| **背景=书籍封面** | 仅封面（无日期/高亮，避免重叠） | 电量 \| 日期 \| 时间 |

**高亮标注特性：**
- 从当前书籍的标注中**随机抽取一条**显示，每次休眠或呼出都可能不同
- 标注内容自动截断，避免过长溢出
- 显示标注的**页码**和**章节**信息（如有）
- 左侧配有竖线装饰，视觉上更像独立书摘

**大日期特性：**
- 无标注时自动切换为日期展示，保持界面不空旷
- 日期格式为数字点分（如 `2026.07`），下方为超大日期数字
- 星期几以本地化语言显示


#### 🧾 票据风格边框（全新绘制方案）

采用 **`WidgetContainer:paintTo`** 底层绘制方式，彻底解决之前 `OverlapGroup` 导致的闪退问题：

- ✅ 上下边缘**半圆齿孔**（模拟撕票痕迹）
- ✅ 左右两侧**半圆票根缺口**
- ✅ 右下**轻微偏移阴影**
- ✅ **白色/透明**背景时自动启用齿孔边框
- ✅ **黑色/图片/封面**背景时自动切换为普通方框，适配更干净

此方案不依赖 KOReader 布局引擎，直接在像素层绘制，**稳定性大幅提升**。


#### 📦 完善的自定义选项

| 配置项 | 可选值 | 说明 |
|--------|--------|------|
| 背景 | 白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面 | 收据背景样式 |
| 背景图片放置 | 适应屏幕 / 拉伸 / 居中 | 仅对图片背景有效 |
| 内容模式 | 书籍收据 / 高亮+进度 / 随机 | 屏保显示内容 |
| 封面缩放 | 0 ~ 2.0（默认 1.0） | 封面大小，0 为隐藏 |
| 自定义休眠文字 | 任意文本 | 屏保时日期位置显示自定义文字 |


### 📈 其他改进

- **尺寸适度放大**：收据宽度约占屏幕 75%，字体（标题 28px、正文 20px、小字 16px）提升可读性
- **书名装饰**：书名左右添加横线（`—— 书名 ——`），采用衬线字体（NotoSerif）
- **布局优化**：封面左对齐，日期右对齐并自动适配封面高度
- **底部状态栏**：电量左对齐、日期居中、时间右对齐
- **进度条**：章节进度隐藏"章节"标题，仅保留章节名；书籍进度标题改为"书籍进度"
- **Emoji 兼容性**：统一替换为通用符号，避免字体兼容问题
- **菜单集成**：在 KOReader 屏保设置中直接选择"书籍收据"，并进入"书籍收据设置"自定义所有选项


### 📦 安装方法

1. 下载 `2-book-receipt-shortcut-and-lockscreen.lua` 文件
2. 将文件放入 KOReader 的 **`patches`** 目录：
   - Kobo/Kindle：`koreader/patches/`
   - Android：`/sdcard/koreader/patches/`
   - Linux：`~/.config/koreader/patches/`
   > 如果 `patches` 目录不存在，请手动创建
3. 重启 KOReader，在 **设置 → 屏保** 中选择"书籍收据"
4. 点击"书籍收据设置"调整背景、内容模式、封面缩放等选项


### 🗺️ 配置选项一览

| 配置项 | 可选值 | 说明 |
|--------|--------|------|
| 背景 | 白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面 | 收据背景样式 |
| 背景图片放置 | 适应屏幕 / 拉伸 / 居中 | 仅对图片背景有效 |
| 内容模式 | 书籍收据 / 高亮+进度 / 随机 | 屏保显示内容 |
| 封面缩放 | 0 ~ 2.0（默认 1.0） | 封面大小，0 为隐藏 |
| 自定义休眠文字 | 任意文本 | 屏保时日期位置的自定义文字 |


### 🛠️ 兼容性

- **最低 KOReader 版本**：2023.01+
- **设备支持**：Kobo / Kindle / Android / Linux 桌面
- **注意**：部分设备可能需要调整字体以支持特殊字符


### 🙏 致谢

- **原作者**：Reddit 用户 [u/hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/)
- **原始仓库**：[omer-faruq/koreader-user-patches](https://github.com/omer-faruq/koreader-user-patches)
- **票据边框参考**：Trae IDE 代码辅助生成
- **本版本修改与汉化**：[Nikola-Tesla45](https://github.com/Nikola-Tesla45)

感谢所有贡献者与测试者！


### 📄 许可证

GNU General Public License v3.0


**Happy Reading! 📖**

# 20260731

# 📖 Release Notes · v2.1.1

## 🎉 中文增强版 · 阅读收据屏保插件 (KOReader Patch)

---
<img width="204.7" height="285.9" alt="22264b8cc6f92270eb5214cca61f05d5" src="https://github.com/user-attachments/assets/d0b00d43-f40c-45a4-babe-7d96da3f2acd" />


### ✨ 新特性

- **全面中文本地化**  
  所有界面文字、菜单项、操作提示均已转换为中文，贴合中文用户习惯。

- **随机高亮显示**  
  当书籍中有标注时，屏保顶部会随机显示一条高亮内容，并配有优雅的竖线装饰。每次休眠都会刷新，让每张收据都独一无二。

- **书名装饰**  
  书名左右各有一条装饰横线（`—— 书名 ——`），使用衬线字体（NotoSerif），更具阅读质感。

- **布局优化**  
  - 封面位于左侧，右侧显示随机高亮内容
  - 书名独立成行，居中显示
  - "书籍进度"标题左对齐，与章节名风格统一
  - 章节进度条保留章节名，隐藏"章节"标题，界面更简洁

- **底部状态栏**  
  电量（⚡）左对齐、日期居中、时间（🕐）右对齐，一目了然。

- **屏保菜单集成**  
  在 KOReader → 设置 → 屏保 中可直接选择"书籍收据"，并进入"书籍收据设置"自定义背景、内容模式、封面缩放等参数。

---

### 📈 改进

- **尺寸全面放大**  
  收据宽度从 50% 提升至 **75%**，字体（标题 28px、正文 20px、小字 16px）增大，阅读更轻松。

- **边框回归简约**  
  采用无圆角细边框（`radius = 0, bordersize = 2`），风格清爽，与收据主题契合。

- **内容模式扩展**  
  支持"书籍收据（默认）""高亮 + 进度""随机"三种模式，屏保内容更丰富。

- **书籍进度标题重命名**  
  将原来的"书籍"改为"书籍进度"，更准确地反映其功能。

---

### 🛠️ 修复与兼容

- **Emoji 兼容性修复**  
  将易出错的 📚、📑 替换为 ◆、◇，后改为横线装饰，避免因字体不支持显示乱码。

- **书籍进度左对齐**  
  统一使用 `TextBoxWidget` 并设置 `alignment = "left"`，与章节名对齐方式一致。

- **移除不稳定的阴影尝试**  
  放弃 OverlapGroup 阴影方案，回归稳定的无圆角细边框，确保屏保稳定运行。

- **整合 kobo-style 高亮功能**  
  从 `2-kobo-style-sleepscreen-banner.lua` 移植高亮随机显示逻辑，并适配到当前布局。

---

### 📦 安装方法

1. 下载 `2-book-receipt-shortcut-and-lockscreen.lua` 文件。
2. 将文件放入 KOReader 的 **`patches`** 目录：
   - Kobo/Kindle：`koreader/patches/`
   - Android：`/sdcard/koreader/patches/`
   - Linux：`~/.config/koreader/patches/`
   > 如果 `patches` 目录不存在，请手动创建。
3. 重启 KOReader，在 **设置 → 屏保** 中选择"书籍收据"。
4. 点击"书籍收据设置"调整背景、内容模式、封面缩放等选项。

---

### 🗺️ 配置选项一览

| 配置项 | 可选值 | 说明 |
|--------|--------|------|
| 背景 | 白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面 | 收据背景样式 |
| 背景图片放置 | 适应屏幕 / 拉伸 / 居中 | 仅对图片背景有效 |
| 内容模式 | 书籍收据 / 高亮+进度 / 随机 | 屏保显示内容 |
| 封面缩放 | 0 ~ 2.0（默认 1.0） | 封面大小，0 为隐藏 |

---

### 🙏 致谢

- **原作者**：Reddit 用户 [u/hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/)  
- **原始仓库**：[omer-faruq/koreader-user-patches](https://github.com/omer-faruq/koreader-user-patches)  
- **kobo-style 高亮灵感**：Discord 用户 [@sandcastles] 及 Reddit 用户 [u/juancoquet]  
- **本版本修改与汉化**：[Nikola-Tesla45](https://github.com/Nikola-Tesla45)

感谢所有贡献者与测试者！

---

### 📄 许可证

GNU General Public License v3.0

---

**Happy Reading! 📖**

# 20260730

# 📖 Release Notes · v2.0

## 🎉 中文增强版 · 阅读收据屏保补丁 (Patch)

---

### ✨ 新特性

- **封面与日期布局优化**  
  封面移至左侧，日期（年月、日、星期）移至右侧，并自动放大至与封面等高，视觉更平衡。

- **日期格式改为数字点分**  
  年份与月份显示为 `2026.07` 格式，简洁清晰。

- **书籍/章节标题恢复菱形图标**  
  标题前添加 `◆`（书籍）和 `◇`（章节），提升辨识度。

- **封面背景时自动隐藏日期**  
  当背景设置为“书籍封面”时，顶部日期区域自动隐藏，避免信息重叠。

- **全面中文本地化**  
  所有界面文字、菜单项、提示信息均切换为中文，贴合中文用户习惯。

---


### 📦 安装方法

1. 下载本 Release 中的 `2-book-receipt-shortcut-and-lockscreen.lua` 文件。
2. 将文件放入 KOReader 的 **`patches`** 目录：
   - Kobo/Kindle：`koreader/patches/`
   - Android：`/sdcard/koreader/patches/`
   - Linux：`~/.config/koreader/patches/`
   > 如果 `patches` 目录不存在，请手动创建。
3. 重启 KOReader，在 **设置 → 屏保** 中选择“书籍收据”。
4. 点击“书籍收据设置”调整背景、内容模式、封面缩放等选项。

---

### 🗺️ 配置选项一览

| 配置项 | 可选值 | 说明 |
|--------|--------|------|
| 背景 | 白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面 | 收据背景样式 |
| 背景图片放置 | 适应屏幕 / 拉伸 / 居中 | 仅对图片背景有效 |
| 内容模式 | 书籍收据 / 高亮+进度 / 随机 | 屏保显示内容 |
| 封面缩放 | 0 ~ 2.0（默认 1.0） | 封面大小，0 为隐藏 |

---

### 🙏 致谢

- **原作者**：Reddit 用户 [u/hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/)  
- **原始仓库**：[omer-faruq/koreader-user-patches](https://github.com/omer-faruq/koreader-user-patches)

感谢所有贡献者与测试者！

---

### 📄 许可证

GNU General Public License v3.0

---

**Happy Reading! 📖**

# main

# 📖 书籍收据屏保插件 v2.0 · 中文增强版

> 在 KOReader 休眠时，展示一张精美的「阅读收据」—— 记录你的每一页阅读。

---

## 🎯 版本概览

本版本在原作者 [hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/) 的原创代码基础上，进行了全面汉化、界面优化和功能增强，专为中文 KOReader 用户打造。

---

## ✨ 新特性

### 🌐 全面汉化
- 所有界面文字、菜单项、按钮、提示信息均已本地化为中文
- 时间单位（小时/分钟）自然本地化
- 菜单中新增「书籍收据设置」完整中文配置界面

### 📏 尺寸优化
- 收据宽度从 50% 扩大至 **75%**，充分利用屏幕空间
- 字体全面增大：标题 28px / 正文 20px / 小字 16px
- 内外边距优化，内容舒展不拥挤

### 🧾 账单风格外框
- 边框从 2px 加粗至 **4px**，更有质感
- 边框颜色改为深灰色（`COLOR_GRAY_5`）
- 圆角从 15 减小至 **5**，硬朗的收据风格

### 🎨 图标装饰
- 书籍标题前添加 ◆ 符号
- 章节标题前添加 ◇ 符号
- 电池前保留 ⚡ 符号
- 时间前保留 🕐 符号

### 🖼️ 背景自定义
- 支持 **5 种背景**：白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面
- 背景图片支持 **3 种放置方式**：适应屏幕 / 拉伸 / 居中

### 📑 三种内容模式
- **书籍收据（默认）**：完整的书籍阅读信息
- **高亮 + 进度**：随机显示一条标注，同时保留进度
- **随机**：在以上两种模式中随机切换

### ⚙️ 屏保菜单集成
- 在 KOReader 设置 → 屏保中直接选择「书籍收据」
- 新增「书籍收据设置」子菜单，便捷配置所有选项
- 支持封面缩放调节（0~2.0，设为 0 隐藏封面）

---

## 🛠️ 修复与优化

### 稳定性提升
- 不再添加额外的标题栏或分隔线等复杂子元素，避免闪退
- 仅修改属性值和文本内容，保持布局结构稳定
- 屏保和快捷查看场景下均可靠运行

### 兼容性优化
- 将易出错的 Emoji（📚、📑）替换为通用符号（◆、◇）
- 避免因字体不支持导致显示方块或问号
- 适配 KOReader 最新版本（v2023.01+）

### 细节改进
- 底部状态栏保持电量和时间显示
- 保留原电池充电状态符号
- 优化内部间距，视觉更统一

---

## 📦 安装方法

### 手动安装
1. 下载 `2-book-receipt-shortcut-and-lockscreen.lua`
2. 将文件放入 KOReader 的 `patches/` 目录
3. 重启 KOReader


### 启用插件
1. 打开 KOReader 设置
2. 进入 **屏保** 设置
3. 选择「**书籍收据**」
4. 点击「**书籍收据设置**」自定义选项

---

## 🎮 使用方法

- **休眠屏保**：合上设备或手动休眠时自动显示
- **快捷查看**：在阅读页面通过手势/按键呼出收据（需配置）
- **自定义配置**：在屏保菜单中调整背景、内容模式、封面缩放等

---

## 🗺️ 配置选项一览

| 配置项 | 可选值 | 说明 |
|--------|--------|------|
| 背景 | 白色填充 / 透明 / 黑色填充 / 随机图片 / 书籍封面 | 收据背景样式 |
| 背景图片放置 | 适应屏幕 / 拉伸 / 居中 | 仅对图片背景生效 |
| 内容模式 | 书籍收据 / 高亮+进度 / 随机 | 收据显示内容 |
| 封面缩放 | 0 ~ 2.0（默认 1.0） | 封面大小，0 为隐藏 |

---

## 📝 更新日志

### v2.0（2026.07）
- 全面汉化所有界面文字
- 尺寸放大（宽度 75%，字体 28/20/16）
- 账单风格外框（4px 粗边框、深灰、圆角 5）
- 添加 ◆ 书籍 / ◇ 章节 图标装饰
- 新增屏保菜单选项
- 修复 Emoji 兼容性问题
- 优化布局稳定性
- 代码注释中文化

### v1.0（原始版本）
- 原作者：Reddit 用户 [hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/)
- 基础书籍收据显示
- 英文界面
- 无定制外观

---

## 🙏 致谢

- **原作者**：Reddit 用户 [u/hundredpercentcocoa](https://www.reddit.com/user/hundredpercentcocoa/)  
  感谢原创代码与创意！
- **原始仓库**：[omer-faruq/koreader-user-patches](https://github.com/omer-faruq/koreader-user-patches)  
  感谢提供可修改的基础版本！

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！  
如果你有好的建议或发现 Bug，请随时反馈。

### 后续计划
- [ ] 支持更多自定义样式
- [ ] 添加阅读周报/月报统计
- [ ] 支持导出收据图片
- [ ] 更多图标/主题选择

---

## 📄 许可证

MIT License

Copyright (c) 2026 [Nikola-Tesla45]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🔗 相关链接

- [KOReader 官方网站](https://koreader.rocks/)
- [KOReader GitHub 仓库](https://github.com/koreader/koreader)

---

**Happy Reading! 📖**
