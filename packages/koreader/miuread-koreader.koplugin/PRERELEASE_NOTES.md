# v5.8.0-beta.16

- 修复 #102 主页与阅读页同时存活时可能互相用旧设置覆盖新设置的问题：ReaderUI 与 FileManager 在同一进程、同一设置文件和数据目录下复用同一份实时 Store，本地书库路径不会再被另一界面的旧快照清空。
- 本地书库选择、目录扫描结果、延迟保存与 reload 现在对主页和阅读页即时一致；无需重启才能看到另一界面刚确认的书库路径或扫描结果。
- 后台下载 worker 继续使用 `isolated=true` 的独立 Store，不与前台共享临时设置副本，保持 beta.15 的下载、断点与云端写入优先级设计不变。
- 保留 `Store:new()` 原有的目录自修复保证：即使已经复用共享 Store，`books / mp / covers / temp / updates / prefetch` 等运行目录缺失时仍会重新建立。
- 增加共享 Store 回归测试，覆盖路径保留、扫描即时可见、延迟保存、reload、独立 worker、写入失败恢复，以及“主页保存无关设置不能把已确认的新阅读进度回滚成旧 pending 状态”。
- Schema 保持 132，ReadReport 保持 v28；不修改 beta.15 的扩展下载线路、官方 Release 包校验、阅读数据同步优先级，也不调整 beta.13 的精确进度换算与 beta.14 的公众号入口。

# v5.8.0-beta.15

- 插件安装固定官方 Release 包；GitHub 中文社区默认首选下载，失败只换线路，不再改装 tag/main 源码包。
- 5 MiB 以上启用持久断点；20 秒建连、90 秒无数据才重连，取消低速误杀和总时长限制。
- 下载后按官方 size/SHA 校验；缺少 shell 工具时使用流式 SHA-256，安装失败可回滚。
- 阅读数据同步优先于后台下载。
- 新下载的大包只对前三条高价值线路做 128 KiB 有界探测，每条最多约 5 秒，成功线路按实测速率排序；未探测的代理仍保留为后备。已有 512 KiB 以上断点优先于测速；跨线路续传只允许同一个官方 asset，复制种子时保留原 partial；新线路不支持 Range 时只重启该线路，不破坏原断点。最近成功线路缓存 6 小时。
- 未固定安装包的已收录仓库可动态读取最新 GitHub Release 并筛选真正的插件 ZIP；两个同分官方 asset 不再猜测，由用户明确选择。只有 GitHub 已确认没有可识别 Release asset，而且 Contents API 又确认源码根目录或唯一 `.koplugin` 目录同时存在 `main.lua + _meta.lua` 时，才允许源码安装；API/网络失败绝不会被解释成“没有 Release”。
- Pinyin IME v1.2.0 继续固定官方 `pinyinime.koplugin-v1.2.0.zip`（63,312,207 bytes / SHA-256 `14047ed2638c32637c1dbc831f676967a221548f435443815b1c223881f4bbcb`），并保留解压后大体积安全上限与 220 MiB 剩余空间预检；FanQie、Z-Library、墨痕壁纸等已固定 Release 包继续按同一校验链安装，不写插件专属下载逻辑。
- 扩展任务继续持久化下载目录、官方 URL、版本、大小、SHA-256、已下载字节和阶段；返回主页、后台、网络短断、KOReader 重启都不会丢断点。用户“暂停/取消”保留 partial，“删除下载数据”才真正删除任务目录；真实休眠无法继续的设备保存断点，唤醒联网稳定后恢复。
- 关键云端写入开始前，书籍下载使用 `cloud_sync_priority`、扩展下载使用 `paused_priority` 临时让路；覆盖阅读结束精确进度、手动进度和批注删除/同步等事务。最多等待约 3 秒确认后台传输停下，云端写入不会被下载无限阻塞，写入结束后只恢复本次由同步暂停的任务。
- Schema 保持 132，ReadReport 保持 v28；不修改 beta.13 的 standalone/partial 精确 `chapter + co` 与整书进度换算，不重新设计 OTA，不改变公众号书架/文章返回方案，主页快捷工具栏继续只有“刷新 / 搜索 / 下载 / 同步 / 休眠 / 设置”六个推荐项。

# v5.8.0-beta.10

