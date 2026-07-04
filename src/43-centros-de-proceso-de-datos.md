# Centros de proceso de datos

## Diseño de un Centro de Procesamiento de Datos (CPD)

El Centro de Procesamiento de Datos (CPD) o Centro de Datos Corporativo (CDC) es el lugar donde se concentran todos los recursos necesarios para el almacenamiento, procesamiento y transmisión de la información de una organización. Su principal objetivo es garantizar la continuidad y disponibilidad de los servicios, asegurando que los sistemas críticos estén siempre operativos.

Las **características básicas** que debe tener un centro de datos son:

- **Robustez**: Capacidad para resistir fallos y mantener la operatividad bajo condiciones adversas.
- **Modularidad**: Diseño que permite añadir o retirar componentes sin afectar al funcionamiento general.
- **Flexibilidad**: Adaptabilidad a cambios tecnológicos y a las necesidades del negocio.
- **Estandarización**: Uso de estándares para facilitar la interoperabilidad y el mantenimiento.

La **evolución** de los centros de datos ha seguido varias etapas:

- **Mainframes**: Sistemas centralizados de gran capacidad.
- **Grid Computing**: Computación distribuida en múltiples nodos interconectados.
- **Clusters**: Conjuntos de servidores que trabajan como una sola unidad lógica.
- **Cloud Computing**: Servicios en la nube que ofrecen Infraestructura (IaaS), Plataforma (PaaS) y Software (SaaS) como servicio.

### Arquitectura: Diseño Físico y Lógico

El diseño de un centro de datos se basa en dos aspectos fundamentales:

**Diseño Físico**:

- **Ubicación**: Selección del emplazamiento considerando factores como riesgo de catástrofes (incendios, inundaciones, terremotos, sabotajes), disponibilidad de la red eléctrica, redes de telecomunicaciones y facilidad de acceso.
- **Infraestructura y Equipamiento**: Construcción que cumple con normativas como el Código Técnico de la Edificación (CTE), reglamentos electrotécnicos y ordenanzas municipales. Se deben definir las medidas de protección frente a fuego, agua, polvo e intrusiones.
- **Exterior del CPD**: Es recomendable que el edificio no sea fácilmente identificable como un centro de datos para evitar riesgos de robos o sabotajes. Colocar todo en una sola planta puede reducir costes y facilitar el mantenimiento.
- **Interior del CPD**: Implementación de suelos técnicos o falsos suelos para alojar cableado, facilitar el acceso y mejorar la refrigeración. Se puede considerar un edificio inteligente que incluya domótica, control de accesos y automatización.

**Diseño Lógico**:

- **Conexión y Organización de Sistemas**: Planificación de cómo se conectan y organizan los sistemas y servicios dentro del centro de datos, incluyendo servidores, almacenamiento y dispositivos de red.
- **Topologías de Cableado**: Modelos de jerarquía de cableado como "Top of the Rack" (ToR), donde los switches se colocan en la parte superior de cada rack, y "End of the Row" (EoR), donde los switches se ubican al final de una fila de racks.

### La Red del Core del Centro y la Seguridad

La red del núcleo o "core" es el corazón del centro de datos, responsable de la interconexión eficiente y segura de todos los sistemas.

**Características de la Red del Core**:

- **Seguridad**: Implementación de medidas de protección para garantizar la confidencialidad, integridad y disponibilidad de la información.
- **Rendimiento**: Alta capacidad de procesamiento y transmisión de datos para satisfacer las necesidades operativas.
- **Disponibilidad**: Redundancia de componentes y enlaces para evitar puntos únicos de fallo.
- **Eficiencia Energética**: Optimización del consumo de energía para reducir costes y minimizar el impacto ambiental.

**Seguridad en el Centro de Datos**:

- **Medidas de Seguridad Física**: Control de accesos mediante cerraduras, sistemas automatizados que registran y permiten el acceso solo a personal autorizado, videovigilancia (CCTV) y racks con cerraduras de llave o sistemas de lector de tarjetas.
- **Esquema Nacional de Seguridad (ENS)**: Marco normativo que establece los principios básicos y requisitos mínimos para garantizar la protección adecuada de la información.

**Principios Básicos del ENS**:

- **Seguridad Integral**
- **Gestión de Riesgos**
- **Prevención, Detección, Respuesta y Conservación**
- **Líneas de Defensa**
- **Vigilancia Continua**
- **Reevaluación Periódica**
- **Función Diferenciada**

**Dimensiones de Seguridad (DICTA)**:

- **Disponibilidad**: Asegurar que los sistemas y datos estén accesibles cuando se necesiten.
- **Integridad**: Garantizar la exactitud y completitud de la información.
- **Confidencialidad**: Proteger la información contra accesos no autorizados.
- **Trazabilidad**: Registrar las acciones realizadas para permitir auditorías y seguimiento.
- **Autenticidad**: Verificar la identidad de usuarios y sistemas.

Cada dimensión de seguridad se evalúa en niveles: Bajo, Medio y Alto, lo que permite determinar el impacto de un incidente y la categoría de los sistemas.

**Medidas de Protección**:

- **Áreas Separadas y Control de Acceso**: Separación física de zonas y control estricto de acceso.
- **Identificación de Personas**: Registro y verificación de identidad de todos los individuos que acceden a las instalaciones.
- **Acondicionamiento de Locales**: Control de temperatura, humedad, protección frente a amenazas identificadas en el análisis de riesgos.
- **Energía Eléctrica**: Garantizar el suministro eléctrico continuo mediante sistemas de alimentación ininterrumpida (SAI) y generadores.
- **Protección contra Incendios e Inundaciones**: Instalación de sistemas de detección y extinción de incendios, y medidas para prevenir daños por agua.
- **Registro de Entrada y Salida de Equipamiento**: Control detallado del movimiento de equipos y materiales.
- **Instalaciones Alternativas**: Planes de contingencia que incluyan ubicaciones secundarias con las mismas garantías de seguridad.

### Instalaciones y Equipamiento del CPD

### Instalaciones de Energía

**1. Sistemas de Alimentación Ininterrumpida (SAI)**:

Protegen frente a:

- **Cortes de Electricidad**: Proporcionan energía temporal durante interrupciones.
- **Fluctuaciones de Tensión**: Protegen contra sobretensiones (picos) e infratensiones.
- **Ruidos y Transientes**: Filtran interferencias eléctricas.

**Tipos de SAI**:

- **Standby**: Protección básica para pequeñas cargas.
- **De Línea Interactiva**: Protección intermedia, corrigen fluctuaciones menores.
- **On-line de Doble Conversión**: Protección total, aíslan completamente la carga de la red eléctrica.

**2. Generadores**:

- **Extensión de Autonomía**: Permiten prolongar el suministro eléctrico durante cortes prolongados.
- **Tipos**: Funcionan con gasóleo, gas natural, entre otros combustibles.

**Protección contra Incendios**:

**1. Detección de Incendios**:

- **Detectores**: Iónicos, ópticos, termovelocimétricos y de detección precoz por aspiración.
- **Sistema de Alarma**: Central de señalización y pulsadores manuales.
- **Sistemas Auxiliares**: Acciones automáticas como cierre de compuertas y desconexión de sistemas.

**2. Extinción de Incendios**:

- **Agentes Extintores**:
    - **Gases**: Recomendados para centros de datos.
        - **Tipos**:
            - **Halón**: Prohibido por dañar la capa de ozono.
            - **Novec 1230**: Poco eficiente.
            - **CO₂**: Asfixiante para humanos.
            - **Halocarburos**: Sustitutos del Halón.
            - **Inertes**: Combinaciones de gases nobles.
    - **Agua Nebulizada**: Utiliza agua pulverizada para reducir el calor.

**Componentes para Generar Fuego**:

- **Combustible**
- **Oxígeno**
- **Calor**
- **Reacción en Cadena**

**Racks y Cableado**:

- **Racks**: Estructuras modulares que alojan equipos TIC. Constan de estructura, puertas, paneles laterales, regletas, techo, suelo, cerraduras, pasahilos, bandejas y guías.
- **Dimensiones Estandarizadas**:
    - **Ancho Interior**: 19 pulgadas (482.6 mm).
    - **Unidad Rack (U)**: Altura de 1,75 pulgadas (4,445 cm).

