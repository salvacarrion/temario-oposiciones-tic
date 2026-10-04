# Cómo colaborar

Las correcciones son bienvenidas: erratas, normativa que ha cambiado, datos
desactualizados o explicaciones mejorables. Abre una
[*issue*](https://github.com/salvacarrion/temario-oposiciones-tic/issues) o
envía un *pull request*; cada página del libro web tiene enlaces para editarla
o reportar un error. En temas legales, cita la fuente (texto consolidado del
BOE o del DOGV) para que la corrección se pueda verificar.

Esta guía recoge cómo está organizado el repositorio y las convenciones que
siguen todos los temas, para que el libro mantenga un estilo homogéneo.

## Estructura del repositorio

- `src/`: el contenido. Un fichero por tema (`NN-slug.md`), numerados según el
  índice (108 temas en 14 bloques), con las imágenes en `src/media/`.
- `mkdocs.yml`: configuración de la web y su índice (`nav`).
- `_quarto.yml`: configuración del PDF y su índice (`book.chapters`).
  **Los dos índices van sincronizados**: cualquier alta, baja o cambio de
  título de un tema se replica en ambos.
- `index.qmd` y `prologo.md` (raíz): envoltorios del PDF para la portada
  (`src/index.md`) y el prólogo (`src/prologo.md`).
- `assets/custom.scss`: estilos propios; es el único sitio donde se toca el
  aspecto visual.
- `assets/diagrams/`: fuentes SVG de los diagramas propios y el script que los
  convierte a PNG.
- `temarios_opos/`: programas de las convocatorias de referencia, para
  contrastar el alcance de cada tema.
- `tools/`: scripts auxiliares.
  - `linkify_temas.py` convierte las menciones «tema N» en enlaces (`--check`
    lista las referencias ambiguas sin tocar nada).
  - `docx2book.py` hizo la conversión inicial desde Word y **no debe volver a
    ejecutarse**: regeneraría `src/` y borraría todas las revisiones.
  - `quarto_to_mkdocs.py` regenera `mkdocs.yml` entero a partir de
    `_quarto.yml`; desde la migración `mkdocs.yml` se edita a mano, así que no
    lo ejecutes sin revisar el diff.
- `book-quarto/` y `book-mkdocs/`: salidas generadas; no se editan ni se
  versionan.

## Compilar

```bash
# Web con recarga automática en http://127.0.0.1:8000
pip install mkdocs-material
mkdocs serve

# PDF (requiere Quarto con TinyTeX)
quarto render --to pdf
```

Antes de abrir un *pull request*, `mkdocs build` debe terminar sin errores y
los enlaces e imágenes del tema tocado deben resolver. Si el cambio afecta a la
estructura, los índices o la configuración, genera también el PDF. Cada push a
`main` regenera el PDF y la web y los publica en GitHub Pages.

## Convenciones de contenido

### Encabezados

- Cada tema empieza con un único H1, igual que su título en el `nav` de
  `mkdocs.yml` sin el prefijo «Tema N:». Sin artículo inicial: «Constitución
  Española de 1978», no «La Constitución…».
- `##` (H2) para los subtemas (en el PDF se numeran N.M) y `###` (H3) para
  estructuras mayores, como los capítulos de una ley.
- Los artículos y conceptos menores no llevan encabezado propio: van como
  elementos de lista con negrita inicial (`- **Art. 1. Objeto**: …` o
  `- **Concepto**: …`).
- Tema de una sola ley: la ley entre paréntesis en el H1, «Características y
  estructura» como primer H2 y los títulos oficiales literales como H2
  («Título I. De los derechos y deberes fundamentales»).
- Tema con varias normas: un H2 por norma («Ley 19/2013, de transparencia…»)
  con sus títulos como H3. Las normas se citan siempre como «Tipo N/AAAA,
  denominación corta».
- Nada de negritas ni imágenes dentro de los encabezados.

### Normativa y fuentes

- Bajo cada ley (bajo el H1, o bajo el H2 de cada norma en los temas con
  varias) va una línea en negrita con la versión usada:
  **«Texto consolidado a D de mes de AAAA.»** o, si la norma no ha cambiado,
  **«Sin modificaciones desde su publicación (D de mes de AAAA).»** (o «desde
  su entrada en vigor», según el caso).
- Cada tema termina con una sección `## Fuentes {.unnumbered .unlisted}`:
  normas con «texto consolidado, última modificación D de mes de AAAA» y
  guías o estándares con su edición y año («CCN-STIC 817, ed. abril 2020»).
- Las fechas salen del texto consolidado oficial (BOE o DOGV), nunca de
  memoria. Al actualizar una norma, cambia a la vez el contenido afectado, la
  línea «Texto consolidado a…» y su entrada en Fuentes.
- No se añade contenido legal sin fuente.

### Alcance y extensión

- Un tema de las bases de convocatoria (`temarios_opos/`) es un tema del
  libro: ni se agrupan normas que las bases tratan por separado ni se parte lo
  que piden juntos.
- Extensión orientativa: 2000-3000 palabras, hasta unas 4000 si el alcance lo
  pide. Manda la cobertura del programa, no la cifra: no se recorta contenido
  dentro del alcance ni se rellena fuera de él. Es un temario de repaso, no un
  manual exhaustivo.

### Estilo

- Esquemático pero comprensible: cada sección abre con 1-3 frases que explican
  la idea, y los datos enumerables (tipos, fases, plazos, órganos) van después
  en listas o tablas. Líneas cortas, sin párrafos largos.
- Temas legales: literalidad. Definiciones, plazos y enumeraciones pegados al
  texto consolidado (recortar, no parafrasear). El objeto, el ámbito y las
  definiciones van casi literales, con las frases exactas entre comillas
  angulares «…».
- Temas técnicos: manda la claridad, no la literalidad de la fuente. En los de
  programación y web, fragmentos de código breves (5-15 líneas) para lo
  preguntable.
- Negrita **solo** para datos preguntables en examen: fechas y plazos, números
  de artículo o título, cifras y porcentajes, órganos competentes y
  denominaciones oficiales (leyes, planes, plataformas).
- Español, con los términos técnicos en inglés cuando sea el uso habitual, en
  cursiva (*framework*, *stakeholder*).
- Sin raya (—): mejor comas, dos puntos o paréntesis. Sin emojis: el PDF no
  los muestra.

### Imágenes, diagramas y tablas

- Imágenes en `src/media/`, enlazadas en markdown:
  `![descripción](media/fichero.png){width=…}`. Nada de `<img>` (el PDF lo
  ignora) y solo PNG, JPEG o SVG (no GIF). El texto alternativo va vacío o
  describe la imagen, nunca es un nombre de fichero: en el PDF se convierte en
  el pie de figura.
- Diagramas propios: un SVG por diagrama en `assets/diagrams/`;
  `./render.sh fichero.svg` (sin argumentos, todos) deja el PNG a doble
  resolución en `src/media/`. Usa Google Chrome en modo *headless* (macOS).
  Imita el estilo de los existentes: título arriba a la izquierda en `#1f3a5f`,
  cajas `#dbe7f3`/`#5b87b0`, acentos `#faeed7`/`#c9a24b`, rojo
  `#fbeae7`/`#b23b2e` para errores y «Elaboración propia.» abajo a la derecha;
  940 px de ancho y texto de al menos 10 px.
- Tablas en formato pipe de markdown. Las tablas HTML heredadas de Word (aún
  quedan en el tema 57) no salen en el PDF: al tocarlas, conviértelas a pipe,
  simplificando las celdas combinadas si hace falta.

## Versiones

- Formato `vX.Y`. Y sube con cada tanda de actualizaciones publicada; X, con
  cambios de estructura (índice nuevo, otra convocatoria). Las correcciones
  menores entre versiones no cambian el número: las distingue la fecha de
  compilación, que pone cada build.
- El número está en dos sitios que deben coincidir: `date-format` en
  `_quarto.yml` (portada del PDF) y `extra.temario_version` en `mkdocs.yml`
  (pie de la web).
- Para publicar una versión, sube el número en ambos sitios, haz commit y crea
  la etiqueta:

  ```bash
  git tag -a vX.Y -m "Versión X.Y"
  git push origin vX.Y
  ```

  Después crea la *Release* en GitHub con el PDF adjunto y un resumen de los
  cambios.
