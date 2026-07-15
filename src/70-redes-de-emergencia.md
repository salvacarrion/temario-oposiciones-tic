# Redes de emergencia

Las redes de emergencia son las redes de comunicaciones móviles que utilizan los servicios de protección ciudadana (policía, bomberos, urgencias sanitarias, protección civil) para coordinar sus operativos. Deben funcionar precisamente cuando las redes comerciales fallan o se saturan, por lo que se diseñan con requisitos propios de disponibilidad, prioridad y seguridad. Este tema cubre el concepto y los requisitos de estas redes, el estándar TETRA que domina su despliegue en Europa y la red COMDES de la Generalitat. Las redes móviles comerciales (4G/5G) se estudian en el tema 71 y la seguridad de las comunicaciones en el 74.

## Redes de emergencia y misión crítica

En la terminología de la UIT estas redes se engloban en el concepto **PPDR (Public Protection and Disaster Relief)**: radiocomunicaciones para la **protección pública** (mantenimiento del orden, protección de vidas y bienes en situaciones cotidianas) y el **socorro en caso de catástrofe** (perturbaciones graves de origen natural o humano). Sus objetivos y requisitos se recogen en el **Informe UIT-R M.2033 (2003)**. Se habla también de comunicaciones de **misión crítica**: aquellas cuyo fallo pone en riesgo vidas humanas o la operación esencial de una organización.

- **Conceptos básicos**:
    - **PMR (Private/Professional Mobile Radio)**: categoría general de redes de radio móviles privadas para **grupos cerrados de usuarios**, independientes de las redes públicas de telefonía. Es el marco en el que se encuadran las redes de emergencia (también las de transporte, industria o grandes eventos).
    - **PMR convencional**: a cada grupo se le asigna un canal fijo; cobertura limitada, ampliable con repetidores.
    - **Trunking (acceso troncalizado)**: técnica en la que los canales forman un conjunto común que el sistema **asigna dinámicamente** a cada comunicación y libera al terminar. Optimiza el uso del espectro y multiplica la capacidad. Existió trunking analógico (estándar **MPT 1327**, hoy obsoleto) y existe trunking digital (TETRA, TETRAPOL, DMR, APCO P25).
    - **Operativa característica**: comunicación semidúplex pulsando para hablar (**PTT, push-to-talk**), organizada en **llamadas de grupo** con establecimiento casi instantáneo.

- **Requisitos de una red de emergencia**:
    - **Tratamiento prioritario del tráfico**: niveles de prioridad y capacidad de desalojar comunicaciones menos urgentes (*preemption*); la llamada de emergencia tiene prioridad máxima.
    - **Alta disponibilidad y resiliencia**: redundancia de equipos y caminos, autonomía energética de las estaciones y restablecimiento rápido del servicio tras un fallo o catástrofe.
    - **Independencia de las redes comerciales**: infraestructura propia que sigue operativa cuando la telefonía móvil se satura o cae.
    - **Seguridad y confidencialidad**: autenticación de terminales y usuarios, cifrado de las comunicaciones, protección frente a escuchas e interferencias.
    - **Cobertura ubicua**: alcance en todo el territorio de responsabilidad, incluidas zonas despobladas sin interés comercial.
    - **Comunicación de grupo y modo directo**: llamadas de grupo entre flotas y comunicación terminal a terminal sin infraestructura cuando la red no está disponible.
    - **Interoperabilidad**: entre cuerpos distintos (policía, bomberos, sanitarios) y con otras redes públicas y privadas.

### Tecnologías de radio empleadas

En Europa las redes PPDR se han construido sobre sistemas de radio troncalizada digital, que sustituyeron a las redes analógicas y al trunking analógico. Las dos tecnologías dominantes son estas:

- **TETRA (Terrestrial Trunked Radio)**: estándar **abierto** del **ETSI** para radio troncalizada digital; el más extendido en Europa para emergencias, transporte e industria. Se desarrolla en el siguiente subtema.
- **TETRAPOL**: tecnología de radio digital **propietaria** (especificación PAS publicada por el foro Tetrapol, origen Matra/Airbus), anterior a TETRA. Acceso **FDMA** con canales de **12,5 kHz**, banda 380-400 MHz, voz digital cifrada y datos de baja velocidad. La usan redes policiales como **SIRDEE** en España o RUBIS (Gendarmería francesa).
- **Otras**: **DMR** (ETSI, orientado a uso comercial) y **APCO P25** (mercado norteamericano de seguridad pública).
- **LTE/5G**: las redes móviles comerciales ofrecen banda ancha pero carecen por sí solas de los atributos de misión crítica (prioridad, resiliencia, cobertura dedicada); se incorporan mediante los estándares de misión crítica del 3GPP y soluciones híbridas (ver más abajo).

### Redes de emergencia en España

- **SIRDEE (Sistema de Radiocomunicaciones Digitales de Emergencia del Estado)**: red nacional de radio troncalizada digital basada en **TETRAPOL**, operada con Telefónica para las **Fuerzas y Cuerpos de Seguridad del Estado** (Policía Nacional y Guardia Civil). En **2024** el Ministerio del Interior inició su **migración a banda ancha LTE** para incorporar imagen y vídeo a las comunicaciones grupales.
- **REMER (Red Radio de Emergencia)**: red complementaria de la **Dirección General de Protección Civil y Emergencias** (Ministerio del Interior), formada por unos **7.000 radioaficionados voluntarios**.
- **RENEM (Red Nacional de Emergencias)**: «sistema de sistemas» coordinado por la **UME (Unidad Militar de Emergencias)**, del Ministerio de Defensa, que integra los sistemas de información y telecomunicaciones de la AGE, las comunidades autónomas y operadores de infraestructuras críticas. Se apoya en redes terrestres (Red SARA, RedIRIS, WAN PG, Internet) y satelitales (**SPAINSAT**, XTAR-EU y redes civiles).
- **COMDES**: la red TETRA de la Generalitat Valenciana (tercer subtema).
- **ES-Alert**: no es una red PPDR, sino el sistema de **alertas a la población** de Protección Civil: envía avisos geolocalizados por **difusión celular** (*cell broadcast*) a todos los móviles presentes en la zona afectada, sobre las redes comerciales y sin registro previo. Implanta el **art. 110** del Código Europeo de Comunicaciones Electrónicas (Directiva (UE) 2018/1972); se probó en toda España en otoño de **2022** y se utilizó masivamente en la **DANA de octubre de 2024**.

### Evolución a la banda ancha de misión crítica

Las redes troncalizadas resuelven la voz crítica pero ofrecen datos de banda estrecha (kbit/s), insuficientes para vídeo, cartografía o telemetría masiva. La evolución del sector combina la fiabilidad de las redes PMR con la capacidad de las redes 4G/5G:

- **Estándares 3GPP de misión crítica (MCX)**: trasladan los servicios PMR a LTE/5G con calidad garantizada: **MCPTT** (*Mission Critical Push-To-Talk*, **Release 13, 2016**), **MCVideo** y **MCData** (**Release 14, 2017**). Incluyen prioridad y *preemption*, llamadas de grupo, modo directo entre terminales (ProSe/*sidelink*) y funcionamiento aislado de estaciones base (IOPS).
- **Espectro**: la CEPT ha armonizado en Europa opciones de espectro para PPDR de banda ancha en las bandas de **700 MHz** y 400 MHz (Decisión ECC/DEC(16)02).
- **Soluciones híbridas**: en la transición conviven TETRA/TETRAPOL para la voz crítica y LTE/5G para los datos de banda ancha, ya sea sobre redes dedicadas o sobre redes comerciales con acuerdos de prioridad (MVNO de misión crítica). Son ejemplos la migración de SIRDEE y los proyectos europeos de itinerancia PPDR (BroadWay/BroadEU.Net).
- **Retos**: mantener la resiliencia y la cobertura de las redes dedicadas, garantizar la interoperabilidad con lo existente y financiar el espectro y el despliegue.

## El estándar TETRA

**TETRA (Terrestrial Trunked Radio)** es el estándar abierto de radio móvil digital troncalizada del **ETSI**, publicado en **1995** (familia **EN 300 392** para voz y datos, EN 300 396 para el modo directo). Es la tecnología de referencia de las redes de emergencia europeas y también se usa en transporte, aeropuertos, industria y grandes eventos.

- **Características técnicas**:
    - **Banda de frecuencias**: en Europa, la banda armonizada **380-400 MHz** se reserva a los servicios de emergencia y seguridad (en España, 380-385/390-395 MHz). El uso de bandas más bajas que la telefonía móvil da **mayor alcance por estación** y abarata la cobertura de grandes territorios.
    - **Acceso al medio**: **TDMA de 4 intervalos** de tiempo por portadora de **25 kHz** (cuatro comunicaciones simultáneas por canal), con modulación π/4-DQPSK.
    - **Voz y datos (V+D)**: voz digital, mensajes de estado, servicio de datos cortos (**SDS**) y datos en modo paquete; **7,2 kbit/s** por intervalo, hasta **28,8 kbit/s** agregando los 4 intervalos.
    - **Llamadas**: individuales (semidúplex o dúplex), de **grupo**, de difusión y de **emergencia** con prioridad máxima; establecimiento de llamada en menos de **300 ms**.
    - **Baja saturación**: red dimensionada y gestionada para mantener capacidad en picos de demanda.
- **Arquitectura**:
    - **SwMI (Switching and Management Infrastructure)**: la infraestructura de conmutación y gestión de la red (el «emplazamiento maestro»: centro de gestión y conmutación).
    - **Estaciones base**: emplazamientos remotos que dan la cobertura radio.
    - **Terminales**: portátiles, móviles vehiculares y fijos, más los puestos de despacho (*dispatchers*) de las salas de control.
- **Interfaces normalizadas** (garantizan la interoperabilidad multifabricante):
    - **AI (Air Interface)**: interfaz radio entre terminales y estaciones base.
    - **DMO**: interfaz radio de modo directo entre terminales.
    - **ISI (Inter-System Interface)**: interconexión entre redes TETRA distintas (de diferentes operadores o fabricantes).
    - **PEI (Peripheral Equipment Interface)**: conexión de equipos periféricos y aplicaciones de datos al terminal.
    - **MMI (Man-Machine Interface)**: interacción del usuario con el terminal.
    - **Otras**: interfaz de estación de línea (puestos de despacho por línea fija), pasarelas hacia otras redes (telefonía, IP) e interfaz de **gestión de red (NMI)**.
- **Modos de operación**:
    - **TMO (Trunked Mode Operation)**: modo troncalizado normal, a través de la infraestructura; transporta voz y datos (V+D).
    - **DMO (Direct Mode Operation)**: comunicación **directa terminal a terminal** sin infraestructura, tipo walkie-talkie; esencial cuando no hay cobertura (interiores, subsuelo, caída de la red). Admite repetidores DMO y pasarelas DMO-TMO.
    - **PDO (Packet Data Optimized)**: variante solo datos definida en el estándar original, sin despliegue comercial relevante.
- **Seguridad**:
    - **Autenticación mutua** entre terminal e infraestructura.
    - **Cifrado de la interfaz aire** con claves estáticas o dinámicas, y **cifrado extremo a extremo** opcional para usuarios de alta seguridad.
    - **Inhabilitación remota** de terminales robados o perdidos (deshabilitación temporal o permanente).
- **TEDS (TETRA Enhanced Data Service)**: la evolución de datos del estándar (TETRA **release 2**, 2005): canales de 25 a 150 kHz y modulaciones de mayor orden (hasta 64-QAM) que elevan la velocidad a **centenares de kbit/s** (hasta ~500 kbit/s). Aun así queda lejos de la banda ancha, lo que empuja las soluciones híbridas con LTE/5G del subtema anterior.

La comparación entre las dos tecnologías troncalizadas europeas es materia habitual de examen:

| | TETRA | TETRAPOL |
| --- | --- | --- |
| Estándar | **Abierto (ETSI, EN 300 392)** | **Propietario** (especificación PAS) |
| Acceso al medio | **TDMA, 4 ranuras por 25 kHz** | **FDMA, canales de 12,5 kHz** |
| Servicios | Voz y datos (SDS, paquete), TEDS | Voz digital y datos de baja velocidad |
| Seguridad | Autenticación, cifrado aire y extremo a extremo | Autenticación, cifrado aire y extremo a extremo |
| Ejemplos | **COMDES**, redes autonómicas, metro y aeropuertos | **SIRDEE**, RUBIS (Francia) |

## La red COMDES

**COMDES (Comunicaciones Móviles Digitales de Emergencias y Seguridad)** es la red corporativa de radio móvil digital de la **Generalitat Valenciana**, basada en el estándar **TETRA**, que da servicio a las organizaciones y flotas de prevención, rescate, emergencias y seguridad que operan en la Comunitat Valenciana. Es un **entorno multimarca**: admite cualquier terminal homologado compatible con TETRA, para voz (fija, portátil y móvil) y datos (sensorización, telemetría).

- **Funcionamiento**:
    - Cada flota opera como una **red privada virtual** dentro de la infraestructura común: organiza sus propios grupos de comunicación con independencia del resto.
    - Existen **grupos comunes** intra e interflotas que articulan la operativa **local, comarcal y autonómica** y la coordinación entre cuerpos distintos.
- **Infraestructura** (datos oficiales, consulta julio 2026):
    - **206 estaciones base**, con cobertura territorial superior al **98 %** y poblacional superior al **99,5 %**.
    - Capacidad para más de **1.534 comunicaciones simultáneas** de voz y datos.
    - Más de **280 radioenlaces** para el transporte del tráfico, con diseño redundante de caminos.
    - **2 estaciones base móviles** con conectividad vía **satélite**, desplegables donde se necesite reforzar o reponer cobertura.
    - Integra más de **17.700 usuarios** de **360 flotas**: urgencias sanitarias, prevención de incendios forestales, el servicio **112CV**, bomberos provinciales y municipales, policía de la Generalitat, policías locales y protección civil de **289 ayuntamientos**.
- **Servicios a las flotas**:
    - Llamadas individuales y de grupo, con configuración **dinámica** de grupos intra e interflotas.
    - **Autenticación de terminales y cifrado** de las comunicaciones.
    - Mensajes de texto (SDS) y **posicionamiento GPS** de los terminales.
    - Comunicaciones de datos con aplicaciones en terminales y servicios centrales.
    - Comunicaciones de voz y datos con redes externas públicas y privadas.
- **Organización**:
    - **Operador de red**: **ISTEC** (Infraestructures i Serveis de Telecomunicacions i Certificació, SAU), la empresa pública de telecomunicaciones de la Generalitat, que asumió la gestión de COMDES por **encargo del Consell** (octubre de 2025 a septiembre de 2027; anteriormente la gestionaba directamente la DGTIC). Le corresponden la planificación, gestión y supervisión técnica, operativa y administrativa de la red.
    - **Usuarios**: las flotas hacen la gestión operativa y usan la red como apoyo a sus servicios; incluyen los servicios de intervención (sanitarios, bomberos, protección civil), los de seguridad (policías) y el **Centro de Coordinación de Emergencias** de la Generalitat, que elabora los protocolos de comunicaciones.
    - **Proveedores externos**: empresas contratadas para el mantenimiento de la infraestructura, el suministro de terminales y las plataformas conectadas (como el 112).

## Fuentes {.unnumbered .unlisted}

- Informe UIT-R M.2033, *Radiocommunication objectives and requirements for public protection and disaster relief* (2003).
- ETSI EN 300 392 (TETRA Voice plus Data) y EN 300 396 (TETRA Direct Mode Operation); TETRA release 2/TEDS (2005).
- 3GPP: especificaciones de misión crítica MCPTT (Release 13, 2016), MCVideo y MCData (Release 14, 2017); CEPT ECC/DEC(16)02 (espectro PPDR de banda ancha).
- Web oficial de la red COMDES (ISTEC, comdes.istecdigital.es; consulta julio 2026) y encargo del Consell a ISTEC (nota de prensa GVA, septiembre 2025).
- Ministerio del Interior: SIRDEE y su migración a banda ancha LTE (2024); DGPCE (REMER, ES-Alert); UME (RENEM).
- Directiva (UE) 2018/1972, Código Europeo de las Comunicaciones Electrónicas, art. 110 (sistemas de alerta a la población).
