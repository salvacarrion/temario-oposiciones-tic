# Seguridad en las comunicaciones

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Seguridad en las Comunicaciones

La seguridad en las comunicaciones protege la integridad, confidencialidad y disponibilidad de los datos durante su transmisión a través de redes. Incluye medidas, políticas y tecnologías que mitigan riesgos y previenen accesos no autorizados.

### Seguridad Perimetral

La seguridad perimetral se refiere a las medidas implementadas en los bordes de una red para protegerla de accesos no autorizados. Un ejemplo común son los **firewalls**, que actúan como barreras entre redes internas seguras y redes externas potencialmente peligrosas, como Internet.

### Sistemas Cortafuegos (Firewalls)

Los firewalls son dispositivos o programas diseñados para bloquear el acceso no autorizado, permitiendo al mismo tiempo comunicaciones autorizadas. Funcionan como un mecanismo para bloquear y permitir el tráfico según políticas de seguridad establecidas.

### Clasificación de Cortafuegos

- **Cortafuegos de red o de filtrado de paquetes**: Deniegan o permiten el flujo de tramas entre dos redes basándose en criterios como direcciones IP y números de puertos.
- **Cortafuegos de estado**: Mantienen un registro de todas las conexiones que pasan a través de ellos, permitiendo decisiones basadas en el estado de la conexión.
- **Cortafuegos de aplicación**: Analizan el tráfico a nivel de aplicación, detectando protocolos no deseados o abusos de protocolos a través de puertos no estándar.

### Tipos de Cortafuegos

- **Nivel de aplicación de pasarela**: Aplica mecanismos de seguridad para aplicaciones específicas consideradas peligrosas (por ejemplo, FTP, Telnet, P2P).
- **Circuito a nivel de pasarela**: Implementa seguridad cuando se establece una conexión TCP o UDP.
- **Cortafuegos de capa de red o de filtrado de paquetes**: Operan a nivel de red, inspeccionando direcciones IP, intercambio de paquetes IP y direcciones MAC.
- **Cortafuegos de capa de aplicación (Application Firewall)**: Adaptan los filtrados a características propias de los protocolos de este nivel, como el filtrado según URL. Un cortafuegos a nivel 7 de HTTP suele denominarse **proxy**.
- **Cortafuegos personal**: Filtra las comunicaciones entre tu ordenador y el resto de la red, proporcionando protección individual.

### Capas de Trabajo de los Cortafuegos

- **Cortafuegos a nivel de red**: Funcionan como un encaminador (router) o computadora especial que examina las características de los paquetes IP para decidir cuáles deben pasar y cuáles no.
- **Cortafuegos a nivel de circuito (Capa de Transporte)**: Analizan la información TCP o UDP para verificar que la solicitud de sesión es legítima.
- **Cortafuegos a nivel de aplicación**: Suelen ser computadoras que ejecutan software de servidor proxy, inspeccionando el contenido de las comunicaciones de aplicaciones específicas.

### Topologías de Cortafuegos

- **Bastion Host**: Es un punto clave de la red donde se instala un firewall en el equipo del usuario, estableciendo una conexión directa desde el usuario (bastión) hacia Internet.
- **Encaminador con filtrado (Screening Router)**: Filtra paquetes y bloquea el tráfico entre redes o nodos específicos. Todas las peticiones de un departamento a Internet pasan por el firewall del router.
    - **Ruta:** Usuarios → Router → Internet
- **Host con doble conexión (Dual-Homed Host)**: Es un servidor bastión con dos tarjetas de red independientes conectadas a la red interna y a Internet, desactivando las funciones de reenvío TCP/IP.
    - **Ruta:** Usuarios → Bastión (2 tarjetas) → Internet
- **Cortafuegos mediante filtrado de Host (Screened Host)**: Combina un bastion host con un router de filtrado. El bastión host es el único nodo de la red accesible desde Internet.
    - **Ruta:** Usuarios → Bastión → Router → Internet
