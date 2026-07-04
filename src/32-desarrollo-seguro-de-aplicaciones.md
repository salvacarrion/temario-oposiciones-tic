# Desarrollo seguro de aplicaciones

## Proceso de desarrollo seguro

El **proceso de desarrollo seguro** se enfoca en la creación de sistemas y aplicaciones robustos que integren medidas de seguridad desde el inicio y a lo largo de todo el ciclo de vida del desarrollo. Este proceso es fundamental para garantizar la protección de los datos y el cumplimiento normativo en el entorno tecnológico actual.

### Pilares de la seguridad

- **Red segmentada** con restricciones de acceso adecuadas, minimizando el riesgo de movimientos laterales en caso de incidentes.
- **Sistemas correctamente configurados y bastionados**, eliminando servicios innecesarios y reforzando configuraciones para reducir vulnerabilidades.
- **Aplicaciones desarrolladas de forma segura**, considerando directrices de seguridad y utilizando herramientas y metodologías probadas.

### Desarrollo seguro de aplicaciones

El desarrollo seguro abarca distintas áreas críticas para garantizar la seguridad de las aplicaciones:

- **Seguridad del proceso de desarrollo**:
    - Alineación con la política de seguridad de la organización.
    - Especificación de los requisitos de seguridad desde las primeras etapas.
    - Gestión rigurosa de la documentación y control de cambios.
    - Mantenimiento continuo y revisión de actualizaciones de seguridad.
- **Análisis de riesgos**:
    - **Modelado de amenazas**: Identificación y evaluación de amenazas potenciales.
    - **Catálogo de amenazas**: Revisión exhaustiva de escenarios de riesgo conocidos.
- **Requisitos legales de las aplicaciones**:
    - Revisión anual de las normativas aplicables para asegurar el cumplimiento de leyes y regulaciones.
- **Directrices**: de diseño, despliegue, programación y auditoria.

### Directrices de desarrollo seguro

### Directrices de diseño

- **Principio de mínimo privilegio**: Otorgar solo los permisos necesarios.
- **Separación de responsabilidades**: Evitar acumulación de funciones críticas en una misma entidad.
- **Defensa en profundidad**: Implementar múltiples capas de seguridad.
- **Fallo seguro**: Garantizar que los sistemas fallen de manera controlada.
- **Economía de mecanismos**: Diseñar soluciones simples para minimizar riesgos.
- **Mediación completa**: Validar todas las solicitudes.
- **Diseño abierto**: Basar la seguridad en principios robustos y transparentes, no en el secretismo.
- **Mecanismo menos común**: Utilizar componentes compartidos con precaución.
- **Aceptabilidad psicológica**: Diseñar sistemas fáciles de usar para fomentar su adopción.
- **Eslabón más débil**: Fortalecer los puntos vulnerables del sistema.
- **Aprovechar componentes existentes**: Utilizar soluciones probadas y seguras.

### Directrices de despliegue

- Utilizar un **procedimiento estandarizado** para garantizar que todas las configuraciones y pruebas de seguridad estén en orden.

### Directrices de programación

- Definir **requisitos de seguridad claros**.
- Aprovechar **frameworks y librerías de seguridad** reconocidas.
- Implementar un **acceso seguro a bases de datos** y validar todas las entradas.
- **Codificar y escapar los datos** para prevenir vulnerabilidades.
- Reforzar los controles de acceso y proteger los datos continuamente.
- Implementar **monitorización de seguridad** y manejar errores de manera controlada.

### Directrices de auditoría

- Realizar auditorías durante el desarrollo y de manera periódica para detectar problemas de seguridad.

## Seguridad en entornos web y aplicaciones

Los entornos web y aplicaciones deben seguir estándares reconocidos para garantizar la seguridad:

- **Normas y organismos**:
    - **ISO 27000**, estándares internacionales de seguridad.
    - **SANS Software Security Institute**, enfoque en la seguridad del software.
    - **OWASP**, estándares para aplicaciones web.
    - **NIST**, directrices y prácticas de ciberseguridad.
- **MITRE**:
    - **MITRE Pre-Att&k**: Base de conocimiento de tácticas y técnicas previas al ataque.
    - **CVE (Common Vulnerabilities & Exposures)**: Listado de vulnerabilidades conocidas, como el **CVE-2021-44228 (log4shell)**.
    - **CWE (Common Weakness Enumeration)**: Tipos de vulnerabilidades, como **CWE-89 (SQL injection)**.

