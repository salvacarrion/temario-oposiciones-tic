# Plataforma Autonómica de Interoperabilidad (PAI)

**Organismo responsable:** Conselleria de Economía, Hacienda y Administración Pública — Generalitat Valenciana.

---

## 1. ¿Qué es la PAI?

La Plataforma Autonómica de Interoperabilidad de la Generalitat Valenciana (PAI) es una **plataforma de interoperabilidad de servicios horizontales** que ofrece la posibilidad de **compartir e integrar servicios entre entidades públicas**.

Está disponible para:

- Todas las **Consellerias** y Organismos dependientes de la Generalitat.
- Las diferentes **Entidades Locales** de la Comunitat Valenciana.

A través de la PAI, las entidades pueden:

- Ofertar en un **catálogo común** sus servicios de interés.
- Acceder a la totalidad de los servicios ofertados.
- Promover la identificación y generación de nuevos servicios.

> **Principio clave:** Cuanto mayor sea la aportación de servicios por parte de las Consellerias y Organismos, mayor será el valor añadido aportado por la plataforma, mayor será la interoperabilidad.

### 1.1. Relación con la Plataforma de Intermediación de Datos (PID)

A nivel estatal, existe la **Plataforma de Intermediación de Datos del Estado (PID)**, que permite el intercambio de información entre Administraciones Públicas, evitando solicitar información a la persona interesada que obra en poder de la Administración (según el Art. 28.2 de la Ley 39/2015).

La PID actúa como intermediaria entre:

- **Organismos tramitadores**: solicitan los datos.
- **Organismos cedentes**: custodian la información.

Esto se realiza mediante el uso de **Servicios de Verificación y Consulta de Datos (SVCD)**, que deben implementar los organismos proveedores siguiendo las especificaciones del **SCSP** (Sustitución de Certificados en Soporte Papel).

### 1.2. La PAI como nodo de interoperabilidad

La PAI actúa de **nodo de interoperabilidad** entre:

1. **La PID y los organismos gestores de la Administración Autonómica y Local** en la Comunitat Valenciana, susceptibles de proporcionar algún tipo de trámite administrativo a los ciudadanos (**Servicios de Verificación de Datos**). Las directrices que sigue la PAI son las marcadas por la PID y por la NTI de Protocolos de Intermediación. Mientras la PID no autorice el acceso a los servicios de verificación solicitados desde un procedimiento administrativo de un organismo, la PAI no podrá autorizarlos.

2. **Los organismos gestores y los servicios instrumentales** que permiten realizar procesos instrumentales a las distintas entidades de la Administración Pública en su gestión con el ciudadano (p. ej., notificaciones).

---

## 2. Ventajas y mejoras

La PAI ofrece un **entorno seguro** donde publicar los servicios de las administraciones, permitiendo:

- Integración de servicios.
- Entorno de ejecución.
- Pasarela entre administraciones.
- Entorno securizado y monitorizable.

Facilita a las aplicaciones autorizadas la realización de las consultas necesarias para **verificar los datos de un ciudadano** que ha iniciado un trámite con la administración, liberándole de la obligación de aportar dicha documentación.

### 2.1. Beneficios principales

| Beneficio | Descripción |
|---|---|
| Actualización de sistemas | Modernización de los sistemas de intercambio de información |
| Acceso vía Internet | Disponibilidad remota de los servicios |
| Menor tiempo de proceso | Minimización del tiempo de proceso de solicitudes |
| Interlocutor único | Independencia de los orígenes de información |
| Reutilización de recursos | Fomento de la reutilización y optimización de recursos |
| Canal homogéneo | Independiente del proveedor/consumidor |
| Consumo múltiple | Ofertado una vez, consumido por múltiples entidades |
| Menos carga al ciudadano | Reducción de la información solicitada al ciudadano |
| Seguridad en comunicaciones | Plataforma robusta con módulo específico de seguridad, que soporta los últimos estándares de firma electrónica |

### 2.2. Funcionalidades

#### 2.2.1. Garantías de seguridad (autenticidad, confidencialidad, integridad, disponibilidad y trazabilidad)

