# Marketplace Expansion Report — yikusiel-codex-marketplace

**Date:** 2026-05-31
**Repo:** `thecardsguy/yikusiel-codex-marketplace`
**Manifest:** `.agents/plugins/marketplace.json` (name `yikusiel-codex-marketplace` — unchanged)
**Method:** Aggressive discovery across `openai/plugins`, `openai/skills`, `hashgraph-online/awesome-codex-plugins`, and GitHub‑wide code search (1,138 `.codex-plugin/plugin.json` hits) → deep validation of ~49 candidates (stub‑detection, safety, API/platform flags, 1–10 scoring) → conservative adds (score ≥ 8, valid non‑stub, not high‑risk, no name collision, reachable manifest).

---

## 1. Plugin count — before & after

| | Count |
|---|---|
| Before | **154** |
| Added this run | **+19** |
| **After** | **173** |

JSON validated ✔ · No duplicate names ✔ · All 19 new manifests reachable (HTTP/gh‑api 200) ✔ · Diff = 263 insertions, 0 deletions, marketplace.json only ✔

---

## 2. Plugins added (19)

All added as `git-subdir` (subfolder) or `url` (repo‑root) sources; `authentication: ON_INSTALL` so nothing activates until you install + authorize it.

| Plugin | Category | Source | Score | API key | What it does |
|---|---|---|---|---|---|
| `writers-loop` | Writing | hashgraph `xxsang/writers-loop` | 9 | — | Multi‑stage writing loop (frame→plan→draft→critique→revise) with local style learning |
| `unslop` | Writing | hashgraph `MohamedAbdallah-14/unslop` | 8 | — | Strips AI‑isms from prose; humanizes output, preserves code |
| `brooks-lint` | Code Review | hashgraph `hyhmrright/brooks-lint` | 9 | — | Code review grounded in 12 classic SE books; Symptom→Source→Consequence→Remedy |
| `pr-storyteller` | Code Review | hashgraph `mturac/pr-storyteller` | 8 | — | Generates full PR descriptions from local git history + diff |
| `codebase-recon` | Coding | hashgraph `yujiachen-y/codebase-recon-skill` | 8 | — | Git‑history analysis: hotspots, bus factor, bug magnets — before reading code |
| `test-gap` | Testing & QA | hashgraph `mturac/test-gap` | 8 | — | Intersects git diff with coverage report to find untested changed lines |
| `env-lint` | Testing & QA | hashgraph `mturac/env-lint` | 8 | — | Diffs `.env` vs `.env.example` (key names only, never values) |
| `secret-guard` | Security | hashgraph `mturac/secret-guard` | 8 | — | Pre‑commit secret scanner (entropy + patterns), redacted output |
| `session-orchestrator` | Agent Orchestration | hashgraph `Kanevry/session-orchestrator` | 9 | — | Research‑plan‑execute‑close session lifecycle, quality‑gated waves |
| `agentops` | Agent Orchestration | hashgraph `boshu2/agentops` | 9 | — | Operational layer for coding agents; repo‑native session memory + 80+ skills |
| `claude-mem` | Memory & Context | `thedotmack/claude-mem` (root) | 9 | — | Persistent memory compression across agent sessions |
| `standup-gen` | Productivity | hashgraph `mturac/standup-gen` | 8 | — | Daily standup notes from git log across repos |
| `todo-harvest` | Productivity | hashgraph `mturac/todo-harvest` | 8 | — | Harvests TODO/FIXME/HACK with git‑blame author + age |
| `pm-skills` | Project Management | `product-on-purpose/pm-skills` (root) | 9 | — | 63 product‑management skills across the full lifecycle |
| `convex` | Developer Tools | `openai/plugins` `plugins/convex` | 8 | — | Official: add a reactive, type‑safe Convex backend to JS/TS apps |
| `maquette` | Design | `Ixe1/codex-plugins` `plugins/maquette` (master) | 8 | — | Image‑guided web design: brand boards → coded HTML/CSS components + tokens |
| `shopify-plugin` | Tools & Integrations | `Shopify/Shopify-AI-Toolkit` (root) | 9 | — | Official Shopify: Admin/Storefront GraphQL, Liquid, Functions, Hydrogen |
| `langfuse` | Analytics | hashgraph `avivsinai/langfuse-mcp` | 9 | **Yes** | LLM observability — query traces/sessions/prompts via Langfuse |
| `dodopayments` | Finance | hashgraph `dodopayments/dodo-agent-plugin` | 9 | Optional | Official Dodo Payments: checkout, subscriptions, billing, webhooks |

---

## 3. Plugins skipped (broken / unsafe / irrelevant)

