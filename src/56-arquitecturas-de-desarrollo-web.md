# Arquitecturas de desarrollo web

## Arquitectura multicapa y modelo de aplicaciones web

Una aplicación web es una aplicación **cliente-servidor** en la que el cliente es un navegador, la comunicación se realiza sobre **HTTP/HTTPS** y la interfaz se construye con tecnologías estándar (HTML, CSS, JavaScript). Su arquitectura define cómo se reparten la presentación, la lógica de negocio y los datos entre el cliente y el servidor, y ha evolucionado desde la página estática hasta las aplicaciones distribuidas basadas en APIs.

- **Modelo cliente-servidor**: el cliente (navegador) solicita recursos mediante peticiones HTTP; el servidor los procesa y devuelve una respuesta (HTML, datos, ficheros). HTTP es un protocolo **sin estado**: cada petición es independiente, y el estado de la sesión se mantiene con mecanismos adicionales (cookies, tokens, almacenamiento en servidor).
- **Cliente ligero**: el navegador actúa como cliente universal: no hay que instalar ni distribuir software específico, y las actualizaciones se despliegan una sola vez en el servidor. Es la ventaja histórica de la web frente a las aplicaciones de escritorio.

**Evolución del modelo**:

- **Web estática (años 90)**: el servidor entrega ficheros HTML fijos; cualquier cambio exige editar la página.
- **Web dinámica (CGI, PHP, JSP, ASP)**: el servidor genera el HTML en cada petición a partir de plantillas y datos (formularios, bases de datos).
- **AJAX (término acuñado en 2005)**: JavaScript pide datos al servidor en segundo plano (*XMLHttpRequest*, hoy *fetch*) y actualiza partes de la página sin recargarla entera.
- **SPA y APIs (década de 2010)**: el navegador ejecuta una aplicación JavaScript completa que consume APIs (JSON); el servidor pasa de generar páginas a exponer servicios.

**Arquitectura multicapa**:

- **Tres capas (three-tier)**: modelo de referencia de las aplicaciones web:
    - **Presentación**: interfaz de usuario; en la web, el navegador y el código front-end.
    - **Lógica de negocio**: reglas y procesos de la aplicación; se ejecuta en el servidor de aplicaciones.
    - **Acceso a datos**: persistencia y consulta; sistemas gestores de bases de datos.
- **Capa frente a nivel**: la **capa** (*layer*) es una separación lógica del código; el **nivel** (*tier*) es la separación física en máquinas distintas. Una aplicación de tres capas puede desplegarse en uno, dos o tres niveles.
- **N capas**: la separación puede refinarse (capa de servicios, capa de integración) o distribuirse en servicios independientes (microservicios, tema [60](60-soa-servicios-web-y-microservicios.md)).
- **Ventajas de separar capas**: mantenibilidad (cambios localizados), escalabilidad independiente de cada nivel, reutilización de la lógica por varios clientes (web, móvil, terceros vía API) y seguridad (la base de datos nunca se expone directamente al cliente).

**Patrones de presentación**:

- **MVC (modelo-vista-controlador)**: separa los datos (modelo), la interfaz (vista) y el control del flujo (controlador). Es el patrón clásico de los frameworks de servidor (Spring MVC, Django, Laravel, ASP.NET MVC).
- **Variantes**: **MVP** (presentador que media entre vista y modelo) y **MVVM** (modelo-vista-vista-modelo, con enlace de datos bidireccional), habituales en frameworks de cliente y móviles.

**Servidor web y servidor de aplicaciones**:

- **Servidor web**: atiende peticiones HTTP y sirve contenido estático; suele actuar además como proxy inverso hacia la lógica. Ejemplos: **Apache HTTP Server**, **Nginx**.
- **Servidor de aplicaciones**: ejecuta la lógica de negocio y ofrece servicios a las aplicaciones (gestión de transacciones, pools de conexiones, seguridad). Ejemplos en Java: **Tomcat** (contenedor de servlets), **WildFly/JBoss** (Java EE/Jakarta EE completo).

## Desarrollo front-end

