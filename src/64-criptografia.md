# Criptografía

La criptografía protege la información transformándola de modo que solo las partes autorizadas puedan interpretarla o verificar su origen. Es la base técnica de la confidencialidad de las comunicaciones, de la firma electrónica (tema 65) y de protocolos como TLS o las VPN (temas 70 y 79). Este tema recorre sus bloques constructivos (cifrado simétrico y asimétrico, funciones hash y MAC), la infraestructura de clave pública que hace utilizables las claves públicas, el uso combinado de todo ello en TLS y la transición poscuántica.

## Conceptos y objetivos de la criptografía

La **criptología** engloba la **criptografía** (diseño de técnicas de protección de la información) y el **criptoanálisis** (su ataque para romperlas). Un **criptosistema** transforma el texto en claro en texto cifrado mediante un algoritmo público y una clave secreta.

- **Servicios de seguridad** que proporciona:
    - **Confidencialidad**: solo quien posee la clave accede a la información.
    - **Integridad**: cualquier alteración de los datos resulta detectable.
    - **Autenticación**: se puede verificar la identidad del origen.
    - **No repudio**: el autor no puede negar su actuación (lo aporta la firma digital).
- **Principio de Kerckhoffs** (1883): la seguridad debe residir **exclusivamente en el secreto de la clave**, nunca en el del algoritmo. Los algoritmos serios son públicos y están sometidos a escrutinio; la «seguridad por oscuridad» se considera una mala práctica.
- **Familias de mecanismos**: cifrado **simétrico** (una clave compartida), cifrado **asimétrico** (par de claves pública/privada), y funciones **sin clave** (hash). En la práctica se combinan (cifrado híbrido, firma digital, TLS).

En las administraciones públicas los algoritmos y parámetros no se eligen libremente: el **ENS (RD 311/2022)** exige emplear algoritmos autorizados.

- **mp.info.3.r2 (ENS)**: en categorías media y alta se emplearán «algoritmos y parámetros autorizados por el CCN o por un esquema nacional o europeo que resulte de aplicación». El CCN los determina conforme a la guía **CCN-STIC 807, Criptología de empleo en el ENS** (ed. **mayo 2022**).
- **op.exp.10 (ENS)**: las claves criptográficas se protegerán durante **todo su ciclo de vida** (generación, uso, custodia y destrucción).
- **Mecanismos acordados europeos**: la referencia clásica es el documento **SOG-IS Agreed Cryptographic Mechanisms** (v1.3, **febrero 2023**), en el que se basa la CCN-STIC 807; su sucesor bajo el esquema europeo de certificación EUCC es el **ECCG Agreed Cryptographic Mechanisms** (v2.0, **abril 2025**), que clasifica cada mecanismo como **recomendado (R)** o **legacy (L)** con fecha límite de uso.

## Cifrado simétrico

En el cifrado simétrico (o de clave secreta) emisor y receptor comparten **la misma clave** para cifrar y descifrar. Los algoritmos son **muy rápidos** (con soporte hardware, como las instrucciones AES-NI), por lo que se usan para cifrar los datos en sí; su punto débil es la **distribución de claves**: hace falta un canal seguro previo y, con *n* usuarios, **n(n−1)/2** claves distintas.

- **Cifrado de bloque** (*block cipher*): opera sobre bloques de tamaño fijo (128 bits en AES).
    - **AES (Advanced Encryption Standard)**: el estándar actual (**FIPS 197, 2001**), basado en el algoritmo **Rijndael**. Red de **sustitución-permutación**, bloques de **128 bits** y claves de **128, 192 o 256 bits** (10, 12 o 14 rondas). Es el algoritmo recomendado con carácter general.
    - **DES**: bloques de 64 bits y clave efectiva de **56 bits**, con estructura de **red de Feistel** (16 rondas). **Roto** por fuerza bruta desde 1998; prohibido.
    - **Triple DES (3DES)**: aplica DES tres veces (clave de 112 o 168 bits). **Retirado por el NIST desde el 31-dic-2023** (SP 800-131A); en Europa queda como legacy con límite **2027** (ECCG). No usar en sistemas nuevos.
    - **Históricos**: Blowfish, IDEA, RC5; hoy sin acreditación y en desuso.
