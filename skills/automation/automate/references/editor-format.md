# Automations editor protocol notes

Use only when the current editor handoff accepts this `WorkflowData` protocol. Its live schema wins if fields differ. SKILL.md governs authorization, tool choice, and unavailable-capability handling; this reference never requires extra approval or prevents supported automation APIs.

## Integration details

- The editor distinguishes a Slack trigger scope from a posting destination. Resolve each requested scope separately. Its action channel IDs use C/G prefixes; D IDs are supported only where the current schema documents an owner DM. Do not substitute member IDs.
- When this editor uses `mcp.server.name`, use the actual catalog's configured serverName rather than inventing a prefix or copying a serverIdentifier. Local server visibility in chat does not prove it exists in a cloud automation's catalog.
- For this editor, authentication can navigate away from an unsaved draft. Resolve required authentication before opening that draft when possible; otherwise preserve the prepared values and identify the setup limitation. Do not turn this behavior into a blanket stop for another automation API.
- Follow current schedule/timezone representation. Do not drop a requested schedule into prompt text while leaving a scheduled automation without a real trigger.

### YAML output shape (agent-internal)

Wire format matches the reviewed Automations draft passed to `open_automation` as `prefillWorkflowData` — canonical proto JSON with full enum names (e.g. `GIT_PULL_REQUEST_ACTION_OPENED`). PR scope lives on `git.pullRequest` (`repos` / `orgs`); `workflow.gitConfig` holds `repo` + `branch` for non-`git` triggers that need a checkout. Use `ignoreDraftPrs`, not `ignoreDraftPr`. Slack channel IDs: `C…` / `G…`; a `D…` id (`slack` action only) resolves to the automation owner's DM.

Skeleton:

```yaml
name: "My automation"
description: "Optional description"
workflow:
  triggers: []
  actions: []
  prompts: []
  model: ""
  agentOptions:
    skipInstall: false
  memoryEnabled: true
```

Prompts use `|` block scalar (`>-` folding breaks bullets). Empty `{}` actions are valid when the field is UI-only. `mcp.server.name` is required when `mcp` is enabled, and the name must match the configured `serverName` in the actual automation catalog — not a guessed folder / `serverIdentifier`. Use `SERVER_METADATA.json` only when the current host supplies it. Confirm the server is available to the automation runtime as described in Integration details above.

**Trigger oneof keys are exhaustive.** Every entry in `workflow.triggers` must use exactly one of these top-level proto keys: `cron`, `git`, `slackTrigger`, `slackReactionAdded`, `slackChannelCreated`, `microsoftTeamsTrigger`, `microsoftTeamsChannelCreated`, `linear`, `webhook`, `pagerduty`, `sentry`. Never invent or paraphrase (`slackReaction`, `slack_reaction`, `slack`, `reactionAdded`, etc.) — the editor decodes triggers with `ignoreUnknownFields: true`, silently drops unknown keys, and renders the result as an unconfigurable "Configure trigger" card that blocks save. Empty `{}` trigger entries hit the same failure mode; never prefill a trigger you cannot fully name.

## Appendix — Trigger selection tables

These labels are agent-only — never show ids to users. If a future structured picker is used, split rows before any option cap.

### Trigger category

**Prompt:** "When should this automation run?"

| Option label | Option id | Proto / YAML |
|--------------|-----------|----------------|
| On a schedule | `cron` | `cron` |
| On a GitHub / GitLab event | `git` | `git` → specific event |
| On a Slack event | `slack` | specific event: `slackTrigger` vs `slackChannelCreated` |
| On a Linear event | `linear` | `linear` → specific event |
| On a PagerDuty incident event | `pagerduty` | `pagerduty` → specific event |
| On a Sentry issue event | `sentry` | `sentry` → specific event |
| On an incoming HTTP webhook | `webhook` | `webhook` |

### Specific event (per category)

**`cron`** — Prompt: "Which schedule shape?"

