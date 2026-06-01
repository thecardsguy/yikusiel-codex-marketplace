# Next Technical Phase — Plan (do NOT implement without approval)

Two optional tracks for after you've installed and tested the first batch. **Nothing here is built, connected, or authenticated.** Each needs your go-ahead.

---

## Track A — Research / search MCP setup

These are **MCP servers**, not marketplace plugins — you connect them in your Codex MCP config, not via `+`. They make research far stronger for The Cards Guy.

| Tool | What it does | Why it matters | Account/API |
|---|---|---|---|
| **Tavily** (`tavily-ai/tavily-mcp`) | Agent-optimized web search | Fast, structured search for card facts, competitor pages, content gaps | Tavily API key (free tier) |
| **Exa** (`exa-labs/exa-mcp-server`) | Neural/semantic search | Finds primary finance sources by meaning, not just keywords | Exa API key |
| **Perplexity** (Perplexity MCP) | Answer engine with citations | Quick sourced answers during fact-checking | Perplexity API key |
| **Firecrawl** (already a plugin: `firecrawl`) | Scrape/crawl pages | Pull exact text from issuer & competitor pages | Firecrawl key (free tier) |

**How they improve Cards Guy research:** issuer-page extraction (Firecrawl) + broad discovery (Tavily) + semantic source-finding (Exa) + cited quick answers (Perplexity) = faster, better-sourced drafts and stronger fact-checking.

**Safest setup order:**
1. **`firecrawl`** first — it's already in the marketplace; just add its free-tier key when you use it.
2. **Tavily MCP** — biggest research win, free tier, low effort.
3. **Exa MCP** — when you want deeper semantic search.
4. **Perplexity MCP** — last; nice-to-have for cited answers.

**Do not connect yet:** anything requiring a paid plan you won't use this month; any MCP server from an unknown publisher. Keep all keys in env/secret storage — never in the repo.

---

## Track B — Identity / video skill wrapping

Goal: same-person identity, face consistency, and (hardest) body/height/scale continuity. Full detail in `reports/identity-video-wrapping-plan.md`; this is the decision summary.

**What you can do with existing plugins (no build):**
- **`higgsfield` Soul-ID** — best current path to same-person/face consistency (trained identity model, reused across shots). *Paid Higgsfield account.*
- **`heygen`** — avatar/presenter continuity. *HeyGen account.*
- **`comfy-workflow-mcp`** — drive ControlNet / IP-Adapter / InstantID / PuLID locally for fine control. *Local ComfyUI; no cloud account.*

**What requires wrapping:**
- **`awesome-genmedia/skills`** (InstantID, IP-Adapter, PhotoMaker, ControlNet, LoRA, StoryDiffusion via eachlabs.ai) — a Claude-format plugin → needs a small Codex wrapper. **This is the recommended first wrapper** (closest ready-made identity toolkit; ~1 small plugin).

**What requires custom skill creation:**
- A custom **`identity-lock`** skill (reference photos → reusable identity → conditioned generation).
- A custom **`height-scale-lock`** skill (per-character continuity sheet + pose/scale enforcement) — **no off-the-shelf solution exists anywhere.**

**The first safe wrapper:** fork/vendor `awesome-genmedia/skills`, add a root `.codex-plugin/plugin.json` over its `skills/`, add it as a `url`/`git-subdir` source with `ON_INSTALL` auth, validate with `--online`. Then the eachlabs.ai key is entered only at use time.

**Guardrails (any identity/video work):**
- **Consent only** — people who agreed; no impersonation of real third parties / no deepfakes.
- No API keys in the repo; `ON_INSTALL` auth; keys via env.
- Human-in-the-loop review of outputs; label AI-generated media; respect provider ToS.

**Recommendation:** try `higgsfield` Soul-ID + `heygen` first (no build). If you need more control, set up local ComfyUI. Only then wrap `awesome-genmedia/skills`. Build the custom `identity-lock` / `height-scale-lock` skills last, and only on your explicit approval.

> **Do not implement either track without your approval.** Tell me "start Track A" or "start Track B" and I'll scope the exact steps.
