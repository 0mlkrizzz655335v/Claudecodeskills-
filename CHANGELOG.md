# Changelog

## 2026-05-30 — v1.0 记忆系统发布

### 已安装插件
| 插件 | 版本 | Stars | 描述 |
|------|------|-------|------|
| Pro Workflow | 3.3.0 | — | 记忆/学习/hooks/上下文工程 |
| Superpowers | 5.1.0 | 213K | TDD/调试/子代理/计划/审查 |
| Matt Pocock Skills | — | 112K | 24个真实工程师技能 |
| Academic Research | 3.9.4 | 24K | 论文/审稿/深度研究 |
| agentmemory | 0.9.24 | — | MCP记忆服务器+向量搜索 |

### 已安装工具
| 工具 | 用途 |
|------|------|
| stealth_browser v2 | 6层反反爬 (nodriver/browserforge/rebrowser/CloakBrowser/curl-cffi/fake-ua) |
| CloakBrowser | C++级反检测浏览器 |
| CodeGraph | 代码知识图谱 |
| iii-engine | agentmemory运行时 |

### 核心特性
- 4层记忆: L1内置 → L2 hooks → L3 跨工具 → L4 agentmemory
- [LEARN]自动捕获 + replay-learnings检索
- 5事件hook自动化 (SessionStart/Stop/PreCompact/PostCompact/SessionEnd)