- **Cifrado de flujo** (*stream cipher*): genera un flujo de clave que se combina bit a bit con los datos; apto para transmisiones continuas.
    - **ChaCha20**: el cifrador de flujo moderno de referencia (RFC 8439), usado en TLS 1.3 como alternativa a AES en dispositivos sin aceleración hardware.
    - **RC4**: roto; su uso en TLS está prohibido (RFC 7465).
- **Modos de operación** (cómo encadenar bloques para cifrar mensajes largos):
    - **ECB** (*Electronic Codebook*): cada bloque se cifra por separado; bloques iguales producen cifrados iguales y los patrones se filtran. **No debe usarse**.
    - **CBC** (*Cipher Block Chaining*): cada bloque se combina con el cifrado del anterior mediante un vector de inicialización (IV); requiere relleno (*padding*) y no es paralelizable al cifrar.
    - **CTR** (*Counter*): convierte el cifrador de bloque en uno de flujo cifrando un contador; paralelizable y sin relleno.
    - **GCM** (*Galois/Counter Mode*): modo de **cifrado autenticado (AEAD)**, que en una sola pasada garantiza confidencialidad, integridad y autenticidad. Es el modo recomendado (AES-GCM); su equivalente de flujo es **ChaCha20-Poly1305**.
- **Longitud de clave**: el mínimo aceptado hoy es **128 bits**; se recomiendan **256 bits** para información de nivel alto o de vida larga (además, resistente a Grover, ver la sección poscuántica).

## Cifrado asimétrico

En el cifrado asimétrico (o de clave pública) cada parte tiene un **par de claves** matemáticamente vinculadas: la **pública**, que se distribuye libremente, y la **privada**, que solo conoce su titular. Lo que se cifra con una solo se descifra con la otra. Resuelve la distribución de claves y hace posible la firma digital, a costa de ser **órdenes de magnitud más lento** que el simétrico.

- **Usos**: cifrado (hacia el titular de la clave privada), **firma digital** (desde el titular) y **acuerdo de claves**.
- **Algoritmos según el problema matemático**:
    - **RSA**: basado en la **factorización de enteros**. Módulo recomendado **≥ 3000 bits** (en la práctica 3072); las claves de 1900-3000 bits quedaron como legacy hasta el 31-dic-2025 y las de 1024 llevan más de una década prohibidas.
    - **Criptografía de curva elíptica (ECC)**: basada en el logaritmo discreto sobre curvas elípticas; logra la misma seguridad con claves **mucho más cortas** (ECC-256 equivale a RSA-3072), por lo que domina en los sistemas actuales. Curvas habituales: **P-256/P-384** (NIST) y **Curve25519**.
- **Acuerdo de claves**: establecer un secreto compartido a través de un canal inseguro.
    - **Diffie-Hellman (DH)**: el protocolo original, por exponenciación modular; grupos de 2048 bits ya legacy, se exige ≥ 3000.
    - **ECDH**: la variante sobre curvas elípticas, la usada hoy. En su forma **efímera (ECDHE)** genera claves nuevas por sesión, lo que aporta **secreto hacia adelante (*perfect forward secrecy*, PFS)**: comprometer la clave privada del servidor no permite descifrar sesiones pasadas.
- **Firma digital**: se calcula el **hash** del mensaje y se cifra con la **clave privada** del firmante; cualquiera verifica con la pública. Aporta autenticación, integridad y **no repudio**.
    - **ECDSA**: firma sobre curvas elípticas, la más extendida (certificados TLS, DNIe).
    - **EdDSA (Ed25519)**: firma sobre curvas de Edwards, estandarizada en **FIPS 186-5 (febrero 2023)**, que a su vez retira DSA para nuevas firmas.
    - **RSA-PSS**: la variante de firma recomendada de RSA.
