# Temario de Oposiciones TIC

Temario en formato libro Quarto para oposiciones de informática de las
administraciones públicas. Nació para el Cuerpo Superior Técnico de
Ingeniería en Informática de la Administración de la Generalitat
Valenciana (A1-06) y se ha ido ampliando a otros procesos (sanidad,
universidades, administración local). Licencia CC BY-NC 4.0.
Se publica en GitHub Pages mediante `.github/workflows/deploy.yml`.

## Estructura

- `src/` — **fuente de verdad del contenido**. Un capítulo por fichero
  (`NN-slug.md`), imágenes en `src/media/`.
- `_quarto.yml` — configuración del libro y **el índice**: orden de
  capítulos y agrupación en bloques (`book.chapters`).
- `index.qmd` — portada del libro; incluye `src/prologo.md`.
- `assets/custom.scss` — estilos propios (imágenes centradas, tablas con
  bordes/cebra). Único sitio donde tocar estilo visual.
- `tools/docx2book.py` — script de la conversión inicial docx → markdown.
  Solo para referencia; el docx original no está en este repo y NO debe
  regenerarse el contenido desde él (pisaría las mejoras hechas en `src/`).
- `references/` — documentos oficiales (leyes BOE/DOGV, guías, estándares)
  contra los que contrastar y corregir el contenido.
- `book-quarto/` — salida generada por `quarto render`. No editar, no
  versionar.

## Comandos

- `quarto render` — compila HTML + PDF (verificación mínima tras editar).
- `quarto render --to html` — solo HTML (mucho más rápido; usar durante
  ediciones iterativas). OJO: elimina el PDF de `book-quarto/`; el último
  render antes de publicar debe ser `quarto render` completo.
- `quarto preview` — vista previa local con recarga automática.

## Convenciones de contenido

- Cada fichero de capítulo empieza con un único H1 igual al título que
  aparece en `_quarto.yml`; las secciones internas usan H2/H3. Los H2 son
  los subtemas y se numeran N.M (`number-depth: 2`).
- Los capítulos van numerados globalmente según el índice objetivo de
  `PLAN.md` (85 caps. en 14 bloques; hoy existen 70). Los números sin
  contenido aún (17, 22, 33, 39, 46, 67, 69, 78-85) quedan como huecos de
  fichero y NO se listan en `_quarto.yml` hasta tener contenido (no
  publicar esqueletos).
- Encabezados (convención completa en `PLAN.md` §1): capítulo de una sola
  ley → la ley entre paréntesis en el H1, «Características y estructura»
  como primer H2 y los Títulos oficiales literales como H2 («Título I. De
  los derechos y deberes fundamentales»); capítulo multi-norma → un H2 por
  norma («Ley 19/2013, de transparencia…») con sus títulos como H3. Normas
  siempre como «Tipo N/AAAA, denominación corta». Nada de negritas ni
  imágenes dentro de encabezados.
- Idioma: español. Términos técnicos en inglés cuando sea el uso habitual
  (p. ej. *stakeholder*, *framework*).
- Estilo: fácil de estudiar, equilibrio entre esquema y prosa. Ni
  telegráfico (un esquema pelado no se entiende) ni denso (los párrafos
  largos no se retienen). Patrón: cada sección abre con 1-3 frases de
  prosa que explican la idea; los datos enumerables (tipos, fases, plazos,
  órganos) van después en listas o tablas. Nivel homogéneo entre capítulos.
- En temas legales premia la literalidad: definiciones, plazos y
  enumeraciones pegados al texto consolidado (recortar, no parafrasear),
  ciñéndose a los títulos/artículos que pide el temario. En temas técnicos
  manda la claridad, no la literalidad de la fuente.
- Negrita **solo** para datos preguntables en examen: fechas y plazos,
  números de artículo/título, cifras y porcentajes, órganos competentes,
  denominaciones oficiales (leyes, planes, plataformas). No usarla en
  prosa normal.
- Cada capítulo termina con una sección `## Fuentes {.unnumbered .unlisted}`
  que lista las fuentes usadas: normas con «texto consolidado, última
  modificación D de mes de AAAA» (fecha real tomada del PDF del BOE/DOGV
  en `references/`, nunca de memoria) y guías/estándares con edición y
  año (p. ej. «CCN-STIC 817, ed. abril 2020»).
- Imágenes: en `src/media/`, referenciadas como markdown
  `![alt](media/…){width=…}`. NO usar `<img>` HTML: el PDF lo ignora.
  Solo PNG/JPEG/SVG (nada de GIF: LaTeX no lo soporta). El alt debe estar
  vacío o ser una descripción real — nunca un nombre de fichero, porque
  se convierte en pie de figura en el PDF.
- Tablas: preferir tablas pipe de markdown. Quedan ~10 capítulos con
  tablas complejas en HTML heredadas de Word (celdas combinadas):
  **no aparecen en el PDF**, solo en HTML. Al tocarlas, convertirlas a
  tablas markdown (simplificando las celdas combinadas si hace falta).
- Evitar emojis en el contenido: el PDF (xelatex) no los renderiza.

## Al corregir o actualizar contenido

- La normativa citada tiene fecha: verificar contra `references/` o el BOE
  consolidado antes de "corregir" un dato legal. Si una ley ha sido
  modificada tras la redacción original, actualizar e indicar la versión
  consolidada usada.
- No inventar contenido nuevo en temas legales sin fuente; en temas
  técnicos, mantener el nivel de síntesis del resto del capítulo (esto es
  un temario de repaso, no un manual exhaustivo).
- Tras cualquier edición: `quarto render --to html` debe terminar sin
  errores y los enlaces/imágenes del capítulo tocado deben resolver.
  Antes de publicar cambios grandes, comprobar también el PDF completo
  (`quarto render`).

## Deuda conocida (mejoras pendientes)

- **`PLAN.md` es la hoja de ruta vigente**: convenciones, índice objetivo
  (85 caps. en 14 bloques, con subtemas), diagnóstico por capítulo y fases
  de ejecución. La fase 1 (reestructura mecánica) se ejecutó el 4 de julio
  de 2026; quedan las fases de contenido 2-7.
- Convertir las tablas HTML heredadas a markdown para que salgan en el PDF
  (en la numeración nueva: caps. 2, 19, 20, 24, 29, 30, 49, 53, 64, 71).
