# Auditoría informática

La auditoría informática es el proceso sistemático, independiente y documentado de obtener y evaluar evidencias sobre los sistemas de información para determinar si cumplen los criterios establecidos (normas, políticas, buenas prácticas) y comunicar los resultados. Este tema repasa su concepto, tipos y fases, los marcos profesionales de referencia, las principales áreas de revisión y las técnicas asistidas por ordenador, y la auditoría en la Administración: la auditoría del ENS y las auditorías en materia de protección de datos.

## Concepto, tipos y fases; evidencias e informes

La auditoría se distingue de la consultoría en que **no diseña soluciones sino que emite una opinión** contrastando la realidad con un criterio, y exige **independencia** del auditor respecto de lo auditado. Se apoya en el **control interno** de la organización: el conjunto de políticas y controles que aseguran la fiabilidad de la información, el cumplimiento y la eficacia de las operaciones. Su objeto habitual son los **controles TIC generales** (ITGC: gestión de accesos, gestión de cambios, operaciones y copias, adquisición y desarrollo) y los **controles de aplicación** (validaciones de entrada, proceso y salida de cada sistema concreto).

- **Tipos por quién la realiza**: **interna** (unidad de auditoría propia) y **externa** (firma o entidad independiente; obligatoria en certificaciones). En el **modelo de las tres líneas** (IIA, 2020), la primera línea gestiona el riesgo (gestión operativa), la segunda lo supervisa (funciones de riesgo y cumplimiento) y la tercera es la **auditoría interna**, que informa al órgano de gobierno.
- **Tipos según ISO 19011**: de **primera parte** (interna, para la propia organización), de **segunda parte** (a proveedores o de parte interesada, como el cliente que audita a su suministrador) y de **tercera parte** (organismo independiente: certificación, acreditación o requisito legal).
- **Tipos por objeto**: de **cumplimiento** (contra una norma: ENS, RGPD, ISO/IEC 27001), de **seguridad** (técnica: revisión de configuraciones, hacking ético), **operativa o de gestión** (eficacia y eficiencia de la función TIC), **financiera** (fiabilidad de los sistemas que soportan las cuentas) y **forense** (investigación de incidentes o fraudes).
- **Fases**:
  1. **Planificación**: definición de alcance y objetivos, estudio preliminar, **análisis de riesgos** para orientar el esfuerzo, y programa de auditoría (pruebas, recursos, calendario).
  2. **Trabajo de campo**: obtención de evidencias mediante entrevistas, observación, inspección documental, re-ejecución y análisis de datos; **pruebas de cumplimiento** (¿existe y funciona el control?) y **pruebas sustantivas** (¿es correcto el resultado?), con muestreo cuando no es viable revisar el universo completo.
  3. **Informe**: comunicación de **hallazgos**, cada uno con condición (lo observado), criterio (lo exigido), causa, efecto o riesgo, y **recomendación**; concluye con una opinión sobre el grado de cumplimiento.
  4. **Seguimiento**: verificación de la implantación del plan de acción acordado.
- **Evidencias**: deben ser **suficientes, fiables, relevantes y útiles**; se documentan en los **papeles de trabajo**, que sustentan la trazabilidad entre evidencia, hallazgo y conclusión.

## Marcos profesionales: ITAF, COBIT, ISO 19011 e ISO/IEC 27007

