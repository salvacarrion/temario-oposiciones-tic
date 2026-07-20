# Servicios de infraestructura: web, correo y monitorización

Sobre los sistemas operativos de servidor (temas [47](47-administracion-de-sistemas-gnu-linux.md) y [48](48-administracion-de-sistemas-windows-y-directorio-activo.md)) se despliegan los servicios que sostienen las aplicaciones corporativas: servidores web y de aplicaciones, proxies y balanceadores, correo electrónico, servicios de directorio y monitorización. Los protocolos de red subyacentes se tratan en el tema [70](70-protocolos-de-comunicaciones.md); aquí interesa la arquitectura y la administración del lado servidor.

## Servidores web

El servidor web atiende peticiones HTTP/HTTPS y sirve contenido estático o lo delega en la capa de aplicación. Los tres dominantes:

- **Apache HTTP Server**: veterano y modular: **mod_ssl** (TLS), **mod_rewrite** (reescritura de URL), **mod_proxy** (proxy inverso), mod_auth (autenticación) y **ModSecurity** (WAF); procesamiento por procesos/hilos (MPM *prefork*, *worker*, *event*), configuración por directivas (`httpd.conf`, hosts virtuales por nombre) y ficheros `.htaccess` por directorio.
- **Nginx**: arquitectura **asíncrona orientada a eventos**, muy eficiente sirviendo estáticos y con miles de conexiones concurrentes; el uso habitual es de **proxy inverso** y terminación TLS delante de la aplicación.
- **IIS (Internet Information Services)**: el servidor web de Windows, administrado por consola o PowerShell, con aislamiento por **grupos de aplicaciones** (*application pools*), configuración por sitio en `web.config`, e integración con el ecosistema .NET y la **autenticación integrada de Windows** (Kerberos/NTLM, tema [48](48-administracion-de-sistemas-windows-y-directorio-activo.md)).
- **Optimización y seguridad comunes**: conexiones persistentes (*keep-alive*), compresión (gzip/brotli), caché de contenido con cabeceras HTTP, y **TLS 1.2/1.3** como únicas versiones vigentes (SSL y TLS 1.0/1.1 están retirados).

Los tres sirven **HTTP/2** de forma general; **HTTP/3** (sobre QUIC, tema [70](70-protocolos-de-comunicaciones.md)) está disponible en Nginx (desde la 1.25) e IIS (desde Windows Server 2022), no aún de forma estable en Apache. El contenido dinámico ya no se genera con el **CGI** histórico (un proceso por petición): corre en procesos persistentes (**FastCGI**/PHP-FPM, WSGI) o en servidores de aplicación propios detrás del proxy inverso.