- **Cortafuegos mediante filtrado de subred (Screened Subnet)**: Sitúa una subred entre las redes externa e interna, creando una zona desmilitarizada (DMZ). Es la topología más utilizada actualmente.
    - **Ruta:** Usuarios → Router → Bastión → Router → Internet

### Traducción de Direcciones de Red (NAT)

La NAT se utiliza para ocultar la verdadera dirección de las computadoras conectadas a la red, proporcionando una capa adicional de seguridad al no exponer las direcciones IP internas al exterior.

### Políticas del Cortafuegos

- **Política restrictiva**: Se deniega todo el tráfico excepto el que está explícitamente permitido. Es más segura pero requiere una configuración detallada.
- **Política permisiva**: Se permite todo el tráfico excepto el que esté explícitamente denegado. Es menos segura y se utiliza en entornos que requieren mayor flexibilidad.

### Firewalls UTM (Unified Threat Management)

Los firewalls UTM ofrecen una gestión unificada de amenazas, concentrando en un único dispositivo múltiples funcionalidades de seguridad como firewall, antivirus, antispam, prevención de intrusiones y filtrado de contenido. Están destinados principalmente a **PyMES** que buscan una solución integral y simplificada.

### Firewalls NGFW (Next-Generation Firewall)

Los firewalls de nueva generación son una evolución de los firewalls tradicionales que incluyen características avanzadas como detección y prevención de intrusiones (IDS/IPS), prevención de amenazas (TPS) y gestión de aplicaciones. Están destinados a **grandes organizaciones** que requieren un alto nivel de seguridad y funcionalidades avanzadas.

### Características de los NGFW

- **Inspección del tráfico en varios niveles**: Analizan desde la capa de red hasta la capa de aplicación.
- **Detección y prevención de intrusiones (IDS/IPS) en tiempo real**: Monitorean y bloquean actividades maliciosas instantáneamente.
- **Prevención de amenazas (TPS)**: Identifican y neutralizan amenazas avanzadas como malware y ataques de día cero.
- **Control de aplicaciones y contenido**: Permiten definir políticas basadas en aplicaciones específicas y tipos de contenido.
- **Control de acceso basado en políticas**: Gestionan quién puede acceder a qué recursos y bajo qué condiciones.
- **Visibilidad y análisis de amenazas**: Ofrecen informes detallados y estadísticas para un análisis profundo de la seguridad.

### Dispositivos de Gestión y Control de Tráfico

Estos dispositivos permiten monitorizar y controlar el tráfico de una red, garantizando su rendimiento y seguridad.

### Características

- **Control de acceso**: Regulan quién puede acceder a la red y a qué recursos.
- **Filtrado de paquetes**: Inspeccionan paquetes de datos para permitir o bloquear su paso según criterios definidos.
- **Control de ancho de banda**: Gestionan el uso del ancho de banda para evitar congestiones y priorizar el tráfico esencial.
- **Monitorización del rendimiento**: Supervisan el estado de la red para detectar y resolver problemas proactivamente.

### Dispositivos Comunes

- **Firewalls**: Actúan como barreras de seguridad entre redes.
- **Routers**: Encaminan el tráfico entre redes y pueden incluir funciones de filtrado.
- **Switches**: Conectan dispositivos dentro de una red y pueden implementar políticas de seguridad y segmentación.

### Control de Accesos a Sistemas y Redes

El control de accesos es una tecnología que permite definir de forma granular qué dispositivos y usuarios pueden acceder a la red y a qué recursos, estableciendo políticas de gestión integradas con el sistema de información de la empresa.

### NAC (Network Access Control)

El NAC permite comprobar si una máquina o dispositivo cumple con los requisitos corporativos de configuración y seguridad antes de que acceda a la red. Busca prevenir que dispositivos contaminados, mal configurados o que presenten riesgos potenciales accedan a la red corporativa (por ejemplo, debido a virus, falta de actualizaciones o configuraciones inapropiadas).

### Tipos de Implementaciones de NAC

