# Gobernanza y planificación estratégica TIC

Las tecnologías de la información dejaron de ser un recurso auxiliar para convertirse en el soporte de la actividad de cualquier organización, y en especial de la Administración, que es en esencia una organización basada en la información. Este tema repasa cómo se gobiernan y planifican las TIC: los marcos de gobernanza (ISO/IEC 38500, COBIT), la planificación estratégica y el Plan de Sistemas de Información, el cuadro de mando como herramienta de dirección, la organización del departamento TIC, la evaluación de las inversiones y la calidad de los servicios públicos.

## Los sistemas de información en las organizaciones

Un **sistema de información (SI)** es el conjunto organizado de personas, procesos, datos y tecnología que recoge, procesa, almacena y distribuye la información necesaria para la operación, la gestión y la toma de decisiones. No debe confundirse con el sistema informático, que es solo su soporte tecnológico.

Según el nivel organizativo al que sirven, se distinguen:

| Nivel | Tipo de sistema | Ejemplo |
| --- | --- | --- |
| Operativo | **TPS** (procesamiento de transacciones) | Registro de entrada, nóminas |
| Táctico | **MIS** (información para la gestión) | Informes periódicos de actividad |
| Directivo | **DSS/EIS** (apoyo a la decisión y a la dirección) | Simulación de escenarios, cuadros de mando |

Entre los sistemas corporativos transversales destacan:

- **ERP** (*Enterprise Resource Planning*): integra en una única base de datos los procesos de gestión interna (económico-financiera, recursos humanos, compras, logística). Ejemplos: SAP, Oracle; en la Administración cumplen este papel los sistemas de gestión económico-presupuestaria y de personal.
- **CRM** (*Customer Relationship Management*): gestiona la relación con clientes o ciudadanos (expedientes de atención, campañas, multicanalidad). Su traslación pública es la atención ciudadana integrada (oficinas, teléfono, sede electrónica).
- **BI** (*Business Intelligence*) y almacenes de datos: explotan la información para el análisis y la decisión (ver temas [37](37-gestion-de-datos-corporativos-y-big-data.md) y [38](38-gobernanza-del-dato.md)).
- **Gestores documentales y de expedientes**: en la Administración, el sistema de información nuclear es el expediente electrónico (ver tema [55](55-documento-y-expediente-electronico.md)).

La Administración es una **organización intensiva en información**: su producto (actos administrativos, resoluciones, registros, prestaciones) es información, por lo que la calidad de sus sistemas de información condiciona directamente la calidad del servicio público.

## Gobernanza TIC: ISO/IEC 38500 y COBIT 2019

La **gobernanza TIC** es el sistema por el que el órgano de gobierno dirige y controla el uso presente y futuro de las TI: fija objetivos, asigna responsabilidades y comprueba resultados. Se distingue de la **gestión TIC**, que planifica y ejecuta dentro del marco fijado por el gobierno.

