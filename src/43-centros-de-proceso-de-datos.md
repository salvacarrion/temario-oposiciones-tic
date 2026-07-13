# Centros de proceso de datos

El **Centro de Proceso de Datos (CPD)**, en inglés *data center*, es la instalación donde se concentran los recursos necesarios para el almacenamiento, procesamiento y transmisión de la información de una organización. Su objetivo principal es garantizar la **continuidad y disponibilidad** de los servicios, asegurando que los sistemas críticos estén siempre operativos.

## Diseño de un CPD: infraestructura física y lógica

El diseño de un CPD abarca desde la elección del emplazamiento hasta la organización lógica de los sistemas. Las características básicas que debe reunir son:

- **Robustez**: capacidad de resistir fallos y mantener la operatividad en condiciones adversas.
- **Modularidad**: añadir o retirar componentes sin afectar al funcionamiento general.
- **Flexibilidad**: adaptación a los cambios tecnológicos y a las necesidades del negocio.
- **Estandarización**: uso de estándares que facilitan la interoperabilidad y el mantenimiento.

La computación corporativa ha evolucionado desde los mainframes centralizados hacia la arquitectura cliente-servidor, los clústeres de servidores, el grid computing, la virtualización y consolidación de sistemas y, finalmente, la computación en la nube y los modelos híbridos, con el edge computing como última etapa descentralizadora (la nube y las altas prestaciones se desarrollan en el tema 47).

Los requisitos generales de un CPD son:

- **Disponibilidad continua (24x7)**: el objetivo clásico de fiabilidad son los «cinco nueves» (**99,999 %**).
- **Redundancia y diversificación**: evitar puntos únicos de fallo (SPOF) en energía, climatización, red y almacenamiento.
- **Seguridad**: protección física y lógica de datos y sistemas.
- **Conectividad**: acceso redundante a Internet y a las redes WAN, idealmente con más de un operador.
- **Escalabilidad y flexibilidad**: despliegue y reconfiguración rápidos.
- **Continuidad de negocio**: planes de contingencia y recuperación, con auditorías periódicas que evalúen el cumplimiento de los requisitos.

### Diseño físico

- **Ubicación**: emplazamientos con bajo riesgo de catástrofes (incendios, inundaciones, terremotos, sabotajes), buen suministro eléctrico, disponibilidad de redes de telecomunicaciones y facilidad de acceso.
- **Edificio**: cumplimiento del **Código Técnico de la Edificación (CTE)**, del reglamento electrotécnico y de las ordenanzas municipales; medidas de protección frente a fuego, agua, polvo e intrusiones. Es recomendable que el edificio no sea identificable como CPD (discreción frente a robos y sabotajes) y que la instalación ocupe una sola planta, lo que reduce costes y facilita el mantenimiento.
- **Interior**: **suelo técnico** (falso suelo) para alojar el cableado y distribuir el aire frío, altura libre suficiente y compartimentación en salas (sala TIC, energía, telecomunicaciones, operación). Puede plantearse como edificio inteligente, con domótica, control de accesos y automatización.

### Diseño lógico y red del CPD

El diseño lógico planifica cómo se conectan y organizan los servidores, el almacenamiento y la electrónica de red dentro del centro.

- **Topologías de cableado**:
    - **Top of the Rack (ToR)**: un switch en la parte superior de cada rack; acorta el cableado y facilita el crecimiento rack a rack.
    - **End of the Row (EoR)**: switches concentrados al final de cada fila de racks; centraliza la gestión a costa de más cableado horizontal.
- **Arquitectura de red**:
    - **Jerárquica de tres niveles**: núcleo (core), agregación o distribución, y acceso; es el modelo clásico, optimizado para el tráfico «norte-sur» (cliente-servidor).
    - **Spine-leaf** (topología Clos de dos niveles): cada switch de acceso (leaf) se conecta a todos los switches troncales (spine). Es el estándar actual del CPD porque ofrece latencia uniforme entre servidores, escalado horizontal y mejor soporte del tráfico «este-oeste» generado por la virtualización y los microservicios.
- **Requisitos de la red**: rendimiento (alta capacidad de conmutación), disponibilidad (equipos y enlaces redundantes, sin puntos únicos de fallo), seguridad (segmentación, cortafuegos perimetrales e internos) y eficiencia energética.