- **Out of Band**: Permite un despliegue rápido sin interrumpir el uso de la red, elimina un único punto de fallo y reduce el riesgo de crear latencias de red.
- **In-band o In-line**: Ofrece mejor control del tráfico y permite monitorizar y restringir el acceso si los dispositivos admitidos violan las políticas de uso.

### Herramientas Complementarias al NAC

- **Gestión de parches (actualizaciones)**: Asegura que los dispositivos estén actualizados con los últimos parches de seguridad.
- **Escáneres de vulnerabilidades**: Detectan debilidades en los sistemas antes de que puedan ser explotadas.
- **Prevención de intrusos**: Sistemas que identifican y bloquean actividades sospechosas o maliciosas.

### Control de Acceso Informático

El control de acceso informático se basa en tres pilares fundamentales conocidos como **AAA**:

- **Autenticación/Identificación**: Responde a la pregunta "¿Quién puede entrar al sistema?". Es el proceso de intentar verificar la identidad digital del remitente de una comunicación, como una petición para conectarse.
- **Autorización**: Responde a "¿Qué puede hacer el sujeto?". Es el proceso por el cual la red de datos autoriza al usuario identificado a acceder a determinados recursos.
- **Auditoría/Rendición de cuentas**: Responde a "¿Qué ha hecho el sujeto?". Es el proceso por el cual la red o sistemas asociados registran todos y cada uno de los accesos a los recursos que realiza el usuario, sean autorizados o no.

### Servidores y Servicios de AAA

Estos servicios son esenciales para garantizar la seguridad y el cumplimiento de políticas dentro de una red. A través de ellos se gestionan las políticas de autorización y se realiza un seguimiento detallado de las actividades de los usuarios.

## Seguridad en redes inalámbricas

La **seguridad inalámbrica** protege redes Wi-Fi mediante autenticación, cifrado y otras medidas que minimizan riesgos.

### Prácticas Recomendadas:

- Cambiar contraseñas predeterminadas del router y Wi-Fi.
- Configurar cifrado WPA2 o WPA3.
- Actualizar firmware del router.
- Deshabilitar funciones no seguras (WPS, UPnP, administración remota).
- Configurar redes para invitados.

### Autentificación

La autentificación es el acto o proceso de confirmar que alguien es quien dice ser.

### Protocolos de Autenticación:

- **RADIUS:** Ideal para redes empresariales, centraliza la autenticación.
- **Kerberos:** Autenticación segura basada en tickets, sin transmitir contraseñas.

### IEEE 802.1X

IEEE 802.1X es un protocolo de control de acceso a la red basado en puertos. Permite la autenticación de dispositivos conectados a un puerto LAN, estableciendo una conexión punto a punto o previniendo el acceso a través de ese puerto si la autenticación falla.

### SSID (Service Set Identifier)

El SSID es el nombre que tiene la red inalámbrica cuando se accede a ella y sirve para identificarla entre otras redes disponibles.

### Protocolos de Seguridad Inalámbrica

- **WEP (Wired Equivalent Privacy)**: Cifra las comunicaciones en el nivel 2 (Ethernet) utilizando una clave compartida de 64 o 128 bits. Emplea el algoritmo de encriptación **RC4**. Sin embargo, presenta vulnerabilidades conocidas que lo hacen inseguro.
- **WPA (Wi-Fi Protected Access)**: Implementa la mayoría del estándar IEEE 802.11i y fue creado como una medida intermedia para reemplazar a WEP. Utiliza **TKIP** (Temporal Key Integrity Protocol) junto con **RC4** para la encriptación. Si se utilizan contraseñas fuertes (más de 10 caracteres), este protocolo sigue siendo seguro. Adopta la autenticación de usuarios mediante el uso de un servidor donde se almacenan las credenciales y contraseñas de los usuarios de la red.
- **WPA2 (Wi-Fi Protected Access II)**: Completa la implementación del estándar IEEE 802.11i. Emplea **CCMP** (Counter Mode with Cipher Block Chaining Message Authentication Code Protocol) con el algoritmo **AES** (Advanced Encryption Standard) para la encriptación.
    - **WPA2-Personal**: Otorga seguridad a través de una contraseña compartida (PSK).
    - **WPA2-Enterprise**: Autentica a los usuarios a través de un servidor, generalmente utilizando protocolos como RADIUS.