- **ISO/IEC 38500** (*Governance of IT for the organization*; **3.ª edición, 2024**): norma dirigida al órgano de gobierno. Su modelo asigna al órgano de gobierno tres tareas cíclicas: **evaluar** el uso actual y futuro de la TI, **dirigir** mediante estrategias y políticas, y **supervisar** (*monitor*) el cumplimiento y el rendimiento. Las ediciones anteriores (2008 y 2015) enunciaban **6 principios** clásicos: responsabilidad, estrategia, adquisición, rendimiento, conformidad y comportamiento humano; la edición de 2024 los reformula y amplía en línea con la ISO 37000 de gobernanza de organizaciones (propósito, generación de valor, estrategia, supervisión, rendición de cuentas, implicación de las partes interesadas, liderazgo, datos y decisiones, gobernanza del riesgo, responsabilidad social y viabilidad y rendimiento a largo plazo).
- **COBIT 2019** (ISACA): marco de **gobierno y gestión de la información y la tecnología (I&T)** de la empresa. Elementos clave:
  - **6 principios del sistema de gobierno**: aportar valor a las partes interesadas; enfoque holístico; sistema de gobierno dinámico; gobierno distinto de la gestión; adaptado a las necesidades de la organización; y de extremo a extremo (cubre toda la I&T, no solo el departamento TIC).
  - **40 objetivos de gobierno y gestión** en **5 dominios**: **EDM** (Evaluar, Dirigir y Monitorizar: gobierno, 5 objetivos), **APO** (Alinear, Planificar y Organizar, 14), **BAI** (Construir, Adquirir e Implementar, 11), **DSS** (Entregar, dar Servicio y Soporte, 6) y **MEA** (Monitorizar, Evaluar y Valorar, 4).
  - **Componentes** del sistema de gobierno (antes «habilitadores»): procesos; estructuras organizativas; principios, políticas y marcos; información; cultura, ética y comportamiento; personas, habilidades y competencias; y servicios, infraestructura y aplicaciones.
  - **Cascada de metas** (necesidades de las partes interesadas → metas empresariales → metas de alineamiento → objetivos de gobierno y gestión) y **factores de diseño** para adaptar el marco a cada organización; niveles de **capacidad de procesos de 0 a 5** basados en CMMI.

Ambos marcos son complementarios: ISO/IEC 38500 fija los principios para el órgano de gobierno y COBIT los desarrolla en objetivos, procesos y métricas auditables (ver tema [33](33-auditoria-informatica.md)).

## Planificación estratégica TIC y el Plan de Sistemas de Información

La planificación estratégica TIC traduce la estrategia de la organización en una cartera ordenada de sistemas, infraestructuras y proyectos. Su producto clásico es el **Plan de Sistemas de Información (PSI)**, que Métrica v3 define como el proceso que proporciona «un marco estratégico de referencia para los sistemas de información de un determinado ámbito de la organización».

- **Participantes**: la dirección (visión estratégica y compromiso, factor crítico de éxito) y los profesionales de SI (aportan las posibilidades de la tecnología). El enfoque es **por procesos**, no por unidades organizativas, para atender intereses globales.
- **Contenido típico del proceso**: definición del alcance y objetivos; estudio de la información relevante (planes estratégicos, normativa); identificación de requisitos; análisis de la situación actual de los SI (diagnóstico DAFO); diseño del modelo de SI objetivo; y plan de acción priorizado.
- **Productos finales** (Métrica v3): el **catálogo de requisitos** y la **arquitectura de información**, compuesta por el modelo de información, el modelo de sistemas de información, la **arquitectura tecnológica**, el **plan de proyectos** y el plan de mantenimiento del PSI. Estos productos alimentan el Estudio de Viabilidad del Sistema (EVS) de cada proyecto.
- **Horizonte y seguimiento**: los planes estratégicos TIC suelen abarcar **3 a 5 años**, con revisión periódica; la cartera de proyectos se gobierna con una oficina de proyectos (PMO, ver tema [19](19-direccion-y-gestion-de-proyectos.md)).

No debe confundirse el PSI con la reingeniería de procesos: ambos estudian los procesos y buscan el alineamiento estratégico, pero el PSI persigue orientar el desarrollo de sistemas de información, no rediseñar los procesos por sí mismos.

## El cuadro de mando integral e indicadores

El **cuadro de mando integral (CMI**, *Balanced Scorecard*, Kaplan y Norton, **1992**) traduce la estrategia en un conjunto equilibrado de objetivos e indicadores, superando la visión exclusivamente financiera.

