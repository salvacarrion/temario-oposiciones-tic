# SOA, servicios web y microservicios

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## La arquitectura orientada a servicios (SOA)

La **Arquitectura Orientada a Servicios (SOA)** es un estilo de diseño que organiza la funcionalidad de un sistema en **pequeñas partes reutilizables llamadas "servicios"**, diseñadas para ser accesibles a través de **interfaces estandarizadas (APIs)**. Sus objetivos principales incluyen:

- **Agilidad**: Facilitar la planificación e implementación de soluciones empresariales.
- **Reutilización**: Maximizar el aprovechamiento de recursos.
- **Federación**: Unificación de criterios empresariales.

**Características clave de SOA**:

- **Interoperabilidad**: Los servicios deben ser compatibles entre distintas plataformas.
- **Capacidad descriptiva**: Cada servicio debe tener una definición clara.
- **Reutilización**: Los servicios pueden integrarse en diferentes aplicaciones.
- **Descubrimiento**: Los consumidores pueden localizar servicios en un registro.
- **Composición**: Integración en procesos más complejos.
- **Auto-contenido**: Funcionan sin dependencias externas innecesarias.
- **Gestionabilidad**: Control eficiente para monitorización y actualización.

**Relación entre proveedor y consumidor**:

- Se basa en **contratos** que definen las características del servicio.
- Implica el intercambio de mensajes con:
    - **Interoperabilidad sintáctica**: Uniformidad en el formato.
    - **Interoperabilidad semántica**: Claridad en el significado.

**Principios de la relación proveedor-consumidor**:

1. **Independencia de dominios**: Pueden pertenecer al mismo sistema o a diferentes.
2. **Independencia de plataformas**: Los servicios se tratan como **cajas negras**.
3. **Independencia de protocolos**: Transformación de mensajes según el formato necesario.

Cada servicio consta de **tres elementos**:

- **Lógica**: Identificación única del servicio.
- **Descripción**: Definición de su funcionalidad.
- **Interfaz**: Punto de acceso para su uso.

Los servicios se registran en un **repositorio**, donde los consumidores pueden descubrirlos para su integración.

### Modelo de Referencia SOA y Arquitectura de Capas

El **Modelo de Referencia SOA** es independiente de la implementación y organiza los sistemas en una **arquitectura de capas**.

- **Capas verticales** (funcionales):
    1. **Operatividad**: Bases de datos, sistemas de monitorización, sistemas industriales, etc.
    2. **Componentes**: Desvinculación del servicio respecto a la tecnología.
    3. **Servicios**: Clasificados como simples o complejos.
    4. **Procesos de negocio**: Coordinación de tareas con un objetivo empresarial.
    5. **Consumidor**: Punto de visualización o acceso a los servicios.
- **Capas horizontales** (transversales):
    1. **Integración**: Conectividad entre servicios.
    2. **Calidad de Servicio (QoS)**: Requisitos no funcionales, como seguridad, rendimiento y escalabilidad.
    3. **Información**: Representación y tratamiento de datos.
    4. **Gobierno**: Normas para el diseño, desarrollo y mantenimiento de los servicios.

### Ciclo de Vida del Servicio SOA

El desarrollo de un servicio SOA sigue un ciclo estructurado que incluye:

1. **Análisis de inventario**: Identificación de necesidades.
2. **Modelado del servicio**: Estructuración y definición.
3. **Diseño del contrato**: Especificación de interfaces y acuerdos.
4. **Diseño de la lógica**: Detalles técnicos del servicio.
5. **Desarrollo o implementación**: Creación técnica del servicio.
6. **Pruebas**: Validación de requisitos funcionales y no funcionales.
7. **Publicación**: Registro en repositorios accesibles.
8. **Monitorización**: Evaluación del rendimiento y uso.
9. **Mejora continua**: Actualización y optimización del servicio.

En la planificación estratégica de servicios, las **fases clave** son:

