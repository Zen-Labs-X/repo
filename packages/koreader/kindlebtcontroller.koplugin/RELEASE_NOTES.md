# v0.1.6

Auto release version v0.1.6

# v0.1.5

Auto release version v0.1.5

# v0.1.4

# Features
- Added instructions for the Bluetooth pairing process

# Fixes
- Fixed an issue where the unmapped device code popup could cause the touchscreen to freeze

---

# 新特性
- 新增蓝牙配对步骤说明

# 缺陷修复
- 修复未映射设备码弹框导致触摸屏卡死问题

# v0.1.3

# Features
Key Config and Action Selection dialogs now support paginated display, single-select and multi-select mode switching

# Fixes
- Fixed unmapped system key code 100xx notification issue

---

# 新特性
- 按键配置 和 动作选择 界面支持分页显示、支持切换多选和单选模式

# 缺陷修复
- 修复系统按键码100xx未映射问题

# v0.1.2

# Fixes
- Fixed the issue where incorrect key codes 10001 and 10002 were generated when unlocking the screen. Now, key events are correctly passed without invalid key codes causing interference.

- Added early validation for the `device_path` configuration. This prevents Koreader from freezing due to incorrect system device configurations.

---

# 缺陷修复
- 修复了解锁屏幕时错误输出按键码 10001 和 10002 的问题。现在按键事件将正确传递，避免了无效的按键代码干扰。
- 增强了 `device_path` 配置的提前校验功能。过滤系统设备，避免了由于误配置而导致的 Koreader 弹框卡死问题。
