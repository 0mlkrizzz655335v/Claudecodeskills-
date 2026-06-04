# 逃离塔科夫 (EFT) 优化记录

## 环境
- CPU: i7-12700H | GPU: RTX 3060 6GB | RAM: 16GB
- 路径: F:\EFT\ | 启动器: F:\BsgLauncher\

## 优化文件清单

| 文件 | 用途 |
|---|---|
| `启动塔科夫_优化版.bat` | **主力启动器v2** — 7步自动优化后启动游戏 |
| `深度优化塔科夫.ps1` | 8步系统深度优化（需管理员） |
| `AdminOptimizeEFT.ps1` | 10项管理员级优化（服务/注册表/网络） |
| `Defender排除EFT.bat` | Windows Defender 排除 |
| `defender_fix.ps1` | Defender 排除 PowerShell 版 |

## 启动流程
1. 运行 `启动塔科夫_优化版.bat`（不需要管理员）
2. 自动: Turbo电源 → 清备用内存 → 启动BattlEye → 启动BSG Launcher
3. 在 Launcher 点 PLAY → 脚本检测到 EscapeFromTarkov.exe → 自动设 P核亲和+高优先级
4. 游戏运行中可关闭 cmd 窗口

## 关键优化项
- CPU: P核绑定(0xFFF) + High优先级，避开E核防卡顿
- 电源: 卓越性能/Turbo
- GPU: 硬件加速调度 + 全屏优化禁用
- 内存: 虚拟内存16-32GB固定
- 网络: TCP优化 + Nagle关闭 + NIC省电关闭
- Defender: 排除EFT路径和进程

## 推荐游戏内设置
- 分辨率: 1920x1080 | 全屏独占
- 纹理: 中 | 阴影: 低 | LOD: 2.5 | 可见度: 1000-1500
- DLSS: 质量模式 | Reflex: 开启+Boost
- SSR/HBAO/草地阴影/噪点/Z模糊/色差: 低或关闭

## 已知问题
- AdminOptimizeEFT.ps1 可能存在编码问题（变量名显示异常）
- 2026-06-05: 系统级 ntdll 崩溃影响所有游戏（含 BsgLauncher）→ 已修复，见 [system-game-crash-fix.md](system-game-crash-fix.md)

---
创建: 2026-06-05 | 基于 2026-06-04 实际文件操作
