# La gestión de los servicios TIC

La gestión de servicios TIC (ITSM, *IT Service Management*) organiza el trabajo de un departamento de tecnología como un conjunto de servicios orientados al valor para el negocio, en lugar de como una colección de sistemas y tareas técnicas. El marco de referencia dominante es **ITIL** (*Information Technology Infrastructure Library*), hoy en su edición **ITIL 4** (2019).

## La gestión de servicios TIC: conceptos

ITIL es un conjunto de buenas prácticas para la gestión de servicios TI, construido a partir de la observación de organizaciones reales. Su meta es alinear los servicios de TI con las necesidades del negocio y aportar valor tanto a clientes externos como internos. Sus conceptos centrales son:

- **Gestión de servicios**: «conjunto de capacidades organizativas especializadas para proporcionar valor a los clientes en forma de servicios».
- **Servicio**: «medio que permite la co-creación de valor al facilitar los resultados que los clientes quieren lograr, sin que el cliente tenga que gestionar costes y riesgos específicos».
- **Valor**: «percepción de beneficios, utilidad e importancia de algo». No lo entrega el proveedor en solitario: se **co-crea** en la relación proveedor-consumidor.
- **Producto y oferta de servicio**: un producto es una configuración de recursos de la organización diseñada para ofrecer valor; una oferta de servicio combina **bienes**, **acceso a recursos** y **acciones de servicio**.
- **Utilidad y garantía**: un servicio debe ofrecer ambas para generar valor.
    - **Utilidad**: la funcionalidad que satisface una necesidad concreta («apto para el propósito», *fit for purpose*).
    - **Garantía**: el aseguramiento de que rendirá según lo acordado («apto para el uso», *fit for use*): disponibilidad, capacidad y rendimiento, continuidad y seguridad.
- **Salidas y resultados**: la salida (*output*) es el entregable tangible; el resultado (*outcome*) es lo que el consumidor consigue gracias a él. El valor se juzga por resultados, costes y riesgos.
- **Roles del consumidor**: **cliente** (define los requisitos y responde de los resultados), **usuario** (utiliza el servicio) y **patrocinador** (autoriza el presupuesto).
- **Carácter no prescriptivo**: ITIL no es un estándar de obligado cumplimiento sino buenas prácticas que cada organización **adopta y adapta** (*adopt and adapt*). Es independiente de proveedor y cuenta con un esquema de certificación de profesionales.
- **ISO/IEC 20000-1:2018**: norma internacional **certificable** de sistemas de gestión de servicios (SGS). Define requisitos auditables y está alineada con ITIL (que, por sí misma, no es certificable para organizaciones, solo para personas).

### Evolución de ITIL

- **ITIL v1 (1989)**: biblioteca inicial de la agencia británica CCTA, una treintena de volúmenes.
- **ITIL v2 (2000-2002)**: consolidación en libros por áreas; los dos centrales fueron **Soporte del Servicio** (libro azul, procesos operativos) y **Provisión del Servicio** (libro rojo, procesos tácticos).
- **ITIL v3 (2007, edición 2011)**: organiza la gestión en el **ciclo de vida del servicio**: **5 fases** y **26 procesos**.
- **ITIL 4 (febrero de 2019)**: publicada por AXELOS (propiedad de PeopleCert desde 2021). Sustituye el ciclo de vida por el **sistema de valor del servicio (SVS)** y los procesos por **34 prácticas**; integra los enfoques agile, DevOps y lean. Es la edición de referencia actual y la base de este tema.
- **ITIL 5 (12 de febrero de 2026)**: lanzada por PeopleCert como evolución, no ruptura: conserva el sistema de valor y los principios guía, e incorpora un ciclo de vida de producto y servicio de **8 etapas**, la gobernanza de la IA y la orientación a la gestión de productos y servicios digitales (DPSM). Convive con ITIL 4 durante la transición (las publicaciones de prácticas se actualizan a lo largo de 2026).

El ciclo de vida de ITIL v3, hoy superado, sigue apareciendo en preguntas de examen:

| Fase (v3) | Procesos |
| --- | --- |
| Estrategia del servicio | 5: generación de la estrategia, portafolio, financiera, demanda y relaciones con el negocio |
| Diseño del servicio | 8: coordinación del diseño, catálogo, niveles de servicio, capacidad, disponibilidad, continuidad, seguridad de la información y suministradores |
| Transición del servicio | 7: planificación y soporte, cambios, activos y configuración, versiones y despliegues, validación y pruebas, evaluación del cambio y conocimiento |
| Operación del servicio | 5 procesos (eventos, incidencias, peticiones, problemas y accesos) y 4 funciones (centro de servicio al usuario, gestión técnica, de operaciones y de aplicaciones) |
| Mejora continua del servicio | proceso de mejora en 7 pasos |

