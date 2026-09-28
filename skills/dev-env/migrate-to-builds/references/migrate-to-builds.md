# Migrate an environment to builds

Use this with SKILL.md for an explicitly requested environment-build migration. Resolve the available environment/build tools from the current catalog; exact commands and configuration fields come from their schemas or current official documentation.

1. Identify the target environment, repository revision, and effective configuration source. Prefer environment-info. Inspect `.cursor/environment.json` when present; a local checkout cannot prove which saved personal/team configuration a remote environment is using.
2. Read the effective install/start/terminals commands and relevant setup logs. Classify durable source-derived setup versus per-boot services according to SKILL.md. Record missing access or unknown remote configuration instead of inventing it.
3. Prepare the smallest requested change. Preserve unrelated settings and secrets; keep a recoverable copy. Repository-managed configuration is edited in the relevant checkout. Saved DB-managed configuration must use the host's supported draft/update mechanism, never a guessed database write.
4. Run static syntax and dependency checks before an expensive build. Confirm commands terminate where expected, are non-interactive, and can repeat safely. Do not execute deployment or production side effects as setup tests.
5. If an authorized build mechanism is available, build the candidate and inspect its real result. Then use a fresh agent/boot from that build for a smoke test of checkout state, dependencies, startup, and service readiness. A successful build alone does not prove per-boot startup.
6. Report the effective source, scoped changes, actual build/fresh-boot evidence, and unresolved limitations. Enabling builds remains a separate environment setting; do not claim it changed from editing files or preparing a build.

If build or fresh-agent tools are unavailable, deliver the inspected configuration and concrete proposed patch when possible, then identify the specific unavailable verification. Do not fabricate a build ID, environment URL, or successful migration.