- **Cuatro perspectivas**: **financiera** (¿qué esperan los propietarios?), **cliente** (¿cómo nos ven los usuarios?), **procesos internos** (¿en qué debemos ser excelentes?) y **aprendizaje y crecimiento** (¿cómo mantener la capacidad de mejorar?). En la Administración la perspectiva del **ciudadano** pasa a primer plano y la financiera se reinterpreta como uso eficiente del presupuesto.
- **Mapa estratégico**: representa las relaciones causa-efecto entre los objetivos de las cuatro perspectivas (la formación mejora los procesos, que mejoran el servicio, que mejora los resultados).
- **Indicadores**: cada objetivo se mide con **KPI** (indicadores clave de rendimiento) con meta y responsable; deben ser **SMART** (específicos, medibles, alcanzables, relevantes y acotados en el tiempo). Se combinan indicadores de resultado (*lag*) e inductores (*lead*).
- **Informes a la dirección**: el CMI estratégico se complementa con cuadros de mando operativos (disponibilidad de servicios, incidencias, avance de proyectos, consumo presupuestario) que hoy se materializan en herramientas de BI con actualización continua.

## Organización de un departamento TIC

No existe una estructura única, pero un departamento TIC maduro separa las funciones de demanda y estrategia de las de construcción y operación, y garantiza la **segregación entre desarrollo y explotación**.

- **Funciones habituales**: dirección y estrategia (CIO); oficina de proyectos y demanda; arquitectura y calidad; **desarrollo** de aplicaciones; **sistemas e infraestructuras** (CPD, comunicaciones, puesto de trabajo); **explotación y operaciones** (producción, monitorización); **soporte a usuarios** (CAU, gestionado con ITIL, ver tema [18](18-gestion-de-los-servicios-tic.md)); **seguridad** (CISO, con independencia funcional respecto de la operación); y, crecientemente, la función del dato (CDO, ver tema [38](38-gobernanza-del-dato.md)).
- **Modelos organizativos**: **centralizado** (un único órgano TIC corporativo: economías de escala, homogeneidad), **descentralizado** (TIC en cada unidad de negocio: cercanía, riesgo de silos) y **federado** (núcleo común más equipos sectoriales).
- **El caso de la Generalitat**: la **DGTIC** concentra desde 2011 la competencia TIC de toda la Administración de la Generalitat y su sector público instrumental (modelo centralizado), incluida la coordinación de ciberseguridad y el CSIRT-CV (ver temas [80](80-agenda-digital-valenciana.md) a [82](82-administracion-electronica-y-plataformas-de-la-generalitat.md)).

## Adquisición de sistemas y rentabilidad de las inversiones TIC

Antes de adquirir o desarrollar un sistema debe realizarse un **estudio de alternativas y de viabilidad** que compare opciones y justifique la inversión.

- **Alternativas de sourcing**: desarrollo a medida (propio o contratado), producto comercial (COTS) parametrizado, software libre, **reutilización** de soluciones de otras Administraciones (las AAPP deben consultar antes el directorio general de aplicaciones, arts. 157 y 158 de la Ley 40/2015, ver tema [50](50-proteccion-juridica-del-software-y-licencias.md)) y servicios en la nube (SaaS, ver temas [22](22-contratacion-publica-de-bienes-y-servicios-tic.md) y [51](51-computacion-en-la-nube-y-altas-prestaciones.md)).
- **Viabilidad**: técnica (¿es realizable?), económica (¿es rentable?), operativa (¿se usará?) y legal (protección de datos, ENS). En Métrica v3 la recoge el proceso **EVS**.
- **Análisis coste-beneficio**: identifica costes de inversión (CAPEX) y recurrentes (OPEX), y beneficios tangibles e intangibles (ahorro de tiempos, calidad del servicio). Métricas principales:

| Métrica | Definición | Criterio |
| --- | --- | --- |
| **ROI** | (Beneficio neto / Coste de la inversión) x 100 | Mayor es mejor |
| **TCO** | Coste total de propiedad en todo el ciclo de vida: adquisición, implantación, operación, soporte, formación y retirada (concepto difundido por Gartner) | Comparar alternativas |
| **VAN** | Valor actual neto: suma de los flujos de caja futuros descontados a una tasa, menos la inversión inicial | **VAN > 0**: la inversión crea valor |
| **TIR** | Tasa interna de retorno: tasa de descuento que hace el **VAN = 0** | **TIR > coste del capital**: aceptable |
| **Payback** | Plazo de recuperación de la inversión | Menor es mejor |

