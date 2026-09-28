# Subscription timer contract

Use only with the available cursor-subscriptions timer tool. The current tool schema and SKILL.md govern authorization, first-run timing, and reporting.

# Subscription timer (cloud)

Use the `cursor-subscriptions` MCP timer to wake this Cloud Agent on a recurring schedule using `cursor-subscriptions-subscribe_timer`.

## Schedule

Call `cursor-subscriptions-subscribe_timer` with:

- `name`: a stable handle, e.g. `loop-<purpose>` derived from the prompt (`loop-check-deploy`). The server dedupes by name and **silently keeps the old config** on a dedupe hit — see "Changing an existing timer" below.
- `prompt`: the literal follow-up text the agent should receive on each tick.
- Exactly one of `delaySeconds` (a positive integer, fixed interval between fires) or `cron` (a cron expression).

Run the prompt immediately only when the request includes an initial run. For a future-only request, subscribe without executing it now. After successful scheduling, confirm the actual first-run behavior, interval, returned `subscriptionId`, and confirmed expiry or stop condition.

Each subsequent tick arrives as a normal follow-up prompt. Do not arm anything client-side; the server keeps firing until you unsubscribe or the timer expires.

## Changing an existing timer

`subscribe_timer` does **not** update an existing timer in place. If a live timer with the same `name` already exists, the server returns its current `subscriptionId` with `created: false` and **drops the `prompt`, `cron`, and `delaySeconds` you just passed**. To actually change any of those, call `cursor-subscriptions-unsubscribe` for the current `subscriptionId` first, then `cursor-subscriptions-subscribe_timer` with the new values.

## Dynamic Schedule

The user wants the agent to self-pace. `cursor-subscriptions` can watch CI checks with `cursor-subscriptions-subscribe_github_ci` or `cursor-subscriptions-subscribe_origin_ci`, but it has no event-watcher analog for arbitrary signals such as file changes or log lines. For those signals, the only knob is the time interval.

1. **Run now only when the request includes an initial run; otherwise wait for the scheduled first execution.**
2. Subscribe once with your first-picked `delaySeconds`.
3. On each tick, if the next desired interval is unchanged, do nothing — the timer keeps firing.
4. To change pace, **unsubscribe first** (`cursor-subscriptions-unsubscribe` with the current `subscriptionId`), then `cursor-subscriptions-subscribe_timer` with the same `name` and the new `delaySeconds`. Skipping the unsubscribe is a silent no-op: the server returns the existing subscription unchanged and ignores the new `delaySeconds`.

## Stop

1. Call `cursor-subscriptions-list_subscriptions` to find the row whose name matches `loop-<purpose>`.
2. Call `cursor-subscriptions-unsubscribe` with that `subscriptionId`.
3. Confirm: the loop has stopped and why. Do not arm another timer.

If several timers match the purpose and you cannot disambiguate, surface the candidates to the user and ask which one to stop.

## Guidance

- Use a unique `name` per loop so unrelated timers do not collide.
- Do not start a local `sleep` loop or any background shell wake — they do not work in cloud.
- Re-arming with the same `name` on a live timer is a silent no-op — the new `prompt` / `cron` / `delaySeconds` are dropped. To change anything about a live timer, unsubscribe first.
- On stop, do not schedule another timer.