- **WPA3 (Wi-Fi Protected Access III)**: Utiliza claves de encriptación de 128 bits para el modo personal y de 192 bits para el modo empresarial, simplificando la configuración y mejorando la seguridad. Emplea **GCMP-256** (Galois/Counter Mode Protocol con claves de 256 bits) para la encriptación.

### RADIUS (Remote Authentication Dial-In User Service)

RADIUS es un protocolo de autenticación y autorización para aplicaciones de acceso a la red o movilidad IP.

### Características de RADIUS:

- **Protocolo No Orientado a Conexión (Stateless)**: Utiliza **UDP** y no emplea conexiones directas, aunque también puede funcionar con **TCP**.
- **Puerto de Comunicación**: Usa el puerto **1812**.
- **Modelo de Seguridad**: Es punto a punto.
- **Gestión de Sesiones**: Puede manejar sesiones y notificar cuándo comienzan y terminan las conexiones.
- **Mecanismos de Autenticación**: Soporta **PAP** (Password Authentication Protocol) y **CHAP** (Challenge Handshake Authentication Protocol) mediante **PPP** (Point-to-Point Protocol).
- **Protección de Credenciales**: Utiliza **MD5** para ocultar las credenciales transferidas.
- **Modelo AAA**: Implementa el modelo de **Autenticación-Autorización-Auditoría** (AAA).
- **Seguridad del Tráfico**: No emplea mecanismos para evitar la escucha del tráfico (como **TLS**), pero se estima que la aleatorización, unida a contraseñas robustas, dificultan el descifrado de los datos.

### Funcionamiento de RADIUS:

Cuando se realiza la conexión con un ISP mediante módem, DSL, cable módem, Ethernet o Wi-Fi, se envía información de autenticación, generalmente un nombre de usuario y una contraseña. El servidor RADIUS comprueba que la información es correcta utilizando esquemas de autenticación como **PAP**, **CHAP** o **EAP** (Extensible Authentication Protocol). Si es aceptado, el servidor autoriza el acceso al sistema del ISP y asigna recursos de red como una dirección IP y otros parámetros como **L2TP** (Layer 2 Tunneling Protocol).

### Tipos de Paquetes RADIUS:

- **Access-Request**: El cliente solicita autenticación.
- **Access-Accept**: El servidor acepta la solicitud.
- **Access-Reject**: El servidor rechaza la solicitud.
- **Access-Challenge**: El servidor solicita información adicional al cliente.

### Estructura de un Paquete RADIUS:

- **Cabecera (Header)**:
    - **Código**: Indica el tipo de mensaje.
    - **Identificador**: Coincide solicitudes y respuestas.
    - **Longitud**: Especifica el tamaño del paquete.
    - **Autenticador**: Utilizado para la seguridad del paquete.
- **Carga/Datos**:
    - **Atributos**: Contienen información específica de autenticación, autorización y configuración.
    - **Valores**: Datos asociados a cada atributo.

### Sistemas de Autenticación

- **PAP (Password Authentication Protocol)**: Protocolo simple que envía el nombre de usuario y contraseña en texto plano, lo que lo hace menos seguro.
- **CHAP (Challenge Handshake Authentication Protocol)**: Utiliza un mecanismo de desafío-respuesta para autenticar, proporcionando mayor seguridad que PAP.
- **EAP (Extensible Authentication Protocol)**: Protocolo extensible que soporta múltiples métodos de autenticación, como tarjetas inteligentes, certificados y autenticación basada en SIM.

### Relación Señal-Ruido (SNR)

La relación señal-ruido se define como la proporción existente entre la potencia de la señal transmitida y la potencia del ruido que la corrompe. Se mide en **decibelios (dB)**.

- **Fórmula**: SNR = Potencia de la Señal / Potencia del Ruido

### Tasa de Error Binario (BER)

La tasa de error binario se define como el número de bits recibidos de forma incorrecta respecto al total de bits enviados durante un intervalo específico de tiempo.

