# Skills 功能分类与简介（重写版）

> 整理日期：2026-09-28
> 范围：PC 端实际导出的 56 个 skills（`~/workspace/pc-skills/skills/`）
> 说明：简介全部重写为中文，"适用"栏标注调用时机；原英文 description 仅作功能依据，不直接沿用。

---

## 一、中文写作与润色（8）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 1 | natural-writing | 通用中文写作总控。起草或润色各类中文文章（兼顾英文），保留事实、立场和作者声音，弱化套话与机械表达。 | 一般文章写作；不确定用哪个写作 skill 时先走它分流 |
| 2 | qu-ai-wei | 中文深度改写去 AI 味。对已有简体中文做保真深改或整篇重组，保留全部实质信息、作者语气和证据边界。 | 中文深改、整篇重写；从零起草用 natural-writing |
| 3 | humanizer-zh-academic | 中文学术语言润色。润色论文、毕业设计、实验报告的语言，减少学术套话与机械句法，不动数据、引用和结论强度。 | 中文论文语言编辑；不改研究结论、不补实验 |
| 4 | research-paper-writing | 论文研究设计与论证。帮你定研究问题、搭章节结构、写方法与文献综述、规划证据链。 | 开题、整篇论文、论证审查；纯语言润色用 humanizer-zh-academic |
| 5 | precise-prose | 技术与工作文档润色。润色技术文章、实验记录、项目说明、工作报告，保护术语、数据、单位、流程步骤和结论强度。 | 专业写作的语言把关 |
| 6 | natural-fiction | 中文小说创作与润色。写、改、续中文小说与网文章节（含玄幻、系统流），抓情节因果、视角、人物声音和连续性。 | 小说去 AI 味、场景改写、章节续写 |
| 7 | prose-audit | 审稿诊断，只审不改。检查 AI 味、套话、翻译腔、重复、逻辑断裂和改写失真，按原文给修改优先级。 | 完稿前的质量审查；不输出 AI 概率、不判断作者 |
| 8 | voice-profile | 文风提炼与匹配。从你的样文提炼文风特征，用于新稿或改写，保持你自己的节奏和用词习惯。 | "按我的风格写"、多篇文章口吻统一；没有样文时不必调用 |

---

## 二、文档与办公（15）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 9 | documents | Word 文档全流程处理。创建、编辑、校对 `.docx`，带渲染验真流程，所见即所得。 | Word 长文档、合同、报告的生成与修改 |
| 10 | pdf | PDF 读取、生成与验真。处理版式敏感的 PDF，支持可填写表单（AcroForms），用渲染做视觉校验。 | PDF 生成、解析、填表、版式检查 |
| 11 | spreadsheets | 表格文件处理与分析。创建、修改、分析 `.xlsx`/`.csv` 等离线表格，含公式、格式、图表。 | 离线表格文件；实时操控 Excel 用 excel-live-control |
| 12 | excel-live-control | 实时操控 Excel 应用。通过 ChatGPT 插件直接操作已打开的 Excel 工作簿。 | 在对话里直接改正在用的 Excel |
| 13 | presentations | 幻灯片制作与编辑。读写 PowerPoint（.pptx）与 Google Slides。 | 演示文稿的新建、改版、内容更新 |
| 14 | google-drive | Google Drive 总入口。查找、整理、分享、导出、删除 Drive 文件，统一调度 Docs/Sheets/Slides 子技能。 | Google 云端文件的统一管理 |
| 15 | google-docs | Google Docs 内容编辑。创建、编辑、总结、改写在线文档，保留样式与结构。 | 在线文档撰写与协作修改 |
| 16 | google-sheets | Google Sheets 精确编辑。按单元格区域精度分析、编辑在线表格，处理公式、图表、数据清洗。 | 在线表格的数据处理 |
| 17 | google-slides | Google Slides 演示制作。按模板或参考稿派生设计系统，制作在线幻灯片。 | Google Slides 的新建与改版 |
| 18 | google-drive-comments | Drive 评论管理。撰写、回复、解决 Docs/Sheets/Slides 上的评论 thread。 | 文档评审与协作批注 |
| 19 | sites-building | 网站搭建。从零搭建完整网站（落地页、作品集、仪表盘、内部工具等）。 | 要一个能用的网站；纯改代码不用它 |
| 20 | sites-hosting | 网站发布与托管。发布用 Sites 建好的网站并管理托管。 | 网站上线、更新发布 |
| 21 | sites-preview-troubleshooting | 预览故障诊断。诊断并恢复失败的 Sites 预览会话（仅托管 Linux 环境）。 | 网站预览挂了的时候 |
| 22 | template-creator | 从参考文档生成可复用模板。把一份参考文档/演示/表格变成以后能反复套用的模板 skill。 | 固定版式的周报、报告、提案 |
| 23 | computer-use | 在 ChatGPT 里操控 Windows 应用。 | 需要实际点开、操作 Windows 软件的任务 |

---