- **Cifrado híbrido**: el patrón universal en la práctica. Los datos se cifran con una **clave de sesión simétrica** (rápida) y esa clave se protege con criptografía asimétrica (el «sobre digital»). Así funcionan TLS, PGP o S/MIME.
- **PGP/OpenPGP**: cifrado y firma de correo y ficheros (estándar OpenPGP, **RFC 9580**, 2024; implementación libre GnuPG). Su rasgo distintivo es el modelo de **confianza en malla (*web of trust*)**: los usuarios firman las claves de otros usuarios, sin autoridades de certificación (contrástese con la PKI de la sección siguiente).

| Criterio | Simétrico | Asimétrico |
| --- | --- | --- |
| Claves | Una compartida | Par pública/privada |
| Velocidad | Muy rápido | Lento (~1000× más) |
| Distribución de claves | Problema principal | Resuelta (la pública es libre) |
| Longitud típica | **128-256 bits** | **RSA 3072 / ECC 256** |
| Servicios | Confidencialidad | Firma, acuerdo de claves, no repudio |
| Uso conjunto | Cifra los datos | Protege la clave de sesión |

- **Equivalencia de fortaleza** entre familias (orientativa, NIST SP 800-57):

| Seguridad | Simétrico | RSA/DH | ECC | Hash |
| --- | --- | --- | --- | --- |
| 128 bits | AES-128 | 3072 | 256 | SHA-256 |
| 192 bits | AES-192 | 7680 | 384 | SHA-384 |
| 256 bits | AES-256 | 15360 | 512 | SHA-512 |

## Funciones hash y códigos de autenticación (MAC)

Una función hash criptográfica condensa una entrada de longitud arbitraria en un **resumen (digest) de longitud fija**, sin usar clave alguna. Es **determinista** (la misma entrada produce siempre la misma salida) y **unidireccional**: del resumen no puede recuperarse el mensaje.

- **Propiedades de seguridad** exigibles:
    - **Resistencia a preimagen**: dado un resumen, es inviable hallar una entrada que lo produzca.
    - **Resistencia a segunda preimagen**: dado un mensaje, es inviable hallar otro con el mismo resumen.
    - **Resistencia a colisiones**: es inviable encontrar dos mensajes cualesquiera con el mismo resumen. Las colisiones existen siempre (hay infinitas entradas y salidas finitas); la seguridad consiste en que no se puedan encontrar.
    - **Efecto avalancha**: un cambio mínimo en la entrada altera radicalmente la salida.
- **Algoritmos**:
    - **MD5** (128 bits): **roto** (colisiones prácticas desde 2004); solo aceptable como suma de verificación no criptográfica.
    - **SHA-1** (160 bits): **roto** (colisión pública *SHAttered*, 2017); prohibido en firmas y certificados.
    - **SHA-2** (FIPS 180-4): la familia en uso general (**SHA-256, SHA-384, SHA-512**), estructura Merkle-Damgård.
    - **SHA-3** (FIPS 202, **2015**): basado en **Keccak**, con construcción de **esponja**; alternativa estandarizada con diseño independiente de SHA-2.
- **Usos**: verificación de integridad, firma digital (se firma el hash, no el documento), sellado de tiempo, cadenas de bloques (tema 42) y almacenamiento de contraseñas.
- **Contraseñas**: nunca se almacenan en claro ni con un hash rápido. Se usa un **salt** aleatorio por usuario (impide tablas precalculadas) y funciones **deliberadamente costosas** que frenan la fuerza bruta: **bcrypt**, **scrypt** o **Argon2** (RFC 9106, ganadora de la Password Hashing Competition de 2015, la recomendada hoy).
- **Códigos de autenticación de mensaje (MAC)**: resumen calculado **con una clave secreta compartida**, que garantiza integridad y autenticidad del origen (quien conoce la clave). A diferencia de la firma digital, **no aporta no repudio** (ambas partes conocen la clave).
    - **HMAC** (RFC 2104): construcción sobre una función hash (HMAC-SHA-256); la más usada.
    - **CMAC**: construcción sobre un cifrador de bloque (AES-CMAC).
    - **GMAC**: la parte de autenticación del modo GCM, utilizable sola.