El front-end es la parte de la aplicación que se ejecuta en el navegador. Sus tres lenguajes base son estándar del W3C/WHATWG y ECMA: **HTML** (estructura), **CSS** (presentación) y **JavaScript** (comportamiento); se desarrollan en el tema [57](57-tecnologias-web.md). Lo arquitectónicamente relevante es dónde y cuándo se genera el HTML que ve el usuario: los modelos de renderizado.

**Modelos de aplicación y renderizado**:

- **MPA (aplicación multipágina)**: modelo clásico. Cada navegación solicita al servidor una página completa, que llega ya renderizada. Sencillo y bueno para SEO; la experiencia es menos fluida (recarga completa en cada paso).
- **SPA (Single Page Application)**: se carga una única página HTML con un paquete JavaScript y, a partir de ahí, la aplicación corre en el navegador: gestiona la navegación, actualiza el DOM y pide al servidor solo datos (JSON) a través de una API. Ofrece experiencia de aplicación de escritorio; a cambio, la carga inicial es mayor y el SEO y la accesibilidad exigen más trabajo.
- **CSR (renderizado en cliente)**: el HTML inicial llega casi vacío y JavaScript construye la interfaz en el navegador. Es el modo natural de una SPA.
- **SSR (renderizado en servidor)**: el servidor devuelve el HTML ya construido. Incluye tanto la web dinámica clásica como el SSR moderno de los frameworks JavaScript universales, donde el servidor renderiza la primera vista con el mismo código de componentes que ejecutará el cliente.
- **Hidratación**: proceso por el que, tras un SSR moderno, el JavaScript descargado en el cliente «toma el control» del HTML recibido (adjunta los manejadores de eventos y el estado) sin volver a construirlo. Convierte la página estática inicial en una SPA interactiva.
- **SSG (generación estática)**: las páginas se generan en el momento de la construcción (*build*) y se sirven como ficheros estáticos, idealmente desde una CDN. Máximo rendimiento; solo apto para contenido que no cambia por usuario ni por minuto.
- **Enfoques híbridos**: los metaframeworks actuales (**Next.js** sobre React, **Nuxt** sobre Vue, SSR de **Angular**) permiten elegir el modelo por ruta y combinarlos (SSR para la portada, CSR para el área privada, SSG para la documentación).

| Modelo | Dónde se genera el HTML | A favor | En contra |
| --- | --- | --- | --- |
| MPA clásica | Servidor, en cada petición | SEO, simplicidad | Recarga completa |
| SPA (CSR) | Cliente (JavaScript) | Interactividad, API reutilizable | Carga inicial, SEO |
| SSR moderno | Servidor + hidratación en cliente | Primera carga rápida y SEO sin renunciar a SPA | Complejidad, coste de servidor |
| SSG | En la construcción (build) | Rendimiento máximo, CDN | Contenido poco dinámico |

**Frameworks de cliente**: la construcción de SPAs se apoya en frameworks basados en componentes reutilizables con estado.

- **React** (Meta, 2013): biblioteca de interfaces de usuario declarativa; componentes, **DOM virtual** (recalcula los cambios mínimos a aplicar), sintaxis **JSX** y flujo de datos unidireccional. Es la más extendida; delega enrutado y estado global en su ecosistema (React Router, Redux) o en Next.js.
- **Angular** (Google, 2016, sucesor de AngularJS): framework completo y opinado: TypeScript obligatorio, inyección de dependencias, enrutado y formularios incluidos. Frecuente en entornos corporativos.
- **Vue** (2014): framework progresivo: puede adoptarse gradualmente desde una página existente o usarse como SPA completa con su ecosistema (Nuxt, Pinia). Curva de entrada suave.

**Herramientas del ecosistema**:

- **TypeScript** (Microsoft, 2012): superconjunto de JavaScript con tipado estático que se transpila a JavaScript; estándar de facto en proyectos medianos y grandes por la detección temprana de errores.
- **npm**: gestor de paquetes de Node.js y mayor registro público de dependencias; define los proyectos mediante `package.json`.
- **Empaquetadores (bundlers)**: transforman y agrupan módulos, hojas de estilo y activos para producción (minificación, división de código). **Vite** es el estándar actual por su velocidad; **Webpack** pervive en proyectos existentes.
- **Preprocesadores CSS** (Sass/LESS) y *frameworks* CSS utilitarios: aceleran la escritura de estilos coherentes.

