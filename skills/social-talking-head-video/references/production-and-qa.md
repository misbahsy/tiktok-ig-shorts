# Production and QA

## Media preparation

Probe all assets before composition. Normalize screen recordings when needed:

```bash
ffmpeg -y -i input.mov -vf "fps=30" \
  -c:v libx264 -crf 18 -g 30 -keyint_min 30 -sc_threshold 0 \
  -pix_fmt yuv420p -movflags +faststart -an output.mp4
```

Re-encode the talking head with dense keyframes and preserve audio:

```bash
ffmpeg -y -i input.mp4 \
  -c:v libx264 -crf 17 -g 30 -keyint_min 30 -sc_threshold 0 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 160k output.mp4
```

Never overwrite user originals.

## HyperFrames invariants

- Keep media elements as direct children of the composition root.
- Keep visual videos muted and mount source program audio separately.
- Use one paused, synchronously registered GSAP timeline.
- Use deterministic timing; no network, wall-clock state, or infinite animation.
- Put timing on direct-root clips and use non-overlapping tracks.
- Use transforms and opacity for motion.
- Keep all media and fonts local.

## Review timestamps

Sample:

- 0.5–1 second into the hook;
- the middle of every A-roll and B-roll beat;
- 0.1 second before and after each handoff;
- every product/brand mention;
- the last readable payoff frame.

Check:

- essential top text begins at or below `y=320` on a 1080×1920 shared Reels/TikTok master;
- the safe-zone overlay does not intersect hook text, product names, prices, or CTA copy;
- speaker crop and face clearance;
- pop-out subject and base layer remain frame-synchronized with no doubled face, RGB halo, matte chatter, or visible seam at the PiP edge;
- screen recording readability;
- continuous caption coverage except intentional pauses;
- word-level caption sync and corrected spelling;
- caption contrast, platform safe zones, and face clearance;
- the longest two-line caption and largest emphasis treatment in every presenter geometry;
- unwanted labels, borders, status pills, cursors, browser chrome, or watermarks;
- black/blank media frames;
- audio continuity across visual cuts;
- whether every intended SFX cue is actually audible beneath speech;
- whether SFX ever mask consonants, product names, numbers, or the CTA;
- whether the final mix retains at least 3 dB of true-peak headroom;
- spelling of brands and technical terms.

## Commands

```bash
npx hyperframes lint --verbose
npx hyperframes check --snapshots --at "0.8,3.2,6.4,9.6"
npx hyperframes preview
```

For platform-UI review, composite or visually align `assets/social-safe-zone-overlay.svg` over representative snapshots. The overlay is a conservative shared-platform guide, not a promise that every app version uses identical chrome.

After explicit approval:

```bash
npx hyperframes render --quality high --fps 30 --output renders/final.mp4
ffprobe -v error -show_entries format=duration,size \
  -show_entries stream=codec_type,codec_name,width,height,r_frame_rate \
  -of json renders/final.mp4
```

For a composition with SFX, follow the measurement and rendered-delta checks in [sound-design.md](sound-design.md). Listening is still mandatory: successful muxing and similar integrated loudness do not prove that short effects are perceptible.

## Git checkpoints

Create a checkpoint before broad visual experiments. Keep generated caches and renders ignored unless the user asks to version them. Use descriptive commits such as:

- `Checkpoint approved editorial cut`
- `Add full-screen product B-roll rhythm`
- `Add alternate brand-styled variant`
