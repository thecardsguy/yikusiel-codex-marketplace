# API & Account Requirements

Which plugins need a key/account/OAuth/local-setup **to use** (none need anything just to appear in the marketplace; all use `authentication: ON_INSTALL`). Machine-readable flags are in `plugin-dashboard.csv` (Account/API column).

> **Do not authenticate or enter keys until you actually want to use a plugin.** Install the zero-config tier first.

## Free tier available → install anytime
| Plugin | Requirement | Service | Notes |
|---|---|---|---|
| `firecrawl` | API key | firecrawl.dev | 1,000 free credits/mo, no card |
| `langfuse` | keys | Langfuse Cloud | free tier; self-host option |
| `clerk` | account | Clerk | generous free tier |
| `sanity` | account | Sanity | free tier |
| `mongodb` | account | MongoDB Atlas | free tier |
| `checkly` | account | Checkly | free tier |

## Paid / business account required → wait until needed
| Plugin | Requirement | Service |
|---|---|---|
| `stripe-link` | US Stripe Link account (CLI login) | Stripe |
| `twilio-dev-kit` | Account SID + Auth Token | Twilio |
| `dodopayments` | OAuth (optional key) | Dodo Payments |
| `codex-seo` | 3 paid APIs | DataForSEO + Firecrawl + Google AI |
| `vidseeds` | Personal Access Token | VidSeeds.ai (trial) |
| `shopify-plugin` | store | Shopify |
| `spotify-ads` | Ads account | Spotify |
| `datocms` | account | DatoCMS |
| `seam` | API key | Seam |
| `alation` | instance | Alation |
| `truefoundry` | account | TrueFoundry |
| `drpc` | account/key | dRPC |
| `accelerate-wp` | WP + Human Made | WordPress |
| `azure-documentdb` | Azure account | Microsoft Azure |
| `metabase` | instance (self-host/cloud) | Metabase |
| `stackhawk` / `fortify` | account/license | StackHawk / OpenText |
| `atlassian-forge` / `bitbucket-cli` | Atlassian creds | Atlassian |
| `jenkins-cli` | Jenkins server creds | Jenkins |
| `loops` / `vibeprospecting` | API key / account | Loops / Explorium |
| `crawlbase` / `armorcodex` / `axonflow` / `base44` / `compound-engineering` / `content-planner` / `papersflow` / `dataproduct-builder-dbt` | API key / account | respective vendors |

## Image/video — paid account/credits
`pika` (Pika OAuth + credits), `higgsfield` (paid Higgsfield account), `nyldn-img` (OpenAI gpt-image-2 and/or Gemini keys), `aether`, `image-studio`, `video-vision`, `roboflow` (Roboflow key). `gpt-researcher` needs an LLM API key (you likely already have one).

## Local setup (no remote account, but needs local install)
| Plugin | Local dependency |
|---|---|
| `comfy-workflow` | a local ComfyUI install |
| `computer-use-windows` | runs against your local Windows desktop |
| `burpsuite-bridge` | local Burp Suite |

## Platform-specific dependency
| Plugin | Platform |
|---|---|
| `agent-vision` | macOS (camera) |
| `codex-obsidian` | macOS |
| `visionos-apps` | macOS + Xcode (visionOS) |
| `kachilu-browser` | WSL2 Chrome on Windows |

## OpenAI-fork connectors (147 local plugins)
Most are SaaS connectors (Gmail, Slack, Notion, Linear, Airtable, Stripe, Supabase, Vercel, Datadog, Sentry, Semrush, FactSet, Factiva, Morningstar, etc.) that **authenticate via OAuth on install**. Treat all as "needs account" for the specific service. Install only the ones you use.
