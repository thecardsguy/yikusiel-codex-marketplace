# Marketplace Expansion Report — yikusiel-codex-marketplace

**Repo:** `thecardsguy/yikusiel-codex-marketplace` · **Manifest:** `.agents/plugins/marketplace.json` (name `yikusiel-codex-marketplace`, unchanged)

## Run history
| Run | Commit | Plugins | Note |
|---|---|---|---|
| Base (OpenAI fork) | `f1dae33`/`4601603` | 147 | local OpenAI plugins |
| Run 1 (creative/visual) | `e4af80b` | 154 | +7 external |
| Run 2 (curated zero-config) | `ef79943` | 173 | +19 |
| **Run 3 (this run — big menu)** | **this commit** | **233** | **+60** |

## This run: 173 → 233 (+60 added, 5 already-covered, 1 stub skipped)
Adding rule relaxed per your instruction: a plugin is added if it has a valid non-stub `.codex-plugin/plugin.json`, a reachable manifest, a real useful purpose, and is not high-risk — **even if it needs an API key / account / OAuth later, is niche, or is Windows-unverified.** Nothing is authenticated or activated; entries use `authentication: ON_INSTALL`.

Validation: JSON valid ✔ · no duplicate names ✔ · all 60 new manifests reachable (gh-api 200) ✔ · `scripts/validate-marketplace.py` passes (offline + `--online`).

### Added this run, by category

**Creative · image · video · vision (8)**
`nyldn-img` (OpenAI gpt-image-2 + Gemini image gen — API), `higgsfield` (image+video, 30+ models, **Soul ID identity** — account), `aether` (visual memory/prompt refine — API), `pika` (Pika video/creative suite — OAuth), `comfy-workflow` (ComfyUI workflow mgmt — local ComfyUI), `roboflow` (computer vision pipelines — API), `fiftyone` (CV dataset/eval), `image-studio` (image editing — API), `video-vision` (video review — API).

**SEO · marketing · content (6)**
`codex-seo` (19-skill SEO audit — DataForSEO/Firecrawl/Google), `enterprise-seo`, `digital-marketing`, `adsense-readiness` (AdSense readiness — useful for credit-card content monetization), `content-planner` (API), `linkedin-skills`.

**Database · backend · web · CMS · auth (4)**
`prisma` (ORM, official), `mongodb` (official — API), `sanity` (CMS, official — API), `clerk` (auth, official — API), `base44` (full-stack apps — API). *(`supabase`, `motherduck` already covered.)*

**Data · BI · monitoring · spreadsheets (5)**
`metabase` (BI — needs instance), `dataproduct-builder-dbt` (dbt — API), `checkly` (monitoring, official — API), `sentry-cli` (errors — account), `spreadsheet-peek` (spreadsheets/reporting).

**Security (4)**
`stackhawk` (DAST, official — API), `fortify` (official — API), `agentic-security`, `armorcodex` (API).

**Research (4)**
`gpt-researcher` (popular research agent — API), `arxiv`, `codex-autoresearch` (546⭐), `papersflow` (API).

**Sales · CRM · email (3)**
`vibeprospecting` (Explorium — API), `loops` (email, official — API), `superhuman-mail` (Superhuman). *(`zoominfo`, `egnyte` already covered.)*

**Automation · browser · scraping (5)**
`computer-use-windows` (computer use on Windows), `browser-bridge`, `crawlbase` (scraping — API), `gsearch` (Google search), `n8n-mcp-synta` (n8n automation).

**Code · CI · QA · dev (13)**
`codex-reviewer`, `commit-narrator`, `changelog-forge`, `flaky-detector`, `deps-doctor`, `spec-driven`, `bitbucket-cli` (API), `jenkins-cli` (API), `compound-engineering` (API), `wshobson-agents`, `atlassian-forge` (official — API), `mermaid`, `context-pack`.

**Productivity · PM (5)**
`task-scheduler`, `gh-project-plugin`, `project-autopilot`, `axonflow` (governance — API), `codex-obsidian` (**macOS-only**).

**Platform-specific (1)**
`visionos-apps` (**macOS-only**, visionOS dev — API).

### Already-covered (skipped — official versions already in the OpenAI fork)
**5 skipped:** `heygen`, `supabase`, `motherduck`, `zoominfo`, `egnyte`. The community/duplicate versions were dropped because the marketplace already contains these services. (`mongodb` was *not* a collision and **was** added.)

### Skipped — broken
`evillollive/Analyze-Video-Skill` — has a `.codex-plugin/plugin.json` but it is a **stub** (score 5). Not added.

## Cumulative state (233 plugins)
- **147** local OpenAI plugins (the fork) · **86** external (`git-subdir` + `url`)
- Run `python scripts/validate-marketplace.py` for the live category/source breakdown.

## API keys / accounts
~30 of the 60 added require an API key, OAuth, or paid account **at install/use time** (not now). See `reports/recommended-install-order.md` (Tier 5) and `reports/candidate-backlog.md` for the exact list. None require credentials to merely appear in the marketplace.

## Platform
- **macOS-only (2 added):** `codex-obsidian`, `visionos-apps` — install only on macOS.
- **Windows-unverified (added):** `nyldn-img`, `higgsfield`, `metabase`, `dataproduct-builder-dbt`, `codex-reviewer`, `armorcodex`, `axonflow`, `compound-engineering`, `sentry-cli` — likely cross-platform, test before relying on them.
- All other added plugins report Windows-compatible.

## Related reports
- `reports/recommended-install-order.md` — tiered install plan.
- `reports/creative-identity-tools.md` — image/video/identity deep-dive + honest identity finding.
- `reports/candidate-backlog.md` — 570+ discovered repos not yet validated + what's needed to add them.

## Next phase
1. Validate the highest-value backlog repos (official orgs: `datocms`, `couchbaselabs`, `avifenesh/valkey-skills`, `kurrent-io`, `litestar-org`, `spotify/ads-agentic-tools`, `Azure/documentdb-agent-kit`, GCP extensions) and promote.
2. Identity/character consistency: still no dedicated Codex plugin — best real paths are `higgsfield` Soul ID and `heygen` avatars (both now installable). A bespoke identity-lock skill remains a custom build (your approval needed).
3. When ready, authorize accounts for the Tier-5 (API/paid) plugins you actually want to use.
