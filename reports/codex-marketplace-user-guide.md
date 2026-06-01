# Codex Marketplace — User Guide

*Your plain-English guide to `yikusiel-codex-marketplace` — what it is, what to install first, and how to use it for The Cards Guy, HY Credit / DisputeIQ, AI scheduling, app building, and creative work.*

---

## 1. Executive summary

**What this is.** `yikusiel-codex-marketplace` is your private plugin marketplace for Codex (and usable in Claude Code / other agents). It started as a fork of OpenAI's official marketplace and has been expanded with carefully-vetted external plugins.

**How big.** **254 plugins** — 147 official OpenAI plugins (vendored locally) + 107 external plugins added across curated waves. Every external plugin was checked: it has a real `.codex-plugin/plugin.json`, the manifest is reachable, it's not a broken stub, not a duplicate, and not high-risk.

**What it helps you do.** Humanized + expert writing, credit-card/finance research, SEO, fact-checking, website/app building (frontend, databases, auth, deploy), API discovery and integration, testing/QA/security, automation and scheduling, research, and creative image/video workflows.

**Install first.** A small zero-config set that's useful immediately and needs **no accounts** — see §2.

**Avoid installing until ready.** Anything that needs a paid account or API key (≈47 external plugins), powerful tools like `windows-computer-use` and `burpsuite-mcp-bridge`, and macOS-only tools (you're on Windows). Don't bulk-install — add account-heavy tools one at a time when you'll actually use them. See §7–8.

> **Golden rules:** never rename the marketplace (`yikusiel-codex-marketplace`) or move `.agents/plugins/marketplace.json`. Adding a plugin never logs you in — you only authenticate when you choose to install + use it.

---

## 2. Best plugins to install first

All zero-config, no account needed, broadly useful. Start here.

| Plugin | What it helps with | Why first | Account/API |
|---|---|---|---|
| `writers-loop` | Structured multi-stage writing (frame→draft→revise) | Your core writing engine | No |
| `unslop` | Strips "AI-sounding" wording | Makes copy read human | No |
| `claude-mem` | Persistent memory across sessions | Keeps context/cases | No |
| `pm-skills` | 63 product-management skills | Planning & roadmaps | No |
| `agentops` | Operational layer + 80+ workflow skills | Better agent runs | No |
| `session-orchestrator` | Plan→execute→review session flow | Quality-gated work | No |
| `microsoft-docs` | Search authoritative MS/Azure/.NET docs | Accurate dev answers | No |
| `citecheck` | Verify citations/sources exist & are relevant | Fact-checking | No |
| `github-librarian` | Research repos, SDKs, code | Find/evaluate tools | No |
| `codebase-recon` | Map a repo's hotspots before editing | Safer code changes | No |
| `brooks-lint` | Code review grounded in classic SE books | Higher code quality | No |
| `commit-narrator` | Clear commit messages from diffs | Cleaner git history | No |
| `gh-project-plugin` | GitHub project/issue management | Track work | No |
| `secret-guard` | Pre-commit secret scanner | Protects keys/PII | No |
| `env-lint` | Checks `.env` vs `.env.example` | Avoids config bugs | No |
| `test-gap` | Finds untested changed lines | QA before shipping | No |
| `mermaid-js-for-agents` | Diagrams from text | Docs & planning | No |
| `spreadsheet-peek` | Inspect spreadsheets/reporting | Quick data checks | No |

---

## 3. Best writing stack for The Cards Guy

Goal: **expert, humanized, factually-careful U.S. credit-card content.** The AI is your writer/editor — **not** your source of truth. Verify every number against issuer pages and reliable finance sources.

- **Humanized writing:** `writers-loop` (draft in your voice), `unslop` (remove AI tells — run last), `content-planner` (outline first).
- **Research:** `firecrawl` (scrape issuer/competitor pages — *needs a free-tier key*), `gpt-researcher` (multi-source synthesis), `github-librarian`; finance sources already in your marketplace: `dow-jones-factiva`, `factset`, `lseg`, `morningstar`, `quartr`, `cb-insights`, `aiera`, `daloopa`; save sources with `readwise`.
- **Fact-checking:** `citecheck` (sources exist + relevant), `scite` (citation strength), confirm figures via `factset`/`factiva`.
- **SEO:** `codex-seo`, `enterprise-frontend-seo`, `semrush`, `similarweb`.
- **Store/sync:** `google-drive`, `github`, `notion`; remember context with `claude-mem`.

**Editing workflow (page refresh):**
1. **Research facts first** — `firecrawl` the issuer page + 2–3 reliable sources; log each fact with its source.
2. **Verify** — `citecheck`/`scite`; confirm figures via `factset`/`factiva`; mark anything unconfirmed as **rumored**.
3. **Outline** — `content-planner` around user intent (eligibility, bonus, benefits, fees, who it's for).
4. **Draft** — `writers-loop` in your editorial voice.
5. **SEO pass** — `codex-seo` + `semrush`; apply only what truly helps.
6. **De-AI pass** — `unslop` (low/medium) to remove AI tells, preserve your voice.
7. **Final fact gate** — re-confirm every number against the issuer page; label confirmed vs rumored; keep affiliate links minimal + disclosed.

**Do NOT rely on for financial accuracy:** `unslop`, `writers-loop`, `codex-seo`, or any generic LLM output — they don't verify facts. Treat issuer pages + `factset`/`factiva`/`morningstar` as the source of truth.

**Style guardrails (put in your `writers-loop` prompt):** human expert tone · professional but readable · no generic AI wording · no filler · no fake certainty · **no made-up financial facts** · U.S. credit cards only · label confirmed vs rumored · issuer pages + reliable sources first · preserve your editorial style · avoid SEO fluff · avoid over-linking · tables only when they clarify.

*(Full detail: `reports/credit-card-writing-stack.md`.)*

---

## 4. Best API discovery & integration stack

There's no single "API finder" — this is a workflow built from real plugins.

- **Find APIs:** `github-librarian` (SDKs/repos), `microsoft-docs` (MS/Azure), `firecrawl` (scrape docs/pricing), `gpt-researcher` + `openai-developers`/`github` (compare).
- **Evaluate** (reliability · pricing · docs · auth · rate limits · webhooks · SDKs): pull each provider's docs with `firecrawl`; check SDK health with `github-librarian`; status/uptime with `checkly`.
- **Specific provider APIs:** `link` (payments), `twilio-developer-kit`/`sendgrid` (comms), `seam` (IoT/access), `drpc-agent-skills` (web3), `clerk-skills` (auth), `supabase`/`vercel`/`netlify`/`cloudflare` (platform).
- **Implement in Vite/React/Supabase/Vercel:** keys server-side only (Supabase Edge Function / Vercel function as proxy); typed client + retries; secrets via env, scanned with `secret-guard`, linted with `env-lint`.
- **Test/monitor/secure:** `checkly` (synthetic), `sentry`/`sentry-cli` (errors), `datadog` (APM), `stackhawk`/`zscaler-terraform-skills` (security), `llm-router` (route LLM APIs).

*(Full detail: `reports/api-discovery-and-integration-stack.md`. Not yet in marketplace — connect as MCP later: Tavily, Exa, Perplexity, Postman, Bruno.)*

---

## 5. Best website / app-building stacks

- **Frontend/UI:** `astro-codex-plugin`, `litestar`, `maquette` (image→components), `stark`, `universal-design-principles`, `mermaid-js-for-agents`, `figma`.
- **Backend/DB:** `supabase`, `convex`, `prisma`, `mongodb`, `couchbase-skills`, `valkey-skills`, `kurrent`, `documentdb`, `metabase`, `dataproduct-builder-dbt`.
- **Auth:** `clerk-skills`, Supabase Auth.
- **Deploy/infra:** `vercel`, `netlify`, `cloudflare`, `truefoundry`.
- **Testing/QA:** `test-gap`, `flaky-detector`, `env-lint`, `brooks-lint`, `codex-reviewer`, `spec-driven`.
- **Security:** `secret-guard`, `deps-doctor`, `stackhawk`, `fortify-skills`, `agentic-security`, `armorcodex`, `zscaler-terraform-skills`, `burpsuite-mcp-bridge`.
- **Monitoring/perf:** `checkly`, `sentry`/`sentry-cli`, `datadog`, `langfuse`.
- **SEO/content:** `codex-seo`, `enterprise-frontend-seo`, `semrush`, `content-planner`.

**Recommended stacks:**
- **The Cards Guy:** React/Vite + `supabase` (+`convex`/`prisma`) + `clerk-skills` + `vercel`; `codex-seo`+`semrush`+`content-planner`; `writers-loop`+`unslop`; `checkly`+`sentry`; `secret-guard`+`deps-doctor`+`stackhawk`.
- **HY Credit / DisputeIQ:** `supabase`/`prisma` (cases) + `clerk-skills`; `secret-guard`+`env-lint` (protect PII/keys); `google-drive`/`box` (documents); `writers-loop`+`unslop` (compliance-aware, FCRA-careful drafting); `claude-mem` (case memory); `codex-reviewer`+`test-gap` (QA). **Keep PII out of logs; verify every dispute claim.**
- **AI scheduling system:** `session-orchestrator`+`agentops`+`claude-mem`+`task-scheduler`; `n8n`/`n8n-mcp-synta-codex`; `google-calendar`+`gmail`+`notion`; `langfuse` (observe runs).
- **Creative:** `maquette`+`comfy-workflow-mcp` (local), then `pika`/`img`/`higgsfield` once accounts are set.

*(Full detail: `reports/website-app-building-stack.md`.)*

---

## 6. Creative — image / video / identity

**What you have now (installable):** `img` (image gen), `pika` (video/image suite), `higgsfield` (image+video + Soul ID identity), `comfy-workflow-mcp` (local ComfyUI), `roboflow`/`fiftyone-skills` (computer vision), `image-studio-mcp`, `codex-video-vision`, `aether`, `maquette`, `remotion`, `vidseeds`; plus fork `hyperframes` (HTML→MP4) and `heygen` (avatar video).

- **Image generation:** `img` (OpenAI gpt-image-2 + Gemini), `comfy-workflow-mcp` (local), `image-studio-mcp`.
- **Video generation:** `pika`, `higgsfield`, `remotion` (programmatic), fork `hyperframes`.
- **Identity consistency:** **`higgsfield` Soul ID is the best current path** (trains a face-faithful identity model, reusable across generations). `heygen` is great for avatar/presenter continuity. `comfy-workflow-mcp` lets you drive ControlNet/IP-Adapter locally.

**Honest gaps:**
- **No perfect Codex-native identity / height / body-continuity plugin exists** (re-confirmed every run).
- The closest dedicated toolkit, **`awesome-genmedia/skills`** (InstantID, IP-Adapter, PhotoMaker, ControlNet, LoRA, StoryDiffusion), is a **Claude-format plugin → would need wrapping** (see `reports/identity-video-wrapping-plan.md`).
- **Height / body-size continuity** has no off-the-shelf solution anywhere — it needs a custom skill (your approval).

*(Full detail: `reports/creative-identity-tools.md`.)*

---

## 7. Plugins that require accounts / API keys

Adding these to the marketplace is free and safe; you only authenticate when you install + use them. **Don't bulk-install.**

| Plugin(s) | Service / account | Install now or wait? |
|---|---|---|
| `firecrawl` | firecrawl.dev (free tier, no card) | OK now (free tier) |
| `langfuse`, `clerk-skills`, `sanity`, `mongodb`, `checkly` | respective free tiers | OK now (free tier) |
| `codex-seo` | DataForSEO + Firecrawl + Google AI (paid) | Wait |
| `link`, `dodopayments` | Stripe / Dodo accounts | Wait |
| `twilio-developer-kit`, `sendgrid` | Twilio account | Wait |
| `img`, `pika`, `higgsfield`, `aether`, `image-studio-mcp`, `codex-video-vision`, `roboflow`, `vidseeds` | image/video provider accounts/keys | Wait |
| `datocms`, `accelerate-ai-toolkit`, `spotify-ads-api`, `seam`, `drpc-agent-skills`, `alation`, `truefoundry`, `documentdb` | vendor accounts | Wait |
| `bkt`, `jk`, `forge-skills` | Atlassian/Jenkins creds | Wait |
| `gpt-researcher`, `llm-router` | an LLM API key (you likely have) | When needed |
| `metabase`, `dataproduct-builder-dbt`, `n8n` | self-hosted instance/warehouse | Wait |
| OpenAI-fork connectors (Gmail, Slack, Notion, Stripe, Supabase, Vercel, Semrush, FactSet, Factiva, Morningstar, …) | each service's OAuth | Per service, when used |

*(Full table: `reports/api-and-account-requirements.md`.)*

---

## 8. Do-not-install-yet list

Powerful or situational — wait until you're ready:
- **`windows-computer-use`** — controls your actual Windows desktop. Powerful; review first.
- **`burpsuite-mcp-bridge`** — security testing; needs local Burp Suite and care.
- **Account/API-heavy (Tier 8):** `dodopayments`, `spotify-ads-api`, `alation`, `accelerate-ai-toolkit`, `vpai`, `loops`, `crawlbase`, `armorcodex`, `axonflow`, `truefoundry`, `n8n`, etc.
- **macOS-only (you're on Windows):** `agent-vision`, `codex-obsidian`, `build-visionos-apps`.
- **Windows-unverified (test first):** `img`, `higgsfield`, `metabase`, `dataproduct-builder-dbt`, `codex-reviewer`, `armorcodex`, `axonflow`, `compound-engineering`, `sentry-cli`, `spotify-ads-api`, `alation`, `truefoundry`.

---

## 9. Full plugin dashboard

The complete, sortable list of all 254 plugins (category, source wave, install priority, account need, platform, risk) lives in:
- **`reports/plugin-dashboard.md`** — readable table.
- **`reports/plugin-dashboard.csv`** — open in Excel/Sheets to filter & sort.

**By source wave:** OpenAI fork 147 · External P1 7 · P2 19 · P3 60 · P4 (latest) 24.
**Biggest categories:** Productivity, Coding, Research, Database, Security, Design, Writing/Content/SEO, Image & Video, Data & Analytics, APIs.

**Companion guides in `reports/`:** `recommended-install-order.md` (9 tiers), `credit-card-writing-stack.md`, `api-discovery-and-integration-stack.md`, `website-app-building-stack.md`, `creative-identity-tools.md`, `api-and-account-requirements.md`, `cross-agent-next-actions.md`, `identity-video-wrapping-plan.md`, `cross-agent-skills-inventory.md`, `skill-wrapping-backlog.md`.
