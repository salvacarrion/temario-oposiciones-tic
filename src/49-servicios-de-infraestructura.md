# Servicios de infraestructura: web, correo y monitorización

Sobre los sistemas operativos de servidor (temas 47 y 48) se despliegan los servicios que sostienen las aplicaciones corporativas: servidores web y de aplicaciones, proxies y balanceadores, correo electrónico, servicios de directorio y monitorización. Los protocolos de red subyacentes se tratan en el tema 70; aquí interesa la arquitectura y la administración del lado servidor.

## Servidores web

El servidor web atiende peticiones HTTP/HTTPS y sirve contenido estático o lo delega en la capa de aplicación. Los tres dominantes:

- **Apache HTTP Server**: veterano y modular (módulos de autenticación, reescritura, TLS), procesamiento por procesos/hilos (MPM *prefork*, *worker*, *event*), configuración por directivas y ficheros `.htaccess`, hosts virtuales por nombre.
- **Nginx**: arquitectura **asíncrona orientada a eventos**, muy eficiente sirviendo estáticos y con miles de conexiones concurrentes; el uso habitual es de **proxy inverso** y terminación TLS delante de la aplicación.
- **IIS (Internet Information Services)**: el servidor web de Windows, administrado por consola o PowerShell, con aislamiento por **grupos de aplicaciones** (*application pools*) e integración con el ecosistema .NET y la autenticación de Windows.

