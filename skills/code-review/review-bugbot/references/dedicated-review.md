# Dedicated bugbot reviewer

Use this reference only when that dedicated reviewer is available. The current tool schema controls invocation and supported retry behavior. Target checkout preparation and user authorization are governed by SKILL.md.

Use this exact prompt shape:

```text
Full Repository Path: <absolute repository path>
Diff: <one of: "branch changes", "uncommitted changes", "natural language">
Base Branch: <only include this line when reviewing branch changes against a known specific base branch>
Change Description: <required only when Diff is "natural language"; list each changed file and what changed in it>
Custom Instructions: <only include this line when the user gave specific review instructions>
```

Default to `branch changes`, which reviews branch changes against the merge-base with the default/base branch, including committed, staged, and unstaged changes. If the user asks to review only uncommitted, local working tree, dirty, or not-yet-committed changes, use `uncommitted changes`.

If the review subagent fails before producing findings, inspect the failure text.

- If the failure is caused by calling the subagent incorrectly, such as a missing `Full Repository Path`, missing `Diff`, wrong prompt shape, or wrong subagent type, correct the invocation and retry it once immediately.
- If the subagent reports it could not compute the diff (for example an empty diff, missing diff metadata, or that it could not compute the diff), retry once with `Diff: natural language`, omitting `Base Branch` and providing a `Change Description`. The subagent will read those files directly. Only use this as a last resort, after the regular diff-based review has failed because the diff could not be computed.

  Write the `Change Description` as one block per changed file: a `<path> (added|modified|deleted|renamed)` header followed by bullet points of what changed. Mention line numbers or ranges inline where they help and you know them (for example `(L40-58)` or `around L120`); they are optional, not required on every bullet. Example:

  ```text
  src/auth/login.ts (modified):
  - rewrote validateSession (L40-58) to check token expiry before the DB lookup
  - removed the fallback that accepted empty tokens

  src/auth/legacy.ts (deleted)

  src/auth/mfa.ts (added):
  - new verifyMfaCode() (L1-30) that calls the TOTP service and rate-limits attempts
  ```
- For any other subagent failure, retry once with the same prompt shape.
- If the same failure persists after the retry, stop. Briefly tell the user that the review subagent could not complete and include the short error or blocker. Do not keep retrying.
