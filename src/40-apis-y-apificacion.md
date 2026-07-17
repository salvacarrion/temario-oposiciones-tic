# APIs y apificación

Las APIs son el mecanismo básico de integración entre aplicaciones y la pieza sobre la que se construyen los servicios digitales modernos. Este tema cubre qué es una API y cómo se diseñan las APIs web (REST y OpenAPI), cómo se gestionan y gobiernan a escala corporativa, y qué papel juega la apificación en la transformación de empresas y administraciones.

## Qué es una API; REST y OpenAPI

Una **API** (*Application Programming Interface*, interfaz de programación de aplicaciones) es un conjunto de definiciones, protocolos y herramientas que permite que dos aplicaciones se comuniquen entre sí para intercambiar datos y funcionalidades. Actúa como un **contrato**: describe qué operaciones se pueden invocar, con qué entradas y salidas y con qué errores, sin exponer los detalles internos de la implementación (encapsulación).

- **El contrato especifica**: operaciones disponibles, formato de peticiones y respuestas, mecanismos de autenticación, códigos de error y condiciones de uso (cuotas, niveles de servicio).
- **Ámbito**: existen APIs locales (bibliotecas, servicios del sistema operativo) y APIs web o remotas, que exponen servicios a través de la red. El resto del tema se centra en las segundas.
- **Según su visibilidad**:
    - **Privadas (internas)**: integran sistemas de la propia organización.
    - **De socios (*partner*)**: expuestas a colaboradores concretos bajo acuerdo.
    - **Públicas (abiertas)**: disponibles para cualquier desarrollador, con o sin registro previo.

### Estilos de APIs web

| Estilo | Características | Uso típico |
| --- | --- | --- |
| SOAP | Protocolo basado en XML, contrato WSDL, extensiones WS-* (seguridad, transacciones) | Integraciones corporativas y servicios heredados |
| REST | Estilo arquitectónico sobre HTTP: recursos identificados por URI, representaciones habitualmente JSON | El estilo dominante en APIs web de propósito general |
| GraphQL | Lenguaje de consultas (Facebook, liberado en 2015): el cliente pide exactamente los campos que necesita a un único *endpoint* | Frontales con necesidades de datos variables |
| gRPC | *Framework* RPC (Google, 2015) sobre HTTP/2 con mensajes binarios Protocol Buffers | Comunicación interna entre microservicios de alto rendimiento |
| Asíncronas | Orientadas a eventos: *webhooks*, colas de mensajes, publicación/suscripción; se describen con AsyncAPI | Notificaciones y procesamiento en tiempo real |

Los servicios web SOAP y la arquitectura SOA se desarrollan en el tema [60](60-soa-servicios-web-y-microservicios.md).

### REST

**REST** (*Representational State Transfer*) es un estilo arquitectónico formulado por **Roy Fielding** en su tesis doctoral (**2000**). Una API que cumple sus restricciones se denomina *RESTful*.

- **Restricciones (6)**: cliente-servidor; **sin estado** (cada petición contiene toda la información necesaria, el servidor no guarda sesión); **cacheable**; **interfaz uniforme**; **sistema en capas**; y código bajo demanda (la única opcional).
- **Recursos**: toda información se modela como un recurso identificado por una **URI** (por ejemplo, `/expedientes/123`). El cliente no manipula el recurso directamente sino sus **representaciones**, normalmente en **JSON** (RFC 8259), aunque el formato es negociable (XML, CSV...).
- **Métodos HTTP** (semántica definida en RFC 9110):
    - **GET**: consulta un recurso (seguro e idempotente).
    - **POST**: crea un recurso o dispara un proceso (no idempotente).
    - **PUT**: sustituye un recurso completo (idempotente).
    - **PATCH**: modifica parcialmente un recurso.
    - **DELETE**: elimina un recurso (idempotente).
