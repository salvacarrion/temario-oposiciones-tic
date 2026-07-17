# Internet de las cosas y redes de sensores

El Internet de las cosas (IoT) conecta objetos físicos cotidianos (contadores, vehículos, semáforos, electrodomésticos, maquinaria) a internet para recopilar datos y actuar sobre el entorno. Este tema cubre el concepto y la arquitectura del IoT, sus redes de comunicación de corto alcance (BLE, NFC, RFID) y de largo alcance (LPWAN), y las redes de sensores con la inteligencia artificial en el borde. Las redes Wi-Fi y móviles se estudian en el tema 76, los protocolos MQTT y CoAP y las plataformas de ciudad en el 74 y la inteligencia artificial en el 34.

## IoT: concepto y arquitectura

La UIT define el **Internet de las cosas (IoT)** como una «infraestructura mundial para la sociedad de la información que propicia la prestación de servicios avanzados mediante la interconexión de objetos (físicos y virtuales) gracias a la interoperabilidad de tecnologías de la información y la comunicación presentes y futuras» (**Recomendación UIT-T Y.2060**, de 2012, renumerada Y.4000). La idea central: dotar a los objetos de identidad, conectividad y capacidad de medir y actuar, de forma que puedan cooperar con mínima intervención humana.

- **Componentes de una solución IoT**:
    - **Objetos conectados**: dispositivos con **sensores** (miden el entorno) y **actuadores** (actúan sobre él), más capacidad de proceso y comunicación.
    - **Redes de comunicación**: de corto alcance o de área extensa (los dos subtemas siguientes).
    - **Protocolos**: de red y de aplicación, adaptados a dispositivos restringidos.
    - **Plataforma IoT**: recibe, almacena, procesa y expone los datos; gestiona los dispositivos (aprovisionamiento, actualizaciones, seguridad).
    - **Aplicaciones**: cuadros de mando, analítica y servicios sobre los datos.
- **Modelos de comunicación** (RFC 7452, de la Internet Architecture Board):
    - **Dispositivo a dispositivo**: comunicación directa entre objetos (p. ej. domótica local).
    - **Dispositivo a nube**: el objeto se conecta directamente a la plataforma.
    - **Dispositivo a pasarela (gateway)**: un intermediario traduce protocolos y agrega el tráfico de dispositivos sin IP.
    - **Compartición en el back-end**: los datos se exportan y combinan entre plataformas de terceros.
- **Arquitectura en capas**: el modelo de referencia clásico tiene tres capas, ampliables con capas intermedias de procesamiento:
    - **Capa de percepción**: sensores, actuadores y nodos que capturan los datos.
    - **Capa de red**: transporte de los datos (pasarelas, redes de acceso, internet).
    - **Capa de aplicación**: plataformas y servicios que explotan los datos.
    - Cuando los objetos no hablan IP, una **pasarela** hace de frontera (arquitectura de tres niveles: dispositivo, pasarela, nube); los objetos con pila IP (p. ej. 6LoWPAN) pueden conectarse de extremo a extremo.
- **Edge y fog computing**: para reducir latencia, tráfico y dependencia de la nube, el procesamiento se acerca al origen de los datos: en el propio dispositivo o pasarela (**edge computing**) o en una capa intermedia distribuida entre el dispositivo y la nube (**fog computing**, arquitectura de referencia OpenFog adoptada como **IEEE 1934-2018**). Es la base del MEC en redes 5G (tema 76).
- **Protocolos de aplicación IoT** (panorama; MQTT y CoAP se desarrollan en el tema 78):
    - **MQTT**: mensajería ligera de publicación/suscripción con broker central; el más usado en IoT.
    - **CoAP**: web REST para dispositivos restringidos, sobre UDP.
    - **AMQP**: colas de mensajes empresariales; **DDS**: distribución de datos en tiempo real (OMG); **XMPP**: mensajería extensible.
    - **oneM2M**: estándar global de plataforma de servicios **M2M** (*machine-to-machine*), el paradigma de comunicación entre máquinas del que el IoT es heredero.
