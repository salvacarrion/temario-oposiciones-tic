# Auditoría informática

La auditoría informática es el proceso sistemático, independiente y documentado de obtener y evaluar evidencias sobre los sistemas de información para determinar si cumplen los criterios establecidos (normas, políticas, buenas prácticas) y comunicar los resultados. Este tema repasa su concepto, tipos y fases, los marcos profesionales de referencia, las principales áreas de revisión y las técnicas asistidas por ordenador, y la auditoría en la Administración: la auditoría del ENS y las auditorías en materia de protección de datos.

## Concepto, tipos y fases; evidencias e informes

La auditoría se distingue de la consultoría en que **no diseña soluciones sino que emite una opinión** contrastando la realidad con un criterio, y exige **independencia** del auditor respecto de lo auditado. Se apoya en el **control interno** de la organización: el conjunto de políticas y controles que aseguran la fiabilidad de la información, el cumplimiento y la eficacia de las operaciones (los controles TIC generales, ITGC, y los controles de aplicación son su objeto habitual).

- **Tipos por quién la realiza**: **interna** (unidad de auditoría propia, tercera línea de defensa) y **externa** (firma o entidad independiente; obligatoria en certificaciones).
- **Tipos por objeto**: de **cumplimiento** (contra una norma: ENS, RGPD, ISO/IEC 27001), de **seguridad** (técnica: revisión de configuraciones, hacking ético), **operativa o de gestión** (eficacia y eficiencia de la función TIC), **financiera** (fiabilidad de los sistemas que soportan las cuentas) y **forense** (investigación de incidentes o fraudes).
- **Fases**:
  1. **Planificación**: definición de alcance y objetivos, estudio preliminar, **análisis de riesgos** para orientar el esfuerzo, y programa de auditoría (pruebas, recursos, calendario).
  2. **Trabajo de campo**: obtención de evidencias mediante entrevistas, observación, inspección documental, re-ejecución y análisis de datos; **pruebas de cumplimiento** (¿existe y funciona el control?) y **pruebas sustantivas** (¿es correcto el resultado?), con muestreo cuando no es viable revisar el universo completo.
  3. **Informe**: comunicación de **hallazgos**, cada uno con condición (lo observado), criterio (lo exigido), causa, efecto o riesgo, y **recomendación**; concluye con una opinión sobre el grado de cumplimiento.
  4. **Seguimiento**: verificación de la implantación del plan de acción acordado.
- **Evidencias**: deben ser **suficientes, fiables, relevantes y útiles**; se documentan en los **papeles de trabajo**, que sustentan la trazabilidad entre evidencia, hallazgo y conclusión.

## Marcos profesionales: ITAF, COBIT, ISO/IEC 27007 e ISO 19011

- **ITAF** (*IT Audit Framework*, ISACA; **4.ª edición, 2020**): marco de prácticas profesionales para la auditoría TI. Organiza las **normas** (de obligado cumplimiento para los titulares de la certificación **CISA**) en tres grupos: **generales** (independencia, objetividad, competencia, debido cuidado profesional), de **desempeño** (planificación, supervisión, obtención de evidencias, uso del trabajo de terceros) y de **informes**; las desarrolla mediante **directrices** alineadas con las fases del proceso de auditoría.
- **COBIT 2019** (ISACA): aunque es un marco de gobierno y gestión (ver tema 17), sus 40 objetivos con sus prácticas y actividades son el **criterio de referencia** más usado para auditar la función TIC; el dominio **MEA** incluye la evaluación del sistema de control interno y del cumplimiento.
- **ISO 19011:2018**: directrices para la **auditoría de sistemas de gestión** (de cualquier disciplina). Define **7 principios** (integridad; presentación imparcial; debido cuidado profesional; confidencialidad; independencia; enfoque basado en evidencias; enfoque basado en riesgos) y regula la gestión del **programa de auditorías**, la realización de cada auditoría y la competencia de los auditores.
- **ISO/IEC 27007:2020**: directrices específicas para auditar **sistemas de gestión de seguridad de la información (SGSI)**, complementando la ISO 19011 con orientación sobre los controles de la ISO/IEC 27001 (las auditorías de certificación se rigen además por la ISO/IEC 27006).

## Principales áreas de auditoría y técnicas CAAT

El plan de auditoría TIC cubre de forma rotatoria las áreas de mayor riesgo. Las más habituales:

| Área | Aspectos revisados |
| --- | --- |
| Seguridad lógica | Gestión de identidades y accesos, privilegios, contraseñas, segregación de funciones |
| Seguridad física y CPD | Control de acceso, climatización, energía, protección contra incendios (ver tema 43) |
| Desarrollo | Metodología del ciclo de vida, gestión de cambios y versiones, separación de entornos, pruebas y pase a producción |
| Explotación y operaciones | Planificación de trabajos, copias de seguridad y restauración, gestión de incidencias, monitorización |
| Bases de datos | Privilegios de administración, integridad, cifrado, registro de actividad (ver tema 36) |
| Redes y comunicaciones | Segmentación, cortafuegos, accesos remotos (ver tema 79) |
| Continuidad | BIA, planes de continuidad y recuperación, resultados de las pruebas (ver tema 31) |
| Cumplimiento y licencias | Legalidad del software instalado, contratos con proveedores, informes SOC 2 / ISAE 3402 de servicios externalizados |

