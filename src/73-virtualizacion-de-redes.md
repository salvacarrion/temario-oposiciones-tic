# Virtualización de redes

La virtualización de redes desacopla los servicios de red del hardware que los soporta: la red deja de ser un conjunto de equipos configurados uno a uno y pasa a definirse, desplegarse y gestionarse por software. Este tema cubre sus dos pilares (las redes definidas por software, SDN, y la virtualización de funciones de red, NFV), su aplicación a la red de área extensa (SD-WAN) y la gestión y administración de red (SNMP). Los dispositivos y tecnologías de red se estudian en el tema [71](71-redes-de-computadores.md), los protocolos en el 66, la seguridad de red en el 75 y las redes 5G (grandes consumidoras de NFV) en el 72.

## Redes definidas por software (SDN)

Virtualizar una red es presentar una vista lógica que difiere de la infraestructura física subyacente: permite **combinar varias redes físicas en una sola red virtual** o, a la inversa, **dividir una red física en varias redes virtuales independientes**, cada una con sus propias características. Se distingue la **virtualización externa** (dispositivos como switches y routers particionan la red física, p. ej. las VLAN del tema [71](71-redes-de-computadores.md)) de la **interna** (redes virtuales dentro de un mismo equipo, p. ej. los switches virtuales de un hipervisor).

Sobre esta idea se construyen las **redes de superposición** (*overlay*): redes virtuales montadas sobre una infraestructura física (*underlay*) que solo aporta conectividad IP. La tecnología de referencia es **VXLAN** (RFC 7348, 2014), que encapsula tramas Ethernet en UDP (puerto **4789**) y sustituye el límite de **4094 VLAN** por un identificador **VNI de 24 bits** (unos **16,7 millones** de segmentos), la base de las redes de los centros de datos y las nubes actuales.

Las **redes definidas por software (SDN)** llevan el desacoplamiento al control de la red: **separan el plano de control** (las decisiones sobre cómo se encamina el tráfico) **del plano de datos** (los dispositivos que reenvían los paquetes) y centralizan el primero en un controlador programable con visión global de la red.

- **Características clave**:
    - **Centralización del control**: una visión global y unificada de la red en el controlador.
    - **Programabilidad**: la red se configura mediante software y API, lo que permite automatizar y adaptar su comportamiento.
    - **Abstracción**: las aplicaciones piden servicios de red sin conocer el detalle físico subyacente.
    - **Separación de planos**: el **plano de control** decide y el **plano de datos** reenvía.
    - **Dinamismo**: políticas y configuraciones ajustables en tiempo real, sin tocar equipo a equipo.

### Arquitectura SDN

La arquitectura se organiza en tres capas conectadas por dos interfaces, y ambas denominaciones son preguntables:

- **Capa de aplicación**: las aplicaciones de red (encaminamiento, balanceo, seguridad, ingeniería de tráfico) que comunican sus necesidades al controlador.
- **Capa de control**: el **controlador SDN**, «cerebro» de la red: mantiene la visión global, toma las decisiones y configura los dispositivos. Plataformas de referencia: **OpenDaylight (ODL)** y **ONOS** (ambas de código abierto), junto a las soluciones comerciales de los fabricantes.
- **Capa de infraestructura**: los dispositivos de reenvío (switches físicos o virtuales) que ejecutan las instrucciones del controlador.
- **Interfaz southbound (hacia abajo)**: comunica el controlador con los dispositivos. El protocolo estándar es **OpenFlow** (ONF; versión vigente **1.5.1, de 2015**), que programa las tablas de flujos de los switches; también se usan NETCONF u OVSDB.
- **Interfaz northbound (hacia arriba)**: expone el controlador a las aplicaciones, habitualmente mediante **API REST**.

- **Modelos de despliegue SDN**:
    - **Abierta**: basada en estándares abiertos (OpenFlow), con dispositivos de cualquier fabricante.
    - **Por API**: el controlador gestiona los dispositivos a través de las API propietarias del fabricante.
    - **De superposición (overlay)**: crea redes virtuales (túneles VXLAN) sobre la red física existente, sin tocarla.
    - **Híbrida**: combina control SDN y protocolos tradicionales en la misma red, lo habitual en las migraciones.

## Virtualización de funciones de red (NFV)

La **virtualización de funciones de red (NFV)** sustituye los equipos de red dedicados (*appliances*: cortafuegos, balanceadores, routers, sondas) por **software que ejecuta las mismas funciones sobre servidores estándar**. La impulsa el **ETSI** desde el *white paper* fundacional de **2012**, firmado por los grandes operadores de telecomunicaciones, y su motivación es económica y operativa: reducir CAPEX y OPEX, acelerar el despliegue de servicios y escalar bajo demanda.