### Estrategia de seguridad

- **Formación** continua del personal en seguridad.
- Implementación de **sistemas y redes seguras**.
- Uso de **Web Firewall Applications (WAF)** para proteger aplicaciones web.
- Desarrollo de **código seguro** siguiendo mejores prácticas.

### Análisis de seguridad

- **Técnicas de análisis**:
    - **SAST (Static Application Security Testing)**: Análisis estático del código fuente.
    - **DAST (Dynamic Application Security Testing)**: Análisis dinámico durante la ejecución.
    - **SCA (Software Composition Analysis)**: Evaluación de bibliotecas y dependencias externas.
    - **Pentesting**: Simulación de ataques para detectar vulnerabilidades.
- Herramientas:
    - **SonarQube** (caja blanca).
    - **Acunetix** (caja negra).

### Validación de aplicaciones

- **Pruebas funcionales**:
    - **Test de integración**: Verificar que los componentes trabajen en conjunto.
    - **Test de regresión**: Detectar errores tras cambios en el código.
    - **Test de aceptación**: Comprobar que se cumplen los requisitos del cliente.
- **Pruebas no funcionales**:
    - **Test de rendimiento**: Evaluar la velocidad y eficiencia.
    - **Test de recuperación**: Medir la capacidad de respuesta tras fallos.
    - **Test de escalabilidad**: Analizar el comportamiento ante incrementos de carga.
    - **Test de seguridad**: Identificar y remediar vulnerabilidades.

## Seguridad y protección de redes de comunicaciones

**Seguridad de redes**: Consiste en las políticas y prácticas adoptadas para prevenir y supervisar el acceso no autorizado, el uso indebido, la modificación o la denegación de una red informática y sus recursos accesibles.

**Autenticación**: Puede llevarse a cabo mediante:

- **1-factor**: Basada en lo que el usuario sabe (contraseña).
- **2-factores**: Basada en lo que el usuario tiene (SMS).
- **3-factores**: Basada en lo que el usuario es (huella dactilar).

**Cortafuegos**: Se encargan de aplicar las políticas de acceso.

**Dimensiones de seguridad**: Incluyen confidencialidad, disponibilidad e integridad.

**Honeypot**: Es una herramienta de seguridad informática dispuesta en una red o sistema para atraer posibles ataques informáticos. Facilita la detección de ataques y la obtención de información sobre el mismo y el atacante.

**Honeynet**: Tipo especial de honeypot de alta interacción que actúa sobre una red completa. Está diseñado para ser atacado y recabar información detallada sobre los atacantes.

**Sistema de detección de intrusos (IDS, Intrusion Detection System)**: Proceso o dispositivo activo que analiza la actividad del sistema y de la red para identificar accesos no autorizados y actividades maliciosas.

**Tipos de IDS**:

- **NIDS (Network-Based Intrusion Detection System)**: Supervisan la actividad de la red, analizando tanto el tráfico entrante como el saliente.
- **HIDS (Host-Based Intrusion Detection System)**: Supervisan la actividad de un sistema específico. Realizan chequeo de la integridad de ficheros, detección de rootkits y monitorización de logs.

**Sistemas de Prevención de Intrusiones (IPS)**: Detectan y bloquean intentos de intrusión, transmisiones de código malicioso o amenazas en la red, sin afectar el rendimiento del sistema. Detectan anomalías a nivel del sistema operativo.

**Tipos de IPS**:

- **NIPS (Network-based Intrusion Prevention System)**.
- **WIPS (Wireless Intrusion Prevention System)**.
- **NBA (Network Behavior Analysis)**.
- **HIPS (Host-based Intrusion Prevention System)**.

### Vulnerabilidades

