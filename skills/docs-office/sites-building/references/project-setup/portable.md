# Portable project setup

Hosted server code runs in Cloudflare Workers, with **128 MB of memory per isolate**, shared across concurrent requests and including JavaScript and WebAssembly allocations.

## Choose the checkout

For a new Site, create an empty project subdirectory inside the task's workspace, preserving existing files. For an existing Site, reuse the checkout from [Open a Site](../../../sites-hosting/SKILL.md#open-a-site). Run setup and authoring in that checkout.

## Prepare the source

- **Existing Site:** Preserve its package manager, lockfile, scripts, architecture, and binding names.
- **New starter:** Run `node <plugin-root>/scripts/project-setup.mjs`. It copies the bundled Vinext starter and configures the execution profile.
- **Static HTML:** Author and track `dist/index.html` and its assets, with `static.directory: "dist"` in `.openai/hosting.json`. Skip starter setup, profile configuration, installation, and builds. Check requested routes, local asset references, and JavaScript syntax once when applicable. Framework exports still require installation and builds.
- **Retained template:** Run `node <plugin-root>/scripts/project-setup.mjs --template-source <absolute-sanitized-source-directory>` in the empty checkout. Use a template without Site identity, Git metadata, credentials, or runtime data; preserve its structure.

## Install dependencies

For a project with `package.json`, run `node <plugin-root>/scripts/install-dependencies.mjs` when dependencies are missing or dependency inputs changed.

Begin application source work once files exist, while installation runs. Keep dependency inputs unchanged until it finishes, and use one installer at a time.
