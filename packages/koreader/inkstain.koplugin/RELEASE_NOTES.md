# v3.8.2

### 3.8.2 更新摘要

**新增**

墨痕阅读统计面板（全屏，阅读时长前 9 本，含品类/作者/进度/本期时长）
手势调出 + 右上角关闭键
设置项「品牌署名（墨痕）」自定义字样
设置菜单「加入内测」入口（QQ群:627525507 提示框）
resources/ 目录：透明 Logo + 导航栏方形 Logo

**修复**
透明 Logo 黑块（改用 ImageWidget alpha 绘制）
ZenOS 导航栏「添加操作」闪退（general=true + callback）
「加入内测」提示框闪退（改用原生 InfoMessage）

**改进**
导航栏换墨痕 Logo、统计文案中文化、加入内测提示框停留 10 秒

**其他**
main.lua 重构统计渲染；新增 stats_screen.lua；版本号升 3.8.2

# v3.8.1

**新增**：热力图改最近 26 周（对齐周一）、灰阶配色（5 级灰度，参考 Simple UI） 修复：标题不显示（原版 po 无 heatmap_title，返回空串；现加硬编码兜底）、版本号不一致（main.lua 的 PLUGIN_VERSION 是 误导 OTA 检查，已统一） 
**变更**：宽度与二维码对齐、去掉图例、月份标签上移、高度 11.5%→14%（仅热力图）

# v3.7.2

修复打包问题

# v3.7.1

### v3.7.1

移植 bookends 字体选择器：可视化选择壁纸字体，分页浏览 + 实时预览
​
修复变量名冲突导致菜单崩溃： local _, update  覆盖 gettext 函数  _ ，触发  attempt to call local '_' (a table value) 
​
改进书单补充逻辑：微信读书书单不足 top_n 时从觅阅进度表补充

修复"本周期暂无显示书单"：微信读书缓存不可用时缺少从觅阅进度表补充书单的兜底逻辑
​
新增统一兜底：所有数据源分支后，书单为空且进度表有数据就按进度排序补充
​
精简重复的补充代码块

# v3.6.4

感谢这位老哥提供的crash
<img width="250" height="100" alt="image" src="https://github.com/user-attachments/assets/8e3bb1a4-ab10-4b7e-9751-9743e653a13e" />


**OTA终于tmd修好了**
