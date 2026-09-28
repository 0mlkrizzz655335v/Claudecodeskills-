# Dedicated security-review reviewer

Use this reference only when that dedicated reviewer is available. The current tool schema controls invocation and supported retry behavior. Target checkout preparation and user authorization are governed by SKILL.md.

Use this exact prompt shape:

```text
Full Repository Path: <absolute repository path>
Diff: <one of: "branch changes", "uncommitted changes">
Base Branch: <only include this line when reviewing branch changes against a known specific base branch>
Custom Instructions: <only include this line when the user gave specific review instructions>
```

Default to `branch changes`, which reviews branch changes against the merge-base with the default/base branch, including committed, staged, and unstaged changes. If the user asks to review only uncommitted, local working tree, dirty, or not-yet-committed changes, use `uncommitted changes`.

If the review subagent fails before producing findings, inspect the failure text.

- If the failure is caused by calling the subagent incorrectly, such as a missing `Full Repository Path`, missing `Diff`, wrong prompt shape, or wrong subagent type, correct the invocation and retry it once immediately.
- For any other subagent failure, retry once with the same prompt shape.
- If the same failure persists after the retry, stop. Briefly tell the user that the review subagent could not complete and include the short error or blocker. Do not keep retrying.
