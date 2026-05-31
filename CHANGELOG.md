
## 2026-05-31 · 记忆系统修复 + 152 Skills 全量盘点

### 修复
- **agentmemory daemon 修复**: worker 进程挂掉导致 MCP 退化到 standalone 模式，重启 daemon 恢复正常
- **自动启动**: 创建 Windows 计划任务 gentmemory-auto-start，开机自动启动，崩溃自动重试
- **openclaw.json**: 启用 browser-cdp, x-search, ai-call-agent, cold-email-salesblink 等共 15 个 skill

### 盘点
- **全系统扫描**: 确认 152 个 skills/plugins/tools/extensions 完整无损
  - Claude Code 插件: 67个
  - OpenClaw workspace skills: 83个
  - OpenClaw 内置 skills: 2个
  - Plugin-skills: 8个
  - 工具脚本: 2个 (stealth_browser.py 6层反反爬引擎)
  - 扩展: 2个
- **反反爬工具**: Python 6层 (curl_cffi, fake_useragent, nodriver, browserforge, rebrowser_playwright, cloakbrowser) + Node rebrowser-playwright 1.52.0

### 记忆灌入
- agentmemory 存入 12 条核心记忆: 身份/环境/能力/规则/4条LEARN教训/架构/技能清单
- 文件备份: SKILLS_INVENTORY.md, CLAUDE.md, LEARNED.md 同步更新

### 待配置
- overleaf-skills: 需浏览器获取 overleaf_session2 cookie
- paper-search-tools: 需 Docker 运行 mcp/paper-search# Changelog

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

