# Protocolos de comunicaciones

Un protocolo de comunicaciones es el conjunto de reglas que permite a dos sistemas intercambiar datos de forma ordenada: define los formatos de los mensajes, la secuencia de intercambio y el tratamiento de errores. Este tema recorre los protocolos de la pila TCP/IP (tema [69](69-modelos-osi-y-tcp-ip.md)) de abajo arriba: la capa de internet (IPv4, IPv6, ICMP, ARP), la capa de transporte (TCP y UDP, con TLS) y la capa de aplicación (DNS, HTTP, SMTP, FTP, DHCP y SSH). Los protocolos de la capa de enlace (Ethernet, PPP, HDLC) se tratan en el tema [71](71-redes-de-computadores.md), y las redes inalámbricas en el [76](76-redes-inalambricas-y-5g.md).

Tabla resumen de los puertos más preguntables (los puertos identifican la aplicación dentro del host):

| Protocolo | Puerto(s) | Transporte |
| --- | --- | --- |
| FTP | **20** (datos) y **21** (control) | TCP |
| SSH (y SFTP/SCP) | **22** | TCP |
| TELNET | **23** | TCP |
| SMTP | **25** (entre servidores), **587** (envío), **465** (SMTPS) | TCP |
| DNS | **53** | UDP y TCP |
| DHCP | **67** (servidor) y **68** (cliente) | UDP |
| TFTP | **69** | UDP |
| HTTP | **80** | TCP |
| POP3 | **110** (con TLS: **995**) | TCP |
| NTP | **123** | UDP |
| IMAP | **143** (con TLS: **993**) | TCP |
| SNMP | **161** (agente) y **162** (traps) | UDP |
| HTTPS | **443** | TCP (HTTP/3: UDP/QUIC) |

## Capa de internet: IPv4, IPv6, ICMP y ARP

La capa de internet encamina los paquetes desde el host origen hasta el destino a través de redes interconectadas. Su protocolo central es IP, un servicio no orientado a conexión y de entrega no garantizada (*best effort*): la fiabilidad, si se necesita, la aportan las capas superiores.

### IPv4 (Internet Protocol version 4)