- 扩展中心升级为 Package Manager v3：推荐插件支持确定性 Package Catalog，安装包 URL、版本、大小、SHA-256 与目标目录可直接由目录声明；Pinyin IME、番茄小说、Z-Library 和墨痕壁纸已使用固定 Release 包，正常安装不再先扫描源码或连续猜候选。
- GitHub 社区继续保持开放发现；当同一仓库存在多个可安装候选时改为由用户明确选择，不再在后台静默连续尝试 Release/Tag/Branch 源码包。
- 插件正常下载恢复 5.8 beta.4 的可靠 fast path：优先使用 KOReader 自身流式 HTTP 下载；只有中断/异常后才进入 curl 断点恢复层。自动模式最多尝试 3 条有价值线路，手动选择 GitHub/镜像时严格使用所选线路。
- 新增持久化 ExtensionTask：每个插件任务拥有独立 `miuread/extensions/tasks/<task-id>/` 工作目录、task/owner/progress/result 状态；同一时刻只允许一个插件传输 owner，启动时会收口旧会话遗留 transport，并保留可恢复下载数据。
- 断点续传重新实现：Range 被拒绝、镜像不支持续传或 ZIP 尚未完整时均不会直接删除 canonical partial；需要从 0 重试时使用独立 scratch 文件，只有完整下载成功后才晋升为 package.zip。
- 插件下载正式接入下载中心，增加“全部 / 书籍 / 插件”筛选；插件使用与图书一致的 ProgressWidget 显示真实字节百分比、已下载/总大小、平滑速度、ETA、下载源以及等待网络/校验/解压/安装阶段。
- 取消插件下载默认保留断点；支持暂停、继续、取消并保留、删除下载数据。KOReader 重启后的 interrupted/downloaded 任务可以从下载中心重新进入完整 Package Pipeline，继续完成下载、校验和安装。
- 插件传输接入 Kindle ScreenSaver Hold：真实插件下载会注册 `extension_download` 后台任务；无法保持后台时进入 `paused_power` 并保存断点。唤醒后不会立刻联网，而是在 Wi-Fi 恢复并稳定后再继续。
- DNS/无网络错误改为 `WAIT_NETWORK`，不再把整机离线误判成单个 GitHub/镜像故障并连续轰炸多个代理；自动线路健康记录增加真实平均速度、TTFB 与 Range 支持，用实际历史传输表现排序，不做额外测速赛马。
- 下载完成后增加 expected size、SHA-256、ZIP 文件头与中心目录校验，再进入现有安全安装链；继续保留路径穿越/符号链接/体积/架构检查、staging、旧插件备份、安装后完整性验证与失败回滚。
- 安装/替换阶段增加独立 `extension_install` 短时 finish lease；KOReader 退出/重启会先 quiesce 插件 transport，避免只结束父 worker 而留下 curl 子进程。
- Schema 升至 129。旧 v2 `miuread/temp` 下载残留不会被 v3 自动认领，避免污染新的任务状态；保留用户下载源选择与自定义镜像，但重置旧的成功/失败线路分数，改由 v3 重新学习真实速度。
- 本版不改图书 DownloadTask、章节抓取/EPUB 生成、Reader 生命周期、同步/批注协议或 OTA 安装核心。

# v5.8.0-beta.9

- 下滑控制中心恢复紧凑单行布局：候选功能池继续完整保留，但实际最多显示 8 个已选择且当前设备支持的快捷项；3/5/7/8 项都会按可用宽度精确等分铺满，不再出现 6+1 的孤立第二行。
- 控制中心自定义上限改为 8 项；旧版已经保存的 >8 项配置不会在升级时被静默删除，运行时只显示按用户顺序筛选后的前 8 项，并在自定义页提示需要收口的数量。设备不支持的项目动态隐藏且不占槽位。
- 快捷按钮压缩垂直留白并放大 SVG；只有至少一个可见项目确实有短状态时整行才保留状态行。Wi-Fi、同步和方向状态改为“已连接 / 无网络 / 同步中 / 已锁定”等短文本，不再在快捷格中显示 SSID 或长说明。
- QuickPanel 文案收口为“返回 / KO设置 / 文件 / 退出 / 重启”等短标签；修复 KOReader 设置请求不存在的 `koreader-settings.svg` 后退化成圆点的问题，并补齐 `koreader-settings → settings`、`reboot → restart`、`poweroff → power-off` SVG 映射。缺失图标统一记录日志并回退 `more.svg`，不再显示莫名其妙的 `•`。
- 保留 QuickPanel 的缓存优先与异步状态策略：打开面板不新增网络检查、磁盘扫描或轮询定时器；下载快捷项不再为了显示 detail 在前台调用下载队列摘要。前光/色温控制、右上角“自定义”、电池与收起入口保持原功能。
- 觅阅自身更新入口重新收拢到“设置 → 更新与关于”：更新通道下面直接显示当前通道对应的“检查正式/内测通道更新”；“工具 → 系统维护”移除重复检查更新入口，避免通道选择与执行更新分散在两个位置。第三方插件更新仍留在“工具 → 插件与扩展”。
- Schema 保持 128；不修改下载器、同步协议、Reader 生命周期、后台 Scheduler、批注同步、统一书架、OTA 安装核心和设备电源逻辑。

# v5.8.0-beta.8

- 修复 Beta Release 被插件目录内开发文档阻断的问题：`PERFORMANCE_IMPLEMENTATION.md` 移至仓库根目录，不再进入 `miuread.koplugin` 发布包；发布校验同时会直接打印具体违规文件名，便于后续定位。
- “觅阅推荐”新增「墨痕壁纸」（miumiupy98-art/inkstain.koplugin），同时进入“精选推荐”和“阅读增强”分类；支持按 KOReader 阅读统计或觅阅书架数据生成墨痕账单风格休眠壁纸。
- 墨痕按标准扩展安装流程处理，不新增专属安装器；推荐卡片补充“阅读统计与休眠壁纸”说明，并保留当前仅 KPW4 完成真机测试的设备提示。
- 修正 beta.6 / beta.7 在 CHANGELOG 中误用一级标题的问题，确保 Release beta workflow 能正确识别版本段落。
