# Mermaid Plugin — Failure Report

## What failed
Installing `mermaid-js-for-agents` (15th of the first batch) failed in Codex; the other 14 installed fine.

## Diagnosis (Category A — broken marketplace entry)
- **Marketplace entry valid?** Structurally yes — single entry, `url` source → `henryennis/mermaid-js-for-agents`, ref `main`, no duplicate.
- **Manifest reachable?** Yes — `.codex-plugin/plugin.json` returns HTTP 200 and is valid JSON; `skills/` exists with real content.
- **UI/install issue or source issue?** Neither network nor UI — it's a **name mismatch in the marketplace entry.**

**Root cause:** the marketplace entry was named **`mermaid-js-for-agents`**, but the plugin's own manifest declares **`name: "mermaid-js-for-agents"`**. Codex resolves a plugin by matching the marketplace entry name to the plugin's manifest name, so it couldn't install `mermaid-js-for-agents`.

**Evidence (decisive):** I compared entry-name vs manifest-name for all 15. All **14 that installed** have entry name == manifest name. **`mermaid-js-for-agents` was the only mismatch — and the only failure.** One-to-one correlation.

## Fix applied
✅ Renamed the marketplace entry `mermaid` → **`mermaid-js-for-agents`** (now matches the plugin's manifest). Source/ref unchanged and still reachable. Validated: JSON valid, no duplicates, `--online` OK.

## Your next steps
1. **Refresh Codex:** Plugins → `yikusiel-codex-marketplace` → reopen/refresh (so it picks up the rename).
2. **Retry install** — it now appears as **`mermaid-js-for-agents`** (not `mermaid-js-for-agents`). Install that.
3. **Test:** "Create a Mermaid architecture diagram (flowchart TD) for a React/Vite + Supabase + Vercel site."
- **Retry install?** Yes — under the new name after refreshing.
- **Refresh/reopen Codex?** Yes — required to see the rename.
- **Skip Mermaid?** Not necessary. (Note: Codex/Claude can already render Mermaid in chat; this plugin just adds diagram skills/guidance — low-stakes if you skip.)
- **Replacement needed?** No — the plugin is fine; only the entry name was wrong.

---

## ⚠️ Systemic finding — 37 entries had the same bug → ✅ 34 fixed
The mismatch wasn't unique to Mermaid. I audited **all 110 external entries**: **37 had entry-name ≠ manifest-name** and would fail to install. **You approved "full cleanup," so I renamed 33 of them + `mermaid-js-for-agents` (34 total) to match their manifests, and re-pointed `kurrent`.** **3 were left as-is** (collisions / risky name — see "Applied" below). The full original list (✅ = renamed):

| Entry (current) | Should be (manifest name) |
|---|---|
| accelerate-wp | accelerate-ai-toolkit |
| adsense-readiness | arb |
| arxiv | @cyanheads/arxiv-mcp-server |
| astro | astro-codex-plugin |
| atlassian-forge | forge-skills |
| azure-documentdb | documentdb |
| bitbucket-cli | bkt |
| browser-bridge | browserbridge |
| burpsuite-bridge | burpsuite-mcp-bridge |
| clerk | clerk-skills |
| comfy-workflow | comfy-workflow-mcp |
| computer-use-windows | windows-computer-use |
| couchbase | couchbase-skills |
| digital-marketing | digital-marketing-pro |
| drpc | drpc-agent-skills |
| enterprise-seo | enterprise-frontend-seo |
| fiftyone | fiftyone-skills |
| fortify | fortify-skills |
| image-studio | image-studio-mcp |
| jenkins-cli | jk |
| n8n-codex | n8n |
| n8n-mcp-synta | n8n-mcp-synta-codex |
| nyldn-img | img |
| papersflow | papersflow-codex-plugin |
| project-autopilot | codex-project-autopilot |
| remotion-external | remotion |
| spotify-ads | spotify-ads-api |
| stripe-link | link |
| tradingview | tradingview-mcp |
| twilio-dev-kit | twilio-developer-kit |
| valkey | valkey-skills |
| vibeprospecting | vpai |
| video-vision | codex-video-vision |
| visionos-apps | build-visionos-apps |
| wshobson-agents | developer-essentials |
| zscaler | zscaler-terraform-skills |

> Note: several manifest names are generic (`img`, `link`, `bkt`, `jk`, `arb`, `vpai`, `n8n`, `documentdb`). The entries now use those exact names (required for install resolution) — functional but less pretty. They install correctly.

### Separate issue — `kurrent` (Category D) — ✅ FIXED
`kurrent`'s upstream (`kurrent-io/skills`) moved its manifest from the repo root to `plugins/kurrent/`. ✅ Re-pointed the entry to a `git-subdir` source (`kurrent-io/skills`, path `plugins/kurrent`, ref `main`); its manifest name `kurrent` already matches. `--online` now passes.

### ✅ Applied (full cleanup — you approved)
Renamed 33 entries + `mermaid` → `mermaid-js-for-agents` (34 total) to match their manifests; re-pointed `kurrent`. Then **removed the 3 remaining problem entries**. Validated: JSON valid, no duplicates, offline + `--online` PASS. Marketplace is now **254 plugins**.

**The 3 exceptions — ✅ RESOLVED (removed):**
- **`arxiv`** — its manifest name `@cyanheads/arxiv-mcp-server` (contains `/` + `@`) is unsafe as a marketplace entry name → **removed** (candidate for a wrapper later).
- **`remotion-external`** — duplicated the existing **local** `remotion` plugin → **removed**. (Local `remotion` kept.)
- **`twilio-dev-kit`** — duplicated the existing **local** `twilio-developer-kit` plugin → **removed**. (Local `twilio-developer-kit` kept.)

See `reports/plugin-rename-map.md` for the full old→new map and the removals.

### Docs note — ✅ refreshed
All reports, trackers, and the README were refreshed to the corrected names (e.g. `mermaid` → `mermaid-js-for-agents`), and the dashboard was regenerated for the 254-plugin marketplace.
