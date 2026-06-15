#!/usr/bin/env python3
"""Speechify TTS for the Heineken video — Mexican-Spanish (es-MX) cloned voice.

Usage:
  python src/generate_tts.py --list                # list available voices
  python src/generate_tts.py --test [--voice-id ID]  # 1 short accent-test phrase
  python src/generate_tts.py [--voice-id ID]       # generate all narration segments
  python src/generate_tts.py --reclone             # re-clone sample with locale=es-MX

The Spain-accent issue (from the web UI) is fixed at synthesis time with
model="simba-multilingual" + language="es-MX". We reuse an existing cloned
voice when possible; --reclone creates a fresh voice with locale=es-MX.
"""
import argparse
import base64
import json
import sys
from pathlib import Path

from sttools import REPO, load_env, normalize_to_wav

import os
from speechify import Speechify

MODEL = "simba-multilingual"
LANGUAGE = "es-MX"
SAMPLE = Path("/mnt/data/repos/st-video/build/voice_sample.m4a")
VOICE_ID_FILE = REPO / "build" / "voice_id.txt"
NARRATION = REPO / "script" / "narration.json"
AUDIO_DIR = REPO / "build" / "audio"
TEST_TEXT = (
    "Hola, somos el Equipo cuatro. Esta es una prueba de la narración "
    "en español de México para el proyecto de Heineken, ruta Planta Tecate a Otay. "
    "El cincuenta y nueve por ciento de las órdenes presentó retrasos."
)


def client() -> Speechify:
    load_env()
    return Speechify(token=os.environ["SPEECHIFY_API_KEY"])


def list_voices(c: Speechify):
    voices = c.tts.voices.list()
    rows = []
    for v in voices:
        vid = getattr(v, "id", None)
        name = getattr(v, "display_name", None) or getattr(v, "name", None)
        vtype = getattr(v, "type", None)
        locale = getattr(v, "locale", None)
        # locale may live under languages[]
        if not locale:
            langs = getattr(v, "languages", None) or []
            if langs:
                locale = getattr(langs[0], "locale", None)
        rows.append((vid, name, vtype, locale))
    return rows


def pick_voice(c: Speechify, override: str | None) -> str:
    if override:
        return override
    if VOICE_ID_FILE.exists():
        vid = VOICE_ID_FILE.read_text().strip()
        if vid:
            return vid
    # auto: prefer a personal/cloned voice (type == "personal")
    rows = list_voices(c)
    personal = [r for r in rows if (r[2] or "").lower() == "personal"]
    chosen = personal[0] if personal else (rows[0] if rows else None)
    if not chosen:
        sys.exit("No voices found. Run --reclone or pass --voice-id.")
    print(f"Auto-selected voice: {chosen}")
    return chosen[0]


def reclone(c: Speechify, sample: Path = SAMPLE) -> str:
    print(f"Cloning voice with locale=es-MX from {sample}…")
    wav = normalize_to_wav(sample)
    voice = c.tts.voices.create(
        name="Equipo4 Heineken (es-MX)",
        gender="male",
        sample=("sample.wav", wav.read_bytes(), "audio/wav"),
        consent=json.dumps({
            "fullName": os.environ.get("CONSENT_NAME", "Equipo 4"),
            "email": os.environ.get("CONSENT_EMAIL", os.environ.get("USER_EMAIL", "")),
        }),
        locale="es-MX",
    )
    VOICE_ID_FILE.write_text(voice.id)
    print(f"  New voice id: {voice.id} (saved to {VOICE_ID_FILE})")
    return voice.id


def synth(c: Speechify, text: str, voice_id: str, out: Path):
    resp = c.tts.audio.speech(
        input=text, voice_id=voice_id,
        audio_format="mp3", model=MODEL, language=LANGUAGE,
    )
    data = resp.audio_data
    audio = base64.b64decode(data) if isinstance(data, str) else data
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(audio)
    print(f"  wrote {out}  ({len(audio)//1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--reclone", action="store_true")
    ap.add_argument("--voice-id", default=None)
    ap.add_argument("--sample", default=str(SAMPLE))
    args = ap.parse_args()

    c = client()

    if args.list:
        for r in list_voices(c):
            print(r)
        return

    voice_id = reclone(c, Path(args.sample)) if args.reclone else pick_voice(c, args.voice_id)
    print(f"Using voice_id={voice_id}  model={MODEL}  language={LANGUAGE}")

    if args.test:
        synth(c, TEST_TEXT, voice_id, AUDIO_DIR / "_accent_test.mp3")
        print("\nListen to build/audio/_accent_test.mp3 — should sound Mexican.")
        return

    segments = json.loads(NARRATION.read_text())
    print(f"Generating {len(segments)} segments…")
    for seg in segments:
        idx = seg["idx"]
        synth(c, seg["text"], voice_id, AUDIO_DIR / f"seg_{idx:02d}.mp3")
    print("Done.")


if __name__ == "__main__":
    main()
