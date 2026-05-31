# Creative / Image / Video / Identity Tools

Focused view of the marketplace's creative capabilities and the honest state of identity/character consistency for Codex.

## What's installable now (added across all runs)

| Plugin | Capability | Needs | Platform |
|---|---|---|---|
| `nyldn-img` | Real image generation — OpenAI **gpt-image-2** + Google **Gemini** image | OpenAI and/or Gemini API key | Win unverified |
| `higgsfield` | Image **+ video** gen across 30+ models (Seedance, Veo, Kling, Nano Banana, GPT Image) + **Soul ID** face-consistent identity + product/marketplace shoots | paid Higgsfield account (CLI login) | Win unverified |
| `pika` | Pika creative suite — video, image, audio/voice, lipsync, captions, brand identity (58 MCP tools) | Pika account (OAuth) + credits | Windows OK |
| `aether` | Visual memory + prompt refinement for image gen | API | Windows OK |
| `image-studio` | Image editing/studio workflows | API | Windows OK |
| `comfy-workflow` | Manage/validate/convert **ComfyUI** workflows (local image/video gen) | local ComfyUI install | Windows OK |
| `roboflow` | Computer-vision pipelines: dataset, label, train, infer (official Roboflow) | Roboflow API key | Windows OK |
| `fiftyone` | CV dataset curation/evaluation (Voxel51) | — | Windows OK |
| `video-vision` | Video review / vision analysis | API | Windows OK |
| `maquette` | Image-guided web design → coded components + tokens | (image backend) | Windows OK |
| `remotion-external` | Programmatic video from React/Remotion | — | Windows OK |
| `vidseeds` | Video SEO/metadata/thumbnails for existing videos | VidSeeds PAT | Windows OK |
| `agent-vision` | Local camera frames | — | **macOS-only** |
| `hyperframes` *(in fork)* | HTML/CSS → MP4 video (HeyGen HyperFrames) | — | Windows OK |
| `heygen` *(in fork)* | HeyGen avatar video + 175-language dubbing | HeyGen API key | Windows OK |

## Identity / height / body / character consistency — honest finding
**There is still NO dedicated Codex-native plugin (`.codex-plugin/plugin.json`) whose purpose is identity-lock, height-lock, body-size continuity, or same-person video.** Confirmed again via GitHub-wide code search (May 2026).

**However, the closest *real, installable* options are now in your marketplace:**
1. **`higgsfield` → Soul ID** — trains a face-faithful identity model from photos and reuses it across image/video generations. This is the most practical path to character consistency today. (Needs a paid Higgsfield account.)
2. **`heygen`** *(already in the fork)* — persistent avatar identity for talking-head/presenter video.

**Toolkits that exist but are NOT Codex plugins (would need wrapping):**
- `awesome-genmedia/skills` — Claude-format; wraps **InstantID, IP-Adapter, PhotoMaker, ControlNet, FLUX LoRA, face-swap, StoryDiffusion** via eachlabs.ai. Closest to true identity/character control, but Claude-plugin format → needs a Codex wrapper.
- `hunix/HoC-Republic` — proprietary format; MagicAnimate/OmniGen/StoryDiffusion/FaceFusion/DeepFaceLab. Experimental, 0 stars — treat with caution.

## Best path for identity / height / body continuity
1. **Now:** use `higgsfield` Soul ID (reusable identity) for consistent character across generations; use `heygen` for avatar/presenter continuity.
2. **If you need ControlNet/IP-Adapter/InstantID-level control:** wrap `awesome-genmedia/skills` (Claude→Codex) — requires a small wrapper plugin + eachlabs.ai key. (Custom-build; needs your approval.)
3. **Height/body-size continuity specifically:** no off-the-shelf solution in any agent ecosystem. Achievable via ComfyUI (`comfy-workflow`) with ControlNet/pose+reference, or via a custom skill encoding your continuity rules — **custom build, your approval required.**

> Per your standing instruction, no custom identity/height skills were created. The above are real, installable, ready-made options plus an honest gap statement.
