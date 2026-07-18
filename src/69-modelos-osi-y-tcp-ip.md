# Modelos OSI y TCP/IP

Los modelos de referencia organizan las funciones de una red en capas, de modo que un problema complejo (llevar datos de una aplicación a otra a través de medios y tecnologías heterogéneos) se descompone en problemas menores y bien delimitados. Este tema cubre los conceptos de la arquitectura en capas, el modelo de referencia OSI, el modelo TCP/IP y la comparativa entre ambos. Los protocolos de cada capa se estudian en el tema [70](70-protocolos-de-comunicaciones.md), y los dispositivos y tecnologías de red en el [71](71-redes-de-computadores.md).

## La arquitectura en capas: conceptos básicos

Para reducir la complejidad del diseño, las redes se estructuran como una pila de capas, cada una construida sobre la inferior: cada capa ofrece servicios a la capa superior ocultando los detalles de cómo los implementa. Esta modularidad permite sustituir o evolucionar una capa sin afectar al resto y hace posible que interoperen equipos de distintos fabricantes.

- **Servicio**: conjunto de operaciones que una capa ofrece a la capa inmediatamente superior. Define *qué* hace la capa, no *cómo* lo hace.
- **Interfaz**: frontera entre dos capas adyacentes de un mismo sistema; define las operaciones y servicios accesibles desde arriba. En terminología OSI, el servicio se accede a través de los **puntos de acceso al servicio (SAP)**.
- **Protocolo**: conjunto de reglas que gobierna el formato y el significado de los mensajes que intercambian las **entidades pares** (entidades de la misma capa en máquinas distintas). Define *cómo* se presta el servicio.
- **Comunicación virtual y real**: las entidades pares «conversan» lógicamente mediante su protocolo, pero los datos reales descienden por la pila del emisor, cruzan el medio físico y ascienden por la pila del receptor.
- **Primitivas de servicio**: OSI define cuatro: **request** (petición), **indication** (indicación), **response** (respuesta) y **confirm** (confirmación). Un servicio **confirmado** usa las cuatro; uno **no confirmado**, solo petición e indicación.
- **Servicio orientado a conexión**: con fases de establecimiento, transferencia y liberación; los datos llegan en orden por el «circuito» acordado (modelo del teléfono).
- **Servicio no orientado a conexión (datagrama)**: cada mensaje viaja de forma independiente, con la dirección de destino completa (modelo del correo postal).

### Encapsulamiento y unidades de datos

En el emisor, cada capa recibe los datos de la capa superior y les añade su propia información de control en una cabecera (la capa de enlace añade además una cola); en el receptor, cada capa retira la cabecera de su nivel y entrega el resto hacia arriba. Este proceso se llama **encapsulamiento** (y su inverso, **desencapsulamiento**).

- **SDU (Service Data Unit)**: los datos que una capa recibe de la superior para transmitir.
- **PDU (Protocol Data Unit)**: la unidad que una capa intercambia con su entidad par; se forma añadiendo la información de control propia (PCI) a la SDU.

Cada capa da un nombre propio a su PDU, y esa denominación es preguntable:

| Capa | Unidad de datos (PDU) |
| --- | --- |
| Aplicación, presentación y sesión | Datos |
| Transporte | **Segmento** (TCP) o **datagrama** (UDP) |
| Red | **Paquete** |
| Enlace de datos | **Trama** |
| Física | **Bits** |

## El modelo de referencia OSI

El modelo de interconexión de sistemas abiertos (OSI, *Open Systems Interconnection*) es un marco conceptual que estandariza las funciones de comunicación en **siete capas** para que sistemas de distintos fabricantes puedan interoperar. La **ISO** inició los trabajos en 1977 y publicó la norma en **1984** como **ISO 7498**, revisada como **ISO/IEC 7498-1:1994** (equivalente a la recomendación **UIT-T X.200**). **No es una arquitectura de red ni define protocolos concretos**: establece qué funciones corresponden a cada capa. Los protocolos OSI apenas llegaron a desplegarse (las clases de transporte TP0-TP4 se ven en el tema [70](70-protocolos-de-comunicaciones.md)), pero el modelo pervive como vocabulario de referencia del sector.

### Las siete capas

De abajo arriba (iniciales F-E-R-T-S-P-A; mnemotecnia clásica en inglés: «Please Do Not Throw Sausage Pizza Away»):

- **Capa 1: física**
    - **Responsabilidad**: transmitir los bits en bruto a través del medio de comunicación.
    - **Funciones**: define las características **mecánicas, eléctricas, funcionales y de procedimiento** de la conexión: voltajes, duración de un bit, conectores, sincronización, velocidades de transmisión y modos símplex/semidúplex/dúplex.