- **Fórmula**: BER = Bits Recibidos con Errores / Total de Bits Recibidos


## Acceso seguro a redes corporativas

El acceso seguro a redes corporativas permite a los usuarios conectarse de manera protegida a los recursos de una red corporativa desde ubicaciones remotas, garantizando la integridad, confidencialidad y autenticidad de la información transmitida. Esto se logra mediante tecnologías como **VPN** (Virtual Private Network) e **IPSec** (Internet Protocol Security).

### 1. Redes Privadas Virtuales (VPN)

Una **Red Privada Virtual (VPN)** es una tecnología que establece una conexión virtual segura, conocida como "túnel", sobre una red física insegura como Internet. Esta conexión permite que un dispositivo en la red envíe y reciba datos como si estuviera conectado directamente a una red privada, manteniendo la funcionalidad, seguridad y políticas de gestión propias de dicha red.

### Características básicas de las VPN:

- **Autenticación y autorización**: Verificación de la identidad del usuario y control de acceso a los recursos.
- **Integridad**: Garantiza que los datos no sean alterados durante la transmisión.
- **Confidencialidad y privacidad**: Protección de la información para que no pueda ser interceptada ni leída por terceros no autorizados.
- **No repudio**: Evita que una de las partes pueda negar la realización de una transacción.
- **Control de acceso**: Restricción del acceso a los recursos de la red a usuarios autorizados.
- **Auditoría y registro de actividades**: Seguimiento y registro de las acciones realizadas para análisis y cumplimiento normativo.
- **Calidad del servicio**: Asegura un rendimiento adecuado de la red para las aplicaciones críticas.

### Requisitos básicos de una VPN:

- **Identificación de usuario**: Uso de credenciales como nombre de usuario y contraseña.
- **Cifrado de datos**: Protección de la información mediante algoritmos de cifrado simétrico como **DES**, **3DES**, **AES** o el algoritmo **SEAL**, que es más rápido que los anteriores.
- **Administración de claves**: Gestión segura de las claves utilizadas para el cifrado y descifrado de datos.

### Tipos de VPN:

- **VPN site-to-site**: Conexión entre sedes remotas de una organización. Protege las comunicaciones entre dos redes a través de Internet, manteniendo la seguridad y enrutando las comunicaciones.
- **VPN de acceso remoto**: Conexión entre un cliente remoto y la sede de la organización. Protege las comunicaciones entre un equipo individual de usuario y la red interna.
- **VPN de equipo a equipo**: Permite establecer conexiones seguras entre dos equipos, protegiendo el tráfico de extremo a extremo.
- **VPN en la nube**: Permite acceder a los recursos tanto de la organización como de servicios en la nube.

### Tecnologías de VPN:

- **Nivel de aplicación**: VPN basadas en túneles **SSH**, que suelen actuar como proxy.
- **Nivel de transporte**: VPN basadas en **TLS**.
- **Nivel de red**: Implementadas con protocolos como **IPSec** o **WireGuard**.
- **Nivel de enlace**: VPN basadas en **MACsec**.

### Tipos de conexión:

- **Conexión de acceso remoto**: Usuarios que se conectan desde ubicaciones externas.
- **Conexión VPN router a router**: Enlaces seguros entre enrutadores de diferentes sedes.
- **Conexión VPN firewall a firewall**: Túneles establecidos entre cortafuegos.
- **VPN en entornos móviles**: Adaptadas para dispositivos móviles y usuarios en movimiento.

### Enrutador VPN y Concentrador VPN

- **Enrutador VPN**: Un enrutador WiFi con software de cliente VPN instalado, que permite conectar múltiples dispositivos a una VPN.
- **Concentrador VPN**: Dispositivo de red que permite a las personas acceder a una red de forma remota desde cualquier parte del mundo a través de múltiples túneles VPN encriptados entre el dispositivo del usuario y la red. Puede proporcionar túneles VPN seguros para miles de personas al mismo tiempo.

### Funcionamiento de una VPN

