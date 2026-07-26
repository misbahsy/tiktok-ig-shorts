# Scrolling Webpage B-roll

Use a real browser scroll recording when a URL is supplied or web research finds a page that materially supports the narration. A moving page usually reads as better evidence and more polished B-roll than a static screenshot.

## Choose the right artifact

- Use a scrolling clip for page design, feature discovery, portfolios, landing pages, articles, repositories, changelogs, or any claim spanning more than one viewport.
- Use a static screenshot for a single small UI state, a chart that must remain readable, or a page that cannot be captured reliably.
- Ask before entering credentials or crossing an authentication boundary. Capture only content the user is authorized to access.
- Preserve the page's real identity. Do not fabricate interactions, claims, testimonials, prices, or product states.

## Capture with Rollberry

[Rollberry](https://github.com/co-r-e/rollberry) records deterministic browser frames and encodes them as a smooth video. Its eased top-to-bottom capture, selector waits, and overlay hiding are well suited to social-video B-roll.

```bash
npx rollberry capture "https://example.com" \
  --out assets/video/example-scroll.mp4 \
  --viewport 1440x900 \
  --fps 60 \
  --duration auto \
  --motion ease-in-out-sine \
  --wait-for selector:main \
  --hide-selector '#cookie-banner' \
  --hide-selector '.intercom-lightweight-app'
```

Use repeated `--hide-selector` flags only for irrelevant chrome such as consent notices, chat bubbles, or sticky signup prompts. Inspect the page first so selectors are specific and safe.

For a directed capture with a hero hold, section stops, clicks, or multiple outputs, create a Rollberry project file and run:

```bash
npx rollberry render rollberry.project.json
```

Useful timeline pattern:

1. Pause on the hero for 0.35–0.7 seconds.
2. Scroll to the section named in the narration over 1.0–1.8 seconds.
3. Pause for readability.
4. Continue to the next meaningful section or the page bottom.

Prefer `ease-in-out-sine` for an editorial glide. Use linear motion only for deliberate technical inspection. A fixed 6–10 second duration is often better than `auto` for very long pages.

## HyperFrames capture fallback

If Rollberry cannot run, capture the page assets and viewport screenshots with:

```bash
npx hyperframes capture "https://example.com" -o capture/example
```

This produces overlapping viewport images and extracted site assets. Animate those images with a controlled vertical pan only after verifying that seams, sticky headers, and repeated fixed elements do not reveal the construction. A true browser scroll clip remains preferred.

## Prepare and edit

- Probe the output with FFprobe and normalize it to the composition frame rate when needed.
- Use the scroll clip full-frame for major proof beats, or place it in the upper content field above a presenter PiP.
- Crop landscape capture deliberately for 9:16. Keep the active page column, headline, product UI, or repository content readable.
- Begin and end on stable frames. Avoid cutting mid-scroll unless the transition is velocity matched.
- Add a quiet wind or scroll whoosh only when the movement warrants it; keep speech dominant.
- Do not show browser tabs, personal bookmarks, notifications, query strings containing secrets, private account data, or unrelated local UI.

## QA

Inspect the first frame, target section, fastest scroll moment, and final frame. Confirm that text remains legible, the page has finished loading, fonts are stable, cookie/chat overlays are absent, no private data is exposed, and the clip supports the exact spoken claim.
