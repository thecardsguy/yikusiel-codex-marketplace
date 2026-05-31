# Creative / Image / Video / Identity Tools

Practical view of the marketplace's creative capabilities. **No images or videos are generated here** — this catalogs installable tools.

## Already installed (across all runs)
| Plugin | Capability | Needs | Platform |
|---|---|---|---|
| `nyldn-img` | Image gen — OpenAI gpt-image-2 + Gemini | API keys | Win unverified |
| `higgsfield` | Image **+ video** (30+ models) + **Soul ID** face-consistent identity + product shoots | paid Higgsfield acct | Win unverified |
| `pika` | Pika suite — video, image, audio, lipsync, captions, brand (58 tools) | Pika OAuth + credits | Windows OK |
| `comfy-workflow` | Manage/validate **ComfyUI** workflows (local image/video gen) | local ComfyUI | Windows OK |
| `roboflow` | Computer-vision pipelines (dataset/label/train/infer) | Roboflow key | Windows OK |
| `fiftyone` | CV dataset curation/evaluation | — | Windows OK |
| `image-studio` | Image editing/studio | API | Windows OK |
| `video-vision` | Video review / vision analysis | API | Windows OK |
| `aether` | Visual memory + prompt refinement | API | Windows OK |
| `maquette` | Image-guided web design → coded components | (image backend) | Windows OK |
| `remotion-external` | Programmatic video from React/Remotion | — | Windows OK |
| `vidseeds` | Video SEO/metadata/thumbnails for existing videos | VidSeeds PAT | Windows OK |
| `agent-vision` | Local camera frames | — | **macOS-only** |
| `hyperframes` *(fork)* | HTML/CSS → MP4 video | — | Windows OK |
| `heygen` *(fork)* | HeyGen avatar video + 175-lang dubbing | HeyGen key | Windows OK |

## Added this run
No new **image/video/identity-native** plugin was added this run (none surfaced that wasn't already covered). New adds that *support* creative work: `firecrawl` (scrape references/competitor visuals), `citecheck` (verify sourced claims), `microsoft-docs` (Azure OpenAI image APIs). For screenshots/visual & browser review you already have `chrome-devtools`, `kachilu-browser`, `browser-bridge`, `computer-use-windows`.

## Install first (creative)
1. `maquette` + `comfy-workflow` (zero remote account if you run ComfyUI locally) · `fiftyone` · `remotion-external`.
2. Then, when you have accounts: `pika` → `nyldn-img` → `higgsfield`.

## Requires accounts
`pika`, `higgsfield`, `nyldn-img`, `aether`, `image-studio`, `video-vision`, `roboflow`, `vidseeds`, fork `heygen`.

## Identity / face / body / height / scene continuity — honest status
**Still NO dedicated Codex-native plugin** for identity-lock, face consistency, body/height/scale continuity, or same-person video. Re-confirmed this run.

**Best real, installable paths today:**
1. **`higgsfield` → Soul ID** — trains a face-faithful identity model, reusable across image/video. Closest thing to same-person consistency.
2. **`heygen`** *(fork)* — persistent avatar identity for presenter/talking-head video.
3. **`comfy-workflow`** — drive a local ComfyUI graph with ControlNet/IP-Adapter/pose+reference for fine-grained face/pose/scene control (you supply the ComfyUI setup).

**Needs wrapping (closest dedicated toolkit, not Codex-native):** `awesome-genmedia/skills` — InstantID, IP-Adapter, PhotoMaker, ControlNet, LoRA, StoryDiffusion (via eachlabs.ai). It's a Claude-plugin → would need a small Codex wrapper (see `skill-wrapping-backlog.md`).

**Still needs a custom skill later (your approval):** true **height / body-size continuity** across shots has no off-the-shelf solution in any agent ecosystem — it would be a bespoke skill encoding your continuity rules on top of ComfyUI or Soul ID.
