# Identificación y firma electrónica

La identificación y la firma electrónicas permiten acreditar quién actúa en un medio digital y garantizar la autenticidad e integridad de lo que firma. Su marco jurídico es común a toda la Unión Europea (Reglamento eIDAS, modificado por eIDAS2) y se completa en España con la Ley 6/2020 y con las reglas de uso ante las Administraciones públicas (Leyes 39/2015 y 40/2015 y RD 203/2021).

## Marco europeo y nacional: eIDAS, eIDAS2 y Ley 6/2020

Antes de entrar en las normas conviene fijar tres conceptos que el Reglamento eIDAS define con precisión (art. 3):

- **Identificación electrónica**: «proceso consistente en utilizar los datos de identificación de la persona en formato electrónico que representan de manera única a una persona física o jurídica».
- **Autenticación**: «proceso electrónico que permite la confirmación de la identificación electrónica de una persona física o jurídica, o la confirmación del origen y la integridad de datos en formato electrónico».
- **Factores de autenticación**: algo que se sabe (contraseña, PIN), algo que se tiene (tarjeta, token, teléfono) y algo que se es (biometría). Combinar dos o más da la **autenticación multifactor**; eIDAS2 la recoge como «autenticación reforzada de usuario»: al menos **dos factores de categorías diferentes** e independientes entre sí (art. 3.51). La autorización (qué puede hacer la identidad ya autenticada) y la trazabilidad completan el modelo AAA, que se trata en el tema de seguridad en las comunicaciones.

### Reglamento (UE) 910/2014 (eIDAS)

**Texto consolidado a 18 de octubre de 2024.**

El Reglamento (UE) 910/2014 (eIDAS, *electronic IDentification, Authentication and trust Services*), aplicable en lo esencial desde el **1 de julio de 2016**, derogó la Directiva 1999/93/CE y es directamente aplicable en toda la UE. En España dejó obsoleta la **Ley 59/2003, de firma electrónica, derogada** por la Ley 6/2020. Tiene dos pilares: el reconocimiento transfronterizo de la identificación electrónica y un régimen común de servicios de confianza.

- **Servicios de confianza** (art. 3.16): expedición y validación de certificados (de firma, de sello y de autenticación de sitios web), creación, validación y conservación de firmas y sellos electrónicos, sellos de tiempo electrónicos, entrega electrónica certificada y, tras eIDAS2, expedición y validación de declaraciones electrónicas de atributos, gestión de dispositivos de creación de firma o sello a distancia, archivo electrónico y registro de datos en libros mayores electrónicos.
- **Prestador cualificado de servicios de confianza** (art. 3.20): el que presta uno o varios servicios de confianza cualificados y al que **el organismo de supervisión ha concedido la cualificación**. Se audita al menos **cada 24 meses** por un organismo de evaluación de la conformidad.
- **Identificación electrónica transfronteriza** (arts. 6-9): los Estados notifican a la Comisión sus sistemas de identificación; los medios expedidos bajo un sistema notificado se reconocen en los demás Estados para acceder a servicios públicos en línea.
- **Niveles de seguridad** de los sistemas de identificación (art. 8): **bajo, sustancial y alto**, según su fiabilidad frente al uso indebido o la alteración de la identidad. El reconocimiento mutuo es obligatorio cuando el medio es de nivel **sustancial o alto**.

En cuanto a la firma, el Reglamento distingue tres tipos con efectos jurídicos crecientes:

- **Firma electrónica** (art. 3.10): «los datos en formato electrónico anejos a otros datos electrónicos o asociados de manera lógica con ellos que utiliza el firmante para firmar». El **firmante es siempre una persona física** (art. 3.9).
- **Firma electrónica avanzada** (art. 26), la que cumple cuatro requisitos:
    - estar vinculada al firmante de manera única;
    - permitir la identificación del firmante;
    - haber sido creada utilizando datos de creación de firma que el firmante puede utilizar, con un alto nivel de confianza, bajo su control exclusivo; y
    - estar vinculada con los datos firmados de modo tal que cualquier modificación ulterior de los mismos sea detectable.
