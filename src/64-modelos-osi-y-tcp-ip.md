# Modelos OSI y TCP/IP

## Modelo de Referencia OSI (Open Systems Interconnection)

El Modelo OSI es un marco de referencia lógico y conceptual diseñado para estandarizar y normalizar la interconexión de sistemas abiertos, facilitando la compatibilidad entre diferentes tecnologías de red. Creado en 1980 por la **ISO** (International Organization for Standardization), **no es un modelo de red** específico **ni define protocolos concretos**, pero sí establece las funcionalidades que deben cumplir los protocolos de comunicación para lograr un estándar común.

### Arquitectura del Modelo OSI: 7 Capas ("FER Tiene Su Pipi Amarillo")

El modelo se compone de siete capas jerárquicas, cada una encargada de funciones específicas en el proceso de comunicación:

- **Capa 7: Aplicación**
    - **Responsabilidad**: Proporcionar servicios de red directamente a las aplicaciones del usuario.
    - **Función**: Facilitar APIs de alto nivel para actividades como compartir recursos, acceso remoto a archivos y servicios de correo electrónico.
    - **Unidad de Datos**: Datos.
- **Capa 6: Presentación**
    - **Responsabilidad**: Transformar y adaptar el formato de los datos para asegurar que la información enviada por la capa de aplicación de un sistema sea entendible por la capa de aplicación de otro.
    - **Función**: Gestionar la codificación de caracteres, compresión de datos y cifrado/descifrado para la seguridad y eficiencia de la información.
    - **Unidad de Datos**: Datos.
- **Capa 5: Sesión**
    - **Responsabilidad**: Establecer, mantener y finalizar sesiones de comunicación entre aplicaciones en diferentes dispositivos.
    - **Función**: Manejar el diálogo entre sistemas, controlando quién transmite y durante cuánto tiempo.
    - **Características Adicionales**:
        - **Control del Diálogo**: Define si la comunicación es bidireccional simultánea (**full-duplex**) o alternada (**half-duplex**).
        - **Agrupamiento**: Permite organizar el flujo de datos en unidades lógicas o transacciones.
        - **Recuperación**: Implementa puntos de comprobación para reiniciar la comunicación desde el último punto válido en caso de fallo.
    - **Unidad de Datos**: Datos.
- **Capa 4: Transporte**
    - **Responsabilidad**: Proporcionar una transferencia de datos confiable y transparente entre extremos, ajustándose a los requisitos de calidad de servicio.
    - **Función**: Realizar la segmentación y reensamblado de datos, control de flujo, detección y corrección de errores, y multiplexación de conexiones.
    - **Unidad de Datos**: Segmento o Datagrama.
    - **Tipos de Servicios**:
        - **Conmutación de Datagramas (Stateless)**: Cada paquete es independiente y se enruta individualmente.
        - **Circuitos Virtuales (Stateful)**: Se establece una ruta predefinida por la que todos los paquetes transitan en orden.
- **Capa 3: Red**
    - **Responsabilidad**: Determinar cómo se enrutan los datos desde el origen hasta el destino a través de múltiples nodos.
    - **Función**: Gestionar el direccionamiento lógico, el enrutamiento y el control de congestión en la red.
    - **Unidad de Datos**: Paquete.
- **Capa 2: Enlace (de Datos)**
    - **Responsabilidad**: Proporcionar transferencia de datos libre de errores entre dos nodos conectados físicamente.
    - **Función**: Encapsular paquetes en tramas, gestionar direcciones físicas (**MAC**), detección y corrección de errores a nivel de enlace.
    - **Unidad de Datos**: Trama.
- **Capa 1: Física**
    - **Responsabilidad**: Definir las características eléctricas, mecánicas y funcionales para activar, mantener y desactivar conexiones físicas.
    - **Función**: Transmitir bits individuales a través de un medio físico, incluyendo aspectos como voltajes, sincronización y velocidades de transmisión.
    - **Unidad de Datos**: Bits.

## Modelo TCP/IP o Internet Protocol Suite

El Modelo TCP/IP es un conjunto de protocolos de comunicación fundamentales para Internet y redes similares. Desarrollado en 1973 por **DARPA** (Defense Advanced Research Projects Agency), precede al Modelo OSI y define protocolos específicos para la comunicación en red, estableciendo estándares prácticos que permiten la interoperabilidad entre sistemas heterogéneos.