## Instalaciones y equipamiento

### Energía eléctrica

El suministro eléctrico es el sistema de soporte más crítico. Se diseña en cadena (acometida, cuadros, SAI, distribución a rack) con la redundancia acorde al nivel de disponibilidad buscado.

- **Sistemas de alimentación ininterrumpida (SAI)**: protegen frente a cortes de electricidad (suministro temporal desde baterías), fluctuaciones de tensión (sobretensiones e infratensiones) y ruido eléctrico (filtrado de interferencias). Tipos:
    - **Standby (offline)**: conmuta a batería al fallar la red; protección básica para cargas pequeñas.
    - **De línea interactiva**: corrige además las fluctuaciones menores mediante regulación automática de tensión.
    - **On-line de doble conversión**: aísla por completo la carga de la red (rectificador e inversor permanentes); es la protección total y la habitual en CPD.
- **Grupos electrógenos**: prolongan la autonomía durante cortes largos (gasóleo o gas natural); el SAI cubre el tiempo de arranque del grupo.
- **Redundancia**: se expresa respecto a la capacidad necesaria N: **N+1** (un componente de reserva), **2N** (sistema completo duplicado) y **2(N+1)** (duplicado con reserva en cada rama), idealmente con doble acometida y regletas (PDU) duales por rack.

### Protección contra incendios

- **Tetraedro del fuego**: combustible, comburente (oxígeno), energía de activación (calor) y reacción en cadena; la extinción actúa eliminando alguno de los cuatro.
- **Detección**: detectores iónicos, ópticos y termovelocimétricos, y sistemas de **detección precoz por aspiración** (muestreo continuo del aire); central de señalización, pulsadores manuales y acciones automáticas auxiliares (cierre de compuertas, parada de climatización).
- **Extinción**: en las salas TIC se prefieren los **agentes gaseosos «limpios»**, no conductores y sin residuo:
    - **Halón**: prohibido por dañar la capa de ozono.
    - **Halocarburos**: los sustitutos del halón, como el HFC-227ea (FM-200) o el FK-5-1-12 (comercializado como Novec 1230; 3M cesó su fabricación al abandonar los PFAS, aunque otros fabricantes siguen produciendo el agente genérico).
    - **Gases inertes**: nitrógeno y argón, solos o combinados (IG-100, IG-01, IG-55, IG-541); reducen la concentración de oxígeno y son inocuos para los equipos.
    - **CO₂**: eficaz, pero asfixiante para las personas (solo apto para espacios no ocupados).
    - **Agua nebulizada**: gotas finísimas que enfrían y desplazan el oxígeno; alternativa a los gases.

### Climatización

La climatización mantiene las condiciones ambientales dentro de los rangos de operación de los equipos y debe ser independiente de la del resto del edificio.

- **Temperatura**: rango recomendado por ASHRAE de **18 a 27 °C** medido en la entrada de aire de los equipos.
- **Humedad**: regla clásica del **45 % ± 5 %** de humedad relativa (el exceso provoca condensación; el defecto, electricidad estática); las guías ASHRAE actuales la controlan por punto de rocío (aproximadamente de -9 a 15 °C, con humedad relativa máxima del 60 %).
- **Polvo**: filtrado del aire y **sobrepresión** (presión positiva) para impedir su entrada, ya que dificulta la disipación de calor.
- **Tecnologías de refrigeración**: expansión directa (condensación por aire o por agua/glicol), agua enfriada, condensación por torre de refrigeración y **free-cooling** (aprovecha el aire o el agua exteriores fríos, con gran ahorro energético).
- **Distribución del aire**: insuflación por el suelo técnico, insuflación superior, sistemas por desplazamiento (convección natural de abajo arriba) y rejillas frontales al rack.
- **Pasillo frío / pasillo caliente**: los racks se enfrentan para alinear las tomas de aire frío y las expulsiones de aire caliente en pasillos separados; el **confinamiento** (barrera física) de uno de los pasillos evita la mezcla de aire y optimiza la eficiencia.

### Racks y equipamiento TIC