- **Firma electrónica cualificada** (art. 3.12): firma avanzada que se crea mediante un **dispositivo cualificado de creación de firmas** y se basa en un **certificado cualificado de firma electrónica**.

| Tipo | Ejemplos | Efecto jurídico (art. 25) |
| --- | --- | --- |
| Simple | PIN, usuario y contraseña, casilla de aceptación, firma escaneada | No se le pueden denegar efectos jurídicos ni admisibilidad como prueba por ser electrónica |
| Avanzada | Firma con certificado no cualificado, firma manuscrita digitalizada con datos dinámicos | Ídem; además garantiza identificación, vinculación única y detección de cambios |
| Cualificada | Certificado cualificado (FNMT, ACCV...) con dispositivo cualificado, DNIe | **Efecto jurídico equivalente al de una firma manuscrita**; se reconoce en todos los Estados miembros |

- **Sello electrónico** (arts. 35-40): el equivalente de la firma para las **personas jurídicas** («creador de un sello», art. 3.24); garantiza el origen y la integridad de los datos. El sello cualificado disfruta de **presunción de integridad de los datos y de corrección del origen** (art. 35.2). Es la base de la actuación administrativa automatizada.
- Estas garantías dan a la firma sus tres propiedades clásicas: **autenticidad** (identifica al firmante), **integridad** (detecta alteraciones) y **no repudio** (el firmante no puede negar la autoría).

### Reglamento (UE) 2024/1183 (eIDAS2) y la cartera europea de identidad digital

El Reglamento (UE) 2024/1183, conocido como **eIDAS2** (DOUE de 30 de abril de 2024, en vigor desde el **20 de mayo de 2024**), modifica el eIDAS para establecer el **marco europeo de identidad digital**. No es un reglamento nuevo: sus cambios están integrados en el texto consolidado del 910/2014.

- **Cartera europea de identidad digital** (*EUDI Wallet*, art. 3.42): «medio de identificación electrónica que permite al usuario almacenar, gestionar y validar de forma segura datos de identificación de la persona y declaraciones electrónicas de atributos con el fin de proporcionarlos a las partes usuarias..., así como firmar por medio de firmas electrónicas cualificadas o sellar por medio de sellos electrónicos cualificados».
- **Obligación de los Estados** (art. 5 bis): cada Estado miembro proporcionará **al menos una cartera** en los **24 meses** siguientes a la entrada en vigor de los actos de ejecución que la desarrollan. Los actos de ejecución se adoptaron el **28 de noviembre de 2024** (Reglamentos de Ejecución (UE) 2024/2977 a 2024/2982; en vigor el 24 de diciembre de 2024), por lo que el plazo vence el **24 de diciembre de 2026**.
- **Características de la cartera**: expedición, uso y revocación **gratuitos para las personas físicas**; uso voluntario; código fuente con **licencia de código abierto**; panel común con el registro de todas las transacciones; nivel de seguridad **alto**; y posibilidad de firmar, por defecto y de forma gratuita, mediante **firmas electrónicas cualificadas** (los Estados pueden limitar la gratuidad a fines no profesionales).
- **Nuevos servicios de confianza**: declaraciones electrónicas de atributos (acreditan características como títulos, poderes o licencias, cotejables con fuentes auténticas), archivo electrónico cualificado, libro mayor electrónico cualificado y gestión de dispositivos cualificados de creación de firma o sello a distancia.

### Ley 6/2020, reguladora de determinados aspectos de los servicios electrónicos de confianza

**Texto consolidado a 9 de mayo de 2023.**

La Ley 6/2020, de 11 de noviembre, **deroga la Ley 59/2003** y regula lo que el eIDAS remite a los Estados miembros. Su objeto (art. 1) es «regular determinados aspectos de los servicios electrónicos de confianza, como complemento del Reglamento (UE) n.º 910/2014».

