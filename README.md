# yikusiel-codex-marketplace

My private Codex plugin marketplace — a curated fork of OpenAI's marketplace, extended with vetted external plugins for creative, coding, data, SEO, security, research, automation, and productivity workflows.

- **Marketplace name:** `yikusiel-codex-marketplace` — **do not rename it**, and do not move `.agents/plugins/marketplace.json` (Codex expects that exact path).
- **Add in Codex:** Plugins → add marketplace → `thecardsguy/yikusiel-codex-marketplace`.
- **Refresh after updates:** Plugins → `yikusiel-codex-marketplace` → reopen/refresh, then install a plugin with `+`.
- **Validate locally:** `python scripts/validate-marketplace.py` (add `--online` to verify every external manifest is reachable).
- **Reports:** see [`reports/`](reports/) — `marketplace-expansion-report.md` (what's added), `recommended-install-order.md` (install tiers), `creative-identity-tools.md` (image/video/identity), `candidate-backlog.md` (leads not yet added).

Existing OpenAI plugins are vendored under `plugins/` as `local` sources; external additions use `git-subdir`/`url` sources that point at upstream repos. Adding a plugin to the marketplace never authenticates it — credentials are entered only when you install + use it (`authentication: ON_INSTALL`).

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
