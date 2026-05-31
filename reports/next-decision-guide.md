# Next Decision Guide — after the first 15 pass

Once your 15 zero-config plugins are installed and tested (see `post-install-test-checklist.md`), pick a direction. You can do more than one over time — just **don't bulk-install**; add account-heavy tools one at a time when you'll use them. Nothing here is installed or authenticated for you.

---

## Option A — Research / search MCPs
**What it unlocks:** much stronger, better-sourced research for The Cards Guy — live web search, semantic source-finding, and exact page extraction. (These are **MCP servers** you add to your Codex MCP config, except Firecrawl which is already a marketplace plugin.)
| Tool | Account/API | Notes |
|---|---|---|
| Firecrawl (`firecrawl` plugin) | Firecrawl key (**free tier**) | scrape issuer/competitor pages |
| Tavily (MCP) | Tavily key (**free tier**) | agent web search |
| Exa (MCP) | Exa key | semantic search |
| Perplexity (MCP) | Perplexity key | cited answers |
**Risk:** Low. **Recommended order:** Firecrawl → Tavily → Exa → Perplexity. (See `next-technical-phase-plan.md` Track A.) **Best first if** your priority is content quality/fact-finding now.

## Option B — Creative / identity tools
**What it unlocks:** real image/video generation and the best available same-person/face consistency.
| Tool | Account/API | Notes |
|---|---|---|
| `higgsfield` (Soul-ID) | paid Higgsfield account | best face-consistency path |
| `heygen` (fork) | HeyGen account | avatar/presenter video |
| `comfy-workflow` | **local ComfyUI** (no cloud acct) | local ControlNet/IP-Adapter |
| `awesome-genmedia` wrapper | eachlabs.ai key + a small wrapper build | InstantID/IP-Adapter/ControlNet — **needs wrapping + your approval** |
**Risk:** Medium (paid accounts; wrapper is a custom build). **Recommended order:** `comfy-workflow` (local, free) → `higgsfield`/`heygen` (accounts) → wrap `awesome-genmedia` last. (See Track B + `identity-video-wrapping-plan.md`.) **Best first if** creative/identity work is your priority — but more setup.

## Option C — App-building stack
**What it unlocks:** build/ship The Cards Guy and DisputeIQ — database, auth, deploy, monitoring, security.
| Tool | Account/API | Notes |
|---|---|---|
| `supabase`, `convex`, `prisma` | accounts (free tiers exist) | data layer |
| `clerk` | account (**free tier**) | auth |
| `vercel` | account (**free tier**) | hosting |
| `checkly`, `sentry` | accounts (**free tiers**) | monitoring/errors |
| `stackhawk` | account | security scanning |
**Risk:** Low–Medium. **Recommended order:** `clerk` + `supabase` (or `prisma`/`convex`) → `vercel` → `sentry` + `checkly` → `stackhawk`. **Best first if** you're actively building the site/app.

## Option D — SEO / content stack
**What it unlocks:** keyword research, competitor analysis, SEO audits, and sourced content — directly grows Cards Guy traffic.
| Tool | Account/API | Notes |
|---|---|---|
| `semrush`, `similarweb` | accounts (paid) | keywords/competitors |
| `codex-seo` | DataForSEO + Firecrawl + Google AI (paid) | full audits |
| `firecrawl` | free tier | page extraction |
| `gpt-researcher` | LLM API key | research synthesis |
| `citecheck` | none (already installed) | fact-checking |
**Risk:** Low–Medium (mostly account/key setup). **Recommended order:** `citecheck` (done) → `firecrawl` → `gpt-researcher` → `semrush`/`similarweb` → `codex-seo`. **Best first if** SEO growth is the priority.

---

## My recommendation
1. **Start with Option A (research MCPs)** — biggest low-cost win; Firecrawl + Tavily are free-tier and supercharge your writing workflow immediately.
2. **Then Option D (SEO/content)** — pairs naturally with A for The Cards Guy.
3. **Option C (app-building)** when you're actively building/shipping.
4. **Option B (creative/identity)** when you commit to image/video — it needs the most setup and paid accounts.

Whenever you're ready, tell me **"start Option A/B/C/D"** (or "start Track A/B" for the technical plans) and I'll scope the exact, safe steps — without authenticating or entering keys for you.