- **Autenticidad:** Se asegura la identidad de todos los agentes que intervienen en el proceso de intercambio de datos. Mecanismos de identificación:
  - **Certificado digital:** Firma de mensajes en cabecera SOAP conforme a estándares WS-Security. Autenticación mediante certificado cliente en el protocolo SSL.
  - **IP del servidor** que realiza la invocación al servicio.
  - **API-key** para los servicios REST.

- **Autorización:** En todas las peticiones, la PAI comprueba que la aplicación consumidora tiene permisos para invocar al servicio.

- **Confidencialidad:**
  - Mensajes cifrados en su totalidad o solo los bloques con datos sensibles.
  - Información protegida mediante protocolo **HTTPS**.
  - No se almacena información personal de ningún ciudadano en la PAI.

- **Integridad:**
  - Validación de firma de las peticiones (verificación de la firma del mensaje SOAP).
  - Firma de respuestas: en algunos servicios instrumentales, la PAI firma el mensaje de respuesta con el certificado indicado por el proveedor.

- **Disponibilidad:** La PAI tiene una disponibilidad de **24×7** (la disponibilidad de cada servicio depende de la del servicio final).

- **Trazabilidad:**
  - La PAI guarda la información necesaria para verificar el intercambio de mensajes entre consumidor y proveedor.
  - **No almacena** información sobre el contenido del intercambio.
  - Ante una auditoría, la información de la PAI se complementa con la que conservan proveedor y consumidor.

#### 2.2.2. Transformación de mensajes

El bus adecúa y transforma los mensajes al formato y tipo esperado por los distintos servicios.

#### 2.2.3. Orquestación de servicios

La PAI permite definir un **flujo diagramado** con:

- Condiciones de invocación.
- Procesamiento de la información.
- Gestión unificada de errores.
- Almacenamiento de datos de cada petición/respuesta para trazabilidad y explotación estadística.

#### 2.2.4. Herramienta de gestión interna

Herramienta interna de gestión y administración de los servicios publicados en la plataforma y gestión de autorizaciones.

---

## 3. Servicios ofrecidos

Los servicios publicados en la PAI se clasifican en **dos grupos**:

### 3.1. Servicios de Verificación de Datos / Intermediación

Hacen referencia a las capacidades de verificación que la Administración (local, autonómica y central) tiene para **evitar solicitar al ciudadano documentación** que pueda obrar en su poder.

#### Catálogo de organismos cedentes y servicios

