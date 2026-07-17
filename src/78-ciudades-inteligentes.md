# Ciudades inteligentes

Las ciudades inteligentes (*smart cities*) aplican las TIC a la gestión urbana para prestar mejores servicios con menos recursos: movilidad, energía, agua, residuos, seguridad o participación ciudadana. Este tema cubre el concepto, la arquitectura y el gobierno de la ciudad inteligente, las plataformas de ciudad (con FIWARE como referencia), los protocolos MQTT y CoAP y los gemelos digitales. El IoT y las redes de sensores que la alimentan se estudian en el tema 77, los SIG y las IDE en los temas 66 y 67, y la inteligencia artificial en el 34.

## Concepto, arquitectura y gobierno

La UIT define la **ciudad sostenible e inteligente** como «una ciudad innovadora que aprovecha las tecnologías de la información y la comunicación (TIC) y otros medios para mejorar la calidad de vida, la eficiencia del funcionamiento y los servicios urbanos y la competitividad, al tiempo que se asegura de que responde a las necesidades de las generaciones presentes y futuras en lo que respecta a los aspectos económicos, sociales, medioambientales y culturales» (**Recomendación UIT-T Y.4900**, 2016). No es un proyecto tecnológico puntual, sino una estrategia transversal de ciudad apoyada en datos.

- **Tecnologías clave**: **IoT** (sensores, actuadores y sus redes: tema 77), **big data y analítica** (procesar y explotar los datos urbanos), **sistemas ciberfísicos** (computación integrada que actúa sobre la ciudad), **computación en la nube y en el borde** y, de forma creciente, la **inteligencia artificial**.
- **Retos**: escalabilidad, integración con sistemas heredados (*legacy*), interoperabilidad entre proveedores (evitar el *vendor lock-in*), gobernanza y financiación sostenida, seguridad y privacidad de los datos ciudadanos y reutilización de las soluciones entre ciudades.
- **Soluciones verticales habituales**: sensorización ambiental, eficiencia energética y alumbrado inteligente, gestión del tráfico y movilidad, gestión de residuos, ciclo integral del agua, aparcamiento inteligente y aplicaciones de participación y promoción del comercio.

La pieza central es la **plataforma de ciudad inteligente**: el sistema que integra los datos de todos los verticales y sistemas municipales y los convierte en servicios. Su arquitectura de referencia está normalizada (**UNE 178104:2017**, «Sistemas integrales de gestión de la ciudad inteligente»; **Recomendación UIT-T Y.4201**, 02/2018, requisitos de alto nivel y marco de referencia de las plataformas de ciudad inteligente; **ISO/IEC 24039:2022**, arquitectura de referencia de la plataforma digital de ciudad; DIN SPEC 91357, *Open Urban Platform*) y suele describirse en **cinco capas**:

- **Capa de adquisición**: captura e integración de datos de los sensores desplegados (semáforos, farolas, riego, aforos), de los sistemas de información municipales y externos, de las aplicaciones ciudadanas y de las redes sociales, preferentemente con protocolos estándar.
- **Capa de conocimiento**: procesamiento y análisis de la información: gestión de datos, minería y aprendizaje automático, evaluación ambiental y socioeconómica, e integración con herramientas de modelización (SIG, BIM, CIM).
- **Capa de interoperabilidad**: interfaces estándar y abiertas para que aplicaciones y sistemas accedan a los datos; **datos abiertos** con metadatos, licencias claras de reutilización y anonimización cuando proceda.
- **Capa de servicios inteligentes**: los servicios e interfaces con la ciudadanía, la administración, los proveedores y los visitantes, incluidos los cuadros de mando y la recepción de peticiones y avisos.
- **Capa de soporte**: seguridad, auditoría, monitorización, registro y administración de la propia plataforma, con visión centralizada.

El **gobierno** de la ciudad inteligente exige un marco organizativo además del tecnológico: liderazgo y oficina técnica municipal, gobernanza del dato en torno a la plataforma, colaboración público-privada y políticas de uso ético y responsable. Hitos preguntables del ecosistema español y europeo:

- **RECI (Red Española de Ciudades Inteligentes, 2012)**: asociación de municipios para intercambiar experiencias y proyectos.
- **Normalización española**: el comité **CTN 178** de UNE (ciudades inteligentes) ha producido la familia de normas **UNE 178xxx** (plataformas, datos abiertos, destinos turísticos inteligentes), referencia internacional.
- **Planes nacionales**: Plan Nacional de Ciudades Inteligentes (2015) y **Plan Nacional de Territorios Inteligentes** (2017), impulsados con Red.es, financiaron las plataformas de muchas ciudades.
- **Destinos turísticos inteligentes (DTI)**: la variante turística del modelo, normalizada en **UNE 178501** (sistema de gestión del DTI) y **UNE 178502** (indicadores), impulsada por **Segittur** y su red de destinos; en la Comunitat Valenciana la lidera **Invat·tur** con la **Red DTI-CV**.
- **Unión Europea**: la misión de Horizonte Europa **«100 ciudades climáticamente neutras e inteligentes para 2030»** (112 ciudades seleccionadas en 2022, siete de ellas españolas, entre ellas València).

