# Seguridad en las comunicaciones

La seguridad en las comunicaciones protege la confidencialidad, la integridad y la disponibilidad de los datos durante su transmisión por las redes. Se articula en capas complementarias: la defensa del perímetro (cortafuegos, IDS/IPS, anti-DDoS), el control de quién accede y qué puede hacer (AAA, NAC), la protección del medio inalámbrico y el cifrado del canal para el acceso remoto (VPN e IPsec).

## Seguridad perimetral: NGFW, IDS/IPS y anti-DDoS

La **seguridad perimetral** agrupa las medidas desplegadas en la frontera entre la red interna y las redes externas no confiables, como Internet. Su objetivo es que solo los flujos autorizados atraviesen el perímetro, detectando y bloqueando el resto.

**Principales amenazas en redes** que estas medidas afrontan:

- **Escucha (*eavesdropping*)**: interceptación pasiva de comunicaciones sin consentimiento de las partes.
- **Man-in-the-middle**: el atacante se interpone en la comunicación y puede leer, insertar y modificar los datos.
- **Repetición (*replay*)**: reutilización maliciosa de una transmisión válida capturada previamente.
- **Suplantación (*spoofing*)**: falsificación de datos (dirección IP, MAC, DNS) para hacerse pasar por otra entidad.
- **Degradación (*downgrade* o *fallback*)**: se fuerza a la comunicación a usar un modo menos seguro (por ejemplo, una versión antigua del protocolo) mantenido por retrocompatibilidad.
- **Denegación de servicio (DoS/DDoS)**: dejar un servicio inaccesible para los usuarios legítimos agotando su ancho de banda o sus recursos; en la variante **distribuida (DDoS)** el ataque procede de miles de equipos coordinados (*botnets*). El ataque *smurf* (ping a direcciones *broadcast* con IP de origen falsificada) es el ejemplo clásico de amplificación.
- **Evasión de la detección**: ataques de **inserción** (aprovechan que el IDS es menos estricto que el sistema final) y de **fragmentación** (trocean los datagramas para ocultar la firma del ataque).
- **Malware**: software malicioso introducido a través de la red (correo, descargas, movimiento lateral).

### Cortafuegos (firewalls)

Un **cortafuegos** es el dispositivo o programa que bloquea los accesos no autorizados entre redes y permite las comunicaciones autorizadas, aplicando una política de seguridad. Tipos, según la capa en la que inspeccionan y su generación:

- **Filtrado de paquetes (*stateless*)**: capa de red; decide paquete a paquete según direcciones IP, protocolo y puertos. Rápido pero ciego al contexto.
- **Inspección de estado (*stateful*)**: capa de transporte; mantiene una tabla de las conexiones establecidas y solo admite el tráfico coherente con una sesión legítima (TCP o UDP).
- **Pasarela de aplicación (*proxy*)**: capa de aplicación; entiende el protocolo (HTTP, FTP, DNS) e inspecciona su contenido, pudiendo filtrar por URL o detectar abusos del protocolo por puertos no estándar. El **WAF** es su caso particular para aplicaciones web (véase el tema de desarrollo seguro).
- **Cortafuegos personal**: software en el equipo del usuario que filtra sus propias comunicaciones.
- **UTM (*Unified Threat Management*)**: un único dispositivo que concentra cortafuegos, antivirus, antispam, IDS/IPS y filtrado de contenidos; orientado a **pymes** por su gestión simplificada.
- **NGFW (*Next-Generation Firewall*)**: evolución del cortafuegos de estado con **inspección profunda de paquetes (DPI)** hasta la capa de aplicación, IDS/IPS integrado en tiempo real, control por aplicación y por usuario (no solo por puerto), prevención de amenazas e inteligencia de amenazas actualizada; orientado a grandes organizaciones.

**Topologías de despliegue**:

- **Bastion host**: host **expuesto y endurecido** (bastionado) que concentra los accesos desde la red no confiable; al estar reforzado, asume el riesgo de la exposición.
- **Screening router**: encaminador con filtrado de paquetes entre la red interna y el exterior.
- **Dual-homed host**: bastión con **dos interfaces de red** (interna y externa) y el reenvío IP desactivado: todo el tráfico debe pasar por sus servicios *proxy*.
- **Screened host**: combina un router de filtrado con un bastión, que es el único nodo interno accesible desde Internet.
- **Screened subnet (DMZ)**: sitúa una **subred intermedia (zona desmilitarizada)** entre la red externa y la interna, delimitada por dos niveles de filtrado; en ella se alojan los servicios públicos (web, correo, DNS). Es la topología más utilizada.