- **Arquitectura de referencia ETSI** (GS NFV 002):
    - **NFVI (NFV Infrastructure)**: la infraestructura física (cómputo, almacenamiento y red) más la capa de virtualización (hipervisor) que la abstrae.
    - **VNF (Virtualised Network Function)**: cada función de red implementada en software (un cortafuegos virtual, un balanceador, el core de una red móvil).
    - **NFV MANO (Management and Orchestration)**: la gestión y orquestación, con tres bloques: el **orquestador (NFVO)**, que compone y despliega los servicios de red; el **gestor de VNF (VNFM)**, que controla el ciclo de vida de cada función; y el **gestor de la infraestructura virtualizada (VIM)**, p. ej. OpenStack.
- **Encadenamiento de servicios** (*service chaining*): componer un servicio haciendo pasar el tráfico por una secuencia de VNF (cortafuegos → inspección → balanceador) definida por software.
- **Beneficios**:
    - **Reducción de CAPEX y OPEX**: consolida funciones en servidores estándar y elimina appliances dedicados.
    - **Agilidad**: un servicio nuevo se despliega instalando software, no esperando hardware.
    - **Escalado elástico**: las funciones crecen o decrecen bajo demanda, como cualquier carga en la nube.
    - **Independencia del fabricante**: hardware común y funciones de distintos proveedores.
- **De VNF a CNF**: la evolución *cloud-native* empaqueta las funciones en contenedores orquestados con Kubernetes (**CNF**), más ligeros y escalables que las máquinas virtuales.
- **SDN y NFV son complementarias e independientes**: NFV virtualiza las funciones (qué ejecuta la red) y SDN programa la conectividad entre ellas (cómo se encamina el tráfico). El ejemplo canónico de su combinación es el **núcleo de las redes 5G**, desplegado como funciones virtualizadas (tema [76](76-redes-inalambricas-y-5g.md)).

## SD-WAN

La **SD-WAN** (*Software-Defined WAN*) aplica los principios SDN a la red de área extensa corporativa. En la WAN tradicional cada sede se conecta por líneas dedicadas (típicamente **MPLS**, tema [71](71-redes-de-computadores.md)) y el tráfico a internet se hace pasar por el centro de datos corporativo (*backhauling*), un modelo caro y poco flexible para un mundo de aplicaciones en la nube. La SD-WAN crea una **red de superposición cifrada sobre cualquier transporte** (MPLS, banda ancha, fibra, 4G/5G) y **encamina el tráfico de forma dinámica según la aplicación** y el estado medido de cada enlace. El servicio está estandarizado por el **MEF** (norma **MEF 70**, 2019, y su revisión **70.1**, 2021).

- **Componentes**:
    - **Edge SD-WAN**: el dispositivo (físico o virtual) de cada sede que levanta los túneles del overlay y aplica las políticas.
    - **Controlador**: mantiene la visión global y distribuye las políticas a los edges.
    - **Orquestador**: el portal centralizado de gestión y aprovisionamiento, con despliegue **zero-touch** (el equipo de la sede se autoconfigura al conectarse).
- **Capacidades diferenciales**:
    - **Independencia del transporte**: agrega y combina enlaces de cualquier tipo y operador.
    - **Encaminamiento por aplicación**: mide en tiempo real la calidad de cada enlace (latencia, *jitter*, pérdida) y dirige cada aplicación por el camino que cumple su SLA, priorizando las críticas.
    - **Salida local a internet**: el tráfico SaaS sale directamente de la sede, sin backhauling al centro de datos.
    - **Gestión centralizada**: políticas y cambios de configuración desde el orquestador, sin reemplazar hardware.
    - Los fabricantes añaden capacidades de **AIOps** (detección de anomalías y resolución automatizada sobre la telemetría de la red).

La comparación con la WAN tradicional resume lo que aporta:

| Aspecto | WAN tradicional (MPLS) | SD-WAN |
| --- | --- | --- |
| Transporte | Líneas dedicadas de un operador | Cualquier enlace y operador (MPLS, banda ancha, 4G/5G) |
| Encaminamiento | Estático, por destino | Dinámico, por aplicación y calidad medida del enlace |
| Tráfico a la nube | *Backhauling* por el centro de datos | Salida local a internet en cada sede |
| Aprovisionamiento | Manual, equipo a equipo | Centralizado, *zero-touch* |
| Cambios de política | Reconfiguración sede a sede | Distribución desde el orquestador |

El paso siguiente es **SASE** (*Secure Access Service Edge*, término acuñado por Gartner en **2019**): la convergencia de SD-WAN con la seguridad entregada desde la nube (pasarela web segura **SWG**, **CASB**, acceso a red de confianza cero **ZTNA** y cortafuegos como servicio **FWaaS**), de modo que cualquier usuario acceda de forma segura desde cualquier ubicación. La variante que agrupa solo los servicios de seguridad, sin la SD-WAN, se denomina **SSE** (*Security Service Edge*). La seguridad de red se desarrolla en el tema [79](79-seguridad-en-las-comunicaciones.md).