| Plugin | Reason |
|---|---|
| `codex-mem` (`2kDarki/codex-mem`) | **Stub** — score 3; placeholder manifest, not a working bundle. (`claude-mem` was added instead for memory.) |
| `prompt-to-asset` (`MohamedAbdallah-14/prompt-to-asset`) | **Stub** (from prior run) — entry points to a nonexistent build artifact. Still excluded. |
| `compass-defi` (`CompassLabs/compass-agent-skill`) | Real but **out of scope** — crypto/DeFi (Aave, Morpho); score 5. |

---

## 4. Candidates for later (real & useful, but need auth / setup / review)

Add these after verifying credential setup and (where noted) Windows compatibility. Listed strongest‑first.

**Creative / image / video (top priority for your creative work):**
| Plugin | Repo | Why later |
|---|---|---|
| `nyldn/img` | `nyldn/img` | **Real image generation** (OpenAI gpt‑image‑2 + Gemini). The genuine replacement for the broken prompt‑to‑asset. Needs OPENAI_API_KEY/GEMINI_API_KEY; brand‑new (0 stars), Windows untested. |
| `higgsfield-ai/skills` | `higgsfield-ai/skills` | **Image + video gen, 30+ models**, plus **Soul ID = face‑consistent identity** (closest real thing to your identity‑consistency goal). Needs paid Higgsfield account + interactive CLI login + curl‑piped install. |
| `aether` | `shawnxie94/aether` | Visual memory + prompt refinement for image gen. Needs API setup. |

**SEO / data / research (high value for The Cards Guy):**
| Plugin | Repo | Why later |
|---|---|---|
| `codex-seo` | hashgraph `BestLemoon/codex-seo` | 19‑skill full‑site SEO audit suite. Needs **DataForSEO + Firecrawl + Google AI** (paid). Excellent once accounts are set. |
| `metabase` | `metabase/metabase-codex-plugin` | Official Metabase BI/analytics. Needs a Metabase instance. |
| `codex-autoresearch` | `TheGreenCedar/codex-autoresearch` | Optimization/research loops (546⭐). |
| `papersflow` | hashgraph `papersflow-ai/...` | Hosted research workflows (API). |
| `dataproduct-builder-dbt` | hashgraph `entropy-data/...` | dbt data‑product builder (API/warehouse). |

**Dev / code / CI / security:**
`codex-reviewer`, `commit-narrator`, `changelog-forge`, `flaky-detector`, `deps-doctor`, `armorcodex` (API), `context-pack`, `spec-driven`, `bitbucket-cli` (API), `jenkins-cli` (API), `axonflow` (governance, API).

**Productivity / PM / automation:**
`task-scheduler`, `gh-project-plugin`, `project-autopilot`, `n8n-mcp-synta`, `base44-skills` (API).

