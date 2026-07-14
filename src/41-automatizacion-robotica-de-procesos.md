# Automatización robótica de procesos (RPA)

La automatización robótica de procesos permite automatizar tareas administrativas repetitivas sin modificar los sistemas existentes, mediante robots software que trabajan sobre las mismas aplicaciones que usan las personas. Este tema cubre el concepto y los niveles de automatización, qué procesos conviene automatizar en la Administración y con qué marco jurídico, y las plataformas y tecnologías de IA que amplían sus capacidades.

## Concepto, beneficios y niveles de automatización

La **automatización robótica de procesos** (*Robotic Process Automation*, RPA) es una tecnología que automatiza procesos de negocio mediante **robots software** (*bots*) que emulan las acciones de una persona sobre la interfaz de usuario de las aplicaciones: leen pantallas, teclean datos, copian información entre sistemas y ejecutan reglas predefinidas.

- **No invasiva**: el robot opera por la capa de presentación, así que no exige modificar los sistemas existentes ni que estos dispongan de API. Es su rasgo distintivo frente a la integración tradicional; cuando la API existe, las plataformas RPA también pueden invocarla.
- **Low-code**: los robots se construyen con grabadoras de acciones y diseñadores visuales de flujos, lo que reduce (aunque no elimina) la necesidad de programar.
- **Tecnología madura**: lejos de ser emergente, es un mercado consolidado (unos **3800 millones de dólares en 2024**, según Gartner); lo emergente es su fusión con la IA.
- **Tipos de robots**:
    - **Atendidos**: se ejecutan en el puesto del empleado y colaboran con él, lanzados a demanda durante su trabajo.
    - **Desatendidos**: se ejecutan en servidores de forma autónoma, planificados o alimentados por colas de trabajo, sin intervención humana.
    - **Híbridos**: combinan ambos modos en un mismo proceso.

Los **beneficios** principales son:

- **Reducción de costes** operativos del trabajo manual repetitivo.
- **Calidad y consistencia**: se eliminan los errores de transcripción y el proceso se ejecuta siempre igual.
- **Rapidez y disponibilidad**: ejecución mucho más rápida que la humana, **24x7**.
- **Escalabilidad**: absorber picos de trabajo añadiendo robots, sin contratar ni formar.
- **Trazabilidad**: cada ejecución queda registrada, lo que facilita el control y la auditoría.
- **Valor del personal**: los empleados se liberan de tareas mecánicas y se dedican a las de mayor valor (atención, supervisión, resolución de casos complejos).
- **Retorno rápido**: al no tocar los sistemas de fondo, un robot puede estar en producción en semanas.

Y las **limitaciones y riesgos** a vigilar:

- **Fragilidad**: cualquier cambio en la interfaz de una aplicación puede romper el robot; exige mantenimiento continuo.
- **Solo reglas**: sin IA, el robot no maneja juicio, excepciones frecuentes ni datos no estructurados.
- **Automatizar el desorden**: robotizar un proceso ineficiente consolida su ineficiencia; a veces lo correcto es rediseñar o integrar de verdad (vía API) en lugar de automatizar la pantalla.
- **Proliferación sin gobierno**: robots huérfanos, credenciales mal gestionadas y automatizaciones no inventariadas son un riesgo operativo y de seguridad.

Los **niveles de automatización** ordenan el camino desde la tarea manual hasta la automatización de extremo a extremo:

| Nivel | Denominación | Características |
| --- | --- | --- |
| 0 | Proceso manual | Toda la tarea la realiza una persona |
| 1 | Scripts y macros | Automatización local, dentro de una sola aplicación |
| 2 | RPA asistida | Robot en el puesto que colabora con la persona (atendido) |
| 3 | RPA desatendida | Robots orquestados en servidor, con colas y planificación |
| 4 | Automatización inteligente (IPA) | RPA + IA: documentos no estructurados, lenguaje natural, decisiones basadas en modelos |
| 5 | Hiperautomatización | Automatización sistemática de extremo a extremo combinando RPA, IA, BPM y minería de procesos |

## Procesos automatizables en la Administración

No todo proceso es buen candidato a RPA. Los idóneos comparten unos **criterios de idoneidad**:

- **Basados en reglas**: pasos estructurados y decisiones predefinidas, sin juicio humano.
- **Alto volumen y repetitivos**: la inversión se rentabiliza por repetición.
- **Datos digitalizados y estructurados**: la entrada debe ser legible por el robot (o requerirá IA).
- **Estables**: procesos y aplicaciones que no cambian con frecuencia.
- **Propensos a error humano**: transcripciones y cotejos manuales.
- **Multi-sistema sin integración disponible**: el robot suple la falta de APIs entre aplicaciones.
- **Con disparadores digitales**: se inician ante eventos identificables (llegada de un formulario, una factura, un vencimiento).

Ejemplos típicos en la Administración pública:

- **Tramitación**: volcado de datos entre el registro de entrada, el gestor de expedientes y las aplicaciones sectoriales.
- **Gestión económica**: procesamiento y contabilización de facturas, conciliaciones.
- **Personal**: nóminas, certificados, gestión de permisos y licencias.
- **Subvenciones y ayudas**: comprobación masiva de requisitos y cruces de datos con otras administraciones.
- **Gestión tributaria**: cruces de información, generación de requerimientos y notificaciones masivas.
- **Atención al ciudadano**: clasificación y contestación de correos y solicitudes frecuentes (con apoyo de IA).
- **Sistemas**: migraciones de datos entre aplicaciones heredadas, informes periódicos, cargas y descargas de datos.

La **integración del RPA en una organización** requiere algo más que comprar una herramienta:

- **Identificación y priorización**: inventariar procesos candidatos (talleres, minería de procesos) y priorizarlos en una matriz beneficio/complejidad.
- **Caso de negocio**: estimar horas liberadas, errores evitados y plazo de retorno.
- **Selección de plataforma**: según integración con el puesto, escalabilidad, seguridad y coste.
- **Piloto y escalado**: empezar por procesos acotados de éxito probable y escalar progresivamente.
- **Centro de excelencia (CoE)**: unidad que fija la metodología, los estándares de desarrollo, el catálogo de robots y la gestión de credenciales.
- **Gestión del cambio**: formación e implicación del personal, cuyo trabajo se rediseña.
- **Operación**: monitorización de los robots, gestión de incidencias y mantenimiento ante cambios en las aplicaciones.

En la Administración, la RPA desatendida que produce efectos en procedimientos enlaza con la **actuación administrativa automatizada** de la **Ley 40/2015**:

- **Art. 41.1**: es actuación administrativa automatizada «cualquier acto o actuación realizada íntegramente a través de medios electrónicos por una Administración Pública en el marco de un procedimiento administrativo y en la que no haya intervenido de forma directa un empleado público».
- **Art. 41.2**: debe establecerse previamente el **órgano u órganos competentes** para la definición de especificaciones, programación, mantenimiento, supervisión y control de calidad y, en su caso, auditoría del sistema de información y de su código fuente; y ha de indicarse el **órgano responsable a efectos de impugnación**.
- **Art. 42**: la firma de estas actuaciones se realiza mediante **sello electrónico** de Administración Pública, órgano, organismo o entidad, o mediante **código seguro de verificación (CSV)** (desarrollados en los arts. 20 y 21 del RD 203/2021).
- **Art. 13 del RD 203/2021**: en el ámbito estatal, la determinación de una actuación administrativa como automatizada se autoriza por **resolución** del titular del órgano competente por razón de la materia y se **publica en la sede electrónica**; la resolución debe expresar los recursos que procedan contra la actuación, el órgano ante el que interponerlos y el plazo.
- Además, los robots deben tratarse como identidades no humanas: credenciales propias y protegidas, mínimo privilegio y registro de actividad, conforme al ENS (tema 29).

## Plataformas y automatización inteligente (RPA + IA)

Las plataformas RPA corporativas comparten una arquitectura de **componentes** común:

- **Estudio (diseñador)**: entorno *low-code* donde se construyen los flujos, con grabadora de acciones.
- **Orquestador**: consola central que planifica ejecuciones, gestiona colas de trabajo y credenciales, monitoriza los robots y guarda los registros de auditoría.
- **Robots**: agentes de ejecución atendidos (en puestos) o desatendidos (en servidores o escritorios virtuales).
- **Repositorio y analítica**: versionado de los procesos publicados y métricas de ejecución y rendimiento.

Las **plataformas líderes** del mercado (los 4 líderes del **Magic Quadrant de Gartner para RPA, ed. 2025**):

- **UiPath**: la plataforma de referencia y mayor cuota; ecosistema muy completo (Studio, Orchestrator, Document Understanding, agentes).
- **Automation Anywhere**: plataforma nativa en la nube, orientada a la automatización con IA integrada.
- **Microsoft Power Automate**: integrada en la Power Platform y Microsoft 365; ha popularizado el RPA en el puesto de trabajo (licenciamiento incluido en el ecosistema Microsoft).
- **SS&C Blue Prism**: pionera del término RPA (Blue Prism, adquirida por **SS&C en 2022**), fuerte en entornos corporativos regulados y robots desatendidos.
- **Alternativas open source**: Robot Framework y otros proyectos permiten automatizaciones sin coste de licencia, a cambio de más esfuerzo técnico.

La **automatización inteligente** (*Intelligent Process Automation*, IPA) amplía el alcance del RPA con capacidades de IA, superando el límite de «solo reglas y datos estructurados»:

- **OCR/ICR y procesamiento inteligente de documentos (IDP)**: extracción de datos de documentos no estructurados (facturas, instancias, contratos) combinando reconocimiento óptico y modelos de aprendizaje automático.
- **Procesamiento de lenguaje natural (NLP)**: clasificación de correos y solicitudes, extracción de entidades, chatbots y asistentes que derivan trabajo a los robots.
- **Aprendizaje automático**: decisiones basadas en modelos (priorización, detección de anomalías y fraude) dentro del flujo automatizado.
- **Minería de procesos y de tareas (process/task mining)**: descubrir, a partir de los registros de los sistemas y de la actividad del puesto, qué procesos existen realmente y cuáles conviene automatizar.
- **IA generativa y automatización agéntica**: los grandes modelos de lenguaje se integran en las plataformas para generar automatizaciones, resumir y redactar documentos y, en su evolución más reciente, desplegar **agentes** que planifican y ejecutan tareas de principio a fin bajo supervisión (tema 34).
- **Hiperautomatización**: término acuñado por **Gartner** para el enfoque disciplinado que combina RPA, IPA, BPM, *low-code* y minería de procesos con el fin de automatizar rápidamente el máximo posible de procesos de negocio de extremo a extremo.

## Fuentes {.unnumbered .unlisted}

- Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (texto consolidado, última modificación 2 de agosto de 2024), arts. 41 y 42.
- Real Decreto 203/2021, Reglamento de actuación y funcionamiento del sector público por medios electrónicos (texto consolidado, última modificación 2 de abril de 2025), arts. 13, 20 y 21.
- Gartner: *Magic Quadrant for Robotic Process Automation*, edición 2025 (líderes: UiPath, Automation Anywhere, Microsoft y SS&C Blue Prism; tamaño de mercado 2024).
- Documentación oficial de las plataformas citadas (UiPath, Automation Anywhere, Microsoft Power Automate, SS&C Blue Prism), consultada en julio de 2026.
