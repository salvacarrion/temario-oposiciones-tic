# SOA, servicios web y microservicios

## La arquitectura orientada a servicios (SOA); el ESB

La **arquitectura orientada a servicios (SOA)** es un estilo de diseño que organiza la funcionalidad de los sistemas en **servicios** reutilizables, accesibles a través de interfaces estandarizadas e independientes de la plataforma. Surgió a principios de los 2000 para integrar los sistemas heterogéneos de las grandes organizaciones alineándolos con sus procesos de negocio.

- **Objetivos**: **agilidad** (componer soluciones nuevas a partir de servicios existentes), **reutilización** (cada funcionalidad se construye una vez) y **federación** (sistemas heterogéneos cooperando bajo normas comunes).
- **Principios del diseño de servicios**: contrato estandarizado, **bajo acoplamiento**, **abstracción** (el servicio es una caja negra), reutilización, autonomía, **ausencia de estado**, capacidad de **descubrimiento** y capacidad de **composición** en procesos mayores.
- **Elementos de un servicio**: la **lógica** (implementación), la **descripción o contrato** (qué hace y bajo qué condiciones) y la **interfaz** (punto de acceso para invocarlo).
- **El triángulo SOA**: el **proveedor** publica la descripción del servicio en un **registro**; el **consumidor** lo descubre allí y se enlaza con el proveedor para invocarlo (publicar, descubrir, enlazar).
- **Interoperabilidad del mensaje**: **sintáctica** (formato común de los mensajes) y **semántica** (significado compartido de los datos).

**Arquitectura de capas de referencia**: el modelo de referencia organiza un sistema SOA en capas **horizontales** (funcionales, de abajo arriba) atravesadas por capas **verticales** (transversales a todas):

- **Horizontales**: 1) **sistemas operacionales** (aplicaciones existentes, bases de datos); 2) **componentes de servicio** (desvinculan el servicio de la tecnología subyacente); 3) **servicios**, simples o compuestos; 4) **procesos de negocio** (composición de servicios con un objetivo empresarial); 5) **consumidores** (presentación y acceso).
- **Verticales**: **integración** (conectividad entre capas), **calidad de servicio** (seguridad, rendimiento, disponibilidad), **información** (modelo de datos común) y **gobierno** (normas de diseño, ciclo de vida y catálogo de servicios).

**Ciclo de vida de un servicio**: análisis del inventario de servicios, modelado, diseño del contrato, diseño de la lógica, implementación, pruebas, publicación en el registro, monitorización y mejora continua.

**Composición de servicios**: dos estilos de coordinación:

- **Orquestación**: un elemento central (el orquestador) controla el flujo e invoca a los servicios en el orden debido; es el modelo de **WS-BPEL**. Máximo control, pero dependencia del coordinador.
- **Coreografía**: no hay control central; cada servicio conoce las reglas de la interacción y reacciona a los mensajes o eventos de los demás. Más escalable y desacoplada, más difícil de seguir de extremo a extremo.

**El bus de servicios empresarial (ESB)**: es la infraestructura de integración característica de SOA: un middleware por el que circulan los mensajes entre consumidores y proveedores, en lugar de conexiones punto a punto.

- **Funciones**: **enrutado** inteligente de mensajes (por contenido, por reglas), **transformación** de formatos y modelos de datos, **conversión de protocolos** (SOAP, REST, colas de mensajes, ficheros), mediación entre versiones de servicios, seguridad centralizada, registro y monitorización.
- **Productos de referencia**: Mule (MuleSoft), WSO2, IBM App Connect Enterprise (heredero de WebSphere ESB), Oracle Service Bus, Apache Camel como framework de integración.
- **Balance**: el ESB desacopla e integra lo heterogéneo, pero tiende a concentrar lógica de negocio y a convertirse en cuello de botella técnico y organizativo. La reacción a ese modelo («tuberías inteligentes») es uno de los orígenes de los microservicios.

## Servicios web y estándares: SOAP, WSDL y UDDI

Los servicios web son la materialización clásica de SOA. Según el **W3C**, un servicio web es «un sistema software diseñado para soportar la interacción máquina a máquina a través de una red de forma interoperable», con una interfaz descrita en formato procesable (**WSDL**) e invocable mediante mensajes **SOAP**, típicamente XML sobre **HTTP**. La pila clásica se completa con **UDDI** para el descubrimiento y las extensiones **WS-\***.