**Complementos del perímetro**:

- **NAT (*Network Address Translation*)**: traduce las direcciones internas a una o varias direcciones públicas, ocultando el direccionamiento interno al exterior.
- **Políticas de cortafuegos**: **restrictiva** (se deniega todo salvo lo explícitamente permitido; más segura y la recomendada) o **permisiva** (se permite todo salvo lo denegado).

### Detección y prevención de intrusiones (IDS/IPS)

- **IDS (*Intrusion Detection System*)**: analiza la actividad de la red o de un sistema para identificar accesos no autorizados y actividades maliciosas, y genera alertas. Tipos:
    - **NIDS** (de red): supervisa el tráfico entrante y saliente de un segmento de red.
    - **HIDS** (de host): supervisa un sistema concreto: integridad de ficheros, detección de *rootkits*, monitorización de registros.
- **IPS (*Intrusion Prevention System*)**: además de detectar, **bloquea en línea** los intentos de intrusión sin intervención del operador. Tipos: **NIPS** (red), **WIPS** (redes inalámbricas), **NBA** (análisis de comportamiento de red: malware, DDoS) y **HIPS** (host).
- **Métodos de detección**: por **firmas** (patrones de ataques conocidos, actualizados automáticamente), por **anomalías** (desviaciones respecto del comportamiento normal aprendido) y por **políticas** (actividades declaradas aceptables por el administrador).
- **Honeypot**: señuelo dispuesto para atraer a los atacantes, detectar los ataques y recabar información sobre sus técnicas sin exponer sistemas reales. Una **honeynet** es una red señuelo completa de alta interacción.

Las alertas de IDS/IPS y honeypots se centralizan en el SIEM del SOC para su correlación (véase el tema de gestión de ciberincidentes).

### Protección frente a la denegación de servicio

Los sistemas **anti-DDoS** protegen los servicios frente a ataques de denegación de servicio, que pueden ser **volumétricos** (saturan el ancho de banda), **de protocolo** (agotan recursos de red, como el SYN flood) o **de aplicación** (agotan el servidor con peticiones aparentemente legítimas). Medidas habituales:

- **Capacidad y redundancia** suficientes para absorber picos.
- **Detección y filtrado** del tráfico de ataque conocido (limitación de tasa, listas de reputación).
- **Mitigación en el proveedor** (filtrado *upstream* en el ISP) o mediante **centros de limpieza de tráfico** (*scrubbing centers*) y redes de distribución (CDN) con *anycast*.
- **Procedimientos** para evitar denegaciones autoinfligidas por errores de configuración.

## Autenticación, autorización y accounting (AAA)

El control de acceso a sistemas y redes se articula en el modelo **AAA**:

- **Autenticación**: verificar la identidad de quien solicita acceso («¿quién eres?»).
- **Autorización**: determinar qué recursos y operaciones puede usar la identidad verificada («¿qué puedes hacer?»).
- **Accounting (registro y auditoría)**: registrar todos los accesos y acciones realizados, autorizados o no, para su trazabilidad y rendición de cuentas («¿qué has hecho?»).

**Factores de autenticación**: la identidad puede probarse con **algo que se sabe** (contraseña, PIN), **algo que se tiene** (tarjeta, certificado, generador de códigos OTP) o **algo que se es** (biometría: huella, rostro). La **autenticación multifactor (MFA)** combina dos o más factores de naturaleza distinta y es la práctica recomendada; los códigos por SMS se consideran el segundo factor más débil (duplicado de SIM).

**Protocolos y servicios AAA**: centralizan la autenticación de los accesos a la red y a los equipos:

| | RADIUS | TACACS+ |
| --- | --- | --- |
| Transporte | UDP, puertos **1812** (autenticación y autorización) y **1813** (*accounting*) | TCP, puerto **49** |
| Cifrado | Solo el atributo de contraseña (con MD5 y secreto compartido); el resto viaja en claro | Todo el cuerpo del paquete |
| Funciones AAA | Autenticación y autorización combinadas | Las tres funciones separadas |
| Uso típico | Acceso a la red: wifi corporativa (802.1X), VPN, ISP | Administración de dispositivos de red |