Las VPN funcionan estableciendo un proceso llamado **tunneling**. Los paquetes de datos se encapsulan y se enrutan a través de la red pública en un túnel que simula una conexión punto a punto, similar a la de una red de área local (LAN). Esto asegura que los datos viajen de forma segura entre el usuario y la red corporativa.

### Protocolos sobre los que se crea una VPN

- **Nivel 2 (Enlace de datos)**:
    - **PPP (Point-to-Point Protocol)**: Protocolo que establece una conexión directa entre dos nodos sin dispositivos intermedios.
    - **PPTP (Point to Point Tunneling Protocol)**: Protocolo utilizado para soportar VPN sobre PPP. Está limitado a un único túnel y ya no se considera seguro.
    - **L2TP (Layer 2 Tunneling Protocol)**: Mejora sobre PPTP y L2F, utilizado para soportar VPN.
- **Nivel 3 (Red)**:
    - **IPSec (Internet Protocol Security)**: Estándar abierto que proporciona seguridad a las comunicaciones a nivel de red. Opera de forma transparente para las aplicaciones y ofrece autenticación, confidencialidad y protección anti-reenvíos.
- **Nivel 4 (Transporte)**:
    - **SSL/TLS (Secure Sockets Layer/Transport Layer Security)**: Securizan el nivel de transporte, ofreciendo a los protocolos de nivel de aplicación conexiones seguras como HTTPS.

### 2. IPSec

### Características básicas de IPSec:

- **Autenticación**: Verifica la identidad de los participantes.
- **Confidencialidad**: Cifra los datos para evitar accesos no autorizados.
- **Protección anti-reenvíos**: Evita ataques de repetición.
- **Transparencia**: No requiere modificaciones en las aplicaciones.
- **Perfect Forward Secrecy**: Garantiza que la exposición de una clave no comprometa sesiones anteriores.

### Modos de funcionamiento de IPSec:

- **Modo transporte**: Sólo cifra la carga útil del paquete IP.
- **Modo túnel**: Cifra el paquete IP completo, incluyendo encabezados y carga útil. Es el modo más habitual en VPN.

### Protocolos de IPSec:

- **Protocolos de seguridad**:
    - **AH (Authentication Header)**: Proporciona autenticación e integridad de los paquetes IP mediante HMAC. Funciona a nivel IP a través del puerto 51.
    - **ESP (Encapsulating Security Payload)**: Proporciona confidencialidad, integridad y autenticación. Funciona a nivel IP a través del puerto 50 y es el protocolo recomendado.
- **Protocolos de autenticación**:
    - **IKE (Internet Key Exchange)**: Establece el intercambio de claves compartidas o de clave pública entre ambos extremos, permitiendo una asociación de seguridad (SA). Funciona a nivel de transporte a través del puerto 500 de UDP.
- **Protocolos de compresión de datos**:
    - **IPComp**: Comprime los datos antes de su cifrado para optimizar la transmisión.

### Acceso Remoto a Sistemas de Información

Para acceder de forma remota a sistemas de información, se utilizan diversos protocolos y herramientas:

- **TELNET (TELecommunication NETwork)**:
    - **Puerto**: 23.
    - **Plataformas**: UNIX, Linux y Windows.
    - Permite emular una terminal remota.
    - **Características**:
        - No es seguro; las credenciales viajan en texto plano.
        - Requiere un proceso en el servidor para gestionar las conexiones.
        - Los datos se envían/reciben en formato ASCII de 8 bits.
        - Comunicación bidireccional en un entorno cliente-servidor.
- **SSH (Secure Shell)**:
    - **Puerto**: 22.
    - Sustituye a Telnet como método de acceso remoto seguro.
    - Utiliza autenticación por clave pública y establece una conexión encriptada.
- **RDP (Remote Desktop Protocol)**:
    - **Puerto**: 3389.
    - Desarrollado por Microsoft para la comunicación en la ejecución de aplicaciones entre un terminal y un servidor Windows.
    - Permite usar un entorno gráfico.
