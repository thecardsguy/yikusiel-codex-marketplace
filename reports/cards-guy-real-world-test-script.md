# The Cards Guy — Real-World Test Script

Tests whether the writing/research stack can refresh a real credit-card page **without sounding AI-generated and without inventing facts.** Run after installing `writers-loop`, `unslop`, `citecheck`, `microsoft-docs`, `github-librarian`, `claude-mem`.

## Master prompt (copy-paste into Codex)

> You are helping refresh a credit-card page for The Cards Guy (U.S. credit cards only). Here is the existing draft:
> ```
> [PASTE YOUR EXISTING PAGE SECTION HERE]
> ```
> Do all of the following, in order:
> 1. **Identify unsupported claims** — list every statement (APR, fee, bonus, benefit, "best/biggest/lowest") that is not backed by a cited source, and mark each as `confirmed`, `rumored`, or `needs-verification`.
> 2. **Improve human tone** — rewrite in a seasoned human finance-editor voice: professional, readable, no filler, no hype.
> 3. **Keep U.S. credit-card focus** — remove anything not relevant to U.S. cards.
> 4. **Avoid AI-style wording** — no "game-changer", "plethora", "in today's fast-paced world", "unlock", "dive in", em-dash overuse, or hedging stacks.
> 5. **Do not invent facts** — never add or change a number; if a figure is needed but missing, insert `[VERIFY: <what to check> on the issuer page]`.
> 6. **Flag verification points** — list exactly which facts I must confirm on the **issuer page** and which on a **reliable finance source**.
> 7. **Produce the clean revised section** — the rewritten copy, ready to paste.
> 8. **Change log** — a short bullet list of what you changed and why.
> Output four labeled parts: **Unsupported claims**, **Verification points**, **Revised section**, **Change log**. Do not rewrite the facts I didn't give you.

**Pass if:** it lists unsupported claims, never invents numbers (uses `[VERIFY: …]`), the revised copy reads human, and the change log is honest.

## Per-plugin focused tests

**`writers-loop`** — "Using ONLY these verified facts [paste], draft a 200-word 'who it's for' section for the Amex Gold, human expert tone, U.S. only, no invented numbers." → *structured, fact-bounded draft.*

**`unslop`** — "Rewrite to read like a human editor, change zero facts: *In today's fast-paced world, this card is a true game-changer that unlocks a plethora of rewards.*" → *clean, natural, same meaning, AI-isms gone.*

**`citecheck`** — "Verify these sources exist and are relevant to a claim that the average U.S. credit-card APR is ~21%: [paste 2 citations]." → *existence + relevance verdict per source.*

**`microsoft-docs`** — "Find official Microsoft docs for using Azure AI Content Safety to moderate user comments on a finance blog." → *cites Microsoft Learn pages.*

**`github-librarian`** — "Find maintained open-source React components for affiliate-disclosure banners / comparison tables, TypeScript, compare stars + recency." → *shortlist with health signals.*

## Combined mini-workflow (end-to-end)
1. `microsoft-docs` / `github-librarian` → gather any docs/components you need.
2. Master prompt above with `writers-loop` doing the draft.
3. `unslop` on the revised section.
4. `citecheck` on any sources you cited.
5. Manually confirm every `[VERIFY: …]` against the issuer page before publishing.
6. `claude-mem`: "Remember the Cards Guy style rules I just used" — so the next page is consistent.

> **Golden rule:** the stack drafts and edits; **you and the issuer page own the facts.** Never publish a `[VERIFY: …]` you haven't confirmed.