- **RADIUS (*Remote Authentication Dial-In User Service*)**: protocolo cliente-servidor sin estado; el cliente (punto de acceso, servidor VPN) reenvía las credenciales al servidor RADIUS, que responde con paquetes **Access-Accept**, **Access-Reject** o **Access-Challenge** (solicita información adicional) a cada **Access-Request**. Soporta métodos PAP, CHAP y EAP.
- **DIAMETER**: evolución de RADIUS sobre TCP/SCTP, usada en redes de operador.
- **Métodos de autenticación**: **PAP** (envía la contraseña en claro; inseguro), **CHAP** (desafío-respuesta, la contraseña no viaja) y **EAP** (*Extensible Authentication Protocol*, marco extensible que admite certificados, tarjetas inteligentes o SIM).
- **Kerberos**: autenticación basada en **tickets** emitidos por un centro de distribución de claves (**KDC**, con servidor de autenticación y de concesión de tickets); las contraseñas nunca viajan por la red. Es la base de la autenticación en dominios Windows (Active Directory). Puerto **88**.
- **LDAP (*Lightweight Directory Access Protocol*)**: protocolo de acceso a directorios (puerto **389**; **LDAPS** cifrado, **636**) que actúa como repositorio centralizado de identidades, credenciales y grupos.

**Single Sign-On (SSO)**: mecanismo por el que una única autenticación da acceso a múltiples sistemas y aplicaciones, sin repetir credenciales. Mejora la experiencia de usuario y concentra el control (y también el riesgo: la cuenta SSO debe protegerse con MFA). En su variante **federada**, la identidad autenticada por un **proveedor de identidad (IdP)** es aceptada por los **proveedores de servicio (SP)** de otros dominios. Estándares:

- **SAML 2.0**: federación de identidades basada en XML, habitual en aplicaciones corporativas y administraciones.
- **OAuth 2.0**: **autorización delegada** (conceder a una aplicación acceso limitado a recursos de otra sin cederle las credenciales).
- **OpenID Connect**: capa de **autenticación** construida sobre OAuth 2.0, habitual en servicios web y móviles.

**Modelos de control de acceso** (cómo se deciden las autorizaciones):

- **DAC (discrecional)**: el **propietario** de cada recurso decide quién accede y con qué permisos.
- **MAC (obligatorio)**: una política central e inmodificable por los usuarios asigna **etiquetas** de clasificación a sujetos y objetos y decide los accesos comparándolas; propio de entornos de alta seguridad.
- **RBAC (basado en roles)**: los permisos se asignan a **roles** y los usuarios reciben roles; simplifica la administración y es el modelo más extendido en las organizaciones.
- **ABAC (basado en atributos)**: las reglas evalúan **atributos** del usuario, del recurso y del contexto (horario, ubicación, dispositivo); es el más flexible y granular.

La **gestión de identidades y accesos (IAM)** integra todo lo anterior: ciclo de vida de las cuentas (alta, cambios, baja), aprovisionamiento automático, directorio centralizado, esquema único de autorizaciones y revisión periódica de permisos.

## Control de acceso a la red (NAC) y seguridad inalámbrica

### Control de acceso a la red (NAC)

El **NAC (*Network Access Control*)** comprueba que un dispositivo cumple los requisitos corporativos de configuración y seguridad **antes** de admitirlo en la red (antivirus activo, parches al día, configuración correcta), impidiendo el acceso de equipos contaminados, desactualizados o no confiables. Además, permite aplicar políticas granulares: qué dispositivos y usuarios acceden, a qué recursos y en qué condiciones (por ejemplo, enviar a una red de cuarentena al que no cumple).

- **Implementación *out-of-band***: el NAC no está en el camino del tráfico; despliegue rápido, sin punto único de fallo ni latencias añadidas.
- **Implementación *in-band* (o *in-line*)**: el NAC está en el camino del tráfico; mejor control y capacidad de restringir en tiempo real a quien viole las políticas.
- **Herramientas complementarias**: gestión de parches, escáneres de vulnerabilidades y sistemas de prevención de intrusiones.

### IEEE 802.1X

**802.1X** es el estándar de **control de acceso a la red basado en puertos**: el puerto (físico del switch o asociación inalámbrica) queda bloqueado hasta que el dispositivo se autentica. Intervienen tres roles:

