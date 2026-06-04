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
- **新嫌疑**: AntiCheatExpert Service (内核级反作弊24x7运行) + ASUS Armoury Crate 6服务 + BattlEye

## 下一轮
1. 测试 nightreign 兼容模式
2. 停掉 AntiCheatExpert + ASUS 全家桶 → 测试
3. DDU 回退 NVIDIA 驱动
4. 最终方案：回退 Win11 23H2

## 关键教训
- HAGS 在此案例中不是根因（关了还崩）
- 修复后必须验证事件日志确认是否还有新崩溃
- 优化脚本可能包含与修复冲突的配置，必须审计
- DISM 在 ntdll 问题上不可靠，跳过
- **内核级反作弊服务可能是隐藏元凶**