**SOAP**: protocolo de mensajería basado en XML (originalmente «Simple Object Access Protocol»; desde la versión **1.2**, Recomendación W3C, el nombre ya no es un acrónimo).

- **Propiedades**: **neutral al transporte** (HTTP es lo habitual; también SMTP o colas de mensajes), **extensible** mediante el Header (seguridad, direccionamiento, fiabilidad) e **independiente** del lenguaje y modelo de programación; sin estado entre peticiones.
- **Estructura del mensaje** (documento XML): **Envelope** (raíz obligatoria que identifica el mensaje como SOAP), **Header** (opcional, información de procesamiento y extensiones), **Body** (obligatorio, la carga útil de la llamada o respuesta) y **Fault** (bloque dentro del Body con la información de error).

```xml
<?xml version="1.0"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header>...</env:Header>
  <env:Body>...</env:Body>
</env:Envelope>
```

- **Modelo de procesado**: el mensaje recorre una ruta (*message path*) desde el **emisor inicial**, a través de **intermediarios** que pueden procesar partes del Header, hasta el **receptor último**, que procesa el Body.
- **MTOM**: mecanismo del W3C para transmitir eficientemente contenido binario en mensajes SOAP, evitando el sobrecoste de la codificación base64.

**WSDL (Web Services Description Language)**: lenguaje XML que describe el contrato del servicio: qué operaciones ofrece, con qué mensajes y tipos de datos, sobre qué protocolo y en qué dirección.

