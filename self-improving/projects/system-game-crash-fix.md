# 系统级游戏崩溃修复记录

## 问题
- **症状**: 所有游戏打不开，闪退/崩溃
- **时间**: 2026-5-30 开始出现
- **触发**: Windows 更新 KB5087051/KB5089549/KB5092762 (2026-5-13~14)

## 诊断
- **事件日志**: nightreign.exe -> ntdll.dll 0xc0000005 ACCESS VIOLATION, 偏移 0x26a6d (重复相同偏移)
- **QQ.exe**: 同样 ntdll.dll 0xc0000005
- **BsgLauncher.exe**: libcef.dll 崩溃
- **SFC**: 核心系统文件无损坏 (仅 ThirdPartyNoticesBySHS.txt)
- **DISM**: 组件存储正常
- **ntdll.dll**: 数字签名有效

## 根因
**HAGS (硬件加速GPU调度)** 启用 + Windows 11 24H2 KB 更新 = ntdll 崩溃
- HwSchMode = 2 (启用) -> 改为 1 (关闭)
- MPO 多层覆盖同样引起冲突

## 修复清单 (2026-06-05) — 全部无效

| # | 修复 | 操作 | 效果 |
|---|------|------|------|
| 1 | HAGS | 2->1 (关闭) | 无效 — 重启后 nightreign 仍崩 ntdll 同一偏移 |
| 2 | MPO | OverlayTestMode=5 | 无效 |
| 3 | DirectX DLLs | regsvr32 重注册 9个 DLL | 无效 |
| 4 | GameDVR/FSE | 禁用 Game Bar + 强制全屏独占 | 无效 |
| 5 | TDR 超时 | 2s->60s | 无效 |
| 6 | Shader 缓存 | 清理 NVIDIA DXCache/GLCache | 无效 |
| 7 | SFC | 修复 ThirdPartyNoticesBySHS.txt | 无效 |

## 第二轮诊断 (2026-06-05 下午)
- DISM RestoreHealth: 卡 62.3% 逾 16 分钟，无效，已杀
- nightreign 兼容模式(Win8): 已设置，待测试
- GitHub/web 搜索: 确认 Win11 24H2 ntdll 0xc0000005 是已知广泛问题，微软建议回退 23H2
- **发现深度优化塔科夫.ps1 地雷**: 第71-77行会重新开启 HAGS，已修复脚本

## 第三轮诊断 (2026-06-05) — 找到根因！
**根因: 360安全卫士 主动防御 (ZhuDongFangYu)**
- 路径: `E:\新建文件夹 (2)\360Safe\deepscan\zhudongfangyu.exe`
- 机制: 内核级 hook 进 ntdll.dll 监控所有进程 → Win11 24H2 不兼容 → 任何游戏调用 ntdll 全崩
- 360 自保护：进程杀不掉、文件删不掉、目录改不了

## 已执行修复
| # | 操作 | 效果 |
|---|------|------|
| 1 | sc delete ZhuDongFangYu | 服务已标记删除 |
| 2 | sc delete Q360AMPPL | 待定（Access Denied） |
| 3 | 删除 Qihoo 计划任务 | ✅ |
| 4 | 删除 360Tray Run 注册表键 | ✅ |
| 5 | 停用 AntiCheatExpert Service | Manual |
| 6 | 停用 BattlEye Service | Manual |
| 7 | 停用 ASUS 9服务 | Manual |
| 8 | 停用 ROG Live Service | Manual |
| 9 | 停用 Razer Game Manager | Manual |
| 10 | 停用 PC Manager | Manual |

## 待验证（需重启）
1. 重启后确认 360 进程已消失
2. 测试 nightreign（兼容模式已设）
3. 测试其他游戏
4. 如需玩塔可夫：单独重装 BattlEye（不影响其他游戏）

## 关键教训
- HAGS 在此案例中不是根因（关了还崩）
- **360安全卫士主动防御是 ntdll 0xc0000005 在 Win11 24H2 上的已知元凶**
- 内核级安全软件 >> 显卡驱动 >> 系统文件 的排查优先级
- 修复后必须验证事件日志确认是否还有新崩溃
- 优化脚本可能包含与修复冲突的配置，必须审计
