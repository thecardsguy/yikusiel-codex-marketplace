# Identity / Video Wrapping Plan

A practical plan for getting **same-person identity, face consistency, and body/height/scale continuity** into your workflow. **Nothing here is implemented** — it's a roadmap. Do not build the custom skills until you approve.

## What currently exists in the marketplace
- **`higgsfield`** — image + video generation across 30+ models, plus **Soul ID**: train a face-faithful identity model from photos and reuse its `reference_id` across generations. *Best current path to same-person consistency.* (Paid Higgsfield account.)
- **`heygen`** *(fork)* — avatar video; a persistent avatar identity for presenter/talking-head clips and 175-language dubbing. (HeyGen account.)
- **`comfy-workflow-mcp`** — manage/validate local **ComfyUI** workflows. With a local ComfyUI install you can run ControlNet, IP-Adapter, InstantID, PuLID, LoRA, pose/reference conditioning yourself. (Local ComfyUI; no cloud account.)
- **`pika` / `img` / `image-studio-mcp` / `aether`** — generation/editing, but **no built-in identity lock**.

## What each can do for identity/continuity
| Tool | Face identity | Body/height continuity | Scene continuity | How |
|---|---|---|---|---|
| `higgsfield` Soul ID | ✅ strong | ⚠️ partial | ⚠️ partial | trained identity model reused across shots |
| `heygen` | ✅ (avatar) | ❌ | ❌ | fixed avatar presenter |
| `comfy-workflow-mcp` (local) | ✅ (InstantID/IP-Adapter) | ⚠️ via pose/ControlNet | ✅ via reference/ControlNet | you build the graph |
| `awesome-genmedia/skills` (needs wrap) | ✅ (InstantID/PhotoMaker) | ⚠️ | ✅ (StoryDiffusion) | eachlabs.ai API |

## What `awesome-genmedia/skills` can do (wrap candidate)
A Claude-format plugin wrapping eachlabs.ai: **InstantID, InstantID+IP-Adapter, PhotoMaker, SDXL/FLUX ControlNet, FLUX LoRA, face-swap, StoryDiffusion** (character-consistent sequences). This is the closest ready-made identity/character toolkit. It is **not** a Codex plugin → must be wrapped.

**Wrapping it (reference, not executed):**
1. Fork `awesome-genmedia/skills` (or vendor its `skills/` into a small folder you control).
2. Add a `.codex-plugin/plugin.json` at the root: `name: "genmedia-identity"`, an `interface` block, `skills: "./skills/"`.
3. Add it to `.agents/plugins/marketplace.json` as a `git-subdir`/`url` source, `authentication: ON_INSTALL`.
4. Validate with `scripts/validate-marketplace.py --online`.
5. Provide the eachlabs.ai key only at use time (env var) — never commit it.
*Risk: medium (external paid API). Effort: ~1 small plugin. Needs your approval.*

## What a custom `identity-lock` skill would need
- Inputs: 1–3 reference photos of the person; a target prompt/scene.
- Pipeline: build/reuse an identity embedding (Soul ID `reference_id`, or InstantID/PuLID via ComfyUI), then generate with that identity conditioned on the prompt.
- Outputs: image/video with the same face; a stored `identity_id` for reuse.
- Guardrails: **only for people who consented**; no impersonation of real third parties; log the reference set used.

## What a custom `height-scale-lock` skill would need
*(No off-the-shelf solution exists anywhere — fully custom.)*
- A per-character **continuity sheet**: canonical height, body proportions, key measurements, and reference renders.
- Enforcement: pose/skeleton via ControlNet (OpenPose/DWPose) scaled to the continuity sheet; consistent camera distance/lens notes; optional post-gen check comparing rendered proportions to the sheet.
- Outputs: shots that keep the same height/scale relative to scene anchors.
- This is the hardest piece — likely an iterative ComfyUI graph + a validation step, encoded as a skill.

## Guardrails (for any identity/video skill)
- **Consent only** — identity tools used on people who agreed; no deepfakes of real third parties.
- No API keys in the repo; `ON_INSTALL` auth; keys via env.
- No auto-generation in CI; human-in-the-loop review of outputs.
- Label AI-generated media; respect each provider's ToS.

## Recommended first implementation path
1. **Now (no build):** use `higgsfield` Soul ID for same-person image/video; `heygen` for avatars. Validate it meets your bar before investing in custom work.
2. **If you need finer control:** stand up a local **ComfyUI** + use `comfy-workflow-mcp` to drive InstantID/IP-Adapter/ControlNet.
3. **If you want it as an installable plugin:** **wrap `awesome-genmedia/skills`** (small, safe, ~1 plugin) — *first custom step, on your approval*.
4. **Only if 1–3 are insufficient:** commission the custom **`identity-lock`** then **`height-scale-lock`** skills, with the guardrails above.

> Per your instruction, no custom identity/height skills were created. Approve a step and I'll scope it precisely.
