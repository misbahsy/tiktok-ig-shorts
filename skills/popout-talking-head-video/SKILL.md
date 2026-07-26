---
name: popout-talking-head-video
description: Create or revise a vertical talking-head social edit so the presenter breaks out of a rounded picture-in-picture frame using a synchronized transparent subject layer, with optional text or graphics placed behind the presenter. Use for pop-out presenter, cutout speaker, subject-over-frame, text-behind-person, or layered depth effects in TikTok, Instagram Reels, and YouTube Shorts.
---

# Pop-out Talking-Head Video

Build a real layered presenter composite, not a shifted duplicate. Use this skill alone for an existing composition or alongside `$social-talking-head-video` for a complete edit.

Inspect [assets/example/popout-presenter.mp4](assets/example/popout-presenter.mp4) when a concrete reference for the layered edge breakout is useful.

## Intake

Confirm:

- presenter source and target 9:16 composition;
- whether the breakout should include hair only, ears and head, upper shoulders, or expressive hands;
- whether captions stay in front or selected phrases sit behind the presenter;
- whether the effect applies to every presenter appearance or selected hero beats.

Reject or reduce the effect when the source already cuts off the intended hair, hands, or shoulders.

## Build

1. Read `/hyperframes`, `/hyperframes-core`, `/hyperframes-cli`, and `/media-use` background-removal guidance.
2. Preserve the approved edit on a branch or Git checkpoint.
3. Generate an alpha-matted copy from the exact presenter source:

```bash
npx hyperframes remove-background presenter.mp4 \
  -o assets/video/presenter-subject.webm --quality best
```

4. Keep three synchronized layers:

   - original presenter video clipped to the PiP rectangle;
   - optional text/graphics layer;
   - transparent presenter WebM above both.

5. Make both videos direct composition-root children. Match `data-start`, `data-duration`, `data-media-start`, dimensions, `object-fit`, `object-position`, transform origin, and every motion tween exactly.
6. Clip only the original presenter layer. Resize or reposition both video layers together; never independently enlarge or shift the cutout.
7. Keep program audio on one separate root-level `<audio>` element.

Read [references/compositing.md](references/compositing.md) for the canonical geometry and QA contract.

## Captions and depth text

Use ordinary captions in a foreground layer. For selected high-value phrases, place text between the clipped base and cutout:

- keep the phrase short and oversized;
- use negative space behind the head or shoulders;
- allow intentional partial occlusion by the presenter;
- never hide the entire key word;
- keep platform controls and essential product proof clear.

Use `$kinetic-caption-video` when captions should roam between foreground, upper-field, and depth zones across the timeline.

## Verify

Snapshot still and gesture moments at full resolution. Check hair, ears, microphone, fingers, shoulders, and the PiP seam. Reject doubled facial edges, matte chatter, color halos, frame drift, or an end-frame cutout drop.

Run `npx hyperframes check --snapshots --frame-check`, then open Studio for approval. Render only after approval.
