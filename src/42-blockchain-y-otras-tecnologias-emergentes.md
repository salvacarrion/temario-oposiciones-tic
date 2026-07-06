# Blockchain y otras tecnologías emergentes

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Tecnología blockchain, funcionamiento, tipos, estructura y aplicaciones

**Tecnología que permite la creación de una base de datos distribuida y descentralizada** de forma segura. Su funcionamiento se basa en bloques de información que están encadenados entre sí, proporcionando una mayor **seguridad, transparencia y confiabilidad** en las transacciones que se realizan.

De manera más técnica, **blockchain** se define como un **libro mayor compartido e inalterable** que facilita el registro y seguimiento de transacciones, así como de activos dentro de una red de negocio. Este sistema es crucial para garantizar la confianza en redes distribuidas.

### Elementos principales de Blockchain

- **Tecnología de libro mayor distribuido**: Todos los participantes de la red tienen acceso a una copia del libro mayor, que contiene un registro inalterable de todas las transacciones. Este enfoque asegura que todos los nodos de la red posean la misma información y evita manipulaciones.
- **Registros inalterables**: Una vez que una transacción se graba en el libro mayor, no puede ser alterada ni eliminada. Si se comete un error en una transacción, en lugar de modificarla, se añade una nueva transacción para corregir el error. Ambas transacciones permanecen visibles, lo que incrementa la **transparencia**.
- **Contratos inteligentes**: Son conjuntos de reglas almacenadas dentro de la blockchain que se ejecutan automáticamente cuando se cumplen ciertas condiciones. Los contratos inteligentes aceleran las transacciones al eliminar intermediarios y permitir procesos más eficientes.

### Funcionamiento de Blockchain

El proceso de blockchain puede describirse como una serie de pasos encadenados:

- Cada transacción que se realiza se registra como un **bloque de datos**.
- Cada bloque está enlazado al bloque anterior y al posterior, formando una cadena continua de datos.
- Esta cadena es **irreversible**, lo que refuerza la confianza y la seguridad de la red. A medida que se añaden bloques, la información almacenada se vuelve más robusta contra alteraciones.

### Beneficios de Blockchain

Blockchain ofrece tres beneficios fundamentales:

- **Mayor confianza**: Los participantes de la red pueden estar seguros de que la información es precisa y no ha sido manipulada.
- **Mayor seguridad**: Gracias a los registros inalterables y la criptografía, las transacciones están protegidas frente a accesos no autorizados.
- **Mayor eficiencia**: Al eliminar intermediarios y optimizar procesos mediante contratos inteligentes, se reducen tiempos y costos.

### Tipos de redes blockchain

- **Redes públicas**: Estas redes están abiertas a cualquier persona que quiera participar. En este tipo de redes, la validación de transacciones es realizada por cualquier nodo de la red, lo que fomenta la descentralización.
    - **Desventajas**:
        - Requieren una **gran potencia computacional** debido al proceso de consenso distribuido, como el mecanismo de prueba de trabajo (PoW).
        - Las transacciones tienen **poca privacidad**, ya que toda la información es visible para los nodos participantes.
        - La seguridad puede ser débil si no hay suficiente participación o si un atacante controla una gran parte de la red.
- **Redes privadas**: Están restringidas a un grupo reducido de participantes, quienes tienen permiso para acceder y validar las transacciones. Funcionan como una red **P2P descentralizada**, pero con acceso limitado.
    - **Desventajas**:
        - Una sola organización administra la red, lo que significa que la descentralización está limitada.
        - Existe un **riesgo de centralización del poder**, lo que puede generar problemas de confianza si los administradores no son imparciales.
- **Redes híbridas**: Combinan las características de las redes públicas y privadas. Permiten una **validación flexible** que puede ser tanto abierta como restringida según las necesidades de la red.
    - Este enfoque híbrido es especialmente útil para organizaciones que necesitan mantener ciertos datos privados mientras comparten otros de forma pública para incrementar la transparencia.

### Estructura de datos en Blockchain

- **Árboles de Merkle**: Son estructuras de datos jerárquicas que permiten organizar y verificar grandes cantidades de información de manera eficiente. Los árboles de Merkle funcionan de la siguiente manera:
    - Las transacciones individuales se representan como **nodos hoja** en el árbol.
    - Cada nodo hoja se codifica con un hash único (una función criptográfica que comprime los datos de la transacción en una secuencia fija de caracteres).
    - Los hashes de los nodos hoja se agrupan en pares y se combinan en un nuevo hash, formando los **nodos intermedios**.
    - Este proceso de combinación continúa hasta que se llega a un único hash final en la raíz, llamado **raíz de Merkle**.
        - Permite verificar la integridad de las transacciones de forma rápida, ya que solo es necesario comparar los hashes relacionados, sin tener que revisar cada transacción individual. Esta eficiencia es especialmente valiosa en redes con gran volumen de datos.
- **Cadena de bloques**: Cada bloque en la blockchain contiene tres componentes principales:
    - **Datos de las transacciones**: Información específica de las transacciones que se registran en ese bloque.
    - **Hash del bloque actual**: Un identificador único que representa todo el contenido del bloque, generado mediante funciones criptográficas.
    - **Hash del bloque anterior**: Vincula el bloque actual con el anterior, creando la continuidad de la cadena. Este enlace garantiza que cualquier cambio en un bloque afectará a todos los bloques posteriores, reforzando la inmutabilidad de la cadena.
