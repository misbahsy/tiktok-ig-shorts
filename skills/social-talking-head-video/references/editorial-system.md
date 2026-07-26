# Editorial system

## Contents

- Frame hierarchy
- A-roll and B-roll rhythm
- Caption direction
- Reference analysis
- Platform-safe composition
- Anti-patterns

## Frame hierarchy

Build every beat with a clear order:

1. Primary claim or evidence.
2. Presenter or supporting visual.
3. Caption or annotation.
4. Structural detail such as a rule, counter, or small metadata label only when it adds meaning.

Keep two focal points in presenter-led frames: face and evidence/caption. Full-screen B-roll may use one strong focal area plus a caption.

## A-roll and B-roll rhythm

Use the presenter to establish trust and reset attention. Use B-roll to prove the words.

A useful 25–35 second arc:

- 0–3s: hook; full-frame motion with presenter PiP.
- 3–7s: first evidence beat; often full-screen.
- 7–11s: presenter return or focused information card.
- 11–15s: second B-roll proof.
- 15–19s: motion-graphic explanation.
- 19–23s: product or brand-specific screen recording.
- 23–end: payoff; briefly return to presenter, then let the result own the close.

This is a rhythm model, not a mandatory template. Match transitions to sentence boundaries and product mentions.

Prefer hard cuts for rapid proof, short opacity/blur transitions for continuous explanation, and one larger transition only for a genuine reveal.

## Caption direction

Captions are on by default. Disable them only when the user explicitly asks. A sparse set of headline callouts does not satisfy the caption requirement.

Group speech by meaning, not fixed duration. Aim for:

- 1–3 words for impact beats;
- up to 5 words for a compact question or clause;
- 0.7–2.2 seconds on screen;
- one emphasized token per group in most cases.

Suggested semantic mapping:

| Meaning | Treatment |
| --- | --- |
| Hook, payoff, strong action | Impact |
| Two-level phrase or process | Stacked |
| Product/API/technical noun | Neon, sparingly |
| Question, number, imperative | Marker |
| Connective explanation | Minimal |

Emphasis must come from the transcript. Never hash words into random styles in a final edit.

Drive word activation from corrected word timestamps, keep one group visible at a time, and hard-hide each group at its end. In presenter-led portrait layouts, place the caption rail over the lower chest or below the PiP rather than over the mouth, chin, or eyes. Reposition the rail when the layout changes instead of forcing one global coordinate onto every scene.

Inspect at least the longest phrase, the largest treatment, and one sample from every presenter geometry. Face clearance is a visual requirement even when automated layout checks pass.

## Reference analysis

When the user supplies a reference video:

1. Probe duration, dimensions, fps, codec, and audio.
2. Transcribe it.
3. Create a contact sheet every 1–3 seconds.
4. Detect scene changes and estimate average shot length.
5. Record its editing grammar: A-roll/B-roll ratio, caption position, color, type hierarchy, transition vocabulary, crop treatment, and CTA.
6. Extract principles, not proprietary artwork or unsupported brand claims.

Write the findings to `REFERENCE_ANALYSIS.md` so the rationale survives the session.

## Platform-safe composition

For a shared Reels/TikTok 1080×1920 master:

- treat `y=0–320` as a top UI exclusion zone; keep essential hook text and card copy below `y=320`;
- prefer `y=340–620` for a top-positioned headline, allowing breathing room below the search surface;
- footage, texture, and nonessential decoration may extend behind the top UI exclusion zone;
- keep essential text at least 64 px from left/right edges;
- avoid the bottom 180 px for essential text;
- keep right-side controls in mind; captions centered or left-of-center are safer;
- place the presenter above the description region when possible;
- inspect on a phone-sized preview with [../assets/social-safe-zone-overlay.svg](../assets/social-safe-zone-overlay.svg), not only a clean desktop canvas;
- when the destination is known, upload a private draft or inspect a platform screenshot because search bars and control placement change over time.

Do not vertically center the entire design merely to satisfy the safe zone. Keep motion and imagery full-frame, then move only essential text or text-bearing cards into the safe content area.

## Anti-patterns

Reject visual devices that signal generic generated output unless the reference explicitly calls for them:

- decorative status pills;
- presenter labels;
- borders around every object;
- uniform card grids;
- gradients on all headlines;
- glass cards over every shot;
- random zooms, rotation, or caption colors;
- stock imagery when real screen recordings exist;
- B-roll that is unrelated to the spoken sentence.
