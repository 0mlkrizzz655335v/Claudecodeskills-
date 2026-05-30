# LEARNED.md — Pro Workflow 学习日志

此文件由 learn-rule / wrap-up 自动维护，replay-learnings 通过 [LEARN] 标签搜索。
纠错索引入口：self-improving/corrections.md

## 活跃规则

[LEARN] Context: 装完插件≠生效，新工具安装后验证是否有产出文件
Mistake: 工具/插件安装后未验证是否真的产出文件
Correction: 安装后检查预期文件是否存在，手动触发首次运行

[LEARN] Configuration: 用户偏好优先用全局持久化而非每会话命令
Mistake: 每次新会话都要手动设置偏好
Correction: 查找全局配置文件，一次配置永久生效

[LEARN] Memory: 纠错系统不应分两处，统一入口减少维护成本
Mistake: 多个文件记录纠错，格式不统一，检索困难
Correction: 统一用 [LEARN] 格式存在 LEARNED.md，corrections.md 只做轻量索引

[LEARN] Memory: 文件格式决定工具能否检索
Mistake: 自定义格式导致 replay-learnings 的 grep 搜不到任何内容
Correction: 全部使用 [LEARN] Category: Rule 标准格式

[LEARN] Context: AI默认不记对话连续性，必须显式维护时间线
Mistake: 多层记忆系统都不记录"昨天聊了什么"
Correction: MEMORY.md 加"最近对话"段落，保留5条，超量自动归档