- **Estructura (WSDL 1.1)**: **types** (tipos de datos, normalmente XML Schema), **message** (mensajes intercambiados), **portType** (las operaciones abstractas), **binding** (protocolo y formato concretos) y **service**/**port** (dirección del punto de acceso).
- **Versiones**: la **1.1** (2001) es la usada en la práctica; la **2.0** (Recomendación W3C de 2007) renombró portType a **interface** y port a **endpoint**, y añadió un binding HTTP pensado para servicios tipo REST que apenas tuvo adopción.
- **Patrones de intercambio de mensajes**: petición-respuesta (el habitual), solo entrada (*one-way*), solo salida (*notification*) y salida-entrada (*solicit-response*).

**UDDI (Universal Description, Discovery and Integration)**: estándar OASIS de registro para publicar y descubrir servicios web.

- **Contenido del registro**: **páginas blancas** (identificación y contacto de la organización), **páginas amarillas** (clasificación por taxonomías sectoriales) y **páginas verdes** (información técnica de los servicios).
- **Tipos de registro**: públicos y privados (corporativos).
- **Estado actual**: el registro público mundial (UDDI Business Registry, operado por IBM, Microsoft y SAP) **cerró en 2006**; UDDI quedó relegado a registros corporativos y hoy el descubrimiento se resuelve con catálogos y portales de APIs (tema 40).

**Extensiones WS-\***: especificaciones que añaden capacidades empresariales sobre SOAP, generalmente mediante el Header:

- **WS-Security**: integridad, cifrado y tokens de seguridad en el mensaje (no solo en el transporte).
- **WS-Policy** (requisitos y capacidades del servicio), **WS-Trust** (emisión de tokens), **WS-ReliableMessaging** (entrega garantizada) y **WS-AtomicTransaction** (transacciones distribuidas).
- **WS-BPEL** (OASIS): lenguaje de orquestación de procesos de negocio sobre servicios web.
- **WS-I Basic Profile**: perfil de interoperabilidad que restringe las opciones de SOAP/WSDL para garantizar la compatibilidad entre plataformas (la organización WS-I se integró en OASIS en 2010).

Los servicios web SOAP sobreviven sobre todo en la integración corporativa y en las administraciones públicas (por ejemplo, la intermediación de datos SCSP, temas 58 y 59); el desarrollo nuevo de APIs es mayoritariamente REST.

## Servicios REST

**REST (Representational State Transfer)** es un **estilo arquitectónico**, no un protocolo ni un estándar, definido por **Roy Fielding** en su tesis doctoral (**2000**) a partir de los principios que hicieron escalar la web. Una API es «RESTful» si cumple sus restricciones apoyándose en los estándares existentes: HTTP, URI, JSON/XML.

**Las seis restricciones**:

- **Cliente-servidor**: separación de interfaz y datos.
- **Sin estado**: cada petición contiene toda la información necesaria; el servidor no guarda sesión.
- **Cacheable**: las respuestas declaran si pueden cachearse.
- **Interfaz uniforme**: identificación de recursos por URI, manipulación mediante representaciones, mensajes autodescriptivos e hipermedia (HATEOAS).
- **Sistema en capas**: el cliente solo ve la capa inmediata (caches, proxies y pasarelas son transparentes).
- **Código bajo demanda** (opcional): el servidor puede enviar código ejecutable al cliente.

**Conceptos básicos**:

- **Recurso**: toda entidad expuesta (un expediente, un ciudadano), identificada por una **URI** estable (`/expedientes/123`).
- **Representación**: el estado del recurso serializado (JSON es lo habitual); la **negociación de contenido** usa las cabeceras `Accept` y `Content-Type` (tipos MIME como `application/json`).
- **Métodos HTTP** con semántica estándar. **Seguro**: no modifica el recurso; **idempotente**: repetirlo produce el mismo resultado:

| Método | Uso | Seguro | Idempotente |
| --- | --- | --- | --- |
| GET | Leer un recurso | Sí | Sí |
| HEAD | Solo cabeceras | Sí | Sí |
| OPTIONS | Métodos soportados | Sí | Sí |
| POST | Crear o procesar | No | No |
| PUT | Crear o sustituir completo | No | Sí |
| PATCH | Modificación parcial | No | No |
| DELETE | Eliminar | No | Sí |

- **Códigos de estado**: **200** OK, **201** Created, **204** No Content; **301** Moved Permanently, **304** Not Modified; **400** Bad Request, **401** Unauthorized, **403** Forbidden, **404** Not Found, **409** Conflict, **429** Too Many Requests; **500** Internal Server Error, **503** Service Unavailable.
- **Caché**: cabeceras `Cache-Control` y `Expires`, y validadores `ETag`/`If-None-Match` y `Last-Modified` (el 304 evita retransmitir).
- **HATEOAS** (*Hypermedia as the Engine of Application State*): las respuestas incluyen enlaces a las acciones posibles, de modo que el cliente navega la API como hipertexto sin conocer las URIs de antemano.
- **Modelo de madurez de Richardson**: nivel 0 (HTTP como túnel RPC), nivel 1 (recursos con URI), nivel 2 (verbos HTTP y códigos de estado: lo habitual en la práctica) y nivel 3 (HATEOAS).
- **Documentación**: el contrato de una API REST se describe con **OpenAPI** (tratada, junto con la gestión y seguridad de APIs, en el tema 40).

**SOAP frente a REST**:

| | SOAP | REST |
| --- | --- | --- |
| Naturaleza | Protocolo (estándar W3C) | Estilo arquitectónico |
| Formato | Solo XML | Cualquiera; JSON de facto |
| Contrato | WSDL | OpenAPI |
| Estado | Sin estado (con extensiones WS) | Sin estado por definición |
| Seguridad | WS-Security (a nivel de mensaje) | HTTPS + OAuth 2.0/JWT (transporte y token) |
| Transporte | HTTP, SMTP, colas | HTTP exclusivamente |
| Uso típico | Integración corporativa, AAPP, transacciones | APIs web y móviles, servicios públicos de datos |

## Arquitectura de microservicios

La arquitectura de microservicios construye una aplicación como un conjunto de **servicios pequeños e independientes**, cada uno ejecutándose en su propio proceso, comunicados por mecanismos ligeros (HTTP/REST o mensajería) y **desplegables por separado**. El término se consolidó con el artículo de **James Lewis y Martin Fowler (2014)**. Es heredera de SOA, pero rechaza el bus central: «**extremos inteligentes, tuberías bobas**»: la lógica vive en los servicios y el canal solo transporta mensajes.

**Características** (según Lewis y Fowler):

- **Componentes como servicios**: la unidad de composición es el servicio desplegable, no la biblioteca.
- **Organización por capacidades de negocio**: cada servicio cubre una función de negocio completa (interfaz, lógica y datos), con equipos multidisciplinares responsables de extremo a extremo (ley de Conway).
- **Productos, no proyectos**: el equipo que construye el servicio lo opera durante toda su vida.
- **Gobierno descentralizado**: cada servicio puede usar el lenguaje y la tecnología que mejor le convenga.
- **Datos descentralizados**: cada servicio es dueño de su **base de datos**; la coherencia entre servicios es **eventual**.
- **Automatización de infraestructura**: integración y despliegue continuos (CI/CD), infraestructura como código.
- **Diseño para el fallo**: se asume que las llamadas remotas fallarán y se diseña para degradarse con elegancia.
- **Diseño evolutivo**: los servicios se sustituyen y recomponen sin parar el sistema.

**Beneficios**: despliegue independiente (ciclos de entrega cortos), **escalado selectivo** (solo el servicio que lo necesita), aislamiento de fallos, libertad tecnológica y equipos autónomos.

**Inconvenientes**: complejidad de **sistema distribuido** (latencia de red, fallos parciales, versionado de contratos), **consistencia eventual** (no hay transacciones globales), pruebas de integración y depuración difíciles, y una operación exigente que requiere madurez en automatización y monitorización. Para sistemas pequeños o equipos reducidos, el monolito (bien modularizado) sigue siendo una opción legítima.

**Patrones habituales**:

- **API Gateway**: punto de entrada único para los clientes: enruta, autentica, limita el tráfico y agrega respuestas de varios servicios.
- **Descubrimiento de servicios**: las instancias se registran dinámicamente y los clientes las localizan por nombre (Consul, Eureka; en Kubernetes, el DNS interno).
- **Base de datos por servicio** y **saga**: las transacciones que cruzan servicios se descomponen en una secuencia de transacciones locales con acciones compensatorias.
- **Tolerancia a fallos**: tiempos de espera y reintentos con límite, **cortocircuito** (*circuit breaker*: deja de llamar a un servicio que falla hasta que se recupere) y **compartimentos estancos** (*bulkhead*: aislar recursos para que un fallo no arrastre al resto).
- **Comunicación por eventos**: los servicios publican eventos en un broker (Kafka, RabbitMQ) y los interesados se suscriben (coreografía), en lugar de encadenar llamadas síncronas.
- **Observabilidad**: logs centralizados, métricas y **trazabilidad distribuida** de cada petición a través de los servicios (OpenTelemetry como estándar).

**Despliegue y ecosistema**: los microservicios se empaquetan en **contenedores** (Docker) y se operan con orquestadores (**Kubernetes**) (tema 44); frameworks típicos: **Spring Boot/Spring Cloud** (Java), NestJS (Node.js), FastAPI (Python). Una **service mesh** (Istio, Linkerd) saca de las aplicaciones la comunicación segura (mTLS), el enrutado y la observabilidad, y los presta como infraestructura.

## Formatos de intercambio: XML y JSON

**XML (eXtensible Markup Language)**: metalenguaje del **W3C** (Recomendación de 1998) derivado de **SGML**, que permite definir lenguajes de marcado para estructurar e intercambiar información de forma legible e independiente de la plataforma.

- **Partes de un documento**: el **prólogo** opcional (declaración y, en su caso, DOCTYPE) y el **cuerpo**, con un **único elemento raíz**:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<expediente id="2026-001">
  <interesado>María Pérez</interesado>
  <estado>abierto</estado>
</expediente>
```

- **Componentes**: **elementos** (etiquetas anidadas), **atributos** (pares nombre-valor en la etiqueta), **entidades predefinidas** para caracteres reservados (`&amp;`, `&lt;`, `&gt;`, `&quot;`, `&apos;`), secciones **CDATA** (texto que el analizador no interpreta como marcado) y **comentarios** (`<!-- ... -->`, nunca antes de la declaración).
- **Bien formado frente a válido**: un documento es **bien formado** si respeta la sintaxis (elementos correctamente anidados y cerrados, un solo elemento raíz, sensible a mayúsculas, atributos entrecomillados); es **válido** si además se ajusta a una gramática definida en un **DTD** o un esquema **XSD**.
- **DTD (Document Type Definition)**: sintaxis propia (no XML) que declara los elementos permitidos, sus modelos de contenido (subelementos y orden), las listas de atributos y las entidades:

```xml
<!DOCTYPE nota [
  <!ELEMENT nota (para, de, asunto, cuerpo)>
  <!ELEMENT para (#PCDATA)>
  <!ELEMENT de (#PCDATA)>
  <!ELEMENT asunto (#PCDATA)>
  <!ELEMENT cuerpo (#PCDATA)>
]>
```

- **XSD (XML Schema)**: alternativa moderna al DTD: se escribe **en sintaxis XML**, soporta **tipos de datos** (primitivos como string, boolean, decimal, dateTime; derivados como integer o ID) y es extensible:

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="contacto">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="telefono" type="xs:integer"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

- **Espacios de nombres** (*namespaces*, atributo `xmlns`): desambiguan elementos de vocabularios distintos en un mismo documento.
- **Procesamiento**: **DOM** (carga el documento completo en memoria como árbol de nodos: permite navegar y modificar, a costa de memoria; para documentos pequeños o edición) frente a **SAX** (lectura **secuencial por eventos** sin cargar el documento: para ficheros grandes procesados una vez). Se complementan con **XPath** (localizar nodos mediante expresiones) y **XSLT** (transformar XML en otros formatos).

**JSON (JavaScript Object Notation)**: formato ligero de intercambio de datos, definido en el **RFC 8259** y en **ECMA-404**. Nació como subconjunto de la notación de objetos de JavaScript y hoy es **independiente del lenguaje** y el formato de facto de las APIs web.

- **Tipos de datos**: **objetos** (pares clave-valor entre llaves), **arrays**, cadenas (siempre con comillas dobles), números, `true`/`false` y `null`. No admite comentarios.
- **Tipo MIME**: **application/json**.
- **En JavaScript**: `JSON.parse()` convierte texto JSON en objetos y `JSON.stringify()` serializa objetos a JSON. Nunca debe evaluarse texto JSON recibido como código (`eval`): es un riesgo de inyección.
- **JSON Schema**: vocabulario para validar documentos JSON contra un esquema (estructura, tipos, campos obligatorios), análogo al papel del XSD en XML.
- **Modelos de procesado**: de **objeto** (todo el documento en memoria) y de **flujo** (*streaming*, secuencial, eficiente para volúmenes grandes).

**Comparación y uso**:

| | XML | JSON |
| --- | --- | --- |
| Verbosidad | Alta (etiquetas de apertura y cierre) | Baja |
| Validación | DTD, XSD (maduros) | JSON Schema |
| Atributos y namespaces | Sí | No |
| Comentarios | Sí | No |
| Procesado en JavaScript | Vía DOM/parsers | Nativo (JSON.parse) |
| Uso típico | Documentos, integración corporativa, firma electrónica (XAdES, facturae) | APIs REST, configuración, web y móvil |

Otros formatos de intercambio: **YAML** (configuración legible, superconjunto de JSON) y **Protocol Buffers** (binario y tipado, usado por gRPC, tema 52).

## Fuentes {.unnumbered .unlisted}

- W3C: SOAP 1.2 (Recomendación, 2.ª ed., 27 de abril de 2007), WSDL 1.1 (Nota, 15 de marzo de 2001), WSDL 2.0 (Recomendación, 26 de junio de 2007), XML 1.0 (5.ª ed., 26 de noviembre de 2008), Web Services Glossary (Nota, 11 de febrero de 2004), MTOM (Recomendación, 25 de enero de 2005).
- OASIS: UDDI v3.0.2 (2004), WS-BPEL 2.0 (abril de 2007), WS-Security 1.1.
- R. T. Fielding, *Architectural Styles and the Design of Network-based Software Architectures*, tesis doctoral, UC Irvine, 2000 (cap. 5: REST).
- J. Lewis y M. Fowler, «Microservices», martinfowler.com, marzo de 2014.
- RFC 8259 (JSON, diciembre de 2017) y ECMA-404 (2.ª ed., diciembre de 2017); JSON Schema (especificación 2020-12).