El diseño adaptativo (*responsive*) y la accesibilidad del front-end se tratan en el tema [58](58-accesibilidad-y-usabilidad.md); las aplicaciones web progresivas (PWA), en el tema [59](59-desarrollo-de-aplicaciones-moviles.md).

## Desarrollo en servidor y conexión a bases de datos

El back-end ejecuta la lógica de negocio, expone las APIs, aplica la seguridad y persiste los datos. Cualquier lenguaje de propósito general sirve; en la práctica dominan unos pocos stacks consolidados.

**Stacks de servidor**:

- **Java + Spring**: plataforma empresarial por excelencia; **Spring Boot** simplifica la configuración y embebe el servidor (Tomcat). Inyección de dependencias, Spring MVC para web y APIs, Spring Data para persistencia. Muy habitual en las administraciones públicas.
- **PHP**: lenguaje histórico de la web dinámica; motoriza WordPress y Drupal. Frameworks modernos: **Laravel** y **Symfony**.
- **Python**: **Django** (framework «con pilas incluidas»: ORM, autenticación y administración de serie) y **Flask**/**FastAPI** (microframeworks; FastAPI, orientado a APIs con validación por tipos).
- **Node.js** (2009): entorno de ejecución de JavaScript en servidor sobre el motor **V8**; modelo asíncrono orientado a eventos, eficiente en entrada/salida concurrente, y un único lenguaje en toda la pila. Frameworks: **Express** (minimalista) y **NestJS** (estructurado, TypeScript).
- **.NET / ASP.NET Core** (Microsoft): multiplataforma y de código abierto desde 2016; lenguaje C#, alto rendimiento e integración natural con el ecosistema Microsoft.

**Conexión a bases de datos**:

- **Drivers y APIs de acceso**: interfaz estándar entre el lenguaje y el gestor: **JDBC** en Java, **ODBC** como estándar genérico, drivers nativos en cada lenguaje.
- **Pool de conexiones**: abrir una conexión es costoso; el servidor mantiene un conjunto de conexiones abiertas que las peticiones reutilizan. Imprescindible para rendir bajo carga.
- **ORM (mapeo objeto-relacional)**: traduce entre objetos del lenguaje y tablas relacionales, generando el SQL: **Hibernate/JPA** (Java), **Entity Framework** (.NET), **Sequelize** y **Prisma** (Node.js), el ORM de Django. Aportan productividad y portabilidad; sus riesgos clásicos son las consultas N+1 y la pérdida de control sobre el SQL generado.
- **Relacionales frente a NoSQL**: relacionales de referencia (**PostgreSQL**, **MySQL**, **Oracle**) para datos estructurados y transacciones; NoSQL según el caso: **MongoDB** (documentos), **Redis** (clave-valor en memoria), **Cassandra** (columnar distribuida). Se desarrollan en el tema [36](36-bases-de-datos.md).
- **Sesiones y caché**: para escalar horizontalmente, el estado de sesión y la caché se externalizan del proceso web a un almacén compartido (Redis, Memcached); así cualquier instancia puede atender a cualquier usuario.

## Interconexión con sistemas y servicios

Una aplicación web rara vez vive aislada: consume y expone APIs, se integra con sistemas corporativos mediante mensajería y delega la identidad en servicios de autenticación. La interconexión se apoya en estándares abiertos sobre HTTP.

**Estilos y protocolos de integración**:

- **APIs REST**: estilo dominante: recursos identificados por URI, métodos HTTP con semántica estándar y representaciones JSON. Se desarrollan en los temas [40](40-apis-y-apificacion.md) (APIs y apificación) y 56 (servicios web).
- **GraphQL** (Meta, publicado en 2015): lenguaje de consulta para APIs con un único punto de entrada; el cliente pide exactamente los campos que necesita, evitando el exceso o defecto de datos (*over/under-fetching*) típico de REST en clientes móviles.
- **gRPC** (Google, 2015): framework RPC de alto rendimiento sobre **HTTP/2** con serialización binaria **Protocol Buffers**; habitual en comunicación interna entre microservicios.
- **WebSocket** (**RFC 6455**): canal bidireccional persistente entre navegador y servidor sobre una conexión HTTP «mejorada» (*upgrade*); base del tiempo real (chat, notificaciones, paneles). Alternativa unidireccional más simple: *Server-Sent Events*.
- **Webhooks**: integración inversa: el proveedor invoca por HTTP una URL del consumidor cuando ocurre un evento, en lugar de que este pregunte periódicamente (*polling*).
- **Mensajería asíncrona**: colas y publicación/suscripción desacoplan sistemas en el tiempo: **RabbitMQ** (broker de colas, protocolo AMQP) y **Apache Kafka** (registro de eventos distribuido para gran volumen y streaming).

**Autenticación y autorización**:

- **OAuth 2.0** (**RFC 6749**): marco de **autorización delegada**: el usuario autoriza a una aplicación a acceder a sus recursos en otro servicio sin entregarle su contraseña, mediante tokens de acceso.
- **OpenID Connect (OIDC)**: capa de **identidad** sobre OAuth 2.0; añade el *ID token* y estandariza el inicio de sesión federado («entrar con» un proveedor de identidad).
- **JWT (JSON Web Token, RFC 7519)**: token autocontenido y firmado con las declaraciones (*claims*) del usuario; el servidor lo valida sin consultar estado, lo que facilita escalar y asegurar APIs.
- **SAML 2.0**: federación de identidad clásica basada en XML; sigue siendo común en el single sign-on corporativo y universitario. La identificación electrónica en la Administración (Cl@ve, certificados) se trata en el tema [65](65-identificacion-y-firma-electronica.md).
- **LDAP / Active Directory**: directorio corporativo de usuarios y grupos contra el que se autentica y autoriza en entornos internos.

**Infraestructura de entrega**:

- **Proxy inverso y balanceador de carga**: reciben el tráfico y lo reparten entre instancias de la aplicación (Nginx, HAProxy, balanceadores en nube); punto natural para terminar TLS, cachear y filtrar.
- **CDN (red de distribución de contenido)**: réplicas geográficamente distribuidas que sirven el contenido estático cerca del usuario, reduciendo latencia y descargando el origen.
- **HTTP/2 y HTTP/3**: multiplexación de peticiones sobre una conexión (HTTP/2) y transporte **QUIC** sobre UDP (HTTP/3), que reducen la latencia de carga; se detallan en el tema [70](70-protocolos-de-comunicaciones.md).
- **HTTPS/TLS**: el cifrado del canal es hoy requisito por defecto de cualquier aplicación web; la criptografía y la seguridad de las comunicaciones se tratan en los temas [64](64-criptografia.md) y [79](79-seguridad-en-las-comunicaciones.md).

## Supuesto práctico: arquitectura de una aplicación web de cita previa

**Enunciado**: una Administración autonómica necesita una aplicación de **cita previa** para su red de oficinas de asistencia: la ciudadanía reserva, consulta y anula citas desde la web y el móvil, y el personal gestiona agendas y calendarios. Requisitos: **200.000 usuarios al mes** con picos de **500 peticiones por segundo** al abrirse las agendas más demandadas; disponibilidad del **99,9 %**; datos personales en sistemas de **categoría MEDIA** del ENS; el equipo de desarrollo domina **Java/Spring** y la plataforma corporativa es un clúster de **Kubernetes** en nube privada.

**Se pide**:

- a) Proponer la arquitectura lógica y el modelo de renderizado del front-end.
- b) Diseñar el back-end y su API, incluida la gestión del estado.
- c) Resolver la escalabilidad y la alta disponibilidad para los picos.
- d) Plantear la seguridad y las integraciones.
- e) Definir entornos, despliegue y observabilidad.

**Resolución**:

**a) Arquitectura lógica y front-end**

- **Tres capas** desplegadas en niveles separados: presentación (front-end en el navegador), lógica de negocio (API en el clúster) y datos (SGBD), de modo que cada nivel escala por separado y la base de datos nunca se expone al cliente.
- **Front-end**: **SPA** basada en componentes (React o Angular, este último frecuente en entornos corporativos) que consume la API JSON. Para la parte pública (información, primera carga) conviene un enfoque **híbrido con SSR o SSG**, que acelera la primera carga y facilita el posicionamiento; el área de reservas funciona como SPA (CSR). La accesibilidad es obligación legal (RD 1112/2018, tema [58](58-accesibilidad-y-usabilidad.md)) y se valida desde el diseño.
- **Contenido estático** (aplicación JavaScript, imágenes) servido desde el proxy inverso o la CDN, no desde la aplicación.

**b) Back-end y API**

- **API REST** con Spring Boot: recursos (`/oficinas`, `/franjas`, `/citas`), verbos y códigos HTTP con semántica estándar, versionado (`/v1`) y especificación **OpenAPI** publicada, reutilizable por la app móvil o por terceros (tema [40](40-apis-y-apificacion.md)).
- **Sin estado (stateless)**: cualquier instancia atiende cualquier petición; la sesión y la caché se externalizan a **Redis** y la autenticación viaja en **tokens JWT** de corta duración.
- **Persistencia**: **PostgreSQL** con **JPA/Hibernate**, **pool de conexiones** (imprescindible bajo carga) y vigilancia de las consultas N+1.
- **Integridad de la reserva**: la asignación de franja es transaccional, con **restricción de unicidad** (oficina, franja) y bloqueo optimista: dos usuarios no pueden quedarse la misma cita.

**c) Escalabilidad y alta disponibilidad**

- **Escalado horizontal**: réplicas stateless tras el balanceador (Ingress); **autoescalado** por CPU y latencia (por ejemplo, entre 4 y 12 réplicas si cada instancia sostiene del orden de 100-150 peticiones por segundo con margen).
- **Absorber el pico de 500 peticiones/s**: la consulta de disponibilidad (la operación masiva) se sirve desde la **caché Redis con TTL corto**; **limitación de tasa** por usuario en el punto de entrada y, para campañas extremas, sala de espera virtual que encola el exceso.
- **Sin punto único de fallo**: al menos **2 réplicas** de cada componente en nodos distintos, base de datos con **réplica** y conmutación, Redis en clúster y despliegues **rolling update** sin corte. El objetivo del 99,9 % admite unas **8,8 horas** de indisponibilidad al año: exige redundancia y ensayo de los fallos, no infraestructura exótica.
- **Asíncrono**: la confirmación por correo o SMS sale por una **cola de mensajería** (RabbitMQ): un envío lento no bloquea la reserva.

**d) Seguridad e integraciones**

- **Perímetro**: TLS en todo el recorrido, **WAF** delante del balanceador, cabeceras de seguridad y desarrollo conforme a OWASP (tema [32](32-desarrollo-seguro-de-aplicaciones.md)).
- **Identidad**: la ciudadanía se identifica con **Cl@ve** o certificado a través de **OIDC** contra el proveedor de identidad corporativo (tema [65](65-identificacion-y-firma-electronica.md)); el personal, contra el directorio corporativo (LDAP/AD) con el mismo patrón OIDC o SAML.
- **ENS categoría MEDIA**: registro de actividad centralizado, control de acceso por perfiles y copias y continuidad heredadas de la plataforma; **minimización** de datos personales (solo los necesarios para la cita) conforme al RGPD (tema [53](53-proteccion-de-datos-personales.md)).
- **Integraciones**: API y webhooks con el sistema de gestión de turnos de las oficinas y con la pasarela de avisos SMS.

**e) Entornos, despliegue y observabilidad**

- **Tres entornos** (desarrollo, preproducción y producción) idénticos y definidos como código.
- **CI/CD** (tema [26](26-control-de-versiones-integracion-continua-y-devops.md)): pipeline con compilación, pruebas, análisis estático, construcción de la imagen de contenedor y despliegue declarativo en Kubernetes (tema [44](44-virtualizacion-y-contenedores.md)).
- **Observabilidad**: métricas (Prometheus/Grafana), logs centralizados y trazas distribuidas; **pruebas de carga** antes de cada campaña, simulando al menos el doble del pico previsto (1.000 peticiones por segundo).

## Fuentes {.unnumbered .unlisted}

- MDN Web Docs (Mozilla): referencia de tecnologías y arquitectura web (consulta: julio de 2026).
- Documentación oficial de React, Angular, Vue, Next.js, Spring, Django y Node.js (consulta: julio de 2026).
- RFC 6455 (WebSocket, 2011), RFC 6749 (OAuth 2.0, 2012), RFC 7519 (JWT, 2015).
- M. Fowler, *Patterns of Enterprise Application Architecture* (2002), para el modelo de capas y patrones de presentación.