- **Funciones hash criptográficas**: Son esenciales en blockchain, ya que permiten:
    - Resumir grandes cantidades de datos en un hash único y fijo.
    - Detectar cualquier alteración en los datos, ya que incluso un pequeño cambio genera un hash completamente diferente.
    - Garantizar la integridad de los datos y la confianza entre participantes.

### Aplicabilidad del Blockchain

La **tecnología blockchain** es una herramienta innovadora que permite gestionar y registrar información de manera segura, inmutable y descentralizada, eliminando la necesidad de intermediarios y fortaleciendo la confianza en los sistemas. Se aplica en una amplia gama de áreas, entre las que destacan:

- **Validación de transacciones financieras**: Blockchain garantiza la integridad, trazabilidad y transparencia en las operaciones financieras, reduciendo riesgos de fraude.
- **Registro de propiedad**: Facilita la inscripción segura de bienes y derechos, evitando conflictos y aumentando la transparencia.
- **Identificación digital**: Proporciona sistemas más seguros para verificar identidades, mejorando la protección contra el robo de datos y el fraude de identidad.
- **Gestión de contratos inteligentes**: Automatiza el cumplimiento de acuerdos mediante **smart contracts**, que se ejecutan automáticamente al cumplirse las condiciones establecidas.
- **Trazabilidad en cadenas de suministro**: Permite rastrear el origen y movimiento de bienes, asegurando calidad, autenticidad y cumplimiento normativo.

## Organizaciones descentralizadas (OD)

Las **organizaciones descentralizadas (OD)** constituyen un modelo de gobernanza donde no existe una autoridad central. Las decisiones son tomadas de forma colectiva mediante **procesos de consenso**, lo que fomenta una participación democrática y la transparencia en todas las operaciones. Estas organizaciones se estructuran en torno a principios como la igualdad, la descentralización y la autogestión, siendo ideales para comunidades con intereses compartidos.

### DAO (Decentralized Autonomous Organization)

Una **DAO (Organización Autónoma Descentralizada)** es una forma avanzada de organización descentralizada basada en reglas codificadas en **contratos inteligentes** que operan sobre blockchain. Las DAOs destacan por:

- **Autonomía**: Funcionan automáticamente según las reglas preestablecidas, sin intervención humana directa.
- **Transparencia**: Toda la actividad es visible y verificable en el blockchain.
- **Toma de decisiones colectiva**: Los miembros participan mediante votaciones digitales, asegurando que las decisiones reflejen los intereses del grupo.
- **Inmutabilidad**: Una vez establecidas, las reglas son difíciles de alterar, aumentando la confianza en el sistema.

### Gobernanza

La **gobernanza** en el contexto de las OD y DAOs se refiere a los procesos y normas que definen cómo se toman las decisiones dentro de estas estructuras descentralizadas. Existen dos principales enfoques:

- **Descentralizado**: Las decisiones son discutidas y acordadas colectivamente por los miembros, sin intermediarios.
- **Descentralizado y autónomo**: La gobernanza está totalmente automatizada mediante contratos inteligentes, lo que garantiza eficiencia y evita manipulaciones externas.\ Este modelo plantea ventajas significativas en términos de transparencia, pero también desafíos al integrar los intereses de todos los participantes de forma justa.

### Aspectos legales y fiscales sobre Blockchain

El uso de blockchain y la descentralización en OD y DAOs presentan retos complejos en el ámbito legal y fiscal:

- **Responsabilidad**: En estructuras descentralizadas, determinar quién es responsable de las acciones o transacciones puede ser complicado, lo que dificulta la aplicación de regulaciones tradicionales.
- **Jurisdicción**: Al operar en redes globales, es difícil identificar bajo qué leyes se rigen las actividades.
- **Implicaciones fiscales**: Las transacciones en blockchain, especialmente aquellas que usan criptomonedas, presentan desafíos para la fiscalización debido a su anonimato y la falta de intermediarios. Esto requiere nuevos enfoques legislativos.

### Blue (Blockchain Universidades Españolas)

La red **Blue**, impulsada por universidades españolas, tiene como objetivo principal promover la innovación y la formación en blockchain. Esta colaboración entre universidades y empresas busca:

- Potenciar la **colaboración en proyectos innovadores** relacionados con blockchain.
- Formar profesionales especializados en tecnología blockchain, adaptados a las demandas del mercado laboral.
- Desarrollar aplicaciones prácticas como la **verificación de identidad**, **gestión de diplomas académicos** y la **trazabilidad de documentos**.

### EBSI (European Blockchain Services Infrastructure)

La **EBSI**, promovida por la Comisión Europea, es una iniciativa clave para integrar la tecnología blockchain en sectores públicos y privados en la Unión Europea. Sus áreas de aplicación incluyen:

- **Verificación de identidad digital**: Ofrece soluciones seguras y confiables para la identificación y autenticación de ciudadanos.
- **Gestión de diplomas**: Facilita el intercambio transfronterizo de títulos académicos, garantizando su validez y autenticidad.
- **Seguridad social**: Mejora la eficiencia y transparencia en la gestión de servicios sociales mediante registros inmutables y trazables.
- **Trazabilidad documental**: Simplifica la gestión administrativa asegurando que los documentos sean auténticos y verificables.
- **Sostenibilidad**: Promueve el uso de blockchain para rastrear y garantizar prácticas sostenibles en distintos sectores.