- **Efectos de los documentos electrónicos** (art. 3): tienen «el valor y la eficacia jurídica que corresponda a su respectiva naturaleza»; su prueba en juicio se rige por el **art. 326 de la Ley de Enjuiciamiento Civil**.
- **Vigencia de los certificados** (art. 4): se extinguen por caducidad o por revocación; el período de vigencia de los **certificados cualificados no será superior a 5 años**.
- **Revocación y suspensión** (art. 5): procede la revocación, entre otras causas, por solicitud del titular, violación o peligro del secreto de los datos de creación, resolución judicial o administrativa, fallecimiento del firmante o extinción de la persona jurídica, terminación de la representación, cese del prestador sin transferencia de certificados o falsedad de los datos aportados.
- **Identidad del titular** (art. 6): en personas físicas, nombre y apellidos y **número de DNI, NIE o NIF** (o un seudónimo inequívoco); en personas jurídicas, denominación o razón social y **NIF**.
- **Comprobación de identidad** (art. 7): exige la **personación** del solicitante, salvo firma legitimada notarialmente o **métodos de identificación a distancia** (vídeo-identificación) con seguridad equivalente certificada por un organismo de evaluación de la conformidad.
- **Obligaciones de los prestadores** (art. 9): no almacenar ni copiar los datos de creación de firma (salvo gestión centralizada en nombre del titular) y ofrecer un **servicio público de consulta** del estado de validez de los certificados. Los prestadores **cualificados** deben además conservar la información de los servicios durante **15 años**, constituir una **garantía (seguro de responsabilidad civil) de al menos 1.500.000 euros** (más **500.000 euros** por cada servicio cualificado adicional) y comunicar el cese de actividad con **2 meses** de antelación.
- **Supervisión** (art. 14): corresponde al **Ministerio de Asuntos Económicos y Transformación Digital** (hoy Ministerio para la Transformación Digital y de la Función Pública), que también mantiene la **lista de confianza (TSL)** con los prestadores cualificados (art. 16).
- **Sanciones** (art. 19): infracciones muy graves, multa de **150.001 a 300.000 euros**; graves, de **50.001 a 150.000 euros**; leves, hasta **50.000 euros**.
- **DNI electrónico** (disposición adicional 3.ª): permite «acreditar electrónicamente la identidad personal de su titular... así como la firma electrónica de documentos», y **todas las personas físicas o jurídicas, públicas o privadas, reconocerán su eficacia**. Lo expiden los órganos competentes del **Ministerio del Interior** (Dirección General de la Policía), que cumplen las obligaciones de los prestadores cualificados.

### Identificación y firma ante las Administraciones públicas

Las Leyes 39/2015 y 40/2015 y el RD 203/2021 concretan qué sistemas se admiten en el procedimiento administrativo.

- **Identificación de los interesados** (art. 9 Ley 39/2015): a) certificados cualificados de **firma electrónica**; b) certificados cualificados de **sello electrónico**; y c) **cualquier otro sistema** que las AAPP consideren válido con **registro previo de usuario** (aquí encajan las claves concertadas tipo Cl@ve, art. 26.2.c del RD 203/2021). Las AAPP deben garantizar que a) y b) sirvan para todo procedimiento, aunque admitan sistemas del tipo c). La aceptación de un sistema por la AGE **vale frente a todas las Administraciones** (art. 9.4).
- **Firma de los interesados** (art. 10 Ley 39/2015): vale «cualquier medio que permita acreditar la autenticidad de la expresión de su voluntad y consentimiento, así como la integridad e inalterabilidad del documento»; en medios electrónicos, los mismos tres bloques de sistemas.
- **Uso obligatorio de firma** (art. 11.2): solo para **formular solicitudes, presentar declaraciones responsables o comunicaciones, interponer recursos, desistir de acciones y renunciar a derechos**; para lo demás basta identificarse.
- **Identificación de las AAPP** (arts. 38-43 Ley 40/2015): certificado de **sede electrónica**, **sello electrónico** basado en certificado cualificado para la actuación administrativa automatizada, **código seguro de verificación (CSV)** vinculado al órgano (art. 42; desarrollado por el art. 21 del RD 203/2021) y firma del **empleado público** (art. 43), con certificados que pueden usar un **número de identificación profesional** en lugar del DNI (art. 23 RD 203/2021). Se desarrollan en los temas de régimen jurídico y administración electrónica.

