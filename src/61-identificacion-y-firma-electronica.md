# Identificación y firma electrónica

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Identificación y firma electrónica. Marco europeo y nacional. Certificados digitales. Claves privadas, públicas y concertadas. Formatos de firma electrónica. Servicios de directorio. Mecanismos de identificación y firma biométricos

### Servicios de autenticación

Los servicios de autenticación son fundamentales para garantizar la seguridad en sistemas informáticos y redes. Permiten verificar la identidad de usuarios y controlar el acceso a recursos y datos sensibles.

- **Definiciones (RD 1720/2007):**
    - **Identificación:** Procedimiento para reconocer la identidad de un usuario, por ejemplo, mediante nombre de usuario o DNI.
    - **Autenticación:** Procedimiento para comprobar la identidad de un usuario, como el uso de una contraseña.
    - **Control de accesos (autorización):** Mecanismo que permite, en función de la identidad autenticada, acceder a datos o recursos específicos.
- **Triple A (AAA):** Concepto que engloba:
    - **Autenticación (Authentication):** Verificación de identidad.
    - **Autorización (Authorization):** Control de permisos y accesos.
    - **Auditoría (Accounting):** Registro y monitoreo de actividades.
- **Métodos de autenticación:**
    - **Algo que sabemos:** Contraseñas, PINs.
    - **Algo que tenemos:** Tokens, tarjetas inteligentes.
    - **Algo que somos:** Características biométricas como huellas digitales.
- **Sistemas de autenticación:**
    - **Factor único:** Utiliza un solo método de autenticación.
    - **Doble factor:** Combina dos métodos, aumentando la seguridad.
    - **Multifactor:** Utiliza tres o más métodos para una autenticación más robusta.
- **Características deseables:**
    - **Fiabilidad:** Precisión en la identificación.
    - **Viabilidad:** Implementación práctica y eficiente.
    - **Integridad:** Protección contra alteraciones no autorizadas.
    - **Amigabilidad:** Facilidad de uso para los usuarios.

### Identificación Digital (ID)

La identificación digital es el conjunto de mecanismos y medios que garantizan la identidad de personas físicas o jurídicas en entornos digitales, incluyendo la gestión y administración de estos servicios.

- **Garantías que debe ofrecer:**
    - **Autenticación:** Confirmación de la identidad.
    - **Autorización:** Control de acceso a recursos.
    - **Integridad:** Aseguramiento de que la información no ha sido alterada.
    - **Confidencialidad:** Protección de la información contra accesos no autorizados.
- **Medios utilizados:**
    - Tarjetas RFID, DNI electrónico, certificados digitales, tokens, sistemas biométricos, entre otros.

### Firma electrónica y firma digital

La firma electrónica y la firma digital son herramientas que permiten garantizar la identidad del firmante y la integridad de los documentos electrónicos.

- **Firma digital:**
    - **Definición:** Mecanismo criptográfico que permite identificar al emisor de un mensaje y asegurar que no ha sido alterado desde su emisión.
        - **Naturaleza técnica.**
    - **Características:**
        - Garantiza la identidad del firmante.
        - Asegura la integridad del mensaje.
        - Proporciona validez jurídico-administrativa equiparable a la firma manuscrita.
- **Firma electrónica:**
    - **Definición:** "Conjunto de datos en forma electrónica, consignados junto a otros o asociados con ellos, que pueden ser utilizados como medio de identificación del firmante."
        - **Naturaleza jurídica.**
    - **Regulación:**
        - ~~Ley 59/2003~~ (derogada).
        - Reglamento (UE) Nº 910/2014 (eIDAS).
    - **Propiedades:**
        - Identidad.
        - Integridad.
        - No repudio.
    - **Funciones:**
        - **Identificar** al firmante de manera inequívoca.
        - **Asegurar** la integridad del documento.
        - **Garantizar** el no repudio del documento firmado.
    - **Tipos de firma electrónica:**
        - **Simple:** Medios básicos de identificación.
            - **Ejemplo:** PIN, login de usuario, casilla de términos y condiciones,…
        - **Avanzada:** Permite identificar al firmante y detectar cualquier cambio en los datos firmados; está vinculada de manera única al firmante.
            - **Ejemplo:** Firma digitalizada, certificado propio,…
        - **Cualificada (o reconocida):** Es una firma avanzada creada mediante un dispositivo cualificado y basada en un certificado reconocido; tiene equivalencia legal con la firma manuscrita.
            - **Ejemplo:** DNIe, Certificado digital,…
