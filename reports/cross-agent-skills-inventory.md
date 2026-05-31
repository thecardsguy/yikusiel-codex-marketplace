# Cross-Agent Skills Inventory

How tools across the ecosystem map to **this Codex marketplace** vs. things better used as Claude skills or MCP servers. "Addable" = has a real `.codex-plugin/plugin.json`.

## Classification key
1. **Codex-addable now** — added or addable to this marketplace.
2. **Needs wrapping** — useful, but ships only `.claude-plugin/plugin.json`, `SKILL.md`, or an MCP config (no Codex manifest).
3. **Claude-only** — best used in Claude Code directly.
4. **MCP-only** — connect as an MCP server in Codex/Claude rather than a marketplace plugin.
5. **Skip.**

## OpenAI skills
- **`openai/skills`** — 44 official `SKILL.md` files (Codex skill catalog). **No `.codex-plugin/plugin.json`** → *(2) consume as Codex skills directly, or wrap a bundle.* Not a marketplace plugin.

## Writing
- Codex-addable (added): **`writers-loop`**, **`unslop`**, **`content-planner`**.
- Needs wrapping / Claude-only: a dedicated brand-voice skill pack would help — none found as a Codex plugin (see wrapping backlog).

## Research / search
- Codex-addable (added): **`gpt-researcher`**, **`firecrawl`**, **`citecheck`**, **`github-librarian`**, **`arxiv`**, **`codex-autoresearch`**, **`papersflow`**, plus fork research connectors (`scite`, `readwise`, `factset`, `dow-jones-factiva`, `morningstar`, `cb-insights`, `quartr`, `aiera`, `daloopa`).
- MCP-only (backlog): **`tavily-ai/tavily-mcp`**, **`exa-labs/exa-mcp-server`**, **Perplexity** — high-quality search APIs; connect as MCP servers.

## Website / app building
- Codex-addable (added): **`astro`**, **`litestar`**, **`supabase`**, **`convex`**, **`prisma`**, **`mongodb`**, **`couchbase`**, **`valkey`**, **`kurrent`**, **`azure-documentdb`**, **`clerk`**, **`vercel`**, **`netlify`**, **`cloudflare`**, **`truefoundry`**, **`maquette`**, **`stark`**, **`universal-design-principles`**.

## API discovery / integration
- Codex-addable (added): **`microsoft-docs`**, **`github-librarian`**, **`firecrawl`**, **`checkly`**, **`stackhawk`**, **`datadog`**, **`sentry-cli`**, **`llm-router`**, **`seam`**, **`twilio-dev-kit`**, **`stripe-link`**, **`drpc`**.
- MCP-only (backlog): **`postman`**, **`bruno`** (API clients) — connect/CLI, not found as Codex plugins.

## Identity / video / creative
- Codex-addable (added): **`pika`**, **`higgsfield`** (Soul ID identity), **`nyldn-img`**, **`comfy-workflow`**, **`roboflow`**, **`fiftyone`**, **`image-studio`**, **`video-vision`**, **`aether`**, **`maquette`**; fork: **`hyperframes`**, **`heygen`**.
- Needs wrapping (Claude-format): **`awesome-genmedia/skills`** — InstantID, IP-Adapter, PhotoMaker, ControlNet, LoRA, StoryDiffusion via eachlabs.ai. **Closest path to true identity/character/body control.**

## Analytics / data
- Codex-addable (added): **`metabase`**, **`dataproduct-builder-dbt`**, **`alation`**, **`langfuse`**.
- Needs wrapping (Claude-format): **`PostHog/skills`** (product analytics; ships `.claude-plugin`, 11 sub-plugins) → wrap or use in Claude.

## Multi-agent / memory / orchestration
- Codex-addable (added): **`session-orchestrator`**, **`agentops`**, **`claude-mem`**, **`context-pack`**, **`wshobson-agents`**, **`compound-engineering`**, **`spec-driven`**.

## Recommended next actions
- **Connect as MCP (no wrapping needed):** Tavily, Exa, Perplexity, Postman/Bruno — add to your Codex MCP config when you want them.
- **Wrap (needs a small custom plugin — your approval):** `awesome-genmedia/skills` (identity/character), `PostHog/skills` (analytics), an `openai/skills` bundle.
- **Use in Claude Code directly:** anything Claude-only you don't want to wrap.
