# Infraestructuras y servicios comunes de interoperabilidad

Las Administraciones públicas españolas comparten un conjunto de infraestructuras y servicios comunes que hacen posible la interoperabilidad en la práctica: identificarse una sola vez, registrar un documento en cualquier oficina, no aportar datos que ya tiene otra Administración o recibir todas las notificaciones en un único punto. El **artículo 12 del Real Decreto 4/2010** (ENI, ver tema [62](62-esquema-nacional-de-interoperabilidad.md)) ordena a las Administraciones enlazar sus infraestructuras y servicios con «las infraestructuras y servicios comunes que proporcione la Administración General del Estado», para facilitar la interoperabilidad y la relación multilateral. En la misma línea, el **artículo 155 de la Ley 40/2015** obliga a cada Administración a facilitar a las demás el acceso a los datos de los interesados que obren en su poder.

La **disposición adicional primera del RD 4/2010** (en la redacción dada por el RD 203/2021) enumera cuatro **instrumentos para la interoperabilidad**:

- **Sistema de Información Administrativa (SIA)**: inventario de procedimientos y servicios.
- **Centro de Interoperabilidad Semántica de la Administración (CISE)**: almacena, publica y difunde los modelos de datos de los servicios de interoperabilidad.
- **Centro de Transferencia de Tecnología (CTT)**: directorio de aplicaciones de las AAPP para su libre reutilización.
- **Directorio Común de Unidades Orgánicas y Oficinas (DIR3)**.

La mayoría de estos servicios los presta hoy la **Agencia Estatal de Administración Digital (AEAD)**, cuyo estatuto aprobó el **Real Decreto 1118/2024, de 5 de noviembre**: constituida el **21 de febrero de 2025**, asume las funciones de la suprimida **Secretaría General de Administración Digital (SGAD)**. La documentación de todos ellos se publica en el **Portal de Administración Electrónica (PAe)**, administracionelectronica.gob.es.

## Identificación, registro y directorios: SIA, DIR3, SIR y Cl@ve

### Sistema de Información Administrativa (SIA)

El SIA es el inventario de información administrativa común: la relación, clasificada y estructurada, de los procedimientos administrativos y servicios de las Administraciones participantes.

- **Base legal**: el **artículo 9 del RD 4/2010** obliga a cada Administración a mantener actualizado su inventario de procedimientos y servicios y a conectarlo electrónicamente con el SIA; enlaza con el deber del **artículo 21.4 de la Ley 39/2015** de publicar las relaciones de procedimientos con sus plazos máximos y el sentido del silencio.
- **Ámbito**: partió como inventario de la AGE y hoy integra, de forma corresponsable, los procedimientos y servicios de las **comunidades autónomas, entidades locales y universidades** participantes.
- **Contenido**: cada procedimiento se describe con su nivel de informatización, materia, órgano responsable o efectos del silencio, entre otros atributos.
- **Código SIA**: identificador único de cada procedimiento o servicio; actúa como referencia común en el resto de plataformas (las autorizaciones de consulta a la PID o los envíos de Notific@ se vinculan al código SIA del procedimiento que los ampara).

### Directorio Común de Unidades Orgánicas y Oficinas (DIR3)

El DIR3 es el directorio unificado de la organización administrativa española: proporciona una **codificación unívoca** de unidades orgánicas, organismos y oficinas de todas las Administraciones (art. 9 del RD 4/2010).

- **Contenido**: estructura orgánica (unidades y sus relaciones jerárquicas), organismos públicos y **oficinas de registro y de asistencia en materia de registros**, con su información de contacto y localización.
- **Mantenimiento corresponsable**: cada Administración da de alta y actualiza sus propias unidades.
- **Código DIR3**: identifica al remitente y destinatario en los intercambios interadministrativos: origen y destino de los asientos en el **SIR**, órgano gestor, oficina contable y unidad tramitadora en la facturación electrónica (**FACe**) o identificación de organismos emisores de notificaciones.

### Sistema de Interconexión de Registros (SIR)

El SIR es la infraestructura que permite el intercambio de asientos electrónicos de registro entre las Administraciones: un documento presentado en cualquier oficina llega electrónicamente y de forma inmediata al organismo de destino, sin tránsito de papel.

