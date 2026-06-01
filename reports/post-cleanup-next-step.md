# Post-Cleanup — Next Step

Marketplace is clean: **254 plugins**, validated (offline + `--online`), all names match their manifests. Here's exactly what to do next.

## Step 1 — Finish the first batch
1. **Refresh Codex:** Plugins → `yikusiel-codex-marketplace` → reopen/refresh (picks up the cleanup).
2. **Install the corrected 15th:** **`mermaid-js-for-agents`** (you already have the other 14). It was previously listed as `mermaid`, which failed because a marketplace entry name must match the plugin's manifest name.
3. **Test it:** "Create a Mermaid architecture diagram (flowchart TD, in a ```mermaid code block) for a React/Vite + Supabase + Vercel credit-card site."
4. **Record the result** in `reports/plugin-test-results.md` (Installed? / Passed?).

## Step 2 — If Mermaid works ✅
You've confirmed the corrected-name install path works → move to **Option A: research / search setup** (biggest low-cost win for The Cards Guy). Full detail in `reports/option-a-research-mcp-plan.md`. Recommended order:

1. **Firecrawl** — already an installable marketplace plugin (`firecrawl`); free tier (1,000 credits/mo, no card). Scrapes issuer/competitor pages for accurate facts. **Set up first.**
2. **Tavily** — MCP server; free tier. Agent-grade web search for content gaps/research.
3. **Exa** — MCP server; semantic/neural search for finding primary sources.
4. **Perplexity** — MCP server; cited answers for quick fact-checking.

- **What each does + keys + order:** see `option-a-research-mcp-plan.md`.
- **Stays manual until you approve:** entering any API key, connecting any MCP server, or activating a paid plan. I'll prepare configs; you paste the keys.

## Step 3 — If Mermaid fails again ⚠️
**Do not add more tools.** Diagnose first:
1. **Capture the exact Codex error** (copy the message) and paste it to me.
2. **Refresh/reopen Codex** again (and fully restart it once).
3. **Confirm Codex sees the corrected marketplace** — the plugin list should reflect 254 plugins and recent changes.
4. **Verify `mermaid-js-for-agents` appears** in the marketplace list (search for it). If it's not listed, the marketplace didn't refresh — re-add it: Plugins → add marketplace → `thecardsguy/yikusiel-codex-marketplace`.
5. **Check connectivity** — external plugins fetch from GitHub at install; confirm Codex can reach GitHub.
6. **If it still fails, skip Mermaid for now** — Codex/Claude can render Mermaid in chat without the plugin (it only adds diagram skills/guidance). Mark it `Skipped` in the tracker and move to Step 2; we'll revisit.

> Either way, you have a working 14-plugin foundation. Mermaid is the smallest/lowest-stakes of the batch.
