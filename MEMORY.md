# MEMORY.md

## 速查（每次启动先看）
- 身份：li | AI：贝拉 🦞 | GMT+8 | 风格：简洁直接
- 当前：记忆系统 3 轮迭代完成（盲区修复→6优化→7漏洞修复）
- 状态：✅ 防失忆 + 可检索（[LEARN]9条）+ 抗膨胀（归档/精简/心跳）
- 下次：验证 thinking=high 自动生效 + replay-learnings 检索 [LEARN]
- 记忆健康：✅ OK（17次心跳，无异常）

---

## 身份
- 用户：li | AI：贝拉 🦞 | 时区：GMT+8
- 风格：简洁直接，不啰嗦，说干就干

## 环境速查
- **模型**：DeepSeek V4 Pro（主力，可直连免代理）| MiMo V2.5（视觉）| Seedream 4.5（生图）
- **代理**：UniClash 托盘常驻，端口 7993。DeepSeek 直连，Google 需梯子
- **Gateway**：端口 18789，开机自启 → `gateway_keeper.bat`
- **权限**：bypassPermissions，不用每步确认

## 可用能力
- 🔍 搜索：DuckDuckGo（免代理）
- 🖼️ 生图：DashScope 万相2.6（异步，200张/天，免费用）
- 👁️ 视觉理解：MiMo V2.5（图片/视频/音频）
- 📈 股票：24个skill（评估/回测/数据源/交易），主力 stock-evaluator
- ✍️ 网文：15个skill（story系列 + openclaw-novel-write）
- 💬 通道：QQ机器人、企业微信、飞书

## 关键规则
- 做事 > 解释。能直接干的就别先汇报
- 修改重要配置前备份 `openclaw.json`
- API keys 在 `openclaw.json` 的 env 段，不要硬编码到脚本
- 代理挂了先关 `proxy.enabled`，DeepSeek 能直连

## 当前项目
- 记忆系统重构：打通 CLAUDE.md ↔ OpenClaw MEMORY.md，告别失忆

## 最近对话（跨会话连续性）
<!-- 保留最近 5 条，旧条目 → self-improving/archive/conversation-timeline.md -->
<!-- 每次重要会话结束时更新，按时间倒序 -->

### 2026-05-30 · 第二轮深度审计 + 7 漏洞修复
- LEARNED.md 改为 [LEARN] 格式（replay-learnings 可检索）
- memory.md 更新过时内容（"在搭系统"→"已建成"）
- 创建 NOTES.md 暂存文件（compact 前保存工作状态）
- 添加 PostCompact hook（compact 后自动重读 CLAUDE.md）
- 创建 .claude/memory/ 目录
- CLAUDE.md 压缩到 64 行 + 添加 4 条 [LEARN] 标签
- 设置 CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50

### 2026-05-30 · 记忆系统 6 项优化
- P0: 合并纠错系统（corrections.md→索引, 内容归 LEARNED.md）
- P0: 最近对话归档机制（保留 5 条, 旧→archive）
- P1: 心跳精简（只记变化, 15条重复噪音删除）
- P1: 速查层（MEMORY.md 顶部 5 行, 省掉翻 4 个文件）
- P2: 跨工具双向同步（确认共享文件读写均生效）
- P2: 激活 context-optimizer / compact-guard / context-engineering

### 2026-05-30 · 记忆系统盲区修复
- 全局持久化 `/thinking high`：在 `~/.claude.json` 加 `"thinking": "high"`
- 三层记忆核实：L1 Auto Memory（活跃）/ L2 Pro Workflow（已装未激活）/ L3 CLAUDE.md→MEMORY.md（已通）
- 修复盲区：MEMORY.md 加"最近对话"、创建 `.claude/LEARNED.md`、生成 session-handoff

### 2026-05-19 · 记忆系统初始化
- 搭建 self-improving 目录结构：memory.md / corrections.md / heartbeat-state.md
- 配置 CLAUDE.md 入口 + 规则
- 首次心跳 HEARTBEAT_OK