- **Suplicante**: el software del dispositivo que solicita el acceso.
- **Autenticador**: el switch o punto de acceso que bloquea o abre el puerto.
- **Servidor de autenticación**: normalmente un servidor **RADIUS** que valida las credenciales.

El intercambio usa **EAP** (encapsulado como EAPOL en la red local); los métodos habituales son **EAP-TLS** (certificados en cliente y servidor, el más robusto), **PEAP** y **EAP-TTLS** (túnel TLS que protege credenciales internas).

### Seguridad de redes inalámbricas

Las redes wifi difunden la señal por un medio compartido y accesible desde el exterior, por lo que exigen autenticación y cifrado robustos. El **SSID** es el nombre que identifica la red. Evolución de los protocolos de seguridad:

| Protocolo | Cifrado | Estado |
| --- | --- | --- |
| **WEP** (1999) | RC4 con claves de 64/128 bits (40/104 efectivos) | **Roto**: no debe usarse bajo ningún concepto |
| **WPA** (2003) | TKIP sobre RC4 (transitorio, sin cambiar hardware WEP) | **Obsoleto**: TKIP está desaconsejado y deprecado |
| **WPA2** (2004) | **AES-CCMP** (implementa completo el estándar IEEE 802.11i) | Mínimo aceptable; vulnerable a **KRACK** (2017) sin parchear |
| **WPA3** (2018) | AES; **SAE** en Personal; modo de **192 bits** con GCMP-256 en Enterprise | **Recomendado** |

- **Modos Personal y Enterprise**: en **WPA2/WPA3-Personal** todos comparten una clave (**PSK**); en **WPA2/WPA3-Enterprise** cada usuario se autentica individualmente contra un servidor **RADIUS** vía **802.1X**.
- **Mejoras de WPA3**: sustituye el intercambio PSK por **SAE** (*Simultaneous Authentication of Equals*), que impide los ataques de diccionario *offline* contra la contraseña y aporta ***forward secrecy*** (el tráfico capturado no puede descifrarse aunque después se obtenga la clave); añade cifrado individualizado en redes abiertas (*Wi-Fi Enhanced Open*) y un modo **Enterprise de 192 bits** (GCMP-256) para redes que tratan información sensible.
- **Prácticas recomendadas** (guía INCIBE): cambiar las contraseñas por defecto del router y de la red; cifrado **WPA2 o WPA3** (nunca WEP); mantener actualizado el firmware; **desactivar WPS**, UPnP y la administración remota; habilitar una red separada para invitados; revisar periódicamente los dispositivos conectados.

## Acceso remoto seguro: VPN e IPsec

### Redes privadas virtuales (VPN)

Una **VPN (*Virtual Private Network*)** extiende de forma segura una red privada sobre una red pública o no confiable, como Internet: establece un **túnel** cifrado por el que los dispositivos se comunican como si estuvieran conectados a la red privada, conservando sus políticas de seguridad y gestión. Debe garantizar autenticación y autorización, integridad, confidencialidad, no repudio, control de acceso y registro de la actividad.

- **Elementos** (CCN-STIC 836): el **servidor, concentrador o gateway VPN** (establece los túneles; puede ser un equipo dedicado o integrarse en un router o cortafuegos) y el **cliente VPN** (software del dispositivo de usuario).
- **Tunneling**: encapsulación de un protocolo de red dentro de otro, creando el túnel que simula una conexión punto a punto sobre la red pública.

**Escenarios de uso** (CCN-STIC 836):

- **VPN site-to-site**: protege las comunicaciones **entre dos redes** (sedes) a través de la red pública, con un servidor VPN en cada extremo; los equipos cliente no necesitan software VPN. Alternativa más económica y segura que una WAN dedicada.
- **VPN de acceso remoto**: protege la comunicación **entre un equipo individual y la red interna**; el cliente lleva software VPN configurado y se autentica antes de acceder (en las VPN SSL/TLS puede bastar el navegador). Es el escenario del teletrabajo.
- **VPN de equipo a equipo**: conexión segura **entre dos equipos**, extremo a extremo; típica para administrar servidores con protocolos inseguros o situados en redes de riesgo, como la DMZ.
- **VPN en la nube**: da acceso a los recursos de la organización y a sus servicios desplegados en la nube.

