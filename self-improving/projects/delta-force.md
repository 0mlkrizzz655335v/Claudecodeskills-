# 三角洲行动 (Delta Force) 优化记录

## 环境
- 路径: D:\Delta Force\ | 启动器: delta_force_launcher.exe
- CPU: i7-12700H | GPU: RTX 3060 | 反作弊: Tencent ACE

## 错误 1067104
- 错误码: 1067104
- 根因: Tencent ACE (AntiCheatExpert) 反作弊服务未运行 + Defender 未排除
- 修复时间: 2026-06-05

## 已修复

### Defender 排除
- 路径: D:\Delta Force, D:\Delta Force\launcher, %LOCALAPPDATA%\DeltaForce, %LOCALAPPDATA%\SGame
- 进程: delta_force_launcher.exe, DeltaForceClient.exe, DeltaForceClient-Win64-Shipping.exe, TASLogin.exe

### ACE 反作弊服务
- AntiCheatExpert Service -> Running (Automatic)
- AntiCheatExpert Protection -> Stopped (需重启加载内核驱动)

## 启动文件
- `启动三角洲_优化版.bat` — 6步优化启动（类似塔可夫启动器）

## 如果 1067104 复现
1. 以管理员身份运行启动脚本
2. 重启电脑（ACE Protection 驱动需要重启）
3. 检查 Defender 是否清除了排除项
4. 检查游戏文件完整性

## 系统级崩溃
- 2026-06-05: ntdll.dll 0xc0000005 影响所有游戏 → 已修复，见 [system-game-crash-fix.md](system-game-crash-fix.md)

---
创建: 2026-06-05