- **Personal interno**.
- **Entidades externas**.
- **Fast Growth and Overuse**.
- **Fallback attacks / Downgrade attacks**: Ataque criptográfico que degrada el modo de operación seguro (por ejemplo, una conexión encriptada) a un modo menos seguro (texto sin cifrar) para mantener la retrocompatibilidad.
- **Eavesdropping**: Escucha no autorizada de conversaciones o comunicaciones sin el consentimiento de las partes.
- **Replay Attacks**: Repetición malintencionada de una transmisión de datos válida.
- **Insertion attacks**: Cuando el IDS es menos estricto que el sistema final.
- **Fragmentation attacks**: Ataque que utiliza la fragmentación de datagramas para producir un Denegación de Servicio (DoS).
- **Buffer overflows**: Error de software que permite la escritura de datos fuera del buffer, con la posibilidad de alterar el flujo del programa y ejecutar código malicioso.
    - **Shellcode**: Código ejecutable preparado para obtener privilegios sobre un programa vulnerable.
- **XSS attacks (Cross-Site Scripting)**: Permite a un atacante inyectar código en páginas web visitadas por el usuario (JavaScript, VBScript).
- **Man-in-the-middle**: El atacante adquiere la capacidad de leer, insertar y modificar datos en la comunicación entre dos partes.
- **Session hijacking**: Obtención de acceso no autorizado a información o servicios mediante el secuestro de una sesión.
    - **Session fixation**: El atacante fija una sesión específica en el navegador de la víctima.
    - **Replay session**: Reutilización de una sesión.
- **Spoofing attacks**: Falsificación de datos para suplantar la identidad de otra entidad.
- **Convert channels (Canal encubierto)**: Canal usado para transferir información de manera no prevista por los desarrolladores del sistema.
- **Smurf attack (ataque pitufo)**: Ataque de denegación de servicio mediante mensajes de ping broadcast con spoofing para inundar el sistema objetivo.
- **Denial of Service (DoS)**: Causar la inaccesibilidad de un servicio o recurso para usuarios legítimos, mediante el consumo de ancho de banda o sobrecarga de los recursos del sistema.
    - **Distributed Denial of Service (DDoS)**
- **Malware**: Software malicioso diseñado para realizar acciones dañinas en el sistema de manera intencionada y sin el conocimiento del usuario.

### Redes privadas virtuales (VPN)

Tecnología que extiende de forma segura una red local (LAN) sobre una red pública o no controlada, como Internet. Permite que los dispositivos en la red envíen y reciban datos de redes compartidas o públicas como si fueran redes privadas, manteniendo la seguridad y las políticas de gestión de una red privada.

**Características básicas de una VPN**:

- Autenticación y autorización.
- Integridad.
- Confidencialidad/Privacidad.
- No repudio.
- Control de acceso.
- Auditoría y registro de actividades.
- Calidad del servicio.

**Requisitos básicos de una VPN**:

- **Identificación de usuario**: Usuario y contraseña.
- **Cifrado de datos**: Con cifrado simétrico (DES, 3DES o AES). Se destaca el algoritmo SEAL, más rápido.
- **Administración de claves**.

**Tipos de VPN**:

- **VPN de acceso remoto**: Conexión de usuarios desde ubicaciones remotas a la red de la empresa mediante Internet.
- **VPN punto a punto**: Conexión de oficinas remotas con la sede de la organización.
- **Tunneling**: Encapsulación de un protocolo de red sobre otro, creando un "túnel" en la red.
- **VPN over WAN**: Variante del tipo "acceso remoto" que utiliza la red WAN de la empresa en lugar de Internet.

**Tipos de conexión en VPN**:

- **Conexión de acceso remoto**.
- **Conexión VPN router a router**.
- **Conexión VPN firewall a firewall**.
- **VPN en entornos móviles**.

**Dispositivos VPN**:

- **Enrutador VPN**: Enrutador con software de cliente VPN.
- **Concentrador VPN**: Dispositivo que permite a múltiples usuarios acceder remotamente a la red a través de túneles VPN cifrados. Puede gestionar miles de conexiones simultáneas.

### Control de accesos

Enfoque de seguridad en redes que unifica las tecnologías de seguridad en equipos finales, usuarios y refuerza la seguridad de acceso a la red.

**Control de acceso informático**: Consiste en la autenticación, autorización de acceso y auditoría.

- **Autenticación/Identificación**: "¿Quién puede entrar al sistema?"
- **Autorización**: "¿Qué puede hacer el sujeto?"
- **Aprobación del acceso**: Definición de políticas de autorizaciones.
- **Auditoría/Rendición de cuentas**: "¿Qué ha hecho el sujeto?"

### Sistemas cortafuegos

Parte de un sistema o red diseñado para bloquear el acceso no autorizado y permitir las comunicaciones autorizadas.

