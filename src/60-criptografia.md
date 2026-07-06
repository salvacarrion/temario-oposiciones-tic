# Criptografía

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Cifrado y Sistemas Criptográficos

### El cifrado

Proceso de codificación de la información para protegerla de accesos no autorizados. Los **algoritmos acreditados** utilizados para este propósito se encuentran en el documento **"SOGIS Agreed Cryptographic Mechanisms"**.

### Sistemas criptográficos

- **Criptografía simétrica:**
    - Utiliza la **misma clave** para cifrar y descifrar.
    - **Ventaja:** Algoritmos muy rápidos y eficientes.
    - **Desventaja:** Problema en el **intercambio seguro de claves**.
    - **Algoritmos comunes:** DES, 3DES, RC5, AES, Blowfish, IDEA.
- **Criptografía asimétrica:**
    - Utiliza un **par de claves**: una **pública** y otra **privada**.
    - **Ventaja:** Permite el intercambio seguro de información sin previo acuerdo.
    - **Desventaja:** Algoritmos más lentos y, en algunos casos, menos prácticos.
    - **Algoritmos comunes:**
        - **Diffie-Hellman:** Basado en exponenciación modular.
        - **RSA:** Basado en la **factorización de números primos**.

### Acreditación de algoritmos

Son aquellos aprobados por SOG-IS o el CCN. En este documento se marcan **como [A/NA] (Acreditado / No-Acreditado)**

### Cifrado simétrico (o de clave secreta)

Es un método criptográfico donde el emisor y el receptor utilizan **la misma clave** para cifrar y descifrar mensajes. Ambos deben acordar previamente la clave a utilizar.

- **Ventajas:**
    - **Algoritmos muy rápidos** y eficientes en términos de rendimiento.
    - Con claves suficientemente largas (56 a 1024 bits), es **“imposible” romperlas en un tiempo razonable** mediante ataques de fuerza bruta.
- **Desventajas:**
    - **Intercambio de claves:** Dificultad para compartir la clave de manera segura.
- **Tipos de cifrado simétrico:**
    - Cifrado de bloques (block cipher)
    - Cifrado de flujo (stream cipher)
    - Funciones de resumen (hash functions)
- Longitud de clave habitual: **128 bits**
- **Algoritmos simétricos:**
    - **DES (Data Encryption Standard)** \[**NA**\]: Inseguro para claves cortas.
        - Utiliza una **Red de Feistel**, aplicando las mismas operaciones repetidamente.
    - **Triple DES (3DES, TDES, TDEA,...)** \[**A**\]: Aplica **tres veces DES** para mayor seguridad.
    - **AES (Advanced Encryption Standard) o Rijndael** \[**A**\]: Más rápido que 3DES y utiliza una **red de sustitución-permutación**.

**\*Nota:** A/NA == Acreditado/No-Acreditado.

### Cifrado asimétrico (o de clave pública)

Este método utiliza **claves diferentes** para cifrar y descifrar mensajes:

- El **emisor** usa la **clave pública** del receptor para cifrar el mensaje.
- El **receptor** usa su **clave privada** para descifrarlo.
- **Clave privada:** Solo conocida por el usuario.
- **Clave pública:** Accesible para todos.
- **Ventajas:**
    - Permite intercambiar información a través de canales no seguros.
    - En la práctica, se utiliza para **cifrar la clave de sesión simétrica** de cada mensaje.
- **Desventajas:**
    - **Algoritmos más lentos** y, en algunos casos, **inseguros o poco prácticos**.
- **Longitud de clave habitual:** **1024 bits**
- **Algoritmos asimétricos:**
    - **DSA (Digital Signature Algorithm)** \[**A**\]: Sirve para **firmar (autenticar)**, **no** para cifrar información.
    - **RSA (Criptosistema RSA)** \[**A**\]: Se basa en la **factorización de números enteros**.
    - **ECDSA (Elliptic Curve Digital Signature Algorithm)** \[**A**\]: Variante más rápida de DSA.
    - **ECIES (Elliptic Curve Integrated Encryption Scheme)** \[**A**\]

**\*Nota:** A/NA == Acreditado/No-Acreditado

### Protocolos de acuerdo de clave

Estos protocolos permiten establecer claves compartidas entre partes que no han tenido contacto previo.

- **Diffie-Hellman (DH o DHKA)** \[**A**\]:
    - Permite el establecimiento de claves a través de un **canal inseguro y de manera anónima**.
- **MQV (Menezes-Qu-Vanstone Key Agreement)** \[**A**\]
- **ECDH (Elliptic Curve Diffie-Hellman)** \[**A**\]
- **ECMQV (Elliptic Curve Menezes-Qu-Vanstone)** \[**A**\]

**\*Nota:** A/NA == Acreditado/No-Acreditado.

### Función HASH (…o resumen)

Una función hash **convierte uno o varios elementos de entrada en otro elemento** de salida, generalmente una cadena de longitud fija.

- **Propiedades:**
    - **Bajo costo** en términos de memoria y CPU.
    - **Compresión:** Reduce datos grandes a pequeños resúmenes.
    - **Uniformidad:** Los valores resultantes son equiprobables.
    - **Rango variable:** Capacidad de expansión según las necesidades.
    - **Inyectividad y función hash perfecta:** Cada entrada única produce una salida única.
    - **Determinismo:** La misma entrada siempre produce la misma salida.
- **Resistencia frente a colisiones:**
    - **Efecto avalancha:** Un pequeño cambio en la entrada produce un cambio significativo en la salida.
- **Algoritmos de funciones hash:**
    - **MD5 (Message-Digest Algorithm 5) [NA]**
    - **SHA-1 (Secure Hash Algorithm 1)** \[N**A**\]
    - **SHA-2 (Secure Hash Algorithm 2)** \[**A**\]
    - **SHA-3 (Secure Hash Algorithm 3)** \[**A**\]
    - **HMAC (Hash Message Authentication Code)** \[**A**\]
    - **RIPEMD-160 (RIPE Message Digest 160-bit) [NA]**

**\*Nota:** A/NA == Acreditado/No-Acreditado.

### CMAC (Cipher-based Message Authentication Code, MAC)

El **CMAC** es un bloque de bits que actúa como resumen de un mensaje y permite verificar su **autenticidad e integridad**.

- **Propiedad clave:** La variación de un solo bit en el mensaje original produce un **cambio total e imprevisible** en los bits del MAC.
