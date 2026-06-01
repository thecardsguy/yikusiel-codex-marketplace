# After the First 15 — Next Step (branching)

Pick the branch that matches your test results from `reports/plugin-test-results.md` / `first-install-feedback-form.md`. **Don't assume everything passed** — start at the bottom branch if it didn't. Nothing is installed/authenticated for you; these are recommendations.

> Rule for all branches: add tools **one at a time**, test, then continue. Don't bulk-install. Enter API keys/accounts only when you choose to use a tool.

## ✅ If MOST WRITING tools passed (`writers-loop`, `unslop`, `claude-mem`, `citecheck`)
**→ Move to the SEO / content stack** to grow The Cards Guy.
- Order: `citecheck` (done) → **`firecrawl`** (free tier — scrape issuer/competitor pages) → **`gpt-researcher`** (LLM key) → **`codex-seo`** (DataForSEO+Firecrawl+Google) → **`semrush`** / **`similarweb`** (paid).
- Why: pairs research + fact-checking + SEO so you can refresh pages faster and rank better.
- Risk: low→medium (mostly account/key setup). Start with the free `firecrawl`.

## ✅ If RESEARCH tools passed (`microsoft-docs`, `citecheck`, `github-librarian`)
**→ Set up research MCP servers** (these connect in your Codex MCP config, not via `+`).
- Order: **Tavily** (free tier) → **Exa** → **Perplexity**.
- Why: live, sourced, semantic web research — biggest low-cost quality boost.
- Risk: low. See `reports/next-technical-phase-plan.md` Track A.

## ✅ If CODE tools passed (`codebase-recon`, `brooks-lint`, `commit-narrator`, `secret-guard`, `env-lint`)
**→ Move to the app-building stack** (for The Cards Guy site + DisputeIQ).
- Order: `clerk` (auth, free tier) + `supabase` (or `prisma`/`convex`) → `vercel` (hosting, free tier) → `sentry` + `checkly` (monitoring, free tiers) → `stackhawk` (security).
- Why: ship and run real apps with auth, data, deploy, monitoring, security.
- Risk: low→medium. Most have free tiers.

## ⏳ If CREATIVE is your next priority
**→ Move slowly — most setup, paid accounts.**
- Order: `comfy-workflow` (local ComfyUI, no cloud acct) → `higgsfield` (Soul-ID identity, paid) → `heygen` (avatars, paid) → `pika` (video, paid). Wrap `awesome-genmedia` only later (custom, your approval).
- Why: real image/video + best face-consistency path.
- Risk: medium (accounts + a wrapper build for full identity control). See `creative-identity-tools.md` + `identity-video-wrapping-plan.md`.

## ⚠️ If MANY of the first 15 FAILED
**→ Do NOT add more plugins. Diagnose first:**
1. **Marketplace refresh:** Codex → Plugins → `yikusiel-codex-marketplace` → reopen/refresh. The marketplace validates clean (257 plugins, `--online` passed), so failures are usually client-side.
2. **Plugin source:** external plugins load from GitHub at install — confirm Codex can reach GitHub; try one plugin again.
3. **Codex install issue:** restart Codex; check its plugin logs; re-add the marketplace if it's not listed.
4. **Re-run `python scripts/validate-marketplace.py --online`** to confirm manifests are still reachable (it was passing as of commit `5696142`).
5. Record specifics in `first-install-feedback-form.md` (which failed, error text) and tell me — I'll help diagnose without adding anything.

---
## My default recommendation (if results are mixed/good)
1. **Research MCPs (Tavily + free `firecrawl`)** — cheapest, biggest research win for Cards Guy.
2. **SEO/content** next (it builds on research).
3. **App-building** when you're actively shipping.
4. **Creative/identity** last (most setup).

When ready, tell me **"start Option A/B/C/D"** (from `next-decision-guide.md`) or **"start Track A/B"** and I'll scope the exact safe steps.
