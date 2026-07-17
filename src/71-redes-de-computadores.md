# Redes de computadores

Una red de computadores es un conjunto de equipos (nodos) interconectados mediante dispositivos físicos y software que intercambian datos a través de impulsos eléctricos, ondas electromagnéticas u otros medios, con el fin de compartir información, recursos y servicios. Este tema cubre los elementos y clasificaciones de las redes, las redes de área local (Ethernet, VLAN, DMZ), las redes de área extensa y el direccionamiento IP con su caso práctico. Los protocolos de cada capa se estudian en el tema 70, las redes inalámbricas en el 72 y la seguridad de red en el 75.

## Componentes, topologías y dispositivos de interconexión

Toda red combina una **capa física** (los elementos tangibles: tarjetas de red, cables, antenas) y una **capa lógica** (las normas y protocolos que proporcionan los servicios de comunicación).

- **Elementos de la comunicación**: **emisor** (envía el mensaje), **mensaje** (la información a transmitir), **medio** (el canal por el que viaja) y **receptor** (quien lo recibe).
- **Componentes básicos de la red**:
    - **Hardware**: los dispositivos físicos (equipos, switches, routers, servidores, cableado).
    - **Software**: los programas que gestionan la comunicación y el flujo de datos.
    - **Protocolos**: las reglas que permiten entenderse a dispositivos de distintos fabricantes (tema 70).

### Dispositivos de interconexión

Cada dispositivo opera en una capa del modelo OSI (tema 69), lo que determina qué información usa para reenviar el tráfico:

| Dispositivo | Capa OSI | Función |
| --- | --- | --- |
| **Repetidor / hub** | **1** (física) | Regenera o replica la señal por todos los puertos; un único dominio de colisión. En desuso |
| **Puente (bridge)** | **2** (enlace) | Interconecta segmentos de red reenviando tramas según la MAC de destino |
| **Conmutador (switch)** | **2** (enlace) | Puente multipuerto: aprende las MAC en una tabla y reenvía cada trama solo por el puerto del destino; cada puerto es un dominio de colisión independiente |
| **Enrutador (router)** | **3** (red) | Interconecta redes con distintos prefijos IP y elige la mejor ruta para cada paquete; separa dominios de difusión |
| **Pasarela (gateway)** | Hasta la **7** | Traduce entre protocolos o arquitecturas distintas |
| **Punto de acceso (WAP)** | 2 | Conecta dispositivos inalámbricos a la red cableada |

### Clasificación de las redes por alcance

- **PAN (Personal Area Network)**: comunicación entre dispositivos cercanos a una persona (smartphone, reloj); su variante inalámbrica es la **WPAN** (p. ej. Bluetooth).
- **LAN (Local Area Network)**: área geográfica pequeña (una sala, un edificio); su variante inalámbrica es la **WLAN** (Wi-Fi, tema 76).
- **CAN (Campus Area Network)**: interconecta las LAN de un campus o parque tecnológico.
- **MAN (Metropolitan Area Network)**: red de alta velocidad de ámbito urbano (una ciudad, una red de edificios públicos).
- **WAN (Wide Area Network)**: área geográfica extensa, usando enlaces de operador, cables submarinos o satélites; Internet es la WAN global.

### Clasificación de las redes por topología

- **Bus (lineal)**: un único canal compartido al que se conectan todos los nodos; sencilla y económica, pero el fallo del canal interrumpe toda la red.
- **Anillo (ring)**: cada estación se conecta a la siguiente y la última a la primera; los datos circulan en un sentido y cada nodo repite la señal. El **doble anillo** añade redundancia.
- **Estrella (star)**: todas las estaciones se conectan a un punto central (switch); fácil de administrar y escalar, es la topología habitual de las LAN actuales.
- **Malla (mesh)**: cada nodo se conecta a varios (malla parcial) o a todos los demás (malla completa o totalmente conexa); máxima redundancia y fiabilidad.
- **Árbol (tree)**: jerarquía de nodos que combina estrella y bus.
- **Híbrida o mixta**: combinación de las anteriores según las necesidades.

![Topologías de red: bus, estrella, mixta, anillo, doble anillo, árbol, malla y totalmente conexa](media/image77.png){width=60%}

### Clasificación de las redes por direccionalidad

- **Simplex (unidireccional)**: un dispositivo transmite y otro recibe (radiodifusión).
- **Half-duplex (semidúplex)**: bidireccional pero no simultánea (walkie-talkie).
- **Full-duplex (dúplex)**: bidireccional y simultánea (telefonía, Ethernet conmutada).

