# claude-skills-zh

[![GitHub stars](https://img.shields.io/github/stars/0mlkrizzz655335v/claude-skills-zh)](https://github.com/0mlkrizzz655335v/claude-skills-zh/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**56 production-ready AI agent skills for Claude Code / Codex — including the only systematic set of 8 Chinese writing skills: de-AI-flavor rewriting, academic polishing, research-paper argumentation, fiction writing.**

**56 个开箱即用的 AI agent skills（含 8 个成体系的中文写作 skills：去 AI 味、学术润色、论文论证、小说创作），覆盖文档办公、任务自动化、代码审查、开发环境。**

## Quick start / 快速开始

```bash
# 只装一个中文写作 skill
cp -r skills/writing/natural-writing $CODEX_HOME/skills/
# 全部安装
cp -r skills/* $CODEX_HOME/skills/
```

完整 skill 目录与中文简介见 [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md)。

## Why this repo / 为什么选这个仓库

- **中文写作是英文世界几乎没人覆盖的生态位。** 8 个写作 skills 分工明确：`natural-writing` 总控路由、`qu-ai-wei` 中文去 AI 味深改、`humanizer-zh-academic` 学术润色、`research-paper-writing` 论文论证、`natural-fiction` 小说创作、`precise-prose` 精确表达、`prose-audit` 文字审计、`voice-profile` 文风提炼。
- 56 个 skills 按 6 大类整理（约 570 个文件），每个 skill 目录下的 `SKILL.md` 即入口，`description` 字段为中文简介，供 agent 路由识别。
- `codex-skills-pack/`：8 个写作 skills 的开箱即用包（含路由规则与导入说明），只想要中文写作能力直接取这个目录。

## 目录结构

```
skills/
├── writing/        中文写作与润色（8）—— natural-writing 总控、去 AI 味、学术润色、论文论证、小说创作……
├── docs-office/    文档与办公（15）—— Word、PDF、表格、幻灯片、Google 全家桶、建站、模板
├── automation/     任务自动化与编排（8）—— 定时任务、PR 自动跟进、事件订阅、长期目标
├── code-review/    代码审查与质量（5）—— Bugbot 缺陷审、安全审、拆 PR
├── dev-env/        开发环境与工程配置（12）—— SDK、仓库、CLI 配置、编辑器设置
└── ecosystem/      技能与插件生态（8）—— 创建/安装 skill 与插件、查官方文档
codex-skills-pack/  开箱即用的 Codex 写作包（8 个写作 skills + 路由规则 + 导入说明）
docs/
└── SKILLS_CATALOG.md  56 个 skills 的完整分类目录与中文简介
```

## 安装

**方式一：用 skill-installer（推荐）**

```
# 在 Codex 里说：
从 GitHub 仓库 0mlkrizzz655335v/claude-skills-zh 安装 <skill-name>
```

skill-installer 会从本仓库的 `skills/` 路径拉取并装到 `$CODEX_HOME/skills`。

**方式二：手动复制**

```bash
# 单个 skill
cp -r skills/writing/natural-writing $CODEX_HOME/skills/
# 全部
cp -r skills/* $CODEX_HOME/skills/
```

**方式三：写作包（只想要中文写作能力）**

直接取 `codex-skills-pack/` 目录，按其中的 `导入说明.md` 操作。

## License

MIT — 详见 [LICENSE](LICENSE)。