- **Retos**: **seguridad y privacidad** (dispositivos poco protegidos, superficies de ataque masivas; tema 79), **interoperabilidad** entre fabricantes y estándares, escalabilidad de las plataformas, consumo energético y coste del despliegue.

## Redes de corto alcance: BLE, NFC y RFID

Las tecnologías de área personal (WPAN) resuelven la conexión de objetos a pocos metros con consumos mínimos. Las tres familias más preguntadas son RFID, NFC y Bluetooth LE.

- **RFID (identificación por radiofrecuencia)**: identifica objetos mediante **etiquetas (tags)** que responden por radio a un **lector**. Es la base de la trazabilidad logística y el control de accesos.
    - **Etiquetas pasivas**: sin batería, se alimentan de la energía del lector; baratas y de corto alcance.
    - **Etiquetas activas**: con batería y transmisor propio; alcance de decenas o centenares de metros.
    - **Etiquetas semipasivas**: batería solo para el circuito (p. ej. registro de temperatura); responden como las pasivas.
    - **Bandas**: **LF** (125-134 kHz, centímetros: identificación animal), **HF** (**13,56 MHz**, hasta ~1 m: tarjetas sin contacto, ISO/IEC 14443 y 15693) y **UHF** (860-960 MHz, varios metros: logística y cadena de suministro, **EPC Gen2/ISO/IEC 18000-63**).
- **NFC (Near Field Communication)**: evolución de la RFID HF para el móvil: opera a **13,56 MHz** con alcance menor de **10 cm** y hasta **424 kbps** (ISO/IEC 14443 e **ISO/IEC 18092**; especificaciones del NFC Forum). La proximidad forzada actúa como factor de seguridad. Tres **modos de operación**:
    - **Lectura/escritura**: el móvil lee o graba etiquetas NFC (carteles inteligentes).
    - **Emulación de tarjeta**: el móvil se comporta como una tarjeta sin contacto (**pagos móviles**, transporte, control de accesos).
    - **Peer-to-peer**: intercambio directo entre dos dispositivos.
- **Bluetooth y BLE**: estándar de WPAN del Bluetooth SIG en la banda de **2,4 GHz**. Convive el Bluetooth «clásico» (BR/EDR, hasta 3 Mbps, audio) con **BLE (Bluetooth Low Energy)**, introducido en **Bluetooth 4.0 (2010)** para IoT: consumo mínimo, conexiones breves, datos organizados en perfiles **GATT**.
    - **Beacons**: balizas BLE que difunden un identificador (iBeacon, Eddystone) para localización y proximidad en interiores.
    - **Bluetooth Mesh** (2017): topología de malla para domótica e iluminación a gran escala.
    - **Evolución**: **Bluetooth 5** (2016) duplicó la velocidad (2 Mbps) y multiplicó el alcance; 5.1 añadió localización angular (AoA/AoD); **Bluetooth 6.0 (septiembre de 2024)** incorpora ***channel sounding***, medición segura de distancia con precisión centimétrica entre dispositivos (llaves digitales, localización de objetos), y 6.1 (mayo de 2025) mejora la privacidad de las direcciones aleatorias.
- **Otras tecnologías de corto alcance**:

| Tecnología | Base | Banda | Rasgo distintivo |
| --- | --- | --- | --- |
| **ZigBee** | IEEE **802.15.4** | 2,4 GHz (y 868 MHz) | Malla de bajo consumo, **250 kbps**; domótica e industrial |
| **Z-Wave** | Propietaria (UIT-T G.9959) | 868 MHz | Malla domótica, sin interferencia con Wi-Fi |
| **Thread** | 802.15.4 + 6LoWPAN | 2,4 GHz | Malla **IP (IPv6)** de bajo consumo |
| **Matter** | CSA (v1.0, **2022**) | Sobre Thread/Wi-Fi/Ethernet | Capa de aplicación **unificada** del hogar inteligente |
| **6LoWPAN** | IETF (RFC 4944/6282) | Sobre 802.15.4 | Compresión de **IPv6** para dispositivos restringidos |
| **UWB** | IEEE 802.15.4z | Banda ultraancha | **Localización de precisión** (centímetros) |

