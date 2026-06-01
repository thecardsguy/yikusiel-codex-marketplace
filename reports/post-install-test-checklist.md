# Post-Install Test Checklist (first 15)

Run each test in Codex **after** installing the plugin (Plugins → `yikusiel-codex-marketplace` → `+`). Tick the box when it passes and note the result in `reports/codex-install-tracker.md`.

**General "it didn't work" fixes (try in order):**
1. Confirm it's installed (Codex → Plugins → it should be enabled).
2. Reopen/refresh the marketplace, then restart Codex.
3. Re-run with a clearer prompt (mention the action, e.g. "use the writers-loop skill").
4. Check the plugin's README/skill for the exact command or slash-command name.
5. These 15 are **zero-config** — if one demands an API key or account, that's unexpected: stop, skip it, and note it (it may have changed upstream).

---

### 1. `writers-loop` — structured writing
- **Test:** "Use a frame → draft → revise pass to write a 150-word intro for a Chase Sapphire Preferred review, human expert tone, no invented numbers."
- **Expected:** A visible plan/critique/revise, not a one-shot blob; reads human; no facts you didn't give it.
- [ ] Pass
- **Failure signs:** one-shot generic paragraph; invents APR/bonus figures.
- **If it fails:** re-prompt asking explicitly for the "frame, draft, critique, revise" stages.

### 2. `unslop` — de-AI editing
- **Test:** "Rewrite to sound like a human professional editor, change no facts: *The card, which is honestly a game-changer, offers a plethora of benefits.*"
- **Expected:** Cleaner, natural phrasing; filler ("honestly", "plethora", "game-changer") removed; meaning intact.
- [ ] Pass
- **Failure signs:** facts changed; still sounds AI; adds new claims.
- **If it fails:** ask for "low intensity, preserve all facts."

### 3. `claude-mem` — persistent memory
- **Test:** "Remember: The Cards Guy = U.S. credit cards only, human expert tone." → then in a **new** task: "What are my content rules?"
- **Expected:** It recalls the rule in the later task.
- [ ] Pass
- **Failure signs:** no recall in a fresh task.
- **If it fails:** confirm it saved (it may store under `.agents/`); re-state and retry.

### 4. `pm-skills` — product management
- **Test:** "Plan a 'best travel cards 2026' page: goals, scope, tasks, risks."
- **Expected:** A structured plan with those sections.
- [ ] Pass
- **Failure signs:** vague prose, no structure.
- **If it fails:** ask it to "use a PM skill / lean canvas format."

### 5. `agentops` — workflow ops
- **Test:** "Set up a research → draft → validate → ship workflow for a card-page refresh and track progress."
- **Expected:** A staged workflow with validation gates; may create notes in `.agents/`.
- [ ] Pass
- **Failure signs:** no stages/gates.
- **If it fails:** ask for "quality-gated stages with a validation step."

### 6. `session-orchestrator` — session lifecycle
- **Test:** "Break 'refresh the Amex Gold page' into a research-plan-execute-close session with quality gates."
- **Expected:** A phased plan with review gates between phases.
- [ ] Pass
- **Failure signs:** flat to-do list, no gates.
- **If it fails:** ask explicitly for "research, plan, execute, close phases."

### 7. `microsoft-docs` — official MS docs search
- **Test:** "Find the official Microsoft docs for Azure OpenAI image generation quotas."
- **Expected:** Cites Microsoft Learn; no hallucinated specifics.
- [ ] Pass
- **Failure signs:** answers from memory with no doc link.
- **If it fails:** ask it to "search Microsoft Learn and cite the page."

### 8. `citecheck` — citation/source verification
- **Test:** "Verify these exist and are relevant to a claim about average U.S. credit-card APRs: [paste 2 links/citations]."
- **Expected:** Existence + relevance verdict per source.
- [ ] Pass
- **Failure signs:** says "looks fine" with no actual check.
- **If it fails:** give clearer citations (DOI/URL/title) and re-run.

### 9. `github-librarian` — repo/library research
- **Test:** "Find maintained React table libraries with TypeScript; compare stars and last release."
- **Expected:** A shortlist with health signals.
- [ ] Pass
- **Failure signs:** generic list, no recency/stars.
- **If it fails:** ask for "stars, last release date, open issues."

### 10. `codebase-recon` — read-only repo analysis
- **Test:** "Analyze this repo's git history for hotspots and bus factor. Do not change any code."
- **Expected:** A read-only report; **no file edits**.
- [ ] Pass
- **Failure signs:** tries to edit files; no analysis.
- **If it fails:** re-state "read-only, analysis only."

### 11. `brooks-lint` — principled code review
- **Test:** "Review [a small file] for design decay; cite the principle for each finding."
- **Expected:** Findings as Symptom→Source→Consequence→Remedy with citations.
- [ ] Pass
- **Failure signs:** vague nitpicks, no principles.
- **If it fails:** point it at a specific file and ask for cited findings.

### 12. `commit-narrator` — commit messages
- **Test:** (stage a small change) "Write a clear commit message for my staged changes."
- **Expected:** A structured message reflecting the diff.
- [ ] Pass
- **Failure signs:** generic "update files."
- **If it fails:** confirm changes are staged (`git add`) first.

### 13. `secret-guard` — secret scanning
- **Test:** "Scan my staged changes for leaked API keys or secrets; redact anything found."
- **Expected:** Flags/redacts secrets; **never prints the raw secret**.
- [ ] Pass
- **Failure signs:** prints a raw secret; misses an obvious key.
- **If it fails:** stage a file with a fake `API_KEY=sk-test123` to verify detection.

### 14. `env-lint` — env file check
- **Test:** "Compare my .env against .env.example; list missing/extra keys (names only)."
- **Expected:** Key-name diff; **no values shown**.
- [ ] Pass
- **Failure signs:** prints values; no diff.
- **If it fails:** ensure both `.env` and `.env.example` exist.

### 15. `mermaid-js-for-agents` — diagrams
- **Test:** "Create a Mermaid architecture diagram: React/Vite frontend + Supabase backend + Vercel hosting + Clerk auth."
- **Expected:** Valid Mermaid code you can render.
- [ ] Pass
- **Failure signs:** invalid syntax; prose instead of diagram code.
- **If it fails:** ask for "a ```mermaid code block, flowchart TD."

---
**When all 15 pass:** run the real-world scripts — `reports/cards-guy-real-world-test-script.md` (writing) and `reports/coding-project-test-script.md` (coding) — then see `reports/next-decision-guide.md`.