- **ITAF** (*IT Audit Framework*, ISACA; **4.ª edición, 2020**): marco de prácticas profesionales para la auditoría TI. Organiza las **normas** (de obligado cumplimiento para los titulares de la certificación **CISA**) en tres grupos: **generales** (independencia, objetividad, competencia, debido cuidado profesional), de **desempeño** (planificación, supervisión, obtención de evidencias, uso del trabajo de terceros) y de **informes**; las desarrolla mediante **directrices** alineadas con las fases del proceso de auditoría.
- **COBIT 2019** (ISACA): aunque es un marco de gobierno y gestión (ver tema [17](17-gobernanza-y-planificacion-estrategica-tic.md)), sus 40 objetivos con sus prácticas y actividades son el **criterio de referencia** más usado para auditar la función TIC. El dominio **MEA** (*Monitor, Evaluate and Assess*) es el propio de la evaluación: **MEA01** supervisión del rendimiento y la conformidad, **MEA02** sistema de control interno, **MEA03** cumplimiento de los requisitos externos y **MEA04** aseguramiento independiente.
- **ISO 19011:2018**: directrices para la **auditoría de sistemas de gestión** (de cualquier disciplina). Define **7 principios** (integridad; presentación imparcial; debido cuidado profesional; confidencialidad; independencia; enfoque basado en evidencias; enfoque basado en riesgos) y regula la gestión del **programa de auditorías**, la realización de cada auditoría y la competencia de los auditores. En 2026 se ha publicado su **4.ª edición (ISO 19011:2026)**; los principios citados corresponden a la edición de 2018, la de referencia en las convocatorias.
- **ISO/IEC 27007:2020**: directrices específicas para auditar **sistemas de gestión de seguridad de la información (SGSI)**, complementando la ISO 19011 con orientación sobre los controles de la ISO/IEC 27001 (las auditorías de certificación se rigen además por la ISO/IEC 27006). Está en revisión (proyecto DIS en curso). La propia **ISO/IEC 27001:2022** exige realizar **auditorías internas del SGSI** a intervalos planificados (cláusula 9.2), por lo que toda organización certificada mantiene un programa de auditoría interna además de la auditoría externa de certificación.

## Principales áreas de auditoría y técnicas CAAT

El plan de auditoría TIC cubre de forma rotatoria las áreas de mayor riesgo. Las más habituales:

| Área | Aspectos revisados |
| --- | --- |
| Seguridad lógica | Gestión de identidades y accesos, privilegios, contraseñas, segregación de funciones |
| Seguridad física y CPD | Control de acceso, climatización, energía, protección contra incendios (ver tema [43](43-centros-de-proceso-de-datos.md)) |
| Desarrollo | Metodología del ciclo de vida, gestión de cambios y versiones, separación de entornos, pruebas y pase a producción |
| Explotación y operaciones | Planificación de trabajos, copias de seguridad y restauración, gestión de incidencias, monitorización |
| Bases de datos | Privilegios de administración, integridad, cifrado, registro de actividad (ver tema [36](36-bases-de-datos.md)) |
| Redes y comunicaciones | Segmentación, cortafuegos, accesos remotos (ver tema [79](79-seguridad-en-las-comunicaciones.md)) |
| Continuidad | BIA, planes de continuidad y recuperación, resultados de las pruebas (ver tema [31](31-gestion-de-ciberincidentes.md)) |
| Cumplimiento y licencias | Legalidad del software instalado, contratos con proveedores, informes SOC 2 / ISAE 3402 de servicios externalizados |

Los servicios externalizados (nube, CPD gestionado, nómina) no siempre pueden auditarse directamente: se revisan mediante **informes de aseguramiento de tercera parte** emitidos por el auditor del proveedor, principalmente **SOC 1** (controles con impacto en la información financiera), **SOC 2** (seguridad, disponibilidad, integridad de proceso, confidencialidad y privacidad, del AICPA) e **ISAE 3402** (norma internacional de aseguramiento equivalente al SOC 1).

Las **CAAT** (*Computer-Assisted Audit Techniques*) son las técnicas de auditoría asistidas por ordenador:

- **Análisis masivo de datos**: herramientas tipo ACL/IDEA o consultas SQL sobre el universo completo de transacciones (duplicados, valores atípicos, conciliaciones), en lugar de muestreos.
- **Datos y transacciones de prueba**: juegos de ensayo procesados por la aplicación auditada para verificar sus controles.
- **Módulos de auditoría embebidos** y pistas de auditoría: captura continua de operaciones marcadas dentro de la propia aplicación.
- **Herramientas técnicas**: escáneres de vulnerabilidades (**Nessus**, **OpenVAS**), analizadores de configuración, revisión de logs y SIEM (ver tema [31](31-gestion-de-ciberincidentes.md)), que sustentan la auditoría de seguridad.
- La explotación de estas técnicas de forma permanente da lugar a la **auditoría continua**, con indicadores y alertas sobre los controles clave.

## Auditoría en la Administración: ENS y protección de datos

### Auditoría del ENS (RD 311/2022)

**Texto consolidado a 6 de noviembre de 2024.**