## Gestión y administración de red: SNMP

El control por software converge en una **gestión centralizada** de los dispositivos de comunicaciones: una consola única con monitorización en tiempo real, configuración masiva mediante plantillas y automatización (menos errores humanos), despliegue rápido de nuevos equipos y distribución uniforme de parches y firmware. El marco conceptual clásico de la administración de red es el **modelo FCAPS** de ISO, que ordena sus cinco áreas funcionales:

| Área | Nombre | Contenido |
| --- | --- | --- |
| **F** | Fallos (*fault*) | Detectar, aislar, registrar y resolver averías |
| **C** | Configuración | Inventario, aprovisionamiento y cambios de configuración |
| **A** | Contabilidad (*accounting*) | Medir el uso de recursos por usuario o servicio |
| **P** | Prestaciones (*performance*) | Monitorizar rendimiento: utilización, latencia, errores |
| **S** | Seguridad | Controlar el acceso y proteger la información de gestión |

### SNMP (Simple Network Management Protocol)

SNMP es el protocolo estándar de Internet para supervisar y administrar dispositivos de red. Opera en la capa de aplicación sobre UDP: el agente escucha las consultas en el puerto **161** y el gestor recibe las notificaciones en el **162**.

- **Arquitectura**:
    - **Gestor (NMS)**: la estación de gestión que consulta y recibe avisos.
    - **Agente**: el software del dispositivo gestionado que responde y notifica.
    - **MIB (Management Information Base)**: la base de datos de objetos gestionables del dispositivo. Cada objeto se identifica por un **OID**, un identificador numérico dentro de un árbol jerárquico global, y se define con la notación **SMI** (basada en ASN.1). La MIB estándar de referencia es la **MIB-II** (RFC 1213), con los objetos comunes (interfaces, IP, TCP…) que implementa cualquier equipo.
- **Operaciones**: **GET** (leer un objeto), **GETNEXT** (recorrer el árbol), **GETBULK** (lectura masiva, desde v2), **SET** (modificar), **TRAP** (notificación asíncrona del agente, sin confirmación) e **INFORM** (notificación confirmada, desde v2).
- **Versiones**:

| Versión | Año | Características |
| --- | --- | --- |
| **SNMPv1** | 1990 (RFC 1157) | Autenticación por **comunidades** en texto claro |
| **SNMPv2c** | 1996 | Añade GETBULK e INFORM y contadores de 64 bits; mantiene las comunidades |
| **SNMPv3** | 2002 (STD 62, RFC 3411-3418) | Seguridad real: **autenticación, integridad y cifrado** (modelos USM y VACM), con niveles noAuthNoPriv, authNoPriv y authPriv |

- **RMON** (*Remote Monitoring*): una MIB especializada que permite a sondas remotas recopilar estadísticas de tráfico por sí mismas y reportarlas al gestor.
- **Otras fuentes de monitorización**: SNMP se complementa con **syslog** (RFC 5424; envío de registros de eventos, habitualmente por UDP **514**) y con el análisis de flujos de tráfico mediante **NetFlow** (Cisco, v9 en el RFC 3954) y su estándar IETF **IPFIX** (RFC 7011), base de la detección de anomalías y la planificación de capacidad.
- **Gestión moderna (programática)**: SNMP sigue dominando la monitorización, pero la configuración se automatiza hoy con **NETCONF** (RFC 6241, 2011: RPC con XML sobre SSH, puerto **830**) y **RESTCONF** (RFC 8040, 2017: la misma idea con HTTP y JSON), ambos sobre modelos de datos **YANG** (RFC 7950). Estas interfaces, junto a la telemetría en *streaming*, son la base de la automatización y orquestación de las redes SDN.

## Fuentes {.unnumbered .unlisted}

- ONF, *OpenFlow Switch Specification*, versión 1.5.1 (marzo de 2015).
- ETSI, *Network Functions Virtualisation*, white paper fundacional (octubre de 2012); ETSI GS NFV 002, marco arquitectónico NFV.
- RFC 7348, *VXLAN* (agosto de 2014).
- MEF 70 (julio de 2019) y MEF 70.1 (noviembre de 2021): definición del servicio SD-WAN.
- RFC 1157, SNMPv1 (mayo de 1990); RFC 1213, MIB-II (marzo de 1991); STD 62, RFC 3411-3418, SNMPv3 (diciembre de 2002).
- RFC 5424, syslog (marzo de 2009); RFC 3954, NetFlow v9 (octubre de 2004); RFC 7011, IPFIX (septiembre de 2013).
- RFC 6241, NETCONF (junio de 2011); RFC 7950, YANG 1.1 (agosto de 2016); RFC 8040, RESTCONF (enero de 2017).
