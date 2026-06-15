"""Shared helpers for the st-video pipeline (no third-party deps)."""
import os
import subprocess
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DLAI_ENV = Path("/mnt/data/repos/dlai-ce/.env")


def load_env(path: Path = DLAI_ENV) -> None:
    """Minimal .env loader (KEY=VALUE per line). Avoids python-dotenv dependency."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def normalize_to_wav(source: Path, max_duration: int = 25) -> Path:
    """Trim to <=max_duration and loudness-normalize for voice cloning (mono 24k)."""
    tmp = Path(tempfile.mkstemp(suffix=".wav")[1])
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(source), "-t", str(max_duration),
         "-ac", "1", "-ar", "24000",
         "-af", "loudnorm=I=-16:LRA=11:TP=-1.5", str(tmp)],
        capture_output=True, check=True,
    )
    return tmp
