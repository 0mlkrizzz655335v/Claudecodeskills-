# Session Handoff — 2026-06-04 · Hooks 修复

## 检测结论
所有 marketplace 插件的 plugin.json 都缺少 "hooks" 字段，导致 hooks.json 从未被加载。

## 修复清单

| 包 | 修复文件 | 修改内容 |
|---|---|---|
| agentmemory | .claude-plugin/plugin.json | 加 "hooks": ["./hooks/hooks.json"] |
| pro-workflow | .claude-plugin/plugin.json | 加 "hooks": ["./hooks/hooks.json"] |
| academic-research-skills | 根目录 | 删除 4 个重复 skill 目录 |
| mattpocock-skills | .claude-plugin/plugin.json | +11 个路径 (deprecated 4 个跳过) |

## 修复后全景

| 插件 | skills | hooks | agents |
|---|---|---|---|
| agentmemory | 8 | 12 events | — |
| pro-workflow | 34 | 24 events (含 quality-gate/read-before-write 等) | 8 |
| superpowers | 14 | — | — |
| academic-research | 4 | — | — |
| mattpocock | 29 | — | — |

## agentmemory hooks (12 events)
SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PreCompact, SubagentStart, SubagentStop, Notification, TaskCompleted, Stop, SessionEnd

## pro-workflow hooks (24 events)
ConfigChange, CwdChanged, FileChanged, Notification, PermissionDenied, PermissionRequest, PostCompact, PostToolUse, PostToolUseFailure, PreCompact, PreToolUse, SessionEnd, SessionStart, Setup, Stop, StopFailure, SubagentStart, SubagentStop, TaskCompleted, TaskCreated, TeammateIdle, UserPromptSubmit, WorktreeCreate, WorktreeRemove
> 注: pro-workflow 的 24 已覆盖 agentmemory 的 12，不是简单相加

## ~/.claude.json 手动 hooks (5 事件)
SessionStart→session-start.js | Stop→learn-capture.js+session-check.js | PreCompact→pre-compact.js | PostCompact→post-compact.js | SessionEnd→session-end.js

## 重启后验证 ✅ 2026-06-04
1. agentmemory SessionStart: "agentmemory: loading session context"
2. agentmemory UserPromptSubmit: "agentmemory: recalling relevant memories"
3. pro-workflow PreToolUse: Edit/Write 时触发 quality-gate
4. 89 skills 全部可用 (原 85 + mattpocock 4 遗漏)
5. 8 agents 可调用
6. 如 .mjs 脚本报错 → 需检查 node 版本对 ES module 的支持

## 验证时发现并修复 (2026-06-04)
1. **pro-workflow 重复安装** — `plugins/pro-workflow/` 缺失 hooks 声明 → 已补 `"hooks": ["./hooks/hooks.json"]`
2. **mattpocock 4 个 skill 遗漏** — design-an-interface, qa, request-refactor-plan, ubiquitous-language → 已添加声明 (25→29)
3. **academic-research 根目录空壳** — 学术4个目录无 SKILL.md → 已删除

## 二次验证修复 (2026-06-04 会话)
1. **P0: pro-workflow 双重加载** — `plugins/pro-workflow/` 和 `plugins/marketplaces/pro-workflow/` 各有独立 .claude-plugin，24 hook 事件可能触发 2-3 次 → 删除 marketplace 副本 + 更新 .claude.json hooks 路径
2. **路径纠正** — 实际 marketplaces 在 `plugins/marketplaces/` 而非 `~/.claude/marketplaces/`
3. **心跳更新** — heartbeat-state 从 5/31 更新到 6/4

## 最终全景 (二次验证通过)
| 包 | skills | hooks | agents |
|---|---|---|---|
| agentmemory (plugins/marketplaces) | 8 | 12 events | — |
| pro-workflow (plugins/) | 34 | 24 events | 8 |
| superpowers (plugins/marketplaces) | 14 | — | — |
| academic-research (plugins/marketplaces) | 4 | — | — |
| mattpocock (plugins/marketplaces) | 29 | — | — |
| **总计** | **89** | **24 events** | **8** |
