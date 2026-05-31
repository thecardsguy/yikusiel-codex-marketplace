# Recommended Install Order (in Codex)

In Codex: **Plugins → `yikusiel-codex-marketplace` → reopen/refresh → install each with `+`.**
Plugins marked **🔑** need an API key / account / OAuth *when you use them* (adding/installing the listing is free; you'll be prompted on first use). Plugins marked **🍎 macOS** or **🪟 Windows** are platform-specific.

## Tier 1 — Install first (zero-config, broadly useful)
`writers-loop`, `unslop` (content polish) · `claude-mem`, `context-pack` (memory) · `pm-skills`, `agentops`, `session-orchestrator` (workflow/PM) · `standup-gen`, `todo-harvest`, `task-scheduler` (productivity) · `codebase-recon`, `wshobson-agents` (coding) · `mermaid` (diagrams) · `spreadsheet-peek` (reporting).

## Tier 2 — Coding & quality tools
`brooks-lint`, `codex-reviewer`, `pr-storyteller`, `commit-narrator`, `changelog-forge` (review/git) · `test-gap`, `flaky-detector`, `env-lint` (testing/QA) · `secret-guard`, `deps-doctor` (security hygiene) · `spec-driven`, `compound-engineering` (methodology) · `gh-project-plugin`, `project-autopilot` (project automation).

## Tier 3 — Business / content / SEO
`enterprise-seo`, `digital-marketing`, `adsense-readiness`, `content-planner`, `linkedin-skills` · `shopify-plugin` · `superhuman-mail` · 🔑 `codex-seo`, `vibeprospecting`, `loops`.

## Tier 4 — Creative / image / video
`maquette`, `remotion-external`, `stark`, `universal-design-principles`, `fiftyone` · `comfy-workflow` (needs local ComfyUI) · 🔑 `pika`, `nyldn-img`, `higgsfield` (Soul ID identity), `aether`, `image-studio`, `video-vision`, `roboflow`, `vidseeds`.

## Tier 5 — Install only when you have the account / API key
🔑 **Data/DB/infra:** `metabase`, `dataproduct-builder-dbt`, `mongodb`, `sanity`, `clerk`, `prisma`, `base44`, `convex`, `checkly`, `bitbucket-cli`, `jenkins-cli`, `atlassian-forge`.
🔑 **Security:** `stackhawk`, `fortify`, `armorcodex`, `axonflow`.
🔑 **Research/observability:** `gpt-researcher`, `papersflow`, `sentry-cli`, `langfuse`, `crawlbase`.
🔑 **Finance/commerce:** `dodopayments`.

## Tier 6 — Optional / platform-specific
🍎 **macOS only:** `agent-vision`, `codex-obsidian`, `visionos-apps`.
🪟 **Windows-oriented:** `computer-use-windows` (computer use), `kachilu-browser` (WSL2 Chrome).
**Windows-unverified (test first):** `nyldn-img`, `higgsfield`, `metabase`, `dataproduct-builder-dbt`, `codex-reviewer`, `armorcodex`, `axonflow`, `compound-engineering`, `sentry-cli`.

## Suggested starting set for your businesses
- **The Cards Guy (content/SEO):** `writers-loop`, `unslop`, `content-planner`, `adsense-readiness`, `enterprise-seo`, then 🔑 `codex-seo`.
- **HY Credit / DisputeIQ:** `writers-loop`, `unslop`, `secret-guard`, `session-orchestrator`, `agentops`, `claude-mem`.
- **AI scheduling / automation:** `session-orchestrator`, `agentops`, `task-scheduler`, `n8n-mcp-synta`, 🔑 `langfuse`.
- **Creative:** `maquette`, `comfy-workflow`, then 🔑 `nyldn-img` / `pika` / `higgsfield`.