## ITIL 4: sistema de valor del servicio y principios guía

El **sistema de valor del servicio (SVS)** es el modelo central de ITIL 4: describe cómo todos los componentes y actividades de la organización trabajan juntos, como un sistema, para facilitar la creación de valor. Sus entradas son la **oportunidad** y la **demanda**; su salida es el **valor**.

Componentes del SVS (5):

- **Principios guía**: recomendaciones que orientan a la organización en cualquier circunstancia, incluso si cambian sus metas, estrategias o estructura.
- **Gobernanza**: dirección y control de la organización por su órgano de gobierno, mediante las actividades de **evaluar, dirigir y monitorizar**.
- **Cadena de valor del servicio**: el modelo operativo central, con 6 actividades.
- **Prácticas**: 34 conjuntos de recursos organizativos diseñados para realizar un trabajo o lograr un objetivo.
- **Mejora continua**: presente en todos los niveles del sistema.

Los **7 principios guía**:

| # | Principio | Idea clave |
| --- | --- | --- |
| 1 | **Enfocarse en el valor** | todo lo que hace la organización debe aportar valor a las partes interesadas; incluye la experiencia de cliente y de usuario (CX/UX) |
| 2 | **Comenzar donde se está** | no partir de cero: evaluar objetivamente lo existente (medición directa) y aprovecharlo |
| 3 | **Progresar iterativamente con retroalimentación** | trabajar en iteraciones pequeñas y manejables, con bucles de feedback antes, durante y después |
| 4 | **Colaborar y promover la visibilidad** | trabajar juntos a través de fronteras organizativas; hacer visibles el trabajo y sus resultados, evitando agendas ocultas |
| 5 | **Pensar y trabajar holísticamente** | ningún servicio, práctica o departamento funciona aislado; visión de extremo a extremo del servicio |
| 6 | **Mantenerlo simple y práctico** | usar el mínimo número de pasos; eliminar lo que no aporta valor; buscar soluciones basadas en resultados |
| 7 | **Optimizar y automatizar** | optimizar primero y automatizar después; reservar la intervención humana para lo que realmente la necesita |

## Las cuatro dimensiones y la cadena de valor

Para que el SVS funcione de forma equilibrada, ITIL 4 obliga a considerar **cuatro dimensiones** en el diseño y operación de todo servicio (sustituyen a las «4 P» del diseño del servicio de v3: personas, procesos, productos y *partners*):

| Dimensión | Alcance |
| --- | --- |
| **1. Organizaciones y personas** | estructura organizativa, roles y responsabilidades, cultura, capacitación y liderazgo |
| **2. Información y tecnología** | la información y el conocimiento que los servicios gestionan y las tecnologías que los soportan, con sus relaciones y controles |
| **3. Socios y proveedores** | relaciones con otras organizaciones para diseñar, desplegar y prestar servicios; estrategia de aprovisionamiento e integración de servicios (SIAM) |
| **4. Flujos de valor y procesos** | cómo se organizan las actividades y los flujos de trabajo de la organización para crear valor |

- **Factores externos (PESTLE)**: políticos, económicos, sociales, tecnológicos, legales y ambientales. Condicionan a las cuatro dimensiones y no están bajo el control de la organización.

La **cadena de valor del servicio** es el modelo operativo del SVS: **6 actividades** que se combinan, junto con las prácticas, en **flujos de valor** específicos para cada escenario (por ejemplo, «resolver un incidente» o «desplegar una nueva funcionalidad»):

| Actividad | Propósito |
| --- | --- |
| **Planificar** | visión compartida, comprensión del estado actual y dirección de mejora para las cuatro dimensiones |
| **Mejorar** | mejora continua de productos, servicios y prácticas en toda la cadena |
| **Involucrar** (*engage*) | comprender las necesidades de las partes interesadas, dar transparencia y mantener las relaciones |
| **Diseño y transición** | asegurar que productos y servicios cumplen las expectativas de calidad, coste y plazo |
| **Obtener/construir** | asegurar que los componentes del servicio están disponibles cuándo y dónde se necesitan y cumplen las especificaciones |
| **Entregar y soportar** | prestar y soportar los servicios según las especificaciones y las expectativas acordadas |