### Arquitectura del Modelo TCP/IP: 4 Capas ("Ana Toca Iguanas Eléctricas")

El modelo consta de cuatro capas, cada una con roles definidos:

- **Capa de Aplicación**
    - **Función**: Proporcionar servicios de red a las aplicaciones del usuario final.
    - **Protocolos Comunes**:
        - **HTTP (HyperText Transfer Protocol)**: Transferencia de documentos web.
        - **FTP (File Transfer Protocol)**: Transferencia de archivos entre sistemas.
        - **DNS (Domain Name System)**: Resolución de nombres de dominio.
        - **SMTP (Simple Mail Transfer Protocol)**, **POP (Post Office Protocol)**, **IMAP (Internet Message Access Protocol)**: Servicios de correo electrónico.
        - **Telnet**: Acceso remoto a servidores.
- **Capa de Transporte**
    - **Función**: Proporcionar comunicación de extremo a extremo y control de flujo.
    - **Protocolos**:
        - **TCP (Transmission Control Protocol)**: Protocolo orientado a conexión que garantiza la entrega confiable de datos.
        - **UDP (User Datagram Protocol)**: Protocolo sin conexión que permite el envío rápido de datagramas sin garantizar su entrega.
        - **TLS (Transport Layer Security)**: Protocolo de seguridad para comunicaciones cifradas.
- **Capa de Internet**
    - **Función**: Encargada del direccionamiento y enrutamiento de paquetes entre redes.
    - **Características**:
        - Los paquetes pueden seguir rutas diferentes entre origen y destino.
        - No se garantiza la entrega en orden ni la integridad de los datos; estas funciones son manejadas por capas superiores si es necesario.
    - **Protocolos**:
        - **IP (Internet Protocol)**: Proporciona direccionamiento lógico y enrutamiento de paquetes.
        - **ICMP (Internet Control Message Protocol)**: Utilizado para mensajes de control y diagnóstico.
        - **ARP (Address Resolution Protocol)**: Resuelve direcciones IP a direcciones MAC.
        - **RARP (Reverse ARP)**: Resuelve direcciones MAC a direcciones IP.
- **Capa de Enlace (de Datos) o Acceso a la Red**
    - **Función**: Gestionar la transmisión física de datos en el medio de comunicación de la red.
    - **Protocolos y Tecnologías**:
        - **Ethernet**, **Fast Ethernet**: Estándares para redes de área local (**LAN**).
        - **Token Ring**, **Token Bus**: Tecnologías de acceso al medio basadas en paso de testigo.
        - **FDDI (Fiber Distributed Data Interface)**: Tecnología para redes de alta velocidad usando fibra óptica.
        - **X.25**, **Frame Relay**, **ATM (Asynchronous Transfer Mode)**: Tecnologías para redes de área amplia (**WAN**).

## Comparativa entre modelos

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Modelo OSI</th>
<th style="text-align: center;">Modelo TCP/IP</th>
<th style="text-align: center;">Protocol Data Unit</th>
<th style="text-align: center;">Protocolos</th>
</tr>
</thead>
<tbody>
<tr>
<td>Capa de Aplicación</td>
<td rowspan="3">Capa de Aplicación</td>
<td>Datos</td>
<td>HTTP, FTP, DNS, SMPT, Telnet..</td>
</tr>
<tr>
<td>Capa de Presentación</td>
<td>Datos</td>
<td>*SSL, TLS, MPEG, JPEG,…</td>
</tr>
<tr>
<td>Capa de Sesión</td>
<td>Datos</td>
<td>*RPC, SCP, NetBIOS, PPTP, Sockets</td>
</tr>
<tr>
<td>Cada de Transporte</td>
<td>Capa de Transporte</td>
<td>Segmento o Datagrama</td>
<td>TCP, UDP, TLS</td>
</tr>
<tr>
<td>Capa de Red</td>
<td>Capa de Internet</td>
<td>Paquete</td>
<td>IP, IPSec, ICMP, Router</td>
</tr>
<tr>
<td>Capa de Enlace (de Datos)</td>
<td rowspan="2">Capa de Enlace o Acceso a la Red</td>
<td>Trama</td>
<td>Ethernet, PPP, Switch, Bridge</td>
</tr>
<tr>
<td>Capa Física</td>
<td>Bit, Baudios</td>
<td>Cables, Fibra, Repeaters, Hub,…</td>
</tr>
</tbody>
</table>
