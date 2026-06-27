# MEMORY.md

## 速查（每次启动先看）
- 身份：li | AI：贝拉 🦞 | GMT+8 | 风格：简洁直接
- 当前：UniClash 已彻底移除，网络直连正常
- 游戏崩溃根因已确认：UniClash ON/OFF → 后续不再需要代理，直连即可
- 记忆健康：✅ OK（19次心跳，无异常）

---

## 身份
- 用户：li | AI：贝拉 🦞 | 时区：GMT+8
- 风格：简洁直接，不啰嗦，说干就干

## 环境速查
- **模型**：DeepSeek V4 Pro（主力，可直连免代理）| MiMo V2.5（视觉）| Seedream 4.5（生图）
- **网络**：直连，无代理。UniClash 已彻底移除（2026-06-05）
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

## 当前项目
- 记忆系统重构：打通 CLAUDE.md ↔ OpenClaw MEMORY.md，告别失忆

## 最近对话（跨会话连续性）
<!-- 保留最近 5 条，旧条目 → self-improving/archive/conversation-timeline.md -->
<!-- 每次重要会话结束时更新，按时间倒序 -->

### 2026-06-05 · UniClash 彻底移除
- 官方卸载程序 → 安装目录 E:\新建文件夹 (2)\UniClash 已删除
- AppData: Local + Roaming UniClash 目录已删除
- Flutter WebView 缓存 (flutter_webview_windows\uniclash) 已删除
- 注册表: Tracing\uniclash_RASAPI32 已删除 | 卸载信息已清理
- 环境变量 HTTP_PROXY (7993) 已永久删除 | ProxyOverride 已清空
- VeryKuai TAP Adapter (以太网2) 已通过 pnputil /remove-device 移除
- openclaw.json 已备份 | 网络连通性: baidu.com 正常
- **后续**：直连无代理，DeepSeek 直连不受影响

### 2026-06-05 · 游戏崩溃第四轮 — 根因：UniClash ON/OFF + 全部恢复
- 用户关键发现：UniClash ON→所有游戏正常，OFF→崩溃(ntdll 0xc0000005)
- 360/ACE/ASUS/BattlEye等全部误判，已恢复所有服务和启动项

### 2026-06-05 · 游戏崩溃第二轮 — 7项修复全无效 + 新诊断

### 2026-06-05 · 三角洲 1067104 修复 + 塔可夫记忆恢复
- 用户发现塔可夫优化工作在记忆系统中零记录（实际 6/4 已完成 5 个文件）
- 全盘扫描 → 发现 F:\EFT\ 下 5 个优化脚本（启动器/系统优化/Defender排除）
- 创建 `self-improving/projects/tarkov.md` 项目记忆
- **教训**：跨日连续对话必须当天写入记忆，不能依赖"明天再说"

### 2026-06-04 · Hooks 修复 + 验证（2轮）
- 根因：agentmemory + pro-workflow 的 plugin.json 缺少 `"hooks"` → hooks.json 从未加载
- 最终：6 包 89 skills + 36 hook 事件 + 8 agents ✅
- handoff → self-improving/session-handoff/session-2026-06-04-hooks-fix.md
