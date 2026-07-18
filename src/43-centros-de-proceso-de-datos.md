# Centros de proceso de datos

El **Centro de Proceso de Datos (CPD)**, en inglés *data center*, es la instalación donde se concentran los recursos necesarios para el almacenamiento, procesamiento y transmisión de la información de una organización. Su objetivo principal es garantizar la **continuidad y disponibilidad** de los servicios, asegurando que los sistemas críticos estén siempre operativos.

## Diseño de un CPD: infraestructura física y lógica

El diseño de un CPD abarca desde la elección del emplazamiento hasta la organización lógica de los sistemas. Las características básicas que debe reunir son:

- **Robustez**: capacidad de resistir fallos y mantener la operatividad en condiciones adversas.
- **Modularidad**: añadir o retirar componentes sin afectar al funcionamiento general.
- **Flexibilidad**: adaptación a los cambios tecnológicos y a las necesidades del negocio.
- **Estandarización**: uso de estándares que facilitan la interoperabilidad y el mantenimiento.

La computación corporativa ha evolucionado desde los mainframes centralizados hacia la arquitectura cliente-servidor, los clústeres de servidores, el grid computing, la virtualización y consolidación de sistemas y, finalmente, la computación en la nube y los modelos híbridos, con el edge computing como última etapa descentralizadora (la nube y las altas prestaciones se desarrollan en el tema [51](51-computacion-en-la-nube-y-altas-prestaciones.md)).

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

- **Cableado estructurado (TIA-942)**: el estándar organiza el CPD en áreas de distribución unidas por cableado troncal y horizontal:
    - **Sala de entrada (entrance room)**: llegada de los operadores de telecomunicaciones y punto de demarcación.
    - **MDA (área de distribución principal)**: centro del cableado troncal; aloja los routers y switches de núcleo (al menos una por CPD).
    - **IDA (intermedia)**: nivel opcional de agregación en CPD grandes o multiedificio.
    - **HDA (horizontal)**: origen del cableado horizontal; aloja los switches de acceso.
    - **ZDA (de zona)**: punto de consolidación opcional entre la HDA y los equipos.
    - **EDA (de equipos)**: los racks con los servidores, el almacenamiento y la electrónica final.
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
- **Refrigeración líquida**: el aire deja de ser suficiente a partir de **20-30 kW por rack**, densidades habituales en los racks con GPU. Modalidades:
    - **Intercambiador de puerta trasera (rear-door)**: radiador agua-aire en la puerta del rack; transición sencilla desde el aire (hasta ~40-50 kW por rack).
    - **Direct-to-chip**: placas frías líquidas sobre CPU y GPU, alimentadas por una **CDU** (unidad de distribución de refrigerante); captura el **70-80 %** del calor y el resto se disipa por aire.
    - **Inmersión**: los servidores se sumergen en un líquido dieléctrico (monofásica o bifásica); máxima densidad, pero mayor cambio operativo.

### Racks y equipamiento TIC

- **Racks**: armarios modulares normalizados que alojan el equipamiento, con ancho de **19 pulgadas** (482,6 mm) y altura medida en unidades rack (**1 U = 1,75 pulgadas = 44,45 mm**); incorporan puertas y paneles con cerradura, regletas de alimentación (PDU), pasahilos, bandejas y guías.
- **Servidores**: formato **torre** (autónomo, buena refrigeración pero ocupa más espacio), **rack** (optimiza el espacio) y **blade** (chasis compartido con alimentación y red comunes: máxima densidad y eficiencia energética, mayor coste).
- **Almacenamiento**: cabinas **NAS** (acceso a nivel de fichero a través de la red) y redes **SAN** (acceso a nivel de bloque por red dedicada); las arquitecturas de almacenamiento y RAID se desarrollan en el tema [45](45-sistemas-de-almacenamiento.md).
- **Electrónica de red**: switches de acceso, agregación y núcleo, routers de interconexión con el exterior, cortafuegos y balanceadores de carga.

## Seguridad física y el Esquema Nacional de Seguridad

La seguridad física combina medidas organizativas y de instalación: zonificación con áreas restringidas, control de accesos automatizado con registro de entradas y salidas (fecha y hora), videovigilancia (CCTV), racks cerrados con llave o lector de tarjeta y normas de operación para el personal y los visitantes.

En las administraciones públicas el marco de referencia es el **Esquema Nacional de Seguridad (RD 311/2022)**, cuyos principios, categorización y medidas generales se estudian en el tema [29](29-esquema-nacional-de-seguridad.md). Al CPD le afecta directamente la familia **mp.if (protección de las instalaciones e infraestructuras)** del Anexo II:

| Medida | Contenido | Aplicación |
| --- | --- | --- |
| **mp.if.1** Áreas separadas y con control de acceso | El equipamiento del CPD se instala en áreas separadas específicas para su función y solo se accede por las entradas previstas | Todas las categorías |
| **mp.if.2** Identificación de las personas | El control de acceso identifica a quien accede a los locales con equipamiento esencial y registra entradas y salidas | Todas las categorías |
| **mp.if.3** Acondicionamiento de los locales | Condiciones de temperatura y humedad, protección frente a las amenazas del análisis de riesgos y protección del cableado | Todas las categorías |
| **mp.if.4** Energía eléctrica | Garantía del suministro y del funcionamiento de las luces de emergencia; refuerzo **R1** (suministro de emergencia para la terminación ordenada de los procesos) en los niveles medio y alto | Dimensión D |
| **mp.if.5** Protección frente a incendios | Protección al menos conforme a la normativa industrial de aplicación | Dimensión D |
| **mp.if.6** Protección frente a inundaciones | Protección frente a incidentes causados por el agua | Dimensión D (no aplica en nivel bajo) |
| **mp.if.7** Registro de entrada y salida de equipamiento | Registro pormenorizado de todo movimiento de equipamiento esencial, con la persona que lo autoriza | Todas las categorías |

Las «instalaciones alternativas» del ENS de 2010 ya no forman parte de mp.if: la disponibilidad de **medios alternativos** es hoy la medida **op.cont.4** (continuidad del servicio, exigible en el nivel alto). Cuando se dispone de un centro de respaldo, se clasifica según su grado de preparación:

- **Centro espejo (mirror)**: réplica activa y sincronizada del CPD principal (activo-activo); recuperación inmediata, coste máximo.
- **Sala caliente (hot site)**: equipada y con los datos replicados; operativa en horas.
- **Sala templada (warm site)**: equipamiento parcial; exige restaurar las copias (días).
- **Sala fría (cold site)**: solo el local acondicionado (energía y climatización); hay que instalar el equipamiento (semanas).
- **Alternativas**: acuerdos recíprocos entre organizaciones y recuperación en la nube (DRaaS).

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

La HCI es uno de los pilares del centro de datos definido por software (SDDC), que se estudia en el tema [51](51-computacion-en-la-nube-y-altas-prestaciones.md) junto con la computación en la nube.

## Monitorización, gestión y tendencias

- **DCIM (Data Center Infrastructure Management)**: software que monitoriza y gestiona de forma integrada la infraestructura física del CPD: consumo energético, climatización, ocupación de espacio en racks, inventario de activos y cableado. Permite planificar la capacidad y simular cambios, y une la gestión TI con la de las instalaciones (BMS).
- **Gestión remota**: interfaces de gestión fuera de banda de los servidores (IPMI, Redfish), consolas KVM sobre IP y acceso a través de redes de gestión dedicadas y protocolos seguros.
- **Automatización y orquestación**: aprovisionamiento automatizado, plantillas e infraestructura como código para despliegues, configuraciones y mantenimiento (tema [26](26-control-de-versiones-integracion-continua-y-devops.md)).
- **Eficiencia energética y sostenibilidad**:
    - **PUE (Power Usage Effectiveness)**: el indicador de eficiencia por excelencia (normalizado en ISO/IEC 30134-2 y EN 50600-4-2): cociente entre la **energía total consumida por la instalación** y la **consumida por los equipos TI**. Su ideal teórico es **1,0**; los valores típicos actuales oscilan entre **1,2 y 1,6**. Lo complementan el DCiE (su inversa, en porcentaje), el WUE (agua) y el CUE (carbono).
    - **Medidas**: free-cooling, confinamiento de pasillos, iluminación LED y equipos de bajo consumo, energías renovables, reutilización del calor residual y reciclaje de equipos obsoletos.
    - **Marco europeo**: el Código de Conducta europeo sobre eficiencia energética en CPD (adhesión voluntaria) y la **Directiva (UE) 2023/1791**, de eficiencia energética, cuyo **Reglamento Delegado (UE) 2024/1364** obliga a los CPD con demanda eléctrica TI de al menos **500 kW** a comunicar anualmente sus indicadores (energía, agua, calor residual) a una base de datos europea.
