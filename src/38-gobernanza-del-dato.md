# Gobernanza del dato

## El gobierno del dato: calidad, linaje, metadatos, CDO

El **gobierno del dato** (*data governance*) es el ejercicio de autoridad, control y toma de decisiones compartida sobre la gestión de los activos de datos, con el fin de convertirlos en un activo estratégico de la organización. Comprende definir políticas y procedimientos para la recopilación, almacenamiento, protección y uso de los datos, asignar responsables e implantar mecanismos de control y supervisión.

- **Gobierno frente a gestión del dato**: el gobierno **decide y controla** (qué puede hacerse con los datos, quién y bajo qué reglas); la gestión del dato **ejecuta** las actividades técnicas y operativas que aplican esas decisiones a lo largo del ciclo de vida del dato.
- **Componentes**: personas, procesos, tecnología y mejora continua.
- **Principios habituales**: los datos deben ser **accesibles y seguros**, **consistentes**, **exactos** y **auditables**, y su gobierno, sostenible y orientado a la mejora continua.

### Conceptos clave

- **Calidad del dato**: grado en que los datos son aptos para el uso previsto. La norma **ISO/IEC 25012** define el modelo de calidad de datos; sus cinco características **inherentes** son **exactitud, completitud, consistencia, credibilidad y actualidad**. La calidad se mide con reglas de validación e indicadores, y se trabaja con el perfilado (*data profiling*) y la limpieza (*data cleansing*) de datos.
- **Linaje del dato** (*data lineage*): traza del ciclo de vida del dato: de dónde procede, qué transformaciones sufre y dónde se consume. Permite auditar un error hasta su origen, evaluar el impacto de los cambios y acreditar el cumplimiento normativo.
- **Metadatos**: «datos sobre los datos». Se distinguen los **de negocio** (significado, definiciones, reglas), los **técnicos** (esquemas, formatos, orígenes) y los **operativos** (registros de ejecución, accesos, uso). Se administran en el **catálogo de datos**: el inventario que permite localizar, entender y reutilizar los activos de datos, e incorpora el glosario de negocio y, habitualmente, el linaje.
- **Datos maestros y de referencia**: los **datos maestros** describen las entidades esenciales del negocio (clientes, productos, empleados) y son de los activos más valiosos y complejos de mantener; la **gestión de datos maestros (MDM)** garantiza una versión única y fiable de cada entidad (*golden record*) en toda la organización. Los **datos de referencia** son conjuntos de valores estandarizados (códigos de países, nomenclátores) que clasifican otros datos.

### El Chief Data Officer (CDO)

- **CDO** (*Chief Data Officer*): directivo responsable de la estrategia y el gobierno del dato. Impulsa la cultura del dato, define políticas y estándares y responde del valor y la calidad de los activos de datos.
- No debe confundirse con el **CIO** (responsable de los sistemas y la tecnología de la información) ni con el **DPO** (delegado de protección de datos, figura legal del RGPD centrada en los datos personales): el CDO se centra en el **valor del dato como activo**.

## El marco DAMA-DMBOK

**DAMA International** (*Data Management Association*) publica el **DMBOK** (*Data Management Body of Knowledge*), el marco de buenas prácticas de gestión de datos más extendido y base de la certificación profesional CDMP. La edición vigente es la **2.ª (2017)**, con una **edición revisada en marzo de 2024**.

La «rueda DAMA» organiza la disciplina en **11 áreas de conocimiento**, con el gobierno del dato en el centro coordinando a las demás:

- **Gobierno de datos**: ejercicio de autoridad, control y toma de decisiones compartida sobre los activos de datos; núcleo que orienta al resto de áreas.
- **Arquitectura de datos**: define y diseña las vistas maestras para satisfacer las necesidades de datos de la organización.
- **Modelado y diseño de datos**: implementa y mantiene las estructuras de datos que cumplen los requerimientos.
- **Almacenamiento y operaciones de datos**: gestiona la infraestructura, las licencias y las copias de seguridad.
- **Seguridad de datos**: autenticación, autorización y auditoría de los accesos.
- **Integración e interoperabilidad de datos**: adquisición, transformación y movimiento de datos entre sistemas.
- **Gestión de documentos y contenido**: acceso e integración de datos estructurados y no estructurados.
- **Datos maestros y de referencia**: consistencia de los valores maestros y de referencia.
- **Data warehousing y business intelligence**: soporte a la decisión y análisis.
- **Gestión de metadatos**: administración de la información que describe los datos.
- **Calidad de datos**: medición, evaluación y aseguramiento de la calidad.

