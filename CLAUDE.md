# CLAUDE.md — Persistent Memory for Claude Code

## 跨工具共享记忆

@~/.openclaw/workspace/MEMORY.md

当你需要了解用户偏好、项目上下文、历史决策时，先读取上述文件。
如果该文件存在但内容为空，正常继续。

---

## 你是谁
- Windows 用户，中文为主 | Python/PowerShell | 目标：AI 长期记忆，不"失忆"

## 记忆系统
本文件 + `self-improving/` 目录 = 你的长期记忆系统。

### 文件结构
- `self-improving/memory.md` — 热记忆（偏好、模式、规则）→ **每次会话必读**
- `self-improving/corrections.md` — 纠错索引（详情见 `~/.claude/LEARNED.md`）
- `self-improving/heartbeat-state.md` — 心跳状态（自动维护）
- `self-improving/heartbeat-rules.md` — 心跳规则（检查间隔/阈值/告警）
- `self-improving/session-handoff/` — 跨会话交接文档（Pro Workflow 生成）
- `self-improving/projects/` — 各项目专属记忆
- `self-improving/domains/` — 领域知识
- `self-improving/archive/` — 归档的旧记忆
- `~/.claude/LEARNED.md` — Pro Workflow 学习日志（learn-rule / replay-learnings）
- `~/.openclaw/workspace/MEMORY.md` — 跨工具共享记忆（含"最近对话"时间线）
- `C:\Users\xnsrz\CLAUDE.md` — 入口（本文件）

### 会话流程
1. **会话开始时**：读取本文件 → 读取 `~/.openclaw/workspace/MEMORY.md`（含最近对话时间线）→ 读取 `self-improving/memory.md` → 读取 `self-improving/corrections.md`
2. **会话中**：如果用户纠正我的错误 → 自动追加到 `~/.claude/LEARNED.md`（`corrections.md` 只更新索引条目）
3. **会话中**：如果用户表达了偏好/规则 → 自动更新 `memory.md`
4. **会话结束时**：用户可以用 `/memory` 命令保存重要上下文；重要会话执行 wrap-up → 生成 session-handoff → 更新 MEMORY.md"最近对话"

## 工具
- MIMO Vision（图片/视频理解）| Python 脚本：gen_img / gen_vid / mimo / multimedia
- CloakBrowser（反检测浏览器，过 Cloudflare/reCAPTCHA）| `cloakbrowser_tool.py`
- stealth_browser（4层反反爬：L1 nodriver → L2 指纹轮换 → L3 rebrowser → L4 CloakBrowser）

## 插件
- Pro Workflow（记忆/学习/hooks）| Superpowers v5.1（TDD/调试/子代理/14 skills）| CodeGraph（代码知识图谱）
- Academic Research Skills v3.9（学术研究4件套：论文/审稿/管道/深度研究）
- Matt Pocock Skills（11万⭐, 24个真实工程师技能：TDD/诊断/原型/PRD/issue管理等）
- Claude Code 中文插件 v2.4.35（112文件，状态栏/提示简体中文）

## 环境
- Windows | PowerShell | `bypassPermissions`

## Context 工程（Pro Workflow: context-optimizer + compact-guard + context-engineering）
- **Write** — 重要状态写 NOTES.md / memory.md，而非依赖上下文窗口
- **Select** — Grep 定位 → offset+limit 定点读，永远不 dump 整个大文件
- **Compress** — 50% 即触发 `/compact`；compact 前保存 5 文件清单 + 当前任务+"下一步"
- **Isolate** — 重搜索/测试→subagent，主 session 保持干净
- **预算**: 规划<20% / 实现<50% / 测试<70% / 审查<85%
- **Auto-compact**: 建议 `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50`

## 规则
1. 优先使用中文回复
2. 修改文件前先确认，但简单操作可直行
3. 如果学到用户的偏好/习惯，主动记录到 `self-improving/memory.md`
4. 如果犯错被纠正，主动记录到 `~/.claude/LEARNED.md`（corrections.md 只做索引）
5. 每 5 次会话检查一次 `heartbeat-state.md`，看记忆系统是否健康
6. MEMORY.md"最近对话"保留最近 5 条，超量自动归档到 `self-improving/archive/conversation-timeline.md`
7. 重要会话结束：执行 wrap-up → 生成 session-handoff → 更新 MEMORY.md 速查+最近对话
8. 高效输出：不谄媚（无"Sure!/Great!"），不啰嗦（无"Let me know if..."），不复述问题，代码优先解释在后
9. 结构化优先：表格/列表 > 段落散文，ASCII字符 > Unicode装饰符
10. 记忆系统优化后 → 同步推送到 Git: `https://github.com/0mlkrizzz655335v/Claudecodeskills-`

> 自动发布: 每次对记忆系统/memory/skills 的改进，自动 commit + push 到上述仓库。

## 已学教训（详情见 ~/.claude/LEARNED.md）
[LEARN] Context: 装完插件≠生效，新工具安装后验证产出文件
[LEARN] Configuration: 用户偏好优先用全局持久化而非每会话命令
[LEARN] Memory: 纠错统一入口 LEARNED.md，corrections.md 仅做索引
[LEARN] Memory: 文件格式决定工具能否检索 — 必须用 [LEARN] 标签

---

## agentmemory 桥接区
<!-- 此区域由 agentmemory CLAUDE_MEMORY_BRIDGE 自动维护，勿手动编辑 -->
<!-- LINE_BUDGET=80，超出后 agentmemory 自动裁剪最旧内容 -->

<!-- AGENTMEMORY_BRIDGE_START -->

<!-- AGENTMEMORY_BRIDGE_END -->
