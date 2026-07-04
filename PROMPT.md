<!-- Pega el texto de abajo como primer mensaje en una sesión nueva de
Claude Code. Es reutilizable: cada sesión continúa desde el registro de
progreso de PLAN.md. -->

Ejecuta la reestructuración y mejora del temario definida en `PLAN.md`.
Léelo entero antes de tocar nada: contiene el diagnóstico capítulo a
capítulo, el índice objetivo (84 capítulos en 14 bloques) y las 7 fases de
ejecución. Trabaja fase a fase y, dentro de cada fase, capítulo a capítulo.

## Registro de progreso (imprescindible)

Mantén al final de `PLAN.md` una sección `## Progreso` con checkboxes por
fase y capítulo. Lo primero en cada sesión: leer ese registro y continuar
donde se quedó la anterior. Si algo del plan resulta inviable o contradice
las referencias, no te bloquees: anótalo en una subsección `Desviaciones`
con el porqué y toma la decisión razonable.

## Estilo de contenido (el que ha aprobado esta oposición)

- **Fácil de estudiar: equilibrio entre esquema y prosa.** Ni telegráfico
  (un esquema pelado no se entiende) ni denso (los párrafos largos no se
  retienen). Patrón: cada sección abre con 1-3 frases de prosa que
  explican la idea y para qué sirve; los datos enumerables (tipos, fases,
  plazos, órganos) van después en listas o tablas. Nivel homogéneo con los
  capítulos ya buenos (p. ej. `35-centros-de-procesamiento-de-datos-cpd.md`).
- **En leyes, premia la literalidad**: definiciones, plazos y enumeraciones
  pegados al texto consolidado (recortar, no parafrasear), ciñéndose a los
  títulos/artículos que pide el temario. En temas técnicos manda la
  claridad de la explicación, no la literalidad de la fuente.
- **Negrita únicamente en los datos preguntables en examen**: fechas y
  plazos, números de artículo/título/capítulo, cifras y porcentajes,
  órganos competentes, denominaciones oficiales de leyes, planes y
  plataformas. Nunca en prosa normal.
- Conserva las secciones «Caso práctico» existentes; añade una breve solo
  si el temario oficial la pide.
- Los títulos de capítulos nuevos deben calcar la literalidad de los
  temarios de `temarios_opos/` para que el opositor los reconozca.

## Fuentes y rigor legal

- Todo dato legal se contrasta con `references/` (carpetas temáticas; ver
  su README). Los PDF de leyes son **textos consolidados** BOE/DOGV: en su
  primera página figura la fecha de última modificación — úsala. Son
  ficheros grandes: léelos por páginas concretas, nunca enteros.
- **No inventes contenido legal sin fuente.** Si no hay referencia local
  ni fuente oficial verificable, deja `<!-- TODO: verificar -->` y no des
  el dato por bueno.
- Cada capítulo termina con `## Fuentes {.unnumbered .unlisted}` listando:
  - Normas: «Ley 39/2015, de 1 de octubre — texto consolidado BOE, última
    modificación D de mes de AAAA» (fecha real del PDF de `references/`,
    no de memoria).
  - Guías/estándares: edición y año (p. ej. «CCN-STIC 817, ed. abril
    2020», «Scrum Guide 2020», «ISTQB CTFL v4.0»).
  - Si usas una fuente que no está en `references/`, cita el identificador
    oficial (BOE-A-…, ELI, URL oficial) y añádela a «Pendientes conocidos»
    del `references/README.md`.
- Antes de reescribir los capítulos de los Decretos 49/2025 y 54/2025,
  verifica en el propio texto de los decretos qué normas derogan
  exactamente (disposiciones derogatorias).

## Reglas técnicas

- Sigue `CLAUDE.md` en todo (H1 único, sin HTML ni emojis, tablas pipe,
  imágenes markdown en `src/media/`).
- Capítulos nuevos sin contenido NO se añaden a `_quarto.yml`: no se
  publican esqueletos vacíos.
- Tras cada capítulo tocado: `quarto render --to html` sin errores y
  enlaces/imágenes del capítulo resolviendo.
- Commit por unidad lógica (la reestructura mecánica; luego un capítulo o
  grupo pequeño), con mensaje descriptivo en español.
- Tras la fase 1, `temarios_opos/__libro.md` queda obsoleto: regenéralo a
  partir del nuevo índice (H1 + H2 de cada capítulo) o márcalo como
  obsoleto en su cabecera.

## Al cerrar cada sesión

Deja: (1) render HTML verde, (2) `## Progreso` de PLAN.md al día,
(3) commit hecho. Antes de publicar cambios grandes, un `quarto render`
completo (HTML + PDF) debe terminar sin errores.
