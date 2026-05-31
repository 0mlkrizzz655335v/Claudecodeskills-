# LEARNED.md — Pro Workflow 学习日志

此文件由 learn-rule / wrap-up 自动维护，replay-learnings 通过 `[LEARN]` 标签搜索。
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