**Tipos de cortafuegos**:

- **Nivel de aplicación de pasarela**: Seguridad para aplicaciones específicas (FTP, Telnet, P2P).
- **Circuito a nivel de pasarela**: Seguridad cuando se establece una conexión TCP o UDP.
- **Cortafuegos de capa de red o de filtrado de paquetes**: Funciona a nivel de red, inspeccionando direcciones IP y paquetes IP.
- **Cortafuegos de capa de aplicación (Application Firewall)**: Filtra comunicaciones adaptadas a protocolos de aplicación (ej.: URL).
- **Cortafuegos personal**: Filtra las comunicaciones entre el ordenador y la red.

**Capa de trabajo de los cortafuegos**:

- **Cortafuegos a nivel de red**: Examina los paquetes IP para decidir si deben pasar o no.
- **Cortafuegos a nivel de circuito**: Examina la información TCP para verificar que la sesión es legítima.
- **Cortafuegos a nivel de aplicación**: Utiliza software de servidor Proxy.

**Topologías de cortafuegos**:

- **Bastion Host**: Firewall en una instalación específica.
- **Screening Router**: Encaminador con filtrado.
- **Dual-Homed Host**: Host con doble conexión.
- **Screened Host**: Filtrado a nivel de host.
- **Screened Subnet**: Filtrado a nivel de subred.

**Traducción de direcciones de red (NAT)**: Oculta la verdadera dirección de la computadora conectada a la red.

**Políticas del cortafuegos**:

- **Política restrictiva**: Deniega todo el tráfico, excepto el explícitamente permitido.
- **Política permisiva**: Permite todo el tráfico, excepto el explícitamente denegado.

## Medidas de protección

La implementación de medidas de protección en el ámbito informático garantiza la seguridad de las infraestructuras, equipos, comunicaciones, información y servicios, mitigando riesgos asociados a incidentes internos y externos. Estas medidas se agrupan en diversas áreas fundamentales que se desarrollan a continuación.

### Protección de las instalaciones e infraestructuras

Las instalaciones deben cumplir estándares de seguridad que minimicen riesgos físicos y fortuitos:

- **Áreas separadas y con control de acceso**: Se delimitarán zonas diferenciadas para prevenir accesos no autorizados mediante sistemas de control y registro de entradas y salidas.
- **Identificación de personas**: Será obligatorio un sistema que identifique a todas las personas con acceso a las instalaciones.
- **Acondicionamiento de locales**: Se controlarán factores como la **humedad**, la **temperatura** y otros riesgos ambientales.
- **Energía eléctrica**: Habrá tomas de energía adecuadas y suministro de emergencia para garantizar continuidad operativa ante cortes de electricidad.
- **Protección frente a incendios**: Se seguirán normas específicas de la normativa industrial en materia de prevención y respuesta.
- **Protección frente a inundaciones**: Las instalaciones deben contar con medidas de protección para evitar daños por agua, como sistemas de drenaje o ubicación elevada de equipos sensibles.
- **Registro de entradas y salidas del equipamiento**: Se llevará un **registro pormenorizado** que garantice la trazabilidad de los movimientos de equipamiento.

### Gestión del personal

- **Concienciación**: El personal debe conocer las **normativas de seguridad**, los **procedimientos de actuación frente a incidentes** y las formas de identificarlos y reportarlos.
- **Formación**: Se proporcionará formación regular para actualizar conocimientos en seguridad.

### Protección de los equipos

- **Puesto de trabajo despejado**: Mantener los puestos libres de elementos innecesarios y guardar materiales sensibles en lugares cerrados y seguros.
- **Bloqueo del puesto de trabajo**: Los equipos deben bloquearse tras periodos de inactividad y cerrarse las sesiones al finalizar su uso.
- **Protección de dispositivos portátiles**: Los dispositivos deberán:
    - Estar inventariados.
    - Contar con gestión centralizada.
    - Restringir el acceso a información fuera de la red corporativa.
    - No contener claves de acceso remoto.
    - Incluir cifrado de disco para proteger la información.

### Protección de las comunicaciones

- **Perímetro seguro**: Uso de sistemas de protección perimetral que autoricen únicamente flujos necesarios.
- **Protección de la confidencialidad**:
    - Uso de **VPNs** en comunicaciones externas.
    - Algoritmos cifrados autorizados por el CCN.
    - VPNs implementadas por hardware.
    - Productos certificados para cifrado de información.
    - Todas las comunicaciones deberán cifrarse.
