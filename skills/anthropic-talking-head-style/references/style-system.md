# Warm editorial style system

## Tokens

```css
:root {
  --paper: #faf9f5;
  --paper-2: #e8e6dc;
  --ink: #141413;
  --muted: #b0aea5;
  --terracotta: #d97757;
  --terracotta-dark: #a55a43;
  --editorial-blue: #6a9bcc;
  --botanical-green: #788c5d;
  --line: rgba(20,20,19,.22);
}
```

Use Poppins 600–700 for display and UI. Use Lora 400–600 for editorial supporting lines. Ship local WOFF2 files; do not rely on workstation fonts.

## Surfaces

- Background: warm paper or charcoal.
- Cards: paper, 2 px charcoal outline, 2–8 px radius.
- Shadow: solid offset block, usually 8–14 px, using one palette accent.
- Texture: subtle 8 px dotted grain.
- Hierarchy: one dominant statement, one proof asset, one annotation layer.

## Captions

Use terracotta emphasis, black/ivory contrast, and a coherent subset of impact, marker, stacked, and minimal treatments. Serif italics or editorial underlines are accents, not defaults.

## Motion

Prefer hard cuts, mask reveals, 0.2–0.5 second slides, short scale pops, and quiet parallax. Elements should settle quickly enough to read on a phone.

## Guardrails

- Do not claim official Anthropic affiliation.
- Do not recreate proprietary logos or artwork.
- Do not place essential text inside shared platform UI zones.
- Keep real product captures legible and factually unchanged.