**Modelos de Jerarquía de Cableado**:

- **Top of the Rack (ToR)**: Switches colocados en la parte superior de cada rack, reduciendo la longitud de cables.
- **End of the Row (EoR)**: Switches ubicados al final de una fila de racks, centralizando la gestión.

**Sistemas Informáticos del CPD**:

- **Servidores**:
    - **Formato Torre**: Similar a un PC convencional, buena refrigeración pero ocupan más espacio.
    - **Formato Rack**: Diseñados para ser montados en racks, ahorran espacio pero tienen ventilación limitada.
    - **Blade**: Servidores modulares que optimizan el espacio y la eficiencia energética, aunque son más costosos.
- **Almacenamiento**:
    - **NAS (Network Attached Storage)**: Dispositivos de almacenamiento conectados a la red que proporcionan acceso a datos a nivel de archivo.
    - **SAN (Storage Area Network)**: Redes de alta velocidad que conectan servidores y dispositivos de almacenamiento a nivel de bloque.
- **Dispositivos de Red**:
    - **Hubs**: Dispositivos básicos que conectan múltiples ordenadores en una red local, replicando los datos a todos los puertos.
    - **Switches**: Conmutadores que envían datos directamente al dispositivo de destino, mejorando la eficiencia y seguridad.
    - **Routers**: Encaminadores que reenvían paquetes entre diferentes redes, incluyendo funciones de hub y switch, además de servicios adicionales como firewall, NAT y DNS.

### Disponibilidad del CPD y Niveles TIER

El **Uptime Institute** establece clasificaciones de disponibilidad conocidas como **TIERS**, según los estándares **TIA-942**. Estos niveles definen la infraestructura necesaria y la tolerancia a fallos del centro de datos.

**Resumen de Niveles TIER**: *(Regla 6-7-8-9)*

- **TIER I (Básico)**:
    - **Redundancia**: No tiene redundancia en componentes críticos.
    - **Disponibilidad Máxima**: 99.671% (máximo 28.82 horas de inactividad al año).
    - **Características**: Puede tener interrupciones planificadas o no planificadas. No suele tener suelo técnico, SAI ni generador eléctrico.
- **TIER II (Componentes Redundantes)**:
    - **Redundancia**: N+1 en componentes críticos.
    - **Disponibilidad Máxima**: 99.741% (máximo 22.68 horas de inactividad al año).
    - **Características**: Dispone de suelo técnico, SAI y generadores eléctricos, pero con una sola línea de distribución eléctrica.
- **TIER III (Mantenimiento Concurrente)**:
    - **Redundancia**: N+1 con doble línea de distribución (una activa y otra inactiva).
    - **Disponibilidad Máxima**: 99.982% (máximo 1.57 horas de inactividad al año).
    - **Características**: Permite realizar mantenimiento sin interrumpir el servicio. La carga máxima en situaciones críticas es del 90%.
- **TIER IV (Tolerante a Fallos)**:
    - **Redundancia**: 2N+1 con dos líneas de distribución activas simultáneamente.
    - **Disponibilidad Máxima**: 99.995% (máximo 26.28 minutos de inactividad al año).
    - **Características**: Tolerante a fallos y permite cualquier tipo de actividad (planificada o no) sin interrupciones.

**Tabla Resumen**:

| Parámetros                         |    TIER I     |           TIER II           |           TIER III            |           TIER IV           |
| ---------------------------------- | :-----------: | :-------------------------: | :---------------------------: | :-------------------------: |
| Nombre                             |  **Básico**   | **Componentes redundantes** | **Mantenimiento concurrente** |   **Tolerante a fallos**    |
| Redundancia a nivel de componentes |     **N**     |          **N + 1**          |           **N + 1**           |         **2N + 1**          |
| Líneas de distribución             |     **1**     |            **1**            |   **1 activa + 1 inactiva**   | **2 activas (simultáneas)** |
| Disponibilidad                     |  **99.671%**  |         **99.749%**         |          **99.982%**          |         **99.995%**         |
| Downtime                           | **28.82h/yr** |        **22.68h/yr**        |         **1.57h/yr**          |       **26.28min/yr**       |
| Mantenimiento concurrente          |    **No**     |           **No**            |            **Sí**             |           **Sí**            |
| Compartimentación                  |    **No**     |           **No**            |            **No**             |           **Sí**            |
| Refrigeración continua             |    **No**     |           **No**            |            **No**             |           **Sí**            |
| Personal                           |    **No**     |         **1 Shift**         |         **1 + Shift**         |      **24 * 7 * 365**       |
| Meses de implementación            |     **3**     |           **3-6**           |           **15-20**           |          **15-20**          |

