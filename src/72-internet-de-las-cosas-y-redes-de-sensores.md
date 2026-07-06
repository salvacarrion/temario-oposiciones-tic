# Internet de las cosas y redes de sensores

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Internet de las Cosas (IoT)

La **Internet de las Cosas, o Internet of Things (IoT)** es una red de dispositivos conectados que pueden recopilar y compartir datos a través de internet. Estos dispositivos no solo se comunican entre sí, sino que también pueden tomar decisiones de manera autónoma.

### Objetivo

Enviar, recibir y analizar datos para mejorar procesos y tomar decisiones informadas.

**Componentes del IoT**:

- **Objetos conectados**: Dispositivos equipados con sensores y actuadores.
- **Tecnologías de red**: Infraestructura que permite la comunicación entre dispositivos.
- **Protocolos de comunicación**: Reglas y estándares que facilitan el intercambio de datos.
- **Plataforma IoT**: Entorno donde se procesan y gestionan los datos recopilados.
- **Aplicaciones de usuario**: Interfaces mediante las cuales los usuarios interactúan con el sistema.

**Actores en el IoT**:

- **Operadores de telefonía**: Proveen la conectividad necesaria.
- **Industria**: Desarrolla dispositivos y soluciones IoT.
- **Administraciones**: Regulan y promueven el uso del IoT.
- **Usuarios**: Finales y empresariales que utilizan las aplicaciones y servicios.

**Tipos de dispositivos**:

- **Interruptores**: Envían instrucciones a otros objetos.
- **Sensores**: Recopilan datos y los envían para su análisis.

**Modelos de comunicación**:

- **Dispositivo a dispositivo**: Comunicación directa entre dispositivos.
- **Dispositivo a la nube**: Los dispositivos se conectan a servicios en la nube para procesamiento y almacenamiento.
- **Dispositivo a puerta de enlace**: Uso de un intermediario que gestiona la comunicación.
- **Intercambio de datos a través del backend**: Los datos se comparten y procesan en sistemas de respaldo.

**Ventajas del IoT**:

- Conectividad de múltiples dispositivos a la red.
- Intercambio de información rápido y en tiempo real.
- Ahorro energético y procesos más sostenibles.
- Comunicación eficiente con el entorno directo.

**Desventajas del IoT**:

- Problemas de **seguridad** y **privacidad**.
- Costes asociados a la implementación y mantenimiento.
- Falta de **compatibilidad** entre diferentes dispositivos y estándares.

**Tipos de arquitecturas**:

- **Arquitectura de tres niveles con objetos conectados sin protocolo IP**: Incluye dispositivos, una puerta de enlace y la nube.
- **Arquitectura de dos niveles con objetos conectados con protocolo IP**: Los dispositivos se conectan directamente a la nube usando IP.
- **Arquitectura de dos niveles con objetos conectados sin protocolo IP**: Los dispositivos se conectan a la nube a través de una puerta de enlace sin usar IP.

**Ecosistema del IoT**:

- **Capa de nodos**: Dispositivos y sensores que recopilan datos.
- **Capa de datos**: Almacenamiento y gestión de la información recopilada.
- **Capa de conectividad**: Redes y protocolos que permiten la comunicación.
- **Capa de aplicación**: Servicios y aplicaciones que utilizan los datos para proporcionar valor al usuario.

**Protocolos del IoT**:

- **AMQP (Advanced Message Queuing Protocol)**
- **CoAP (Constrained Application Protocol)**
- **DDS (Servicio de Distribución de Datos)**
- **MQTT (Message Queue Telemetry Transport)**
- **M2M (Protocolo de Comunicaciones entre Máquinas)**
- **XMPP (Extensible Messaging and Presence Protocol)**
- **Tecnologías inalámbricas**: Bluetooth, Zigbee, Z-Wave, 6LoWPAN, Thread, Wi-Fi, NFC.
- **Redes de largo alcance**: Sigfox, LoRaWAN.
- **Conectividad celular**: Redes móviles tradicionales.

## Redes de Sensores

Las **redes de sensores** son sistemas que utilizan dispositivos para recopilar y transmitir datos sobre condiciones físicas o ambientales, como temperatura, sonido o presión. Consisten en una red de pequeños ordenadores o **nodos**, equipados con sensores que colaboran en una o más tareas comunes. Estas redes forman parte de conceptos como la **inteligencia ambiental** y la **computación ubicua**.

**Tipos de redes**:

- **Redes de corto alcance o PAN (Personal Area Network)**:
    - Alcance limitado, generalmente de menos de 10 metros.
    - Utilizadas en aplicaciones de hogar y edificios inteligentes.
    - **Ejemplos**: Bluetooth, Wi-Fi, Zigbee, NFC, RFID, Z-Wave, 6LoWPAN, IR, UWB, bandas ISM.
- **Redes de largo alcance o WAN (Wide Area Network)**:
    - Alcance mucho mayor, utilizadas para transmitir datos a largas distancias.
    - Empleadas en aplicaciones de monitoreo ambiental y transporte.
    - **Ejemplos**: LoRaWAN, Sigfox, LTE-M, NB-IoT, 5G.

**Variantes de redes de sensores**:

- **Wireless Sensor Network (WSN)**: Redes de sensores autónomos distribuidos espacialmente para monitorear condiciones ambientales.
- **Mobile Wireless Sensor Network (MWSN)**: Variante de WSN donde los nodos son móviles, lo que aumenta la flexibilidad y el alcance de la red.

**Factores que pueden afectar a la comunicación**:

- **Rendimiento** y **potencia** de los dispositivos.
- **Ruido** y **frecuencia** en el entorno de comunicación.
- **Pérdida de espacio libre** y **difracción** de las señales.
- **Multitrayectoria** y **absorción** que pueden degradar la señal.
- Características del **terreno** y obstáculos físicos.
- Calidad de las **antenas** y el **alcance** efectivo de la comunicación.
