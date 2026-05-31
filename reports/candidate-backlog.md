# Candidate Backlog — useful plugins/skills not added yet

Long-term backlog. **Nothing here has been added to the marketplace.** Each entry needs an action before it can be added. Discovery surfaced **613 distinct external repos** with `.codex-plugin/plugin.json`; 40 were deep-validated this run (34 added). The rest are inventoried below by priority.

## A. Not added this run — specific reasons
| Item | Reason | To add later |
|---|---|---|
| `evillollive/Analyze-Video-Skill` | Has a manifest but it's a **stub** | Wait for a real release, or replace with another video-analysis plugin |
| `heygen`, `supabase`, `motherduck`, `zoominfo`, `egnyte` (community versions) | **Already-covered** — the marketplace already has these services | Nothing; use the existing entries |
| `CompassLabs/compass-agent-skill` | Out of scope (crypto/DeFi), score 5 | Add only if you start DeFi work |
| `openai/skills` (44 `SKILL.md`) | Loose skills, **no `.codex-plugin/plugin.json`** | Consume as Codex skills directly, or wrap into a plugin |
| `awesome-genmedia/skills` | **Claude-plugin format** (InstantID/IP-Adapter/PhotoMaker/ControlNet/LoRA/StoryDiffusion via eachlabs.ai) | Wrap Claude→Codex (custom; needs approval) — closest path to identity/character control |
| `hunix/HoC-Republic` | Proprietary format, experimental, 0 stars (MagicAnimate/OmniGen/FaceFusion) | Skip unless it matures; caution |

**What "validate before adding" means:** locate `.codex-plugin/plugin.json`, confirm it's not a stub, check it isn't high-risk (no curl|bash installers / unknown binaries), confirm reachable + non-duplicate name. (Use the same process as `scripts/validate-marketplace.py` + manual manifest review.)

## B. High-priority discovered repos (official / reputable — validate next)
**Data / DB / infra:** `datocms/agent-skills`, `couchbaselabs/agent-skills`, `avifenesh/valkey-skills`, `kurrent-io/skills`, `Alation/alation-plugins`, `Azure/documentdb-agent-kit`, `GoogleCloudPlatform/cloud-bigtable-ecosystem`, `zscaler/zscaler-terraform-skills`, `truefoundry/tfy-deploy-skills`, `chrishuffman5/postgres`, `latitude-dev/latitude-codex`.
**Web / app frameworks:** `litestar-org/litestar-skills`, `Kotlin/kotlin-agent-skills`, `incluud/astro-codex-plugin`, `georgeguimaraes/claude-code-elixir`, `wieslawsoltes/development-plugin-for-avalonia`, `humanmade/accelerate-ai-toolkit` (WordPress), `Automattic/data-liberation-agent` (WordPress).
**Marketing / ads / commerce:** `spotify/ads-agentic-tools`, `clerk/skills` *(added)*, `sergebulaev/linkedin-skills` *(added)*.
**Sales / email / CRM:** `jmerelnyc/agentmail`, `explorium-ai/*` *(vibeprospecting added)*.
**Research:** `statzhero/zotero-fulltext`, `damionrashford/arxiv-mcp`, `cyanheads/brapi-mcp-server`.
**Security / monitoring:** `edamametechnologies/edamame_codex`, `drpcorg/drpc-agent-skills`, `cyanheads/ntfy-mcp-server`, `seamapi/seam-plugin`.

## C. Finance / credit-card-adjacent (relevant to your businesses — validate)
`atilaahmettaner/tradingview-mcp` (markets), `kentaroajisaka/moneyforward-cloud-codex` (finance), `exglade/my-tax-specialist` (tax), `g32jcj86/taiwan-stock-analysis` (equities), `daloopa/daloopa-plugin-codex` (financial data).

## D. Creative / visual (validate)
`panic-z/remotion-scenes`, `Halfapear/codex-wallpaper-plugin`, `DAT1305/SpriteSheet-Creator-Plugin`, `millionart/codex-plugin-UnrealPluginPipline`, `roboflow/computer-vision-skills` *(added)*.

## E. Productivity / notes / PM (validate)
`Nehoko/joplin-curl`, `aarondpn/redmine-cli`, `thelabnyc/redmine-mcp`, `rewdy/nano-kanban`, `kamiazya/whiteboard`, `henryennis/mermaid-js-for-agents` *(added)*.

## F. Plugin marketplaces worth mining (each may contain several plugins)
`jmanhype/claude-code-plugin-marketplace`, `obra/superpowers-marketplace`, `lyric-wren/skills-marketplace`, `xuniversity/plugins-marketplace`, `buildatscale-tv/claude-code-plugins`, `tmchow/tmc-marketplace`, `rami-code-review/claude-code-marketplace`.

## G. Lower-signal (large volume — validate opportunistically)
Many individual-author repos surfaced: numerous `everything-claude-code*` forks, ~15 `mempalace`/memory clones (duplicates of one project), and assorted personal `skills`/`harness` repos. These are unvetted, often Claude-only or loose-skill, and frequently low-maintenance — validate individually only if a specific one matches a need. The full 613-repo discovery list is reproducible via:
`gh api -X GET 'search/code' -f q='filename:plugin.json path:.codex-plugin' -f per_page=100 -f page=N`.

## Notes
- Bias when promoting: a plugin is addable if it has a valid non-stub `.codex-plugin/plugin.json`, reachable manifest, real purpose, and is not high-risk — API-key/account/niche/Windows-unverified are **not** blockers (label them instead).
- Always skip: stubs, missing manifests, curl|bash-at-load installers, unknown-binary execution, obvious malware, duplicates.
