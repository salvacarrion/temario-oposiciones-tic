# Análisis y gestión de riesgos

El análisis de riesgos determina qué puede pasarle a los activos de una organización y qué daño supondría; la gestión de riesgos decide qué hacer al respecto y lo mantiene bajo revisión continua. En el sector público esta disciplina es obligatoria (el ENS la exige como principio básico y como medida operacional) y su metodología de referencia es **MAGERIT**. La gestión de los riesgos de un proyecto (área de Riesgos del PMBOK) se estudia en el tema [19](19-direccion-y-gestion-de-proyectos.md); la gestión del ciberincidente, que es el riesgo ya materializado, en el tema [31](31-gestion-de-ciberincidentes.md).

## La gestión de riesgos: conceptos

La terminología básica del análisis de riesgos encadena unos conceptos con otros: las amenazas explotan vulnerabilidades y degradan activos, causando un impacto; el riesgo pondera ese impacto con su probabilidad.

- **Activo**: «componente o funcionalidad de un sistema de información susceptible de ser atacado deliberada o accidentalmente con consecuencias para la organización» (UNE 71504:2008). Los activos esenciales son **la información que se maneja y los servicios que se prestan**; el resto de componentes están subordinados a ellos.
- **Amenaza**: «causa potencial de un incidente que puede causar daños a un sistema de información o a una organización» (UNE 71504:2008).
- **Vulnerabilidad**: debilidad de un activo o de sus medidas de protección que facilita el éxito de una amenaza. En MAGERIT equivale a las ausencias o ineficacias de las salvaguardas pertinentes (por eso se habla también de «insuficiencias»).
- **Impacto**: medida del daño sobre el activo derivado de la materialización de una amenaza.
- **Probabilidad**: expectativa de materialización de la amenaza; se modela con escalas cualitativas (de muy baja a muy alta) o como **tasa anual de ocurrencia**.
- **Riesgo**: medida del daño probable sobre un sistema; crece con el impacto y con la probabilidad.

Según el momento del cálculo se distingue:

- **Riesgo potencial (o inherente)**: el que existiría si no hubiera salvaguarda alguna desplegada.
- **Riesgo residual**: el que permanece tras considerar la eficacia de las salvaguardas desplegadas.
- **Riesgo de terceros**: el introducido por componentes y servicios de proveedores externos con los que interactúa el sistema (cadena de suministro, externalización).

Las opciones clásicas de tratamiento son cuatro: **evitar** la actividad que origina el riesgo, **reducirlo** con controles, **transferirlo o compartirlo** con un tercero (seguros, externalización) y **aceptarlo** formalmente cuando es tolerable. MAGERIT las concreta en eliminación, mitigación, compartición y financiación (más abajo).

El marco normativo y los estándares aplicables:

- **Real Decreto 311/2022 (ENS)**. **Texto consolidado a 6 de noviembre de 2024.**
    - **Art. 7. Gestión de la seguridad basada en los riesgos**: el análisis y la gestión de los riesgos es «parte esencial del proceso de seguridad, debiendo constituir una actividad continua y permanentemente actualizada»; la gestión de riesgos permitirá minimizar los riesgos «a niveles aceptables» mediante medidas proporcionadas a la naturaleza de la información, los servicios y los riesgos.
    - **Medida op.pl.1 Análisis de riesgos** (marco operacional, planificación): en categoría **BÁSICA** basta un análisis **informal** en lenguaje natural; la categoría **MEDIA** añade el refuerzo R1 (análisis **semiformal**, con tablas, catálogo básico de amenazas y semántica definida); la categoría **ALTA** exige además un análisis **formal**, con fundamento matemático reconocido internacionalmente. En todos los casos hay que identificar y valorar los activos más valiosos, las amenazas, las salvaguardas y el riesgo residual.
- **ISO 31000:2018**: principios y directrices para gestionar cualquier tipo de riesgo (8 principios, marco de trabajo y proceso). Sustituyó a la edición de 2009, con cuya terminología se alineó MAGERIT v3.
- **ISO/IEC 27005:2022**: guía específica de gestión de riesgos de seguridad de la información, de apoyo a un SGSI ISO/IEC 27001.

## MAGERIT v3: el método

**MAGERIT** (Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información) es la metodología de referencia de las administraciones públicas españolas. La primera versión es de **1997**, la segunda de 2005 y la vigente es la **versión 3, de octubre de 2012**, elaborada por el **Ministerio de Hacienda y Administraciones Públicas** con la participación del **Centro Criptológico Nacional (CCN)** y publicada en el PAe. Siguiendo la terminología de ISO 31000, MAGERIT implementa el proceso de gestión de riesgos dentro de un marco de trabajo para que los órganos de gobierno tomen decisiones teniendo en cuenta los riesgos del uso de las TIC; es el camino habitual para cumplir la medida op.pl.1 del ENS, y la herramienta **PILAR** del CCN la automatiza (tema [28](28-ciberseguridad.md)).