Cada área se documenta en el DMBOK con un diagrama de contexto: definición, objetivos, actividades, entregables, roles y métricas.

Otros marcos de referencia complementarios para el gobierno del dato:

- **COBIT** (ISACA): gobierno de las TI en su conjunto, con objetivos específicos sobre la información.
- **TOGAF** (The Open Group): arquitectura empresarial, que incluye la arquitectura de datos.
- **DGI Data Governance Framework** (Data Governance Institute): marco específico de gobierno del dato.

## Modelos estratégico, operativo y organizativo

El despliegue del gobierno del dato en una organización se articula en tres modelos complementarios. Sus bases:

- **Mapa de entidades de datos** (modelo operativo): qué datos posee la organización.
- **Catálogo de servicios** (modelo operativo): cómo se gestionarán los datos.
- **Roles y responsabilidades** (modelo organizativo): quiénes participan en el gobierno.
- **Estructura organizativa** (modelo organizativo): cómo se organiza internamente.
- **Comités de gobierno** (servicios y tecnología): cómo se toman las decisiones.
- **Arquitectura del dato** (servicios y tecnología): con qué herramientas se gobierna.

### Modelo estratégico

Establece la **estrategia organizacional** sobre la gestión y el uso de los datos y orienta a la organización hacia una **cultura basada en el dato**: identifica las necesidades de datos, define objetivos y metas sobre su uso e implanta los planes y políticas para alcanzarlos. Sus principios: **esponsorizado y alineado** (con el apoyo de la dirección), **sostenible y escalable**, **accesible y seguro**, **ágil y tangible**, y orientado a la **evolución y mejora continua**.

### Modelo operativo

Define los procesos y políticas de gestión para asegurar la **disponibilidad**, la **integridad**, la **usabilidad** y la **seguridad** de los datos, con un marco documentado que mitiga riesgos:

- **Inventario y mapa de datos**: identifica y describe los datos disponibles en la organización.
- **Procesos y políticas**, en una jerarquía documental:
    - **Políticas**: reglas generales para todos los implicados (calidad, privacidad, seguridad, reglas de negocio, gestión de riesgos).
    - **Estándares**: requisitos concretos que desarrollan las políticas.
    - **Procedimientos**: cómo alcanzar los estándares y políticas (tareas, responsables y momentos).
    - **Guías**: instrucciones paso a paso para aplicar los procedimientos.

### Modelo organizativo

Define la estructura que asegura la implantación de la estrategia del dato. Formas posibles:

- **Centralizada**: un único equipo central de gobierno del dato concentra las decisiones y la carga de trabajo.
- **Descentralizada**: basada en comités, sin un responsable único.
- **Híbrida**: combina un equipo central con grupos de trabajo descentralizados en las áreas clave.
- **Federada**: como la híbrida, con capas adicionales de centralización y descentralización (habitual en grandes grupos y organizaciones multinivel).

Elementos comunes:

- **Comités de gobierno**: promueven y aplican la estrategia, los procesos y las políticas; destacan el **comité de gobierno del dato** (*governance board*) y el **consejo de data stewards** (*data steward council*).
- **Roles y responsabilidades**:
    - **Chief Data Officer (CDO)**: máxima responsabilidad ejecutiva sobre el dato.
    - **Data owner** (propietario del dato): responsable de negocio de un conjunto de datos; aprueba los accesos y responde de su calidad.
    - **Data steward** (administrador del dato): responsable operativo del día a día; aplica las políticas y estándares, documenta y vigila la calidad.
    - **Oficina de gobierno del dato**: unidad interna que coordina el programa: define políticas y estándares, cataloga e inventaría los datos, presta apoyo al resto de la organización y supervisa el cumplimiento.
    - Colaboran además el **CIO** y el **DPO** (protección de datos).