- **Particularidades públicas**: en la Administración el «beneficio» incluye el valor público (reducción de cargas administrativas, transparencia, inclusión), por lo que el análisis coste-beneficio se complementa con el análisis coste-eficacia.

## Calidad de los servicios: EFQM, CAF e ISO 9004; cartas de servicios

La gestión de la calidad de los servicios (públicos o TIC) se apoya en modelos de excelencia basados en la autoevaluación y la mejora continua (la calidad del software se trata en el tema [25](25-calidad-del-software.md); la de los servicios TIC, en el 18).

- **Modelo EFQM** (edición **2025**): modelo europeo de excelencia en gestión. Se estructura en **tres bloques**: **Dirección** (por qué y cómo se orienta la organización), **Ejecución** (cómo entrega valor) y **Resultados** (qué consigue), desarrollados en **7 criterios** y 32 subcriterios; la evaluación aplica la lógica **RADAR** (Resultados, Enfoques, Despliegue, Evaluación y Revisión) y da acceso a los sellos de reconocimiento.
- **CAF 2020** (*Common Assessment Framework*): adaptación **gratuita del modelo EFQM para las administraciones públicas** europeas, promovida por la red EUPAN y el EIPA. Es un modelo de **autoevaluación** con **9 criterios**: **5 agentes facilitadores** (liderazgo; estrategia y planificación; personas; alianzas y recursos; procesos) y **4 de resultados** (en las personas; en los ciudadanos/clientes; de responsabilidad social; clave de rendimiento).
- **ISO 9004:2018**: directrices para el **éxito sostenido** de una organización mediante la gestión de la calidad; incluye una herramienta de autoevaluación de madurez. No es certificable (complementa a la ISO 9001:2015).
- **Cartas de servicios**: en la AGE se regulan en el **Real Decreto 951/2005**, que establece el **marco general para la mejora de la calidad** con **6 programas**: análisis de la demanda y evaluación de la satisfacción; **cartas de servicios**; quejas y sugerencias; evaluación de la calidad de las organizaciones; reconocimiento; y Observatorio de la Calidad de los Servicios Públicos. La carta de servicios informa sobre los servicios, los **derechos** de los usuarios, los **compromisos de calidad** (plazos, horarios, indicadores) y las **medidas de subsanación** en caso de incumplimiento (que no generan responsabilidad patrimonial). Existen también **cartas de servicios electrónicos** y la norma **UNE 93200** especifica sus requisitos.

## La organización TIC de la Administración General del Estado

La gobernanza TIC de la AGE se renovó por completo a finales de 2024, sustituyendo el modelo del RD 806/2014.

- **Real Decreto 1125/2024**, de 5 de noviembre, de organización e instrumentos operativos para la **Administración Digital** de la Administración del Estado (**deroga el RD 806/2014**). Órganos de gobernanza:
  - **Comisión de Estrategia sobre Tecnologías de la Información y las Comunicaciones (CETIC)**: órgano superior, presidido por la persona titular del **Ministerio para la Transformación Digital y de la Función Pública**.
  - **Comisiones Ministeriales de Administración Digital (CMAD)**: órganos colegiados de cada departamento, presididos por su Subsecretaría.
  - **Comité de Dirección de las Tecnologías de la Información y las Comunicaciones (CDTIC)**: órgano de apoyo, presidido por la dirección de la Agencia.
  - Instrumentos operativos: la **Estrategia TIC** (aprobada por el Gobierno), los planes de acción departamentales y el catálogo de medios y servicios comunes.