Sus objetivos son tres directos y uno indirecto:

- **Concienciar** a los responsables de las organizaciones de la existencia de riesgos y de la necesidad de gestionarlos.
- Ofrecer un **método sistemático** para analizar los riesgos derivados del uso de las TIC.
- Ayudar a descubrir y planificar el **tratamiento** oportuno para mantener los riesgos bajo control.
- (Indirecto) **Preparar a la organización** para procesos de evaluación, auditoría, certificación o acreditación.

Se publica en **tres libros**: el **Libro I (Método)**, que desarrolla el análisis, la gestión, los proyectos de análisis de riesgos y el plan de seguridad; el **Libro II (Catálogo de elementos)**, con los tipos de activos, dimensiones, criterios de valoración, amenazas y salvaguardas (siguiente apartado); y el **Libro III (Guía de técnicas)**, con las técnicas de trabajo.

### El análisis de riesgos paso a paso

El análisis de riesgos sigue **cinco pasos**: determinar los activos y su valor, determinar las amenazas, determinar las salvaguardas y su eficacia, estimar el impacto y estimar el riesgo. Entre los pasos 2 y 3 se calculan el impacto y el riesgo potenciales (los teóricos, sin salvaguardas).

- **Paso 1. Activos**: se identifican, se establecen sus **dependencias** y se valoran. Los activos forman árboles de dependencias: un activo «superior» depende de un «inferior» cuando la materialización de una amenaza en el inferior perjudica al superior (la información y los servicios, arriba; equipos, comunicaciones, instalaciones y personal, abajo). Las dependencias propagan el daño de abajo hacia arriba, y el valor de arriba hacia abajo: el valor puede ser **propio** o **acumulado** (el de los activos que se apoyan en él). Se valora el coste que supondría recuperarse de la destrucción del activo (reposición, mano de obra, lucro cesante, sanciones, daños a personas), de forma **cualitativa** (escala de niveles, en órdenes de magnitud) o **cuantitativa** (numérica, idealmente económica). La interrupción de la disponibilidad se valora por escalones temporales (no es lo mismo una parada de una hora que de un mes).
- **Dimensiones de valoración**: en qué facetas es valioso el activo. MAGERIT usa **cinco**: **disponibilidad [D]**, **integridad [I]**, **confidencialidad [C]**, **autenticidad [A]** y **trazabilidad [T]** (las mismas del ENS).
- **Paso 2. Amenazas**: para cada activo se identifican las amenazas posibles y se valoran en dos sentidos: **degradación** (cuán perjudicado resultaría el valor del activo, como fracción de su valor) y **probabilidad** (escala de muy baja a muy alta, o tasa anual de ocurrencia).
- **Impacto potencial**: daño derivado de la materialización de la amenaza, en función del valor y la degradación. El **impacto acumulado** se calcula sobre un activo con su valor acumulado (el propio más el de los activos que dependen de él) y las amenazas a que está expuesto: sirve para decidir las salvaguardas de los medios de trabajo. El **impacto repercutido** se calcula con el valor propio del activo y las amenazas de los activos de los que depende: es la presentación gerencial, que muestra las consecuencias de las incidencias técnicas sobre la misión del sistema.
- **Riesgo potencial**: impacto ponderado con la probabilidad de ocurrencia (con las mismas variantes acumulado/repercutido). En el plano impacto-probabilidad se distinguen **cuatro zonas de riesgo**: **zona 1** (riesgos muy probables y de muy alto impacto), **zona 2** (franja intermedia, desde improbables de impacto medio hasta muy probables de impacto bajo), **zona 3** (improbables y de bajo impacto) y **zona 4** (improbables pero de muy alto impacto).
- **Paso 3. Salvaguardas**: procedimientos o mecanismos tecnológicos que reducen el riesgo. Se seleccionan según el tipo de activo, la dimensión a proteger y la amenaza; las que se descartan se justifican como «no aplica» o «no se justifica» (desproporcionadas), y el resultado es la **declaración de aplicabilidad**. Su eficacia se gradúa del 0 % al 100 % combinando la idoneidad técnica con la madurez de su operación (escala **L0 inexistente a L5 optimizado**).
- **Pasos 4 y 5. Impacto y riesgo residual**: se repiten los cálculos incorporando la eficacia de las salvaguardas (menor degradación y menor probabilidad). El sistema pasa de los valores potenciales a los **residuales**.

Por su efecto, las salvaguardas se clasifican así:

| Efecto | Tipos |
| --- | --- |
| Reducen la probabilidad (preventivas) | [PR] preventivas · [DR] disuasorias · [EL] eliminatorias |
| Acotan la degradación | [IM] minimizadoras · [CR] correctivas · [RC] recuperativas |
| Consolidan el efecto de las demás | [MN] de monitorización · [DC] de detección · [AW] de concienciación · [AD] administrativas |

### Las tareas del método y sus informes

El Libro I formaliza el análisis en **cuatro tareas (MAR)**, cada una con sus informes normalizados:

| Tarea | Contenido | Informe resultante |
| --- | --- | --- |
| **MAR.1** Caracterización de los activos | Identificación, dependencias y valoración | **Modelo de valor** |
| **MAR.2** Caracterización de las amenazas | Identificación y valoración (probabilidad y degradación) | **Mapa de riesgos** |
| **MAR.3** Caracterización de las salvaguardas | Identificación de las pertinentes y valoración de su eficacia | **Declaración de aplicabilidad**, evaluación de salvaguardas e insuficiencias |
| **MAR.4** Estimación del estado de riesgo | Cálculo de impacto y riesgo (potencial y residual) | **Estado de riesgo** e **informe de insuficiencias** |

### La gestión del riesgo: evaluación, aceptación y tratamiento

Con el análisis hecho, la gestión interpreta los valores residuales y decide. La **aceptación del riesgo** corresponde a la Dirección y no es una decisión técnica: cualquier nivel de impacto y riesgo es aceptable si la Dirección lo conoce y lo **acepta formalmente**. Para lo no aceptado, MAGERIT contempla cuatro opciones de tratamiento:

- **Eliminación**: suprimir la fuente del riesgo (prescindir de componentes no esenciales, reordenar la arquitectura del sistema). Exige repetir el análisis sobre el sistema modificado.
- **Mitigación**: reducir la degradación o la probabilidad ampliando o mejorando las salvaguardas (subir su nivel de madurez).
- **Compartición**: la clásica «transferencia»; cualitativa mediante externalización de componentes, o cuantitativa mediante la contratación de seguros.
- **Financiación**: reservar fondos de contingencia para responder de las consecuencias si el riesgo aceptado se materializa.

La decisión se orienta por las zonas de riesgo: los de la **zona 1** hay que sacarlos de ahí (reducir); en la **zona 2** caben varias opciones según coste y beneficio; los de la **zona 3** pueden dejarse como están; y los de la **zona 4**, improbables pero de impacto muy alto, piden medidas de **reacción y recuperación** más que preventivas.

### Proyectos de análisis de riesgos y plan de seguridad

El Libro I añade dos guías de ejecución:

- **Proyecto de análisis de riesgos (PAR)**: en tres actividades: **PAR.1** actividades preliminares (estudio de oportunidad, alcance, planificación y lanzamiento), **PAR.2** elaboración del análisis y **PAR.3** comunicación de resultados.
- **Plan de seguridad (PS)**: convierte las decisiones de tratamiento en proyectos: **PS.1** identificación de proyectos de seguridad, **PS.2** planificación y **PS.3** ejecución del plan.

## Catálogo de elementos

El **Libro II** ofrece catálogos estándar con un doble objetivo: facilitar el trabajo (ítems de partida en cada paso del análisis) y **homogeneizar los resultados**, de modo que análisis hechos por equipos distintos sean comparables e integrables.

- **Tipos de activos**: los **activos esenciales** ([info] información, con atención a los datos personales y clasificados, y [service] servicio) y, subordinados a ellos: **[D]** datos/información, **[K]** claves criptográficas, **[S]** servicios, **[SW]** software o aplicaciones, **[HW]** equipamiento informático, **[COM]** redes de comunicaciones, **[Media]** soportes de información, **[AUX]** equipamiento auxiliar, **[L]** instalaciones y **[P]** personal.
- **Dimensiones de valoración**: las cinco citadas (D, I, C, A, T), cada una con la pregunta que la valora (¿qué perjuicio causaría no poder usarlo?, ¿que estuviera dañado?, ¿que lo conociera quien no debe?, ¿no saber quién ha hecho qué?, ¿no poder rastrear el uso o el acceso?).
- **Criterios de valoración**: una **escala común de 0 a 10, logarítmica**, para todas las dimensiones: **10** extremo (daño extremadamente grave), **9** muy alto, **6-8** alto, **3-5** medio, **1-2** bajo y **0** despreciable.
- **Catálogo de amenazas**, en cuatro grupos:

| Grupo | Ejemplos |
| --- | --- |
| **[N] Desastres naturales** | [N.1] fuego, [N.2] daños por agua |
| **[I] De origen industrial** | [I.5] avería física o lógica, [I.6] corte del suministro eléctrico, [I.8] fallo de servicios de comunicaciones |
| **[E] Errores y fallos no intencionados** | [E.1] errores de los usuarios, [E.2] errores del administrador, [E.15] alteración accidental de la información, [E.20] vulnerabilidades de los programas |
| **[A] Ataques intencionados** | [A.5] suplantación de identidad, [A.8] difusión de software dañino, [A.11] acceso no autorizado, [A.24] denegación de servicio, [A.30] ingeniería social |