## Certificados digitales y claves privadas, públicas y concertadas

La firma electrónica basada en certificados se apoya en la criptografía asimétrica (tema de criptografía): cada titular dispone de un par de claves matemáticamente vinculadas, y el certificado da fe de a quién pertenece la pública.

- **Clave privada**: solo la conoce y controla su titular; se usa para **firmar** y para descifrar lo cifrado con la pública.
- **Clave pública**: se distribuye libremente; permite **verificar** las firmas del titular y cifrar información destinada a él.
- **Clave concertada**: secreto compartido pactado entre el usuario y el sistema (usuario y contraseña, PIN); no usa certificados y por eso exige un **registro previo** que garantice la identidad (art. 28 RD 203/2021, conforme al ENS). Es la base del sistema Cl@ve.

El **certificado electrónico** es, según el eIDAS (art. 3.14), «una declaración electrónica que vincula los datos de validación de una firma con una persona física y confirma, al menos, el nombre o el seudónimo de esa persona». Es **cualificado** cuando lo expide un prestador cualificado y cumple el anexo I del Reglamento.

- **Estándar X.509 v3** (UIT-T): formato universal de los certificados; contenido típico: número de serie, identidad del titular, clave pública certificada, período de validez, usos permitidos de la clave, emisor y su firma electrónica.
- **Formatos de codificación**:
    - **DER**: binario (extensiones .der, .cer, .crt).
    - **PEM**: texto Base64 (.pem, .cer, .crt, .key).
    - **PKCS#7** (.p7b): contenedor de certificados, sin clave privada.
    - **PKCS#12** (.p12, .pfx): certificado y clave privada cifrada en un único fichero.
- **Tipos de certificados** habituales en el sector público: de **persona física**, de **representante** (de persona jurídica o de entidad sin personalidad), de **empleado público** (incluida la variante con número de identificación profesional), de **sede electrónica**, de **sello electrónico** (actuación automatizada) y de **autenticación de sitio web** (QWAC).
- **DNI electrónico**: contiene dos certificados del ciudadano, el de **autenticación** y el de **firma**, con claves generadas dentro del chip y protegidas por PIN; la vigencia de los certificados es de **30 meses** (la renovación se hace en los puntos de actualización de las oficinas de expedición).

La gestión de los certificados sigue un **ciclo de vida**: solicitud y registro (comprobación de identidad del art. 7 de la Ley 6/2020), emisión (el prestador firma el certificado con su clave privada y lo entrega sin conservar la clave privada del titular), uso, renovación y extinción (caducidad, como máximo a los **5 años** en cualificados, o revocación/suspensión).

Todo ello lo sostiene la **infraestructura de clave pública (PKI)**:

- **Autoridad de Certificación (CA)**: emite y gestiona los certificados; las CA se organizan jerárquicamente bajo una **CA raíz**.
- **Autoridad de Registro (RA)**: verifica la identidad de los solicitantes antes de la emisión.
- **Autoridad de Validación (VA)**: informa del estado de los certificados.
- **Repositorio** y **Declaración de Prácticas de Certificación (CPS)**: publicación de certificados, políticas y prácticas del prestador.
- **Consulta del estado de revocación**: mediante **CRL** (listas de revocación descargables) o **OCSP** (consulta en línea del estado de un certificado concreto, más eficiente).