## Infraestructura de clave pública (PKI) y ciclo de vida de certificados

La criptografía asimétrica deja un problema abierto: garantizar que una clave pública pertenece de verdad a quien dice ser su titular (sin ello, un atacante interpuesto puede suplantar claves). La solución es el **certificado digital**: un documento electrónico, firmado por un tercero de confianza, que **vincula una identidad con su clave pública**. La **PKI (Public Key Infrastructure)** es el conjunto de componentes, políticas y procedimientos que sostienen esa confianza.

- **Modelos de confianza**:
    - **Jerárquico (PKI/X.509)**: la confianza emana de una **CA raíz** autofirmada, que certifica CA subordinadas, que a su vez emiten los certificados de entidad final. Es el modelo de la web y de las AAPP.
    - **Malla o *web of trust* (PGP)**: sin autoridades; cada usuario decide en qué claves confía y las firmas cruzadas propagan la confianza.
- **Componentes** (desarrollados en el tema 65): **Autoridad de Certificación (CA)**, que emite y revoca; **Autoridad de Registro (RA)**, que verifica la identidad del solicitante; **Autoridad de Validación (VA)**, que informa del estado; repositorio y **Declaración de Prácticas de Certificación (CPS)**.
- **Certificado X.509 v3** (RFC 5280): formato estándar; contiene la identidad del titular, su clave pública, el período de validez, los usos de la clave y la firma de la CA emisora.
- **Validación de la cadena**: quien verifica un certificado comprueba la **cadena de certificación** completa (entidad final → CA intermedias → CA raíz en su almacén de confianza), la vigencia de cada eslabón y su estado de revocación.
- **Ciclo de vida del certificado (y de sus claves)**:
    1. **Generación del par de claves**, idealmente en el dispositivo del titular o en un HSM (la privada no debe salir).
    2. **Registro**: la RA comprueba la identidad.
    3. **Emisión**: la CA firma el certificado.
    4. **Uso** durante el período de validez.
    5. **Renovación** (con o sin nuevas claves) antes de la caducidad.
    6. **Revocación** si la clave se compromete o cesan las condiciones; **expiración** y archivo al final de la vida.
- **Comprobación de revocación**:
    - **CRL** (*Certificate Revocation List*): lista firmada y periódica de certificados revocados; puede quedar desactualizada entre publicaciones.
    - **OCSP** (RFC 6960): consulta **en línea** del estado de un certificado concreto; con ***OCSP stapling*** es el propio servidor quien adjunta una respuesta OCSP reciente, evitando la consulta del cliente.
- **Custodia de claves privadas**: el ENS exige protegerlas durante todo su ciclo de vida (**op.exp.10**). Medios habituales: **HSM** (*Hardware Security Module*, módulo físico que genera y usa claves sin exponerlas), tarjetas criptográficas (el chip del **DNIe**) y, en firma cualificada, los **QSCD** (dispositivos cualificados de creación de firma del eIDAS, anexo II).

El marco jurídico (eIDAS, Ley 6/2020), los tipos de certificados, los prestadores (FNMT-RCM, ACCV) y las plataformas (@firma, Cl@ve) se estudian en el tema 65.

## Protocolos seguros: TLS

**TLS (Transport Layer Security)** es el protocolo que asegura la mayoría de las comunicaciones en Internet (HTTPS, correo, VPN SSL) y el mejor ejemplo de cómo se combinan todas las piezas anteriores: acuerdo de claves asimétrico, autenticación con certificados X.509 y cifrado simétrico autenticado para los datos. Sus versiones, puertos y despliegue se tratan en el tema 70; las VPN e IPsec, en el 75.