### Clasificación de las redes por medios de transmisión

- **Medios guiados**:
    - **Par trenzado**: pares de hilos entrelazados para reducir interferencias; el cableado habitual de las LAN (categorías 5e, 6, 6A).
    - **Cable coaxial**: conductor central con malla de blindaje; usado en las Ethernet antiguas y en las redes de cable (HFC).
    - **Fibra óptica**: transmite pulsos de luz por hilos de vidrio; máxima velocidad y alcance, inmune a interferencias electromagnéticas.
- **Medios no guiados**: **radio** (Wi-Fi, telefonía móvil), **infrarrojos** (línea de visión directa) y **microondas** (radioenlaces y satélites).

## Redes de área local: VLAN y DMZ

Las LAN actuales son casi universalmente redes **Ethernet conmutadas** en topología de estrella, segmentadas de forma lógica mediante VLAN y protegidas con zonas perimetrales (DMZ).

### Ethernet (IEEE 802.3)

- Tecnología estándar de las redes de área local cableadas, normalizada como **IEEE 802.3**.
- **Direcciones MAC de 48 bits**: identificador físico de cada tarjeta, grabado por el fabricante (los primeros 24 bits, OUI, identifican al fabricante).
- **Método de acceso clásico: CSMA/CD** (*Carrier Sense Multiple Access with Collision Detection*): escuchar antes de transmitir y detectar colisiones en el medio compartido. Hoy es historia: en las redes **conmutadas full-duplex** cada puerto del switch es un enlace dedicado sin colisiones.
- **Velocidades**: **10 Mbps** (Ethernet), **100 Mbps** (Fast Ethernet), **1 Gbps** (Gigabit), **10 Gbps**, y **25/40/100 Gbps** en centros de datos y troncales.
- **Dominios**: el **switch** separa dominios de **colisión** (uno por puerto); el **router**, y también las VLAN, separan dominios de **difusión** (broadcast).

### VLAN (IEEE 802.1Q)

- Una **VLAN** (*Virtual LAN*) divide lógicamente un mismo switch (o conjunto de switches) en varias redes independientes: los equipos de VLAN distintas no se comunican entre sí aunque compartan la electrónica física.
- **Etiquetado 802.1Q**: inserta en la trama Ethernet una etiqueta de **4 bytes** cuyo identificador de VLAN (**VLAN ID, 12 bits**) admite hasta **4094 VLAN**.
- **Tipos de asignación**: **estática o por puerto** (cada puerto pertenece a una VLAN) o **dinámica** (según la MAC o la autenticación del equipo, p. ej. con 802.1X, tema 79).
- **Tipos de enlaces**: de **acceso** (transportan una sola VLAN, hacia los equipos) y **troncales (trunk)** (transportan varias VLAN etiquetadas entre switches; la **VLAN nativa** viaja sin etiquetar).
- **Comunicación entre VLAN**: requiere un dispositivo de capa 3: un router (*router-on-a-stick*) o un **switch de capa 3**.
- **Ventajas**: segmentación y seguridad (aísla departamentos, invitados, VoIP), dominios de difusión más pequeños y flexibilidad (mover un usuario de red sin recablear).

### DMZ (zona desmilitarizada)

- Segmento de red intermedio entre la red interna y el exterior donde se ubican los **servicios expuestos a Internet** (web, correo, DNS público).
- **Arquitectura**: entre dos cortafuegos (uno frente a Internet y otro frente a la red interna) o en una **tercera interfaz** de un mismo cortafuegos.
- **Principio**: desde la DMZ **no se permite iniciar conexiones hacia la red interna**; si un servidor expuesto se ve comprometido, el atacante no alcanza la red corporativa. Las arquitecturas de cortafuegos se desarrollan en el tema 79.
- Las LAN inalámbricas (**WLAN**, familia IEEE 802.11/Wi-Fi) se estudian en el tema 76, y su seguridad en el 75.

## Redes de área extensa (WAN)

Las redes de área extensa interconectan redes de ámbito menor (LAN, MAN) a través de grandes distancias, permitiendo la comunicación entre sedes y el acceso global a Internet. Pueden ser **privadas** (contratadas por la organización a un operador) o **públicas** (la propia Internet, a través de un ISP). La mayoría de los enlaces WAN son **punto a punto** entre dos ubicaciones.