En España los prestadores cualificados figuran en la **lista de confianza (TSL)** que publica el ministerio supervisor. Destacan la **FNMT-RCM** (certificados de persona física, representante y AAPP), la **Dirección General de la Policía** (DNIe) y, en el ámbito valenciano, la **ACCV** (Autoritat de Certificació de la Comunitat Valenciana), gestionada hoy por **Istec** (Infraestructures i Serveis de Telecomunicacions i Certificació, SA), empresa del sector público instrumental de la Generalitat.

## Formatos de firma electrónica y sellado de tiempo

Técnicamente, firmar consiste en calcular la **huella digital (hash)** del documento y cifrarla con la clave privada del firmante; quien verifica recalcula el hash y lo compara con el descifrado usando la clave pública. Los formatos normalizan cómo se empaqueta esa firma junto con el documento, los certificados y las evidencias de validación.

- **Familia AdES** (*Advanced Electronic Signatures*, estándares ETSI):
    - **XAdES**: firma en sintaxis XML; habitual en documentos administrativos y servicios web.
    - **CAdES**: firma binaria basada en CMS/ASN.1; apta para ficheros grandes.
    - **PAdES**: firma embebida en documentos PDF; la ve cualquier lector de PDF.
    - **ASiC**: contenedor que asocia ficheros y sus firmas XAdES/CAdES en un único paquete.
- **Decisión de Ejecución (UE) 2015/1506**: fija los perfiles de estos formatos que las AAPP están obligadas a reconocer cuando reciben firmas avanzadas (arts. 27.5 y 37.5 del eIDAS).
- **Niveles *baseline*** (evidencias incrementales que alargan la validez de la firma):

| Nivel | Contenido |
| --- | --- |
| **B-B** (Basic) | Firma básica con el certificado del firmante |
| **B-T** (Timestamp) | Añade un **sello de tiempo** que prueba cuándo se firmó |
| **B-LT** (Long Term) | Añade los datos de validación (cadena de certificados, CRL/OCSP) |
| **B-LTA** (Long Term with Archive) | Añade resellados periódicos para conservación **longeva** |

- **Relación firma-documento**: firma *enveloped* (dentro del documento), *enveloping* (el documento dentro de la firma) y *detached* (en fichero separado).
- **NTI de Política de Firma y Sello Electrónicos y de Certificados** (Resolución de 27 de octubre de 2016): define las reglas comunes de creación y validación de firmas en las AAPP: formatos CAdES, XAdES y PAdES conforme a la Decisión 2015/1506, perfil mínimo **-EPES** (firma básica con referencia a la política de firma), resellado de tiempo para las firmas longevas y valores del metadato «Tipo de firma» de la NTI de Documento electrónico.
- **Sello de tiempo electrónico** (art. 3.33 eIDAS): «datos en formato electrónico que vinculan otros datos en formato electrónico con un instante concreto, aportando la prueba de que estos últimos datos existían en ese instante». Lo emite una **Autoridad de Sellado de Tiempo (TSA)**. El sello **cualificado** goza de **presunción de exactitud de la fecha y hora** y de integridad de los datos vinculados (art. 41.2), y debe basarse en una fuente de tiempo vinculada al **Tiempo Universal Coordinado (UTC)** y estar firmado o sellado por el prestador cualificado (art. 42).

## Plataformas: @firma, FIRe y Cl@ve Firma

La AGE ofrece a todas las Administraciones un conjunto de servicios comunes de identificación, firma y validación, gestionados hoy por la **Agencia Estatal de Administración Digital (AEAD)** y descritos en el tema de infraestructuras y servicios comunes de interoperabilidad.