- **Protección de la integridad y la autenticidad**:
    - Uso de mecanismos de **autenticación e identificación** aprobados.
    - Prevención de ataques mediante algoritmos autorizados y productos certificados.
- **Separación de flujos de información en red**:
    - Tráfico segregado según funciones: usuarios, servicios y administración.
    - Segmentación lógica básica (VLANs) y avanzada (VPNs).
    - Segmentación física y monitorización de puntos de interconexión.

### Protección de soportes de información

- **Marcado de soportes**: Los soportes deben indicar claramente el nivel de seguridad de la información que contienen y emplear marcas de agua.
- **Criptografía**:
    - Garantizar la **confidencialidad** e **integridad** mediante algoritmos autorizados.
    - Usar productos certificados por el CCN.
    - Realizar copias de seguridad cifradas según los requisitos del CCN.
- **Custodia**: Los soportes se custodiarán con diligencia y respetando las condiciones de mantenimiento recomendadas por el fabricante.
- **Transporte**: Se registrarán las entradas y salidas de los soportes, empleando mecanismos criptográficos para su protección y una adecuada gestión de claves.
- **Borrado y destrucción**: Se utilizarán métodos de borrado seguro según el CCN y productos certificados.

### Protección de las aplicaciones informáticas

- **Desarrollo de aplicaciones**:
    - Los entornos de desarrollo deben estar separados del de producción.
    - Aplicar principios de **mínimo privilegio** y una **metodología de desarrollo seguro**.
    - Diseñar con seguridad desde la concepción.
    - Usar datos de prueba y una lista de componentes de software controlada.
- **Aceptación y puesta en servicio**:
    - Comprobación de los criterios de aceptación y no deterioro de la seguridad.
    - Realizar pruebas en entornos aislados y auditorías del código fuente.

### Protección de la información

- **Datos personales**: Cumplir con los requisitos establecidos en la normativa de protección de datos.
- **Calificación de la información**: Definir responsables y garantizar la clasificación adecuada de la información.
- **Firma electrónica**:
    - Emplear **firmas autorizadas** y certificados cualificados con algoritmos aprobados.
    - Usar productos certificados para la validación de la firma electrónica avanzada.
- **Sellos de tiempo**: Renovar regularmente los sellos cualificados cuando se requiera evidencia temporal.
- **Limpieza de documentos**: Eliminar campos ocultos, metadatos o comentarios en documentos.
- **Copias de seguridad**:
    - Deben permitir la recuperación completa y estar sujetas a procedimientos documentados que definan frecuencia, lugar y acceso.
    - Realizar pruebas regulares de recuperación y almacenar copias en lugares alternativos.

### Protección de los servicios

- **Protección del correo electrónico**:
    - Cifrar cuerpo de mensajes y anexos.
    - Proteger las conexiones y encaminar mensajes de manera segura.
    - Implementar sistemas contra spam, código dañino y applets.
- **Protección de servicios y aplicaciones web**:
    - Prevenir intentos de escalado de privilegios y ataques XSS.
    - Realizar auditorías de seguridad avanzadas y proteger las cachés.
- **Protección de la navegación web**:
    - Implementar normativas de uso y formar al personal en navegación segura.
    - Usar listas blancas de destinos permitidos y monitorizar registros de navegación.
- **Protección frente a la denegación del servicio**:
    - Sistemas con capacidad suficiente para resistir ataques.
    - Tecnologías de detección y reacción ante ataques conocidos.
    - Procedimientos para evitar ataques propios o errores de configuración.

## OWASP 4.0 (Open Web Application Security Project)

OWASP es una iniciativa libre y sin ánimo de lucro que busca promover la seguridad en el software, enfocándose principalmente en aplicaciones web. Este proyecto se organiza en función del estado de madurez del desarrollo, y sus etapas incluyen:

- **Definición**: Revisión de requerimientos.
- **Diseño**: Revisión de arquitectura, diseño, y modelos UML.
- **Desarrollo**: Revisión de código, pruebas unitarias y de sistema.
- **Despliegue**: Pruebas de penetración, revisiones de configuración y pruebas adicionales.
- **Mantenimiento**: Realización de “health checks”, revisiones operacionales y pruebas de regresión.