- **Art. 31. Auditoría de la seguridad**: los sistemas de información del ámbito del ENS son objeto de una **auditoría regular ordinaria, al menos cada dos años**, que verifique el cumplimiento de sus requerimientos. Con carácter **extraordinario** deberá realizarse siempre que se produzcan **modificaciones sustanciales** que puedan repercutir en las medidas de seguridad (y su realización **determina la nueva fecha de cómputo** de los dos años). El plazo puede **extenderse tres meses** por impedimentos de fuerza mayor no imputables a la entidad. La auditoría se realiza **en función de la categoría del sistema** y, en su caso, del perfil de cumplimiento específico, conforme a los anexos I y III y a la **ITS de Auditoría de la Seguridad de los Sistemas de Información**.
- **Informe de auditoría (art. 31.4-31.7)**: dictamina el **grado de cumplimiento** identificando los hallazgos de cumplimiento e incumplimiento, e incluye los criterios metodológicos, el alcance y el objetivo. Se presenta al **responsable del sistema y al responsable de la seguridad**; este último lo analiza y presenta sus conclusiones al responsable del sistema para que adopte medidas correctoras. En categoría **ALTA**, a la vista del dictamen, el **responsable del sistema puede suspender temporalmente** el tratamiento, la prestación de servicios o la operación total del sistema hasta la subsanación (**art. 31.6**). Los informes pueden ser requeridos por los **responsables de cada organización con competencias sobre seguridad TI y por el CCN** (art. 31.7).
- **Anexo III. Auditoría de la seguridad**: la auditoría constata que la **política de seguridad** define roles y funciones (con procedimientos de resolución de conflictos y personas designadas conforme al principio de **diferenciación de responsabilidades**), que hay **análisis de riesgos con revisión y aprobación anual**, que se cumplen las medidas del **anexo II** aplicables y que existe un **SGSI documentado** con aprobación regular por la dirección sobre la base de la **Declaración de Aplicabilidad** (art. 28). Las evidencias incluyen la documentación de procedimientos, el registro de incidentes, el examen del personal y el empleo de **productos certificados** (art. 19); debe existir un **programa o plan de auditorías documentado**, y las comprobaciones sobre sistemas en operación se planifican y acuerdan previamente. Niveles:
  - **Categoría BÁSICA**: no necesita auditoría; basta una **autoevaluación** documentada realizada por el propio personal que administra el sistema (o en quien delegue), cuyos informes analiza el responsable de la seguridad.
  - **Categorías MEDIA y ALTA**: **auditoría formal** cuyo informe dictamina el grado de cumplimiento con hallazgos de conformidad y no conformidad.
- **ITS de Auditoría de la Seguridad (Resolución de 27 de marzo de 2018)**: desarrolla cómo realizar la auditoría del ENS:
  - **Hallazgos**: **no conformidad menor** (ausencia o fallo en la implantación o el mantenimiento de uno o más requisitos del ENS que genere una duda significativa sobre la conformidad), **no conformidad mayor** (varias no conformidades menores en el marco organizativo, el marco operacional o las medidas de protección que puedan implicar el incumplimiento del objetivo del grupo o subgrupo de medidas) y **observación** (evidencia de una debilidad o vulnerabilidad que, sin comprometer el sistema, pueda derivar en un problema).
  - **Dictamen**: **favorable** (sin no conformidades), **favorable con no conformidades** (exige un **plan de acciones correctivas en el plazo máximo de un mes**) o **desfavorable** (el número o la trascendencia de las no conformidades impide resolverlas mediante plan y obliga a una **auditoría extraordinaria en 6 meses**).
  - **Equipo auditor**: debe garantizar su **independencia objetiva**; sus tareas no incluirán en ningún caso actividades de **consultoría** (implantación o modificación de aplicaciones, recomendación de productos concretos).
  - **Informe**: incluye las áreas cubiertas y ubicaciones, la **categoría del sistema y los niveles** alcanzados en las dimensiones de seguridad, los hallazgos justificados con **evidencias objetivas** y la conclusión sobre la certificación.
  - Remite a las guías **CCN-STIC 802, 804, 808 y 824**.