**Tecnologías VPN según la capa** en la que operan (CCN-STIC 836):

- **Nivel de aplicación**: túneles **SSH**, que suelen actuar como *proxy* de aplicaciones concretas.
- **Nivel de transporte**: VPN basadas en **TLS** (las «VPN SSL»), de despliegue sencillo para acceso remoto.
- **Nivel de red**: **IPsec** y **WireGuard**; protegen todo el tráfico IP con independencia de la aplicación, aunque solo redes IP. Son las habituales en túneles corporativos.
- **Nivel de enlace**: **MACsec** (IEEE 802.1AE), para proteger tramas Ethernet en la LAN o entre centros de datos.
- **Protocolos históricos**: PPP como base de las conexiones punto a punto; **PPTP**, ya **inseguro** y descartado; **L2TP**, que al carecer de cifrado propio se combina con IPsec (**L2TP/IPsec**).

**Despliegue seguro de una VPN** (proceso de la CCN-STIC 836): identificación de necesidades y requisitos, diseño, selección del producto (para el ámbito ENS, productos del **Catálogo de Productos y Servicios de Seguridad TIC, CPSTIC**, según la categoría del sistema), pruebas de la solución, implantación y despliegue, y operación y mantenimiento, con algoritmos criptográficos acreditados por el CCN.

### IPsec

**IPsec** es el estándar del IETF de seguridad en la **capa de red**: protege los paquetes IP de forma **transparente para las aplicaciones**, ofreciendo autenticación, confidencialidad, integridad y protección anti-repetición (*anti-replay*).

**Protocolos que lo componen**:

- **AH (*Authentication Header*, RFC 4302)**: proporciona **integridad y autenticación del origen** de los paquetes, sin confidencialidad. Es el **protocolo IP 51** (no un puerto).
- **ESP (*Encapsulating Security Payload*, RFC 4303)**: proporciona **confidencialidad, integridad y autenticación**; es el **protocolo IP 50** y la opción recomendada.
- **IKE (*Internet Key Exchange*)**: negocia la autenticación de los extremos, el intercambio de claves y las **asociaciones de seguridad (SA)** que fijan los parámetros del túnel. Usa **UDP 500** (y **UDP 4500** con **NAT-T**, el mecanismo de NAT *traversal* de la RFC 3947). Existen **IKEv1 e IKEv2 (RFC 7296)**: debe usarse **IKEv2**, con ***Perfect Forward Secrecy* (PFS)** activado para que el compromiso de una clave no exponga las sesiones anteriores.
- **IPComp**: compresión de los datos previa al cifrado.

**Modos de funcionamiento**:

- **Modo transporte**: cifra solo la **carga útil** del paquete IP; se usa entre equipos finales.
- **Modo túnel**: cifra el **paquete IP completo** (cabeceras incluidas) y lo encapsula en uno nuevo; es el modo habitual en VPN entre pasarelas.

### Otros protocolos de acceso remoto

- **SSH (*Secure Shell*)**, TCP **22**: acceso remoto cifrado a consola; sustituye a Telnet, admite autenticación por clave pública y permite túneles y reenvío de puertos.
- **Telnet**, TCP **23**: terminal remota **sin cifrar** (credenciales en claro); no debe usarse.
- **RDP (*Remote Desktop Protocol*)**, TCP **3389**: escritorio remoto gráfico de Microsoft; no debe exponerse directamente a Internet, sino publicarse a través de VPN o de una pasarela con MFA.
- **VNC (protocolo RFB)**: control remoto gráfico multiplataforma, viendo la pantalla del equipo distante.

## Fuentes {.unnumbered .unlisted}

- CCN-STIC 836, Seguridad en redes privadas virtuales (VPN) (ed. febrero 2022; edición vigente verificada en ccn-cert.cni.es en julio de 2026).
- INCIBE, Seguridad en redes wifi: una guía de aproximación para el empresario (2019).
- RFC 4302 (AH), RFC 4303 (ESP), RFC 7296 (IKEv2), RFC 3947 (NAT-T) y RFC 2865/2866 (RADIUS), IETF.
- Wi-Fi Alliance, especificaciones WPA2/WPA3 (wi-fi.org, consultado el 13 de julio de 2026).
- IEEE 802.1X (control de acceso basado en puertos) e IEEE 802.11i (seguridad de redes inalámbricas).