- **Formatos técnicos de firma electrónica:**
    - **CAdES:** Basado en CMS y sintaxis ASN.1.
    - **XAdES:** Basado en sintaxis y formato XML.
- **Modalidades de firma:**
    - **Básica:** Combinación de hash y clave privada.
    - **Fechada:** Firma básica más sello de tiempo.
    - **Completa (validada):** Firma fechada más Dispositivo Seguro de Creación de Firma (DSCF) y certificado reconocido.

### Certificados digitales

Un certificado digital es un documento electrónico firmado por un prestador de servicios de certificación que vincula una clave pública a una identidad, confirmando su autenticidad.

- **Funciones:**
    - Firma electrónica de documentos.
    - Cifrado de información transmitida.
    - Autenticación de identidad en comunicaciones.
- **Información básica contenida:**
    - Identidad del titular.
    - Periodo de validez.
    - Clave pública certificada.
    - Emisor del certificado (Autoridad de Certificación).
- **Formatos de codificación (basados en X.509):**
    - **DER (Distinguished Encoding Rules):** Codificación binaria; extensiones .der, .cer, .crt.
    - **PEM (Privacy-enhanced Electronic Mail):** Texto ASCII Base64; extensiones .pem, .cer, .crt, .key.
    - **PKCS#7 (.p7b / .p7c):** Formato contenedor; no almacena claves privadas.
    - **PKCS#12 (.p12 / .pfx):** Almacena certificados y claves privadas cifradas en un único archivo.
- **Tipos de certificados:**
    - **Certificados del DNI electrónico:** Emitidos por el Cuerpo Nacional de Policía.
    - **Certificado de Sede Electrónica:** Identifica y autentica a un servidor como sede electrónica de una Administración Pública.
    - **Certificado de Empleado Público:** Para identificación y autenticación de empleados públicos en el ejercicio de sus funciones.
    - **Certificado de Sello Electrónico:** Para actuaciones administrativas automatizadas; identifica al órgano o entidad pública.
    - **Certificado de Firma de Código:** Garantiza la identidad del autor de software al firmar código ejecutable.

### Tipos de sellos

- **Sello de tiempo:** Método que prueba que un conjunto de datos existió antes de un momento dado y que no ha sido modificado desde entonces.
- **Sello de tiempo cualificado:** Añade valor a la firma digital al proporcionar una marca temporal fiable de una entidad de confianza, evitando depender únicamente de la hora proporcionada por el firmante.

### Huella digital

Conjunto de datos asociados a un mensaje que permiten asegurar que no ha sido modificado. Se obtiene aplicando una función hash al mensaje.

### Estándar X.509 v3

- **Descripción:** Estándar de la UIT-T para infraestructuras de clave pública (PKI).
- **Características:**
    - Especifica formatos para certificados digitales y algoritmos de hash.
    - Utiliza un sistema jerárquico de autoridades de certificación.
    - Definido en lenguaje ASN.1.
    - Codificado mediante DER o PEM.

### Gestión del ciclo de vida de un certificado

Proceso normalizado que incluye:

1. **Verificación y confirmación de identidad:** La Autoridad de Certificación (CA) verifica la identidad del solicitante, a menudo requiriendo presencia física.
2. **Emisión del certificado:** La CA firma el certificado con su clave privada.
3. **Entrega del certificado:** La CA entrega el certificado al titular, sin mantener copias de la clave privada.

### Infraestructura de Clave Pública (PKI)

La PKI es un conjunto de componentes que permiten la emisión, gestión y validación de certificados digitales.

