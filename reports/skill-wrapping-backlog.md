# Skill-Wrapping Backlog

Useful packages that are **not** directly Codex-installable (no `.codex-plugin/plugin.json`). None are added to the marketplace. "Wrapping" = create a small Codex plugin that points at the same skills, or connect the MCP server. **Wrapping requires creating a custom plugin — not done yet (your approval needed).**

| Skill / package | Source repo | Type | Why useful | Helps me with | Wrapping required | Risk | Priority |
|---|---|---|---|---|---|---|---|
| InstantID / IP-Adapter / ControlNet / PhotoMaker / LoRA / StoryDiffusion | `awesome-genmedia/skills` | Claude plugin (`.claude-plugin`) | Real face/identity & character-consistency controls via eachlabs.ai | Same-person identity, face/body/scene consistency for creative work | Add `.codex-plugin/plugin.json` pointing at its skills/; needs eachlabs.ai API key | Medium | **High** (only real path to identity control) |
| Product analytics skills | `PostHog/skills` | Claude plugin (11 sub-plugins) | Funnels, events, dashboards for sites/apps | Product analytics for The Cards Guy / DisputeIQ | Wrap a Codex manifest over the skills dir; PostHog account | Low | Medium |
| Tavily search | `tavily-ai/tavily-mcp` | MCP server | High-quality web search API for agents | Research, fact-finding, content gaps | None — connect as MCP server in Codex config; Tavily API key | Low | **High** |
| Exa neural search | `exa-labs/exa-mcp-server` | MCP server | Semantic/neural web search | Deep research, finding primary sources | None — connect as MCP; Exa API key | Low | Medium |
| Perplexity | (Perplexity MCP) | MCP server | Answer engine with citations | Quick sourced answers for fact-checking | Connect as MCP; Perplexity API key | Low | Medium |
| Postman | (Postman MCP/CLI) | MCP/CLI | API client, collections, testing | API discovery/testing/integration | Connect MCP or use CLI; Postman account | Low | Medium |
| Bruno | (usebruno) | CLI/app | Open-source API client | Local API testing without cloud | Use CLI directly; no Codex plugin needed | Low | Low |
| OpenAI skill bundle | `openai/skills` | Loose `SKILL.md` (44) | Official Codex skill catalog | General agent capabilities | Either use as Codex skills directly, or wrap a curated bundle into one plugin | Low | Medium |

## How wrapping works (reference, not executed)
- **Claude-plugin → Codex:** add a `.codex-plugin/plugin.json` at the repo root (or a fork) with `name`, `interface`, and `skills: "./skills/"` (or the relevant dir). Same skills, Codex-readable. Best done in a small fork you control.
- **MCP-only → Codex:** create a tiny Codex plugin whose `.mcp.json` references the MCP server command/URL, plus a thin SKILL.md describing usage. Or just add the MCP server to your Codex MCP settings (no plugin needed).
- **Safety:** never bake API keys into the wrapper; use `ON_INSTALL` auth / env vars. Don't wrap anything that runs unknown binaries at load.