## Plataformas de ciudad: FIWARE

**FIWARE** es la plataforma abierta de referencia europea para ciudades inteligentes: un conjunto de componentes de código abierto (*Generic Enablers*) con API estandarizadas para construir soluciones inteligentes. Nació del programa europeo de la Internet del futuro (**FI-PPP, 2011**) y desde **2016** la gobierna la **Fundación FIWARE** (Berlín), con una comunidad global de empresas, ciudades y laboratorios (*iHubs*); las soluciones conformes lucen el sello «*Powered by FIWARE*».

- **Context Broker (Orion/Orion-LD)**: el componente **obligatorio** de toda plataforma FIWARE. Gestiona la **información de contexto** de la ciudad: el estado en tiempo real de sus **entidades** (un autobús, un contenedor, una farola) descritas mediante atributos. Las aplicaciones consultan y actualizan ese contexto y se **suscriben** a cambios (publicación/suscripción), desacoplando productores y consumidores de datos.
- **API NGSI**: la interfaz de gestión de contexto. La versión FIWARE original (**NGSI-v2**) sirvió de base a **NGSI-LD**, estandarizada por el grupo **ETSI ISG CIM** (primera especificación en **2019**), que incorpora *linked data* (JSON-LD): entidades enlazadas, con semántica formal y grafos de información entre organizaciones.
- **Smart Data Models**: modelos de datos comunes y abiertos (aparcamiento, alumbrado, calidad del aire) impulsados por FIWARE con TM Forum y otros socios, para que los datos de distintas ciudades sean interoperables.
- **Ecosistema europeo**: el Context Broker es un ***building block* de la Comisión Europea** (programa CEF/Interoperable Europe) recomendado para publicar datos de contexto en tiempo real, y FIWARE es una de las bases de los espacios de datos y de los gemelos digitales locales.
- **El caso VLCi (València)**: la plataforma **VLCi** del Ayuntamiento de València fue la **primera plataforma de ciudad basada en FIWARE en España** (proyecto impulsado con Red.es desde 2014-2016), conforme a la **UNE 178104:2017**: integra los datos de los servicios municipales y sensores urbanos en un cuadro de mando de ciudad con indicadores.
- **Otras plataformas**: **Sentilo** (Ayuntamiento de Barcelona, código abierto, centrada en sensores) y plataformas comerciales de fabricantes; la tendencia es exigir estándares abiertos (NGSI, UNE 178104) en los pliegos para evitar la dependencia del proveedor.

## Protocolos: MQTT y CoAP

Los dispositivos urbanos son restringidos (poca batería, poca memoria, redes inestables), y HTTP resulta demasiado pesado para ellos. Los dos protocolos de aplicación dominantes en IoT y plataformas de ciudad son MQTT y CoAP.

- **MQTT (Message Queuing Telemetry Transport)**: protocolo de **mensajería ligera por publicación/suscripción**, creado en 1999 (IBM) y estandarizado por **OASIS**: la versión **3.1.1 (2014)** es también la norma **ISO/IEC 20922:2016**, y la vigente es la **5.0 (2019)**.
    - **Broker central**: los clientes no se hablan entre sí; **publican** mensajes en **temas (topics)** jerárquicos (`ciudad/distrito1/farola42/estado`) y el broker los distribuye a los **suscriptores** (admite comodines `+` y `#`).
    - **Calidades de servicio (QoS)**: **0** (a lo sumo una vez), **1** (al menos una vez) y **2** (exactamente una vez).
    - **Otras piezas**: mensajes **retenidos** (el último valor queda disponible para nuevos suscriptores), **testamento (LWT)** que el broker publica si un cliente se desconecta abruptamente, y sesiones persistentes.
    - Funciona sobre **TCP** (puertos **1883** y **8883** con TLS), con cabecera mínima de **2 bytes**; la variante MQTT-SN cubre redes de sensores sin TCP.