- **Funciones principales:**
    - **Confidencialidad:** Protección de la información.
    - **Integridad:** Garantía de que la información no ha sido alterada.
    - **Autenticación:** Verificación de identidades.
    - **No repudio:** Imposibilidad de negar la autoría de una acción.
- **Entidades involucradas:**
    - **Autoridad de Certificación (CA):** Emite y gestiona certificados.
    - **Autoridad de Registro (RA):** Verifica la identidad de los solicitantes.
    - **\*Autoridad de Depósito (AD):** Conserva de forma segura los certificados.
    - **\*Suscriptores:** Usuarios que solicitan y utilizan los certificados.
- **Otros componentes:**
    - **Política de Seguridad:** Reglas para mantener la seguridad.
    - **Declaración de Prácticas de Certificados (CPS):** Detalla cómo se implementa la política de seguridad.
    - **Sistema de Distribución de Certificados:** Distribuye y localiza certificados.
    - **Listas de Revocación de Certificados (CRL):** Listas de certificados revocados.

### Localización de claves públicas

- **PGP (Pretty Good Privacy):** Alternativa descentralizada a la PKI tradicional.
    - **Servidores de claves públicas:** Facilitan la distribución de claves.
    - **Anillos de confianza:** Los usuarios firman las claves de otros, estableciendo una red de confianza.

### Prestación de servicios de certificación públicos y privados

- **Obligaciones de los prestadores:**
    - No almacenar ni copiar datos de firma sin autorización.
    - Proporcionar información clara a los solicitantes sobre sus obligaciones y derechos.
    - Mantener directorios actualizados de certificados y su estado.
    - Garantizar servicios de consulta sobre la vigencia de los certificados.
    - En caso de cese de actividad, comunicar con antelación y gestionar la continuidad o extinción de certificados.
- **Obligaciones adicionales para certificados reconocidos:**
    - Demostrar fiabilidad y certificaciones obtenidas.
    - Garantizar la precisión de fechas y horas.
    - Emplear personal cualificado y sistemas fiables.
    - Tomar medidas contra la falsificación.
    - Conservar información relativa a los certificados durante 15 años.
    - Disponer de un seguro de responsabilidad civil adecuado.

### Autoridad de Certificación (CA)

- **Función principal:** Emitir y gestionar certificados digitales.
- **Jerarquía de autoridades:** Las CA pueden estar organizadas en una estructura jerárquica, donde cada CA es avalada por otra de nivel superior hasta llegar a una CA raíz.
- **Principales CA en España:**
    - **Para particulares y empresas:**
        - Fábrica Nacional de Moneda y Timbre (FNMT).
        - Agència Catalana de Certificació (CATCert).
        - Autoritat de Certificació de la Comunitat Valenciana (ACCV).
        - IZENPE.
        - DNI electrónico (Dirección General de la Policía).
    - **Para empresas:**
        - Agencia Notarial de Certificación (ANCERT).
        - ANF Autoridad de Certificación (ANF AC).
        - Autoridad de Certificación de la Abogacía (ACA).
        - Camerfirma.
        - EDICOM.
        - Firma Profesional.

### Mecanismos de identificación y firma biométricos

Los sistemas biométricos utilizan características físicas o comportamentales para identificar y autenticar a los usuarios.

- **Factores biométricos comunes:**
    - **Huellas dactilares.**
    - **Iris y retina.**
    - **Reconocimiento facial.**
    - **Geometría de la mano.**
    - **Venas del dedo o mano.**
    - **Voz.**
- **Ventajas:**
    - Difíciles de falsificar.
    - No requieren memorizar contraseñas.
    - Proporcionan alta seguridad.
- **Consideraciones:**
    - **Privacidad y protección de datos personales.**
    - **Necesidad de equipos especializados.**
    - **Posibles errores de lectura o identificación.**

### Tipos de claves

- **Clave privada:**
    - Conocida solo por el propietario.
    - Utilizada para descifrar información cifrada con la clave pública correspondiente.
    - También se usa para firmar digitalmente.
- **Clave pública:**
    - Disponible para cualquier persona.
    - Utilizada para cifrar información destinada al propietario de la clave privada.
    - Permite verificar firmas digitales.
