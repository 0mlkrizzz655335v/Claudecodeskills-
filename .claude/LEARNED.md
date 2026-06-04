# LEARNED.md — Pro Workflow 学习日志

[LEARN] Memory: 项目操作当日必须写入记忆，跨日会话不会自动回溯
Mistake: 6/4 做了大量塔可夫优化（5文件），6/5 完全遗忘，记忆系统零记录
Correction: 创建 self-improving/projects/tarkov.md，重要操作当日归档
纠错索引入口：`self-improving/corrections.md`

## 活跃规则

[LEARN] Context: 装完插件≠生效，新工具安装后验证是否有产出文件
Mistake: Pro Workflow 安装后从未产出 LEARNED.md，learn-rule/session-handoff/wrap-up 空转
Correction: 手动创建 LEARNED.md 并用 [LEARN] 格式，确保 replay-learnings 可搜索

[LEARN] Context: AI默认不记对话连续性，必须显式维护时间线
Mistake: 三层记忆（Auto Memory / Pro Workflow / CLAUDE.md）都不记录"昨天聊了什么"
Correction: MEMORY.md 加"最近对话"段落，保留5条，超量自动归档到 archive/conversation-timeline.md

[LEARN] Configuration: 用户偏好优先用全局持久化而非每会话命令
Mistake: 每次新会话都要手动 /thinking high
Correction: ~/.claude.json 加 "thinking": "high"，一劳永逸

[LEARN] Memory: 纠错系统不应分两处，统一入口减少维护成本
Mistake: corrections.md 和 LEARNED.md 职能重叠，格式不统一
Correction: corrections.md 改为轻量索引，实际内容全部用 [LEARN] 格式存 LEARNED.md

[LEARN] Memory: 记忆文件格式决定工具能否检索
Mistake: LEARNED.md 初始用自定义格式，replay-learnings 的 grep [LEARN] 搜不到任何内容
Correction: 全部改用 `[LEARN] Category: Rule` 格式，Mistake/Correction 紧跟其后

[LEARN] AuditTest: 终验闭环
Mistake: N/A
Correction: N/A

[LEARN] Verification: handoff 文档路径不可盲信，每次验证需实地探查文件系统
Mistake: session-handoff 写 `~/.claude/marketplaces/`，实际路径是 `~/.claude/plugins/marketplaces/`
Correction: 验证时从文件系统获取实际路径再比对，不假设 handoff 路径正确

[LEARN] Deploy: 插件去重必须是标准验证项
Mistake: pro-workflow 在 plugins/ 和 plugins/marketplaces/ 各一份，24 hook 事件可能触发 3 次（双重 plugin.json + .claude.json 手动 hooks）
Correction: 删除 marketplace 副本，统一用 plugins/pro-workflow/；更新 .claude.json hooks 路径

[LEARN] Gaming: HAGS + Win11 24H2 = ntdll 0xc0000005 游戏全崩
Mistake: 所有游戏崩溃后先怀疑系统文件损坏，跑 SFC/DISM 耗时无效
Correction: 事件查看器直接定位 ntdll.dll 同偏移 ACCESS VIOLATION → 关闭 HAGS(2→1) + MPO 一把修好
详情: self-improving/projects/system-game-crash-fix.md

[LEARN] Hooks: plugin.json 的 hooks 声明 ≠ .claude.json 自动加载 — 必须手动合并
Mistake: 上次修复只补了 plugin.json 的 hooks 字段，误以为 Claude Code 会自动发现并加载。实际仅 .claude.json 手动配置的 5 个 pro-workflow 事件生效 (6/40 executions)，evermem/superpowers/academic/mattpocock hooks 完全未加载
Correction: 将所有 plugin hooks.json 内容合并到 .claude.json（24事件/40执行），验证每个 hook 引用的脚本文件存在

[LEARN] Diagnosis: 修复后必须验证实际生效，不能假设成功就结束
Mistake: 7项游戏崩溃修复（HAGS/MPO/DirectX/GameDVR/TDR/Shader/SFC）应用后重启仍崩，但项目文件标记"修复完成"
Correction: 每项修复后检查事件日志确认是否还有新崩溃；修复无效时更新项目状态而非标记完成

[LEARN] Optimization: 优化脚本必须审计与系统修复的冲突
Mistake: 深度优化塔科夫.ps1 第71-77行会强行设置 HwSchMode=2（开启HAGS），与手动关闭的修复冲突。一旦跑了该脚本，修复全废
Correction: 修改脚本移除 HAGS 自动开启逻辑，改为提示已禁用。全盘搜索确认无残留 HwSchMode 引用

[LEARN] Tool: DISM RestoreHealth 在 Win11 24H2 不可靠，不应用于 ntdll 相关修复
Mistake: DISM 运行 16 分钟卡在 62.3%，CPU 0.03% 实际无进展，浪费诊断时间
Correction: SFC 扫一遍就够，ntdll 问题跳过 DISM 直接做其他修复

[LEARN] Search: GitHub API 搜索 ntdll 崩溃太泛，DuckDuckGo + 定点抓取更有效
Mistake: GitHub issue search 返回 9316 条结果，几乎全是无关的 Proton/模拟器 issue
Correction: 用 DuckDuckGo 搜具体错误信息 + 定向到 Reddit/Microsoft Answers/Steam 社区，更有针对性

[LEARN] Gaming: 内核级反作弊服务可能是 ntdll 崩溃元凶
Finding: AntiCheatExpert Service (24x7运行) + BattlEye + ASUS Armoury Crate 6个服务 — 这些内核级组件直接注入所有进程，Win11 24H2 升级后兼容性存疑
Status: 待验证（下一步停掉这些服务后测试）

[LEARN] Gaming: 360安全卫士主动防御 = ntdll 0xc0000005 真正元凶
Finding: 360Safe ZhuDongFangYu 内核级 hook ntdll.dll 监控所有进程，Win11 24H2 不兼容导致所有游戏崩溃
Fix: sc delete 服务 + 删计划任务 + 删Run键 + 停用其他内核服务（AntiCheatExpert/BattlEye/ASUS/Razer/ROG）
Note: 360自保护锁死进程/文件，需重启生效；原 E:\新建文件夹 (2)\360Safe\ 路径为可疑非标准安装

[LEARN] Proxy: UniClash 彻底移除的教训 — 官方 unins000.exe + AppData残留 + 注册表Tracing + 环境变量HTTP_PROXY + VeryKuai TAP Adapter + Flutter缓存，共6处需清理，不能只卸载不管残留