## Redes de largo alcance (LPWAN)

Las **LPWAN (Low Power Wide Area Networks)** conectan dispositivos a kilómetros de distancia con baterías que duran años, a cambio de velocidades muy bajas y mensajes pequeños y esporádicos (contadores, sensores urbanos y agrícolas, alarmas). Se dividen en dos familias: sobre espectro **no licenciado** (LoRaWAN, Sigfox) y sobre espectro **licenciado** celular (NB-IoT, LTE-M).

- **LoRaWAN**: especificación **abierta** de la **LoRa Alliance** sobre la capa física LoRa (de Semtech), con modulación de espectro ensanchado **CSS** (*chirp spread spectrum*), muy robusta frente a interferencias. Opera en bandas ISM (**868 MHz** en Europa), con topología en **estrella de estrellas** (los gateways reenvían a un servidor de red), velocidad adaptativa de **0,3 a 50 kbps**, cifrado AES-128 y tres **clases de dispositivo**: **A** (mínimo consumo, escucha solo tras transmitir), **B** (ventanas programadas por balizas) y **C** (escucha continua). Normalizada también como **Recomendación UIT-T Y.4480 (2021)**. Permite montar redes privadas propias (campus, regadíos, ciudades).
- **Sigfox**: tecnología **propietaria** de red «0G» global, en **banda ultraestrecha (UNB**, canales de 100 Hz) sobre espectro no licenciado: ~**600 bps**, hasta **140 mensajes al día** de **12 bytes** de subida (y muy pocos de bajada). Máxima sencillez y autonomía, mínima flexibilidad. Tras la quiebra de Sigfox S.A. (enero de 2022), la tecnología y la red las **opera UnaBiz** (Singapur), con dificultades financieras recurrentes (nueva reorganización judicial de la red francesa en 2025).
- **NB-IoT (Narrowband IoT)**: estándar **3GPP (Release 13, 2016)** sobre espectro **licenciado** de operador: portadora de **180 kHz** desplegable dentro de una banda LTE, decenas de kbps y una ganancia de cobertura de **+20 dB** que alcanza interiores profundos (sótanos, arquetas de contadores). Ahorro con los modos **PSM** y **eDRX**. Sin movilidad plena ni voz: pensado para objetos estáticos.
- **LTE-M (eMTC)**: estándar 3GPP (Release 13) de **1,4 MHz** de ancho de banda: hasta ~**1 Mbps**, menor latencia y, a diferencia de NB-IoT, **movilidad con traspaso (handover) y voz (VoLTE)**: wearables, seguimiento de flotas y activos. NB-IoT y LTE-M están integrados en el ecosistema **5G** como las tecnologías del caso de uso **mMTC** (tema 76).

| | Sigfox | LoRaWAN | NB-IoT | LTE-M |
| --- | --- | --- | --- | --- |
| Tipo | **Propietaria** (UnaBiz) | **Abierta** (LoRa Alliance) | Estándar **3GPP** | Estándar **3GPP** |
| Espectro | No licenciado (868 MHz) | No licenciado (868 MHz) | **Licenciado** | **Licenciado** |
| Ancho de banda | **100 Hz** | 125-250 kHz | **180 kHz** | **1,4 MHz** |
| Velocidad | ~600 bps | 0,3-50 kbps | Decenas de kbps | Hasta ~1 Mbps |
| Alcance | 10-50 km | 5-15 km | 1-15 km, gran penetración | Como la red LTE |
| Batería | ~15 años | ~15 años | ~10 años | Menor |
| Movilidad y voz | No | Limitada | No | **Sí (VoLTE)** |
| Uso típico | Alarmas, contadores | Agro, ciudad, redes privadas | Contadores en interiores | Wearables, flotas |

## Sensórica e inteligencia artificial

