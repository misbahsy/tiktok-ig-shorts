# Motion-synced sound design

Use SFX to clarify motion, not to decorate every cut. Speech remains the primary audio layer.

## Cue map

| Visual event | Preferred cue | Placement |
| --- | --- | --- |
| Fast slide or major scene handoff | Short whoosh/swoosh | Start just before or exactly with motion |
| Card, keyword, node, or headline landing | Soft pop | Sync to the visual landing, not the animation start |
| Full-screen B-roll takeover | Airy or cinematic sweep | Trim so the swell leads into the takeover |
| Minor caption change | Usually none | Accent only a genuine hook, brand, or payoff |

Favor 6–12 meaningful cues in a 20–40 second edit. A clustered sequence may use staggered pops, but lower successive cue levels so it reads as one gesture.

## Resolve and inspect assets

Use the installed `/media-use` skill. Review candidates before resolving new files, then freeze selected assets locally.

Measure every source effect:

```bash
ffmpeg -hide_banner -nostats -i effect.mp3 \
  -af volumedetect -f null - 2>&1 | rg 'Duration|mean_volume|max_volume'
```

The source level determines the composition multiplier. A `data-volume="0.05"` multiplier is about −26 dB and will bury most SFX under narration.

## Calibrated starting levels

For typical bundled or normalized effects, start here:

| Cue | `data-volume` | Typical purpose |
| --- | ---: | --- |
| Short whoosh/swoosh | `0.30–0.40` | Slides and scene changes |
| Soft pop | `0.35–0.45` | Card/headline landings |
| Sustained wind/sweep | `0.18–0.25` | Full-screen transition bed |
| Small secondary accent | `0.25–0.35` | Selected caption or UI beat |

Adjust for the measured source and the voice recording. Target perceived SFX roughly 6–12 dB below speech during overlap. Use the lower end under quiet or information-dense dialogue and the upper end during pauses or energetic delivery.

Keep overlapping audio clips on separate `data-track-index` values. Mount every `<audio>` as a direct child of the composition root. Preserve narration at `data-volume="1"` unless an intentional mix decision says otherwise.

## Density and hierarchy

- Give major scene transitions the strongest whoosh.
- Use pops only on selected landings; do not pop every caption group.
- Reduce successive pops in a rapid stagger, for example `0.45`, `0.40`, `0.35`.
- Keep sustained sweeps lower than short transients.
- Do not stack a pop, click, and whoosh on the same minor event.
- If the effect cannot be heard, raise it deliberately; do not add more effects to compensate.

## Render verification

Render to a new filename and listen on ordinary headphones or laptop/phone speakers. Check at least the hook, each major transition, the densest dialogue passage, and the payoff.

Measure final loudness and true peak without applying normalization:

```bash
ffmpeg -hide_banner -nostats -i renders/final-sfx.mp4 -map 0:a:0 \
  -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json \
  -f null - 2>&1 | tail -18
```

Treat this as analysis only. Prefer final true peak at or below −3 dBTP; never accept clipping.

When a visually identical no-SFX render exists, approximate the added effects layer by subtracting its audio from the SFX render:

```bash
ffmpeg -hide_banner -nostats \
  -i renders/final-sfx.mp4 -i renders/final-no-sfx.mp4 \
  -filter_complex "[0:a]aresample=48000,aformat=channel_layouts=stereo[a0];[1:a]aresample=48000,aformat=channel_layouts=stereo[a1];[a0][a1]amerge=inputs=2[m];[m]pan=stereo|c0=c0-c2|c1=c1-c3,volumedetect[out]" \
  -map "[out]" -f null - 2>&1 | rg 'mean_volume|max_volume'
```

AAC differences make this approximate, but it catches a nearly silent SFX pass. A useful transient-effects layer commonly peaks around −14 to −8 dBFS while the complete program retains headroom. Integrated program loudness may barely change even when short SFX are audible, so do not use that metric alone.

If the user says the SFX cannot be heard, believe the listening result: inspect source loudness, raise the multipliers, re-render, and verify again rather than defending the initial mix.