- **Capa 2: enlace de datos**
    - **Responsabilidad**: transferencia libre de errores entre dos nodos **adyacentes** (conectados al mismo enlace).
    - **Funciones**: encapsular los paquetes en **tramas** y delimitarlas, direccionamiento **físico (MAC)**, detección y corrección de errores del enlace, control de flujo entre nodos y control de acceso al medio compartido.
    - En las redes IEEE 802 se subdivide en dos subcapas: **LLC** (control de enlace lógico) y **MAC** (control de acceso al medio).
- **Capa 3: red**
    - **Responsabilidad**: encaminar los paquetes desde el origen hasta el destino a través de múltiples nodos intermedios.
    - **Funciones**: direccionamiento **lógico**, **encaminamiento** (*routing*) y control de la congestión.
    - **Tipos de servicio**: de **datagramas** (cada paquete se encamina de forma independiente, sin estado) o de **circuitos virtuales** (se establece una ruta por la que transitan todos los paquetes en orden, con estado).
- **Capa 4: transporte**
    - **Responsabilidad**: primera capa **extremo a extremo**: comunica el origen con el destino final, no con los nodos intermedios, con la calidad de servicio requerida.
    - **Funciones**: segmentación y reensamblado, control de flujo y de errores extremo a extremo y multiplexación de conexiones. El servicio puede ser orientado a conexión o sin conexión; OSI define **cinco clases de protocolo (TP0 a TP4)** según la fiabilidad de la red subyacente (tema [70](70-protocolos-de-comunicaciones.md)).
- **Capa 5: sesión**
    - **Responsabilidad**: establecer, mantener y finalizar sesiones de comunicación entre aplicaciones.
    - **Funciones**: **control del diálogo** (quién transmite y cuándo: dúplex o semidúplex), **agrupamiento** del flujo en unidades lógicas o transacciones y **recuperación** mediante puntos de comprobación (*checkpoints*) que permiten reanudar la comunicación tras un fallo desde el último punto válido.
- **Capa 6: presentación**
    - **Responsabilidad**: la sintaxis y la semántica de la información transmitida, para que sistemas con representaciones internas distintas se entiendan.
    - **Funciones**: representación común de los datos (notación **ASN.1**), conversión de códigos de caracteres, **compresión** y **cifrado**.
- **Capa 7: aplicación**
    - **Responsabilidad**: proporcionar servicios de red directamente a las aplicaciones del usuario.
    - **Funciones**: protocolos de alto nivel para correo electrónico, transferencia de ficheros, terminal virtual o acceso a recursos remotos.

## El modelo TCP/IP

El modelo TCP/IP (*Internet protocol suite*) es la arquitectura de protocolos sobre la que funciona Internet. Nació en la red **ARPANET** de **DARPA**: Cerf y Kahn publicaron su diseño en **1974** («A Protocol for Packet Network Intercommunication»); el protocolo se separó después en TCP e IP (cuyas versiones 4 definen los **RFC 791 y 793, de 1981**) y ARPANET migró a TCP/IP el **1 de enero de 1983**. El modelo de **cuatro capas** quedó formalizado en los **RFC 1122 y 1123 (1989)**. A diferencia de OSI, aquí **los protocolos precedieron al modelo**: TCP/IP describe una pila real ya construida.

### Las cuatro capas

- **Capa de acceso a la red (enlace)**
    - **Función**: conectar el equipo con su red física.
    - TCP/IP **no la especifica**: se apoya en las tecnologías de red existentes (**Ethernet**, **Wi-Fi IEEE 802.11**, **PPP**; históricamente también Token Ring, FDDI, X.25, Frame Relay o ATM, hoy legadas: tema [71](71-redes-de-computadores.md)). IP es agnóstico del medio («IP sobre cualquier cosa»).
- **Capa de internet**
    - **Función**: encaminar **datagramas** entre redes, de forma **no orientada a conexión** y de **mejor esfuerzo** (*best effort*): los paquetes pueden seguir rutas distintas y no se garantiza la entrega, el orden ni la integridad (esas garantías, si se necesitan, las aporta el transporte).
    - **Protocolos**: **IP** (IPv4/IPv6, direccionamiento lógico y encaminamiento), **ICMP** (mensajes de control y diagnóstico) y **ARP** (resolución de direcciones IP a MAC, en la frontera con el enlace). Su predecesor inverso RARP quedó obsoleto, sustituido por BOOTP y después DHCP.
- **Capa de transporte**
    - **Función**: comunicación extremo a extremo entre procesos.
    - **Protocolos**: **TCP** (orientado a conexión, fiable, con control de flujo y de congestión) y **UDP** (sin conexión, no fiable, de mínima sobrecarga). Sobre ellos se apoyan **TLS** (cifrado sobre TCP) y **QUIC** (transporte cifrado sobre UDP).