- **Acuerdo de usuario**: Definición de contratos.
- **Servicio**: Descripción detallada.
- **Interfaz**: Especificación de mensajes.
- **Implementación**: Desarrollo y mantenimiento.

### Estilos de Composición de Tareas en SOA

SOA permite la ejecución de tareas, definidas como **acciones atómicas** realizadas por actores humanos. Existen varios estilos para coordinar estas tareas:

1. **Orquestación**: Un elemento externo controla el flujo de tareas.
2. **Coreografía**: Relaciones predefinidas entre tareas, sin un control central.
3. **Colaboración**: Ejecución independiente con relaciones puntuales entre tareas.

### Servicios Web y Tecnologías Asociadas

Los **Servicios Web (WS)** son una tecnología clave en SOA, que utiliza estándares para facilitar la integración y la interoperabilidad entre aplicaciones.

**Definición según el W3C**: Un servicio web es un sistema software diseñado para soportar la interacción máquina-a-máquina a través de una red de forma interoperable. Sus características clave incluyen:

- **Interfaz estándar**: Definida en **WSDL**.
- **Mensajería estructurada**: Basada en **SOAP**.
- **Transporte**: Generalmente **HTTP**, con serialización en **XML**.

**Estándares y herramientas utilizadas en los servicios web**:

1. **SOAP**: Protocolo para el intercambio de mensajes.
2. **WSDL**: Lenguaje para la descripción de interfaces.
3. **UDDI**: Registro para descubrimiento de servicios.
4. **REST**: Alternativa ligera basada en HTTP.
5. **\*WS- (Web Services Extensions):** Seguridad, transacciones y confiabilidad.
6. **WS-BPEL**: Orquestación y coreografía de servicios.

**Principios de diseño de servicios web**:

- **Contrato de servicios estandarizados**: Interfaces bien definidas.
- **Desacoplamiento**: Reducción de dependencias entre sistemas.
- **Abstracción**: Ocultación de detalles internos.
- **Reutilización**: Uso eficiente de recursos.
- **Sin estado**: Los servicios no mantienen datos entre peticiones.
- **Granularidad**: Nivel adecuado de detalle.
- **Transparencia de ubicación**: El usuario no necesita conocer la localización física del servicio.

## Servicios web y estándares

### Arquitectura de Servicios Web (SOA)

La Arquitectura Orientada a Servicios (SOA) es un diseño de software que promueve la reutilización de componentes mediante interfaces de servicios que se comunican a través de una red utilizando un lenguaje común. Esto permite que diferentes aplicaciones interactúen y compartan datos de manera interoperable.

### Servicios Web

Un servicio web es una tecnología que utiliza un conjunto de protocolos y estándares para intercambiar datos entre aplicaciones.

- **Definición del W3C:** *"Un servicio web es un sistema software diseñado para soportar la interacción máquina-a-máquina, a través de una red, de forma interoperable. Cuenta con una interfaz descrita en un formato procesable por un equipo informático (específicamente en WSDL), a través de la que es posible interactuar con el mismo mediante el intercambio de mensajes SOAP, típicamente transmitidos usando serialización XML sobre HTTP conjuntamente con otros estándares web."*

### Estándares Empleados en Servicios Web

Los servicios web hacen uso de diversos estándares para garantizar la interoperabilidad y comunicación efectiva entre aplicaciones:

- **XML** (eXtensible Markup Language)
- **SOAP** (Simple Object Access Protocol)
- **WSDL** (Web Services Description Language)
- **UDDI** (Universal Description, Discovery and Integration)
- **REST**
- **WS-\*** (Conjunto de protocolos de servicios web)

### SOAP (Simple Object Access Protocol)

SOAP es un protocolo estándar que define cómo dos objetos en diferentes procesos pueden comunicarse mediante el intercambio de datos en formato XML. Confía en protocolos de aplicación como HTTP o SMTP para su funcionamiento y es **stateless** (no mantiene estado entre peticiones). Puede servir como la capa base de una "pila de protocolos de servicios web".