| Organismo cedente | Ejemplos de servicios |
|---|---|
| **AEAT** | Nivel de renta; Certificados de estar al corriente de obligaciones tributarias; IRPF; IAE; Pensiones públicas exentas; Validación del NIF; Domicilio fiscal |
| **Catastro** | Datos catastrales; Certificación de titularidad; Bienes e inmuebles; Descriptiva y gráfica; Valor de referencia de inmueble; Documento CSV |
| **CCAA** (todas las que prestan el servicio, incluida GVA) | Estar al corriente de pago con CCAA; Familia numerosa; Discapacidad (RD 888/2022); Tarjeta de estacionamiento por discapacidad; Pareja de hecho; Escolarización; Renta de salario de prestación social básica |
| **CORPME** (Colegio de Registradores) | Registro público concursal; Vigencia de cargo en sociedad; Sucesión de empresas |
| **CGCOM** (Consejo General de Médicos) | Datos públicos de médicos colegiados; Habilitación de médicos colegiados |
| **Consejo General del Notariado** | Subsistencia de poderes notariales; Copia simple de poderes; Notarios y notarías; Subsistencia de administradores de sociedad; Cesiones de crédito |
| **CSD** (Consejo Superior de Deportes) | Condición de deportista de alto nivel |
| **CRUE** | Matrículas universitarias; Datos de acceso a la universidad |
| **DGMM** (Marina Mercante) | Aprobados/titulaciones de embarcaciones de recreo y profesionales; Propiedades; Buques; Certificado profesional; MMSI; Motos náuticas |
| **DGP** (Dirección General de Policía) | Datos de identidad; Verificación de datos de identidad; Residencia de extranjeros; Identidad ampliada de extranjeros |
| **DGT** (Dirección General de Tráfico) | Datos de vehículo; Listado de vehículos de conductor; Permisos de conducir; Sanciones; Titular de vehículo; Distintivo medioambiental; Datos para IVTM; EUCARIS; Historial de domicilios |
| **DGSFP** (Seguros y Fondos de Pensiones) | Entidades aseguradoras; Mediadores de seguros; Planes y fondos de pensiones; Datos de solvencia para concursos públicos |
| **GVA** (servicios propios) | Estar al corriente con la GVA; Familia monoparental; Valenciano (JQCV); Representación desde Cliente PAI; Renta Valenciana de Inclusión (RVI) |
| **IMSERSO** | Nivel y grado de dependencia |
| **INE** | Datos de residencia con fecha de última variación padronal; Convivencia a fecha actual; Histórico de municipios de residencia; Verificación de datos de residencia; Variantes POR LEY (SECOPA) |
| **Instituto Cervantes** | Calificaciones para pruebas de conocimientos constitucionales (nacionalidad) |
| **INSS** | Histórico de prestaciones de incapacidad temporal; Prestaciones de Tarjeta Social Digital; Integrantes de unidad familiar IMV/RIS; Datos económicos de Tarjeta Social Digital |
| **IGAE** | Inhabilitaciones para subvenciones (BDNS); Concesiones de subvenciones ampliado; Subvenciones con MINIMIS; Estar al corriente de pago para reintegro de préstamos y subvenciones; Ayudas del Estado (BDNS) |
| **Ministerio de Asuntos Exteriores** | Firmas para legalización diplomática de documentos públicos extranjeros |
| **Ministerio de Educación** | Títulos universitarios y no universitarios (por documentación y por filiación); Condición de estar becado; Datos de título; Profesiones reguladas (RJCU); Universidades y centros universitarios (RJCU) |
| **Ministerio de Hacienda** | Datos del Registro Oficial de Licitadores y Empresas Clasificadas del Sector Público |
| **Ministerio de Interior** | Víctima del terrorismo; Solicitante de asilo; Datos de una asociación |
| **Ministerio de Justicia** | Nacimiento, matrimonio, defunción (DICIREG); Certificados literales; Antecedentes penales (por filiación, documentación y entidades); Delitos sexuales; Inhabilitaciones para empleo público; Inhabilitaciones para tenencia de animales |
| **Ministerio de Política Territorial** | Inscripción en Registro Central de Personal; Cambio de domicilio |
| **Ministerio de Sanidad** | Formación sanitaria especializada |
| **Ministerio de Transportes** | Vehículo adscrito a autorización de transporte; Autorizaciones de transporte; Licencia internacional; Títulos de transporte; Vehículos VTC y TAXI |
| **Ministerio de Universidades** | Especialidades de titulaciones universitarias sanitarias |
| **MUFACE** | Afiliación; Abonos de servicios; Prestaciones de pago único |
| **SECAD** (Caja General de Depósitos) | Garantías |
| **SEPE** | Datos de contrato; Situación actual de desempleo; Importes de prestación de desempleo; Demandante de empleo |
| **TGSS** | Estar al corriente con la Seguridad Social; Situación laboral; Vida laboral (12 meses / 5 años); Números de afiliación; Plantilla media de empresa; Tramos de autónomos; Deudores tributarios; Trabajadores de empresa por CCC |

### 3.2. Servicios Web Instrumentales

Servicios que permiten realizar **procesos instrumentales** a las entidades de la Administración Pública en su gestión con el ciudadano:

- **Comunicaciones y Notificaciones.**
- **SDC** — Sistema de Datos del Ciudadano de EELL.
- **Registro de Grupos de Interés de la Generalitat:** Servicio de comunicación de actividades de influencia.
- **WSCARBUITS.**

### 3.3. Solicitud de acceso a servicios

Para solicitar el acceso a los servicios de la PAI:

1. Cumplimentar el **formulario de solicitud de acceso** del servicio deseado.
2. **Firmarlo digitalmente** por el titular del órgano solicitante.
3. Enviarlo a: **formularios_interoperabilidad@gva.es**

> La validación de la firma de solicitudes de servicios del Estado se realiza en: https://valide.redsara.es/valide/

### 3.4. Cambio de certificado de acceso

Para cambiar el certificado de la aplicación, se utilizan formularios específicos según el tipo de servicio:

- Servicios de verificación.
- Servicios de verificación de la AEAT.
- Servicios instrumentales.

---

## 4. Arquitectura de la plataforma

La PAI sigue un **modelo de arquitectura SOA** (Arquitectura Orientada a Servicios), siendo la pieza central un **bus** que proporciona una comunicación fiable entre los distintos recursos tecnológicos. Se consigue:

- Óptima **conexión** entre proveedores y consumidores de servicios.
- **Enrutamiento inteligente.**
- **Gestión de errores.**
- **Seguridad.**
- **Monitorización.**

### 4.1. Control de acceso, seguridad y autorizaciones

La plataforma dispone de mecanismos de control basados en **firma digital** en todas las peticiones de servicio:

1. **Primer nivel — Identificación:** Cada petición debe ir firmada con un **certificado válido reconocido por @firma**, lo que permite conocer con total certeza la identidad de la aplicación solicitante.
2. **Segundo nivel — Autorización:** Una vez identificada la entidad, cada aplicación solo puede utilizar servicios para los cuales está **autorizada**.

---

## 5. ¿Cómo usar la plataforma?

### 5.1. Roles de participación

La Administración General del Estado, Entidades Locales y Comunidades Autónomas pueden participar en la PAI con uno de los siguientes roles:

- **Consumidor de servicios** (o *Cesionario* según el ENI — NTI de Protocolos de Intermediación de Datos): entidad que consume un servicio concreto.
- **Proveedor de servicios** (o *Cedente* según el ENI — NTI de Protocolos de Intermediación de Datos): entidad que ofrece un servicio a terceros.

### 5.2. Consumir servicios

Las Entidades Públicas deben generar una petición respetando las reglas del proveedor del servicio y la plataforma, que una vez procesada devuelve la respuesta.

**Requisitos de certificados:**

- **Servicios de verificación:** Se requiere un **certificado de sello de órgano** (exigencia de los organismos proveedores y el MINHAP).
- **Servicios instrumentales:** Se puede utilizar **certificado de aplicación** o de **sello de órgano**.

**Ciclo de consumo completo:**

1. **Preproducción:** documentación disponible → autorización → ejecución y prueba.
2. **Producción:** autorización → puesta en producción.

Se debe solicitar acceso al administrador de la plataforma, que realiza el **alta de la aplicación** y establece los **permisos de acceso**.

Una vez autorizado, las peticiones se realizan conforme al estándar **WS-SECURITY**.

### 5.3. Proveer servicios

Proveer un servicio significa añadirlo a la plataforma para ponerlo a disposición de cualquier entidad.

**Beneficios para el ciudadano:**

- Enriquecer el catálogo de servicios.
- Aumentar en cantidad y calidad la información ofrecida.
- Satisfacer mayor variedad de necesidades.

**Beneficios para la Administración:**

- Fomentar la relación ciudadano-administración.
- Posicionar la Administración Electrónica como referencia en la prestación de servicios web.

### 5.4. Procedimiento para consumo de servicios de verificación

**Base legal:** Art. 28.2 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común:

> *"Los interesados tienen derecho a no aportar documentos que ya se encuentren en poder de la Administración actuante o hayan sido elaborados por cualquier otra Administración. La administración actuante podrá consultar o recabar dichos documentos salvo que el interesado se opusiera a ello."*

**Pasos del procedimiento:**

1. **Análisis de documentación:** El gestor del Sistema de Información analiza qué documentación/información se solicita a la persona interesada para la gestión del procedimiento.

2. **Justificación normativa:** La normativa que regula el procedimiento debe justificar el consumo de los servicios de verificación. Sin justificación normativa, el organismo cedente no autorizará el acceso.

3. **Consulta de servicios disponibles:** Verificar si la documentación puede obtenerse electrónicamente consultando el listado de servicios de verificación en el Portal de la PAI.

4. **Requisitos de consentimiento** (atendiendo al Art. 28.2 de la Ley 39/2015):
   - **Informar** a la persona interesada de que se van a consultar los datos necesarios.
   - Ofrecerle la posibilidad de **oposición motivada** a la consulta.
   - Recoger la **autorización expresa** para el acceso a datos tributarios (si corresponde).
   - En **procedimientos de oficio:** las consultas deben estar amparadas por una LEY (no cabe consentimiento ni oposición, ya que ambas deben ser explícitas).

