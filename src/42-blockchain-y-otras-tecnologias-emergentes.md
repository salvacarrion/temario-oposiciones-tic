# Blockchain y otras tecnologías emergentes

Blockchain permite registrar transacciones y activos de forma compartida e inalterable sin depender de un intermediario central: la confianza la aporta la propia tecnología. Este tema cubre sus fundamentos y funcionamiento, los tipos de redes y los contratos inteligentes, las organizaciones descentralizadas y los casos de uso en la Administración, y cierra con una panorámica breve de la realidad extendida y los metaversos.

## Blockchain: fundamentos y funcionamiento

**Blockchain** (cadena de bloques) es una tecnología de **libro mayor distribuido** (*Distributed Ledger Technology*, DLT) que mantiene una base de datos compartida, descentralizada e inalterable entre participantes que no necesitan confiar entre sí: la confianza la aportan la criptografía y el consenso de la red, no una autoridad central.

Sus elementos principales:

- **Libro mayor distribuido**: todos los nodos de la red guardan una copia del registro completo de transacciones; ninguna entidad lo controla en exclusiva.
- **Registros inalterables (inmutabilidad)**: una transacción registrada no puede modificarse ni eliminarse; un error se corrige añadiendo una nueva transacción, y ambas quedan visibles, lo que refuerza la transparencia.
- **Criptografía**: cada participante posee un par de claves con el que firma sus transacciones; las funciones hash garantizan la integridad de los datos.
- **Consenso**: el mecanismo por el que los nodos acuerdan qué bloque se añade a la cadena.

El **funcionamiento** sigue una secuencia:

- Las transacciones se firman electrónicamente por el emisor y se difunden a la red.
- Los nodos las agrupan en **bloques**. Cada bloque contiene los datos de las transacciones, su propio **hash** (identificador único generado criptográficamente) y el **hash del bloque anterior**, que encadena los bloques entre sí.
- Las transacciones del bloque se resumen en un **árbol de Merkle**: cada transacción es un nodo hoja con su hash, los hashes se combinan por pares en nodos intermedios y el proceso continúa hasta un único hash final, la **raíz de Merkle**. Así se puede verificar la integridad de una transacción comparando unos pocos hashes, sin revisar todo el bloque.
- Alterar un bloque cambia su hash e invalida todos los posteriores: manipular la cadena exigiría rehacerla y ganar el consenso de la red, lo que resulta inviable en redes grandes.

Los **mecanismos de consenso** determinan quién valida y con qué coste:

- **Prueba de trabajo** (*Proof of Work*, PoW): los mineros compiten por resolver un problema criptográfico costoso; quien lo logra propone el bloque y recibe una recompensa. Es el mecanismo de **Bitcoin**: muy seguro, pero de **alto consumo energético** y capacidad limitada.
- **Prueba de participación** (*Proof of Stake*, PoS): los validadores se seleccionan en función de las monedas que depositan como garantía (*stake*) y pierden parte de ella si actúan deshonestamente. **Ethereum migró de PoW a PoS en 2022** (*The Merge*), recortando su consumo energético en más del **99 %**.
- **Consensos permisionados**: en redes con validadores identificados se usan algoritmos de tolerancia a fallos bizantinos (BFT y variantes), rápidos y sin minería.
- **Ataque del 51 %**: quien controle la mayoría del poder de cómputo (PoW) o de la participación (PoS) podría reescribir la parte reciente de la cadena; es la principal amenaza teórica, relevante sobre todo en redes públicas pequeñas.

En conjunto, blockchain ofrece **confianza sin intermediarios**, integridad, transparencia, trazabilidad y disponibilidad (no hay punto único de fallo), además de automatización mediante contratos inteligentes. Sus **limitaciones**: el llamado trilema entre escalabilidad, seguridad y descentralización (mejorar dos suele sacrificar la tercera), un rendimiento muy inferior al de una base de datos convencional, el coste energético del PoW y el encaje difícil de la inmutabilidad con el derecho de supresión del RGPD. Si existe una autoridad de confianza natural, una base de datos tradicional suele ser la solución adecuada.

## Tipos de redes y smart contracts

Según quién puede participar, las redes son **abiertas** (*permissionless*: cualquiera lee y valida) o **permisionadas** (*permissioned*: el acceso y la validación requieren autorización). Sobre esa base se distinguen cuatro tipos:

| Tipo | Acceso y validación | Ejemplos |
| --- | --- | --- |
| Públicas | Abiertas a cualquiera; validación descentralizada entre miles de nodos anónimos | Bitcoin, Ethereum |
| Privadas | Una sola organización controla el acceso y la validación | Redes internas corporativas |
| De consorcio (federadas) | Varias organizaciones identificadas comparten la gobernanza y validan | Alastria, EBSI |
| Híbridas | Combinan una parte restringida con otra pública | Datos privados con anclaje de pruebas en una red pública |

- **Públicas**: máxima descentralización y transparencia; a cambio, alto coste computacional (PoW), poca privacidad (todo es visible) y rendimiento limitado.
- **Privadas**: eficientes y con control de acceso, pero de descentralización limitada: existe riesgo de concentración del poder en el administrador.
- **De consorcio**: equilibrio entre confianza y eficiencia; es el modelo habitual en banca y Administraciones, donde los participantes están identificados.
- **Híbridas**: útiles cuando conviene mantener datos privados y publicar pruebas verificables de ellos.

Los **contratos inteligentes** (*smart contracts*) son programas almacenados en la propia blockchain que se ejecutan automáticamente cuando se cumplen las condiciones pactadas, sin intermediarios:

- **Ethereum** los popularizó (2015) con su máquina virtual (**EVM**) y el lenguaje **Solidity**; las plataformas permisionadas empresariales (Hyperledger Fabric, Besu) también los soportan.
- **Aplicaciones**: pagos condicionados, garantías y depósitos, automatización de acuerdos entre múltiples partes.
- **Riesgos**: un error de programación es explotable y difícil de revertir (el caso **The DAO, 2016**, acabó bifurcando Ethereum) y dependen de **oráculos** (fuentes externas de datos) cuya fiabilidad hay que garantizar.
- **Tokens**: activos digitales emitidos mediante contratos inteligentes; pueden ser **fungibles** (intercambiables entre sí, como las criptomonedas; estándar ERC-20) o **no fungibles** (**NFT**, únicos e indivisibles; estándar ERC-721), usados para representar activos digitales o físicos.
- **dApps**: aplicaciones descentralizadas cuya lógica de negocio reside en contratos inteligentes.

## Organizaciones descentralizadas (DAO) y casos de uso en la Administración

Una **DAO** (*Decentralized Autonomous Organization*, organización autónoma descentralizada) es una organización cuyas reglas de funcionamiento están codificadas en contratos inteligentes sobre una blockchain, sin autoridad central:

- **Autonomía**: opera automáticamente según las reglas preestablecidas.
- **Transparencia**: toda su actividad es visible y verificable en la cadena.
- **Decisión colectiva**: los miembros votan las propuestas, habitualmente con *tokens* de gobernanza.
- **Inmutabilidad**: las reglas son difíciles de alterar una vez desplegadas, lo que da confianza pero resta flexibilidad.
- **Retos**: la mayoría de ordenamientos no les reconoce personalidad jurídica, con lo que la responsabilidad de sus actos y la jurisdicción aplicable siguen siendo cuestiones abiertas.

El **marco regulatorio europeo** de los criptoactivos ya existe y conviene conocerlo:

- **Reglamento (UE) 2023/1114 (MiCA**, *Markets in Crypto-Assets*): primer marco integral de la UE sobre criptoactivos; regula a los emisores y a los proveedores de servicios (custodia, intercambio) y es **plenamente aplicable desde el 30 de diciembre de 2024**. En España supervisan la **CNMV** y el **Banco de España**.
- **Reglamento (UE) 2022/858**: régimen piloto para infraestructuras de mercado basadas en DLT (negociación y liquidación de instrumentos financieros tokenizados).
- **Reglamento (UE) 2024/1183 (eIDAS 2)**: incorpora los **libros mayores electrónicos** como nuevo servicio de confianza y crea la **Cartera Europea de Identidad Digital** (EUDI Wallet), punto de convergencia con la identidad basada en blockchain (tema 65).

**Casos de uso en la Administración**:

- **Identidad digital**: identidad autosoberana (*Self-Sovereign Identity*, SSI) con **credenciales verificables** (estándar del W3C): el ciudadano custodia sus credenciales y el verificador comprueba su autenticidad contra la cadena, sin consultar al emisor; converge con la EUDI Wallet.
- **Trazabilidad**: notarización de documentos y evidencias (huella con sellado de tiempo), seguimiento de ayudas y fondos, cadenas de suministro (alimentaria, farmacéutica).
- **Contratación pública**: registro inmutable de ofertas, aperturas y adjudicaciones para reforzar la integridad y la transparencia de las licitaciones.
- **Voto electrónico**: registro verificable y anónimo del voto; existen pilotos, pero persisten retos de secreto del sufragio y verificabilidad de extremo a extremo.
- **Educación**: emisión y verificación transfronteriza de títulos y diplomas, caso de uso insignia de EBSI; en España lo trabaja la red **Blue** (Blockchain de Universidades Españolas).

**Redes institucionales**:

- **Alastria** (2017): consorcio español sin ánimo de lucro, pionero mundial como red nacional permisionada multisectorial; red semipública sujeta a la regulación española, pensada para que sus socios desarrollen servicios con eficacia jurídica.
- **EBSI** (*European Blockchain Services Infrastructure*): infraestructura permisionada de la **European Blockchain Partnership** (Comisión Europea y Estados miembros, **2018**), con nodos distribuidos por los Estados y casos de uso de credenciales educativas, identidad y trazabilidad documental. Desde **mayo de 2024** su gobernanza se transfiere al consorcio **EUROPEUM-EDIC** (del que **España** es miembro) para llevarla a producción; el proyecto de expansión EBSI-NE, liderado por la **Agencia Estatal de Administración Digital**, amplió la red hasta **59 nodos**, y la infraestructura evoluciona hacia un libro mayor electrónico certificable como servicio de confianza cualificado conforme a eIDAS 2.
- **ISBE** (Infraestructura de Servicios Blockchain de España): iniciativa nacional de servicios blockchain, en despliegue desde **2025**.

## Realidad extendida y metaversos

La **realidad extendida** (*eXtended Reality*, XR) agrupa las tecnologías que combinan entorno físico y digital en distintos grados:

- **Realidad virtual (RV)**: inmersión completa en un entorno digital mediante visores; el usuario deja de ver el mundo real.
- **Realidad aumentada (RA)**: superpone información digital sobre el mundo real, a través del móvil o de gafas.
- **Realidad mixta (RM)**: los objetos digitales se anclan al entorno real e interactúan con él.
- **Dispositivos y estándares**: visores autónomos (Meta Quest, Apple Vision Pro, lanzado en **2024**) y el estándar abierto **OpenXR** (Khronos Group) para la interoperabilidad entre aplicaciones y dispositivos.

El **metaverso** designa la evolución hacia espacios virtuales tridimensionales, persistentes e interoperables donde los usuarios interactúan mediante avatares; combina XR con blockchain (activos digitales, NFT) y con los **gemelos digitales**, réplicas virtuales de objetos o sistemas reales sincronizadas con sus datos (los gemelos urbanos se tratan en el tema 78).

- **Marco europeo**: la Comisión adoptó en **julio de 2023** su estrategia sobre **Web 4.0 y mundos virtuales** (COM(2023) 442), para orientar esta transición conforme a los valores y derechos de la UE.
- **Aplicaciones en el sector público**: formación inmersiva (sanitaria, emergencias, seguridad), planificación urbana participativa sobre gemelos digitales, atención ciudadana en entornos virtuales, turismo y patrimonio cultural.
- **Perspectiva**: tras el pico de expectativas de 2021-2022, el foco de la industria se desplazó hacia la IA generativa; la XR avanza de forma más gradual, ligada a casos de uso concretos.

## Fuentes {.unnumbered .unlisted}

- Nakamoto, S.: *Bitcoin: A Peer-to-Peer Electronic Cash System*, 2008.
- Reglamento (UE) 2023/1114 (MiCA, DOUE 9 de junio de 2023; aplicable en su totalidad desde el 30 de diciembre de 2024); Reglamento (UE) 2022/858 (régimen piloto DLT); Reglamento (UE) 2024/1183 (eIDAS 2, DOUE 30 de abril de 2024).
- Comisión Europea: EBSI y EUROPEUM-EDIC (digital-strategy.ec.europa.eu y Digital Building Blocks), consultado en julio de 2026.
- Comunicación de la Comisión «Una iniciativa de la UE sobre la Web 4.0 y los mundos virtuales», COM(2023) 442, 11 de julio de 2023.
- Documentación de Ethereum (ethereum.org) y de Alastria (alastria.io), consultada en julio de 2026.
