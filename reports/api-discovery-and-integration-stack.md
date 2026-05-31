# API Discovery & Integration Stack

How to find, evaluate, and integrate the best API for a feature, using what's in this marketplace. (There is no single "API finder" plugin, so this is a workflow built from real tools.)

## Best tools already in the marketplace
- **Discovery / research:** `github-librarian` (find SDKs/repos), `microsoft-docs` (authoritative MS/Azure API docs), `firecrawl` (scrape any API's docs/pricing), `gpt-researcher` + `gsearch`/`browser-bridge` (compare options), `openai-developers`/`github` (fork).
- **Specific provider APIs (official):** `stripe`/`stripe-link` (payments), `twilio-dev-kit` (SMS/voice/WhatsApp/Verify/SendGrid), `seam` (IoT/access), `drpc` (web3 RPC), `clerk` (auth), `supabase`/`convex`/`mongodb`/`couchbase` (data), `cloudflare`/`vercel`/`netlify` (platform), `microsoft-docs` (Graph/Azure).
- **Testing:** `checkly` (API/synthetic monitoring + checks), `test-gap`, `env-lint` (config/keys hygiene).
- **Monitoring:** `checkly`, `datadog`, `sentry`/`sentry-cli`, `langfuse` (LLM-API tracing).
- **Security:** `stackhawk` (DAST), `zscaler`, `burpsuite-bridge`, `secret-guard` (don't leak API keys), `deps-doctor` (SDK CVEs).
- **Routing/cost (LLM APIs):** `llm-router`.

## Best MCP-only / not-yet-added tools worth connecting later
`postman`, `bruno` (API clients), `tavily`, `exa`, `perplexity` (research/search APIs), `posthog` (product analytics). See `skill-wrapping-backlog.md` / `cross-agent-skills-inventory.md`.

## Workflow: find the best API for a product feature
1. Define the capability + constraints (region, compliance, budget, volume).
2. `gpt-researcher` + `firecrawl` to gather candidates; `github-librarian` to check SDK quality/maintenance; `microsoft-docs` for MS/Azure options.
3. Shortlist 2–3; pull each provider's docs/pricing with `firecrawl`.

## Workflow: evaluate an API (reliability, pricing, docs, auth, limits, webhooks, SDKs)
| Dimension | How to check |
|---|---|
| Reliability/SLA | status page + `checkly` synthetic check; provider uptime history |
| Pricing | `firecrawl` the pricing page; model your volume |
| Docs quality | `microsoft-docs`/`firecrawl`; are there OpenAPI specs + examples? |
| Auth | API key vs OAuth vs mTLS; secret handling (`secret-guard`) |
| Rate limits | docs + test calls; plan backoff |
| Webhooks | does it push events? signature verification? |
| SDKs | `github-librarian` — official SDK, stars, last release, open issues |
| Security | `stackhawk`/`burpsuite-bridge` against your integration |

## Workflow: implement an API in a Vite/React/Supabase/Vercel app
1. Keys in env (never client-side); for sensitive calls use a Supabase Edge Function / Vercel serverless function as a proxy.
2. Generate a typed client from the OpenAPI spec; add retries + backoff.
3. Store secrets in Vercel/Supabase env; scan with `secret-guard`, lint with `env-lint`.
4. Add `checkly` monitors + `sentry` error capture; review with `codex-reviewer`; security-scan with `stackhawk`.
