# Presenter treatments

## Standard borderless PiP

Use the original muted presenter video as a direct child of the composition root. Crop it with `object-fit: cover`, use 48–72 px portrait side insets, and keep program audio on a separate root-level `<audio>` track.

## Layered pop-out PiP

Use this treatment when the user requests the speaker to break the PiP edge and the source includes clean head or hand clearance. Reject it when hair, hands, or the intended breakout area are already cut off in the source.

Generate the transparent subject from the exact presenter source:

```bash
npx hyperframes remove-background presenter.mp4 \
  -o assets/video/presenter-subject.webm --quality best
```

Build two synchronized visual layers:

1. Base: the original presenter video, clipped to the rounded PiP rectangle.
2. Foreground: `presenter-subject.webm`, not clipped, above the base.

Both layers must:

- be direct children of the composition root;
- use identical `data-start`, `data-duration`, `data-media-start`, dimensions, `object-fit`, `object-position`, transform origin, and GSAP motion;
- use separate non-overlapping timeline tracks;
- remain muted while the original program audio plays once from its dedicated `<audio>` element.

Use one shared media geometry and clip only the base. The clip inset creates the PiP boundary while the foreground remains free to cross it:

```css
.presenter-base,
.presenter-subject {
  position: absolute;
  left: -20px;
  top: 1040px;
  width: 1120px;
  height: 784px;
  object-fit: cover;
  object-position: 50% 48%;
}

.presenter-base {
  z-index: 8;
  clip-path: inset(154px 88px 0 88px round 26px);
}

.presenter-subject {
  z-index: 9;
  filter: drop-shadow(0 -10px 16px rgba(0,0,0,.28));
}
```

Treat those numbers as a geometry example, not a template. Derive the inset from the intended PiP rectangle and source framing. The subject should cross the top edge by roughly 40–140 px without entering essential headline or product space.

Do not shift or independently scale the transparent subject to manufacture more breakout. Misaligned copies create doubled facial edges and moving seams. If more breakout is needed, enlarge or reposition both layers together, then recompute the base clip inset.

## QA

Inspect representative frames with the subject still and gesturing. Check hair, microphone, fingers, and shirt edges at full resolution. Verify:

- exact base/subject alignment;
- no flicker or matte chatter;
- no bright or dark RGB halo;
- no second face or body edge beneath the cutout;
- no collision with captions, headline, or platform controls;
- a clean visual seam where the subject crosses the PiP boundary.

Use `--quality best` when compositing the cutout over its own source; lower VP9 quality can expose color mismatch at the overlap.