- **Clave concertada:**
    - Compartida entre dos o más partes.
    - Utilizada para autenticar identidades y cifrar comunicaciones en entornos donde se requiere confianza mutua.

### Certificados del DNI electrónico

- **Tipos de certificados:**
    - **Certificado de Componente:** Asociado al chip del DNIe.
    - **Certificado de Autenticación:** Permite autenticar la identidad del ciudadano.
    - **Certificado de Firma:** Permite realizar firma electrónica reconocida.

### Protocolos de verificación de certificados

- **OCSP (Online Certificate Status Protocol):**
    - Permite determinar el estado de revocación de un certificado en tiempo real.
    - Más eficiente que consultar listas CRL completas.
- **Listas de Revocación de Certificados (CRL):**
    - Listas que contienen certificados revocados antes de su fecha de expiración.
    - Deben ser consultadas para verificar la validez de un certificado.

## Servicios de directorio

Los servicios de directorio son aplicaciones y componentes que permiten gestionar y acceder a información de directorios en una red.

- **Características:**
    - **Dinamismo:** Datos modificables en tiempo real.
    - **Flexibilidad:** Organización y tipos de datos adaptables.
    - **Seguridad:** Gestión de accesos y autenticación.
    - **Personalización:** Información y acceso según el tipo de usuario.
- **Protocolos y estándares:**
    - **X.500:** Conjunto de estándares para servicios de directorio.
    - **LDAP (Lightweight Directory Access Protocol):** Protocolo para acceder y mantener servicios de directorio distribuidos.
        - Basado en TCP/IP.
        - Utiliza estructuras ASN.1.
        - Organiza datos en un árbol de directorio (DIT).
- **Elementos clave:**
    - **DN (Distinguished Name):** Identificador único de cada objeto en el directorio.
    - **LDIF (LDAP Data Interchange Format):** Formato estándar para intercambiar datos de directorio.
- **Funciones de un servicio de directorio:**
    - Autenticación de usuarios.
    - Integración con otras aplicaciones y servicios.
    - Implementación de políticas de seguridad.
    - Gestión y distribución de certificados digitales.
- **Implementaciones de LDAP:**
    - **Active Directory:** De Microsoft.
    - **OpenLDAP:** Proyecto de código abierto.

### Marcos de autenticación

Conjunto de protocolos y tecnologías que permiten autenticar usuarios y gestionar identidades.

- **Funciones:**
    - Autenticar usuarios.
    - Aplicar políticas de acceso.
    - Gestionar credenciales.
- **Categorías:**
    - **Tecnologías delegadas de control de acceso:**
        - **Kerberos:** Protocolo de autenticación en redes que utiliza cifrado simétrico y una tercera entidad de confianza.
        - **RADIUS (Remote Authentication Dial-In User Service):** Protocolo para autenticación y autorización.
        - **Estándar 802.1x:** Control de acceso a redes basado en puertos.
    - **Tecnologías para gestión de identidades federadas:**
        - **OpenID:** Protocolo de autenticación descentralizado que permite a los usuarios acceder a múltiples servicios con una sola identidad.
        - **SAML (Security Assertion Markup Language):** Estándar para intercambio de datos de autenticación y autorización.
        - **XACML (eXtensible Access Control Markup Language):** Estándar para control de acceso basado en atributos.
        - **SPML (Service Provisioning Markup Language):** Estándar para aprovisionamiento de servicios.
- **Otros protocolos y métodos de autenticación:**
    - **RPC seguro (Remote Procedure Call):** Permite llamadas a procedimientos en red con seguridad.
    - **PAM (Pluggable Authentication Module):** Sistema modular para autenticación en Unix.
    - **SASL (Simple Authentication and Security Layer):** Proporciona autenticación y seguridad en protocolos de internet.
    - **SSH (Secure Shell):** Protocolo para acceso remoto seguro.
    - **DIAMETER:** Evolución de RADIUS, utilizado para AAA (Autenticación, Autorización y Accounting).
