# Codex Copy-Paste Test Prompts (first 15)

One short prompt per plugin. Install the plugin in Codex first, then paste its prompt. None need an API key. Record outcomes in `reports/plugin-test-results.md`.

### `writers-loop`
> Plan and draft a 150-word intro for a credit-card review using a frame → draft → revise pass. Human expert tone. Do not invent any numbers.

### `unslop`
> Rewrite this to sound like a human professional editor without changing any facts: "In today's fast-paced world, this card is a true game-changer that unlocks a plethora of benefits."

### `claude-mem`
> Remember: The Cards Guy covers U.S. credit cards only and uses a human expert tone. (Then, in a new task, ask: "What are my content rules?")

### `pm-skills`
> Create a lightweight product plan for a "best travel cards 2026" page: goals, scope, tasks, and risks.

### `agentops`
> Set up a research → draft → validate → ship workflow for a credit-card page refresh, with a validation gate before shipping.

### `session-orchestrator`
> Break "refresh the Amex Gold page" into a research-plan-execute-close session with quality gates between phases.

### `microsoft-docs`
> Search the official Microsoft docs and cite the page for: Azure OpenAI image generation quotas.

### `citecheck`
> Check whether these two sources exist and are relevant to a claim that the average U.S. credit-card APR is about 21%: [paste 2 links].

### `github-librarian`
> Find well-maintained React table libraries with TypeScript support; compare stars and last release date.

### `codebase-recon`
> Analyze this repository's git history for hotspots and bus factor. Do not change any files — analysis only.

### `brooks-lint`
> Review [path/to/file] for design decay; for each finding give Symptom → Source → Consequence → Remedy and cite the principle. Do not edit the file.

### `commit-narrator`
> (Stage a small change first.) Write a clear commit message for my currently staged changes.

### `secret-guard`
> (Use a FAKE key only.) Stage a file containing `STRIPE_KEY=sk_test_fake123`, then scan my staged changes for secrets and redact anything found.

### `env-lint`
> Compare my .env against .env.example and list missing or extra keys — names only, no values.

### `mermaid`
> Create a Mermaid architecture diagram (flowchart TD, in a ```mermaid code block) for: React/Vite frontend + Supabase backend + Vercel hosting + Clerk auth.

---
**If a prompt does nothing:** confirm the plugin is installed/enabled, refresh the marketplace, restart Codex, and mention the skill by name. These 15 should never ask for an API key — if one does, stop and note it in `reports/first-install-feedback-form.md`.
