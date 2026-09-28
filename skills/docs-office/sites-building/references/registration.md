# Site registration

Use native `create_site` in the Site-owning task. Reuse an existing `project_id` or registration attempt. Registration leaves the Site private and unpublished.

1. Start one registration call. When retained `functions.exec` cells are available, use its own cell with `// @exec: {"yield_time_ms": 1000}`, keeping installation and unrelated reads separate. Await the native call inside that cell and continue authoring while it runs. Otherwise await the native call normally.
2. On success, retain the returned Site `id` and source credential in session memory under a Site-specific key, then await this command in the project directory:

   ```text
   node <plugin-root>/scripts/set-project-id.mjs --project-id <returned-id>
   ```

   The helper preserves the manifest's other fields and atomically saves the identity. Return its result; keep the credential in memory.
3. Collect that registration cell before further manifest edits or opening the checkout. Use `functions.wait` for a returned running-cell ID.

Resume the same Site or registration attempt. Resolve an uncertain creation outcome before starting another registration.