- **Capa de aplicación**
    - **Función**: servicios al usuario final; absorbe las funciones de las capas de sesión y presentación de OSI.
    - **Protocolos**: **HTTP**, **DNS**, **SMTP**, **FTP**, **DHCP**, **SSH**, **SNMP**… (se estudian en el tema [70](70-protocolos-de-comunicaciones.md)).

Un principio de diseño célebre de esta pila es el **principio de robustez** (RFC 1122, atribuido a Jon Postel): «sé conservador en lo que envías y liberal en lo que aceptas».

## Comparativa entre modelos

Ambos modelos comparten la idea esencial: una pila de capas independientes, con funciones parecidas en las capas comunes y un transporte extremo a extremo. Difieren en el número de capas, en la filosofía de diseño y en su éxito práctico.

### Correspondencia entre capas

| Modelo OSI | Modelo TCP/IP | Unidad de datos | Protocolos y estándares |
| --- | --- | --- | --- |
| 7. Aplicación | Aplicación | Datos | HTTP, FTP, DNS, SMTP, SSH, SNMP |
| 6. Presentación | Aplicación | Datos | TLS (cifrado), MIME, ASN.1, JPEG |
| 5. Sesión | Aplicación | Datos | RPC, NetBIOS, *sockets* |
| 4. Transporte | Transporte | Segmento (TCP) o datagrama (UDP) | TCP, UDP, QUIC |
| 3. Red | Internet | Paquete | IP, ICMP, IPsec |
| 2. Enlace de datos | Acceso a la red | Trama | Ethernet (802.3), Wi-Fi (802.11), PPP |
| 1. Física | Acceso a la red | Bits | Especificaciones del medio: cobre, fibra, radio |

### Diferencias clave

- **Número de capas: 7 frente a 4**. TCP/IP funde la física y el enlace en el acceso a la red, y absorbe la sesión y la presentación en la aplicación.
- **Filosofía**: OSI es **prescriptivo** (el modelo se definió antes que sus protocolos y aspira a ser general); TCP/IP es **descriptivo** (documenta una pila ya construida y no sirve para describir otras redes).
- **Rigor conceptual**: OSI distingue con claridad **servicio, interfaz y protocolo**; TCP/IP no separa estos conceptos.
- **Tipos de servicio**: en la capa de red OSI contempla datagramas y circuitos virtuales, pero en transporte solo servicio orientado a conexión; TCP/IP ofrece solo datagramas en internet (IP) y ambos tipos en transporte (TCP y UDP), la combinación que se impuso.
- **Resultado práctico**: los protocolos OSI fracasaron comercialmente y la pila TCP/IP domina Internet; el modelo OSI sobrevive como marco de referencia y vocabulario común («un switch es un dispositivo de capa 2»).

### Críticas y modelo híbrido

Las críticas clásicas (Tanenbaum) resumen por qué ninguno de los dos modelos es perfecto:

- **A OSI**: llegó en mal momento (TCP/IP ya estaba implantado cuando aparecieron sus protocolos), con mala tecnología (las capas de sesión y presentación casi vacías, las de enlace y red sobrecargadas) y con implementaciones iniciales lentas y pesadas.
- **A TCP/IP**: no distingue servicio, interfaz y protocolo; no es un modelo general; y la capa de acceso a la red es más una interfaz que una capa verdadera, pues no separa la física del enlace.

Por ello, la docencia y la práctica profesional usan un **modelo híbrido de cinco capas** (física, enlace, red, transporte y aplicación), el de los libros de texto de referencia (Tanenbaum; Kurose y Ross). La estructura de los temas [70](70-protocolos-de-comunicaciones.md) y [71](71-redes-de-computadores.md) responde a este modelo.

## Fuentes {.unnumbered .unlisted}

- ISO/IEC 7498-1:1994 (equivalente a UIT-T X.200): modelo de referencia OSI (primera edición: ISO 7498:1984).
- RFC 1122 y RFC 1123 (octubre de 1989): requisitos de los hosts de Internet; definen las cuatro capas del modelo TCP/IP.
- RFC 791, *Internet Protocol* (septiembre de 1981); RFC 9293, *Transmission Control Protocol* (agosto de 2022).
- V. Cerf y R. Kahn, «A Protocol for Packet Network Intercommunication», *IEEE Transactions on Communications* (mayo de 1974).
- A. Tanenbaum, N. Feamster y D. Wetherall, *Computer Networks*, 6.ª ed., Pearson, 2021.
- J. Kurose y K. Ross, *Computer Networking: A Top-Down Approach*, 8.ª ed., Pearson, 2021.