- **Catálogo de salvaguardas**: relación de protecciones por objeto protegido: protecciones generales, de los datos, de las claves, de los servicios, de las aplicaciones, de los equipos, de las comunicaciones, de los puntos de interconexión, de los soportes, de los elementos auxiliares, seguridad física de las instalaciones, salvaguardas del personal, de tipo organizativo, continuidad de operaciones, externalización y adquisición y desarrollo.

El **Libro III (Guía de técnicas)** completa el método con técnicas específicas (análisis mediante tablas, análisis algorítmico, **árboles de ataque**) y generales (técnicas gráficas, sesiones de trabajo como entrevistas y reuniones, y la **valoración Delphi**).

## Supuesto práctico: análisis de riesgos con MAGERIT

Un organismo pone en producción una aplicación web de tramitación de expedientes con datos personales. Se resume un análisis semiformal (categoría MEDIA del ENS, op.pl.1 + R1) siguiendo los pasos del método.

**Paso 1: activos y valoración**. Se identifican los activos, sus dependencias (los esenciales arriba) y su valor por dimensiones (escala 0-10):

| Activo | Tipo | Valor | Dimensiones relevantes |
| --- | --- | --- | --- |
| Expedientes (datos personales) | [info] esencial | Propio | C:8 · I:7 · T:6 |
| Servicio de tramitación | [service] esencial | Propio | D:7 · A:6 |
| Aplicación web | [SW] | Acumulado | Hereda de los esenciales |
| Servidor de aplicaciones | [HW] | Acumulado | Hereda de los esenciales |
| Red corporativa | [COM] | Acumulado | Hereda de los esenciales |

**Paso 2: amenazas, impacto y riesgo potencial**. Para cada pareja amenaza-activo se estiman probabilidad y degradación, y de ahí el impacto y el riesgo potenciales con su zona:

| Amenaza | Activo | Dimensión | Prob. | Degradación | Riesgo potencial | Zona |
| --- | --- | --- | --- | --- | --- | --- |
| [A.8] Software dañino (ransomware) | [SW]/[HW] | D, I, C | Media | Muy alta | Alto | 1 |
| [A.11] Acceso no autorizado | [info] | C | Baja | Alta | Medio | 4 |
| [E.15] Alteración accidental de la información | [info] | I | Alta | Baja | Medio | 2 |
| [I.8] Fallo de comunicaciones | [COM] | D | Media | Alta | Medio | 2 |

**Paso 3: salvaguardas**. La declaración de aplicabilidad selecciona, entre otras:

| Salvaguarda | Tipo | Efecto |
| --- | --- | --- |
| Antimalware/EDR en servidores y puestos | [PR]/[DC] | Reduce probabilidad y detecta [A.8] |
| Copias de seguridad con restauración probada | [RC] | Acota la degradación en D e I |
| Control de acceso, mínimo privilegio y doble factor | [PR] | Reduce probabilidad de [A.11] |
| Cifrado de la información almacenada | [EL] | Elimina la divulgación útil de datos |
| Validación de datos en la aplicación | [PR] | Reduce probabilidad de [E.15] |
| Línea de comunicaciones alternativa | [CR] | Acota la degradación de [I.8] |

**Pasos 4 y 5: impacto y riesgo residual, y tratamiento**. Con las salvaguardas al nivel de madurez actual (L3), el riesgo de ransomware baja a medio (zona 2) y el resto a bajo. La Dirección **acepta formalmente** los riesgos residuales; las carencias detectadas (por ejemplo, falta de segmentación de la red) se recogen en el **informe de insuficiencias** y originan proyectos del **plan de seguridad**. El análisis se revisará al menos anualmente o cuando cambie el sistema. Si pese a todo una amenaza se materializa, se activa la gestión de ciberincidentes (tema [31](31-gestion-de-ciberincidentes.md)).

## Fuentes {.unnumbered .unlisted}

- MAGERIT versión 3.0, Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información: Libro I (Método), Libro II (Catálogo de Elementos) y Libro III (Guía de Técnicas). Ministerio de Hacienda y Administraciones Públicas, octubre de 2012 (NIPO 630-12-171-8). Versión vigente, sin sucesor a julio de 2026 (verificado en el PAe y el CCN).
- Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024), arts. 7 y 8 y Anexo II, medida op.pl.1.
- UNE 71504:2008 (terminología), ISO 31000:2018 e ISO/IEC 27005:2022, citadas por edición.
