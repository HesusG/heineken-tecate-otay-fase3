#!/usr/bin/env python3
"""Assemble narrated slides into the final MP4.

For each segment: still PNG (scaled to 1080p) + narration mp3 (padded with a
little lead/trailing silence). Segments are joined with cross-dissolve
transitions (video xfade + audio acrossfade over the silence padding, so spoken
words never overlap). Falls back to hard-cut concat if the xfade graph fails.

Output: output/equipo4_heineken_tecate_otay.mp4 (H.264 + AAC, yuv420p, 1080p).
"""
import json
import subprocess
import sys
from pathlib import Path

from sttools import REPO, ffprobe_duration

PNG_DIR = REPO / "build" / "png"
AUDIO_DIR = REPO / "build" / "audio"
SEG_DIR = REPO / "build" / "seg"
NARRATION = REPO / "script" / "narration.json"
OUT = REPO / "output" / "equipo4_heineken_tecate_otay.mp4"

W, H, FPS = 1920, 1080, 30
LEAD, TRAIL = 0.20, 0.60      # silence padding (s)
T = 0.40                       # transition length (s)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def build_segment(idx: int) -> tuple[Path, float]:
    png = PNG_DIR / f"{idx}.png"
    mp3 = AUDIO_DIR / f"seg_{idx:02d}.mp3"
    if not png.exists() or not mp3.exists():
        sys.exit(f"Missing input for segment {idx}: {png.exists()=} {mp3.exists()=}")
    dur = ffprobe_duration(mp3) + LEAD + TRAIL
    out = SEG_DIR / f"seg_{idx:02d}.mp4"
    fc = (
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,setsar=1,fps={FPS},format=yuv420p[v];"
        f"[1:a]adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad=pad_dur={TRAIL},"
        f"aresample=48000[a]"
    )
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(mp3),
        "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
        "-t", f"{dur:.3f}", "-c:v", "libx264", "-crf", "20", "-preset", "medium",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", str(out),
    ]
    r = run(cmd)
    if r.returncode != 0:
        sys.exit(f"segment {idx} build failed:\n{r.stderr[-1500:]}")
    return out, dur


def build_crossfade(segs: list[tuple[Path, float]]) -> bool:
    n = len(segs)
    inputs = []
    for p, _ in segs:
        inputs += ["-i", str(p)]
    parts, prev_v, prev_a = [], "[0:v]", "[0:a]"
    acc = segs[0][1]
    for i in range(1, n):
        off = acc - T
        vout, aout = f"[vx{i}]", f"[ax{i}]"
        parts.append(f"{prev_v}[{i}:v]xfade=transition=fade:duration={T}:offset={off:.3f}{vout}")
        parts.append(f"{prev_a}[{i}:a]acrossfade=d={T}:c1=tri:c2=tri{aout}")
        prev_v, prev_a = vout, aout
        acc += segs[i][1] - T
    total = acc
    parts.append(f"{prev_v}fade=t=in:st=0:d=0.5,fade=t=out:st={total-0.6:.3f}:d=0.6[vout]")
    parts.append(f"{prev_a}afade=t=in:st=0:d=0.4,afade=t=out:st={total-0.6:.3f}:d=0.6[aout]")
    fc = ";".join(parts)
    cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", fc,
           "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-crf", "20", "-preset", "medium",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", str(OUT)]
    r = run(cmd)
    if r.returncode != 0:
        print(f"[warn] crossfade failed, will fall back:\n{r.stderr[-1200:]}")
        return False
    return True


def build_concat(segs: list[tuple[Path, float]]):
    lst = SEG_DIR / "concat.txt"
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p, _ in segs))
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
           "-c", "copy", str(OUT)]
    r = run(cmd)
    if r.returncode != 0:
        sys.exit(f"concat fallback failed:\n{r.stderr[-1500:]}")


def main():
    segments = json.loads(NARRATION.read_text())
    pngs = sorted(PNG_DIR.glob("*.png"), key=lambda p: int(p.stem))
    if len(segments) != len(pngs):
        sys.exit(f"COUNT MISMATCH: {len(segments)} narration segments vs {len(pngs)} PNG frames. "
                 f"Re-author narration.json or re-export slides so they match.")
    SEG_DIR.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)

    print(f"Building {len(segments)} segments…")
    segs = [build_segment(seg["idx"]) for seg in segments]

    print("Assembling with cross-dissolve transitions…")
    if not build_crossfade(segs):
        print("Using hard-cut concat fallback…")
        build_concat(segs)

    dur = ffprobe_duration(OUT)
    print(f"\n✅ {OUT}")
    print(f"   duration: {dur:.1f}s ({dur/60:.2f} min)")


if __name__ == "__main__":
    main()