**\*Compartimentación:** Aislamiento de los sistemas complementarios y las redes de distribución

### Requisitos y Evaluación del CPD

Los requisitos del centro de datos se determinan en función de la criticidad de los servicios que soporta, mediante evaluaciones cuantitativas y cualitativas.

**Aspectos Clave**:

- **Disponibilidad 24/7x365**: Operatividad continua.
- **Fiabilidad**: Objetivo de alcanzar una disponibilidad de "cinco nueves" (99.999%).
- **Seguridad**: Protección integral de datos y sistemas.
- **Redundancia y Diversificación**: Evitar puntos únicos de fallo.
- **Control Ambiental y Prevención de Incendios**: Sistemas de climatización y detección/extinción de incendios.
- **Conectividad**: Acceso a Internet y redes WAN.
- **Flexibilidad**: Rápido despliegue y reconfiguración.
- **Gestión Continua del Negocio**: Planes de contingencia y recuperación.
- **Cableado**: Infraestructura robusta y de altas prestaciones.

Es esencial realizar **auditorías periódicas** para evaluar el estado del centro de datos y garantizar el cumplimiento de los requisitos establecidos.

### Climatización del CPD

La climatización es fundamental para mantener las condiciones ambientales óptimas que aseguren el correcto funcionamiento de los equipos.

**Variables a Controlar**:

- **Humedad**: Mantener un nivel de 45% ±5%. Humedad excesiva puede causar condensación; niveles bajos pueden generar electricidad estática.
- **Polvo**: Uso de filtros y mantenimiento de presión positiva para evitar la entrada de polvo, que dificulta la disipación de calor.

**Tecnologías de Refrigeración**:

- **Expansión Directa**: Con condensación por aire o agua/glicol.
- **Condensación por Torre de Refrigeración**: Utiliza agua para disipar el calor.
- **Unidad Enfriadora de Agua**: Enfriamiento mediante circulación de agua fría.
- **Free-Cooling**: Aprovecha las bajas temperaturas del exterior para refrigerar.

**Distribución del Aire**:

- **Insuflación por el Suelo**: El aire frío se suministra desde el suelo hacia los equipos.
- **Insuflación Superior**: El aire frío se suministra desde arriba de los equipos.
- **Sistema Displacement**: Aprovecha la convección natural de abajo hacia arriba.
- **Rejillas Frontales**: Aire frío suministrado directamente al frontal de los racks.

**Notas sobre Climatización**:

- El sistema de aire acondicionado del CPD debe ser independiente del resto del edificio.
- Es crucial crear una barrera física entre el pasillo frío y el pasillo caliente para optimizar la eficiencia.
- **Técnica de Pasillo Frío/Caliente**: Los racks se disponen de manera que las entradas de aire frío y las salidas de aire caliente estén alineadas en pasillos separados.

## Centro de Datos Definido por Software (SDDC)

El SDDC es una arquitectura de centro de datos donde todos los elementos de infraestructura (redes, almacenamiento, CPU y seguridad) están virtualizados y entregados como un servicio. La gestión del centro de datos está totalmente automatizada por software, permitiendo una mayor eficiencia y agilidad.

### Características del SDDC

- **Virtualización Completa**: Todos los recursos están abstraídos del hardware físico.
- **Automatización y Orquestación**: Procesos automatizados para aprovisionamiento y gestión de recursos.
- **Infraestructura como Código**: La configuración y gestión se realizan mediante scripts y herramientas de automatización.
- **Seguridad Integrada**: Políticas de seguridad aplicadas de forma consistente en todo el entorno virtualizado.

### Ventajas y Desafíos del SDDC