- **Racks**: armarios modulares normalizados que alojan el equipamiento, con ancho de **19 pulgadas** (482,6 mm) y altura medida en unidades rack (**1 U = 1,75 pulgadas = 44,45 mm**); incorporan puertas y paneles con cerradura, regletas de alimentación (PDU), pasahilos, bandejas y guías.
- **Servidores**: formato **torre** (autónomo, buena refrigeración pero ocupa más espacio), **rack** (optimiza el espacio) y **blade** (chasis compartido con alimentación y red comunes: máxima densidad y eficiencia energética, mayor coste).
- **Almacenamiento**: cabinas **NAS** (acceso a nivel de fichero a través de la red) y redes **SAN** (acceso a nivel de bloque por red dedicada); las arquitecturas de almacenamiento y RAID se desarrollan en el tema 45.
- **Electrónica de red**: switches de acceso, agregación y núcleo, routers de interconexión con el exterior, cortafuegos y balanceadores de carga.

## Seguridad física y el Esquema Nacional de Seguridad

La seguridad física combina medidas organizativas y de instalación: zonificación con áreas restringidas, control de accesos automatizado con registro de entradas y salidas (fecha y hora), videovigilancia (CCTV), racks cerrados con llave o lector de tarjeta y normas de operación para el personal y los visitantes.

En las administraciones públicas el marco de referencia es el **Esquema Nacional de Seguridad (RD 311/2022)**, cuyos principios, categorización y medidas generales se estudian en el tema 29. Al CPD le afecta directamente la familia **mp.if (protección de las instalaciones e infraestructuras)** del Anexo II:

| Medida | Contenido | Aplicación |
| --- | --- | --- |
| **mp.if.1** Áreas separadas y con control de acceso | El equipamiento del CPD se instala en áreas separadas específicas para su función y solo se accede por las entradas previstas | Todas las categorías |
| **mp.if.2** Identificación de las personas | El control de acceso identifica a quien accede a los locales con equipamiento esencial y registra entradas y salidas | Todas las categorías |
| **mp.if.3** Acondicionamiento de los locales | Condiciones de temperatura y humedad, protección frente a las amenazas del análisis de riesgos y protección del cableado | Todas las categorías |
| **mp.if.4** Energía eléctrica | Garantía del suministro y del funcionamiento de las luces de emergencia; refuerzo **R1** (suministro de emergencia para la terminación ordenada de los procesos) en los niveles medio y alto | Dimensión D |
| **mp.if.5** Protección frente a incendios | Protección al menos conforme a la normativa industrial de aplicación | Dimensión D |
| **mp.if.6** Protección frente a inundaciones | Protección frente a incidentes causados por el agua | Dimensión D (no aplica en nivel bajo) |
| **mp.if.7** Registro de entrada y salida de equipamiento | Registro pormenorizado de todo movimiento de equipamiento esencial, con la persona que lo autoriza | Todas las categorías |

Las «instalaciones alternativas» del ENS de 2010 ya no forman parte de mp.if: la disponibilidad de **medios alternativos** es hoy la medida **op.cont.4** (continuidad del servicio, exigible en el nivel alto).

## Disponibilidad y estándares: TIER, TIA-942 y EN 50600

Tres esquemas independientes clasifican la infraestructura de un CPD según su redundancia y tolerancia a fallos, y conviene no confundirlos: los **Tier** son la certificación propietaria del **Uptime Institute**; el estándar **ANSI/TIA-942** clasifica como **Rated 1 a 4** (retiró el término «tier» en 2014, precisamente a petición del Uptime Institute); y la serie europea **EN 50600** define **clases de disponibilidad 1 a 4**.

- **Uptime Institute (Tier Standard: Topology)**: cuatro niveles progresivos:
    - **Tier I (básico)**: sin redundancia; las paradas, planificadas o no, afectan al servicio. Suele carecer de suelo técnico, SAI y generador.
    - **Tier II (componentes redundantes)**: redundancia **N+1** en componentes críticos, con una única línea de distribución.
    - **Tier III (mantenimiento concurrente)**: componentes redundantes y **dos líneas de distribución (una activa)**; permite el mantenimiento sin interrumpir el servicio.
    - **Tier IV (tolerante a fallos)**: componentes duplicados y **dos líneas de distribución activas simultáneamente**; soporta cualquier fallo único sin interrupción.