- **Cl@ve**: sistema común de **identificación, autenticación y firma electrónica** para el sector público, basado en claves concertadas; evita que cada Administración mantenga sus propios sistemas y que el ciudadano recuerde múltiples contraseñas. Requiere **registro previo** (presencial en oficina, por vídeo-identificación desde la app o por internet con certificado o carta de invitación), con nivel básico o avanzado según el método. Modalidades:
    - **Cl@ve PIN**: clave ocasional de un solo uso y validez limitada, orientada a accesos esporádicos.
    - **Cl@ve Permanente**: usuario y contraseña duradera, reforzada con claves de un solo uso por SMS; da acceso a la firma en la nube.
    - **Cl@ve Móvil**: identificación sin contraseñas, escaneando un código QR o confirmando una notificación en la app Cl@ve.
    - Admite además la identificación con **DNIe y certificados electrónicos**, e integra el **nodo eIDAS** español para el reconocimiento de identidades de otros Estados miembros.
- **Cl@ve Firma**: servicio de **firma en la nube** con **certificados centralizados emitidos y custodiados por la Dirección General de la Policía**; la **Gerencia de Informática de la Seguridad Social (GISS)** actúa como prestador de servicios de confianza y custodia la copia de seguridad. El ciudadano firma sin instalar nada, autenticándose con Cl@ve Permanente.
- **@firma**: plataforma de **validación multi-PKI de certificados y firmas** de la AGE; es la «plataforma de verificación de la vigencia y del contenido de los certificados cualificados» del **art. 16 del RD 203/2021**, de uso libre y gratuito para todo el sector público, a la que los prestadores cualificados deben facilitar acceso gratuito de verificación.
- **VALIDe**: portal público de @firma para validar certificados y firmas, generar firmas en múltiples formatos y visualizarlas con su visor.
- **Autofirma**: aplicación de escritorio de firma electrónica; el usuario elige el fichero y la aplicación aplica automáticamente el formato de firma adecuado. Es también el componente de firma local que invocan las sedes electrónicas.
- **FIRe**: **solución integral de firma** que unifica tras una única API la firma local (Autofirma) y la firma en la nube (Cl@ve Firma), de modo que las aplicaciones deleguen en ella toda la lógica de firma.
- **TS@**: plataforma de **sellado de tiempo** de la AGE (autoridad de sellado de tiempo para las AAPP).

## Identificación y firma biométricas; servicios de directorio

La biometría autentica a la persona por lo que **es**, midiendo rasgos fisiológicos (huella dactilar, iris y retina, geometría facial o de la mano, patrón venoso) o de comportamiento (voz, dinámica de tecleo, trazo de la firma manuscrita).

- **Ventajas**: el rasgo no se olvida, no se presta y es difícil de falsificar; comodidad de uso.
- **Limitaciones**: tasas de error (falsos positivos y falsos rechazos), necesidad de sensores específicos y, sobre todo, **irrevocabilidad**: una huella comprometida no puede sustituirse como una contraseña.
- **Protección de datos**: los datos biométricos dirigidos a identificar de manera unívoca a una persona son una **categoría especial de datos** (art. 9 RGPD): su tratamiento exige una base de legitimación reforzada y, con carácter general, **evaluación de impacto** previa (tema de protección de datos).
- **Firma biométrica (manuscrita digitalizada)**: captura en una tableta el trazo con sus datos dinámicos (presión, velocidad, aceleración) y los vincula al documento. Si garantiza la vinculación única al firmante, su identificación y la detección de cambios posteriores, puede constituir una **firma electrónica avanzada** del art. 26 del eIDAS; es habitual en la atención presencial (banca, sanidad, oficinas de registro).

Los **servicios de directorio** almacenan y sirven de forma centralizada la información de identidad de una organización (usuarios, credenciales, grupos, certificados), y son la pieza sobre la que se apoyan la autenticación centralizada y las políticas de acceso.

