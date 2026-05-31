# Credit-Card / Finance Writing Stack (The Cards Guy)

A focused workflow for writing **expert, humanized, factually-careful U.S. credit-card content** using plugins that are actually in this marketplace. All financial facts must be verified against issuer pages and reliable sources — the LLM is the writer/editor, not the source of truth.

## Best plugins for humanized writing
- **`writers-loop`** — multi-stage frame → plan → draft → critique → revise; keeps editorial control, learns your style. *Primary drafting tool.*
- **`unslop`** — strips AI-isms (sycophancy, hedging, em-dash overuse, filler) so copy reads human. *Run last, on the near-final draft.*
- **`content-planner`** — outline/structure before writing.
- *(Claude-only candidate: a dedicated brand-voice skill — see `skill-wrapping-backlog.md`.)*

## Best plugins for financial / credit-card research
- **Primary, high-trust:** `dow-jones-factiva`, `factset`, `lseg`, `morningstar`, `quartr`, `cb-insights`, `aiera`, `daloopa` (issuer/market data, earnings, filings).
- **Web research:** `gpt-researcher` (multi-source synthesis), `firecrawl` (scrape issuer pages / competitor pages), `github-librarian` (find data/tools).
- **Markets:** `tradingview`.
- **Save/recall sources:** `readwise`.
> For card terms, APRs, bonuses, and benefits: pull from **issuer pages** (via `firecrawl`) and confirm against Factiva/FactSet. Do not state a number you can't source.

## Best plugins for SEO and page improvement
- **`codex-seo`** (19-skill audit), **`enterprise-seo`**, **`semrush`**, **`similarweb`** (keywords, competitors, gaps), **`digital-marketing`**, **`adsense-readiness`** (monetization readiness).

## Best plugins for fact-checking and avoiding mistakes
- **`citecheck`** — verify citations/sources exist and are relevant.
- **`scite`** — citation strength / supporting vs disputing.
- **`gpt-researcher`** + **`firecrawl`** — cross-check claims against primary sources.
- **`factset` / `dow-jones-factiva`** — confirm financial figures.

## Workflow: rewrite a credit-card page so it sounds expert (not AI)
1. **Research first (facts before prose):** `firecrawl` the issuer page + 2–3 reliable sources; pull confirmed APR/fees/bonus/benefits. Log each fact with its source.
2. **Verify:** run `citecheck`/`scite` on any cited studies; confirm figures via `factset`/`factiva`. Mark anything unconfirmed as **rumored**.
3. **Outline:** `content-planner` → structure around user intent (eligibility, bonus, benefits, fees, who it's for).
4. **Draft:** `writers-loop` in your editorial voice — expert, plain English, no filler, no fake certainty, tables only when they aid clarity.
5. **SEO pass:** `codex-seo` + `semrush` for keyword/structure gaps — apply only what improves the page (no SEO fluff, no over-linking).
6. **De-AI pass:** `unslop` at low/medium intensity to remove AI tells while preserving your voice.
7. **Final fact gate:** re-confirm every number against the issuer page; label confirmed vs rumored; keep affiliate links minimal and disclosed.

## Do NOT rely on these for financial accuracy
- `unslop`, `writers-loop` (style/structure only — they don't verify facts).
- Generic LLM output, `codex-seo`/SEO tools, image/design tools — none confirm APRs, fees, or bonuses.
- Always treat issuer pages + `factset`/`factiva`/`morningstar` as the source of truth.

## Editorial guardrails (enforce in `writers-loop` prompt)
Human expert tone · professional but readable · no generic AI wording · no filler · no fake certainty · **no made-up financial facts** · U.S. credit cards only · clearly label confirmed vs rumored · cite issuer pages + reliable finance sources · preserve your editorial style · avoid SEO fluff · avoid over-linking · tables only when they help clarity.