- **Cultura del dato**: actitud de la organización ante los datos: decisiones fundamentadas en información, colaboración e intercambio entre departamentos y prácticas éticas y responsables, que consolidan la confianza en el dato como activo.

## El gobierno del dato en el sector público

Las administraciones públicas gestionan volúmenes enormes de datos (tributarios, sanitarios, geográficos, estadísticos) y su gobierno es condición para la administración digital, la transparencia y las políticas públicas basadas en evidencia.

- **Marco europeo**: la estrategia europea de datos impulsa los **espacios comunes europeos de datos** y se apoya en el **Reglamento (UE) 2022/868, de Gobernanza de Datos (DGA)** (reutilización de datos protegidos del sector público, servicios de intermediación y cesión altruista de datos) y el **Reglamento (UE) 2023/2854, de Datos (Data Act)**; se tratan en el tema [37](37-gestion-de-datos-corporativos-y-big-data.md).
- **La Oficina del Dato**: división de la **Secretaría de Estado de Digitalización e Inteligencia Artificial (SEDIA)**, dirigida por el **Chief Data Officer** nacional. Su misión es «dinamizar la compartición, la gestión y el uso de los datos en todos los sectores de la economía y la sociedad»: espacios de datos sectoriales, gobernanza y tecnologías del dato.
- **Especificaciones UNE del dato** (2023, impulsadas por la Oficina del Dato junto a UNE): marco español para implantar y evaluar el gobierno del dato, alineado con las normas ISO:
    - **UNE 0077:2023, gobierno del dato**: marco para evaluar, dirigir y monitorizar el uso del dato (**5 procesos**).
    - **UNE 0078:2023, gestión del dato**: actividades del ciclo de vida del dato (**13 procesos**).
    - **UNE 0079:2023, gestión de la calidad del dato**: planificar, controlar, asegurar y mejorar la calidad (**4 procesos**).
    - **UNE 0080:2023**: guía de evaluación de la **madurez** del gobierno, la gestión y la calidad del dato.
    - **UNE 0081:2023**: evaluación de la **calidad de un conjunto de datos** (basada en ISO/IEC 25012 y 25024), para planes de mejora o certificación.
- **Datos abiertos y reutilización**: la **Ley 37/2007, sobre reutilización de la información del sector público**, modificada por el **Real Decreto-ley 24/2021** que transpone la **Directiva (UE) 2019/1024** de datos abiertos, ordena la apertura de la información pública para su reutilización. Su gestión práctica exige:
    - **Publicación** de los conjuntos de datos en portales de datos abiertos: **datos.gob.es** (Iniciativa Aporta) como punto nacional, federando los catálogos de las administraciones, y **data.europa.eu** en el nivel europeo.
    - **Interoperabilidad de los catálogos** mediante metadatos comunes (vocabulario **DCAT** del W3C y su perfil europeo DCAT-AP).
    - **Seguridad y privacidad**: anonimización y control de accesos cuando hay datos personales.
    - **Calidad**: indicadores técnicos y funcionales sobre los conjuntos publicados.
    - **Ética del dato**: uso responsable, evitando sesgos y usos lesivos, como parte de la cultura del dato pública.

## Fuentes {.unnumbered .unlisted}

- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*, 2.ª ed. revisada, Technics Publications, marzo de 2024 (2.ª ed. original de 2017).
- Especificaciones UNE 0077, 0078, 0079, 0080 y 0081:2023 (gobierno, gestión y calidad del dato; UNE y Oficina del Dato).
- ISO/IEC 25012:2008, *Data quality model*.
- Real Decreto-ley 24/2021, de 2 de noviembre (texto consolidado, última modificación 29 de junio de 2023), que modifica la Ley 37/2007 sobre reutilización de la información del sector público.
- Reglamento (UE) 2022/868, de Gobernanza de Datos (DOUE 3-jun-2022) y Reglamento (UE) 2023/2854, de Datos (DOUE 22-dic-2023).
- Oficina del Dato y datos.gob.es (SEDIA), consultados en julio de 2026.