- **Base legal**: el **artículo 16 de la Ley 39/2015** impone a cada Administración un **Registro Electrónico General** y exige que los registros electrónicos de todas las Administraciones sean «plenamente interoperables».
- **Funcionamiento**: las **oficinas de asistencia en materia de registros** digitalizan la documentación presentada en papel, generan copia auténtica y remiten el asiento electrónico al destino a través del SIR, con independencia de su ubicación geográfica o nivel administrativo.
- **Estándar**: los intercambios siguen la NTI de modelo de datos para el intercambio de asientos entre entidades registrales, **SICRES**; la versión vigente es **SICRES 4.0** (Resolución de 22 de julio de 2021), que sustituyó a SICRES 3.0. Solo pueden intercambiar las aplicaciones de registro **certificadas** en el estándar.
- **Soluciones de acceso**: la AGE ofrece en la nube **GEISER** (aplicación integral de gestión de registro para organismos de cualquier nivel) y **ORVE** (oficina de registro virtual, orientada a entidades locales y comunidades autónomas). La adhesión de CCAA y EELL a GEISER/ORVE se regula en la **Resolución de 3 de mayo de 2017**.

### Cl@ve

Cl@ve es la plataforma común del sector público estatal de **identificación, autenticación y firma electrónica** mediante claves concertadas (usuario y contraseña): permite al ciudadano relacionarse electrónicamente sin certificado, aunque también admite los medios tradicionales. Requiere registro previo (presencial en oficinas de registro Cl@ve o por internet).

- **Cl@ve Móvil**: el método más reciente: identificación sin contraseñas, confirmando la petición en la aplicación móvil o escaneando un código QR.
- **Cl@ve PIN**: clave de un solo uso y validez limitada en el tiempo, pensada para accesos esporádicos.
- **Cl@ve Permanente**: usuario y contraseña de validez duradera, reforzada con códigos de un solo uso (SMS) para servicios de mayor nivel de seguridad; es la puerta de acceso a la firma en la nube.
- **Certificado electrónico y DNIe**: la plataforma los admite como medios de identificación junto a las claves concertadas.
- **Firma en la nube (Cl@ve Firma)**: firma electrónica con **certificados centralizados** custodiados en servidores remotos de la Administración. La identificación y firma electrónica se desarrollan en el tema [65](65-identificacion-y-firma-electronica.md).

## Intermediación de datos: la PID

La intermediación de datos da efectividad al derecho del interesado **a no aportar documentos** que ya se encuentren en poder de la Administración actuante o que hayan sido elaborados por cualquier otra Administración (**art. 28.2 de la Ley 39/2015**). La Administración actuante podrá consultarlos o recabarlos «salvo que el interesado se opusiera a ello» (oposición que no cabe en el ejercicio de potestades sancionadoras o de inspección), y deberá recabarlos electrónicamente «a través de sus redes corporativas o mediante consulta a las plataformas de intermediación de datos u otros sistemas electrónicos habilitados al efecto».

La **NTI de Protocolos de intermediación de datos** (Resolución de 28 de junio de 2012) define los roles de todo intercambio intermediado:

- **Cedente**: organización que posee los datos del ciudadano y es responsable de ellos; establece las condiciones de acceso y los ofrece a través de un emisor.
- **Emisor**: quien facilita la cesión de los datos desde el punto de vista tecnológico.
- **Cesionario**: organización autorizada a consultar determinados datos, siempre dentro del marco de un procedimiento administrativo y conforme a las condiciones del cedente.
- **Requirente**: quien facilita la consulta desde el punto de vista tecnológico.
- **Nodo de interoperabilidad**: organismo que presta funcionalidades comunes de intercambio; cedentes y cesionarios pueden delegar en él sus tareas técnicas.

La **Plataforma de Intermediación de Datos (PID)** es el nodo de interoperabilidad de la AGE (hoy gestionado por la AEAD): presta las funcionalidades comunes de intercambio entre emisores y requirentes. Según la NTI, la plataforma:

- **Gestiona** los cesionarios y requirentes según las condiciones establecidas por cada cedente.
- **No almacena** información personal de ningún ciudadano derivada de los intercambios.
- **Asegura** la confidencialidad e integridad de la información intercambiada.
- **Publica** un portal web con el catálogo de servicios disponibles y los formularios de solicitud de acceso.

Los **servicios de verificación y consulta de datos (SVD)** de la PID cubren los certificados en papel más habituales, con un catálogo en crecimiento constante: verificación de datos de **identidad** y **residencia**, prestaciones por desempleo, titulaciones oficiales, condición de familia numerosa o grado de discapacidad, o estar al corriente de las obligaciones tributarias y con la Seguridad Social. Técnicamente los intercambios se realizan mediante servicios web conformes al protocolo **SCSP** (Sustitución de Certificados en Soporte Papel, ver tema [62](62-esquema-nacional-de-interoperabilidad.md)). Las comunidades autónomas acceden a la PID a través de sus propios nodos de interoperabilidad: en la Comunitat Valenciana, la **Plataforma Autonómica de Interoperabilidad (PAI)** (ver tema [82](82-administracion-electronica-y-plataformas-de-la-generalitat.md)).