- **Ventajas**:
    - Agilidad en la provisión de recursos.
    - Reducción de costos operativos.
    - Escalabilidad y flexibilidad mejoradas.
- **Desafíos**:
    - Complejidad en la implementación inicial.
    - Necesidad de personal con habilidades especializadas.
    - Consideraciones de seguridad y cumplimiento normativo.


## Infraestructura Convergente e Hiperconvergente

**Infraestructura Convergente (CI)**:

- Combina servidores, almacenamiento y redes en una solución integrada.
- Gestionada como una unidad única, simplificando la administración.

**Infraestructura Hiperconvergente (HCI)**:

- Evolución de la CI, definida por software.
- Virtualiza todos los componentes, incluyendo computación, almacenamiento y redes.
- **Ventajas**:
    - Simplificación y unificación de la gestión.
    - Mejora la eficiencia y reduce costes.
    - Mayor escalabilidad y flexibilidad.
- **Desventajas**:
    - Dependencia de soluciones específicas de hardware y software.
    - Posibles desafíos en la integración y migración de aplicaciones.

## Tendencias en Infraestructuras y Operaciones (I&O)

### Infrastructure and Operations (I&O):

Se refiere a la **gestión y mantenimiento de la infraestructura tecnológica** de una organización, abarcando hardware, software y servicios de red. La evolución en esta área busca garantizar que las organizaciones sean más ágiles, eficientes y resilientes frente a los cambios tecnológicos.

### Serverless computing:

Este modelo elimina la necesidad de que los usuarios gestionen directamente la infraestructura subyacente. **El proveedor de servicios asume la asignación y gestión de los recursos informáticos**, permitiendo que las aplicaciones y servicios se ejecuten sin preocuparse por detalles como el aprovisionamiento de servidores. Esto simplifica el desarrollo y reduce los costes operativos.

### FPaaS (Function Platform as a Service):

Se trata de un modelo que permite ejecutar código encapsulado en funciones individuales. Los usuarios no necesitan aprovisionar ni gestionar explícitamente la infraestructura, lo que **facilita la escalabilidad automática y la ejecución eficiente de funciones en respuesta a eventos específicos**.

### Network agility:

Es la capacidad de una red para adaptarse de manera rápida y eficiente a los **cambios en el entorno o a las necesidades del usuario**. Una red ágil es clave para soportar cargas de trabajo dinámicas, optimizar el rendimiento y mejorar la experiencia del usuario final.

### Death of the data center:

La tendencia hacia la **descentralización de la informática** y el uso de la computación en la nube está transformando la manera en que las organizaciones gestionan sus datos. Esto podría conducir a una reducción significativa en el uso de centros de datos físicos tradicionales, favoreciendo entornos híbridos o completamente basados en la nube.

### Edge computing (Computación frontera):

Este paradigma lleva el **procesamiento y almacenamiento de datos cerca de donde se generan** o necesitan, en lugar de depender exclusivamente de centros de datos centralizados. Esto mejora los tiempos de respuesta, **reduce la latencia** y optimiza el uso del ancho de banda, siendo especialmente útil en aplicaciones de IoT y análisis en tiempo real.

### Digital diversity management:

La **gestión de la diversidad tecnológica** es esencial para integrar múltiples plataformas, dispositivos y tecnologías en una organización. Este enfoque maximiza el potencial de las herramientas disponibles y asegura la interoperabilidad entre los diferentes sistemas.

### Nuevos roles dentro de I&O:

La evolución tecnológica está generando nuevos desafíos y oportunidades en el área de infraestructura y operaciones. Esto se traduce en la aparición de **nuevos roles y responsabilidades** que se centran en áreas como la automatización, la inteligencia artificial, la ciberseguridad y la integración de tecnologías emergentes.

### Negación SaaS:

Algunas organizaciones optan por rechazar el uso de **software como servicio (SaaS)** debido a preocupaciones relacionadas con la seguridad, la privacidad o una preferencia por modelos de implementación más controlados. Esta postura puede estar influenciada por la sensibilidad de los datos o por políticas corporativas específicas.

## Tendencias: Impacto Ambiental, Escalabilidad, Automatización y Gestión Remota

Los centros de datos modernos se enfrentan a desafíos y tendencias que influyen en su diseño y operación.

