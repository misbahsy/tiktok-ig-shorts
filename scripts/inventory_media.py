#!/usr/bin/env python3
"""Inventory media files with ffprobe and emit deterministic JSON."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

MEDIA_EXTENSIONS = {
    ".mp4", ".mov", ".m4v", ".webm", ".mkv",
    ".mp3", ".wav", ".m4a", ".aac", ".flac",
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg",
}


def probe(path: Path) -> dict:
    command = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        payload = json.loads(result.stdout or "{}")
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as exc:
        return {"error": str(exc)}

    streams = payload.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), {})
    audio = next((s for s in streams if s.get("codec_type") == "audio"), {})
    fmt = payload.get("format", {})
    return {
        "duration": float(fmt["duration"]) if fmt.get("duration") else None,
        "width": video.get("width"),
        "height": video.get("height"),
        "fps": video.get("avg_frame_rate") or video.get("r_frame_rate"),
        "videoCodec": video.get("codec_name"),
        "audioCodec": audio.get("codec_name"),
        "hasAudio": bool(audio),
    }


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".mp4", ".mov", ".m4v", ".webm", ".mkv"}:
        return "video"
    if ext in {".mp3", ".wav", ".m4a", ".aac", ".flac"}:
        return "audio"
    return "image"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in MEDIA_EXTENSIONS:
            continue
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        files.append({
            "path": str(path.relative_to(root)),
            "type": classify(path),
            "bytes": path.stat().st_size,
            **probe(path),
        })

    output = json.dumps({"root": str(root), "count": len(files), "files": files}, indent=2)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()

