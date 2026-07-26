---
name: social-talking-head-video
description: Package existing talking-head, interview, tutorial, or founder footage into a polished short-form social video with word-timed dynamic captions enabled by default, picture-in-picture A-roll, full-screen B-roll, product or screen-recording inserts, motion graphics, calibrated motion-synced sound effects, brand assets, and platform-safe 9:16 framing. Use when creating or revising Instagram Reels, TikTok videos, YouTube Shorts, vertical tool demos, founder clips, or professional social edits from local video files and supporting assets.
---

# Social Talking-Head Video

Create a professional vertical social edit from existing speech-led footage. Preserve the source narration while designing an intentional rhythm between presenter, B-roll, product evidence, motion graphics, and semantic captions.

When a visual reference is useful, inspect [assets/example/standard-talking-head.mp4](assets/example/standard-talking-head.mp4). Treat it as a quality and structure example, not a template to copy blindly.

## 1. Run the intake gate before building

Read [references/intake.md](references/intake.md) and collect its three information groups in one concise round. Do not scaffold, transcribe, source media, or design frames until the intake is answered or the user explicitly delegates decisions.

If the user supplies files or folders, inventory them before proposing more assets:

```bash
python3 scripts/inventory_media.py /path/to/media --out media-inventory.json
```

Treat supplied material as specific creative direction, not merely input. State how each useful asset could appear in the edit.

## 2. Establish the technical workflow

Use HyperFrames as the default output framework unless the user explicitly selects another framework.

1. Read the installed `/hyperframes` skill, then `/hyperframes-core`, `/hyperframes-animation`, `/hyperframes-creative`, `/hyperframes-cli`, and `/media-use` only as needed.
2. Run `npx hyperframes skills update talking-head-recut` before relying on its workflow.
3. Run `npx hyperframes doctor` and confirm FFmpeg, FFprobe, Chrome, and local transcription are available.
4. Probe source and reference videos with FFprobe. Analyze reference footage with contact sheets, scene-change timings, and transcription rather than copying its surface appearance.
5. Scaffold the project with `npx hyperframes init ... --video <source>`, then write the confirmed intake to `BRIEF.md` immediately after initialization.

Do not re-ask questions already settled by this skill's intake. If another workflow owns a technical step, pass the confirmed `BRIEF.md` forward.

## 3. Analyze speech and assets

Transcribe to word-level timestamps. Prefer an explicit English model for known English speech:

```bash
npx hyperframes transcribe input.mp4 -d analysis/transcript --json --model small.en
python3 scripts/group_transcript.py analysis/transcript/transcript.json --out caption-groups.json
```

Correct product names, brands, APIs, acronyms, and technical terms without changing timestamps. Read the transcript for:

- the hook and payoff;
- named products, features, and steps that need proof on screen;
- natural B-roll opportunities;
- words that deserve caption emphasis;
- sections where the presenter should disappear so the evidence can take over.

## 4. Plan the edit before authoring

Read [references/editorial-system.md](references/editorial-system.md). Write a lightweight storyboard that maps each transcript beat to one primary visual role:

- presenter-led A-roll or bottom PiP;
- full-screen product or scroll B-roll;
- screen recording or website capture;
- focused motion graphic;
- payoff or CTA.

Default short-form rhythm when the user delegates decisions:

- 1080×1920, 30 fps;
- reserve the first 320 px for platform chrome; place essential hook text at `y >= 320`;
- first 1–3 seconds: active full-frame B-roll behind a borderless bottom PiP;
- change the dominant visual every 2–4 seconds;
- use at least two full-screen B-roll moments in a 20–40 second clip;
- return to the presenter between evidence beats so the edit breathes;
- keep one idea per frame and one visual climax near the end.

Do not force B-roll on a timer. Every insert must prove or clarify the current spoken idea.

## 5. Build the visual system

Use three depth layers: atmospheric background, primary content, and foreground accents/captions. Prefer editorial structure, strong type hierarchy, real product evidence, and hard cuts or short velocity-matched transitions.

### Presenter treatment

- Offer two treatments during intake: `standard` borderless PiP or `pop-out` layered PiP. Default to `standard` unless the user chooses pop-out or supplies a matching reference.
- Use a clean borderless PiP with 48–72 px side insets in portrait.
- Keep the face and gestures readable; use `object-position` deliberately.
- Never add a `PRESENTER` label.
- Avoid decorative borders, fake device chrome, or nested rounded frames unless a reference explicitly requires them.
- Hide the presenter during full-screen B-roll, dense product demonstrations, or hero motion-graphic beats.
- Preserve the original program audio on a separate root-level `<audio>` track.

For the pop-out treatment, read [references/presenter-treatments.md](references/presenter-treatments.md). Generate a real transparent subject layer with `hyperframes remove-background`, then align it exactly over a clipped copy of the same source so the head or hands can cross the PiP edge. Do not fake the effect with a shifted duplicate.

### Dynamic captions

Treat dynamic captions as a core deliverable. Enable them by default unless the user explicitly requests no captions. Do not substitute a few occasional callout cards for continuous spoken coverage.

Build captions from the corrected word-level transcript. Use short groups, generally one to three words or one compact phrase, and extend each group only to the next natural phrase boundary. The script determines scale and treatment:

- emphasize the word carrying the claim, action, number, brand, or payoff;
- keep connective words smaller;
- activate words on their spoken timestamps and hard-hide each group at its end;
- change style only when meaning or energy changes;
- avoid random color, rotation, or scale;
- keep one group visible at a time;
- keep captions inside platform-safe zones and away from faces;
- in a presenter PiP, default to a lower-chest rail rather than the vertical center of the card;
- inspect the longest two-line group and every layout change; technical in-frame status does not prove face clearance.
- Never place essential hook text, product names, or CTA copy in the top 320 px of a shared Reels/TikTok 1080×1920 master. Search bars, status controls, and upload-time UI can cover this area.

Copy or adapt [assets/caption-styles.css](assets/caption-styles.css). The five supplied treatments are `impact`, `stacked`, `neon`, `marker`, and `minimal`. Use a coherent subset of two to four in one video.

### B-roll and screen recordings

- When a user supplies a webpage URL, or research identifies a page worth showing, prefer a smooth scrolling webpage capture over a static full-page screenshot. Read [references/scrolling-webpage-broll.md](references/scrolling-webpage-broll.md).
- Capture the real page in a browser at a deterministic frame rate. Begin with a short hero hold, scroll with an eased curve, and optionally pause at the section that proves the spoken claim.
- Hide cookie banners, chat launchers, sticky signup bars, and other unrelated overlays before capture. Do not hide meaningful product UI or disclosure text.
- Use a viewport that fits the intended proof: desktop for layout and product breadth; mobile when responsive behavior is the subject. Record both only when the edit benefits from the contrast.
- Normalize high-frame-rate recordings to the composition fps and use dense keyframes for seek-safe rendering.
- Keep all `<video>` and `<audio>` elements as direct children of the HyperFrames composition root.
- Use `object-fit: cover` for portrait or crop-safe material; use a deliberate dark or branded stage for landscape recordings that must remain uncropped.
- Animate the media itself subtly with scale or translation only when the crop stays safe.
- Let full-screen evidence replace the presenter rather than shrinking both into unreadable panels.

### Motion-synced sound design

Read [references/sound-design.md](references/sound-design.md) before adding SFX. Run one semantic sound pass after motion timing is stable:

- short whoosh or swoosh for fast slides and major scene handoffs;
- soft pop for selected card, keyword, or headline landings;
- quiet wind-like sweep for a larger full-screen B-roll transition;
- no cue when the visual motion is too small to justify one.

Measure each source effect before mixing. Do not assume a small `data-volume` is audible: quiet pop assets often need `0.35–0.45`, common whooshes `0.30–0.40`, and sustained sweeps `0.18–0.25`. These are calibrated starting points, not universal constants. Keep speech dominant, avoid accenting every caption, and audition the rendered mix on ordinary speakers or headphones.

## 6. Avoid generated-looking shortcuts

Do not use generic rounded pills as decoration, especially status labels such as `Connected`, `Live`, `AI`, or `Presenter`. Also avoid:

- gratuitous glassmorphism and purple-blue gradients;
- repeated identical rounded cards;
- tiny web-layout typography;
- emoji standing in for real icons;
- random caption styling;
- empty solid backgrounds without structural or thematic depth;
- branding or claims not supported by supplied material.

Rounded shapes are acceptable when function demands them: PiP crops, real product UI, buttons present in source footage, or a specific approved reference.

## 7. Verify and review

Read [references/production-and-qa.md](references/production-and-qa.md) before checks or rendering.

1. Run `npx hyperframes lint` after the first full composition pass.
2. Add a `*.motion.json` sidecar for important entrances, ordering, and in-frame assertions.
3. Run `npx hyperframes check --snapshots` at transcript beats, every A-roll/B-roll handoff, and representative short and long caption groups.
4. Inspect the snapshots yourself with [assets/social-safe-zone-overlay.svg](assets/social-safe-zone-overlay.svg) as a guide. Automated success does not prove that screen recordings are readable, crops are flattering, or platform UI will not obscure text.
5. Open Studio with `npx hyperframes preview` and ask for final approval.
6. Render only after approval; use high quality for delivery.
7. Verify duration, dimensions, audio, file size, caption continuity and face clearance, SFX audibility, and peak headroom. Compare against a no-SFX reference or inspect cue windows when practical.

## 8. Deliver durable artifacts

Preserve:

- `BRIEF.md` with intake decisions and asset uses;
- corrected word-level transcript;
- storyboard or beat map;
- source composition and motion assertions;
- normalized local media;
- final MP4;
- reference-analysis notes when a style reference was supplied.

Checkpoint meaningful approved versions in Git before large stylistic experiments.

## Installation

Install from a local checkout by copying this folder into the harness skill directory, keeping `SKILL.md`, `agents/`, `scripts/`, `references/`, and `assets/` together.

Common locations:

```bash
# Codex
cp -R social-talking-head-video "${CODEX_HOME:-$HOME/.codex}/skills/"

# Universal agents directory used by several coding harnesses
cp -R social-talking-head-video "$HOME/.agents/skills/"
```

For a published Git repository, compatible harnesses can use the Skills CLI:

```bash
npx skills add <owner>/<repo>
```

Install HyperFrames separately with `npx hyperframes skills update talking-head-recut`. The skill repository does not vendor the HyperFrames runtime.