- **X.500**: familia de estándares UIT-T de la que deriva el modelo de directorio.
- **LDAP** (*Lightweight Directory Access Protocol*): protocolo estándar de acceso a directorios sobre TCP/IP; organiza los datos en un árbol (**DIT**), identifica cada entrada por su **nombre distinguido (DN)** e intercambia datos en formato **LDIF**.
- **Implementaciones**: **Active Directory** (Microsoft, integra LDAP con Kerberos en dominios Windows) y **OpenLDAP** (código abierto).
- **Funciones típicas**: autenticación de usuarios, inicio de sesión único corporativo, aplicación de políticas de seguridad y publicación de certificados y listas de revocación.
- **Federación de identidades**: permite el inicio de sesión único entre organizaciones distintas mediante un proveedor de identidad de confianza; estándares **SAML 2.0** (habitual en las AAPP y en Cl@ve), **OAuth 2.0** (autorización delegada) y **OpenID Connect** (autenticación sobre OAuth 2.0). Los protocolos de control de acceso a red y AAA (Kerberos, RADIUS, 802.1X) se estudian en el tema de seguridad en las comunicaciones.

## Supuesto práctico: identificación y firma en un trámite de subvenciones

**Enunciado**: un organismo autonómico diseña un nuevo trámite de **solicitud de subvenciones** en su sede electrónica, dirigido a personas físicas y jurídicas. Debe decidir qué sistemas de **identificación y firma** admite a los interesados y en qué pasos exige cada cosa; cómo se identifica y firma la **Administración**, incluida la **resolución automatizada** de las solicitudes que cumplen requisitos objetivos; qué **formatos de firma** usar para que las firmas sigan siendo válidas durante los **6 años** de conservación del expediente; y sobre qué **plataformas comunes** apoyarse.

**Se pide**:

- a) Seleccionar los sistemas de identificación y firma de los interesados y cuándo exigir firma.
- b) Definir la identificación y firma de la Administración actuante.
- c) Elegir los formatos de firma y garantizar su validez a largo plazo.
- d) Diseñar la arquitectura sobre las plataformas comunes.

**Resolución**:

**a) Sistemas de los interesados**

- **Identificación (art. 9 Ley 39/2015)**: se admiten los tres bloques: **certificados cualificados de firma** (incluido el DNIe), **certificados cualificados de sello** y un sistema de **clave concertada con registro previo**: **Cl@ve** (PIN, Permanente y Móvil), cuya aceptación por la AGE **vale frente a todas las Administraciones** (art. 9.4). Los sistemas basados en certificado deben poder usarse **en todo caso**.
- **Nivel de seguridad**: el trámite maneja datos personales y económicos, por lo que se exige un nivel de garantía equivalente a **sustancial** (eIDAS): en Cl@ve, el **registro avanzado** (presencial, vídeo-identificación o con certificado) habilita la tramitación completa; el registro básico se limita a consultas.
- **Cuándo exigir firma (art. 11.2 Ley 39/2015)**: solo para **formular la solicitud**, presentar declaraciones responsables o comunicaciones, interponer recursos, desistir y renunciar; para el resto (consultar el expediente, comparecer una notificación) **basta la identificación**.
- **Personas jurídicas**: certificado de **representante** (o apoderamiento inscrito en el registro electrónico de apoderamientos, tema [54](54-administracion-electronica.md)).

**b) Identificación y firma de la Administración**

- **Sede electrónica**: certificado de **sede** que autentica el dominio y cifra el canal (TLS).
- **Actuación administrativa automatizada**: la resolución automatizada se firma con **sello electrónico de órgano** basado en certificado cualificado (art. 42 Ley 40/2015); el sello cualificado goza de **presunción de integridad y de corrección del origen** (art. 35.2 eIDAS).
- **Código seguro de verificación (CSV)**: todos los documentos emitidos lo incorporan, permitiendo el **cotejo en la sede** de las copias impresas (art. 42 Ley 40/2015 y art. 21 RD 203/2021).
- **Personal actuante**: firma de **empleado público** con certificado cualificado, usando el **número de identificación profesional** en lugar del DNI para no exponer datos personales (art. 23 RD 203/2021).

