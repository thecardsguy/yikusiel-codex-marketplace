# Coding / Project Test Script

Tests `codebase-recon`, `brooks-lint`, `commit-narrator`, `secret-guard`, `env-lint`, `mermaid-js-for-agents` on a real repo. **Start read-only** — none of these should change your code in the test (only `commit-narrator` touches git, and only to read the diff).

> Run these from inside a repo you don't mind exploring (e.g. a copy of a Cards Guy / DisputeIQ project). Read-only steps first; do the staged-change steps last.

## 1. Repo overview (read-only) — `codebase-recon`
> "Analyze this repository's git history: surface hotspots, bus factor, bug-magnet files, and overall structure. **Do not modify any files** — analysis only."

**Pass if:** you get a read-only report and **zero file edits**.

## 2. Code quality review (read-only) — `brooks-lint`
> "Review `[path/to/a/source/file]` for design decay using classic software-engineering principles. For each finding give Symptom → Source → Consequence → Remedy and cite the principle. Do not edit the file."

**Pass if:** principled, cited findings; no edits.

## 3. Env / secrets check (read-only) — `env-lint` + `secret-guard`
> "1) Compare `.env` against `.env.example` and list missing or extra keys — **key names only, never values**. 2) Scan the working tree (or staged changes) for leaked API keys, tokens, or secrets and **redact** anything found — never print the raw secret."

**Pass if:** env diff shows only key names; `secret-guard` flags/redacts (test it by adding a fake `STRIPE_KEY=sk_test_fake123` to a staged file first).

## 4. Architecture diagram — `mermaid-js-for-agents`
> "Create a Mermaid diagram (flowchart TD, in a ```mermaid code block) of this app's architecture: frontend, backend/API, database, auth, hosting, and external services."

**Pass if:** valid Mermaid you can paste into a renderer.

## 5. Commit summary — `commit-narrator`
> (First make a tiny change and `git add` it.) "Write a clear, conventional commit message for my currently staged changes, with a one-line summary and a short body."

**Pass if:** the message reflects the actual diff (not generic).

## Suggested order & safety
1. **Read-only first:** `codebase-recon` → `brooks-lint` → `env-lint` → `secret-guard` → `mermaid-js-for-agents`. None should write files.
2. **Then git-aware:** `commit-narrator` (reads staged diff; writes only a message you choose to use).
3. If any plugin tries to **edit files** during these tests, stop it and note the issue — these should be advisory/read-only here.

## What this proves
A passing run means you can hand any repo to these tools to (a) understand it fast, (b) get principled review, (c) catch leaked secrets and env drift, (d) document architecture, and (e) write clean commits — all without surprise file changes.
