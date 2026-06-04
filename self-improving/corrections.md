# Corrections Index
> 详细纠错内容见 `~/.claude/LEARNED.md`，本文件仅做索引。

| 日期 | 类别 | 摘要 | LEARNED.md 行 |
|------|------|------|--------------|
| 2026-06-05 | Diagnosis | 7项修复无效但标记完成 — 修复后未验证事件日志 | L42-44 |
| 2026-06-05 | Optimization | 深度优化脚本会重新开启HAGS与修复冲突 | L45-47 |
| 2026-06-05 | Tool | DISM RestoreHealth卡62.3%不可靠 | L48-50 |
| 2026-06-05 | Search | GitHub API搜索太泛，DuckDuckGo+定点抓取更有效 | L51-53 |
| 2026-06-04 | Verification | handoff 路径盲信 (`marketplaces/` vs 实际 `plugins/marketplaces/`) | L32-34 |
| 2026-06-04 | Deploy | pro-workflow 双重安装导致 hooks 3 倍触发风险 | L36-38 |
| 2026-06-04 | Hooks | 声称 "36 hook事件" 实际仅6个生效 — plugin hooks.json 未被 .claude.json 加载 | L40-42 |