- **Tendencias**:
    - **Edge computing y micro-CPD**: procesamiento cerca de donde se generan los datos, que descentraliza la infraestructura (se desarrolla en el tema [51](51-computacion-en-la-nube-y-altas-prestaciones.md)).
    - **CPD modulares y prefabricados**: bloques estandarizados, incluso en contenedor, de despliegue rápido.
    - **Alta densidad e inteligencia artificial**: los aceleradores (GPU) multiplican la potencia por rack y generalizan la refrigeración líquida; el **suministro eléctrico** pasa a ser el principal factor limitante de los nuevos CPD de IA (la potencia disponible y los plazos de conexión a la red condicionan dónde y cuándo se construyen).
    - **Nube híbrida**: el CPD propio convive con servicios de nube pública; el reto operativo actual es la gestión unificada de ambos entornos.

## Supuesto práctico 1: diseño de un CPD

**Enunciado**: una administración autonómica quiere consolidar en un CPD propio los servicios que hoy reparte entre varias salas técnicas envejecidas (sede electrónica, registro electrónico, gestión de expedientes y plataformas internas). Los sistemas están categorizados como de **categoría media** del ENS, con **nivel medio** en disponibilidad, y se exige poder realizar los mantenimientos programados sin parada de servicio.

Datos de partida:

- **Carga TI**: **40 racks** con una densidad media de **5 kW por rack**, con previsión de crecimiento del **25 %** a cinco años.
- **PUE objetivo**: **1,4**.
- Doble acometida eléctrica disponible en la parcela y espacio exterior para grupo electrógeno.
- Necesidad de conexión a la **Red SARA** para los servicios interadministrativos.

**Se pide**:

- a) Justificar la solución de infraestructura (CPD propio, housing o nube) y el nivel de disponibilidad objetivo.
- b) Dimensionar la instalación eléctrica y la climatización.
- c) Describir el diseño físico y las instalaciones de protección.
- d) Relacionar las medidas de seguridad física con el ENS.
- e) Diseñar la red del CPD.
- f) Plantear la continuidad del servicio y la operación.

**Resolución**:

**a) Solución de infraestructura y nivel de disponibilidad**

- **CPD propio frente a alternativas**: el housing (alquiler de espacio en un CPD ajeno) y la nube pública con servicios certificados ENS de categoría media son opciones válidas, pero la consolidación de un parque estable de servicios, el control directo de las instalaciones y la soberanía del dato justifican el CPD propio; se adopta una estrategia **híbrida**, reservando la nube para cargas elásticas y para el respaldo (apartado f).
- **Nivel objetivo: Tier III** (equivalente a **Rated 3** de TIA-942 y clase de disponibilidad 3 de EN 50600): el requisito de mantener sin parar exige **mantenimiento concurrente**, que Tier II no ofrece (una sola línea de distribución); Tier IV (tolerante a fallos) duplicaría la inversión (2N, dos líneas activas, compartimentación) sin un requisito que lo justifique. Disponibilidad orientativa: **99,982 %** (parada máxima de **1,57 h/año**).

**b) Dimensionamiento eléctrico y térmico**

- **Potencia TI**: 40 racks × 5 kW = **200 kW**; con el crecimiento del 25 %, se diseña para **250 kW**.
- **Potencia total de la instalación**: con PUE 1,4, 250 × 1,4 = **350 kW**. La demanda TI (250 kW) queda por debajo de los **500 kW**, por lo que no aplica la obligación de comunicación del **Reglamento Delegado (UE) 2024/1364**.
- **SAI**: on-line de doble conversión en configuración **N+1** por línea de distribución (dos líneas, una activa). Carga TI de 250 kW con factor de potencia 0,9 ≈ **280 kVA**: por ejemplo, tres módulos de 140 kVA (dos necesarios más uno de reserva). Autonomía de **10-15 minutos**, suficiente para cubrir el arranque del grupo y sus reintentos.
- **Grupo electrógeno**: cubre la demanda total (350 kW) con margen (en torno a **500 kVA**) y autonomía de combustible de **48-72 horas**, con contrato de repostaje prioritario.
- **Climatización**: la potencia frigorífica iguala aproximadamente la carga TI: **250 kW** en configuración **N+1** (por ejemplo, cuatro unidades de 85 kW, tres necesarias más una), con **free-cooling** para acercarse al PUE objetivo. A 5 kW por rack basta la refrigeración por aire con pasillos confinados (la refrigeración líquida solo se plantea a partir de 20-30 kW por rack).
- **Distribución**: doble acometida, cuadros duplicados y **PDU duales** por rack, con cada equipo alimentado desde las dos líneas.