- **Códigos de estado**: **2xx** éxito (200 OK, 201 Created, 204 No Content); **3xx** redirección (304 Not Modified); **4xx** error del cliente (400 petición incorrecta, 401 no autenticado, 403 prohibido, 404 no encontrado, 429 demasiadas peticiones); **5xx** error del servidor (500, 503). Para el cuerpo de los errores existe el formato estándar *Problem Details* (RFC 9457).
- **Convenciones habituales**: paginación, filtrado y ordenación mediante parámetros de consulta (`?page=2&sort=fecha`).
- **HATEOAS** (*Hypermedia As The Engine Of Application State*): las respuestas incluyen enlaces a las acciones posibles, de modo que el cliente navega la API como se navega la web.
- **Modelo de madurez de Richardson**: gradúa cuán RESTful es una API en **4 niveles**: 0 (HTTP como mero transporte), 1 (recursos con URI propias), 2 (verbos HTTP y códigos de estado, el nivel habitual en la práctica) y 3 (HATEOAS).
- **Versionado**: en la URI (`/v1/...`), en cabeceras o por negociación de contenido; permite evolucionar la API sin romper las aplicaciones consumidoras.

### OpenAPI

La **OpenAPI Specification (OAS)** es el formato estándar para describir APIs REST en un documento legible por máquinas (YAML o JSON). Nació como **Swagger** (2011) y en **2015** fue donada a la **OpenAPI Initiative**, consorcio de la **Linux Foundation** que la mantiene desde entonces.

- **Versión vigente**: **3.2.0 (septiembre de 2025)**; las ramas 3.0 y 3.1 siguen siendo las más extendidas en herramientas y pasarelas.
- **Qué describe**: rutas y operaciones, parámetros, esquemas de datos (basados en JSON Schema), mecanismos de autenticación, ejemplos y servidores.
- **Para qué sirve**: documentación interactiva (Swagger UI, Redoc), generación automática de código cliente y servidor, *mocks* para desarrollar en paralelo, pruebas automatizadas y configuración de pasarelas.
- **Diseño *contract-first* (o *API-first*)**: definir primero el contrato OpenAPI y programar después. Garantiza coherencia, permite validar el diseño con los consumidores antes de implementar y habilita el trabajo en paralelo de varios equipos.

## Gestión y gobierno de APIs

Cuando las APIs se multiplican dejan de ser un asunto de cada proyecto y pasan a tratarse como activos corporativos: la **gestión** cubre la operación diaria y el ciclo de vida de cada API; el **gobierno**, las políticas y estándares comunes a todas.

- **Ciclo de vida de una API**: diseño, desarrollo y pruebas, publicación, operación y monitorización, evolución con nuevas versiones y, finalmente, **deprecación** y retirada (anunciada con plazos a los consumidores).

La **gestión de APIs** (*API management*) se apoya en plataformas que centralizan su publicación y operación:

- **Pasarela (API gateway)**: punto único de entrada a las APIs. Se ocupa del enrutado, la autenticación y autorización, los **límites de uso** (*rate limiting* y cuotas), la caché, la transformación de mensajes y el registro de trazas.
- **Portal del desarrollador**: catálogo de las APIs publicadas con su documentación, alta de aplicaciones consumidoras y emisión de credenciales.
- **Analítica**: métricas de uso, rendimiento, errores y consumidores; es la base para verificar los niveles de servicio y planificar capacidad.
- **Plataformas habituales**: Google Apigee, Azure API Management, Amazon API Gateway, Kong, WSO2 API Manager, MuleSoft Anypoint, Red Hat 3scale.

La **seguridad de las APIs** merece atención específica, porque exponen directamente datos y lógica de negocio:

- **Mecanismos**: claves de API (identifican la aplicación consumidora), **OAuth 2.0** (RFC 6749, autorización delegada), **OpenID Connect** (autenticación sobre OAuth 2.0), *tokens* **JWT** (RFC 7519) y TLS mutuo (mTLS) entre sistemas.
- **OWASP API Security Top 10 (edición 2023)**: catálogo de referencia de los riesgos propios de las APIs. Lo encabezan los fallos de autorización: a nivel de objeto (**BOLA**, riesgo n.º 1), a nivel de propiedad del objeto y a nivel de función; siguen la autenticación rota, el consumo de recursos sin restricciones, el acceso sin límites a flujos de negocio sensibles, el SSRF, las configuraciones incorrectas, la gestión deficiente del inventario (APIs «sombra» y «zombis») y el consumo inseguro de APIs de terceros.

El **gobierno de APIs** define el marco común para que todas las APIs de la organización sean coherentes, seguras y localizables:

- **Estándares de diseño**: guía de estilo corporativa (convenciones de nombres, paginación, gestión de errores, versionado).
- **Catálogo e inventario**: registro único de APIs y versiones; evita duplicidades y APIs fuera de control.
- **Políticas**: seguridad y protección de datos, planes y límites de consumo, condiciones de uso.
- **Monetización**: modelos gratuito, *freemium*, pago por uso o suscripción. En la Administración lo habitual es el acceso gratuito con límites de uso.
- **Roles**: propietario de cada API como producto, oficina o centro de excelencia de APIs (arquitectura, estándares) y equipos consumidores.

## La apificación en la Administración

La **apificación** es la estrategia de exponer los datos y funcionalidades de los sistemas de una organización como APIs reutilizables, tratando cada API como un **producto** con sus consumidores, su ciclo de vida y sus métricas. Sobre ella se asienta la **economía de las APIs**: el valor que generan los servicios de unos actores al integrarse en los productos de otros.

- **Origen empresarial**: las grandes plataformas digitales (pagos, mapas, mensajería, autenticación) crecieron ofreciendo sus capacidades como APIs a terceros. En Europa, el **open banking** de la Directiva **PSD2** (Directiva (UE) **2015/2366**) obligó a la banca a exponer APIs de acceso a cuentas y pagos a proveedores autorizados.
- **Qué aporta**: reutilización de servicios existentes, integración ágil con terceros, innovación (los reutilizadores crean servicios que la organización no había previsto) y desacoplamiento entre sistemas.

En la Administración pública, la apificación sustenta tres ámbitos principales:

- **Interoperabilidad entre administraciones**: los servicios de verificación y consulta de datos (Plataforma de Intermediación de Datos y demás soluciones compartidas) se consumen como servicios web, para no exigir al ciudadano documentos que ya obran en poder de la Administración. Se desarrollan en el tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md).
- **Datos abiertos y reutilización (RISP)**: las APIs son el canal preferente para publicar datos dinámicos y en tiempo real. La **Iniciativa Aporta** publica la «Guía práctica para la publicación de datos abiertos usando APIs» (datos.gob.es, versión de **febrero de 2025**), con pautas para el sector público: documentar con OpenAPI, versionar, establecer límites de uso, ofrecer datos actualizados y monitorizar el servicio. Además, el Reglamento de Ejecución (UE) **2023/138** exige que los **conjuntos de datos de alto valor** (geoespaciales, meteorológicos, estadísticos, movilidad, medio ambiente, sociedades) se publiquen también mediante APIs.
- **Servicios públicos digitales**: exponer los trámites y servicios como APIs permite que terceros (gestorías, aplicaciones ciudadanas, otras administraciones) los integren, y es la base de servicios proactivos y personalizados.

Ejemplos de APIs públicas en España:

- **datos.gob.es**: API del catálogo nacional de datos abiertos, para consultar y federar conjuntos de datos.
- **AEMET OpenData**: API REST de datos meteorológicos y climatológicos.
- **INE**: API de difusión estadística (sistema Tempus3).
- **CNIG/IDEE**: servicios OGC y OGC API de información geográfica (tema [67](67-infraestructuras-de-datos-espaciales.md)).

Los beneficios para la Administración son la **transparencia** (acceso automatizable a la información pública), la **eficiencia** (servicios comunes reutilizados por muchos organismos), la mejora del servicio al ciudadano y la creación de un ecosistema **infomediario** que genera valor económico sobre los datos públicos.

## Fuentes {.unnumbered .unlisted}

- Fielding, R. T.: *Architectural Styles and the Design of Network-based Software Architectures*, tesis doctoral, Universidad de California en Irvine, 2000 (capítulo 5: REST).
- RFC 9110 *HTTP Semantics* (IETF, junio de 2022); RFC 8259 *The JavaScript Object Notation (JSON) Data Interchange Format* (IETF, diciembre de 2017); RFC 9457 *Problem Details for HTTP APIs* (IETF, julio de 2023).
- OpenAPI Specification v3.2.0, OpenAPI Initiative (Linux Foundation), septiembre de 2025.
- OWASP API Security Top 10, edición 2023.
- «Guía práctica para la publicación de datos abiertos usando APIs», Iniciativa Aporta (datos.gob.es), versión de febrero de 2025.
- Reglamento de Ejecución (UE) 2023/138 de la Comisión, relativo a los conjuntos de datos de alto valor (DOUE 20 de enero de 2023).