- **Conformidad (ITS de conformidad, Resolución de 13 de octubre de 2016)**: la auditoría sustenta la publicidad de la conformidad con el ENS:
  - **Declaración de Conformidad**: para sistemas de categoría **BÁSICA**; la emite la **propia entidad** tras la autoevaluación.
  - **Certificación de Conformidad**: para sistemas de categorías **MEDIA o ALTA**; la expide una **entidad de certificación acreditada por ENAC** conforme a la norma **UNE-EN ISO/IEC 17065:2012**.
  - Los **distintivos** tienen una **vigencia de dos años** (renovación mediante nueva autoevaluación o auditoría) y se exhiben en la **sede electrónica** de la entidad, con enlace al documento completo. Los **operadores del sector privado** que prestan servicios o proveen soluciones a las entidades públicas exhiben sus declaraciones o certificaciones por los mismos procedimientos.
  - La guía **CCN-STIC 802** (auditorías de cumplimiento, ed. junio 2025) desarrolla el alcance, el equipo auditor, la planificación, las evidencias y el dictamen.

### Auditorías en materia de protección de datos (RGPD)

**Reglamento (UE) 2016/679: DOUE de 4 de mayo de 2016 (sin actos modificativos posteriores).**

El RGPD no impone una auditoría periódica general, pero la exige como instrumento de **responsabilidad proactiva**:

- **Art. 32.1.d**: entre las medidas de seguridad figura «un proceso de **verificación, evaluación y valoración regulares** de la eficacia de las medidas técnicas y organizativas».
- **Art. 39.1.b**: el **delegado de protección de datos** supervisa el cumplimiento del Reglamento y de las políticas del responsable o del encargado, «**y las auditorías correspondientes**».
- **Art. 28.3.h**: el **encargado del tratamiento** debe permitir y contribuir a la realización de auditorías, **incluidas inspecciones**, por parte del responsable **o de otro auditor autorizado** por dicho responsable.
- **Art. 58.1.b**: las autoridades de control (AEPD) pueden «llevar a cabo investigaciones **en forma de auditorías** de protección de datos».
- **Arts. 42 y 43**: promueven los **mecanismos de certificación, sellos y marcas** de protección de datos para demostrar el cumplimiento; los **organismos de certificación** deben estar acreditados por la autoridad de control o por el **organismo nacional de acreditación** (en España, ENAC) con arreglo a la norma **EN-ISO/IEC 17065:2012** y los requisitos adicionales de la autoridad de control.
- **DA 1.ª LOPDGDD** (LO 3/2018, texto consolidado a 27 de diciembre de 2025): el **ENS incluirá las medidas** que deban implantarse en caso de tratamiento de datos personales, adaptando los criterios de determinación del riesgo al art. 32 del RGPD; los responsables del sector público (art. 77.1) **aplicarán las medidas del ENS** e impulsarán medidas equivalentes en sus empresas o fundaciones vinculadas de Derecho privado; cuando un tercero preste servicios en régimen de **concesión, encomienda de gestión o contrato**, las medidas se corresponden con las de la Administración de origen y se ajustan al ENS.
- En la práctica, las auditorías RGPD revisan el registro de actividades de tratamiento, las bases jurídicas, las medidas de seguridad (en las AAPP, alineadas con el ENS), las evaluaciones de impacto y los contratos de encargo (ver tema [53](53-proteccion-de-datos-personales.md)).

## Fuentes {.unnumbered .unlisted}

- ITAF, *Information Technology Audit Framework*, 4.ª ed. (ISACA, 2020).
- COBIT 2019 (ISACA, 2018); ISO 19011:2018 (4.ª edición, ISO 19011:2026, publicada; citadas por edición); ISO/IEC 27007:2020 (citada por edición).
- Real Decreto 311/2022, Esquema Nacional de Seguridad, art. 31 y anexo III (texto consolidado, última modificación 6 de noviembre de 2024).
- Resolución de 27 de marzo de 2018, ITS de Auditoría de la Seguridad de los Sistemas de Información (BOE de 3 de abril de 2018).
- Resolución de 13 de octubre de 2016, ITS de conformidad con el ENS (BOE de 2 de noviembre de 2016).
- CCN-STIC 802, *Auditorías de cumplimiento del ENS* (ed. junio 2025, citada por edición; descarga restringida del portal CCN).
- Reglamento (UE) 2016/679 (RGPD), arts. 28, 32, 39, 42, 43 y 58, DOUE L 119, de 4 de mayo de 2016 (sin actos modificativos posteriores; consulta de julio de 2026).
- Ley Orgánica 3/2018 (LOPDGDD), disposición adicional primera (texto consolidado, última modificación 27 de diciembre de 2025).
