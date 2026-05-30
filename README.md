# Claude Code 长期记忆系统

> 让 Claude Code 拥有跨会话的持久记忆，不再每次"失忆"。

## 三层架构

`
L1 内置    Claude Code Auto Memory   自动记录代码规范/构建命令/偏好
L2 插件    Pro Workflow hooks        [LEARN]自动捕获 + 会话交接 + 上下文恢复
L3 共享    MEMORY.md 跨工具时间线    跨 Claude Code / {跨工具平台} 的对话连续性
`

## 快速安装

### 1. 安装 Pro Workflow 插件
`ash
claude plugins install rohitg00/pro-workflow
`

### 2. 复制本仓库文件
`ash
git clone https://github.com/{user}/claude-memory-system.git
cp CLAUDE.md ~/CLAUDE.md
cp MEMORY.md {SHARED_MEMORY_PATH}/MEMORY.md
cp -r self-improving/ ~/self-improving/
cp -r .claude/ ~/.claude/          # LEARNED.md + rules + memory/
cp NOTES.md ~/NOTES.md
`

### 3. 配置 hooks（核心自动化）
将 .claude/settings.template.json 中的 hooks 段合并到你的 ~/.claude.json：
`json
{
  "thinking": "high",
  "env": { "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50" },
  "hooks": { ... }
}
`

### 4. 编译 Pro Workflow dist
`ash
cd ~/.claude/plugins/marketplaces/pro-workflow
npm install --ignore-scripts
npx tsc
`

### 5. 应用 learn-capture 补丁
`ash
cp patch/learn-capture.js ~/.claude/plugins/marketplaces/pro-workflow/scripts/
`
此补丁让 learn-capture.js 在 better-sqlite3 不可用时回退到直接写 LEARNED.md。

## 文件说明

| 文件 | 作用 |
|------|------|
| CLAUDE.md | 入口，定义记忆系统结构+规则+[LEARN]标签 |
| MEMORY.md | 跨工具共享记忆，含速查层+最近对话时间线 |
| self-improving/memory.md | 热记忆：用户偏好、模式、规则 |
| self-improving/corrections.md | 纠错索引（详情在 LEARNED.md） |
| self-improving/heartbeat-state.md | 记忆健康心跳 |
| self-improving/session-handoff/ | 跨会话交接文档 |
| self-improving/archive/ | 归档的旧时间线条目 |
| .claude/LEARNED.md | [LEARN] 格式的学习规则（replay-learnings 可检索） |
| .claude/rules/ | Pro Workflow .mdc 规则文件（双保险） |
| NOTES.md | compact 前保存工作状态 |

## 自动化能力

| Hook | 触发时机 | 功能 |
|------|----------|------|
| SessionStart | 会话启动 | 加载 [LEARN] 模式 + 显示上次会话摘要 |
| Stop | 每次回复后 | 自动扫描 [LEARN] 并存入 LEARNED.md |
| PreCompact | compact 前 | 保存上下文状态 |
| PostCompact | compact 后 | 恢复关键上下文 |
| SessionEnd | 会话结束 | 提示记录学习 |

## 特性

- **防失忆**：3 层记忆，跨会话/跨工具
- **可检索**：replay-learnings 通过 [LEARN] 标签检索 9+ 条规则
- **抗膨胀**：心跳精简、最近对话归档（保留 5 条）
- **秒级冷启动**：MEMORY.md 速查 5 行进入状态（~200 bytes）
- **自动闭环**：learn-capture 文件回退，无需 better-sqlite3

## 维护

- 每 5 次会话检查 heartbeat-state.md
- 重要会话结束执行 wrap-up → session-handoff → 更新 MEMORY.md
- 最近对话超过 5 条时手动归档到 archive/