Las **34 prácticas** de ITIL 4 se organizan en **3 grupos**:

| Grupo | Prácticas |
| --- | --- |
| **Gestión general (14)** | estrategia; portafolio; arquitectura; gestión financiera de servicios; fuerza de trabajo y talento; mejora continua; medición e informes; riesgos; seguridad de la información; conocimiento; cambio organizacional; proyectos; relaciones; proveedores |
| **Gestión de servicios (17)** | análisis del negocio; catálogo de servicios; diseño del servicio; nivel de servicio; disponibilidad; capacidad y rendimiento; continuidad del servicio; monitorización y eventos; centro de servicios; incidentes; peticiones de servicio; problemas; versiones; habilitación del cambio; validación y pruebas; configuración del servicio; activos de TI |
| **Gestión técnica (3)** | despliegues; infraestructura y plataforma; desarrollo y gestión de software |

## Prácticas clave: incidencias, problemas, cambios, nivel de servicio

Estas prácticas concentran la operación diaria de un departamento TIC y la mayor parte de las preguntas de examen. El punto de entrada habitual es el **centro de servicios** (*service desk*): el **punto único de contacto** (SPOC) entre el proveedor y los usuarios, que captura la demanda de resolución de incidentes y de **peticiones de servicio** (solicitudes que forman parte de la entrega normal y preacordada del servicio, como altas de usuarios o accesos, gestionadas por la práctica de gestión de peticiones y a menudo automatizables).

- **Gestión de incidentes**:
    - **Incidente**: «interrupción no planificada de un servicio o reducción de la calidad de un servicio».
    - **Objetivo**: restaurar la operación normal del servicio **lo antes posible**, minimizando el impacto negativo.
    - **Priorización**: prioridad = **impacto × urgencia**; determina los tiempos objetivo de resolución acordados en los SLA.
    - **Escalado**: **funcional** (a un grupo con más conocimiento técnico) y **jerárquico** (a la línea de mando).
    - **Incidentes graves** (*major incidents*): procedimiento propio, equipo temporal dedicado y comunicación reforzada; el ***swarming*** (varios especialistas trabajando a la vez sobre el caso) es una técnica de colaboración habitual.
- **Gestión de problemas**:
    - **Problema**: «causa, o causa potencial, de uno o más incidentes».
    - **Tres fases**: **identificación del problema** (análisis de tendencias, incidentes graves o recurrentes), **control del problema** (análisis de causas y priorización) y **control de errores** (gestión de los errores conocidos y evaluación periódica de su solución definitiva).
    - **Error conocido**: problema que ha sido analizado pero aún no resuelto.
    - **Solución temporal** (*workaround*): reduce o elimina el impacto del incidente o problema sin resolver su causa; se documenta y se reevalúa.
    - **Enfoques**: **reactivo** (a partir de incidentes ya ocurridos) y **proactivo** (identificar riesgos y debilidades para prevenir incidentes futuros).
- **Habilitación del cambio** (*change enablement*):
    - **Cambio**: «adición, modificación o eliminación de cualquier elemento que pueda tener un efecto directo o indirecto sobre los servicios».
    - **Tipos de cambio**: **estándar** (preautorizado, de bajo riesgo y bien documentado), **normal** (requiere autorización según su riesgo, desde un responsable de equipo hasta la dirección) y **de emergencia** (implantación urgente; autoridad de cambio propia y documentación que puede diferirse).
    - **Autoridad de cambio** (*change authority*): la persona o grupo que autoriza cada tipo de cambio. ITIL 4 la descentraliza: el comité de cambios (CAB) de v3 deja de ser el único órgano autorizador.
    - **Las 7 R** (lista de comprobación heredada de v3): quién lo **solicitó** (*raised*), **razón**, **retorno**, **riesgos**, **recursos**, **responsable** y **relación** con otros cambios.
    - **Calendario de cambios**: planifica y comunica los cambios para evitar conflictos y ventanas simultáneas.
- **Gestión de nivel de servicio**:
    - **Objetivo**: fijar objetivos claros de rendimiento del servicio basados en el negocio y evaluar, monitorizar y gestionar los servicios contra esos objetivos.
    - **SLA** (*Service Level Agreement*, acuerdo de nivel de servicio): documento acordado entre proveedor y cliente con los niveles de servicio comprometidos; debe ligarse a **resultados definidos** para el cliente, no solo a métricas operativas.
    - **Efecto sandía** (*watermelon SLA*): un SLA «verde» por fuera (todas las métricas cumplidas) y «rojo» por dentro (cliente insatisfecho); se evita midiendo también la experiencia y los resultados.
    - **Soportes del SLA**: acuerdos de nivel operativo (**OLA**) con los grupos internos y contratos con proveedores externos (gestionados por la práctica de gestión de proveedores).
    - **Fuentes de información**: retroalimentación de clientes y usuarios, métricas operativas y de negocio, y revisiones periódicas del servicio.