### Características Principales de SOAP

- **Extensibilidad**: Permite añadir funcionalidades adicionales como seguridad (WS-Security) y direccionamiento (WS-Addressing).
- **Neutralidad**: Puede operar sobre cualquier protocolo de transporte como HTTP, SMTP, TCP o UDP.
- **Independencia**: Es compatible con cualquier modelo de programación.

### Estructura de un Mensaje SOAP

Un mensaje SOAP es un documento XML con una estructura definida:

- **Envelope** (Obligatorio): Identifica al mensaje como un mensaje SOAP y encapsula toda la información.
- **Header** (Opcional): Mecanismo de extensión que permite enviar información sobre cómo debe ser procesado el mensaje.
- **Body** (Obligatorio): Contiene la información relativa a la llamada y la respuesta.
- **Fault**: Bloque que incluye información sobre errores ocurridos durante el procesamiento del mensaje.

### Propiedades del Mensaje SOAP

- **Bien Formado**: Todas las etiquetas deben estar correctamente abiertas y cerradas en el orden adecuado.
- **Válido**: Debe cumplir con la estructura y sintaxis definidas en su DTD o esquema XML.

### Ejemplo de Mensaje SOAP

```xml
<?xml version='1.0' ?>
<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
  <env:Header>...</env:Header>
  <env:Body>...</env:Body>
</env:Envelope>
```

### Modelo de Procesado SOAP

SOAP define un sistema distribuido con diferentes nodos que pueden asumir varios roles:

- **SOAP Sender**: Nodo que transmite un mensaje SOAP.
- **SOAP Receiver**: Nodo que recibe y procesa un mensaje SOAP.
- **Initial SOAP Sender**: Emisor original del mensaje.
- **SOAP Intermediary**: Nodo que actúa como receptor y emisor, procesando parcialmente el mensaje.
- **Ultimate SOAP Receiver**: Destino final responsable de procesar completamente el mensaje.
- **SOAP Message Path**: Ruta que sigue el mensaje a través de los nodos SOAP.

### REST (Representational State Transfer)

REST es un estilo de arquitectura de software que describe una interfaz uniforme entre componentes desacoplados en Internet, siguiendo una arquitectura Cliente-Servidor. Aunque no es un estándar en sí mismo, las implementaciones **RESTful** utilizan estándares como HTTP, URI, JSON y XML.

### Principios de REST

- **Arquitectura Cliente-Servidor**
- **Stateless**: Ausencia de estado en las comunicaciones.
- **Uso de Caché**: Opcional, para mejorar el rendimiento.
- **Sistema por Capas**: El cliente solo interactúa con la capa inmediata.
- **Interfaz Uniforme**: Uso consistente de métodos y recursos.

### Aspectos Básicos de REST

