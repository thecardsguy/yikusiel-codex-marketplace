# Website & App-Building Stack

Tools in this marketplace for building sites/apps, grouped by layer. Pick per project; you don't need all of them.

## Frontend / UI / design
`astro`, `litestar` (Python backend+templates), `maquette` (image-guided design → coded components + tokens), `stark` (UI/UX router), `universal-design-principles` (accessibility/UX heuristics), `mermaid` (diagrams), `figma` (fork).

## Backend / database
`supabase`, `convex`, `prisma`, `mongodb`, `couchbase`, `valkey`, `kurrent`, `azure-documentdb`, `metabase` (BI), `dataproduct-builder-dbt` (analytics).

## Auth
`clerk` (official), Supabase Auth (via `supabase`).

## Deployment / infra
`vercel`, `netlify`, `cloudflare`, `truefoundry` (ML services). CI: `jenkins-cli`, `bitbucket-cli`, GitHub Actions (via `github`).

## Testing / QA
`test-gap` (coverage gaps), `flaky-detector`, `env-lint`, `brooks-lint` (code review heuristics), `codex-reviewer`, `compound-engineering`, `spec-driven`.

## Security
`secret-guard` (pre-commit secret scan), `deps-doctor` (dependency CVEs), `stackhawk` (DAST), `fortify`, `agentic-security`, `armorcodex`, `zscaler`, `burpsuite-bridge`.

## Performance / monitoring / observability
`checkly` (synthetic/uptime), `sentry`/`sentry-cli` (errors), `datadog` (APM), `langfuse` (LLM-app tracing).

## SEO / content
`codex-seo`, `enterprise-seo`, `semrush`, `similarweb`, `content-planner`, `digital-marketing`, `adsense-readiness`.

## Recommended stacks
**The Cards Guy (React/Vite/Supabase/Vercel):** `supabase` + `convex` (or `prisma`) + `clerk` + `vercel` → build; `codex-seo` + `semrush` + `content-planner` → SEO/content; `writers-loop` + `unslop` → copy; `checkly` + `sentry` → ops; `secret-guard` + `deps-doctor` + `stackhawk` → security.

**HY Credit / DisputeIQ:** `supabase`/`prisma` (case data) + `clerk` (client auth); `secret-guard` (protect PII/keys) + `env-lint`; document/data workflows via fork connectors (`google-drive`, `box`); `writers-loop` + `unslop` for compliance-aware, FCRA-careful drafting; `claude-mem` for client/case memory; `codex-reviewer` + `test-gap` for QA. **Keep PII out of logs; verify every dispute claim.**

**AI scheduling / automation:** `session-orchestrator` + `agentops` (orchestration) + `claude-mem` (memory) + `task-scheduler`; `n8n-codex`/`n8n-mcp-synta` (workflow automation); `google-calendar` + `gmail` + `notion` (fork); `langfuse` (observe runs).
