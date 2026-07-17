# RedIRIS e identidad digital federada

**RedIRIS** es la red académica y de investigación española: la infraestructura que interconecta las universidades y los centros de investigación del país entre sí y con las redes académicas internacionales, y que presta a esa comunidad servicios avanzados de conectividad, seguridad e identidad. Sobre ella se apoyan los servicios de **identidad digital federada** del ámbito académico: **eduroam** para la movilidad Wi-Fi y **SIR2/eduGAIN** para el acceso federado a servicios web.

## RedIRIS: la red académica y de investigación española

- **Qué es**: red creada en **1988** en el marco del Plan Nacional de I+D para interconectar los recursos informáticos de las universidades y centros de investigación. Hoy cuenta con **más de 500 instituciones afiliadas** (universidades, OPI, hospitales de investigación, centros tecnológicos), conectadas directamente o a través de las **redes académicas autonómicas**.
- **Gestión**: corresponde a la entidad pública empresarial **Red.es**. RedIRIS tiene la consideración de **Infraestructura Científico-Técnica Singular (ICTS)**.
- **Catálogo de servicios**, agrupables en:
  - **Conectividad**: acceso IP avanzado (IPv4/IPv6, multicast), circuitos dedicados para proyectos científicos y enlaces internacionales.
  - **Seguridad**: el equipo de respuesta a incidentes **IRIS-CERT**, alerta temprana y coordinación de la seguridad de las instituciones afiliadas.
  - **Identidad y movilidad**: **eduroam** y el Servicio de Identidad de RedIRIS (**SIR2**).
  - **Colaboración y comunidad**: correo y filtrado, listas de distribución, servicios a proyectos (y el nodo de interoperabilidad **NISUE**, tema [108](108-administracion-electronica-universitaria.md)).

## RedIRIS-NOVA y GÉANT

- **RedIRIS-NOVA**: la red troncal **de fibra oscura** de RedIRIS, con una huella del orden de **12.000 km** y unos **60 puntos de presencia**, que ofrece a la comunidad investigadora múltiples circuitos de hasta **100 Gbps** desde los principales centros de investigación (incluidos los observatorios de Canarias). Al disponer de fibra propia, la capacidad puede ampliarse iluminando nuevos canales ópticos, lo que la sitúa como infraestructura de las próximas décadas.
- **GÉANT**: la red académica **paneuropea**, una infraestructura de fibra con un punto de presencia por país que interconecta las **redes académicas nacionales (NREN)** europeas (RedIRIS es la NREN española) y las enlaza con las redes académicas del resto del mundo. GÉANT coordina además los servicios federados internacionales de la comunidad (eduroam, eduGAIN).
- **Jerarquía**: campus universitario → red autonómica (si existe) → RedIRIS(-NOVA) → GÉANT → redes académicas mundiales.

## Identidad digital federada: conceptos

En una **federación de identidad**, cada institución actúa como **proveedor de identidad (IdP)** de sus miembros y cada servicio como **proveedor de servicio (SP)**: el usuario se autentica siempre contra su institución de origen, y el servicio recibe solo los **atributos** necesarios (afiliación, correo…), sobre una relación de confianza articulada mediante **metadatos firmados**.

- **Ventajas**: credencial institucional única, las contraseñas nunca viajan al servicio, altas y bajas gestionadas en origen y escalabilidad internacional.
- **Protocolos**: **SAML 2.0** (el estándar de las federaciones académicas) y **OpenID Connect** sobre OAuth 2.0 (tema [65](65-identificacion-y-firma-electronica.md)); dentro de cada universidad, el **single sign-on (SSO)** institucional extiende la misma cuenta a todos los servicios corporativos.

## eduroam: movilidad Wi-Fi académica

- **Qué es**: servicio mundial de **itinerancia Wi-Fi** del ámbito académico (*education roaming*): un miembro de cualquier institución participante se conecta a la red inalámbrica de otra usando las credenciales de su institución de origen, con el identificador `usuario@dominio`.
- **Cómo funciona**: se basa en **IEEE 802.1X** con métodos **EAP** (autenticación extremo a extremo cifrada) y en una **jerarquía de servidores RADIUS**: el punto de acceso delega la autenticación en el RADIUS de la institución visitada, que encamina la petición por el nodo **nacional** (operado por **RedIRIS** en España) hasta el RADIUS de la institución de origen, que valida al usuario. La institución visitada nunca conoce la contraseña.
- **Gobernanza**: servicio global coordinado en Europa por **GÉANT**; cada NREN opera la federación nacional.

## SIR2 y eduGAIN: acceso federado a servicios

- **SIR2 (Servicio de Identidad de RedIRIS)**: la **federación de identidad española** del ámbito académico, con arquitectura de **concentrador (hub)**: los IdP institucionales y los SP se conectan al hub mediante **SAML 2.0** (perfil SAML2int), lo que da a la comunidad **single sign-on web** sobre los servicios académicos (bibliotecas y editoriales, servicios de computación, aplicaciones interuniversitarias).
- **eduGAIN**: la **interfederación** internacional coordinada por GÉANT, que interconecta las federaciones académicas nacionales estableciendo confianza entre sus proveedores. SIR2 participa en eduGAIN: los IdP españoles pueden acceder a servicios académicos globales y los SP españoles recibir usuarios de otras federaciones.
- **Adhesión**: la institución elige su software de IdP (por ejemplo, implementaciones SAML como Shibboleth o SimpleSAMLphp), supera las pruebas técnicas y firma las condiciones de uso de SIR2, que incluyen la solicitud de participación en eduGAIN.

## Fuentes {.unnumbered .unlisted}

- RedIRIS, webs oficiales rediris.es y redirisnova.es (consultadas en julio de 2026).
- GÉANT, geant.org, y documentación de eduroam (eduroam.org) y eduGAIN (edugain.org), consultadas en julio de 2026.
- Procedimientos de adhesión a SIR2/eduGAIN, rediris.es/sir2 (consultados en julio de 2026).
