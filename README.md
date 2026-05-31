# Claude Code 工程环境

> 4层记忆 + 6层反反爬 + 5个插件 + 自动化 — 开箱即用

---

## 插件 (5个)

| 插件 | Stars | 核心 |
|------|-------|------|
| Pro Workflow 3.3 | — | 记忆/学习/hooks/上下文工程 |
| Superpowers 5.1 | 213K | TDD/调试/子代理/14 skills |
| Matt Pocock Skills | 112K | 24个工程师技能 |
| Academic Research 3.9 | 24K | 论文/审稿/深度研究 |
| agentmemory 0.9 | — | MCP+BM25+向量搜索 |

## 工具

| 工具 | 用途 |
|------|------|
| stealth_browser v2 | 6层反反爬 (nodriver→browserforge→rebrowser→CloakBrowser→curl-cffi→fake-ua) |
| CodeGraph | 代码知识图谱 |
| CloakBrowser | C++级反检测浏览器 |

## 四层记忆

`
L1 内置     Auto Memory                        自动
L2 hooks    Pro Workflow (5事件/6脚本)          [LEARN]自动捕获
L3 共享     MEMORY.md                          跨工具时间线+速查
L4 智能     agentmemory (1862条观测)            BM25+向量+图谱+MCP
`

## 自动化

| Hook | 何时 | 做什么 |
|------|------|--------|
| SessionStart | 启动 | 加载[LEARN] + 上次会话摘要 |
| Stop | 每次回复 | learn-capture自动扫描[LEARN] |
| PreCompact | compact前 | 保存上下文 |
| PostCompact | compact后 | 恢复上下文 |
| SessionEnd | 结束 | 提示记录学习 |

## 目录树

`
├── CLAUDE.md           # 入口+规则+插件注册+agentmemory桥接
├── MEMORY.md           # 速查+最近对话
├── NOTES.md            # 工作状态暂存
├── CHANGELOG.md        # 更新日志
├── tools/              # stealth_browser.py v2
├── .claude/            # LEARNED.md/rules/settings模板
├── self-improving/     # memory/corrections/heartbeat/session-handoff/archive
├── patch/              # learn-capture.js 补丁
├── openclaw/           # OpenClaw工具集成
└── docs/               # 文档
`

## 维护规则

1. 学到偏好→memory.md | 被纠正→LEARNED.md[LEARN]
2. 最近对话保留5条,超量→archive
3. 记忆系统改进 → 自动 git push
4. 每5会话检查 heartbeat-state

---

[CHANGELOG](./CHANGELOG.md)