| Option label | Option id | Notes |
|--------------|-----------|-------|
| Every hour | `cron_every_hour` | UI preset |
| Every day | `cron_every_day` | preset |
| Every week | `cron_every_week` | preset |
| Custom cron expression | `cron_custom` | user supplies full cron |

**`git`** — Prompt: "Which Git event?"

| Option label | Option id | Maps to |
|--------------|-----------|---------|
| Draft pull request opened | `git_draft_opened` | `DRAFT_OPENED` |
| Pull request opened | `git_pr_opened` | `OPENED` |
| Code pushed to a pull request | `git_pr_pushed` | `PUSHED` |
| Pull request merged | `git_pr_merged` | `MERGED` |
| Comment added on pull request | `git_pr_commented` | `COMMENTED` |
| Label change | `git_label` | label trigger |
| New push to branch | `git_push` | push |
| Checks completed | `git_ci` | `ciCompleted` |

**`slack`** — Prompt: "Which Slack trigger?"

| Option label | Option id | YAML |
|--------------|-----------|------|
| New message in channel | `slack_message` | `slackTrigger` |
| Reaction added to message | `slack_reaction_added` | `slackReactionAdded` |
| Channel created | `slack_channel_created` | `slackChannelCreated` |

**`slackReactionAdded` payload** — `{ channels: ["C…"], emojiName: "<name>" }`. `emojiName` is the Slack short name **without** surrounding colons (e.g. `thumbsup`, not `:thumbsup:`); the server normalizes Unicode emoji to the matching alias on save. Completion reactions are not supported on `slackReactionAdded` triggers (would recurse) and are silently dropped.

**Completion reaction on a Slack message trigger.** "React with `:foo:` when the agent finishes" is a completion-reaction option on `slackTrigger`, not a separate trigger. Put `slackCompletionReactionMode: SLACK_COMPLETION_REACTION_MODE_CUSTOM` and `slackCompletionReactionCustomEmoji: ":foo:"` (with surrounding colons) on the same `slackTrigger` entry. Do not create a `slackReactionAdded` trigger to express completion behavior.

**Disambiguate "react with …".** When the user says "react with X to trigger" the trigger is `slackReactionAdded` (`emojiName: "x"`, no colons). When the user says "react with X when done" / "upon completion" / "after success" the trigger is `slackTrigger` with the completion-reaction fields above. Ask one focused question when intent is ambiguous instead of guessing.

**`linear`** — Prompt: "Which Linear event?"

| Option label | Option id | Proto JSON |
|--------------|-----------|------------|
| Issue created | `linear_created` | `linear.issueCreated` |
| Issue status changed | `linear_status` | `linear.statusChanged` |
| End of cycle | `linear_cycle` | `linear.endOfCycle` |

**`pagerduty`** — Prompt: "Which PagerDuty incident event?"

| Option label | Option id | Proto JSON |
|--------------|-----------|------------|
| Incident triggered | `pagerduty_triggered` | `incidentTriggered: {}` |
| Incident acknowledged | `pagerduty_ack` | `incidentAcknowledged: {}` |
| Incident resolved | `pagerduty_resolved` | `incidentResolved: {}` |
| Any incident event | `pagerduty_any` | `incidentAny: {}` |

Optional `serviceIds`. Proto may include `incidentEscalated` — only if user asks.

**`sentry`** — Prompt: "Which Sentry issue event?"

| Option label | Option id | Proto JSON |
|--------------|-----------|------------|
| Issue created | `sentry_created` | `issueCreated: {}` |
| Issue resolved | `sentry_resolved` | `issueResolved: {}` |
| Issue assigned | `sentry_assigned` | `issueAssigned: {}` |
| Issue archived | `sentry_archived` | `issueArchived: {}` |
| Issue unresolved | `sentry_unresolved` | `issueUnresolved: {}` |
| Any issue event | `sentry_any` | `issueAny: {}` |

Optional `projectIds`.

**`webhook`** — skip specific-event; `webhook: {}`; user gets URL/auth after save.

---
