# Pop-out compositing contract

## Canonical layers

```html
<video id="presenter-base" class="clip" src="presenter.mp4"
  data-start="0" data-duration="6" data-media-start="0"
  data-track-index="8" muted playsinline></video>

<div id="depth-copy">BEHIND YOU</div>

<video id="presenter-subject" class="clip" src="presenter-subject.webm"
  data-start="0" data-duration="6" data-media-start="0"
  data-track-index="7" muted playsinline></video>
```

Use CSS z-index for visual order: base `7`, depth text `8`, cutout `9`, foreground captions `14`.

```css
#presenter-base,
#presenter-subject {
  position: absolute;
  left: -40px;
  top: 970px;
  width: 1160px;
  height: 850px;
  object-fit: cover;
  object-position: 50% 48%;
}

#presenter-base {
  z-index: 7;
  clip-path: inset(190px 160px 70px 160px round 26px);
}

#depth-copy { position: absolute; z-index: 8; }
#presenter-subject { z-index: 9; }
```

The numbers are an example, not a template. Derive the side insets from the desired PiP width. Set the top inset where the box should cross the subject: hairline, ear, shoulder, or hands. Keep the media rectangle larger than the visible PiP to make the subject feel prominent while reducing room background.

## Motion

Apply one selector to both videos:

```js
tl.fromTo(
  "#presenter-base, #presenter-subject",
  { scale: 1.01 },
  { scale: 1.035, duration: 6, ease: "none" },
  0,
);
```

## End-frame rule

Background-removal output may be one or two frames shorter than the source. Inspect the last 0.2 seconds. Shorten the cutout clip or composition if the foreground disappears before the base; never allow a one-frame subject collapse.

## QA

- base and cutout are the same frame at every sampled timestamp;
- no doubled eye, mouth, shoulder, or microphone edge;
- no bright/dark RGB fringe at hair and hands;
- cutout does not cover essential B-roll or platform UI;
- depth text remains meaningfully legible after subject occlusion;
- lower foreground captions remain clear of the face;
- transparent WebM decodes in preview and final render.