## La mejora continua

En ITIL 4 la mejora continua es tres cosas a la vez: un componente del SVS, una actividad de la cadena de valor y una práctica de gestión general. Alcanza a todos los productos, servicios, prácticas y relaciones de la organización, y es responsabilidad de todos los niveles, no de un único equipo de calidad.

El **modelo de mejora continua** guía cualquier iniciativa mediante **7 pasos** en forma de pregunta:

| Paso | Pregunta | Contenido |
| --- | --- | --- |
| 1 | ¿Cuál es la visión? | visión, misión, metas y objetivos del negocio |
| 2 | ¿Dónde estamos ahora? | evaluación de la situación actual (línea base) |
| 3 | ¿Dónde queremos estar? | objetivos de mejora medibles (KPI, factores críticos de éxito) |
| 4 | ¿Cómo llegamos allí? | definición del plan de mejora |
| 5 | Actuar | ejecución de las acciones de mejora |
| 6 | ¿Hemos llegado? | comprobación de métricas e indicadores frente a los objetivos |
| 7 | ¿Cómo mantenemos el impulso? | consolidar e institucionalizar la mejora en la cultura |

- **Registro de mejora continua (CIR,** *continual improvement register***)**: base de datos o documento estructurado donde se registran, priorizan y siguen las ideas de mejora; puede haber varios (por organización, equipo o servicio).
- **Métodos complementarios**: el modelo es compatible con el ciclo **PDCA** de Deming (planificar-hacer-verificar-actuar), lean (eliminación de desperdicio), agile y DevOps.
- **Papel del liderazgo**: la dirección debe integrar la mejora en la cultura, asignar recursos y dar ejemplo; los principios «progresar iterativamente» y «enfocarse en el valor» aplican a cada iniciativa.

## Supuesto práctico: catálogo de servicios, SLA y dimensionamiento de un CAU

**Enunciado**: una conselleria con **3.000 empleados** repartidos entre los servicios centrales y las direcciones territoriales decide centralizar su soporte TIC, hoy disperso: las incidencias se comunican por teléfono o correo a técnicos concretos, sin registro, sin prioridades y sin compromisos de servicio. Se implantará un modelo conforme a **ITIL 4** con un **centro de atención a usuarios (CAU)** como punto único de contacto. Datos medidos durante tres meses: **0,7 contactos por usuario y mes** (70 % incidencias, 30 % peticiones de servicio), tiempo medio de atención de **10 minutos** por contacto, horario de soporte de **8:00 a 20:00** de lunes a viernes (**21 días laborables** al mes de media), ocupación máxima de los agentes del **75 %**, jornada efectiva de **7 horas** y factor de merma por vacaciones, ausencias y formación del **20 %**.

**Se pide**:

- a) Diseñar el modelo de soporte: funciones del centro de servicios, niveles y escalados.
- b) Definir el catálogo de servicios y la estructura del SLA, con su matriz de prioridades.
- c) Dimensionar el número de agentes del CAU.
- d) Establecer los indicadores de seguimiento y el plan de mejora continua.

**Resolución**:

**a) Modelo de soporte**

- **Centro de servicios como punto único de contacto (SPOC)**: todo contacto entra por los canales oficiales (teléfono, correo, portal de autoservicio) y se **registra, clasifica y prioriza** en la herramienta ITSM; desaparece el soporte informal a técnicos concretos.
- **Separación de flujos**: las **incidencias** (interrupción o degradación no planificada) siguen la gestión de incidentes; las **peticiones de servicio** (altas, accesos, software estándar) siguen flujos preacordados y automatizables desde el portal; los cambios derivados pasan por la **habilitación del cambio** (estándar preautorizado, normal o de emergencia).
- **Niveles de soporte**: **nivel 1** (CAU: registro, diagnóstico con guiones y base de conocimiento, resolución del mayor número posible de casos), **nivel 2** (grupos especialistas: sistemas, comunicaciones, aplicaciones) y **nivel 3** (fabricantes y proveedores, bajo contrato). Escalado **funcional** entre niveles y **jerárquico** hacia la línea de mando; los **incidentes graves** tienen procedimiento propio, con equipo dedicado y comunicación reforzada.
- **Gestión de problemas**: análisis de tendencias sobre lo registrado para identificar problemas, documentar **errores conocidos** y sus **soluciones temporales** (*workarounds*) en la base de conocimiento del nivel 1.