## Notificaciones y documentos: DEHú, Notific@, INSIDE y ARCHIVE

Las notificaciones electrónicas se practican «mediante comparecencia en la sede electrónica de la Administración u Organismo actuante, a través de la dirección electrónica habilitada única o mediante ambos sistemas» (**art. 43.1 de la Ley 39/2015**). Se entienden practicadas con el acceso a su contenido y **rechazadas a los diez días naturales** desde la puesta a disposición sin acceso (art. 43.2); el aviso al dispositivo o correo electrónico comunicado por el interesado es meramente informativo y su falta no impide la validez de la notificación (art. 41.6 de la Ley 39/2015 y art. 43 del RD 203/2021). Los **artículos 42 a 45 del RD 203/2021** desarrollan la práctica de las notificaciones por ambos sistemas.

### Dirección Electrónica Habilitada única (DEHú)

- **Definición**: «el sistema de información para la notificación electrónica» (**art. 44 del RD 203/2021**), alojado en la sede electrónica del **Punto de Acceso General electrónico (PAGe)** de la AGE. Portal: dehu.redsara.es. Sustituye a la antigua Dirección Electrónica Habilitada (DEH).
- **Obligación estatal**: toda notificación de un emisor del ámbito estatal se pone a disposición del interesado a través de la DEHú; la publicación complementaria en la sede del emisor es opcional (**art. 42.5 del RD 203/2021**).
- **Uso por el ciudadano**: acceso con certificado electrónico, DNIe o Cl@ve, sin necesidad de registro previo; permite consultar y comparecer las notificaciones y comunicaciones de todos los organismos adheridos (AGE, comunidades autónomas y entidades locales) y genera un acuse con fecha y hora del acceso o del rechazo.
- **Sincronización**: si la notificación se pone a disposición también en una sede electrónica, el estado del trámite se sincroniza automáticamente entre ambos sistemas (arts. 44.6 y 45.2 del RD 203/2021), y el plazo cuenta desde el primer acceso o rechazo.
- **Incidencias técnicas**: si una incidencia imposibilita el funcionamiento ordinario de la DEHú, los emisores pueden ampliar el plazo no vencido para comparecer (art. 44.4).

### Notific@

- **Definición**: plataforma compartida de la AGE para la **gestión de notificaciones y comunicaciones**: los organismos emisores le entregan sus envíos y ella gestiona la puesta a disposición y la recogida de evidencias (acuses), devolviéndolas al emisor.
- **Vías de entrega**: puesta a disposición electrónica en la **DEHú** y en la **Carpeta Ciudadana** del Punto de Acceso General y, para las notificaciones en papel, impresión y envío postal a través del **Centro de Impresión y Ensobrado (CIE)**.
- **Ámbito**: disponible también para comunidades autónomas y entidades locales.

### INSIDE

- **Definición**: sistema de gestión de **documentos y expedientes electrónicos conforme al ENI**: garantiza que unos y otros se almacenan e intercambian según las NTI de documento y expediente electrónico (ver temas [55](55-documento-y-expediente-electronico.md) y [62](62-esquema-nacional-de-interoperabilidad.md)), como gestión documental «viva» previa al archivo definitivo.
- **Funciones**: almacenamiento en cualquier gestor documental compatible con el estándar **CMIS**; gestión de los **metadatos obligatorios**; asociación de documentos a expedientes y gestión del índice electrónico; validación y visualización de documentos y expedientes; gestión de las firmas de cada fichero.
- **Interconexión con Justicia**: permite la **remisión electrónica de expedientes administrativos** a los órganos judiciales, eliminando el papel en las relaciones con la Administración de Justicia.

### ARCHIVE

- **Definición**: aplicación de **archivo definitivo** de expedientes y documentos electrónicos de **procedimientos finalizados**; da soporte al **archivo electrónico único** que el **art. 17 de la Ley 39/2015** exige a cada Administración.
- **Modelo**: sigue el modelo **OAIS** de gestión de archivos y cumple las NTI de documento y expediente electrónico, copiado auténtico y política de gestión documental.
- **Funciones**: transferencia de expedientes (desde INSIDE u otros gestores), cuadros de clasificación, políticas de conservación y eliminación, y consulta a largo plazo en formatos interoperables y duraderos.

