# Claudecodeskills

56 个 AI Skills 合集：中文写作、文档办公、任务自动化、代码审查、开发环境、技能生态，覆盖日常工作流的大部分场景。

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

完整简介见 [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md)。

## 安装

**方式一：用 skill-installer（推荐）**

```
# 在 Codex 里说：
从 GitHub 仓库 0mlkrizzz655335v/Claudecodeskills- 安装 <skill-name>
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

## 说明

- 每个 skill 目录下的 `SKILL.md` 是入口，`description` 字段为中文简介，供 agent 路由识别。
- `skills/writing/` 的 8 个写作 skills 另有一份打包在 `codex-skills-pack/`，内容一致，方便整体取用。
