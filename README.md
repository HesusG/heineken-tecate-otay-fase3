# st-video — Video narrado Heineken / Ruta Tecate–Otay (Paso 6)

Genera un video MP4 (≤5 min) con voz clonada en **español de México** y diapositivas
estilo **Heineken**, para la Fase 3 de Inteligencia de Negocios (Equipo 4).

**Entregable:** `output/equipo4_heineken_tecate_otay.mp4` — H.264 + AAC, 1920×1080, ~4:21.
Reproduce en cualquier dispositivo (VLC, navegador, PowerPoint, móvil).

## Estructura
```
slides/slides.md        Deck Slidev (tema Heineken, figuras del PDF)
slides/style.css        Paleta corporativa Heineken
slides/public/*.png     Figuras extraídas del PDF (dashboard, FODA, Ishikawa, pronósticos)
script/narration.json   Guion por segmento (1 por diapositiva), es-MX
script/guion.md         Guion legible (para el equipo)
src/generate_tts.py     Speechify: clona voz es-MX y genera audio por segmento
src/assemble_video.py   ffmpeg: PNG + audio -> segmentos -> video con transiciones
build/                  Artefactos (png/, audio/, seg/, voice_id.txt)
build_all.sh            Reconstrucción de extremo a extremo
```

## Reconstruir
```bash
./build_all.sh
```
Pasos sueltos:
```bash
python3 src/generate_tts.py --reclone      # (1 vez) crea la voz clonada es-MX
python3 src/generate_tts.py --test         # prueba de acento -> build/audio/_accent_test.mp3
python3 src/generate_tts.py                # genera los 11 segmentos
(cd slides && node node_modules/@slidev/cli/bin/slidev.mjs export slides.md --format png --output ../build/png)
python3 src/assemble_video.py              # ensambla el MP4 final
```

## Nota sobre el acento (España → México)
El acento se controla por la **API**, no por la web UI de Speechify:
- voz creada con `locale="es-MX"`, y
- síntesis con `model="simba-multilingual"`, `language="es-MX"`.

## Editar contenido
- Texto hablado: `script/narration.json` (debe haber **1 segmento por diapositiva**).
- Diapositivas: `slides/slides.md`. Tras editar, vuelve a correr `./build_all.sh`.
- El ensamblador valida que #segmentos == #diapositivas y aborta si no coinciden.