| Parámetros | TIER I | TIER II | TIER III | TIER IV |
| --- | :---: | :---: | :---: | :---: |
| Nombre | **Básico** | **Componentes redundantes** | **Mantenimiento concurrente** | **Tolerante a fallos** |
| Redundancia de componentes | **N** | **N + 1** | **N + 1** | **2N o 2(N+1)** |
| Líneas de distribución | **1** | **1** | **1 activa + 1 inactiva** | **2 activas (simultáneas)** |
| Disponibilidad | **99,671 %** | **99,741 %** | **99,982 %** | **99,995 %** |
| Parada anual máxima | **28,82 h** | **22,68 h** | **1,57 h** | **26,28 min** |
| Mantenimiento concurrente | No | No | **Sí** | **Sí** |
| Compartimentación | No | No | No | **Sí** |
| Refrigeración continua | No | No | No | **Sí** |

Los porcentajes siguen la regla mnemotécnica «**6-7-8-9**» (99,**6** / 99,**7** / 99,9**8** / 99,99**5**) y son los valores orientativos clásicos de la industria. La compartimentación es el aislamiento físico de los sistemas complementarios y de las redes de distribución.

- **ANSI/TIA-942-C** (TIA, **mayo de 2024**): estándar de infraestructura de telecomunicaciones para centros de datos. Especifica requisitos en **cuatro subsistemas** (telecomunicaciones, arquitectura, eléctrico y mecánico) y clasifica las instalaciones como **Rated 1 a 4**, conceptualmente equivalentes a los Tier (básico, componentes redundantes, mantenimiento concurrente y tolerante a fallos). La revisión C incorpora los CPD de borde (edge) y adopta las guías térmicas de ASHRAE.
- **Serie EN 50600 (CENELEC) / ISO/IEC 22237**: el estándar europeo de diseño y operación de CPD, adoptado como norma internacional. Sus partes cubren la construcción, la distribución eléctrica, el control ambiental, el cableado y los sistemas de seguridad (50600-2-x), la gestión y operación (50600-3-1) y los indicadores de eficiencia (50600-4-x, entre ellos el PUE). Define **clases de disponibilidad 1 a 4** que se asignan por subsistema (energía, climatización, cableado), además de clases de protección física.

## Infraestructura convergente e hiperconvergente

- **Infraestructura convergente (CI)**: integra servidores, almacenamiento, red y virtualización en una solución empaquetada y validada por el fabricante, que se gestiona como una unidad. Simplifica el despliegue y el soporte, pero cada componente sigue siendo hardware dedicado.
- **Infraestructura hiperconvergente (HCI)**: evolución de la CI **definida por software**: la computación, el almacenamiento y la red se virtualizan sobre nodos x86 estándar y se administran desde una consola única, escalando horizontalmente mediante la adición de nodos.
    - **Ventajas**: gestión unificada y simplificada, escalado flexible, menores costes operativos y base natural para la nube privada.
    - **Desventajas**: dependencia del fabricante (*lock-in*), crecimiento conjunto de los recursos (posible sobredimensionamiento) y retos de integración o migración de las aplicaciones existentes.

La HCI es uno de los pilares del centro de datos definido por software (SDDC), que se estudia en el tema 47 junto con la computación en la nube.

## Monitorización, gestión y tendencias

- **DCIM (Data Center Infrastructure Management)**: software que monitoriza y gestiona de forma integrada la infraestructura física del CPD: consumo energético, climatización, ocupación de espacio en racks, inventario de activos y cableado. Permite planificar la capacidad y simular cambios, y une la gestión TI con la de las instalaciones (BMS).
- **Gestión remota**: interfaces de gestión fuera de banda de los servidores (IPMI, Redfish), consolas KVM sobre IP y acceso a través de redes de gestión dedicadas y protocolos seguros.
- **Automatización y orquestación**: aprovisionamiento automatizado, plantillas e infraestructura como código para despliegues, configuraciones y mantenimiento (tema 26).
- **Eficiencia energética y sostenibilidad**:
    - **PUE (Power Usage Effectiveness)**: el indicador de eficiencia por excelencia (normalizado en ISO/IEC 30134-2 y EN 50600-4-2): cociente entre la **energía total consumida por la instalación** y la **consumida por los equipos TI**. Su ideal teórico es **1,0**; los valores típicos actuales oscilan entre **1,2 y 1,6**. Lo complementan el DCiE (su inversa, en porcentaje), el WUE (agua) y el CUE (carbono).
    - **Medidas**: free-cooling, confinamiento de pasillos, iluminación LED y equipos de bajo consumo, energías renovables, reutilización del calor residual y reciclaje de equipos obsoletos.
    - **Marco europeo**: el Código de Conducta europeo sobre eficiencia energética en CPD (adhesión voluntaria) y la **Directiva (UE) 2023/1791**, de eficiencia energética, cuyo **Reglamento Delegado (UE) 2024/1364** obliga a los CPD con demanda eléctrica TI de al menos **500 kW** a comunicar anualmente sus indicadores (energía, agua, calor residual) a una base de datos europea.