- **Agencia Estatal de Administración Digital (AEAD)**: sucede a la Secretaría General de Administración Digital como brazo ejecutor TIC de la AGE; su Estatuto se aprobó por el **Real Decreto 1118/2024**, de 5 de noviembre, y se constituyó el **21 de febrero de 2025**. Presta los servicios comunes y compartidos de administración digital (ver tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)) y se organiza en tres direcciones (Administración Digital; Provisión de Infraestructuras y Operaciones; y Ciberseguridad, Tecnologías Disruptivas e Integridad de los Datos) más una Secretaría General.
- **Plan de Digitalización de las Administraciones Públicas 2021-2025**: estrategia de administración digital dentro de la agenda **España Digital 2026**, financiada por el Plan de Recuperación; sus **tres ejes** eran la transformación digital de la AGE, los proyectos tractores sectoriales (sanidad, justicia, empleo) y la digitalización de CCAA y EELL. Su informe de balance se presentó en 2026 y la planificación pasa a articularse mediante la Estrategia TIC del RD 1125/2024.
- **Contraste con la GVA**: la AGE combina un órgano ejecutivo común (AEAD) con unidades TIC departamentales coordinadas por la CETIC; la Generalitat concentra la competencia en la DGTIC (ver tema [80](80-agenda-digital-valenciana.md)).

## Supuesto práctico: elaboración de un plan estratégico TIC

**Enunciado**: un organismo autónomo de la Generalitat con **1.500 empleados** encarga a su nueva jefatura de servicio de informática un **plan estratégico TIC 2027-2029**. Situación de partida: unas **40 aplicaciones** desarrolladas sin arquitectura común (varias sobre tecnologías fuera de soporte), tramitación aún parcialmente en papel, adecuación al ENS sin completar, proyectos que se aprueban caso a caso sin cartera priorizada y presupuesto TIC disperso entre unidades. La dirección quiere alinear las TIC con su plan de gestión (mejorar el servicio al ciudadano, reducir cargas, cumplir la normativa) y aprovechar los servicios comunes de la DGTIC.

**Se pide**:

- a) Metodología y fases de elaboración del plan.
- b) Diagnóstico de la situación actual.
- c) Modelo objetivo: líneas estratégicas y cartera de proyectos priorizada.
- d) Gobernanza del plan, cuadro de mando y seguimiento.

**Resolución**:

**a) Metodología y fases**

Se adapta el proceso de **Plan de Sistemas de Información** de Métrica v3, con horizonte de **3 años** y revisión anual:

1. **Inicio**: alcance (todo el organismo, con enfoque **por procesos**, no por unidades), patrocinio explícito de la dirección (factor crítico de éxito) y equipo mixto (dirección y profesionales de SI).
2. **Estudio de la información relevante**: plan de gestión del organismo, normativa aplicable (Leyes 39 y 40/2015, ENS, RGPD, accesibilidad), estrategias superiores (Estrategia TIC de la AGE, agenda digital de la GVA) y catálogo de servicios comunes reutilizables.
3. **Identificación de requisitos**: entrevistas y talleres por proceso de negocio.
4. **Diagnóstico de la situación actual** (apartado b).
5. **Modelo de SI objetivo**: arquitectura de información y arquitectura tecnológica.
6. **Plan de acción**: cartera de proyectos priorizada, calendario, presupuesto y plan de mantenimiento del PSI.
7. **Aprobación por la dirección** y comunicación a toda la organización.

**b) Diagnóstico (DAFO)**

| | Favorable | Desfavorable |
| --- | --- | --- |
| **Interno** | Fortalezas: equipo TIC con conocimiento del negocio; datos de gestión abundantes | Debilidades: obsolescencia tecnológica, 40 aplicaciones sin integrar, ENS incompleto, ausencia de gestión de cartera |
| **Externo** | Oportunidades: servicios comunes de la DGTIC y del Estado, nube, fondos europeos, automatización e IA | Amenazas: ciberamenazas crecientes, dependencia de proveedores, dificultad para retener talento TIC, exigencia normativa |

