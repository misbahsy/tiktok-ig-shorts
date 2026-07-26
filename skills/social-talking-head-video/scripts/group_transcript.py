#!/usr/bin/env python3
"""Normalize common transcript shapes and draft short caption groups."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "was",
    "we", "with", "you", "your",
}
STYLES = ["minimal", "impact", "stacked", "marker", "neon"]


def seconds_from_offsets(item: dict) -> tuple[float, float]:
    if "start" in item and "end" in item:
        return float(item["start"]), float(item["end"])
    offsets = item.get("offsets", {})
    return float(offsets.get("from", 0)) / 1000, float(offsets.get("to", 0)) / 1000


def normalize(payload) -> list[dict]:
    if isinstance(payload, list):
        source = payload
    elif isinstance(payload, dict) and isinstance(payload.get("words"), list):
        source = payload["words"]
    elif isinstance(payload, dict) and isinstance(payload.get("transcription"), list):
        source = []
        for segment in payload["transcription"]:
            tokens = segment.get("tokens") or []
            source.extend(tokens if tokens else [segment])
    else:
        raise ValueError("Unsupported transcript shape")

    words = []
    for item in source:
        text = str(item.get("text", "")).strip()
        if not text or text.startswith("["):
            continue
        start, end = seconds_from_offsets(item)
        if end <= start:
            continue
        words.append({"text": text, "start": start, "end": end})
    return words


def candidate(words: list[dict]) -> str:
    content = []
    for word in words:
        clean = re.sub(r"[^A-Za-z0-9'-]", "", word["text"]).lower()
        if clean and clean not in STOPWORDS:
            content.append((len(clean), word["text"]))
    return max(content, default=(0, words[-1]["text"]))[1]


def group(words: list[dict], max_words: int, max_chars: int, pause: float) -> list[dict]:
    groups = []
    current = []
    for word in words:
        proposed = " ".join([w["text"] for w in current] + [word["text"]])
        gap = word["start"] - current[-1]["end"] if current else 0
        should_break = current and (
            len(current) >= max_words or len(proposed) > max_chars or gap > pause
            or re.search(r"[.!?]$", current[-1]["text"])
        )
        if should_break:
            groups.append(current)
            current = []
        current.append(word)
    if current:
        groups.append(current)

    result = []
    for index, item in enumerate(groups):
        result.append({
            "id": f"caption-{index + 1:02d}",
            "start": round(item[0]["start"], 3),
            "end": round(item[-1]["end"], 3),
            "text": " ".join(w["text"] for w in item),
            "words": item,
            "emphasisCandidate": candidate(item),
            "draftStyle": STYLES[index % len(STYLES)],
            "reviewRequired": True,
        })
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--max-words", type=int, default=3)
    parser.add_argument("--max-chars", type=int, default=18)
    parser.add_argument("--pause", type=float, default=0.45)
    args = parser.parse_args()

    payload = json.loads(args.transcript.read_text(encoding="utf-8"))
    output = json.dumps(group(normalize(payload), args.max_words, args.max_chars, args.pause), indent=2)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
