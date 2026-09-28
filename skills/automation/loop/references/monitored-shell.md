# Monitored shell wakeups

Read only after the host shell schema confirms output notifications that wake the agent. These examples do not apply to ordinary exec_command background sessions without that feature. SKILL.md governs first-run timing and notification intent.

# Monitored shell output (local)

Use monitored shell output to wake the agent for recurring local work.

## Fixed Schedule

```bash
while true; do
  sleep <seconds>
  echo 'AGENT_LOOP_TICK_<purpose> {"prompt":"<prompt>"}'
done
```

1. Check existing terminals for an already-running matching loop.
2. Start one background shell loop with `notify_on_output`.
3. Use a unique sentinel and a regex such as `^AGENT_LOOP_TICK_<purpose>`.
4. Smoke-check once to confirm clean startup.
5. Run the prompt once after arming only when the request includes an immediate initial run; skip this for a future-only request.
6. The first sentinel should arrive only after the initial sleep, so startup does not double-run the prompt.
7. Track the PID so the agent can stop the loop if asked.
8. Briefly confirm the actual initial-run behavior, interval, first tick, lifetime, and stop mechanism supported by the host. On later ticks, follow SKILL.md notification intent; do not emit unchanged status unless requested. On stop, say the loop has stopped and why.

## Dynamic Schedule

The user wants the agent to self-pace. Decide what makes the next iteration worth running — a passage of time, or an observable event.

1. **Run now only when the request includes an initial run; otherwise wait for the scheduled first execution.**
2. **If the next run is gated on an event** (a git ref advancing, a log line matching, a file changing, a CI check completing), arm a background watcher that emits the sentinel only when the event fires, with `notify_on_output` on `^AGENT_LOOP_WAKE_<purpose>`. Arm once; skip on later ticks if it's still running.
3. **At the end of the turn, arm a one-shot time-based wake**:

```bash
sleep <seconds>
echo 'AGENT_LOOP_WAKE_<purpose> {"prompt":"<prompt>"}'
```

   With a watcher armed, this is the **fallback heartbeat** — lean long so idle ticks aren't pure overhead. Without a watcher, this is the cadence — pick a delay based on when the result is worth checking again.

4. **On wake**, read the latest payload, execute its `prompt`, then re-arm the next heartbeat (and re-arm the watcher only if it exited). If both an output wake and a completion notification arrive, act on the output and ignore the completion.
5. **To stop**, kill any watcher PID and don't arm the next heartbeat.
6. Briefly confirm the chosen pacing, primary wake signal, fallback delay, and whether an initial run actually occurred.

## Prompt Payload

Wake notifications include an output file path, not a submitted prompt. Put the prompt beside the sentinel, preferably as JSON. On wake, read the latest matching line and act on its `prompt`. The prompt may vary by tick.

## Guidance

- Title shell commands as `Loop <schedule>: <prompt>` (e.g. `Loop every 5m: check deploy status`).
- Adapt loop syntax to the user's shell (e.g. PowerShell `while ($true) { ... Start-Sleep }` on Windows). The examples above use bash.
- Prefer monitored shell output over OS cron when the agent needs wake notifications; stdout stays attached to the monitored task.
- Use a unique sentinel per loop so unrelated output does not trigger notifications.
- Avoid noisy commands inside the loop.
- Do not create duplicate fixed loops or dynamic sleepers.
- If the user asks to stop, kill any tracked loop/sleeper PID, then await the shell task so its completion notification is consumed and does not wake the agent later. Do not schedule another dynamic wake.
