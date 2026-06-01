# Plugin Rename Map

During install debugging we found Codex installs a plugin only when the **marketplace entry name matches the plugin's own manifest `name`**. 34 external entries were renamed to match; 3 were removed. Marketplace count: 257 → **254**. Machine-readable: `plugin-rename-map.csv`.

## Renamed (34) — install under the new name

| Old name | New name | Reason | Install impact |
|---|---|---|---|
| `mermaid` | `mermaid-js-for-agents` | name must match manifest | now installs (use new name) |
| `accelerate-wp` | `accelerate-ai-toolkit` | name must match manifest | now installs (use new name) |
| `adsense-readiness` | `arb` | name must match manifest | now installs (use new name) |
| `astro` | `astro-codex-plugin` | name must match manifest | now installs (use new name) |
| `atlassian-forge` | `forge-skills` | name must match manifest | now installs (use new name) |
| `azure-documentdb` | `documentdb` | name must match manifest | now installs (use new name) |
| `bitbucket-cli` | `bkt` | name must match manifest | now installs (use new name) |
| `browser-bridge` | `browserbridge` | name must match manifest | now installs (use new name) |
| `burpsuite-bridge` | `burpsuite-mcp-bridge` | name must match manifest | now installs (use new name) |
| `clerk` | `clerk-skills` | name must match manifest | now installs (use new name) |
| `comfy-workflow` | `comfy-workflow-mcp` | name must match manifest | now installs (use new name) |
| `computer-use-windows` | `windows-computer-use` | name must match manifest | now installs (use new name) |
| `couchbase` | `couchbase-skills` | name must match manifest | now installs (use new name) |
| `digital-marketing` | `digital-marketing-pro` | name must match manifest | now installs (use new name) |
| `drpc` | `drpc-agent-skills` | name must match manifest | now installs (use new name) |
| `enterprise-seo` | `enterprise-frontend-seo` | name must match manifest | now installs (use new name) |
| `fiftyone` | `fiftyone-skills` | name must match manifest | now installs (use new name) |
| `fortify` | `fortify-skills` | name must match manifest | now installs (use new name) |
| `image-studio` | `image-studio-mcp` | name must match manifest | now installs (use new name) |
| `jenkins-cli` | `jk` | name must match manifest | now installs (use new name) |
| `n8n-codex` | `n8n` | name must match manifest | now installs (use new name) |
| `n8n-mcp-synta` | `n8n-mcp-synta-codex` | name must match manifest | now installs (use new name) |
| `nyldn-img` | `img` | name must match manifest | now installs (use new name) |
| `papersflow` | `papersflow-codex-plugin` | name must match manifest | now installs (use new name) |
| `project-autopilot` | `codex-project-autopilot` | name must match manifest | now installs (use new name) |
| `spotify-ads` | `spotify-ads-api` | name must match manifest | now installs (use new name) |
| `stripe-link` | `link` | name must match manifest | now installs (use new name) |
| `tradingview` | `tradingview-mcp` | name must match manifest | now installs (use new name) |
| `valkey` | `valkey-skills` | name must match manifest | now installs (use new name) |
| `vibeprospecting` | `vpai` | name must match manifest | now installs (use new name) |
| `video-vision` | `codex-video-vision` | name must match manifest | now installs (use new name) |
| `visionos-apps` | `build-visionos-apps` | name must match manifest | now installs (use new name) |
| `wshobson-agents` | `developer-essentials` | name must match manifest | now installs (use new name) |
| `zscaler` | `zscaler-terraform-skills` | name must match manifest | now installs (use new name) |

## Removed (3)

| Removed entry | Reason | What to use instead |
|---|---|---|
| `arxiv` | manifest name `@cyanheads/arxiv-mcp-server` (has `/` + `@`) — unsafe as an entry name | skip for now; wrap later |
| `remotion-external` | duplicate of the existing **local** `remotion` | use local `remotion` (kept) |
| `twilio-dev-kit` | duplicate of the existing **local** `twilio-developer-kit` | use local `twilio-developer-kit` (kept) |

> The local `remotion` and `twilio-developer-kit` plugins were **kept** — only the redundant external duplicates were removed.
