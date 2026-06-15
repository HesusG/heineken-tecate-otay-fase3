#!/usr/bin/env bash
# Reproducible build of the Heineken Tecate–Otay narrated video.
# Prereqs (already satisfied on this machine):
#   - ffmpeg/ffprobe, node, python3 + `speechify` package
#   - slides/node_modules symlink -> dlai-ce/slides/node_modules (Slidev + Playwright)
#   - Speechify creds in /mnt/data/repos/dlai-ce/.env
#   - cloned es-MX voice id in build/voice_id.txt (create with: python3 src/generate_tts.py --reclone)
set -euo pipefail
cd "$(dirname "$0")"
SLIDEV="slides/node_modules/@slidev/cli/bin/slidev.mjs"

echo "==> 1/3  Exporting slides to PNG"
( cd slides && node "node_modules/@slidev/cli/bin/slidev.mjs" export slides.md \
    --format png --output ../build/png --timeout 120000 )

echo "==> 2/3  Generating Mexican-Spanish narration (Speechify)"
python3 src/generate_tts.py

echo "==> 3/3  Assembling final MP4"
python3 src/assemble_video.py

echo "Done -> output/equipo4_heineken_tecate_otay.mp4"
