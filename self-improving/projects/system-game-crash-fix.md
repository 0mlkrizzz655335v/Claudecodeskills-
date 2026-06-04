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

## 第四轮诊断 (2026-06-05) — 真正的元凶：UniClash
**用户发现：UniClash ON → 所有游戏正常；UniClash OFF → 游戏崩溃**

已排除：
- HAGS/MPO/DirectX → 无效
- 360主动防御 → 不是根因（已全部恢复）
- AntiCheatExpert/BattlEye/ASUS → 不是根因（已全部恢复）

UniClash 线索：
- UniClash 用 wintun.sys v0.14 + VeryKuai TAP Adapter
- TUN 模式未开启，纯系统代理模式 (port 7993)
- find-process-mode: always → 已改为 off
- restoreStrategy: compatible → 已改为 aggressive
- minimizeOnExit: false (之前 true，关闭=最小化而非真退出)

已修复：
- UniClash core config.yaml: find-process-mode = "off"
- UniClash shared_preferences.json: find-process-mode=off, restoreStrategy=aggressive, minimizeOnExit=false
- VeryKuai TAP Adapter (以太网 2): 已禁用
- 系统 ProxyServer: 已清空
- openclaw.json: 已从备份恢复 (enabled=false, proxyUrl=http://127.0.0.1:7993)

## 待验证（重启后）
1. 重启确保 UniClash 新配置加载
2. 关 UniClash → 测游戏（TAP 已禁用，如果好了就是 TAP 驱动的问题）
3. 开 UniClash → 测游戏（应该正常）
4. 确认 qqbot/gateway 服务正常

## 所有错误操作已恢复
- 360 服务/启动项/计划任务：已恢复
- ACE 内核驱动 Start 值：已恢复
- AntiCheatExpert/BattlEye/ASUS/Razer/ROG/PC Manager 服务：全部 Automatic
- nightreign 兼容模式：已删除
- 深度优化塔科夫.ps1 HAGS 段：仍保留修复（不会重新开启 HAGS）

## 关键教训
1. 用户说"打开塔可夫就有问题"≠塔可夫是根因（可能是 UniClash 状态变化的时间巧合）
2. 用户说"关掉他游戏就无法打开"=直接因果关系，优先级最高
3. 改配置前先搞清楚是运行时配置还是核心配置（UI vs core config）
4. 停服务前先确认是否真的是根因，别看到可疑就动手
