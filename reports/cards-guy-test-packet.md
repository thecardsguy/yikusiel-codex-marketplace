# The Cards Guy — Test Packet

A complete, self-contained scenario to test the writing/research stack end-to-end. It uses a **FICTIONAL** card so nothing here asserts real-world facts.

> ⚠️ **The "verified facts" below are fictional placeholders for testing only.** For a real page, delete them and use facts confirmed on the actual issuer's page. Never publish these numbers.

## The scenario
You're refreshing a product section for the **"Summit Bank Cash Rewards Card"** (fictional, U.S. consumer credit card).

### A. Sample page section (existing draft to refresh)
> The Summit Bank Cash Rewards Card is a solid everyday card. It gives you cash back on your purchases and has no annual fee. There's a welcome bonus for new cardholders and some travel perks. It's a good choice for most people who want to earn rewards.

### B. Verified facts (FICTIONAL — for testing)
- Annual fee: **$0** *(confirmed — example)*
- Rewards: **3% cash back on groceries, 1% on everything else** *(confirmed — example)*
- Welcome offer: **$200 after $1,000 spend in 90 days** *(confirmed — example)*
- Foreign transaction fee: **3%** *(confirmed — example)*
- Intro APR: **UNKNOWN — must verify on issuer page**
- "Travel perks": **UNKNOWN — not in verified facts**

### C. Bad AI-sounding version (what to avoid)
> In today's fast-paced financial landscape, the Summit Bank Cash Rewards Card is an absolute game-changer that unlocks a plethora of unparalleled benefits. Whether you're a seasoned spender or just diving in, this card's robust rewards ecosystem and myriad travel perks make it hands-down the best card for everyone — it's a no-brainer!

## Test prompts

### 1. `writers-loop` — draft from verified facts only
> Using ONLY the verified facts below, write a ~140-word "who it's for" section for the Summit Bank Cash Rewards Card (U.S. card). Human expert tone, professional and readable. Do NOT add any benefit, perk, or number not in my facts. For anything missing (e.g., intro APR, travel perks), insert `[VERIFY: <what to check> on the issuer page]` instead of guessing.
> Verified facts: $0 annual fee; 3% groceries / 1% everything else; $200 after $1,000 in 90 days; 3% foreign transaction fee; intro APR unknown; travel perks unknown.

**Pass if:** no invented benefits/perks, uses `[VERIFY: …]` for unknowns, reads human.

### 2. `unslop` — humanize without changing facts
> Rewrite the following to read like a seasoned human finance editor. Remove AI-sounding wording and hype, keep every fact and number identical, add no new claims:
> "[paste the bad AI-sounding version from section C]"

**Pass if:** AI-isms gone, no facts changed, no new perks added, no exaggeration.

### 3. `citecheck` — verify support
> Here is a draft section and the only sources I have. Flag every statement that is NOT supported by my facts/sources, mark each as `confirmed`, `unknown`, or `needs-verification`, and list exactly what I must confirm on the issuer page. Do not rewrite.
> Draft: [paste your draft]. Sources/facts: [paste section B].

**Pass if:** it flags "travel perks" and "intro APR" as unknown/needs-verification and doesn't rubber-stamp unsupported claims.

## Final review checklist (before "publishing")
- [ ] U.S. credit card only.
- [ ] No invented benefits or perks (nothing beyond verified facts).
- [ ] No invented welcome offer / numbers.
- [ ] Confirmed vs unknown clearly separated (`[VERIFY: …]` for unknowns).
- [ ] Human expert tone; no generic AI wording.
- [ ] No exaggerated claims ("best for everyone", "no-brainer", "game-changer").
- [ ] No over-linking; affiliate links minimal + disclosed.
- [ ] Tables only where they aid clarity.

**What a good result looks like:** a clean, human section that states only the confirmed facts, marks intro-APR and travel perks as `[VERIFY: …]`, and reads like an expert wrote it — not an AI.