5. **Si no hay Sistema de Información integrado:** Puede utilizarse el **Cliente de la PAI** (frontal web). Para solicitar acceso se contacta con el Administrador Delegado del organismo.

6. **Si hay aplicación de tramitación:** Se realiza la integración con la capa de servicios web. Se cumplimentan los formularios del servicio correspondiente y se remiten a **formularios_interoperabilidad@gva.es**.

**Documentación habitual para la solicitud:**

- **Solicitud de acceso:** Formulario firmado electrónicamente por el titular del órgano solicitante (Subdirector, equivalente o superior; para AEAT, Director General o superior).
  - Para servicios de la AEAT: firma del titular del órgano + firma del Interlocutor Único de la GVA (Directora General de la ATV).
  - Se cumplimenta una solicitud por cada cedente.
- **Plantilla de procedimientos administrativos:** Hoja con la lista de procedimientos y la normativa asociada que justifica la consulta.

---

## 6. Cliente de la PAI

### 6.1. ¿Qué es?

El **Cliente PAI CV** es un **frontal web** que permite hacer consultas a los servicios de intermediación/verificación de datos que proporciona la PAI.

Tiene disponibles todos los servicios de verificación ofrecidos por:

- El **Estado** a través de la PID.
- Servicios **NO intermediados de la AEAT**.
- La **Generalitat Valenciana** a través de la PAI.

Para que un organismo cesionario firme las peticiones desde el Cliente PAI CV, su certificado debe estar instalado en los servidores de la **DGTIC** (Dirección General de Tecnologías de la Información y las Comunicaciones), lo que implica facilitar la **clave privada del certificado de sello de órgano**.

> **Marco normativo:** Acuerdo del Consell del 28 de junio de 2013, que establece las condiciones y garantías para el acceso y utilización de la PAI de la Generalitat.

### 6.2. ¿Quién puede utilizarlo?

Puede ser utilizado por todo aquel que haya sido **autorizado** para la finalidad descrita en el marco del/los procedimiento/s administrativo/s que gestiona.

### 6.3. ¿Cómo solicitar el acceso?

Contactar con el **Personal Administrador Delegado (PAD)** del organismo para que habilite el acceso.

**Información necesaria para la solicitud:**

| Dato | Descripción |
|---|---|
| Servicios de verificación | Servicios concretos a consultar |
| Código del procedimiento | Para organismos integrados en el **SIA** (Sistema de Información Administrativa): código SIA. Para los no integrados: `[CIF]_[Código procedimiento]` (máx. 20 caracteres, ej: `SXXXX_12345`) |
| Nombre y descripción del procedimiento | Identificación del procedimiento administrativo |
| Consentimiento | Indicar si requiere consentimiento expreso del ciudadano |
| Norma legal | Nombre y enlace de la norma legal del procedimiento |
| Artículos de la norma legal | Artículos que justifican la consulta |
| Caducidad | Indicar si existe caducidad y, en su caso, la fecha |
| Credencial de usuario | Cumplimentar el formulario "Credencial Usuario Cliente" |

### 6.4. Personal Administrador Delegado (PAD)

Cada organismo designa un **Administrador Delegado** encargado de la gestión de usuarios de su organismo en el Cliente PAI CV.

- Debe cumplimentar el **Formulario Solicitud Alta Administrador Delegado**, autorizado por su responsable.
- Se envía firmado electrónicamente a: **formularios_interoperabilidad@gva.es**
- La PAI facilita al PAD el password de acceso a la **zona restringida** de administración.

---

## 7. Normativa y referencias

- **Ley 39/2015**, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (Art. 28.2).
- **Esquema Nacional de Interoperabilidad (ENI)** — RD 4/2010.
- **NTI de Protocolos de Intermediación de Datos.**
- **Acuerdo del Consell del 28 de junio de 2013** — Condiciones de acceso a la PAI de la Generalitat.
- **SCSP** — Sustitución de Certificados en Soporte Papel (especificaciones técnicas de la PID).
- Estándar **WS-Security** (firma SOAP).
- Portal de la PAI: https://pai.gva.es
