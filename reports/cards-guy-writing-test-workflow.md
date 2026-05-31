# The Cards Guy — Writing Test Workflow

A repeatable workflow to rewrite a credit-card page so it reads **expert and human, not AI-generated** — without inventing facts. Use after installing Day-1/Day-2 plugins (`writers-loop`, `unslop`, `claude-mem`, `microsoft-docs`, `citecheck`, `github-librarian`). The AI writes/edits; **you and your sources own the facts.**

## 1. Input needed
- **Existing page text** (the draft to refresh).
- **Target card/product** (e.g., Chase Sapphire Preferred).
- **Verified sources** — the issuer's official card page + 1–2 reliable finance sources.
- **Desired tone** — human expert, professional, readable; your editorial style.

## 2. Research step (facts before prose)
1. **Issuer page first** — pull APR, annual fee, sign-up bonus, benefits directly from the issuer. This is the source of truth.
2. **Reliable finance source second** — corroborate with `factset`/`dow-jones-factiva`/`morningstar` (already in your marketplace) or a reputable finance publication.
3. **SEO source third** — `codex-seo`/`semrush` for structure/keywords (last, and only what truly helps).
> Log every fact with its source. Anything you can't source from the issuer or a reliable outlet = **rumored**, and must be labeled.

## 3. Drafting step — `writers-loop`
Prompt it with your facts + tone, in a frame → plan → draft → critique → revise loop. Keep your editorial voice; it should not introduce any number you didn't supply.

## 4. Humanizing step — `unslop`
Run on the near-final draft at low/medium intensity to strip AI tells (filler, hedging stacks, em-dash overuse). Confirm no facts changed.

## 5. Fact-checking step
- `citecheck` — verify any cited sources/studies exist and are relevant.
- **Manual source review** — re-open the issuer page; confirm every APR/fee/bonus/benefit matches exactly.

## 6. Final review checklist
- [ ] No made-up facts — every figure traces to the issuer or a reliable source.
- [ ] U.S. credit cards only.
- [ ] Confirmed vs **rumored** clearly labeled.
- [ ] No generic AI filler; human expert tone.
- [ ] No exaggerated claims ("best card ever").
- [ ] No over-linking; affiliate links minimal + disclosed.
- [ ] Tables only where they aid clarity.

## 3 copy-paste test prompts for Codex
**A — Draft from verified facts**
> "Using ONLY these verified facts from the issuer page [paste facts], write a 200-word section on the Chase Sapphire Preferred sign-up bonus for The Cards Guy. Human expert tone, U.S. cards only, no invented numbers, label anything not in my facts as 'rumored'."

**B — Humanize without changing facts**
> "Rewrite the following to read like a seasoned human finance editor — remove AI-sounding phrasing and filler, keep every fact and figure exactly the same, no new claims: [paste draft]."

**C — Fact-check pass**
> "Review this draft against my source list [paste sources]. Flag any statement not supported by a source, any figure that doesn't match the issuer page, and any claim that should be labeled 'rumored' rather than 'confirmed'. Do not rewrite — just list issues."

## What this test proves
If A produces a clean draft with no invented numbers, B keeps facts identical while sounding human, and C catches unsupported claims, your writing stack is ready for real Cards Guy page refreshes.