- **RFB (Remote FrameBuffer Protocol)**:
    - Permite manejar equipos a distancia utilizando el teclado y el ratón, viendo la pantalla remota como si estuviera delante de la máquina.
- **ICA (Independent Computing Architecture)**:
    - Permite ejecutar aplicaciones en un servidor desde un cliente remoto.
    - Es reconocida por su alta velocidad y rendimiento.
- **Otros**:
    - Herramientas como **TeamViewer**, **LogMeIn**, **AnyDesk**, **Remote Desktop** (extensión de Google Chrome), **Ammyy**, entre otras, ofrecen soluciones para el acceso remoto.

### Gestión de Identidades y Accesos

El acceso remoto requiere una autenticación previa para validar quién solicita el acceso. La gestión de identidades y accesos es crucial para mantener la seguridad en las conexiones remotas.

### Funciones:

- **Gestión de cuentas de usuario y contraseñas**: Aplicación de políticas de la empresa para la creación y mantenimiento de cuentas.
- **Gestión centralizada de los permisos de los usuarios**: Basada en directorios de usuarios como **LDAP**.
- **Esquema de autorizaciones**: Centralización de las autorizaciones de acceso en un solo punto.
- **Sistemas de identificación y autenticación única corporativa**: Implementación de **Single Sign-On (SSO)**.

### Mecanismos de autenticación:

- **Usuario y contraseña**: Métodos tradicionales, complementados con sistemas como **Kerberos**, **LDAP** o autenticación biométrica.
- **Certificado digital**: Uso de certificados para verificar la identidad del usuario.
- **Autenticación de múltiple factor**: Combinación de varios métodos para aumentar la seguridad.

### SSO (Single Sign-On)

El **Single Sign-On** es un mecanismo de autenticación que permite a los usuarios acceder a múltiples sistemas y aplicaciones con un único nombre de usuario y contraseña.

### Características:

- **Multiplataforma**: Compatible con diferentes sistemas y aplicaciones.
- **Facilidad de uso**: Reduce la necesidad de recordar múltiples credenciales.
- **Transparente**: El usuario no percibe cambios en su experiencia.
- **Gestión sencilla**: Simplifica la administración de accesos y permisos.
- **Control de acceso**: Mejora el control sobre quién accede a qué recursos.
- **Seguro**: Minimiza riesgos asociados con la gestión de múltiples contraseñas.

### Arquitectura de SSO:

- **Arquitectura simple**: Existe una única autoridad de certificación.
- **Arquitectura compuesta o federación**: Varias autoridades de certificación colaboran para autenticar usuarios en diferentes dominios.

### Tipos de autenticación en SSO:

- **Basada en vales (tokens)**: Utiliza criptografía simétrica para la generación y validación de tokens.
- **Basada en PKI (Public Key Infrastructure)**: Emplea criptografía asimétrica y certificados digitales.
- **Autenticación múltiple mediante cacheo en cliente**: Las credenciales se almacenan temporalmente en el cliente.
- **Autenticación múltiple mediante cacheo en servidor**: Las credenciales se gestionan y almacenan en el servidor.

### Modelos de Autorización de Accesos

El control de acceso es fundamental para proteger los recursos y datos de una organización. Existen varios modelos para gestionar las autorizaciones:

- **Control de Acceso Discrecional (DAC, Discretionary Access Control)**:
    - Método que restringe el acceso a objetos basándose en la identidad de los sujetos.
    - Los propietarios de los recursos deciden quién puede acceder y qué acciones pueden realizar.
- **Control de Acceso Basado en Roles (RBAC, Role-Based Access Control)**:
    - Asigna permisos a los usuarios en función de los roles que desempeñan.
    - Facilita la gestión de permisos al asociarlos a roles en lugar de usuarios individuales.
- **Control de Acceso Obligatorio (MAC, Mandatory Access Control)**:
    - Añade una capa adicional de seguridad mediante el etiquetado de todos los elementos del sistema.
    - Las políticas de control de acceso se aplican en función de estas etiquetas.
    - Los usuarios no pueden modificar los permisos asignados, lo que garantiza un control estricto.
