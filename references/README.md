# Referencias

Documentos oficiales contra los que contrastar y corregir el temario (no se
publican en el libro; sirven de fuente de verdad al revisar contenido con
Claude Code). Los PDF no se versionan en git (ver `.gitignore`); los `.md`
con enlaces sí.

## Organización

Carpetas temáticas alineadas con los bloques del libro. Las normas estatales
y de la UE van en la carpeta del tema donde se estudian; las normas propias
de una administración van en la carpeta de esa administración.

- `01-marco-juridico/` — Derecho general (Bloque I): Constitución, TUE/TFUE,
  leyes 39/2015 y 40/2015, LCSP, TREBEP, transparencia, igualdad, violencia
  de género, PRL.
- `02-generalitat-valenciana/` — Normativa y planes de la GVA: Estatut, Ley
  del Consell, Hacienda, Función Pública Valenciana y sus decretos,
  seguridad de la información (Decreto 49/2025), simplificación
  administrativa (Decreto 54/2025), GEN Digital 2025, PAI.
- `03-proteccion-datos/` — RGPD y LOPDGDD.
- `04-seguridad/` — ENS (RD 311/2022), guías CCN-STIC, gestión de
  ciberincidentes, NIS2, estrategia nacional, OWASP.
- `05-administracion-electronica/` — RD 203/2021, ENI y sus NTI, firma
  electrónica (eIDAS, eIDAS2, Ley 6/2020), accesibilidad (RD 1112/2018).
- `06-datos-ia/` — Datos abiertos (RDL 24/2021), Data Governance Act, Data
  Act, AI Act, Década Digital 2030.
- `07-gestion-proyectos/` — Guías metodológicas: Scrum, PM², gvLOGOS, ISTQB.
- `08-redes/` — Informes técnicos de redes y 5G.
- `09-sanidad/` — Normativa sanitaria (bloque Conselleria de Sanitat).
- `10-administracion-local/` — Régimen local (bloque Ayuntamiento).
- `11-universidades/` — LOSU y ENS para universidades (bloque UPV).

## Convención de nombres

`<tipo>-<num>-<año>-<slug>__<fuente>.pdf`, en minúsculas y kebab-case.
El sufijo `__<fuente>` identifica el origen y la versión: `BOE-A-XXXX-NNNNN-
consolidado`, `DOGV-...`, `eur-lex`, o la edición (`ed-2020-04`). Sufijo
`-va` = versión en valenciano.

Ejemplos: `ley-39-2015-procedimiento-administrativo__BOE-A-2015-10565-consolidado.pdf`,
`decreto-49-2025-politica-seguridad-informacion-gva__DOGV-2025-8786.pdf`.

Preferir siempre la **versión consolidada** (BOE/DOGV/EUR-Lex). Si un
documento pesa demasiado, añadir en su lugar un `.md` con el enlace oficial.

## Pendientes conocidos

- MAGERIT v3 (libros I y II), OWASP Top 10 2021, CCN-STIC 803/804.
- Ley 37/2007 consolidada (reutilización; el RDL 24/2021 solo es la reforma).
- Ley 55/2003 Estatuto Marco (sanidad, para A2) — verificar reforma en curso.
- La CCN-STIC 817 guardada es la ed. abril 2020 (anterior al RD 311/2022);
  comprobar en ccn-cert.cni.es si hay edición posterior.
- Los Decretos 42/2019 y 49/2021 están en valenciano; sustituir por la
  versión castellana si se prefiere.
