# TikTok & Instagram Talking-Head Skills

A composable collection of agent skills for turning existing talking-head, founder, interview, or tutorial footage into polished vertical social videos for Instagram Reels, TikTok, and YouTube Shorts.

The collection covers asset triage, reference analysis, transcript-driven editing, standard and layered pop-out picture-in-picture, kinetic captions, an Anthropic-inspired editorial style, full-screen B-roll, scrolling webpage captures, product screen recordings, motion graphics, calibrated motion-synced SFX, review, and render verification.

## Skills

| Skill | Use it for |
| --- | --- |
| `social-talking-head-video` | Complete short-form edit with dynamic captions enabled by default |
| `popout-talking-head-video` | Layered cutout presenter that breaks beyond the PiP edge |
| `kinetic-caption-video` | Captions that move among upper, lower, mid-frame, and behind-presenter zones |
| `anthropic-talking-head-style` | Warm ivory, charcoal, terracotta, editorial print-inspired art direction |

The skills are composable. For example, invoke the base editor with the pop-out and kinetic-caption skills to create a complete layered edit, or add the Anthropic-inspired style to either presenter treatment.

## Example

[![Watch the finished vertical social edit](examples/ai-shorts-editing-assistant-poster.jpg)](examples/ai-shorts-editing-assistant-final.mp4)

[Watch or download the MP4](examples/ai-shorts-editing-assistant-final.mp4). This example demonstrates a typed chat hook, product screen recording, animated asset cards, dynamic captions, borderless presenter PiP, a complete 9:16 edit shown inside a phone frame, platform-safe spacing, and motion-synced SFX.

The composition uses a conservative shared Instagram/TikTok safe zone: essential top copy begins below `y=320` on the 1080×1920 master, while the presenter card retains breathing room above the bottom platform controls.

## What the agent asks first

Before it begins production, the skill collects three compact groups of information:

1. **Source and outcome** — talking-head footage, destination platform, target duration, language, and desired call to action.
2. **Available assets** — logos, brand files, screenshots, screen recordings, B-roll, music, sound effects, product footage, and references.
3. **Style and constraints** — visual references, colors and type, caption energy, presenter treatment, pacing, safe zones, and elements to avoid.

The agent inventories files already supplied before requesting more material. If you delegate creative decisions, it records its assumptions in the project brief before building.

## Install

### Codex and other agents — Skills CLI (recommended)

Using [Vercel's Skills CLI](https://github.com/vercel-labs/skills), which supports Codex, Claude Code, Cursor, and other compatible agents:

```bash
npx skills add misbahsy/tiktok-ig-shorts             # choose skills and agents interactively
npx skills add misbahsy/tiktok-ig-shorts -a codex    # install the collection for Codex
```

Install one skill explicitly when preferred:

```bash
npx skills add misbahsy/tiktok-ig-shorts -s social-talking-head-video -a codex
npx skills add misbahsy/tiktok-ig-shorts -s popout-talking-head-video -a codex
npx skills add misbahsy/tiktok-ig-shorts -s kinetic-caption-video -a codex
npx skills add misbahsy/tiktok-ig-shorts -s anthropic-talking-head-style -a codex
```

In Codex, invoke a skill with `$social-talking-head-video`, `$popout-talking-head-video`, `$kinetic-caption-video`, or `$anthropic-talking-head-style` (or use `/skills` to browse). Harnesses that expose installed skills as slash commands can use the corresponding `/skill-name` command.

### Manually (drop-in skill)

Clone the repository, then copy the complete folder so its relative `assets/`, `references/`, and `scripts/` paths remain intact:

```bash
git clone https://github.com/misbahsy/tiktok-ig-shorts.git
cp -R tiktok-ig-shorts/skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"  # Codex
cp -R tiktok-ig-shorts/skills/* "$HOME/.agents/skills/"               # compatible agents
```

For another coding harness, configure its skill loader to discover the folders under `skills/` and preserve each skill's relative `assets/`, `references/`, and `scripts/` paths.

## Use

Ask your agent:

```text
Use $social-talking-head-video to turn my talking-head clip into a polished vertical social video.
```

The agent will run the intake before production. You can provide a folder instead of listing every asset manually; the included media inventory script probes common video, audio, image, and font formats.

If you provide a webpage URL—or research identifies a useful page—the base skill prefers a smooth browser-recorded scroll over a static screenshot. It uses Rollberry-style eased capture with optional hero holds, section stops, mobile/desktop viewports, and removal of irrelevant cookie or chat overlays.

## Requirements

- Python 3.10+
- FFmpeg and FFprobe
- Node.js and a Chromium-based browser
- HyperFrames, installed separately

Install or refresh the supporting HyperFrames workflow with:

```bash
npx hyperframes skills update talking-head-recut
```

## Repository contents

- `skills/social-talking-head-video/` — complete edit workflow, intake, scrolling-page B-roll, safe zones, SFX, QA, and helper scripts
- `skills/popout-talking-head-video/` — transparent-subject compositing and depth-layer contract
- `skills/kinetic-caption-video/` — roaming semantic captions and transcript grouping helper
- `skills/anthropic-talking-head-style/` — reusable warm editorial visual tokens and styling guidance
- `examples/ai-shorts-editing-assistant-final.mp4` — finished 9:16 reference edit

The skill intentionally discourages generated-looking shortcuts such as decorative status pills, presenter labels, gratuitous glassmorphism, and arbitrary caption styling.
