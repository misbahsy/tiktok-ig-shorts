---
name: kinetic-caption-video
description: Add continuous word-timed kinetic captions to talking-head and social videos, with semantic emphasis and intentional movement between lower rail, upper field, mid-frame, and behind-presenter depth zones. Use when captions should pop, resize, roam around the frame, alternate placement, become part of the scene, or sit behind a cutout presenter instead of remaining fixed at the bottom.
---

# Kinetic Caption Video

Create captions that participate in the edit rather than behaving like fixed subtitles. Use alone on an existing HyperFrames video or alongside `$social-talking-head-video` and `$popout-talking-head-video`.

Inspect [assets/example/kinetic-depth-captions.mp4](assets/example/kinetic-depth-captions.mp4) when a concrete reference for roaming and behind-presenter caption zones is useful.

## Source

Require corrected word-level timestamps. Generate and group them when needed:

```bash
npx hyperframes transcribe input.mp4 -d analysis/transcript --json --model small.en
python3 scripts/group_transcript.py analysis/transcript/transcript.json --out caption-groups.json
```

Correct brands, products, APIs, numbers, and acronyms without changing timestamps.

## Caption plan

Map every phrase to:

- one semantic emphasis word;
- one coherent treatment: impact, stacked, marker, minimal, or restrained standard;
- one placement zone: `bottom`, `top`, `mid`, or `depth`;
- entrance, active-word motion, and hard exit time.

Read [references/kinetic-system.md](references/kinetic-system.md). Copy or adapt [assets/caption-styles.css](assets/caption-styles.css).

Do not choose placement randomly. Move captions when negative space, scene meaning, or depth composition supports it. Keep one group visible at a time and activate words on their spoken timestamps.

## Depth captions

Depth captions require a real transparent presenter layer. Put the clipped room/PiP at z=7, depth text at z=8, cutout presenter at z=9, and foreground captions at z=14. Use `$popout-talking-head-video` for the compositing contract.

## QA

Inspect the longest phrase, largest emphasized word, every placement change, and every presenter geometry. Verify face clearance, product-proof clearance, WCAG contrast, hard group exits, and platform-safe placement. Intentional subject occlusion may hide part of depth text, but the phrase must remain recognizable.

Run `npx hyperframes check --snapshots --frame-check` and review a contact sheet before rendering.