Una **red de sensores inalámbrica (WSN, *Wireless Sensor Network*)** es un conjunto de nodos autónomos distribuidos espacialmente que miden condiciones físicas o ambientales (temperatura, presión, sonido, contaminación) y cooperan para hacer llegar los datos a una estación base. Son la capa de percepción del IoT y la base de conceptos como la **computación ubicua** y la **inteligencia ambiental**.

- **Elementos y topologías**:
    - **Nodo sensor (mote)**: microcontrolador, radio de bajo consumo, sensores y batería (a veces con captación de energía).
    - **Sumidero (sink) o estación base**: recoge los datos de la red y los envía a la plataforma; suele ser la pasarela.
    - **Topologías**: **estrella** (todos contra el sink), **malla** (los nodos se reenvían entre sí, más alcance y tolerancia a fallos) y **árbol jerárquico** (agrupación en clústeres con nodos cabecera).
    - **MWSN**: variante con nodos móviles (vehículos, drones, ganado), que añade flexibilidad y complica el encaminamiento.
- **La energía como recurso crítico**: los nodos deben durar años sin mantenimiento, y transmitir cuesta mucho más que computar. Técnicas habituales: ciclos de sueño profundo, **agregación de datos en la red** (fusionar lecturas antes de transmitir), protocolos jerárquicos de encaminamiento eficiente (tipo LEACH) y ***energy harvesting*** (captar energía solar, de vibraciones o de radiofrecuencia).
- **Factores que degradan la comunicación**: ruido e interferencias, atenuación (pérdida de espacio libre), difracción, multitrayecto, absorción atmosférica, orografía y obstáculos, y la calidad y orientación de las antenas.
- **Sensórica**: la caída de coste de los sensores **MEMS** (microelectromecánicos) ha multiplicado los despliegues. Tipos habituales: **ambientales** (temperatura, humedad, gases, partículas), **inerciales** (acelerómetro, giróscopo), de **posición** (GNSS), **ópticos y de imagen**, de **presencia y proximidad**, y **actuadores** (relés, válvulas, motores) que cierran el lazo de control.
- **Inteligencia artificial en el IoT (AIoT)**: la analítica se desplaza de la nube al borde:
    - **Edge AI**: la inferencia de modelos de IA se ejecuta en la pasarela o en el propio dispositivo, lo que reduce la **latencia**, el consumo de ancho de banda y la exposición de datos personales, y permite operar sin conectividad.
    - **TinyML**: modelos de aprendizaje automático comprimidos para ejecutarse en microcontroladores de milivatios (con marcos como TensorFlow Lite para microcontroladores).
    - **Aplicaciones**: **mantenimiento predictivo** (detectar el fallo antes de que ocurra a partir de vibración y temperatura), detección de anomalías en contadores y redes de suministro, visión artificial en el borde (aforos, seguridad) y reconocimiento de voz local.
    - Las técnicas de IA subyacentes se estudian en el tema 34; su aplicación urbana (plataformas de ciudad y gemelos digitales), en el 74.

## Fuentes {.unnumbered .unlisted}

- Recomendación UIT-T Y.2060 (junio de 2012, renumerada Y.4000): definición y visión general del IoT; Recomendación UIT-T Y.4480 (2021): protocolo LoRaWAN.
- RFC 7452, *Architectural Considerations in Smart Object Networking* (IAB, 2015).
- ISO/IEC 14443, 15693 y 18092 (tarjetas sin contacto y NFC); ISO/IEC 18000-63/EPC Gen2 (RFID UHF); IEEE 802.15.4; UIT-T G.9959 (Z-Wave); Matter 1.0 (CSA, octubre de 2022); IEEE 1934-2018 (fog computing).
- Bluetooth SIG: Core 4.0 (2010), 5.0 (2016), 6.0 (septiembre de 2024) y 6.1 (mayo de 2025), verificadas online en julio de 2026.
- 3GPP Release 13 (2016): NB-IoT y LTE-M; LoRa Alliance (especificación LoRaWAN); estado de Sigfox/UnaBiz verificado online en julio de 2026.