**c) Diseño físico e instalaciones de protección**

- **Emplazamiento y sala**: edificio discreto, sin riesgos naturales relevantes; instalación en una sola planta con **suelo técnico** y compartimentación en salas (TIC, energía, telecomunicaciones y operación).
- **Distribución del aire**: racks enfrentados en **pasillo frío / pasillo caliente**, con confinamiento del pasillo frío e insuflación por el suelo técnico; sobrepresión y filtrado contra el polvo.
- **Incendios**: detección precoz por **aspiración**, central de señalización con acciones automáticas (parada de clima, cierre de compuertas) y extinción por **gas inerte** (IG-55 o IG-541, inocuo para personas y equipos).
- **Agua**: detección de líquidos bajo el suelo técnico y trazado de las canalizaciones fuera de la vertical de la sala.

**d) Seguridad física y cumplimiento del ENS (familia mp.if, categoría media)**

- **mp.if.1**: la sala TIC es un área separada, específica y con acceso solo por las entradas previstas.
- **mp.if.2**: control de acceso por tarjeta con registro de entradas y salidas (fecha y hora).
- **mp.if.3**: temperatura y humedad monitorizadas dentro de los rangos ASHRAE; cableado protegido y etiquetado.
- **mp.if.4**: el suministro queda garantizado por el SAI y el grupo; en nivel medio de disponibilidad aplica el refuerzo **R1** (suministro de emergencia para la terminación ordenada de los procesos), cubierto por la autonomía del SAI.
- **mp.if.5**: la protección contra incendios del apartado c) cumple la normativa industrial de aplicación.
- **mp.if.6**: detección de inundaciones (exigible al ser nivel medio en disponibilidad).
- **mp.if.7**: registro pormenorizado de entrada y salida de equipamiento, con la persona que lo autoriza.
- **Complementos**: videovigilancia (CCTV), racks con cerradura electrónica y normas de operación para el personal y las visitas.

**e) Red del CPD**

- **Arquitectura spine-leaf** con switches **ToR** redundantes en cada rack y enlaces agregados a dos leaf, adecuada al tráfico este-oeste de la virtualización.
- **Perímetro**: cortafuegos redundantes en alta disponibilidad y balanceadores de carga para los servicios web de la sede.
- **Conectividad exterior**: doble salida WAN con **dos operadores** distintos y rutas físicas separadas; conexión a la **Red SARA** (tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)).
- **Segmentación**: DMZ para sede y registro, zona interna para expedientes y plataformas, y red de gestión fuera de banda (IPMI/Redfish, consolas KVM sobre IP).

**f) Continuidad del servicio y operación**

- **Análisis de impacto (op.cont.1)**, exigible en nivel medio de disponibilidad: identifica los servicios críticos y fija objetivos de recuperación, por ejemplo **RTO de 4 horas** y **RPO de 1 hora** para la sede y el registro.
- **Copias de seguridad (mp.info.6)**: regla **3-2-1** (tres copias, dos soportes distintos, una fuera del CPD), con la copia externa en otro edificio o en nube certificada ENS.
- **Respaldo**: los medios alternativos (op.cont.4) solo son exigibles en nivel alto, pero se recomienda replicar los servicios críticos en la nube híbrida del apartado a) para reducir el RTO.
- **Operación**: **DCIM** para monitorizar energía, climatización, ocupación de racks e inventario; gestión remota fuera de banda; seguimiento mensual del **PUE** frente al objetivo de 1,4 y **auditoría ENS bienal** (obligatoria en categoría media).

## Supuesto práctico 2: ampliación para cargas de inteligencia artificial

**Enunciado**: dos años después de la puesta en marcha del CPD del caso 1, la administración quiere desplegar una plataforma de IA generativa: un asistente interno para los empleados públicos y la tramitación asistida de expedientes con modelos de lenguaje (LLM) sobre documentación propia. Por soberanía del dato, la inferencia debe ejecutarse en las instalaciones propias. El piloto dimensionado por el área de sistemas consta de **8 servidores de 8 GPU**, con un consumo aproximado de **10 kW por servidor** (**80 kW** TI adicionales).

**Se pide**:

- a) Definir la estrategia de despliegue (qué se ejecuta en el CPD y qué en la nube).
- b) Ubicar la nueva carga: densidad por rack y solución de refrigeración.
- c) Evaluar el impacto sobre la instalación eléctrica y el cumplimiento normativo.
- d) Adaptar la red, el almacenamiento y la operación.

**Resolución**:

**a) Estrategia de despliegue**