### Pruebas de seguridad

Las pruebas de seguridad en OWASP se dividen en dos fases principales:

- **Pasiva**: Se examina el funcionamiento de la aplicación para comprender su lógica operativa e identificar posibles vulnerabilidades.
- **Activa**: Se realizan pruebas específicas en base a los vectores de ataque identificados en la fase pasiva.

Estas pruebas están organizadas en **11 categorías**, con un total de **91 puntos de control**. Las categorías **incluyen**:

Recopilación de información, gestión de configuración y despliegue, gestión de identidades, autenticación, autorización, gestión de sesiones, validación de entrada, tratamiento de errores, criptografía, lógica empresarial y pruebas en el lado del cliente. Ejemplos de puntos de control son pruebas de métodos HTTP, pruebas de inyección SQL y chequeos de integridad.

### Informe de resultados de la auditoría

El informe de auditoría en OWASP se estructura en tres secciones:

- **Informe ejecutivo**: Proporciona una visión clara y no técnica de los resultados.
- **Informe de pruebas**: Describe en detalle las pruebas, el alcance y limitaciones de cada test.
- **Informe de hallazgos**: Presenta los problemas encontrados junto con recomendaciones para mitigarlos.

### Top riesgos de seguridad en OWASP

Algunos de los principales riesgos de seguridad en aplicaciones web son: inyección (SQL, LDAP), ruptura de autenticación y secuestro de sesión, cross-site scripting (XSS), referencias a objetos no seguras, configuración de seguridad insuficiente, exposición de datos sensibles, falta de control en el nivel de acceso, cross-site request forgery (CSRF), componentes con vulnerabilidades conocidas y redirecciones no validadas.

### Seguridad de los servicios en nube

Para asegurar servicios en la nube, se recomienda un decálogo de medidas:

Determinar la categoría del sistema según el ENS, elaborar una declaración de aplicabilidad, realizar un análisis de riesgos, acogerse a un perfil de cumplimiento específico, establecer condiciones contractuales antes de la contratación, detallar aspectos específicos en las condiciones contractuales, supervisar el cumplimiento de requisitos legales por el CSP, realizar un seguimiento de los acuerdos de nivel de servicio (SLA), planificar revisiones periódicas de la información del CSP y desarrollar normativa de seguridad específica para usuarios de la nube.

### Herramientas de seguridad

Las herramientas de seguridad se clasifican en:

- **Herramientas de auditoría**
- **Herramientas de protección** (ej., IDS, IPS, IDS/IPS como Tripwire, OSSEC)
- **Herramientas de detección**
- **Herramientas de reacción**

### Sistema de detección de intrusos (IDS)

Un IDS analiza la actividad en sistemas y redes en busca de entradas no autorizadas o actividades maliciosas. Los IDS se dividen en:

- **NIDS** (Network-Based Intrusion Detection System): Analizan el tráfico de red en tiempo real, buscando ataques DoS, escaneo de puertos e intentos de intrusión, entre otros.
- **HIDS** (Host-Based Intrusion Detection System): Analizan actividades de un host en busca de anomalías que sugieran posibles amenazas.

### Sistemas de Prevención de Intrusiones (IPS)

Los IPS detectan y bloquean intentos de intrusión y amenazas sin afectar el rendimiento. Las características de un IPS incluyen:

- **Detección basada en anomalías**: Identificación, registro y bloqueo de actividad maliciosa.
- **Actualización automática** de bases de firmas.
- **Detección basada en políticas**: Los administradores pueden declarar detalladamente qué actividades son aceptables. Los IPS protegen contra gusanos, spyware, DoS/DDoS, inyección SQL y otros ataques.

Los IPS incluyen diferentes tipos:

- **NIPS**: Basado en la red, buscan tráfico sospechoso en la red.
- **WIPS**: Basado en redes inalámbricas, buscan tráfico sospechoso en la red inalámbrica.
- **NBA**: Analizan comportamientos anómalos en la red, como ciertos tipos de malware y ataques de denegación de servicio.
- **HIPS**: Detectan actividades sospechosas en hosts individuales.

### AntiDDoS

Los sistemas AntiDDoS están diseñados para proteger servidores y redes contra ataques de denegación de servicio (DoS).