**Platform‑restricted (macOS‑only — you're on Windows):**
`codex-obsidian` (`greg-asher/codex-obsidian`), `visionos-apps` (`studiomeije/visionos-codex-plugin`).

---

## 5. Broken / stub packages found
- `MohamedAbdallah-14/prompt-to-asset` — stub, dead entry path.
- `2kDarki/codex-mem` — stub manifest (score 3).
- `tmchow/tmc-marketplace`, `OutlineDriven/odin-codex-plugin`, `angristan/codex-wakatime` — no `.codex-plugin/plugin.json` at a resolvable path (not directly addable).

---

## 6. Claude‑only / loose‑skill packages (useful later, need wrapping for Codex)
| Repo | Type | Note |
|---|---|---|
| `openai/skills` | 44 loose `SKILL.md` | Official Codex **skills catalog** — consumed as skills, not marketplace plugins; no `.codex-plugin/plugin.json`. |
| `awesome-genmedia/skills` | Claude plugin (`.claude-plugin`) | **Closest real identity/character toolkit** — wraps InstantID, IP‑Adapter, PhotoMaker, ControlNet, FLUX LoRA, face‑swap, StoryDiffusion via eachlabs.ai. Would need Claude→Codex wrapping. |
| `hunix/HoC-Republic` | Proprietary `hoc.plugin.json` | MagicAnimate/OmniGen/StoryDiffusion/FaceFusion/DeepFaceLab — experimental, 0 stars, not Codex format. Treat with caution. |

> Note: `obra/superpowers` and HeyGen `hyperframes` are **already in your marketplace** (vendored as `local` plugins by the OpenAI fork), so they were not re‑added.

---

## 7. Identity / height / body / character‑consistency findings
**Honest finding: there is NO real, packaged Codex plugin (`.codex-plugin/plugin.json`) for identity preservation, face identity, portrait/character consistency, body/height/scale continuity, same‑person video, pose control, ControlNet, IP‑Adapter, InstantID, PuLID, LoRA, or ComfyUI character workflows.** (Exhaustive `gh search code` / `gh search repos` / tree inspection, May 2026.)

Closest real, installable options (none are Codex‑native):
- **`higgsfield-ai/skills` → Soul ID** — trains a face‑faithful identity model usable across generations. Real plugin, but candidate‑later (paid account, CLI login). **This is the most practical near‑term path to identity consistency.**
- **`awesome-genmedia/skills`** — Claude‑format; wraps InstantID/IP‑Adapter/PhotoMaker/StoryDiffusion. Would need wrapping.

A bespoke identity‑lock / height‑lock / body‑continuity skill remains a **custom build** (you asked me not to create custom skills yet — flagged for your approval when you're ready).

---

## 8. Plugins requiring API keys / accounts
- **Added:** `langfuse` (LANGFUSE_PUBLIC_KEY / SECRET_KEY / HOST — free tier available); `dodopayments` (browser OAuth by default; optional DODO_API_KEY).
- **Candidates:** `codex-seo` (DataForSEO + Firecrawl + Google AI), `nyldn/img` (OpenAI/Gemini), `higgsfield` (Higgsfield account), `aether`, `papersflow`, `armorcodex`, `axonflow`, `dataproduct-builder-dbt`, `bitbucket-cli`, `jenkins-cli`, `base44`.
- **No key needed (added):** the other 17, incl. all writing/QA/security/git/memory/PM/convex/maquette/shopify.

## 9. macOS‑only
- **Added:** none.
- **Candidates:** `codex-obsidian`, `visionos-apps`. (Also note `agent-vision`, already in your marketplace, is macOS‑only.)

## 10. Windows‑friendly
- **Confirmed Windows‑OK (added):** writers-loop, unslop, brooks-lint, pr-storyteller, codebase-recon, test-gap, env-lint, secret-guard, standup-gen, todo-harvest, claude-mem, pm-skills, convex, maquette, shopify-plugin, langfuse, dodopayments (17).
- **Likely cross‑platform, Windows unverified (added):** `session-orchestrator`, `agentops` (Node‑based; test before relying on them).

---

## 11. Most useful for your businesses

**The Cards Guy (credit‑card content/tools):** `writers-loop`, `unslop` (content polish) · `maquette` (landing pages/visual) · `pm-skills` (roadmap) · later: `codex-seo`, `nyldn/img`.

**HY Credit / DisputeIQ (credit‑repair automation):** `writers-loop` + `unslop` (dispute letters) · `secret-guard` (avoid leaking PII/keys) · `session-orchestrator` + `agentops` (automation workflows) · `dodopayments` (billing) · `claude-mem` (case context).

**AI scheduling / workflow automation:** `session-orchestrator`, `agentops`, `claude-mem`, `langfuse` (observe your AI runs) · later: `task-scheduler`, `n8n-mcp-synta`.

**Medical / family coordination:** `pm-skills`, `standup-gen`, `todo-harvest`, `claude-mem` (durable context) · later: `codex-obsidian` (macOS only).

**Creative image/video:** `maquette` (added) · later: `nyldn/img` (image gen), `higgsfield` (image+video + Soul‑ID identity). HeyGen `hyperframes` (HTML→MP4) is already in your marketplace.

**Web apps / engineering (all businesses):** `convex` (backend), `brooks-lint` + `pr-storyteller` + `codebase-recon` + `test-gap` + `env-lint` (code quality/QA), `shopify-plugin` (if you ever run a store).

---

## 12. Recommended install order in Codex
1. **Tier 1 — zero‑config, broadly useful (install first):** `writers-loop`, `unslop`, `brooks-lint`, `pr-storyteller`, `codebase-recon`, `secret-guard`, `claude-mem`, `pm-skills`, `agentops`, `session-orchestrator`, `standup-gen`, `todo-harvest`, `test-gap`, `env-lint`.
2. **Tier 2 — light setup / project‑specific:** `convex`, `maquette`, `shopify-plugin`.
3. **Tier 3 — needs an account/keys:** `langfuse` (Langfuse keys), `dodopayments` (Dodo OAuth).

In Codex: **Plugins → `yikusiel-codex-marketplace` → reopen/refresh → install each with `+`.**

---

## 13. Recommended next phase
1. **Creative pipeline:** test `nyldn/img` (image gen) and `higgsfield` (image+video + **Soul‑ID identity**) in a scratch project; verify API‑key setup + Windows behavior, then promote to add‑now.
2. **SEO for The Cards Guy:** provision DataForSEO + Firecrawl + Google AI, then add `codex-seo`.
3. **Identity/character consistency:** decide between (a) adopting Higgsfield Soul‑ID, (b) wrapping `awesome-genmedia/skills` (Claude→Codex), or (c) approving a **custom skill** build. No ready‑made Codex plugin exists.
4. **Maintenance:** re‑scan `openai/plugins` + `hashgraph-online/awesome-codex-plugins` periodically for new bundles (this run already syncs you to current official set, minus `convex` which is now added).
5. Optionally promote the strongest dev/CI candidates (`codex-reviewer`, `deps-doctor`, `commit-narrator`) once you confirm `gh`/CI auth in your Codex environment.
