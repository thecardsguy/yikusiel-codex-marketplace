# yikusiel-codex-marketplace

My private Codex plugin marketplace — a curated fork of OpenAI's marketplace, extended with vetted external plugins for creative, coding, data, SEO, security, research, automation, and productivity workflows.

- **Marketplace name:** `yikusiel-codex-marketplace` — **do not rename it**, and do not move `.agents/plugins/marketplace.json` (Codex expects that exact path).
- **Add in Codex:** Plugins → add marketplace → `thecardsguy/yikusiel-codex-marketplace`.
- **Refresh after updates:** Plugins → `yikusiel-codex-marketplace` → reopen/refresh, then install a plugin with `+`.
- **Validate locally:** `python scripts/validate-marketplace.py` (add `--online` to verify every external manifest is reachable).
- **Reports:** see [`reports/`](reports/) — `marketplace-expansion-report.md` (what's added), `recommended-install-order.md` (install tiers), `creative-identity-tools.md` (image/video/identity), `candidate-backlog.md` (leads not yet added).

Existing OpenAI plugins are vendored under `plugins/` as `local` sources; external additions use `git-subdir`/`url` sources that point at upstream repos. Adding a plugin to the marketplace never authenticates it — credentials are entered only when you install + use it (`authentication: ON_INSTALL`).

## Start here

1. **Read the guide:** [`reports/codex-marketplace-user-guide.md`](reports/codex-marketplace-user-guide.md) (a `.docx` copy is alongside it).
2. **Open the tracker:** [`reports/codex-install-tracker.md`](reports/codex-install-tracker.md) — install order + a test prompt for each plugin.
3. **Install the first 15 only** (zero-config, no account): `writers-loop`, `unslop`, `claude-mem`, `pm-skills`, `agentops`, `session-orchestrator`, `microsoft-docs`, `citecheck`, `github-librarian`, `codebase-recon`, `brooks-lint`, `commit-narrator`, `secret-guard`, `env-lint`, `mermaid`.
4. **Do not bulk-install** API/account-heavy tools — add those one at a time, only when you'll use them.
5. **Follow the 5-day plan:** [`reports/first-week-codex-plugin-plan.md`](reports/first-week-codex-plugin-plan.md).

## How to use this marketplace

**New here? Start with the [Codex Marketplace User Guide](reports/codex-marketplace-user-guide.md)** (`reports/codex-marketplace-user-guide.md`) — plain-English: what to install first, the writing / API / app-building stacks, and which plugins need accounts. A `.docx` copy is in `reports/` too.

### Recommended first install (zero-config, no account, broadly useful)
`writers-loop`, `unslop`, `claude-mem`, `pm-skills`, `agentops`, `session-orchestrator`, `microsoft-docs`, `citecheck`, `github-librarian`, `codebase-recon`, `brooks-lint`, `commit-narrator`, `secret-guard`, `env-lint`, `mermaid`.

1. **Refresh in Codex:** Plugins → `yikusiel-codex-marketplace` → reopen/refresh → install any plugin with `+`.
3. **Don't bulk-install** the account/API-heavy plugins (Tier 8 in [`reports/recommended-install-order.md`](reports/recommended-install-order.md)). Add those one at a time, only when you'll use them — many need a paid account or API key.
4. **Browse everything:** [`reports/plugin-dashboard.md`](reports/plugin-dashboard.md) (or `.csv`) lists every plugin with category, install priority, account needs, platform, and risk. Focused guides: `credit-card-writing-stack.md`, `api-discovery-and-integration-stack.md`, `website-app-building-stack.md`, `creative-identity-tools.md`, `api-and-account-requirements.md`.
5. **Validate locally** after any edit: `python scripts/validate-marketplace.py` (add `--online` to confirm every external manifest resolves).
6. **Do not** rename the marketplace (`yikusiel-codex-marketplace`) or move `.agents/plugins/marketplace.json` — Codex depends on both.

---

# Plugins

This repository contains a curated collection of Codex plugin examples.

Each plugin lives under `plugins/<name>/` with a required
`.codex-plugin/plugin.json` manifest and optional companion surfaces such as
`skills/`, `.app.json`, `.mcp.json`, plugin-level `agents/`, `commands/`,
`hooks.json`, `assets/`, and other supporting files.

Highlighted richer examples in this repo include:

- `plugins/figma` for `use_figma`, Code to Canvas, Code Connect, and design system rules
- `plugins/notion` for planning, research, meetings, and knowledge capture
- `plugins/build-ios-apps` for SwiftUI implementation, refactors, performance, and debugging
- `plugins/build-macos-apps` for macOS SwiftUI/AppKit workflows, build/run/debug loops, and packaging guidance
- `plugins/build-web-apps` for deployment, UI, payments, and database workflows
- `plugins/expo` for Expo and React Native apps, SDK upgrades, EAS workflows, and Codex Run actions
- `plugins/netlify`, `plugins/remotion`, and `plugins/google-slides` for additional public skill- and MCP-backed plugin bundles
