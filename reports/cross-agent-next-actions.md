# Cross-Agent Next Actions

High-value tools that are **not** Codex-marketplace plugins (so they're not in `.agents/plugins/marketplace.json`) but are worth connecting or wrapping. Nothing here is installed or authenticated yet.

**How to act on each:**
- **Connect directly (MCP):** add the server to your Codex MCP config (e.g. `~/.codex` MCP settings) — no marketplace entry needed. Enter its API key only when you set it up.
- **Wrap:** create a small Codex plugin (a `.codex-plugin/plugin.json` over the tool's skills, or a thin `.mcp.json`) — a custom build; needs your approval.
- **Skip / use in Claude:** leave it; use in Claude Code if/when useful.

| Tool / package | Type | Why useful | How it helps you | Action | Priority |
|---|---|---|---|---|---|
| **Tavily** (`tavily-ai/tavily-mcp`) | MCP server | High-quality web search API built for agents | Research, content-gap finding, fact discovery for Cards Guy | **Connect (MCP)** — Tavily API key | **High** |
| **Exa** (`exa-labs/exa-mcp-server`) | MCP server | Neural/semantic web search | Deep research, finding primary finance sources | **Connect (MCP)** — Exa API key | Medium |
| **Perplexity** (Perplexity MCP) | MCP server | Answer engine with citations | Quick sourced answers during fact-checking | **Connect (MCP)** — Perplexity key | Medium |
| **Postman** (Postman MCP/CLI) | MCP / CLI | API client, collections, testing | API discovery + integration testing | **Connect (MCP)** or use CLI | Medium |
| **Bruno** (`usebruno`) | CLI / app | Open-source local API client | Local API testing, no cloud | **Use CLI directly** | Low |
| **PostHog** (`PostHog/skills`) | Claude plugin (`.claude-plugin`, 11 sub-plugins) | Product analytics, funnels, events | Measure Cards Guy / DisputeIQ usage | **Wrap** (Codex manifest over skills) or use in Claude — PostHog account | Medium |
| **awesome-genmedia** (`awesome-genmedia/skills`) | Claude plugin | InstantID, IP-Adapter, PhotoMaker, ControlNet, LoRA, StoryDiffusion (eachlabs.ai) | **Real face/identity + character consistency** | **Wrap** (see `identity-video-wrapping-plan.md`) — eachlabs.ai key | **High** (for creative identity) |
| **OpenAI skills** (`openai/skills`) | Loose `SKILL.md` (44) | Official Codex skill catalog | General agent capabilities | **Use as Codex skills directly**, or wrap a curated bundle | Medium |
| **Claude skills** (various `.claude/skills`) | Claude skill | Many writing/research/coding skill packs | Reusable workflows | Use in Claude Code; wrap selectively | Low–Med |
| **MCP browser/computer-use** (e.g. Playwright MCP) | MCP server | Browser automation / visual review | Screenshot/visual QA of your sites | **Connect (MCP)** when needed | Medium |

## Recommended order
1. **Connect Tavily MCP** (biggest research win, low effort).
2. **Connect Exa + Perplexity MCP** when you want deeper/sourced research.
3. **Wrap `awesome-genmedia/skills`** when you commit to identity/character creative work (see plan).
4. **Postman MCP** if/when you do heavy API integration.
5. PostHog: wrap or use in Claude once you have analytics to track.

> MCP connections live in your Codex config, not this repo. Keep API keys in env/secret storage — never commit them.