**b) Catálogo de servicios y SLA**

- **Catálogo de servicios**: describe los servicios en explotación con la vista del usuario, no de la tecnología: puesto de trabajo, correo y colaboración, cada aplicación corporativa, telefonía, conectividad, impresión. Cada entrada recoge descripción, destinatarios, horario, forma de solicitud y niveles comprometidos.
- **Estructura del SLA**: alcance y descripción del servicio, horario de soporte, compromisos medibles (tiempos de respuesta y resolución por prioridad, disponibilidad), exclusiones, forma de medición, informes y calendario de revisión. Debe ligarse a **resultados** para el usuario, no solo a métricas operativas.
- **Soportes internos y externos**: el SLA se apoya en **OLA** con los grupos internos de nivel 2 y en los **contratos con proveedores** (tema [22](22-contratacion-publica-de-bienes-y-servicios-tic.md)), cuyos tiempos de soporte deben ser coherentes con lo comprometido al usuario.
- **Matriz de prioridades** (prioridad = **impacto × urgencia**):

| Impacto \ Urgencia | Alta | Media | Baja |
| --- | :---: | :---: | :---: |
| **Alto** (servicio esencial o muchos usuarios) | P1 | P2 | P3 |
| **Medio** (una unidad o grupo) | P2 | P3 | P4 |
| **Bajo** (un usuario con alternativa) | P3 | P4 | P4 |

- **Objetivos por prioridad** (ejemplo de compromiso en el SLA): **P1**: respuesta 15 min y resolución 4 h; **P2**: respuesta 1 h y resolución 8 h laborables; **P3**: respuesta 4 h y resolución 2 días; **P4**: respuesta 1 día y resolución 5 días.

**c) Dimensionamiento del CAU**

- **Volumen**: 3.000 usuarios × 0,7 = **2.100 contactos/mes**; 2.100 / 21 = **100 contactos/día**.
- **Carga de atención**: 100 × 10 min = 1.000 min ≈ **16,7 horas/día**.
- **Con ocupación máxima del 75 %**: 16,7 / 0,75 ≈ **22,2 horas-agente/día** (la ocupación limitada absorbe los picos y el trabajo interno: documentación, formación).
- **Agentes simultáneos**: 22,2 / 7 ≈ 3,2 → **4 agentes** operativos cada día, en dos turnos solapados que cubren las 12 horas y refuerzan el pico de media mañana.
- **Plantilla con merma del 20 %**: 4 / 0,8 = **5 agentes** en plantilla.
- Para volúmenes mayores, el cálculo fino de la simultaneidad se haría con teoría de colas (**Erlang C**, probabilidad de espera por franja); a esta escala basta el cálculo por carga, con el margen que dan la ocupación del 75 % y el redondeo al alza.

**d) Indicadores y mejora continua**

- **KPI operativos**: volumen por canal y servicio, **tasa de resolución en primer contacto (FCR)**, tiempos medios de respuesta y resolución por prioridad, **porcentaje de cumplimiento del SLA**, casos pendientes (backlog) y reaperturas.
- **KPI de experiencia**: encuesta breve tras cada cierre y medición periódica de satisfacción, para evitar el **efecto sandía** (SLA verde por fuera, usuarios descontentos por dentro).
- **Mejora continua**: las desviaciones e ideas alimentan el **registro de mejora continua (CIR)** y se gestionan con el **modelo de 7 pasos**: la visión es el soporte único con compromisos; la línea base, los tres meses medidos; los objetivos, medibles (p. ej. FCR > 70 %, cumplimiento de SLA > 95 %); y cada trimestre se revisan catálogo, SLA y dimensionamiento con los datos reales, progresando iterativamente con retroalimentación.

## Fuentes {.unnumbered .unlisted}

- ITIL Foundation, ITIL 4 Edition. AXELOS, febrero de 2019 (material oficial de formación ITIL 4 Foundation v4.2, PeopleCert, marzo de 2025).
- ITIL v3, edición 2011 (Cabinet Office), para la evolución histórica y el ciclo de vida del servicio.
- ISO/IEC 20000-1:2018, Information technology. Service management. Part 1: Service management system requirements.
- PeopleCert, lanzamiento de ITIL 5 (Foundation, 12 de febrero de 2026), peoplecert.org.