## 三、任务自动化与编排（8）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 24 | automate | 创建自动化、提醒与监控。按你的要求设定自动执行的任务。 | 定时提醒、价格/到货监控、周期性检查 |
| 25 | loop | 定时循环执行。每隔固定时间重复跑一条 prompt 或 skill。 | `/loop 5m` 这类周期性小任务 |
| 26 | autopilot | PR 自动跟进。循环处理 PR 评论、解决冲突、修 CI，直到可合并。 | PR 挂起等合入时扔给它盯着 |
| 27 | subscribe | 订阅外部事件。用订阅代替轮询，等 GitHub CI 结果、PR 动态、Slack 消息、Linear issue。 | 等外部事件触发的任务 |
| 28 | goal | 设定长期目标。让 Codex 持续推进一个目标直到完成。 | 跨多次会话的长期任务 |
| 29 | create-hook | 创建事件钩子。识别运行环境后按钩子 schema 注册指定行为。 | 想让 agent 在特定事件发生时自动做事 |
| 30 | create-subagent | 创建自定义子代理。为专门任务定制子代理（代码审查、调试、领域助手等）。 | 需要一个有特定职责的分身 |
| 31 | onboard | 新手引导流程。了解你的基本偏好、定第一个目标、指引下一步。 | 刚开始用 Codex 时跑一遍 |

---

## 四、代码审查与质量（5）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 32 | review | 代码审查总入口。按需调度 Bugbot 或安全审查子代理。 | 改完代码要审查时先找它 |
| 33 | review-bugbot | 缺陷导向代码审查。用 Bugbot 子代理找 bug。 | 合入前的缺陷扫描 |
| 34 | review-security | 安全代码审查。用安全审查子代理找漏洞。 | 涉及鉴权、输入处理、密钥的代码 |
| 35 | review-agent | 只读深度审查。对指定改动做只读的、缺陷优先的审查，返回所有可落地的发现。 | 别的 agent 委托审 diff、审 commit |
| 36 | split-to-prs | 拆分 PR。把当前工作拆成多个小而可审的 PR。 | 改动太大、一次合入审不动时 |

---

## 五、开发环境与工程配置（12）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 37 | sdk | Codex SDK 集成开发。用 TypeScript/Python SDK 做 agent 生命周期、流式输出、本地/云端执行等集成。 | 二次开发、对接 SDK |
| 38 | shell | 执行 shell 命令。把 `/shell` 之后的内容当字面命令直接跑。 | 你明确敲 `/shell` 想跑命令时 |
| 39 | new-repo | 创建并推送托管仓库。验证平台后创建 Codex 托管仓库并推送。 | 开新项目要建仓库时 |
| 40 | origin | origin CLI 管理。安装、登录、更新、修复 origin.cursor.com 的 CLI。 | Codex 托管仓库推拉鉴权失败、CLI 缺失时 |
| 41 | share | 项目分享与备份。把当前项目存到 Codex 托管并分享，校验上传与访问范围。 | 备份项目或发给别人看时 |
| 42 | statusline | 状态栏配置。配置 Codex 或兼容 CLI 的状态栏。 | 自定义终端状态栏显示 |
| 43 | update-cli-config | CLI 配置修改。查看或修改 Codex/兼容 CLI 的配置。 | 改 agent 命令行工具的设置 |
| 44 | update-cursor-settings | 编辑器设置修改。改 Cursor/VS Code 的设置与快捷键，保留原有注释和无关项。 | 调编辑器配置 |
| 45 | canvas | Canvas 交互视图。用 `.canvas.tsx` 工件做原生交互界面。 | 需要可视化交互呈现的任务 |
| 46 | migrate-to-builds | 迁移到预构建环境。测试云端 agent 环境是否兼容预构建镜像并给出改造建议。 | 想用 Builds 功能前先验证 |
| 47 | migrate-to-skills | 旧规则迁移。把 `.mdc` 规则或斜杠命令完整迁移成 skills。 | 升级旧工作流到 skill 体系 |
| 48 | rename-chat | 重命名当前聊天。按聊天内容改标题。 | 你主动调用 `/rename-chat` 时 |

---

## 六、技能与插件生态（8）

| # | 名称 | 简介 | 适用 |
|---|------|------|------|
| 49 | skill-creator | 创建与更新 skill。写作用域合理的 skill 指令及配套资源。 | 要新增或改造一个 skill 时 |
| 50 | create-skill | skill 创建兼容入口。收到明确的创建 skill 请求时，路由给 skill-creator。 | 直接说"创建一个 skill"时走它 |
| 51 | plugin-creator | 创建本地插件。写插件清单、打包、发布到个人市场。 | 开发 Codex 插件时 |
| 52 | plugin-management | 插件发现与管理。推荐相关插件、查看权限依赖、管理插件连接与卸载。 | 找插件、管插件 |
| 53 | skill-installer | 安装 skill。从精选列表或 GitHub 仓库路径把 skill 装进本地。 | 装别人写好的 skill |
| 54 | create-rule | 创建持久化项目规则。写 AGENTS.md 等项目级长期指导。 | 要给项目立规矩时 |
| 55 | imagegen | 图像生成与编辑。生成或改图：照片、插画、mockup、位图素材；矢量/SVG 走原生编辑。 | 要配图、做素材时 |
| 56 | openai-docs | 查 OpenAI 官方文档。查 OpenAI 产品/API、Codex 配置、模型、skill 的一手资料，疑难杂症以官方为准。 | 遇到产品行为不确定、要核实官方说法时 |

---

## 备注

- 分类依据是各 skill 的 SKILL.md 原始 description，不是按目录名（原 `agent/`、`plugins/`、`system/`、`user/` 是来源划分，不是功能划分）。
- 有调用关系的已在"适用"栏注明（如 natural-writing 是写作总控、review 调度子代理、google-drive 调度 Docs/Sheets/Slides）。
- 本文档是目录与简介层，不改变任何 skill 文件本身；如需把新简介写回各 SKILL.md 的 description 字段，另行执行。