El diagnóstico se completa con el inventario valorado de aplicaciones e infraestructuras (criticidad, estado tecnológico, coste anual) y una evaluación de madurez (por ejemplo, con los niveles de capacidad de COBIT).

**c) Modelo objetivo y cartera de proyectos**

Se definen **4 líneas estratégicas** con objetivos medibles, y los proyectos se priorizan por **valor** (público y económico: coste-eficacia, VAN/TCO) frente a **esfuerzo y riesgo**, empezando por victorias rápidas (*quick wins*):

| Línea estratégica | Proyectos (ejemplos) | Prioridad |
| --- | --- | --- |
| 1. Servicios digitales al ciudadano | Tramitación electrónica de extremo a extremo de los 10 procedimientos de mayor volumen; carpeta ciudadana | Alta |
| 2. Modernización tecnológica | Racionalización de las 40 aplicaciones; retirada de tecnologías fuera de soporte; migración a la plataforma corporativa/nube | Alta |
| 3. Seguridad y cumplimiento | Completar la adecuación al ENS (tema [29](29-esquema-nacional-de-seguridad.md)); continuidad de servicios | Alta (obligación normativa) |
| 4. Gobierno del dato | Inventario y calidad del dato; cuadro de mando directivo | Media |

Cada proyecto de la cartera se documenta con: objetivo, línea a la que sirve, coste (CAPEX/OPEX), beneficios esperados, riesgos, dependencias y calendario.

**d) Gobernanza, cuadro de mando y seguimiento**

- **Gobernanza** (ISO/IEC 38500): un **comité de dirección TIC** presidido por la dirección del organismo **evalúa, dirige y supervisa**; la ejecución de la cartera se encomienda a una **oficina de proyectos** (PMO, tema [19](19-direccion-y-gestion-de-proyectos.md)); la seguridad se reporta con independencia de la operación.
- **Cuadro de mando integral** adaptado al sector público, con indicadores SMART por perspectiva:

| Perspectiva | KPI (ejemplo) | Meta |
| --- | --- | --- |
| Ciudadano | % de tramitación electrónica de los procedimientos objetivo | > 90 % en 2029 |
| Financiera (presupuesto) | Ejecución del presupuesto TIC; TCO de las aplicaciones racionalizadas | 100 %; reducción del 20 % |
| Procesos internos | Disponibilidad de servicios críticos; % de proyectos en plazo y coste | 99,5 %; 80 % |
| Aprendizaje y crecimiento | Horas de formación TIC por persona; puestos críticos cubiertos | 20 h/año; 100 % |

- **Seguimiento**: cuadro de mando operativo mensual para el comité, revisión **anual** del plan (repriorización de la cartera según resultados y cambios normativos) y evaluación final que alimente el siguiente ciclo de planificación.

## Fuentes {.unnumbered .unlisted}

- ISO/IEC 38500:2024, *Information technology. Governance of IT for the organization*, 3.ª ed., febrero de 2024.
- COBIT 2019 *Framework: Introduction and Methodology* (ISACA, 2018).
- Métrica versión 3, documento «Introducción» (Ministerio de Administraciones Públicas, PAe).
- Kaplan, R. y Norton, D., *The Balanced Scorecard* (1992, Harvard Business Review; 1996, HBS Press).
- Real Decreto 951/2005, marco general para la mejora de la calidad en la AGE (texto consolidado, última modificación 30 de junio de 2009).
- Modelo EFQM, edición 2025 (EFQM, 2024); CAF 2020 (EIPA); ISO 9004:2018; UNE 93200:2008.
- Real Decreto 1118/2024 (Estatuto de la AEAD) y Real Decreto 1125/2024 (organización de la Administración Digital del Estado), BOE, contrastados online en julio de 2026.
- Ley 40/2015, arts. 157-158 (texto consolidado, última modificación 2 de agosto de 2024).
- Plan de Digitalización de las Administraciones Públicas 2021-2025 y España Digital 2026 (webs oficiales, consultadas en julio de 2026).