**c) Formatos de firma y validez a largo plazo**

- **Formatos AdES** conforme a la **NTI de Política de Firma** (Resolución de 27 de octubre de 2016) y la Decisión 2015/1506: **PAdES** para los PDF del expediente (la firma la ve cualquier lector), **XAdES** para los intercambios XML entre aplicaciones y **CAdES** para ficheros grandes; perfil mínimo **-EPES**, con referencia a la política de firma.
- **El problema de la caducidad**: los certificados cualificados duran como máximo **5 años** (30 meses los del DNIe), menos que los 6 años de conservación: una firma básica dejaría de poder validarse con garantías.
- **Solución**: completar las firmas al nivel ***baseline* B-LT** (incorporando en el momento de la validación la cadena de certificados y las evidencias CRL/OCSP) y **resellar periódicamente** (**B-LTA**) con **sellos de tiempo cualificados**, que gozan de presunción de exactitud de fecha y hora (art. 41.2 eIDAS) y renuevan la protección criptográfica mientras dure la conservación.
- **Verificación en la recepción**: cada firma recibida se valida contra la **TSL** de prestadores cualificados y el estado de revocación, y la evidencia de esa validación se archiva con el documento.

**d) Arquitectura sobre plataformas comunes**

- **Identificación**: integración de la sede con **Cl@ve**, que engloba claves concertadas, certificados y DNIe, e incorpora el **nodo eIDAS** español para ciudadanos de otros Estados miembros.
- **Firma del interesado**: **FIRe** como API única que orquesta **Autofirma** (firma local con el certificado del usuario) y **Cl@ve Firma** (firma en la nube con certificados centralizados, para quien no tiene certificado en su equipo).
- **Validación**: **@firma**, la plataforma multi-PKI del art. 16 del RD 203/2021, para validar certificados y firmas recibidas (con **VALIDe** como herramienta de apoyo).
- **Sellado de tiempo**: **TS@** como autoridad de sellado de tiempo para los sellos y resellados de las firmas longevas.
- **Ámbito valenciano**: los certificados de la **ACCV** (empleado público, sello de órgano, sede) y las plataformas equivalentes de la Generalitat (tema [82](82-administracion-electronica-y-plataformas-de-la-generalitat.md)) completan la solución.

## Fuentes {.unnumbered .unlisted}

- Reglamento (UE) n.º 910/2014 (eIDAS), texto consolidado a 18 de octubre de 2024 (02014R0910-20241018, EUR-Lex; incorpora las modificaciones del Reglamento (UE) 2024/1183).
- Reglamento (UE) 2024/1183 (eIDAS2), DOUE L de 30 de abril de 2024; Reglamentos de Ejecución (UE) 2024/2977 y 2024/2981, de 28 de noviembre de 2024 (DOUE de 4 de diciembre de 2024), consultados vía EUR-Lex/cellar en julio de 2026.
- Ley 6/2020, de 11 de noviembre, reguladora de determinados aspectos de los servicios electrónicos de confianza (texto consolidado, última modificación 9 de mayo de 2023).
- Ley 39/2015, de 1 de octubre (texto consolidado, última modificación 6 de noviembre de 2024); Ley 40/2015, de 1 de octubre (texto consolidado, última modificación 2 de agosto de 2024).
- Real Decreto 203/2021, de 30 de marzo, Reglamento de actuación y funcionamiento del sector público por medios electrónicos (texto consolidado, última modificación 2 de abril de 2025).
- NTI de Política de Firma y Sello Electrónicos y de Certificados de la Administración (Resolución de 27 de octubre de 2016, BOE de 3 de noviembre de 2016; sin modificaciones).
- Portales oficiales: clave.gob.es, firmaelectronica.gob.es (AEAD), dnielectronico.es, accv.es y RedIRIS (ficha FIRe). Consultados en julio de 2026.
