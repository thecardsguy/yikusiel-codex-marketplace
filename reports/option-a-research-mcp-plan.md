# Option A — Research / Search Setup Plan

The safest way to add strong, sourced research to The Cards Guy. **Nothing here is connected or authenticated** — this is a plan. Approve a step and I'll prepare the exact config; you paste the key.

> **Firecrawl** is already an installable **marketplace plugin** (`firecrawl`) — just install it and add a key. **Tavily / Exa / Perplexity** are **MCP servers** you add to your Codex MCP config (not via the `+` marketplace button).

---

## 1. Firecrawl  — set up FIRST
- **What it helps with:** scrape/crawl any web page into clean text/markdown (issuer card pages, competitor pages, pricing).
- **Why for The Cards Guy:** pull exact, current APRs / fees / bonuses straight from the issuer page so drafts are fact-anchored (not guessed).
- **Account/API key:** yes — `FIRECRAWL_API_KEY` from firecrawl.dev.
- **Free tier:** ✅ 1,000 credits/month, no credit card.
- **Setup:** it's the `firecrawl` plugin in your marketplace — install it, then add the key when prompted (`ON_INSTALL`).
- **Example placeholder (env):** `FIRECRAWL_API_KEY=<your-firecrawl-key>`
- **Security:** key via env / Codex secret prompt only — never commit it.
- **Connect now or wait:** **now** (free tier, immediate value).

## 2. Tavily  — set up SECOND
- **What it helps with:** fast, agent-optimized web search with clean results.
- **Why for The Cards Guy:** find content gaps, competitor angles, and source candidates quickly.
- **Account/API key:** yes — `TAVILY_API_KEY` from tavily.com.
- **Free tier:** ✅ (monthly free search credits).
- **Setup:** MCP server in Codex config. **Example placeholder:**
  ```json
  { "mcpServers": { "tavily": { "command": "npx", "args": ["-y", "tavily-mcp"], "env": { "TAVILY_API_KEY": "<your-tavily-key>" } } } }
  ```
- **Security:** key in env block only; don't paste into chat or commit.
- **Connect now or wait:** **soon** (after Firecrawl) — low cost, big research boost.

## 3. Exa  — set up THIRD
- **What it helps with:** neural/semantic search — finds pages by meaning, good for primary sources.
- **Why for The Cards Guy:** surface authoritative finance sources you'd miss with keyword search.
- **Account/API key:** yes — `EXA_API_KEY` from exa.ai.
- **Free tier:** limited free credits.
- **Setup:** MCP server. **Example placeholder:**
  ```json
  { "mcpServers": { "exa": { "command": "npx", "args": ["-y", "exa-mcp-server"], "env": { "EXA_API_KEY": "<your-exa-key>" } } } }
  ```
- **Security:** env only; rotate if exposed.
- **Connect now or wait:** **wait** until you want deeper semantic research.

## 4. Perplexity  — set up LAST (optional)
- **What it helps with:** answer engine that returns cited answers.
- **Why for The Cards Guy:** quick sourced answers during fact-checking (always verify against the issuer page).
- **Account/API key:** yes — `PERPLEXITY_API_KEY` (paid; limited/again-check free options).
- **Free tier:** limited; mostly paid.
- **Setup:** MCP server. **Example placeholder:**
  ```json
  { "mcpServers": { "perplexity": { "command": "npx", "args": ["-y", "perplexity-mcp"], "env": { "PERPLEXITY_API_KEY": "<your-perplexity-key>" } } } }
  ```
- **Security:** env only.
- **Connect now or wait:** **wait** — nice-to-have; Firecrawl + Tavily cover most needs.

---

## Suggested order & guardrails
1. **Firecrawl** (free, already a plugin) → 2. **Tavily** (free MCP) → 3. **Exa** (when needed) → 4. **Perplexity** (optional).
- **Manual until you approve:** I will NOT enter keys, connect MCP servers, or activate paid plans. When you're ready, say "set up Firecrawl" (or Tavily/etc.) and I'll give you the exact, copy-paste config — you supply the key in your own environment.
- **Never** commit API keys; keep them in env / Codex secret storage. The placeholders above use `<your-...-key>` on purpose.
- These tools **find and fetch** information — you and the issuer page still own the facts (see `reports/cards-guy-writing-test-workflow.md`).