- **Handshake (visión criptográfica)**, en TLS 1.3 (RFC 8446):
    1. **Acuerdo de claves** con **ECDHE** (efímero, con PFS): cliente y servidor derivan un secreto compartido.
    2. **Autenticación** del servidor (y opcionalmente del cliente, mTLS) mediante su **certificado X.509**, cuya cadena valida el cliente.
    3. **Derivación de claves de sesión** simétricas a partir del secreto compartido (función HKDF).
    4. **Datos de aplicación** cifrados con **AEAD** (AES-GCM o ChaCha20-Poly1305).
- **Suites criptográficas** (*cipher suites*): combinación de algoritmos que negocian las partes. TLS 1.3 las reduce a **5**, todas AEAD (p. ej. `TLS_AES_256_GCM_SHA384`), y **elimina los mecanismos débiles** de versiones anteriores: intercambio RSA estático (sin PFS), RC4, 3DES, SHA-1 y los modos CBC.
- **Buenas prácticas**: TLS 1.2 como mínimo (1.0/1.1 deprecadas por RFC 8996), certificados de CA reconocida renovados a tiempo, y priorizar suites con PFS y AEAD.

## Criptografía poscuántica

Un ordenador cuántico criptográficamente relevante rompería la criptografía asimétrica actual: el **algoritmo de Shor** (1994) resuelve la factorización y el logaritmo discreto, acabando con **RSA, DH y ECC**. Al simétrico le afecta menos: el **algoritmo de Grover** (1996) solo reduce la seguridad a la mitad, por lo que **AES-256** sigue siendo seguro. Aunque ese ordenador no existe aún, la amenaza es actual por el patrón ***harvest now, decrypt later***: capturar hoy tráfico cifrado para descifrarlo cuando la tecnología llegue.

- **Estándares NIST** (publicados el **13-ago-2024**):
    - **FIPS 203, ML-KEM** (CRYSTALS-Kyber): encapsulamiento de claves (sustituye a ECDH/RSA en el acuerdo de claves).
    - **FIPS 204, ML-DSA** (CRYSTALS-Dilithium): firma digital, la de uso general.
    - **FIPS 205, SLH-DSA** (SPHINCS+): firma basada en hash, alternativa conservadora.
- **Adopción europea**: el ECCG Agreed Cryptographic Mechanisms v2.0 (abril 2025) ya los recoge como **recomendados**, con preferencia por los parámetros altos (ML-KEM-768/1024, ML-DSA-65/87) y por la **hibridación**: combinar un mecanismo clásico y uno poscuántico, de modo que la seguridad se mantenga si uno de los dos cae. Los navegadores ya despliegan acuerdos híbridos en TLS (X25519 + ML-KEM).
- **Transición**: las organizaciones deben inventariar dónde usan criptografía (inventario criptográfico), priorizar los datos de vida larga y diseñar con **cripto-agilidad** (poder sustituir algoritmos sin rehacer los sistemas).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024): medidas op.exp.10 y mp.info.3.
- CCN-STIC 807, Criptología de empleo en el ENS (ed. mayo 2022).
- SOG-IS Agreed Cryptographic Mechanisms, v1.3 (febrero 2023); ECCG Agreed Cryptographic Mechanisms, v2.0 (abril 2025).
- NIST: FIPS 197 (AES, 2001), FIPS 180-4 (SHA-2, 2015), FIPS 202 (SHA-3, 2015), FIPS 186-5 (firma digital, febrero 2023), FIPS 203/204/205 (poscuántica, agosto 2024), SP 800-57 y SP 800-131A Rev. 2.
- RFC 2104 (HMAC), RFC 5280 (X.509), RFC 6960 (OCSP), RFC 8439 (ChaCha20-Poly1305), RFC 8446 (TLS 1.3), RFC 9106 (Argon2), RFC 9580 (OpenPGP).
- Ediciones de guías y estándares verificadas online en julio de 2026.