Patrón habitual: Nginx (o Apache) delante, sirviendo estático, terminando **TLS** y pasando lo dinámico al servidor de aplicaciones; certificados automatizados (ACME/Let's Encrypt) y cabeceras de seguridad (el desarrollo seguro se trata en el tema 32).

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

- **Apache Tomcat**: contenedor de **servlets** Java (y JSP), ligero y ubicuo; el despliegue empaqueta la aplicación como **WAR**; su rendimiento se ajusta dimensionando la **JVM** (memoria, recolector de basura) y los conectores.
- **Jakarta EE completos**: **WildFly/JBoss EAP** (Red Hat) y **Oracle WebLogic** (habitual en administraciones con Oracle): clustering, colas de mensajes, transacciones distribuidas y consolas de administración de dominio.
- **Otras plataformas**: cada ecosistema trae su servidor de aplicación (procesos PHP-FPM, Gunicorn/uWSGI en Python, Node.js), normalmente detrás del proxy inverso (las plataformas de desarrollo se tratan en el tema 61).

## Proxy, proxy inverso y balanceo de carga

- **Proxy directo**: intermedia las salidas de los usuarios hacia Internet: control de acceso y filtrado de contenidos, caché y registro de navegación. El referente libre es **Squid** (ACL por origen/destino/horario, jerarquías de caché, integración con autenticación corporativa).
- **Proxy inverso**: intermedia las entradas hacia los servidores: publica aplicaciones internas, oculta la topología, termina TLS, cachea y protege (limitación de tasa; se complementa con WAF, tema 32). Lo hacen Nginx, Apache (mod_proxy) y HAProxy.
- **Balanceo de carga**: reparte peticiones entre varios servidores para escalar y tolerar fallos: algoritmos **round robin**, menos conexiones o hash de IP; **comprobaciones de salud** que retiran nodos caídos; **persistencia de sesión** (*sticky sessions*) cuando la aplicación lo exige. **HAProxy** es el balanceador software de referencia (capas 4 y 7); en nube lo dan los balanceadores gestionados, y a escala Internet las **CDN**.

## Correo electrónico y mensajería

En el correo intervienen el **MUA** (cliente), el **MTA** (agente de transferencia que encamina entre servidores por **SMTP**) y el **MDA** (entrega al buzón). El cliente lee por **IMAP** (correo en el servidor, el estándar corporativo) o POP3 (descarga), sobre puertos cifrados (SMTP **587**/465, IMAP **993**).

- **Servidores**: **Postfix** (MTA libre de referencia, con Dovecot como IMAP), **Microsoft Exchange** (integrado con AD; Exchange Online en Microsoft 365) y las plataformas SaaS (Microsoft 365, Google Workspace), mayoritarias hoy.
- **Autenticación del correo** frente a la suplantación (*spoofing*), publicada en DNS:

| Mecanismo | Qué comprueba | Registro |
| --- | --- | --- |
| **SPF** (RFC 7208) | Qué servidores pueden enviar en nombre del dominio | TXT: `v=spf1 mx ip4:194.0.2.10 -all` |
| **DKIM** (RFC 6376) | Firma criptográfica del mensaje por el dominio emisor | TXT con la clave pública (selector) |
| **DMARC** (RFC 7489) | Alineación de SPF/DKIM y política ante fallos | TXT: `v=DMARC1; p=quarantine` (none/quarantine/reject) |

- **Higiene y protección**: pasarelas antispam/antimalware, listas de bloqueo (RBL), cifrado TLS entre MTA (MTA-STS) y concienciación anti-*phishing* (tema 28).
- **Mensajería y colaboración**: la mensajería instantánea corporativa y las plataformas colaborativas (Teams, Slack y equivalentes) complementan al correo como servicio de comunicación gestionado (comunicaciones unificadas, tema 74).

## Servicios de directorio

Un **directorio** es una base de datos jerárquica optimizada para lecturas que centraliza identidades y recursos: cuentas, grupos, equipos, certificados. El protocolo estándar es **LDAP** (RFC 4511): entradas identificadas por un **DN** (nombre distinguido) en un árbol (`uid=maria,ou=personal,dc=gva,dc=es`) y esquema extensible.

- **Implementaciones**: **Active Directory** (el dominante corporativo, tema 48), **OpenLDAP** y 389 Directory Server en el mundo libre, y los directorios en la nube (Entra ID).
- **Usos**: autenticación y autorización centralizadas de aplicaciones (con LDAPS), libretas de direcciones, inventario de equipos y base de la federación de identidad (tema 65).

## Monitorización y gestión de logs

La monitorización vigila disponibilidad, capacidad y rendimiento, y alerta antes de que el fallo llegue al usuario; se completa con la centralización de logs para diagnóstico y auditoría.

- **Monitorización clásica de infraestructura**: **Nagios** y **Zabbix**: comprobaciones activas/pasivas por agente o red (ping, puerto, servicio, disco), umbrales, dependencias y alertas (correo, mensajería, guardias).
- **Métricas y observabilidad**: **Prometheus** (recolección *pull* de métricas en series temporales, lenguaje PromQL, alertas con Alertmanager) con **Grafana** para cuadros de mando; estándar de facto en contenedores y Kubernetes (tema 44). La observabilidad moderna añade trazas distribuidas (OpenTelemetry).
- **Logs centralizados**: reenvío por **syslog**/journald a una plataforma central: pila **ELK** (Elasticsearch, Logstash, Kibana) o Grafana Loki; retención y correlación con el SIEM de seguridad (tema 31).
- **Disponibilidad y niveles de servicio**: la monitorización alimenta los indicadores de los acuerdos de nivel de servicio (SLA, tema 18). La disponibilidad se expresa en «nueves», valores redondos que se pactan como objetivo de servicio (no confundir con las disponibilidades de los niveles **TIER** de la infraestructura del CPD, valores propios del estándar: **99,671 a 99,995 %**, tema 43):

| Disponibilidad | Indisponibilidad máxima al año |
| --- | --- |
| **99 %** | 3,65 días |
| **99,9 %** | 8,76 horas |
| **99,99 %** | 52,6 minutos |
| **99,999 %** | 5,26 minutos |

- **Gestión de red**: la supervisión SNMP de electrónica de red y el modelo FCAPS se tratan en el tema 73.

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Apache HTTP Server, Nginx, Microsoft IIS, Apache Tomcat, WildFly, Oracle WebLogic, Squid, HAProxy, Postfix, Prometheus y Zabbix, consultada en julio de 2026.
- RFC 5321 (SMTP, 2008), RFC 9051 (IMAP4rev2, 2021), RFC 7208 (SPF, 2014), RFC 6376 (DKIM, 2011), RFC 7489 (DMARC, 2015) y RFC 4511 (LDAP, 2006).