**Impacto Ambiental**:

- **Eficiencia Energética**: Implementación de sistemas de climatización eficientes, uso de iluminación LED y equipos de bajo consumo.
- **Energías Renovables**: Integración de fuentes de energía limpias como solar o eólica.
- **Gestión de Residuos**: Políticas de reciclaje y disposición adecuada de equipos obsoletos.

**Escalabilidad**:

- **Infraestructura Convergente (CI)**: Combina servidores, almacenamiento y redes en soluciones integradas gestionadas como un todo. Facilita la expansión y mejora la eficiencia.
- **Infraestructura Hiperconvergente (HCI)**: Virtualiza todos los elementos de los sistemas convencionales definidos por hardware. Incluye computación virtualizada, almacenamiento y redes definidos por software.

**Características de la HCI**:

- **Simplificación de la Gestión**: Administración unificada de recursos.
- **Escalabilidad Flexible**: Capacidad para crecer según las necesidades.
- **Ventajas**: Reduce costes, mejora la eficiencia, aumenta la agilidad y la seguridad.
- **Desventajas**: Dependencia de hardware y software específicos, posible dificultad para integrar aplicaciones o migrar a otros sistemas.

**Automatización y Gestión Remota**:

- **Centro de Datos Definido por Software (SDDC)**: Arquitectura en la que todos los componentes se gestionan y controlan mediante software. Permite una mayor flexibilidad y agilidad en la gestión de recursos.
- **Orquestación y Automatización**: Uso de herramientas que permiten automatizar despliegues, configuraciones y operaciones de mantenimiento.
- **Gestión Remota Segura**: Implementación de protocolos seguros para acceder y administrar el centro de datos desde ubicaciones remotas.

## Caso práctico: diseño de un CPD

### Caso Práctico 1: Medidas de Seguridad Física

- **Control de Accesos**:
    - Las puertas deben contar con cerraduras y sistemas automatizados que registren y permitan el acceso solo a personal autorizado.
    - El sistema de seguridad debe mantener una lista de autorizaciones y registrar entradas y salidas, incluyendo fechas y horas.
- **Prevención de Atrapamientos**:
    - Instalación de mecanismos de seguridad que eviten que alguien quede atrapado en las instalaciones.
- **Protección de Equipos**:
    - Los servidores deben estar protegidos con rejas o en zonas restringidas (zonificación).
    - Los racks deben contar con cerraduras, ya sea de llave o con sistemas de lector de tarjetas.
- **Videovigilancia**:
    - Implementación de un sistema de circuito cerrado de televisión (CCTV) para monitorear las instalaciones en tiempo real.
- **Normativas y Protocolos**:
    - Establecimiento de un conjunto de normas y estándares de operación que guíen a los usuarios y personal en las mejores prácticas de seguridad.

### Caso Práctico 2: Medidas de Protección según el ENS

- **Áreas Separadas y Control de Acceso**:
    - El equipamiento debe instalarse en áreas separadas con control de acceso estricto.
    - Se debe identificar a todas las personas que acceden a locales con equipamiento, registrando sus entradas y salidas.
- **Acondicionamiento de Locales**:
    - Los locales deben estar acondicionados con sistemas de control de temperatura y humedad.
    - Protección frente a amenazas identificadas en el análisis de riesgos, incluyendo protección de cableado.
- **Suministro Eléctrico**:
    - Garantizar el suministro de energía eléctrica y el correcto funcionamiento de luces de emergencia.
    - **Nivel Medio**: En caso de fallo del suministro, se debe garantizar energía suficiente para la terminación ordenada de procesos mediante SAIs.
- **Protección contra Incendios e Inundaciones**:
    - Aplicar la normativa industrial pertinente para proteger los locales frente a incendios.
    - Implementar medidas para proteger los locales frente a incidentes causados por el agua.
- **Registro de Equipamiento**:
    - Realizar un registro detallado de toda entrada y salida de equipamiento, incluyendo la identificación de la persona que autoriza el movimiento.
- **Instalaciones Alternativas**:
    - Garantizar la existencia y disponibilidad de instalaciones alternativas en caso de que las habituales no estén disponibles, manteniendo las mismas garantías de seguridad.