- **Direcciones de 32 bits** (2^32, unos 4300 millones), en notación decimal punteada (p. ej. 192.0.2.33). El direccionamiento (clases, CIDR, subredes) se estudia en el tema [71](71-redes-de-computadores.md).
- **No orientado a conexión**: cada datagrama se encamina de forma independiente; pueden perderse, duplicarse o llegar desordenados.
- **Checksum solo de cabecera**: verifica la integridad de la cabecera, no de los datos.
- **Fragmentación**: los routers pueden fragmentar los datagramas que excedan la **MTU** del enlace; el reensamblado se hace solo en el destino. Todo host debe aceptar datagramas de al menos **576 bytes**.
- **Cabecera IPv4**: longitud variable, de **20 bytes** (sin opciones) a **60 bytes**. Campos:
    - **Versión (4 bits)**: 0100 en binario (4).
    - **IHL, tamaño de cabecera (4 bits)**: en palabras de 32 bits; mínimo 5 (20 bytes).
    - **Tipo de servicio (8 bits)**: hoy campo **DSCP/ECN**, para calidad de servicio.
    - **Longitud total (16 bits)**: tamaño del datagrama en octetos, cabecera incluida; mínimo **20**, máximo **65 535**.
    - **Identificación (16 bits)**: identifica los fragmentos de un mismo datagrama.
    - **Flags (3 bits)**: control de fragmentación (DF *don't fragment*, MF *more fragments*).
    - **Offset de fragmento (13 bits)**: posición del fragmento, en unidades de 8 bytes.
    - **TTL (8 bits)**: saltos máximos antes de descartar el paquete; cada router lo decrementa. Valores iniciales típicos: **64 o 128**.
    - **Protocolo (8 bits)**: protocolo de la capa superior (**1** ICMP, **6** TCP, **17** UDP).
    - **Checksum de cabecera (16 bits)**.
    - **Direcciones origen y destino (32 bits cada una)**, más opciones y relleno.

![Formato de la cabecera IPv4](media/image75.png)

### IPv6 (Internet Protocol version 6)

Diseñado para sustituir a IPv4 ante el agotamiento de sus direcciones, con **direcciones de 128 bits** y una cabecera simplificada. No es directamente compatible con IPv4: ambos conviven mediante mecanismos de transición.

- **Ventajas frente a IPv4**:
    - **Espacio de direcciones** prácticamente ilimitado (2^128).
    - **Cabecera fija de 40 bytes** con solo **8 campos** (la de IPv4 tiene 12-14 y longitud variable): menos proceso en los routers. Las opciones van en **cabeceras de extensión** encadenadas.
    - **Sin fragmentación en tránsito**: solo fragmenta el nodo origen (con descubrimiento de la MTU del camino); los routers descartan y avisan por ICMPv6.
    - **Autoconfiguración**: **SLAAC** (*Stateless Address Autoconfiguration*) a partir de los anuncios de router, además de DHCPv6.
    - **Seguridad**: soporte nativo de **IPsec** (obligatorio en la especificación original, recomendado desde el RFC 8200).
    - **Etiqueta de flujo**: permite dar tratamiento diferenciado a los paquetes de un mismo flujo (p. ej. vídeo en tiempo real).
    - **Sin broadcast**: solo **unicast** (1 a 1), **multicast** (1 a n) y **anycast** (1 al miembro más cercano de un grupo).
    - **Movilidad (MIPv6)**: los dispositivos conservan su dirección al cambiar de red.
- **Cabecera IPv6** (40 bytes fijos):
    - **Versión (4 bits)**: 0110 en binario (6).
    - **Clase de tráfico (8 bits)**: prioridad (equivale al DSCP de IPv4).
    - **Etiqueta de flujo (20 bits)**.
    - **Longitud del campo de datos (16 bits)**: tamaño del payload.
    - **Cabecera siguiente (8 bits)**: cabecera de extensión o protocolo superior.
    - **Límite de saltos (8 bits)**: equivale al TTL.
    - **Direcciones origen y destino (128 bits cada una)**.
- **Notación**: **8 grupos de 4 dígitos hexadecimales** separados por dos puntos (2001:0db8:85a3:0000:0000:8a2e:0370:7334). Se pueden omitir los ceros iniciales de cada grupo y comprimir **una sola vez** grupos consecutivos de ceros con «::» (2001:db8::8a2e:370:7334). Las direcciones IPv4 se representan en IPv6 como *IPv4-mapped*: **::ffff:192.0.2.33**.
- **Transición IPv4/IPv6**: **doble pila** (el host habla ambos protocolos), **túneles** (IPv6 encapsulado en IPv4, p. ej. 6in4) y **traducción** (NAT64/DNS64).

![Formato de la cabecera IPv6](media/image76.png)

### ICMP (Internet Control Message Protocol)

- Protocolo auxiliar de IP para mensajes de **error, diagnóstico y control** (protocolo IP número 1). Sus mensajes también pueden perderse (viajan sobre IP).
- **Tipos de mensaje** más relevantes:

| Tipo | Mensaje | Uso |
| --- | --- | --- |
| **0** | Echo reply | respuesta a ping |
| **3** | Destino inaccesible | red/host/puerto inalcanzable |
| **5** | Redirect | indica una ruta mejor |
| **8** | Echo request | solicitud de ping |
| **11** | Tiempo excedido | TTL agotado (lo usa traceroute) |

- **Herramientas**: **ping** (echo request/reply, tipos 8 y 0) comprueba la conectividad; **traceroute** descubre la ruta enviando paquetes con TTL creciente y recogiendo los mensajes de tipo 11 de cada salto.
- **ICMPv6** (RFC 4443): versión para IPv6; además de errores y diagnóstico, integra el descubrimiento de vecinos (**NDP**) y la gestión de grupos multicast (MLD).

### ARP (Address Resolution Protocol) y NDP

- **ARP** resuelve direcciones IP en direcciones **MAC** dentro de una red local (IPv4):
    - **ARP Request**: el emisor pregunta en **broadcast** «¿quién tiene esta IP?».
    - **ARP Reply**: el propietario responde en **unicast** con su MAC.
    - Las asociaciones se guardan en la **caché ARP** para no repetir la consulta.
    - **ARP gratuito**: un host anuncia su propia asociación IP-MAC (p. ej. al arrancar), útil para detectar direcciones duplicadas.
- **NDP (Neighbor Discovery Protocol)**, RFC 4861: sustituye a ARP en **IPv6**, usando mensajes ICMPv6 (*Neighbor Solicitation/Advertisement* y *Router Solicitation/Advertisement*). Además de resolver direcciones, descubre routers y prefijos (base de SLAAC) y detecta direcciones duplicadas (DAD).
- **Otros protocolos de la capa**:
    - **RARP**: la función inversa de ARP (MAC a IP); obsoleto, sustituido por DHCP.
    - **IGMP**: gestión de la pertenencia a grupos **multicast** en IPv4.

## Capa de transporte: TCP y UDP

La capa de transporte proporciona comunicación extremo a extremo entre procesos, identificados por **puertos** (16 bits): **0-1023** bien conocidos, **1024-49151** registrados y **49152-65535** dinámicos o efímeros. La combinación IP + puerto forma un **socket**. Ofrece dos servicios: fiable y orientado a conexión (TCP) o ligero y sin conexión (UDP).

### TCP (Transmission Control Protocol)

- Servicio de **flujo de bytes fiable y ordenado**: garantiza que los datos llegan sin errores, sin duplicados y en el orden de envío. Especificación consolidada en el RFC 9293 (2022).
- **Orientado a conexión (stateful)**: establece, mantiene y cierra conexiones.
- **Cabecera de 20 bytes** como mínimo (frente a los 8 de UDP), con números de secuencia y confirmación, ventana y **flags**: SYN (sincronizar), ACK (confirmar), FIN (cerrar), RST (abortar), PSH y URG.
- **Establecimiento de conexión** en tres pasos (*three-way handshake*):
    1. **SYN**: el cliente solicita la conexión (número de secuencia inicial x).
    2. **SYN-ACK**: el servidor acepta (secuencia y, confirma x+1).
    3. **ACK**: el cliente confirma; puede empezar el intercambio de datos.

![Establecimiento de conexión TCP en tres pasos](media/image73.png)

- **Transferencia de datos**:
    - **Números de secuencia**: identifican y ordenan los bytes transmitidos.
    - **Confirmaciones (ACK) y retransmisión**: lo no confirmado a tiempo se reenvía.
    - **Checksum**: verifica la integridad de cabecera y datos.
    - **Ventana deslizante (control de flujo)**: el receptor anuncia cuántos bytes puede aceptar, y el emisor se ajusta a ese límite.
- **Control de congestión**: evita saturar la red ajustando la ventana de congestión:
    - **Slow start**: comienza con una ventana pequeña y la duplica en cada ida y vuelta.
    - **Congestion avoidance**: superado un umbral, el crecimiento pasa a ser lineal.
    - **Fast retransmit**: ante tres ACK duplicados retransmite sin esperar al temporizador.
    - **Fast recovery**: tras la retransmisión rápida continúa sin volver a slow start.
- **Cierre de conexión** en cuatro pasos (*four-way handshake*): cada sentido se cierra por separado (**FIN**, **ACK**, **FIN**, **ACK**), lo que permite el cierre a medias (*half-close*) mientras el otro extremo termina de enviar.

![Cierre de conexión TCP en cuatro pasos](media/image74.png)

### UDP (User Datagram Protocol)

- Envío de **datagramas** sin establecer conexión previa (RFC 768).
- **Características**:
    - **No orientado a conexión (stateless)**: no guarda estado entre mensajes.
    - **Sin garantías**: no hay confirmaciones, retransmisiones ni control de flujo o congestión; la entrega y el orden no están asegurados.
    - **Ligero y rápido**: cabecera fija de **8 bytes** (puerto origen, puerto destino, longitud y checksum).
- **Usos**: consultas DNS, DHCP, streaming de audio y vídeo, VoIP, juegos en línea y, en general, tráfico en tiempo real donde retransmitir llega tarde. Sobre UDP se construye **QUIC**, el transporte de HTTP/3.

![Cabecera UDP](media/image72.png)

### TLS (Transport Layer Security)

- Protocolo criptográfico que proporciona **confidencialidad, integridad y autenticación** a las comunicaciones sobre TCP. Es el sucesor de **SSL** (Secure Sockets Layer), hoy prohibido por inseguro.
- **Versiones**: vigentes **TLS 1.2** (RFC 5246, 2008) y **TLS 1.3** (RFC 8446, 2018); SSL 2.0/3.0 y TLS 1.0/1.1 están formalmente deprecadas (RFC 8996, 2021).
- **Funcionamiento (handshake)**:
    - **Negociación**: cliente y servidor acuerdan versión y suite criptográfica.
    - **Intercambio de claves**: acuerdo de una clave de sesión, típicamente con **ECDHE** (Diffie-Hellman efímero, que aporta secreto hacia adelante o *forward secrecy*).
    - **Autenticación** con certificados **X.509**: habitualmente solo se autentica el servidor; en **TLS mutuo (mTLS)** también el cliente presenta certificado.
    - **Cifrado del tráfico**: con criptografía simétrica autenticada (**AES-GCM**, **ChaCha20-Poly1305**), mucho más rápida que la asimétrica.
- **TLS 1.3** simplifica el handshake (**1 RTT**, y 0-RTT al reanudar sesiones) y elimina los algoritmos débiles (RSA estático, RC4, 3DES, SHA-1, modos CBC).

### Clases de transporte OSI (TP0-TP4)

El modelo OSI (ISO/IEC 8073, UIT-T X.224) define cinco clases de protocolo de transporte según la calidad de la red subyacente: **tipo A** (fiable), **tipo B** (errores señalizados pero no corregidos) y **tipo C** (no fiable, tasa de error inaceptable).

| Clase | Características | Red |
| --- | --- | --- |
| **TP0** | La más simple: solo fragmentación y reensamblado | A |
| **TP1** | Añade recuperación básica de errores | B |
| **TP2** | Multiplexa varias conexiones de transporte sobre una de red; control de flujo | A |
| **TP3** | Combina TP1 y TP2 (recuperación + multiplexación) | B |
| **TP4** | Detección y recuperación completas de errores; equivale a TCP | C |

## Capa de aplicación: DNS, HTTP, SMTP, FTP, DHCP y SSH

La capa de aplicación agrupa los protocolos con los que trabajan directamente los programas de usuario y los servicios de red. Cada uno usa TCP o UDP a través de sus puertos asignados (tabla de la introducción).

### DNS (Domain Name System)

- Sistema de nombres **jerárquico y descentralizado** que traduce nombres de dominio en direcciones IP (y a la inversa), sobre una **base de datos distribuida** en zonas.
- **Puerto 53**: **UDP** para las consultas habituales y **TCP** para las transferencias de zona y las respuestas grandes. Variantes cifradas: **DoT** (DNS over TLS, TCP 853) y **DoH** (DNS over HTTPS, 443).
- **Espacio de nombres**:
    - **FQDN** (*Fully Qualified Domain Name*): nombre completo (www.ejemplo.es.), que se resuelve de derecha a izquierda: raíz, **TLD** o dominio de primer nivel (genéricos como .com y .org, territoriales como .es), dominio de segundo nivel (ejemplo) y subdominios o hosts (www).
    - **Límites**: 255 octetos por nombre completo y **63** por etiqueta.
    - Los **subdominios** pueden delegarse a otros servidores (www.support.ejemplo.org).
- **Servidores raíz**: **13 identidades** ([A-M].root-servers.net), replicadas globalmente mediante anycast.
- **Tipos de servidores DNS**:
    - **Autoritativos**: responden con los datos originales de sus zonas de autoridad. El **primario (maestro)** mantiene la copia original; los **secundarios (esclavos)** la replican por transferencia de zona.
    - **Recursivos o caché (resolvers)**: resuelven por encargo de los clientes y guardan las respuestas durante su **TTL**.
    - **Reenviadores (forwarders)**: delegan las consultas en otro servidor recursivo.
- **Tipos de resolución**:
    - **Recursiva**: el servidor asume la resolución completa y devuelve la respuesta final (caso típico: del host a su DNS local).
    - **Iterativa**: el servidor devuelve la mejor referencia que conoce y el solicitante continúa (caso típico: del DNS local hacia raíz, TLD y autoritativos).

![Resolución DNS recursiva e iterativa](media/image71.png)

- **Registros DNS** principales:
    - **A** / **AAAA**: dirección IPv4 / IPv6.
    - **CNAME**: alias de otro nombre (nombre canónico).
    - **NS**: servidor de nombres autoritativo de la zona.
    - **MX**: servidores de correo del dominio, con prioridad.
    - **PTR**: resolución inversa (IP a nombre).
    - **SOA**: parámetros de la zona y su servidor primario (inicio de autoridad).
    - **SRV**: localización de servicios; **TXT**: texto libre (SPF, verificaciones).
- **DNSSEC**: extensión que **firma criptográficamente** los registros para garantizar su autenticidad e integridad (no cifra: no da confidencialidad).

### HTTP (Hypertext Transfer Protocol)

- Protocolo de **petición-respuesta** para la transferencia de recursos en la web; **puerto 80**.
- **Sin estado (stateless)**: cada petición es independiente; el estado de sesión se añade en la aplicación (cookies, tokens).
- **Métodos de petición**: **GET** (obtener un recurso, sin efectos secundarios), **HEAD** (como GET sin cuerpo), **POST** (enviar datos), **PUT** (reemplazar el recurso), **DELETE** (eliminarlo), **PATCH** (modificación parcial), **OPTIONS** (capacidades disponibles), **CONNECT** (establecer un túnel) y **TRACE** (eco de la petición).
- **Códigos de estado**:
    - **1xx** informativos; **2xx** éxito (**200** OK, **201** Created).
    - **3xx** redirección (**301** permanente, **302** temporal, **304** Not Modified).
    - **4xx** error del cliente (**400** Bad Request, **401** Unauthorized, **403** Forbidden, **404** Not Found).
    - **5xx** error del servidor (**500** Internal Server Error, **503** Service Unavailable).
- **Versiones**:
    - **HTTP/1.1** (1997; hoy RFC 9112): protocolo de texto, conexiones persistentes.
    - **HTTP/2** (2015; RFC 9113): binario, **multiplexa** varias peticiones sobre una conexión y comprime cabeceras (HPACK).
    - **HTTP/3** (2022; RFC 9114): funciona sobre **QUIC (UDP)**, integra TLS 1.3 y elimina el bloqueo de cabeza de línea de TCP.
- **HTTPS**: HTTP sobre **TLS**, **puerto 443**. Frente al HTTP plano (susceptible de escuchas y ataques *man-in-the-middle*), cifra el canal y autentica al servidor. Es el estándar de facto: los navegadores marcan como «no seguro» el HTTP sin cifrar.

### SMTP (Simple Mail Transfer Protocol)

- Protocolo de **envío** de correo electrónico, entre servidores y del cliente a su servidor de salida. No define cómo almacenar ni leer el correo (eso corresponde a POP/IMAP).
- **Puertos**: **25** (entre servidores), **587** (envío autenticado desde el cliente, con STARTTLS) y **465** (SMTPS, TLS implícito).
- **Con estado (stateful)**: la sesión mantiene un diálogo de comandos: **HELO/EHLO** (saludo), **MAIL FROM** (remitente), **RCPT TO** (destinatario), **DATA** (contenido) y **QUIT**. El mensaje termina con una línea que contiene solo un punto (\<CRLF>.\<CRLF>).
- **Recepción del correo**:
    - **POP3** (puerto **110**; con TLS, **995**): descarga los mensajes al cliente y normalmente los borra del servidor.
    - **IMAP** (puerto **143**; con TLS, **993**): gestiona los mensajes **en el servidor**, con carpetas y sincronización entre múltiples dispositivos.

### FTP (File Transfer Protocol)

- Protocolo clásico de **transferencia de archivos** cliente-servidor sobre TCP, bidireccional (subida y descarga).
- **Dos conexiones**: **control por el puerto 21** (comandos y respuestas) y **datos por el 20** (o un puerto negociado).
- **Modos de conexión de datos**:
    - **Activo (PORT)**: el cliente indica su puerto y el **servidor inicia** la conexión de datos; problemático tras cortafuegos y NAT.
    - **Pasivo (PASV)**: el servidor indica un puerto y el **cliente inicia** la conexión; es el modo compatible con cortafuegos.
- **Inseguro por diseño**: credenciales y datos viajan en **texto plano**.
- **Comandos** habituales: USER y PASS (autenticación), LIST (listar), RETR (descargar), STOR (subir), QUIT. **Códigos de respuesta** de tres dígitos: 1xx en proceso, 2xx éxito, 3xx falta información, 4xx error temporal, 5xx error permanente.
- **Variantes seguras**:
    - **FTPS**: FTP sobre TLS (puerto **990** en modo implícito).
    - **SFTP**: transferencia de archivos como subsistema de **SSH** (puerto **22**); es un protocolo distinto de FTP, no FTP cifrado.

### DHCP (Dynamic Host Configuration Protocol)

- Asigna dinámicamente la **configuración de red** de los equipos: dirección IP, máscara, puerta de enlace, servidores DNS y otras opciones. Funciona sobre **UDP 67 (servidor) / 68 (cliente)**.
- **Métodos de asignación**:
    - **Manual (estática)**: IP fija reservada a una MAC concreta.
    - **Automática**: IP permanente asignada la primera vez.
    - **Dinámica**: IP temporal de un rango, en régimen de **concesión (lease)** renovable.
- **Proceso en cuatro pasos (DORA)**:
    1. **Discover**: el cliente busca servidores en broadcast.
    2. **Offer**: los servidores ofrecen una configuración.
    3. **Request**: el cliente solicita la oferta elegida.
    4. **Acknowledge**: el servidor confirma y entrega la concesión.
- **Agente de retransmisión (DHCP relay)**: reenvía las peticiones broadcast a un servidor situado en otra subred, para centralizar el servicio.
- **En IPv6**: **DHCPv6**, que convive con la autoconfiguración SLAAC.

### SSH (Secure Shell)

- Protocolo de **acceso remoto seguro** sobre un canal cifrado; **puerto TCP 22**. Versión vigente: **SSH-2** (RFC 4251 a 4254).
- **Arquitectura en tres subprotocolos**:
    - **Transporte**: cifrado, integridad y autenticación del **servidor** (claves de host).
    - **Autenticación de usuario**: por **contraseña** o por **clave pública** (la recomendada), entre otros métodos.
    - **Conexión**: multiplexa varios canales (sesiones, reenvíos) sobre el mismo túnel.
- **Servicios**: terminal remota, transferencia de archivos (**SFTP** y **SCP**), **túneles y reenvío de puertos** (local, remoto y dinámico tipo SOCKS) y reenvío X11.
- Sustituye a **TELNET** (puerto **23**): terminal remota en **texto plano**, en desuso por transmitir las credenciales sin cifrar (igual que rlogin/rsh).

### Otros protocolos de la capa de aplicación

- **TFTP** (*Trivial File Transfer Protocol*), UDP **69**: transferencia simple de archivos sin autenticación; usado en arranque por red (PXE) y carga de firmware.
- **NFS** (*Network File System*): acceso a sistemas de archivos remotos como si fueran locales, originario de Sun Microsystems.
- **NTP** (*Network Time Protocol*), UDP **123**: sincronización horaria jerárquica (estratos).
- **SNMP** (*Simple Network Management Protocol*), UDP **161/162**: gestión y monitorización de dispositivos de red (se estudia en el tema [73](73-virtualizacion-de-redes.md)).

## Fuentes {.unnumbered .unlisted}

- RFC 791 (IPv4, 1981), RFC 8200 (IPv6, 2017), RFC 792 (ICMP, 1981), RFC 4443 (ICMPv6, 2006), RFC 826 (ARP, 1982) y RFC 4861 (NDP, 2007), IETF.
- RFC 9293 (TCP, 2022), RFC 768 (UDP, 1980), RFC 8446 (TLS 1.3, 2018) y RFC 8996 (deprecación de TLS 1.0/1.1, 2021), IETF.
- RFC 1034/1035 (DNS, 1987), RFC 9110-9114 (HTTP/1.1, HTTP/2 y HTTP/3, 2022), RFC 5321 (SMTP, 2008), RFC 959 (FTP, 1985), RFC 2131 (DHCP, 1997) y RFC 4251-4254 (SSH-2, 2006), IETF.
- ISO/IEC 8073 / UIT-T X.224 (clases de transporte OSI).
