# 写作 Skills 工作流（Codex）

本目录 `skills/` 下的 8 个 skill 构成一套中文写作系统，全部兼容 Codex 的
`~/.codex/skills/<name>/SKILL.md` 格式。把 `skills/` 整个复制到
`~/.codex/skills/` 即可用。

## 调用规则

**所有写作任务，先读 `natural-writing`（总控）。** 它会根据任务类型把你
路由到正确的专门 skill，不要凭感觉直调下游。

| 任务 | 主 skill |
|---|---|
| 一般文章起草 / 轻改润色 / 英文稿 | natural-writing |
| 已有中文深改、整篇结构重组 | qu-ai-wei |
| 中文论文语言润色（不动结论） | humanizer-zh-academic |
| 论文提纲 / 研究论证 / 章节结构 / 证据规划 | research-paper-writing |
| 技术报告 / 实验记录 / 工作汇报 | precise-prose |
| 小说创作 / 章节润色 / 续写 | natural-fiction |
| 只审稿、不改写（诊断 AI 味、保真对比） | prose-audit |
| 提炼文风 / "按我的风格写" | voice-profile |

## 铁律（所有 skill 共通）

1. **保真优先**：不编造数字、案例、引用、经历；不确定就写小、写成假设、或问用户要。
2. **一次只调一个主 skill**，不串行加载整套；下游不反向调用总控。
3. **默认交付成稿**，不附长篇自我评估；用户要审稿意见时才给。
4. 不承诺"AI 检测通过率"，不输出自然度分数。