Las **CAAT** (*Computer-Assisted Audit Techniques*) son las técnicas de auditoría asistidas por ordenador:

- **Análisis masivo de datos**: herramientas tipo ACL/IDEA o consultas SQL sobre el universo completo de transacciones (duplicados, valores atípicos, conciliaciones), en lugar de muestreos.
- **Datos y transacciones de prueba**: juegos de ensayo procesados por la aplicación auditada para verificar sus controles.
- **Módulos de auditoría embebidos** y pistas de auditoría: captura continua de operaciones marcadas dentro de la propia aplicación.
- **Herramientas técnicas**: escáneres de vulnerabilidades, analizadores de configuración, revisión de logs y SIEM (ver tema 31), que sustentan la auditoría de seguridad.
- La explotación de estas técnicas de forma permanente da lugar a la **auditoría continua**, con indicadores y alertas sobre los controles clave.

## Auditoría en la Administración: ENS y protección de datos

### Auditoría del ENS (RD 311/2022)

- **Art. 31. Auditoría de la seguridad**: los sistemas de información del ámbito del ENS son objeto de una **auditoría regular ordinaria, al menos cada dos años**, que verifique el cumplimiento de sus requerimientos. Con carácter **extraordinario** deberá realizarse siempre que se produzcan **modificaciones sustanciales** que puedan repercutir en las medidas de seguridad (y su realización **reinicia el cómputo** de los dos años). El plazo puede **extenderse tres meses** por fuerza mayor no imputable a la entidad. La auditoría se realiza **en función de la categoría del sistema** y, en su caso, del perfil de cumplimiento específico, conforme a los anexos I y III y a la Instrucción Técnica de Seguridad de Auditoría de la Seguridad de los Sistemas de Información.
- **Anexo III. Auditoría de la seguridad**: la auditoría constata que la **política de seguridad** define roles y funciones (con procedimientos de resolución de conflictos y personas designadas), que hay **análisis de riesgos con revisión y aprobación anual**, que se cumplen las medidas del **anexo II** aplicables y que existe un **SGSI documentado** aprobado por la dirección sobre la base de la **Declaración de Aplicabilidad** (art. 28). Las evidencias incluyen la documentación de procedimientos, el registro de incidentes, el examen del personal y el empleo de **productos certificados** (art. 19). Niveles:
  - **Categoría BÁSICA**: no necesita auditoría; basta una **autoevaluación** documentada realizada por el propio personal que administra el sistema (o en quien delegue), cuyos informes analiza el responsable de la seguridad.
  - **Categorías MEDIA y ALTA**: **auditoría formal** cuyo informe dictamina el grado de cumplimiento, con hallazgos de conformidad y no conformidad, criterios metodológicos, alcance y objetivo. Los informes se presentan al **responsable del sistema y al responsable de la seguridad**; este último los analiza y presenta sus conclusiones al responsable del sistema para que adopte medidas correctoras. En categoría **ALTA**, a la vista del dictamen, el responsable del sistema puede **suspender temporalmente** el tratamiento, la prestación de servicios o la operación total del sistema hasta la subsanación.
- **Conformidad**: la auditoría sustenta la **Certificación de Conformidad** con el ENS, expedida por entidades de certificación acreditadas (en categoría BÁSICA basta la **Declaración de Conformidad** tras la autoevaluación), conforme a la ITS de conformidad; los distintivos se publican y los informes pueden ser requeridos por el **CCN** (art. 31.7). La guía **CCN-STIC 802** (auditorías de cumplimiento, ed. junio 2025) desarrolla el alcance, el equipo auditor, la planificación, las evidencias y el dictamen.

### Auditorías en materia de protección de datos (RGPD)

El RGPD no impone una auditoría periódica general, pero la exige como instrumento de **responsabilidad proactiva**:

- **Art. 32.1.d**: entre las medidas de seguridad figura «un proceso de **verificación, evaluación y valoración regulares** de la eficacia de las medidas técnicas y organizativas».
- **Art. 39.1.b**: el **delegado de protección de datos** supervisa el cumplimiento, **incluidas las auditorías**.
- **Art. 28.3.h**: el **encargado del tratamiento** debe permitir y contribuir a las auditorías e inspecciones del responsable o de otro auditor mandatado.
- **Art. 58.1.b**: las autoridades de control (AEPD) pueden «llevar a cabo investigaciones **en forma de auditorías** de protección de datos».
- En la práctica, las auditorías RGPD revisan el registro de actividades de tratamiento, las bases jurídicas, las medidas de seguridad (en las AAPP, alineadas con el ENS), las evaluaciones de impacto y los contratos de encargo (ver tema 53).

## Fuentes {.unnumbered .unlisted}

- ITAF, *Information Technology Audit Framework*, 4.ª ed. (ISACA, 2020).
- COBIT 2019 (ISACA, 2018); ISO 19011:2018; ISO/IEC 27007:2020 (citadas por edición).
- Real Decreto 311/2022, Esquema Nacional de Seguridad, art. 31 y anexo III (texto consolidado, última modificación 6 de noviembre de 2024).
- CCN-STIC 802, *Auditorías de cumplimiento del ENS* (ed. junio 2025, citada por edición; descarga restringida del portal CCN).
- Resolución de 13 de octubre de 2016, ITS de conformidad con el ENS.
- Reglamento (UE) 2016/679 (RGPD), arts. 28, 32, 39 y 58 (DOUE de 4 de mayo de 2016).