Patrón habitual: Nginx (o Apache) delante, sirviendo estático, terminando **TLS** y pasando lo dinámico al servidor de aplicaciones; certificados automatizados (ACME/Let's Encrypt) y cabeceras de seguridad (el desarrollo seguro se trata en el tema [32](32-desarrollo-seguro-de-aplicaciones.md)).

```nginx
server {
    listen 443 ssl;
    server_name app.gva.es;
    location /static/ { root /var/www/app; }
    location / { proxy_pass http://127.0.0.1:8080; }   # al servidor de aplicaciones
}
```

## Servidores de aplicaciones

Ejecutan la lógica de negocio y ofrecen a las aplicaciones servicios comunes: gestión de hilos y sesiones, **pools de conexiones** a base de datos, transacciones, despliegue en caliente y monitorización.

- **Apache Tomcat**: contenedor de **servlets** Java (y JSP), ligero y ubicuo (puerto por defecto **8080**); el despliegue copia la aplicación empaquetada como **WAR** en `webapps/`. Configuración en **server.xml** (conectores HTTP; el conector **AJP** con Apache está en desuso tras la vulnerabilidad Ghostcat) y usuarios de las consolas en `tomcat-users.xml`; la conexión a base de datos usa **pools JDBC** definidos como recursos. El rendimiento se ajusta dimensionando la **JVM**: tamaño del *heap* (`-Xms`/`-Xmx`) y recolector de basura (G1 por defecto).
- **Jakarta EE completos**: implementan la plataforma empresarial Java completa (**Jakarta EE**, el antiguo Java EE, renombrado al transferirse de Oracle a la **Eclipse Foundation**): **WildFly/JBoss EAP** (Red Hat) y **Oracle WebLogic** (habitual en administraciones con Oracle): clustering, colas de mensajes, transacciones distribuidas y consolas de administración de dominio.
- **Arquitectura WebLogic** (el patrón de los Jakarta EE grandes): el **dominio** agrupa un **servidor de administración** (configuración y consola) y varios **servidores gestionados** (*managed servers*) donde corren las aplicaciones, agrupables en **clústeres** con réplica de sesión; el **Node Manager** arranca y vigila los servidores en cada máquina, y la administración se automatiza con **WLST** (scripting).
- **Otras plataformas**: cada ecosistema trae su servidor de aplicación (procesos PHP-FPM, Gunicorn/uWSGI en Python, Node.js), normalmente detrás del proxy inverso (las plataformas de desarrollo se tratan en el tema [61](61-programacion.md)).
- **Servidor embebido**: el patrón moderno invierte la relación: la aplicación (Spring Boot y equivalentes) **embebe** su propio Tomcat/Jetty/Netty, se empaqueta como JAR ejecutable o imagen de contenedor y se despliega en Kubernetes (tema [44](44-virtualizacion-y-contenedores.md)), dejando al servidor de aplicaciones clásico el parque heredado.

## Proxy, proxy inverso y balanceo de carga

- **Proxy directo**: intermedia las salidas de los usuarios hacia Internet: control de acceso y filtrado de contenidos, caché y registro de navegación. El referente libre es **Squid** (puerto por defecto **3128**; ACL por origen/destino/horario, jerarquías de caché, integración con autenticación corporativa).
- **Proxy inverso**: intermedia las entradas hacia los servidores: publica aplicaciones internas, oculta la topología, termina TLS, cachea y protege (limitación de tasa; se complementa con WAF, tema [32](32-desarrollo-seguro-de-aplicaciones.md)). Lo hacen Nginx, Apache (mod_proxy) y HAProxy; **Varnish** es su especialización como caché inversa de contenido.
- **Balanceo de carga**: reparte peticiones entre varios servidores para escalar y tolerar fallos: algoritmos **round robin**, menos conexiones o hash de IP; **comprobaciones de salud** que retiran nodos caídos; **persistencia de sesión** (*sticky sessions*) cuando la aplicación lo exige. Puede operar en **capa 4** (TCP: reparte conexiones sin mirar el contenido, máximo rendimiento) o en **capa 7** (HTTP: decide por URL, cabeceras o cookies, y permite terminar TLS). **HAProxy** es el balanceador software de referencia (ambas capas); en nube lo dan los balanceadores gestionados, y a escala Internet las **CDN**.
- **Alta disponibilidad y especializaciones**: el propio balanceador se redunda en pareja activo-pasivo con una IP virtual flotante (**VRRP**, implementado por keepalived); para publicar APIs, su especialización es el **API gateway** (tema [40](40-apis-y-apificacion.md)).

## Correo electrónico y mensajería

En el correo intervienen el **MUA** (cliente), el **MTA** (agente de transferencia que encamina entre servidores por **SMTP**, puerto **25**) y el **MDA** (entrega al buzón); el MTA localiza el servidor del dominio de destino consultando su registro **MX** en el DNS. El cliente envía por el puerto **587** (*submission*, autenticado; **465** con TLS implícito) y lee por **IMAP** (correo en el servidor, el estándar corporativo; puerto **993**) o POP3 (descarga; **995**). El diálogo SMTP y los protocolos se detallan en el tema [70](70-protocolos-de-comunicaciones.md).

- **Flujo de un mensaje**: (1) el MUA lo entrega por *submission* autenticado al MTA de su organización; (2) este resuelve el **MX** del dominio destino; (3) lo transfiere por SMTP (25, cifrado oportunista STARTTLS) al MTA receptor, que aplica los filtros SPF/DKIM/DMARC y antispam; (4) el MDA lo deposita en el buzón; (5) el destinatario lo lee por IMAP desde sus dispositivos.
- **Formato**: el mensaje son cabeceras + cuerpo en texto; **MIME** extiende el formato para adjuntos, HTML y juegos de caracteres distintos del ASCII (tipos `Content-Type`, codificación base64).
- **Administración del servicio**: **alias** y **listas de distribución** (direcciones que reparten a varios buzones), **buzones compartidos** (unidades y servicios: `registro@`), cuotas de buzón, y **retención y archivado** (conservación por obligación legal o de expediente, con búsqueda *eDiscovery* en las plataformas corporativas).
- **Alta disponibilidad**: Exchange replica los buzones entre servidores en un **DAG** (*Database Availability Group*, conmutación automática de bases de datos); en SaaS la da la propia plataforma.

- **Servidores**: **Postfix** (MTA libre de referencia, con Dovecot como IMAP), **Microsoft Exchange** (integrado con AD; Exchange Online en Microsoft 365) y las plataformas SaaS (Microsoft 365, Google Workspace), mayoritarias hoy.
- **Autenticación del correo** frente a la suplantación (*spoofing*), publicada en DNS:

| Mecanismo | Qué comprueba | Registro |
| --- | --- | --- |
| **SPF** (RFC 7208) | Qué servidores pueden enviar en nombre del dominio | TXT: `v=spf1 mx ip4:192.0.2.10 -all` |
| **DKIM** (RFC 6376) | Firma criptográfica del mensaje por el dominio emisor | TXT con la clave pública (selector) |
| **DMARC** (RFC 9989, sustituye desde may-2026 al RFC 7489) | Alineación de SPF/DKIM y política ante fallos | TXT: `v=DMARC1; p=quarantine` (none/quarantine/reject) |

- **Higiene y protección**: pasarelas antispam/antimalware, listas de bloqueo (RBL), cifrado TLS entre MTA (MTA-STS) y concienciación anti-*phishing* (tema [28](28-ciberseguridad.md)).
- **Mensajería y colaboración**: la mensajería instantánea corporativa y las plataformas colaborativas (Teams, Slack y equivalentes) complementan al correo con **presencia**, canales e integración con la identidad corporativa (**SSO**); como estándares abiertos y federables perviven **XMPP** y **Matrix** (autoalojables, con cifrado de extremo a extremo). Comunicaciones unificadas en el tema [74](74-redes-de-transporte-voz-y-audiovisuales.md).

## Servicios de directorio

Un **directorio** es una base de datos jerárquica optimizada para lecturas que centraliza identidades y recursos: cuentas, grupos, equipos, certificados. El protocolo estándar es **LDAP** (RFC 4511), nacido como versión ligera del acceso a los directorios **X.500**: entradas identificadas por un **DN** (nombre distinguido) en un árbol (`uid=maria,ou=personal,dc=gva,dc=es`) y esquema extensible.

- **Operaciones y formato**: **bind** (autenticarse contra el directorio), **search** (la operación dominante), add/**modify**/delete y unbind; los datos se importan y exportan en ficheros de texto **LDIF**.
- **Diseño y réplica**: el árbol (**DIT**, *directory information tree*) se diseña estable (por dominios y unidades organizativas, no por organigramas cambiantes); la disponibilidad se logra replicando entre servidores (multimaestro en AD; *syncrepl* proveedor-consumidor en OpenLDAP).
- **Implementaciones**: **Active Directory** (el dominante corporativo, tema [48](48-administracion-de-sistemas-windows-y-directorio-activo.md)), **OpenLDAP** y 389 Directory Server en el mundo libre, y los directorios en la nube (Entra ID). Contraste rápido:

| | Active Directory | OpenLDAP |
| --- | --- | --- |
| Alcance | Suite completa (Kerberos, DNS, GPO) | Directorio LDAP puro |
| Esquema | Predefinido, extensible con cautela | Totalmente configurable |
| Clientes típicos | Parque Windows corporativo | Aplicaciones y sistemas UNIX |

- **Usos**: autenticación y autorización centralizadas de aplicaciones (con LDAPS), libretas de direcciones, inventario de equipos y base de la federación de identidad (tema [65](65-identificacion-y-firma-electronica.md)).

## Monitorización y gestión de logs

La monitorización vigila disponibilidad, capacidad y rendimiento, y alerta antes de que el fallo llegue al usuario; se completa con la centralización de logs para diagnóstico y auditoría.

- **Monitorización clásica de infraestructura**: **Nagios** y **Zabbix**: comprobaciones activas/pasivas **con agente** (métricas internas del host) o **sin agente** (ping, puerto, SNMP), umbrales, dependencias y alertas (correo, mensajería, guardias); a escala se trabaja con **plantillas** por tipo de equipo y **autodescubrimiento** de hosts y discos.
- **Caja negra y caja blanca**: la monitorización de caja negra prueba el servicio desde fuera, como un usuario (¿responde la web en menos de 2 segundos?); la de caja blanca lee métricas internas (colas, hilos, memoria). Se complementan: la primera detecta el síntoma, la segunda explica la causa.
- **Métricas y observabilidad**: **Prometheus** (recolección *pull* de métricas en series temporales expuestas por *exporters* como node_exporter, lenguaje PromQL, alertas con Alertmanager) con **Grafana** para cuadros de mando; estándar de facto en contenedores y Kubernetes (tema [44](44-virtualizacion-y-contenedores.md)). La observabilidad moderna añade trazas distribuidas (OpenTelemetry). La latencia se vigila por **percentiles** (p95/p99: lo que sufren los peores usuarios), no por la media, que esconde los picos.
- **Logs centralizados**: rotación local (logrotate) y reenvío por **syslog**/journald a una plataforma central: pila **ELK** (Elasticsearch, Logstash, Kibana) o Grafana Loki; retención y correlación con el SIEM de seguridad (tema [31](31-gestion-de-ciberincidentes.md)). En el ámbito público, el ENS exige activar los registros de actividad de los servidores y protegerlos (medida **op.exp.8** del RD 311/2022, tema [29](29-esquema-nacional-de-seguridad.md)).
- **Disponibilidad y niveles de servicio**: la monitorización alimenta los indicadores de los acuerdos de nivel de servicio (SLA, tema [18](18-gestion-de-los-servicios-tic.md)): los **SLI** (indicadores medidos: disponibilidad, latencia, tasa de error) se contrastan con los **SLO** internos que sostienen el SLA pactado. La disponibilidad se expresa en «nueves», valores redondos que se pactan como objetivo de servicio (no confundir con las disponibilidades de los niveles **TIER** de la infraestructura del CPD, valores propios del estándar: **99,671 a 99,995 %**, tema [43](43-centros-de-proceso-de-datos.md)):

| Disponibilidad | Indisponibilidad máxima al año |
| --- | --- |
| **99 %** | 3,65 días |
| **99,9 %** | 8,76 horas |
| **99,99 %** | 52,6 minutos |
| **99,999 %** | 5,26 minutos |

- **Gestión de red**: la supervisión SNMP de electrónica de red y el modelo FCAPS se tratan en el tema [73](73-virtualizacion-de-redes.md).

## Supuesto práctico: publicación de una aplicación web

Una consellería debe publicar en Internet una aplicación de cita previa (Java sobre Tomcat, base de datos interna) con dominio propio, notificaciones por correo y objetivo de disponibilidad del **99,9 %**. Diseño de referencia:

- **Arquitectura en DMZ**: los usuarios entran por un **balanceador HAProxy** redundado (VRRP) que reparte hacia dos **proxies inversos Nginx** en la DMZ; estos terminan **TLS** (certificados automatizados por ACME), aplican limitación de tasa y **WAF**, y pasan el tráfico a dos nodos **Tomcat** en la red interna (réplica de sesión o *sticky sessions*). La base de datos nunca es alcanzable desde la DMZ.
- **Salud y reparto**: comprobaciones de salud HTTP del balanceador contra una URL de estado de cada Tomcat; un nodo que falla se retira del reparto sin corte (la capacidad se dimensiona N+1).
- **Correo del dominio**: el envío de notificaciones sale por el **MTA corporativo** (nunca directo desde la aplicación); en el DNS se publican **SPF**, la clave **DKIM** y una política **DMARC** para que las citas no acaben en spam ni el dominio sea suplantado.
- **Monitorización**: caja negra (la URL pública respondiendo en menos del umbral desde fuera) y caja blanca (node_exporter y métricas JVM de cada nodo en **Prometheus**, cuadros en Grafana); logs de Nginx/Tomcat centralizados para el diagnóstico y el SIEM.
- **Nivel de servicio**: el SLO interno del 99,9 % admite unas **8,76 horas** de indisponibilidad al año; se mide con el SLI de disponibilidad de la sonda externa y las ventanas de mantenimiento se planifican fuera del horario de cita.

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Apache HTTP Server, Nginx, Microsoft IIS, Apache Tomcat, WildFly, Oracle WebLogic, Squid, HAProxy, Postfix, Prometheus y Zabbix, consultada en julio de 2026.
- RFC 5321 (SMTP, 2008), RFC 9051 (IMAP4rev2, 2021), RFC 7208 (SPF, 2014), RFC 6376 (DKIM, 2011), RFC 9989-9991 (DMARC, mayo de 2026; sustituyen al RFC 7489 de 2015) y RFC 4511 (LDAP, 2006).
- Real Decreto 311/2022, Esquema Nacional de Seguridad, texto consolidado, última modificación 6 de noviembre de 2024 (Anexo II, medida op.exp.8).