### Infraestructura de una WAN

- **Equipamiento local del cliente (CPE)**: dispositivos y cableado en las instalaciones del cliente.
- **DTE (equipo terminal de datos)**: los equipos del cliente que generan y consumen los datos (routers, ordenadores).
- **DCE (equipo de comunicación de datos)**: la interfaz con la red del proveedor (módems, unidades CSU/DSU).
- **Punto de demarcación**: límite físico que separa la responsabilidad del cliente y la del operador.
- **Bucle local (última milla)**: la conexión física entre el CPE y la central del proveedor.
- **Central del operador (CO)** y **red troncal**: las instalaciones y enlaces interurbanos del proveedor.

### Técnicas de conmutación

- **Conmutación de circuitos**: se establece y reserva un circuito dedicado durante toda la comunicación (red telefónica tradicional).
- **Conmutación de paquetes**: los datos se dividen en paquetes que comparten la red y pueden seguir rutas distintas; se reensamblan en destino (Internet).
- **Conmutación de mensajes**: cada nodo almacena y reenvía el mensaje completo (*store and forward*); en desuso.

### Tecnologías de acceso y transporte WAN

- **Líneas dedicadas**: enlaces punto a punto permanentes y exclusivos, con ancho de banda garantizado. Sus protocolos de enlace clásicos son:
    - **PPP (Point-to-Point Protocol)**: multiprotocolo, con autenticación **PAP** (contraseña en claro) o **CHAP** (desafío-respuesta), compresión y detección de errores.
    - **HDLC (High-Level Data Link Control)**: protocolo orientado a bits para enlaces síncronos, con control de flujo y de errores; base de muchos protocolos de enlace posteriores (incluido PPP).
- **MPLS (Multiprotocol Label Switching)**: conmuta los paquetes según **etiquetas** cortas asignadas en el ingreso a la red, en lugar de consultar la dirección IP en cada salto (se le llama de «capa 2,5»). Es la base de las **VPN de nivel 3** de operador que interconectan sedes, con ingeniería de tráfico y calidad de servicio.
- **Ethernet WAN (metro Ethernet)**: extiende Ethernet sobre la fibra del operador para enlaces metropolitanos de alta velocidad.
- **Banda ancha sobre el bucle local**: **DSL** (sobre el par de cobre telefónico), **cable** (sobre la red HFC de televisión, estándar DOCSIS) y **FTTH** (fibra hasta el hogar, con redes ópticas pasivas GPON), hoy la tecnología dominante en España.
- **Acceso inalámbrico**: **VSAT** (terminales de satélite, para zonas remotas) y **datos móviles** 4G/5G, incluido el acceso fijo inalámbrico (las generaciones móviles se estudian en el tema 76).
- **SD-WAN**: gestión centralizada por software de múltiples enlaces WAN (MPLS, fibra, 4G/5G), seleccionando el camino según la aplicación (se estudia en el tema 73).
- **Tecnologías legadas**, hoy retiradas o residuales pero preguntables:

| Tecnología | Características | Conmutación |
| --- | --- | --- |
| **Dial-up** | Acceso telefónico con módem analógico, máx. 56 kbps | Circuitos |
| **RDSI (ISDN)** | Voz y datos digitales sobre la línea telefónica (2B+D: 2×64 + 16 kbps) | Circuitos |
| **X.25** | Circuitos virtuales con corrección de errores salto a salto; lenta pero robusta; abarca las capas **1 a 3** | Paquetes |
| **Frame Relay** | Sucesora de X.25, menor sobrecarga; cada circuito virtual se identifica por un **DLCI** local; capa de enlace | Paquetes |
| **ATM** | **Celdas de tamaño fijo de 53 bytes** (48 de datos + 5 de cabecera) sobre canales y trayectos virtuales; pensada para voz, vídeo y datos | Celdas |
| **WiMAX (802.16)** | Acceso inalámbrico metropolitano de banda ancha; desplazada por 4G/5G | Paquetes |

## Direccionamiento IP y subredes

Una dirección IPv4 son **32 bits** divididos en dos partes: la que identifica la **red** y la que identifica el **host** dentro de ella. La **máscara de red** marca esa frontera: sus bits a 1 señalan la parte de red (255.255.255.0 o, en notación de prefijo, **/24**).

- **Clases de direcciones** (direccionamiento con clase, hoy sustituido por CIDR pero aún preguntable):