## Redes de las AAPP: SARA y sTESTA

### La Red SARA

La Red SARA (**Sistema de Aplicaciones y Redes para las Administraciones**) es la red privada de comunicaciones que interconecta las Administraciones públicas españolas entre sí y con las instituciones europeas: una intranet administrativa sobre la que circulan los servicios comunes.

- **Base legal**: el **artículo 13 del RD 4/2010** establece que las Administraciones «utilizarán preferentemente la Red de comunicaciones de las Administraciones públicas españolas» para comunicarse entre sí, conectando a ella sus redes o sus nodos de interoperabilidad; «La Red SARA prestará la citada Red de comunicaciones».
- **Alcance**: conecta la AGE, las comunidades autónomas (que a su vez extienden la conexión a sus entidades locales y organismos a través de sus redes territoriales), universidades y otros organismos públicos.
- **Requisitos de conexión**: los fija la **NTI de requisitos de conexión a la red de comunicaciones de las Administraciones Públicas españolas** (Resolución de 19 de julio de 2011); la interconexión sigue el **plan de direccionamiento** de la Administración (art. 14 del RD 4/2010).
- **Puntos de presencia (PdP)**: ubicaciones con conexión directa a la red sin organismos intermedios; la **Resolución de 4 de julio de 2017** fija las condiciones para que los proveedores de servicios en la nube que sirven a varias Administraciones obtengan esa consideración.
- **Servicios**: sobre SARA se prestan los servicios comunes de este tema (PID, SIR, Notific@, DEHú, @firma) y servicios básicos de infraestructura, como la sincronización con la **hora oficial** del Real Instituto y Observatorio de la Armada (art. 15 del RD 4/2010).
- **nubeSARA**: la nube híbrida del Estado: infraestructura cloud privada de la AGE, gestionada por la AEAD, que aloja a organismos sin centro de proceso de datos propio y ofrece un catálogo de servicios de infraestructura en expansión.
- **Gestión**: corresponde a la **AEAD** (antes SGAD), que planifica, opera y supervisa la red.

### La red europea sTESTA

- **Definición**: la red transeuropea de servicios telemáticos entre administraciones (**Trans European Services for Telematics between Administrations**): red **privada IP** de la Unión Europea que garantiza el intercambio seguro de información entre las administraciones de los Estados miembros y las instituciones y agencias europeas, al margen de internet.
- **Evolución**: nació como **TESTA** (programa IDA, 1996); la versión segura **sTESTA** la sustituyó, y la generación en servicio es **TESTA-ng** (new generation), gestionada por la Comisión Europea en el marco de sus programas de interoperabilidad (ISA² y sucesores).
- **Conexión española**: la **Red SARA está conectada a TESTA**, de modo que cualquier Administración española alcanza los servicios paneuropeos (y las administraciones europeas, los españoles) sin salir de redes privadas.

## Fuentes {.unnumbered .unlisted}

- Real Decreto 4/2010, de 8 de enero, por el que se regula el Esquema Nacional de Interoperabilidad (texto consolidado, última modificación 6 de noviembre de 2024).
- Real Decreto 203/2021, de 30 de marzo, Reglamento de actuación y funcionamiento del sector público por medios electrónicos (texto consolidado, última modificación 2 de abril de 2025).
- Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común (texto consolidado, última modificación 6 de noviembre de 2024); Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (texto consolidado, última modificación 2 de agosto de 2024).
- NTI de Protocolos de intermediación de datos (Resolución de 28 de junio de 2012, BOE núm. 178, de 26 de julio de 2012; sin modificaciones).
- NTI de modelo de datos para el intercambio de asientos entre entidades registrales, SICRES 4.0 (Resolución de 22 de julio de 2021, BOE de 10 de agosto de 2021).
- Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital (BOE-A-2024-22929; constitución efectiva de la Agencia el 21 de febrero de 2025), consultado online en julio de 2026.
- Resoluciones de 19 de julio de 2011 (NTI de requisitos de conexión a la red de comunicaciones), de 3 de mayo de 2017 (adhesión a GEISER/ORVE) y de 4 de julio de 2017 (puntos de presencia de la Red SARA), BOE online, consultadas en julio de 2026.
- Portal de Administración Electrónica (administracionelectronica.gob.es): fichas del CTT de la Red SARA, DEHú, Notific@, INSIDE, ARCHIVE y Servicio de Verificación y Consulta de Datos; portales clave.gob.es y dehu.redsara.es. Consultados en julio de 2026.
