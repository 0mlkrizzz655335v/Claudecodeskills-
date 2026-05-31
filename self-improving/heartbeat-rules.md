# Heartbeat Rules
auto_check_interval: 5
alert_on_stale: true
stale_threshold_days: 3

## Rules
- 心跳日志只记录变化事件，不记录"无变化"
- 超过 5 次会话未检查触发提醒
- 发现异常自动追加到 corrections.md 索引
