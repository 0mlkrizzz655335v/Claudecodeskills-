# 来源与选材

核查日期：2026-09-05。首轮比较了下列 8 个公开项目的技能入口，并读取主要参考项目的许可证；星数是核查时的快照，不代表实测质量。

按中文适配、事实保真、体裁覆盖、示例可靠性、规则克制和可维护性选材。本套现由八个可独立调用的技能组成；全部中文工作流、案例、文风卡、小说扩展及审稿脚本均重新编写，没有直接安装上游整套，也没有给未做的横向效果测试下“最好”的结论。

| 项目 | 星数快照 | 最后推送日期 | 取舍 |
|---|---:|---|---|
| [blader/humanizer](https://github.com/blader/humanizer) | 43032 | 2026-08-19 | 通用编辑、作者声音、保真与误报约束；筛选吸收，重写中文流程。 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 16695 | 2026-01-19 | 中文分类便于入门；不沿用无依据补细节、强改三项及英文标点迁移。 |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | 16822 | 2026-03-17 | 参考空话与结构检查；不沿用禁用全部副词、被动句、三项列举的硬规则。 |
| [ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh) | 137 | 2026-05-22 | 参考中文句法和文章主线；不导入名人语料、自动文风询问和固定术语替换。 |
| [adewale/anti-slop-writing](https://github.com/adewale/anti-slop-writing) | 17 | 2026-08-29 | 参考先查逻辑关系、再改节奏以及保留有依据表达的方法。 |
| [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | 1401 | 2026-07-03 | 参考证据强度与专业表达保护；不移植基金申报规则或补造数据的示范。 |
| [ZeddYu/humanizer_zh](https://github.com/ZeddYu/humanizer_zh) | 1 | 2026-05-25 | 比较中文场景覆盖；部分示例含原文外细节，未直接移植。 |
| [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) | 441 | 2026-04-18 | 比较生成时约束；绝对禁词及标点配额较多，未直接移植。 |

## 对上游方法的修正

保留值得使用的编辑观察，移除固定句长、禁用三项、禁用所有副词和一律去除破折号等约束。把常用词当成需要结合上下文复核的线索，保护真实对比、正式文风及技术术语。

所有改写示例显式给出素材；非虚构改稿不从无到有补数字、经历、引文和成效。小说可以虚构，但遵守用户设定。审稿以可定位的文本问题为依据，不做作者身份判断或“AI 率”承诺。

许可证归属保留在 [第三方声明](../THIRD_PARTY_NOTICES.md)。上游文章及 Wikipedia 原文没有打包，名人文风语料没有导入。原始文件标识与核查记录见 [来源快照](source-snapshot.json)，供未来按具体版本核对；运行技能无需联网检查更新。

## 技能分工

| 名称 | 主要用途 |
|---|---|
| natural-writing | 通用文章起草和改写，中文优先，含英文、体裁和长文参考 |
| voice-profile | 从用户样文提炼与应用文风 |
| natural-fiction | 小说场景、对话、视角、连载及成长连续性 |
| precise-prose | 学术、技术及工作文本的准确表达 |
| prose-audit | 问题定位、保真对比、只读扫描 |

各技能自带完成其任务的规则，不依赖安装路径或其他技能必然存在。按任务使用，避免把全部规则同时加载。

## 2026-09-05 融合扩展

新增 qu-ai-wei、humanizer-zh-academic 与 research-paper-writing 的融合版入口，按中文深改、论文语言编辑、研究方法论分工。吸收语义账本、引用绑定和证据规划，修正排除范围扩张；排除检测配额与虚构研究过程的示例。

- [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei/tree/v0.9.0)
- [redbaronyyyyy-eng/humanizer-zh-academic](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic/tree/main)
- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/main)
