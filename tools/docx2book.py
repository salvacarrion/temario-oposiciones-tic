#!/usr/bin/env python3
"""Convierte el docx del temario en un libro mdBook (capítulos markdown + SUMMARY.md).

Uso:
    python3 tools/docx2book.py

Requiere pandoc. Es idempotente: regenera src/ desde cero en cada ejecución.
OJO: si ya has editado los .md a mano, NO lo vuelvas a ejecutar o perderás los cambios
(el docx es solo el punto de partida; la fuente de verdad es src/).
"""

import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCX = ROOT / "word" / "temario_ingenieria_informatica.docx"
SRC = ROOT / "src"

# Bloques temáticos: (nombre, nº de capítulos consecutivos que agrupa).
# El orden de los capítulos del docx se respeta siempre; esto solo añade
# títulos de sección en la barra lateral de mdBook. Ajústalo a tu gusto.
BLOQUES = [
    ("Bloque I — Marco jurídico y administrativo", 14),
    ("Bloque II — Sociedad digital y gestión TIC", 6),
    ("Bloque III — Ingeniería del software", 3),
    ("Bloque IV — Seguridad de la información", 4),
    ("Bloque V — Datos, IA y tecnologías emergentes", 7),
    ("Bloque VI — Sistemas e infraestructuras", 5),
    ("Bloque VII — Protección de datos y administración electrónica", 2),
    ("Bloque VIII — Desarrollo web y de aplicaciones", 7),
    ("Bloque IX — Servicios digitales e interoperabilidad", 6),
    ("Bloque X — Redes y comunicaciones", 9),
]

SKIP_CHAPTERS = {"Contenido"}  # el índice del docx: mdBook genera el suyo propio
UNNUMBERED = {"Prólogo": "prologo", "Referencias": "referencias"}


def slugify(title: str) -> str:
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def clean(text: str) -> str:
    # Quita los atributos {#id} de los encabezados (Quarto genera los suyos;
    # no hay enlaces internos que dependan de ellos)
    text = re.sub(r"^(#{1,6} .*?)\s*\{[#.][^}]*\}\s*$", r"\1", text, flags=re.MULTILINE)
    # Marcadores de salto de página de Word que pandoc deja como negrita vacía
    text = re.sub(r"\*\*\\\*\*", "", text)
    text = re.sub(r"^\*\*\\\**\*?\s*$", "", text, flags=re.MULTILINE)
    # Rutas de imagen: 'src/media/...' -> 'media/...' (los capítulos viven en src/)
    text = text.replace("src/media/", "media/")
    # Colapsa 3+ líneas en blanco
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    if not DOCX.exists():
        sys.exit(f"No se encuentra {DOCX}")

    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir(parents=True)

    print("Convirtiendo docx con pandoc…")
    result = subprocess.run(
        # gfm+attributes: las imágenes con tamaño salen como ![](img){width=…}
        # en vez de HTML crudo (imprescindible para que aparezcan en el PDF)
        ["pandoc", str(DOCX), "-t", "gfm+attributes", "--extract-media=src", "-o", "-"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"pandoc falló:\n{result.stderr}")
    full = result.stdout

    # Trocea por encabezados H1 (descarta la portada previa al primer H1)
    parts = re.split(r"^# (.+)$", full, flags=re.MULTILINE)[1:]
    # El título puede traer atributos {#id} con gfm+attributes: fuera
    titles = [re.sub(r"\s*\{[^}]*\}\s*$", "", t).strip() for t in parts[0::2]]
    chapters = list(zip(titles, parts[1::2]))
    chapters = [(t, b) for t, b in chapters if t not in SKIP_CHAPTERS]

    numbered = [(t, b) for t, b in chapters if t not in UNNUMBERED]
    assert sum(n for _, n in BLOQUES) == len(numbered), (
        f"Los bloques suman {sum(n for _, n in BLOQUES)} capítulos "
        f"pero hay {len(numbered)}: revisa BLOQUES"
    )

    summary = ["# Resumen\n"]
    num = 0
    bloque_iter = iter(BLOQUES)
    restantes = 0

    for title, body in chapters:
        if title in UNNUMBERED:
            fname = f"{UNNUMBERED[title]}.md"
            if title == "Referencias":
                summary.append("\n---\n")
            summary.append(f"- [{title}]({fname})")
            if title == "Prólogo":
                summary.append("\n---\n")
        else:
            if restantes == 0:
                bloque, restantes = next(bloque_iter)
                summary.append(f"\n# {bloque}\n")
            restantes -= 1
            num += 1
            fname = f"{num:02d}-{slugify(title)}.md"
            summary.append(f"- [{title}]({fname})")

        (SRC / fname).write_text(f"# {title}\n{clean(body)}", encoding="utf-8")

    (SRC / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    n_imgs = len(list((SRC / "media").glob("*"))) if (SRC / "media").exists() else 0
    print(f"OK: {len(chapters)} capítulos escritos en src/ ({n_imgs} imágenes en src/media/)")


if __name__ == "__main__":
    main()