- **Entrenamiento desde cero**: descartado; exige decenas de miles de GPU y solo está al alcance de los grandes proveedores. Se parte de **modelos fundacionales** ya entrenados.
- **Ajuste fino (fine-tuning) y experimentación**: en **nube con servicios certificados ENS** de categoría media: es una carga puntual e intensiva en la que el pago por uso evita inmovilizar inversión.
- **Inferencia**: en el **CPD propio**: es una carga continua y predecible, procesa documentación interna (soberanía del dato) y su coste es estable frente al pago por consumo. Las arquitecturas de computación (HPC, nube) se desarrollan en el tema [51](51-computacion-en-la-nube-y-altas-prestaciones.md).

**b) Densidad y refrigeración**

- **Densidad**: con 4 servidores por rack, la ampliación cabe en **2 racks** de **40 kW por rack** (frente a los 5 kW del resto de la sala), fuera del alcance de la refrigeración por aire (límite práctico de 20-30 kW por rack).
- **Solución**: zona dedicada con **direct-to-chip**: placas frías en GPU y CPU alimentadas por una **CDU en N+1** conectada al circuito de agua enfriada; el 20-30 % del calor restante lo asume el aire de la sala. Se descartan el intercambiador de puerta trasera (a 40 kW queda al límite, sin margen de crecimiento) y la inmersión (cambio operativo excesivo para un piloto).
- **Peso**: un rack de GPU cargado supera los **1.000 kg**; se verifica la carga admisible del suelo técnico y, si es preciso, la zona se apoya directamente sobre el forjado.

**c) Impacto eléctrico y cumplimiento normativo**

La electricidad es hoy el principal cuello de botella de la IA: antes de adquirir las GPU hay que asegurar que la instalación (y la red eléctrica que la alimenta) puede soportarlas. Se reverifica toda la cadena:

- **Acometida**: se comprueba con la distribuidora la potencia contratada y la disponible en la zona (en los grandes CPD de IA, los **plazos de conexión a la red eléctrica** son ya el factor que decide dónde se construye).
- **Carga TI**: 250 + 80 = **330 kW**.
- **SAI**: los 280 kVA del caso 1 no cubren la nueva carga (330 kW / 0,9 ≈ **367 kVA**): se añaden módulos manteniendo la configuración **N+1** y las dos líneas de distribución (la ampliación conserva el Tier III).
- **Grupo electrógeno**: la demanda total sube a unos **445 kW** (los 350 kW previos más la zona GPU, que opera con un PUE parcial de ~1,2 gracias al líquido); el grupo de 500 kVA (~400 kW) se queda corto y se instala un **segundo grupo en paralelo**.
- **Umbral normativo**: la demanda TI (330 kW) sigue por debajo de los **500 kW**, por lo que continúa sin aplicar el **Reglamento Delegado (UE) 2024/1364**; el cálculo se repetirá en cada ampliación.
- **PUE global**: mejora ligeramente (hacia **~1,35**), porque la zona líquida es más eficiente que la media de la sala.

**d) Red, almacenamiento y operación**

- **Red**: fabric dedicado para el tráfico este-oeste entre GPU (**Ethernet de 200/400 Gb/s con RoCE** o InfiniBand), separado de la red spine-leaf de producción, a la que la plataforma se conecta como un servicio más.
- **Almacenamiento**: cabina **NVMe** de alto rendimiento para los modelos y la documentación indexada que consultan.
- **Operación**: el **DCIM** incorpora la telemetría del circuito líquido (caudal, temperatura, detección de fugas) y el **PUE parcial** de la zona GPU; el registro de entrada del nuevo equipamiento cumple **mp.if.7**.

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024): Anexo II, medidas mp.if, op.cont y mp.info.
- Uptime Institute, Tier Standard: Topology (niveles Tier I-IV).
- ANSI/TIA-942-C, Telecommunications Infrastructure Standard for Data Centers (mayo de 2024).
- Serie EN 50600 (CENELEC) e ISO/IEC 22237; ISO/IEC 30134-2 y EN 50600-4-2 (PUE).
- ASHRAE TC 9.9, Thermal Guidelines for Data Processing Environments, 5.ª edición (2021).
- Directiva (UE) 2023/1791, de eficiencia energética (art. 12), y Reglamento Delegado (UE) 2024/1364 (información de los CPD con demanda TI de al menos 500 kW).
- Verificación web de ediciones y datos volátiles (TIA, Uptime Institute, situación del FK-5-1-12/Novec 1230), consulta de julio de 2026.
