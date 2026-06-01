# First-Week Codex Plugin Plan

A practical 5-day plan to install and test the safe first batch (all zero-config, no account, low risk). In Codex: **Plugins → `yikusiel-codex-marketplace` → reopen/refresh → `+`**. Track results in `reports/codex-install-tracker.md`.

> **Do not install yet:** any account/API-heavy plugin, `windows-computer-use`, `burpsuite-mcp-bridge`, or macOS-only tools (`agent-vision`, `codex-obsidian`, `build-visionos-apps`). One day at a time — don't bulk-install.

## Day 1 — Writing & memory
**Install:** `writers-loop`, `unslop`, `claude-mem`
**Test (small credit-card page rewrite):**
1. Paste 2–3 paragraphs from an existing card page.
2. `writers-loop`: "Rewrite this in a human expert tone for The Cards Guy — U.S. cards only, no invented facts."
3. `unslop`: "Now remove any AI-sounding wording without changing the facts."
4. `claude-mem`: "Remember my content rules: U.S. cards only, human expert tone, label confirmed vs rumored."
**Looks right if:** the rewrite sounds human/expert, no new facts appeared, and `claude-mem` recalls your rules in a later prompt.

## Day 2 — Research & citation
**Install:** `microsoft-docs`, `citecheck`, `github-librarian`
**Test:**
- `microsoft-docs`: "Find official docs for Azure OpenAI image quotas." → cites Microsoft Learn.
- `citecheck`: "Verify these sources exist and are relevant: <paste 2 links>." → existence/relevance check.
- `github-librarian`: "Find maintained React table libraries with TypeScript; compare stars/recency." → shortlist with health signals.
**Looks right if:** sources are real and relevant, library picks are current/maintained.

## Day 3 — Code review & safety (read-only)
**Install:** `codebase-recon`, `brooks-lint`, `secret-guard`, `env-lint`
**Test on your repo without changing code:**
- `codebase-recon`: "Analyze this repo's git history (hotspots, bus factor). Don't change code."
- `brooks-lint`: "Review <file> for design decay; cite the principle for each finding."
- `secret-guard`: "Scan my staged changes for secrets and redact any found."
- `env-lint`: "Compare .env vs .env.example (key names only)."
**Looks right if:** nothing edits your code, secrets are redacted (not printed), env diff shows only key names.

## Day 4 — Planning & project workflow
**Install:** `pm-skills`, `agentops`, `session-orchestrator`, `commit-narrator`
**Test (project planning):**
- `pm-skills`: "Plan a 'best travel cards 2026' page: goals, scope, tasks, risks."
- `session-orchestrator`: "Turn that into a research-plan-execute-close session with quality gates."
- `agentops`: "Track this as a research→draft→validate→ship workflow."
- `commit-narrator`: "Write a commit message for my staged changes."
**Looks right if:** you get a clear staged plan and a clean commit message.

## Day 5 — Visual / documentation helper
**Install:** `mermaid-js-for-agents`
**Test:** "Create a Mermaid architecture diagram for The Cards Guy: React/Vite frontend + Supabase backend + Vercel hosting + Clerk auth."
**Looks right if:** you get valid Mermaid code you can paste into a renderer.

## End of week
You'll have a 15-plugin foundation covering writing, memory, research, fact-checking, code-safety, planning, and diagrams — all zero-config. Next steps (only when ready): the Cards Guy writing workflow (`reports/cards-guy-writing-test-workflow.md`) and the MCP/identity plans (`reports/next-technical-phase-plan.md`).