- **Tendencias**:
    - **Edge computing y micro-CPD**: procesamiento cerca de donde se generan los datos, que descentraliza la infraestructura (se desarrolla en el tema 47).
    - **CPD modulares y prefabricados**: bloques estandarizados, incluso en contenedor, de despliegue rápido.
    - **Alta densidad e inteligencia artificial**: los aceleradores (GPU) multiplican la potencia por rack y generalizan la **refrigeración líquida** (direct-to-chip y por inmersión).
    - **Nube híbrida**: el CPD propio convive con servicios de nube pública; el reto operativo actual es la gestión unificada de ambos entornos.

## Caso práctico: diseño de un CPD

**Enunciado**: una administración autonómica quiere consolidar sus servicios (sede electrónica, registro, gestión de expedientes) en un CPD propio. Los sistemas se han categorizado como de **categoría media** del ENS, con nivel medio en disponibilidad, y se exige poder realizar mantenimientos sin parada de servicio.

**Resolución por pasos**:

1. **Requisitos y dimensionamiento**: inventario de servicios y sistemas, potencia TI prevista con margen de crecimiento y requisitos derivados de la categorización ENS (en nivel medio de disponibilidad aplican mp.if.4 con refuerzo R1 y mp.if.6).
2. **Nivel de disponibilidad objetivo**: se adopta el equivalente a **Tier III** (mantenimiento concurrente): redundancia **N+1** y dos líneas de distribución con una activa, que permiten mantener sin interrumpir el servicio (disponibilidad orientativa del 99,982 %).
3. **Diseño físico**: emplazamiento discreto y sin riesgos naturales relevantes; sala técnica en una sola planta con suelo técnico; racks en pasillos frío/caliente con confinamiento; climatización N+1 con free-cooling; doble acometida eléctrica, SAI on-line de doble conversión y grupo electrógeno con autonomía de combustible de 48-72 horas.
4. **Protección contra incendios e inundaciones**: detección precoz por aspiración, extinción por gas inerte y detección de líquidos bajo el suelo técnico (mp.if.5 y mp.if.6).
5. **Seguridad física (mp.if)**: área separada con control de acceso por tarjeta y registro de entradas y salidas (mp.if.1 y mp.if.2), videovigilancia, racks con cerradura y registro de entrada y salida de equipamiento con autorización (mp.if.7).
6. **Red**: arquitectura spine-leaf con switches ToR redundantes, doble salida WAN con operadores distintos y conexión a la Red SARA para los servicios interadministrativos (tema 59).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024): Anexo II, medidas mp.if y op.cont.
- Uptime Institute, Tier Standard: Topology (niveles Tier I-IV).
- ANSI/TIA-942-C, Telecommunications Infrastructure Standard for Data Centers (mayo de 2024).
- Serie EN 50600 (CENELEC) e ISO/IEC 22237; ISO/IEC 30134-2 y EN 50600-4-2 (PUE).
- ASHRAE TC 9.9, Thermal Guidelines for Data Processing Environments, 5.ª edición (2021).
- Directiva (UE) 2023/1791, de eficiencia energética (art. 12), y Reglamento Delegado (UE) 2024/1364 (información de los CPD con demanda TI de al menos 500 kW).
- Verificación web de ediciones y datos volátiles (TIA, Uptime Institute, situación del FK-5-1-12/Novec 1230), consulta de julio de 2026.