- **URI (Uniform Resource Identifier)**: Identifica de forma única los recursos en la red (e.g., http://api.example.com/).
- **Métodos HTTP Estándar**:
    - **GET**: Solicita un recurso específico.
    - **POST**: Envía datos para ser procesados por el recurso identificado.
    - **PUT**: Actualiza o crea un recurso en el servidor.
    - **DELETE**: Elimina el recurso especificado.
    - **OPTIONS**: Recupera los métodos HTTP soportados por el servidor para una URL.
    - **HEAD**: Obtiene la cabecera HTTP sin el cuerpo.
- **Tipos de Medio (MIME Types)**: Identificadores para formatos de archivo transmitidos por Internet (e.g., application/json, text/html).

### Clasificación de Métodos HTTP

- **Métodos Seguros**: No modifican recursos (e.g., **GET**).
- **Métodos Inseguros**: Pueden modificar recursos (e.g., **POST**, **DELETE**).
- **Métodos Idempotentes**: El resultado es el mismo sin importar cuántas veces se ejecuten (e.g., **GET**, **PUT**, **DELETE**).

### Códigos de Respuesta HTTP Comunes

- **200 OK**
- **201 Created**
- **400 Bad Request**
- **401 Unauthorized**
- **404 Not Found**
- **405 Method Not Allowed**
- **409 Conflict**
- **500 Internal Server Error**

### Caching en REST

- **Headers relevantes**: Date, Last-Modified, Cache-Control, Expires, Age.

### SOAP vs. REST

- **SOAP**: Protocolo orientado a servicios que utiliza XML para el intercambio de mensajes.
- **REST**: Arquitectura orientada a recursos que aprovecha las características de HTTP y utiliza diversos formatos (XML, JSON).

### Descripción y Descubrimiento de Servicios

Los servicios pueden ser descritos mediante documentos que detallan su funcionalidad, parámetros de entrada y salida, y cómo invocarlos. Esto facilita su descubrimiento y uso por parte de otras aplicaciones.

### Estándares de Descripción y Descubrimiento

- **WSDL (Web Services Description Language)**: Lenguaje basado en XML para describir servicios web y sus interfaces.
- **UDDI (Universal Description, Discovery and Integration)**: Estándar para publicar y descubrir información sobre servicios web.
- **OpenAPI**: Especificación para describir y documentar APIs RESTful.

### WSDL (Web Services Description Language)

WSDL es un estándar que permite describir servicios web y APIs. Aunque se utiliza principalmente con SOAP, también soporta servicios RESTful. Especifica la interfaz abstracta y los detalles necesarios para interactuar con el servicio.

### Estructura de WSDL

- **types**: Define los tipos de datos (usualmente usando XML Schema).
- **message**: Contiene la información para realizar operaciones.
- **portType**/**interface**: Define las operaciones que el servicio ofrece y los mensajes utilizados.
- **binding**: Especifica los detalles de protocolo y formato de datos para cada operación.
- **service**: Agrupa endpoints relacionados.
- **endpoint**/**port**: Define la dirección donde el servicio está disponible.

### Patrones de Mensaje en WSDL

- **One-way**: Solo entrada.
- **Notification**: Solo salida.
- **Solicit-response**: Salida seguida de entrada (el orden es importante).
- **Request-response**: Entrada seguida de salida.

### UDDI (Universal Description, Discovery and Integration)

UDDI es un estándar basado en XML para publicar y descubrir información sobre servicios web y otras APIs. Aunque ha perdido popularidad frente a WSDL y OpenAPI, proporciona un catálogo de negocios que facilita el registro y búsqueda de servicios.

### Componentes de UDDI

- **Páginas Blancas**: Información básica de contacto y dirección.
- **Páginas Amarillas**: Categorización industrial basada en taxonomías estándar.
- **Páginas Verdes**: Información técnica detallada sobre los servicios web.

### Tipos de Registro en UDDI

- **Públicos**: Accesibles a cualquier usuario.
- **Privados**: Implementados dentro de organizaciones, a menudo detrás de cortafuegos.

**Protocolos de Servicios Web (WS-\*)**

El conjunto **WS-\*** abarca una serie de protocolos y estándares que permiten el intercambio de datos en Internet entre aplicaciones, independientemente del lenguaje o plataforma. Algunos de los protocolos más comunes incluyen:

- **WS-Policy**
- **WS-Security**
- **WS-Trust**
- **WS-SecureConversation**
- **WS-Reliable Messaging**
- **WS-AtomicTransactions**

Estos protocolos abordan aspectos como seguridad, confiabilidad y transacciones en servicios web.

### WS-I (Web Services Interoperability Organization)

La **WS-I** es una organización dedicada a promover la interoperabilidad de servicios web entre diferentes plataformas, sistemas operativos y lenguajes de programación. Su **WS-I Basic Profile** es un conjunto de especificaciones que garantiza la compatibilidad entre implementaciones de servicios web.

### Formatos Comunes: XML y JSON

- **XML**: Lenguaje de marcado extensible utilizado para representar y transmitir datos de forma estructurada. Es ampliamente empleado en aplicaciones empresariales para el intercambio de información.
- **JSON**: Formato de intercambio de datos ligero y fácil de leer, basado en JavaScript. Es común en aplicaciones web modernas y es compatible con la mayoría de los lenguajes de programación.

### MTOM (Message Transmission Optimization Mechanism)

MTOM es un mecanismo definido por el W3C para optimizar la transmisión de datos binarios codificados en base64 entre servicios web. Permite una transferencia más eficiente al evitar el sobrecoste asociado con la codificación base64 en mensajes SOAP.

## Arquitectura de microservicios

La arquitectura de microservicios es un enfoque de diseño de software basado en la construcción de aplicaciones mediante la composición de pequeños servicios **independientes** que interactúan a través de **APIs** y suelen contar con almacenamiento propio. Cada microservicio es responsable de una funcionalidad específica del sistema, lo que permite su despliegue, escalado y mantenimiento de forma autónoma. Este modelo es una evolución de la arquitectura orientada a servicios (SOA), con un diseño **descentralizado y distribuido**.

Los **beneficios** de esta arquitectura incluyen:

- **Modularidad**, que facilita el desarrollo y mantenimiento.
- **Escalabilidad**, ya que los servicios se escalan de manera independiente.
- **Versatilidad** en la implementación tecnológica.
- **Rapidez de actuación** al aislar los cambios.
- **Mantenimiento más simple y económico**.
- **Agilidad** para responder a las necesidades del negocio.

Sin embargo, también presenta **desventajas**:

- **Consumo elevado de memoria**.
- **Alta complejidad en la gestión** del sistema.
- **Requiere perfiles especializados** de desarrolladores.
- **Dificultad en las pruebas**, dado el número de servicios involucrados.
- **Falta de uniformidad** entre servicios.
- **Coste elevado de implementación inicial**.

### Características de la arquitectura de microservicios

- Los componentes son **servicios independientes**.
- Se organiza en torno a las **funcionalidades del negocio**, integrando elementos como interfaces de usuario, persistencia de datos e interoperabilidad en cada servicio.
- Fomenta una mentalidad de **productos, no proyectos**, lo que implica que los equipos son responsables de los servicios durante todo su ciclo de vida.
- Sigue el principio de **extremos inteligentes, tuberías bobas**, lo que asegura bajo acoplamiento y alta cohesión.
- **Gobierno descentralizado**, permitiendo el uso de diferentes lenguajes y tecnologías según las necesidades de cada servicio.
- Gestión de datos también **descentralizada**, garantizando mayor independencia entre servicios.
- Diseño **tolerante a fallos**, incluyendo mecanismos como:
    - **Tiempos de espera máximos**, que realizan reintentos o encolan solicitudes fallidas.
    - **Disyuntores**, que actúan como “interruptores” para evitar sobrecargar el sistema al desconectar servicios cuando se alcanzan umbrales de fallos.
    - **Compartimentos estancos**, que aíslan fallos para evitar que afecten al sistema completo.
- Automatización de infraestructura mediante **CI/CD** (Integración y Despliegue Continuo).
- Fomenta un **diseño evolutivo**, adaptándose a las necesidades del negocio y las mejoras tecnológicas.

### Integración de servicios

Existen diferentes enfoques para coordinar los microservicios, dependiendo de las necesidades del sistema:

- **Orquestación**: Un servicio centralizado actúa como **orquestador**, controlando la ejecución de los demás servicios. Es útil para garantizar un mayor control y seguimiento, aunque puede generar una dependencia excesiva del orquestador y aumentar la complejidad del sistema.
- **Coreografía**: Los servicios interactúan de manera más **autónoma**, reduciendo la dependencia centralizada y mejorando la escalabilidad. Sin embargo, este enfoque puede requerir una mayor coordinación y ser más difícil de implementar.
- **Colaboración**: Los servicios trabajan de manera **informal**, sin una estructura rígida de coordinación. Esto ofrece mayor flexibilidad, pero implica tolerar cierta incertidumbre en los flujos de trabajo y puede ser complejo de gestionar.

### Soluciones para microservicios

Los microservicios suelen desplegarse en contenedores (por ejemplo, **Docker**) para garantizar su portabilidad y capacidad de ejecución en cualquier máquina o servidor. Esto facilita el despliegue y ofrece beneficios como:

- Mayor **flexibilidad** en la asignación de recursos.
- Mejor **disponibilidad** del sistema.
- Incremento en la **tolerancia a fallos**.

## Formatos de intercambio: XML y JSON

### JSON (JavaScript Object Notation)

Es un formato abierto ampliamente utilizado para el intercambio de datos. Aunque originalmente es un subconjunto de la notación literal de objetos de JavaScript, su adopción masiva lo ha consolidado como un **formato independiente del lenguaje**. JSON se posiciona como una alternativa a XML, pero es habitual encontrar aplicaciones que combinan ambos formatos.

JSON destaca por su simplicidad, ya que es mucho más sencillo desarrollar un **parser** (analizador sintáctico) para JSON que para XML. Los tipos de datos admitidos en JSON incluyen **números, cadenas de texto, valores booleanos, null, arrays** y **objetos** (estructuras similares a diccionarios en otros lenguajes).

### Modelos de procesamiento de JSON

- **Modelo de objeto**: Todo el contenido del JSON se carga en memoria como un árbol de datos, permitiendo una manipulación completa pero consumiendo más memoria.
- **Modelo de flujo**: Los datos se procesan de forma secuencial en bloques, lo que resulta más eficiente en memoria pero limita la accesibilidad directa al JSON completo.

### Conversión de JSON a objetos del lenguaje

Una práctica común en lenguajes como JavaScript es convertir estructuras JSON en objetos nativos. Sin embargo, es importante evitar el uso de **eval()** debido a los riesgos de seguridad que implica, ya que eval ejecuta directamente el código. En su lugar, se recomienda usar **Function()**, que permite generar una función que solo se ejecutará bajo control explícito del usuario.

### Validación de JSON

- **Validación sintáctica**: Verifica que el JSON esté correctamente formado según las reglas del formato, como el uso de comillas, comas, y delimitadores adecuados.
- **Validación semántica**: Comprueba que el JSON sea válido respecto a un esquema predefinido. Un esquema especifica la **gramática, estructura, contenido y significado** esperado, y puede definir modelos como “Persona”, “Automóvil” o “Usuario”.

### MIME type de JSON

El **MIME type** asociado a JSON es **application/json**, y es esencial especificarlo al intercambiar datos a través de HTTP para garantizar el correcto reconocimiento del formato.

### Manipulación de JSON en JavaScript

JavaScript ofrece métodos nativos para trabajar con JSON:

- **JSON.stringify()**: Convierte un objeto o estructura de datos en una cadena JSON.
- **JSON.parse()**: Transforma una cadena JSON válida en un objeto JavaScript.

### XML (eXtensible Markup Language)

XML (eXtensible Markup Language) es un metalenguaje desarrollado por el **World Wide Web Consortium (W3C)** que permite definir lenguajes de marcas para **almacenar datos en forma legible** y facilitar el intercambio de información estructurada entre diferentes plataformas. Deriva del **SGML (Standard Generalized Markup Language)** y permite definir gramáticas específicas para estructurar grandes documentos.

### Partes de un documento XML

- **Prólogo** (opcional): Describe información como la versión XML y el tipo de documento. Ejemplo:

> \<?xml version="1.0" encoding="UTF-8"?> > > \<!DOCTYPE Edit_Mensaje SYSTEM "Edit_Mensaje.dtd">

- **Cuerpo** (obligatorio): Contiene un único **elemento raíz**. Ejemplo: \<Edit_Mensaje> [...] \</Edit_Mensaje>
- **Elementos**: Pueden incluir caracteres alfanuméricos, puntos (.), guiones (-) y barras bajas (\_).\ Ejemplo: \<queso>\</queso>
- **Atributos**: Proporcionan características adicionales a los elementos.\ Ejemplo: \<Estudiante Mario="come croquetas" tipo="talento"> [...] \</Estudiante>
- **Entidades predefinidas**: Representan caracteres especiales. Ejemplos:\ \&amp; → &, \&lt; → \<
- **Secciones CDATA**: Permiten usar caracteres sin interpretarlos como marcado XML.\ Ejemplo: \<!\[CDATA[contenido especial: áéíóúñ&]\]>
- **Comentarios**: No pueden aparecer antes de la declaración XML.\ Ejemplo: \<!-- Mi comentario -->

### Documentos XML bien formados y válidos

- **Bien formados (well-formed)**: Cumplen las definiciones básicas de formato, como:
    - Estructuras anidadas y elementos cerrados correctamente.
    - Un único elemento raíz.
    - Sensibilidad a mayúsculas y minúsculas (case sensitive).
    - Uso consistente de comillas simples o dobles.
- **Válidos**: Además de estar bien formados, se ajustan a un esquema (**XSD**) o una definición de tipo de documento (**DTD**).

### Definición de tipo de documento (DTD)

El **DTD** define elementos, atributos y entidades permitidos, así como sus combinaciones. Incluye:

- **Declaraciones tipo elemento**: Qué elementos son válidos.
- **Modelos de contenido**: Especifican subelementos permitidos y su orden.
- **Listas de atributos**: Atributos posibles para los elementos.
- **Entidades**: Pueden ser internas, externas, analizadas o no analizadas.
- **Espacios de nombres (namespaces)**: Separan semánticamente elementos dentro de un documento.

Ejemplo de **DTD interno**:

```xml
<!DOCTYPE note [
  <!ELEMENT note (to,from,heading,body)>
  <!ELEMENT to (#PCDATA)>
  <!ELEMENT from (#PCDATA)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend</body>
</note>
```

### XML Schema (XSD)

Los **esquemas XML (XSD)** son similares a los DTD, pero con diferencias clave:

- Utilizan la sintaxis de XML.
- Permiten especificar **tipos de datos**.
- Son **extensibles**.

Ejemplo de esquema XSD:

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="contact">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name" type="xs:string" />
        <xs:element name="company" type="xs:string" />
        <xs:element name="phone" type="xs:int" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Parseadores de XML: DOM y SAX

- **DOM (Document Object Model)**:
    - Carga toda la estructura en memoria como un árbol de nodos.
    - Permite **editar documentos** y **navegar entre nodos**.
    - Consumo elevado de memoria, ideal para documentos pequeños o manipulaciones frecuentes.
    - **Usos recomendados:**
        - Crear o modificar documentos XML.
        - Procesar múltiples veces un documento.
- **SAX (API Simple para XML)**:
    - Procesa el documento de forma **secuencial** mediante eventos (inicio/fin de documento, etiquetas, etc.).
    - No carga el documento completo en memoria, ideal para **archivos grandes**.
    - **Usos recomendados:**
        - Procesar documentos grandes una sola vez.
        - Capturar eventos específicos.

### Tipos de datos en XML

- **Primitivos**: Ejemplos: string, boolean, decimal, dateTime.
- **Derivados**: Ejemplos: normalizedString, ID, integer (derivado de decimal).

### Building blocks de XML

- **Attributes**: \<element myattribute="value">\</element>
- **Predefined entities**: \&lt;, \&gt;, \&amp;, \&quot;, \&apos;
- **PCDATA**: Texto dentro de etiquetas que **será parseado**.
- **CDATA**: Texto dentro de etiquetas que **no será parseado**.
- **Elements**: \<element>\</element>
- **DTD**: Define estructuras válidas para un documento.