| Clase | Primer octeto | Máscara por defecto | Uso |
| --- | --- | --- | --- |
| **A** | 1-126 (empieza por 0) | 255.0.0.0 (**/8**) | Redes enormes: 126 redes de **16,7 millones** de hosts |
| **B** | 128-191 (empieza por 10) | 255.255.0.0 (**/16**) | Redes medianas: 16 384 redes de **65 534** hosts |
| **C** | 192-223 (empieza por 110) | 255.255.255.0 (**/24**) | Redes pequeñas: 2 millones de redes de **254** hosts |
| **D** | 224-239 | (no aplica) | **Multicast** |
| **E** | 240-255 | (no aplica) | Experimental |

- **Direcciones especiales**:
    - **Dirección de red**: todos los bits de host a 0; identifica la subred y no es asignable.
    - **Dirección de broadcast**: todos los bits de host a 1; difusión a toda la subred.
    - **Loopback**: la red 127.0.0.0/8 (típicamente **127.0.0.1**) apunta al propio equipo (por eso la clase A llega a 126).
    - **APIPA (link-local)**: 169.254.0.0/16, autoasignada cuando falla DHCP.
    - **Direcciones privadas (RFC 1918)**, no enrutables en Internet: **10.0.0.0/8**, **172.16.0.0/12** y **192.168.0.0/16**.
- **CIDR (Classless Inter-Domain Routing)**: elimina las clases y permite prefijos de cualquier longitud (/n = número de bits de red), lo que aprovecha mejor el espacio y permite **agregar rutas** (superredes). **VLSM** aplica la misma idea dentro de una organización: subredes de distinto tamaño según las necesidades de cada segmento.
- **Subnetting**: tomar prestados **n bits** de la parte de host crea **2^n subredes**; con **h** bits de host restantes, cada subred tiene **2^h - 2** direcciones útiles (se descuentan la de red y la de broadcast).
- **NAT/PAT**: la traducción de direcciones de red permite que una red privada salga a Internet con una o pocas IP públicas; **PAT** (NAT con sobrecarga) multiplexa muchas conexiones sobre una sola IP distinguiéndolas por el puerto. Ha sido el gran paliativo del agotamiento de IPv4.
- **Direccionamiento IPv6** (tema 70): prefijos habituales **/64** por subred; direcciones **link-local** (fe80::/10, autoconfiguradas en cada interfaz), **ULA** (fc00::/7, el equivalente a las privadas), **unicast globales** (2000::/3) y **multicast** (ff00::/8); no existe el broadcast.

## Caso práctico: cálculo de subredes

**Enunciado**: dividir la red **192.168.48.0** con máscara **255.255.255.0** en **4 subredes**.

- **Bits necesarios**: para obtener 4 subredes se aplica **2^n ≥ 4**, de donde **n = 2**: se toman **2 bits** prestados de la parte de host.
- **Nueva máscara**: la original es **/24** (255.255.255.0); al añadir 2 bits de subred pasa a **/26**, es decir, **255.255.255.192** (los dos primeros bits del último octeto a 1: 11000000 en binario = 192).
- **Direcciones por subred**: quedan **8 - 2 = 6 bits** de host, luego cada subred tiene **2^6 = 64** direcciones.
- **Direcciones útiles por subred**: de esas 64 se reservan 2 (la dirección de red y la de broadcast): **62 hosts** por subred.
- **Rangos resultantes** (las subredes van de 64 en 64):

| Subred | Rango | Hosts útiles | Broadcast |
| --- | --- | --- | --- |
| 1 | 192.168.48.**0** - 63 | .1 a .62 | .63 |
| 2 | 192.168.48.**64** - 127 | .65 a .126 | .127 |
| 3 | 192.168.48.**128** - 191 | .129 a .190 | .191 |
| 4 | 192.168.48.**192** - 255 | .193 a .254 | .255 |

La primera dirección de cada rango (.0, .64, .128, .192) es la de identificación de la subred y la última (.63, .127, .191, .255) la de broadcast: ninguna de las dos se asigna a hosts.

## Fuentes {.unnumbered .unlisted}

- IEEE 802.3 (Ethernet) e IEEE 802.1Q (VLAN).
- RFC 950 (subredes, 1985), RFC 1918 (direccionamiento privado, 1996) y RFC 4632 (CIDR, 2006), IETF.
- RFC 1661 (PPP, 1994) y RFC 3031 (arquitectura MPLS, 2001), IETF.
