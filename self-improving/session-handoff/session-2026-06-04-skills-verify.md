# Session Handoff — 2026-06-04 · Skills 验证与修复

## 做了什么
验证 Superpowers / Matt Pocock / Academic Research 三个 skills 包是否生效。

## 发现与修复
| 插件 | 根因 | 修复 |
|------|------|------|
| Superpowers | plugin.json 缺少 "skills" 字段 | 添加 "skills": ["./skills/"] |
| Academic Research | 同上 | 同上 |
| Matt Pocock | 已声明 17 条 skills 路径 | 无需改动 |

## 验证
- 43 个 SKILL.md 全部格式正确，零失败
- **运行时验证需要新会话** — skills 在启动时编译进 system prompt

## 修改的文件
- ~/.claude/plugins/marketplaces/superpowers/.claude-plugin/plugin.json — 加 skills 字段
- ~/.claude/plugins/marketplaces/academic-research-skills/.claude-plugin/plugin.json — 加 skills 字段

## 新会话要做
1. 启动 Claude Code
2. 验证 Superpowers 14 skills（TDD、系统调试、子代理开发等）
3. 验证 Academic Research 4 skills（论文写作、审稿、管道、深度研究）
4. 验证 Matt Pocock 14+ skills（diagnose、triage、prototype、to-prd 等）
5. 如未生效，检查是否需要注册到 known_marketplaces.json

## 其他已确认生效
- Pro Workflow hooks 全链路 ✅
- CodeGraph MCP ✅
- MIMO Vision MCP ✅
- 中文插件 v2.4.35 ✅
- thinking=high（全局）✅
- CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50 ✅
