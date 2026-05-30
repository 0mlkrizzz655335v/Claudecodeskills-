# CLAUDE.md — Persistent Memory for Claude Code

## 跨工具共享记忆

@{SHARED_MEMORY_PATH}/MEMORY.md

当你需要了解用户偏好、项目上下文、历史决策时，先读取上述文件。

---

## 你是谁
- {用户描述} | 目标：AI 长期记忆，不"失忆"

## 记忆系统
本文件 + self-improving/ 目录 = 你的长期记忆系统。

### 文件结构
- self-improving/memory.md — 热记忆（偏好、模式、规则）→ **每次会话必读**
- self-improving/corrections.md — 纠错索引（详情见 ~/.claude/LEARNED.md）
- self-improving/heartbeat-state.md — 心跳状态（自动维护）
- self-improving/session-handoff/ — 跨会话交接文档（Pro Workflow 生成）
- self-improving/projects/ — 各项目专属记忆
- self-improving/domains/ — 领域知识
- self-improving/archive/ — 归档的旧记忆
- ~/.claude/LEARNED.md — Pro Workflow 学习日志（learn-rule / replay-learnings）
- {SHARED_MEMORY_PATH}/MEMORY.md — 跨工具共享记忆（含"最近对话"时间线）
- CLAUDE.md — 入口（本文件）

### 会话流程
1. **会话开始时**：读取本文件 → 读取 {SHARED_MEMORY_PATH}/MEMORY.md（含最近对话时间线）→ 读取 self-improving/memory.md → 读取 self-improving/corrections.md
2. **会话中**：如果用户纠正我的错误 → 自动追加到 ~/.claude/LEARNED.md（corrections.md 只更新索引条目）
3. **会话中**：如果用户表达了偏好/规则 → 自动更新 memory.md
4. **会话结束时**：执行 wrap-up → 生成 session-handoff → 更新 MEMORY.md 速查+最近对话

## 环境
- {OS} | {Shell} | ypassPermissions

## Context 工程（需 Pro Workflow 插件）
- **Write** — 重要状态写 NOTES.md / memory.md，而非依赖上下文窗口
- **Select** — Grep 定位 → offset+limit 定点读，永不 dump 整个大文件
- **Compress** — 50% 即触发 /compact；compact 前保存 5 文件清单 + 当前任务
- **Isolate** — 重搜索/测试→subagent，主 session 保持干净
- **Auto-compact**: 建议 CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50

## 规则
1. 优先使用中文回复（可自定义）
2. 修改文件前先确认，但简单操作可直行
3. 如果学到用户的偏好/习惯，主动记录到 self-improving/memory.md
4. 如果犯错被纠正，主动记录到 ~/.claude/LEARNED.md（corrections.md 只做索引）
5. 每 5 次会话检查一次 heartbeat-state.md
6. MEMORY.md"最近对话"保留最近 5 条，超量自动归档
7. 重要会话结束：wrap-up → session-handoff → 更新 MEMORY.md
8. 高效输出：不谄媚，不啰嗦，不复述问题，代码优先解释在后
9. 结构化优先：表格/列表 > 段落散文

## 已学教训（详情见 ~/.claude/LEARNED.md）
[LEARN] Context: 装完插件≠生效，新工具安装后验证产出文件
[LEARN] Configuration: 用户偏好优先用全局持久化而非每会话命令
[LEARN] Memory: 纠错统一入口 LEARNED.md，corrections.md 仅做索引
[LEARN] Memory: 文件格式决定工具能否检索 — 必须用 [LEARN] 标签