- **CoAP (Constrained Application Protocol)**: protocolo **web REST para dispositivos restringidos**, del grupo CoRE del IETF (**RFC 7252, 2014**). Traslada el modelo de HTTP (recursos con URI `coap://` y métodos **GET/POST/PUT/DELETE**) a un formato binario compacto (cabecera de **4 bytes**) sobre **UDP** (puerto **5683**; **5684** con DTLS).
    - **Fiabilidad opcional**: mensajes **confirmables (CON)**, que exigen acuse, y **no confirmables (NON)**.
    - **Observación (RFC 7641)**: un cliente puede «observar» un recurso y recibir notificaciones cuando cambia (efecto suscripción sin broker).
    - Transferencia por **bloques** para cargas grandes, cachés y proxies con pasarela natural a HTTP; extensiones sobre TCP/TLS/WebSockets (RFC 8323).

| | MQTT | CoAP | HTTP |
| --- | --- | --- | --- |
| Paradigma | **Publicación/suscripción** (broker) | **REST** petición/respuesta (+observación) | REST petición/respuesta |
| Transporte | **TCP** (1883/8883) | **UDP** (5683/5684) | TCP (80/443) |
| Cabecera mínima | **2 bytes** | **4 bytes** | Cientos de bytes (texto) |
| Fiabilidad | QoS 0/1/2 | Mensajes CON/NON | La de TCP |
| Seguridad | TLS | **DTLS** | TLS |
| Uso típico | Telemetría hacia plataformas | Consulta/actuación sobre dispositivos | Integración de sistemas y API |

## Gemelos digitales

Un **gemelo digital** (*digital twin*) es una réplica virtual de una entidad física (un edificio, una red de agua, una ciudad entera) **sincronizada con datos reales**, que permite monitorizar, simular escenarios, predecir comportamientos y optimizar decisiones antes de actuar sobre el mundo físico. El concepto lo formuló **Michael Grieves (2002)** en el ámbito de la gestión del ciclo de vida del producto y lo popularizó la **NASA (2010)**; su terminología está normalizada en **ISO/IEC 30173:2023**.

- **Componentes**: la **entidad física** instrumentada con sensores, el **modelo virtual** (geométrico, físico o de comportamiento) y el **flujo de datos bidireccional** que los sincroniza: las medidas actualizan el modelo y las decisiones simuladas vuelven como actuaciones. Esa sincronización continua lo distingue de una simulación estática o una maqueta 3D.
- **Niveles de madurez**: **descriptivo** (espejo del estado actual), **predictivo** (anticipa qué va a pasar: averías, congestión) y **prescriptivo** (recomienda o ejecuta la mejor acción).
- **Gemelos digitales urbanos**: integran el modelo 3D de la ciudad (BIM de los edificios, CIM urbano, cartografía de los SIG e IDE: temas 66 y 67) con los datos en tiempo real de la plataforma de ciudad. Usos: planificar movilidad y urbanismo, simular inundaciones y olas de calor, evaluar el impacto de peatonalizaciones o nuevas líneas de transporte, y ensayar políticas antes de implantarlas.
- **Iniciativas**: la Comisión Europea impulsa los **gemelos digitales locales** (*Local Digital Twins*, programa Europa Digital) sobre estándares abiertos (FIWARE/NGSI-LD entre ellos), y a escala planetaria **Destination Earth (DestinE)**, el gemelo digital de la Tierra para el cambio climático (primera versión en 2024). Ciudades pioneras: Helsinki, Róterdam o Zaragoza.
- **Retos**: coste y calidad del dato (un gemelo desactualizado engaña), interoperabilidad de modelos, ciberseguridad (concentra información crítica de la ciudad) y gobernanza de su uso.

## Fuentes {.unnumbered .unlisted}

- Recomendaciones UIT-T Y.4900/L.1600 (2016, definición e indicadores de ciudad sostenible e inteligente) y UIT-T Y.4201 (febrero de 2018, marco de referencia de plataformas de ciudad inteligente).
- UNE 178104:2017, «Sistemas integrales de gestión de la ciudad inteligente»; UNE 178501 y 178502 (destinos turísticos inteligentes, Segittur/Invat·tur); ISO/IEC 24039:2022 (arquitectura de referencia de plataformas digitales de ciudad, verificada online); ISO/IEC 30173:2023 (gemelos digitales, conceptos y terminología).
- FIWARE Foundation: catálogo de componentes, Orion/Orion-LD y Smart Data Models; ETSI ISG CIM: especificación NGSI-LD (desde 2019); plataforma VLCi del Ayuntamiento de València (smartcity.valencia.es); todo consultado online en julio de 2026.
- MQTT 3.1.1 (OASIS, 2014; ISO/IEC 20922:2016) y MQTT 5.0 (OASIS, marzo de 2019); RFC 7252 (CoAP, junio de 2014), RFC 7641 (observación) y RFC 8323 (CoAP sobre TCP).
- Misión de la UE «100 ciudades climáticamente neutras e inteligentes para 2030» (Horizonte Europa) y programa Destination Earth (Comisión Europea), consultados online en julio de 2026.
