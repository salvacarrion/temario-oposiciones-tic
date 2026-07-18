# Cableado estructurado y medios de transmisión

La capa física de una red corporativa se materializa en sus medios de transmisión y en el sistema de cableado que los organiza. El **cableado estructurado** es un cableado genérico, planificado e independiente de las aplicaciones que lo usarán, normalizado por **ANSI/TIA-568** e **ISO/IEC 11801**, que permite que voz, datos y vídeo compartan una misma infraestructura con una vida útil de 15 a 25 años.

## Medios de transmisión

Los medios guiados transportan la señal por un soporte físico (cobre o fibra); los no guiados la radian por el aire. La elección depende del ancho de banda, la distancia, el coste y la inmunidad al ruido. Tres fenómenos limitan a todo medio: la **atenuación** (pérdida de potencia con la distancia, en dB), la **distorsión** (cada frecuencia se propaga distinto) y el **ruido** (interferencias externas, EMI, y diafonía entre pares).

- **Par trenzado**: cuatro pares de hilos de cobre trenzados (el trenzado cancela interferencias y diafonía), conector **RJ45** y alcance de canal de **100 m**. Según el apantallamiento se denomina **U/UTP** (sin pantalla), **F/UTP** (pantalla global de lámina) o **S/FTP** (malla global y lámina por par). Es el medio estándar del cableado horizontal por su coste y facilidad de instalación.

| Categoría | Ancho de banda | Aplicación típica |
| --- | --- | --- |
| **5e** | 100 MHz | 1000BASE-T (1 Gbps) |
| **6** | 250 MHz | 1 Gbps (10 Gbps solo hasta ~55 m) |
| **6A** | 500 MHz | **10GBASE-T (10 Gbps a 100 m)**; mínimo recomendado en instalación nueva |
| **7 / 7A** | 600 / 1000 MHz | Siempre apantalladas (solo ISO, sin reconocimiento TIA) |
| **8** | 2000 MHz | **25/40GBASE-T hasta 30 m**, enlaces cortos de CPD |

- **Cable coaxial**: conductor central y malla concéntrica, gran inmunidad al ruido. Hoy es residual en redes de datos; pervive en las redes de televisión por cable **CATV/HFC** (75 ohmios, tema [74](74-redes-de-transporte-voz-y-audiovisuales.md)) y en radiofrecuencia (antenas).
- **Fibra óptica**: transmite pulsos de luz por un núcleo de vidrio que los confina por reflexión total interna; inmune a interferencias electromagnéticas, sin emisiones (más segura frente a escuchas) y con atenuaciones muy bajas (del orden de **0,2 a 0,4 dB/km**), lo que da alcances y anchos de banda muy superiores al cobre. Se transmite en las **ventanas** de menor atenuación: **850 nm** (multimodo), **1310 y 1550 nm** (monomodo). Dos tipos:
  - **Monomodo (OS1/OS2)**: núcleo de **9 µm**, láser a 1310/1550 nm, alcances de kilómetros; es la fibra de los enlaces troncales, el acceso FTTH y las redes de operador.
  - **Multimodo (OM1 a OM5)**: núcleo de **50 µm** (62,5 µm en la antigua OM1), fuentes VCSEL a 850 nm, alcances de cientos de metros: **OM3** (10 Gbps hasta 300 m), **OM4** (10 Gbps hasta 550 m, 100 Gbps en paralelo), **OM5** (multiplexación por longitud de onda corta, SWDM). Habitual dentro del edificio y el CPD.
  - **Conectores**: **LC** (pequeño factor de forma, el habitual), SC, y MPO/MTP para enlaces paralelos de alta densidad.
- **Medios no guiados**: radioenlaces y microondas, Wi-Fi y comunicaciones móviles; se tratan en el tema [76](76-redes-inalambricas-y-5g.md).

## Cableado estructurado: subsistemas y topología

Las dos normas de referencia definen el mismo modelo: **ANSI/TIA-568** (familia norteamericana; revisión vigente del par trenzado: **ANSI/TIA-568.2-E, de octubre de 2024**) e **ISO/IEC 11801-1:2017** (internacional; su equivalente europeo es la serie **EN 50173**). La topología es una **estrella jerárquica**: cada toma llega a un repartidor de planta, y los repartidores se interconectan por el troncal.

- **Acometida o entrada del edificio**: punto donde entran los servicios externos de los operadores y se protege y adapta el cableado exterior.
- **Sala de equipos**: aloja los equipos activos centrales del edificio (núcleo de red, servidores, centralita).
- **Subsistema troncal (vertical o *backbone*)**: interconecta la sala de equipos con los repartidores de planta y entre edificios de un campus; habitualmente fibra óptica.
- **Cuarto de telecomunicaciones (repartidor de planta)**: armario o sala por planta con los paneles de parcheo y la electrónica de acceso.
- **Subsistema horizontal**: desde el repartidor de planta hasta la toma de usuario: máximo **90 m** de enlace permanente más **10 m** de latiguillos (canal de **100 m**). No debe haber empalmes ni derivaciones.
- **Área de trabajo**: la toma de telecomunicaciones (TO) y los latiguillos del puesto.

La norma ISO define **clases** de canal (el enlace completo instalado) que se corresponden con las **categorías** de los componentes (cable y conectores):

| Clase ISO (canal) | Categoría (componentes) | Frecuencia |
| --- | --- | --- |
| D | 5e | 100 MHz |
| E | 6 | 250 MHz |
| **EA** | **6A** | **500 MHz** |
| F / FA | 7 / 7A | 600 MHz / 1 GHz |
| I / II | 8.1 / 8.2 | 2 GHz |

La administración del sistema (etiquetado de tomas, paneles y cables, registros y códigos de color) se normaliza en **ANSI/TIA-606**; toda toma y todo latiguillo deben quedar identificados de forma única.

## Parámetros y certificación

Certificar un cableado es medirlo con un **certificador de campo** y compararlo automáticamente con los límites de la norma para la clase o categoría declarada, dejando informe por enlace. Se puede medir el **canal** completo (con latiguillos) o el **enlace permanente** (lo instalado de forma fija, la medida habitual de recepción de obra).

- **Mapa de hilos y longitud**: continuidad, orden de los pares (esquemas T568A/T568B) y longitud máxima.
- **Pérdida de inserción (atenuación)**: pérdida de potencia de la señal con la distancia y la frecuencia; se mide en dB.
- **Diafonía**: acoplamiento de señal entre pares. **NEXT** (extremo cercano) y su suma de potencia **PS-NEXT**; por el extremo lejano se evalúa **ACR-F** (antes ELFEXT). El margen entre señal y diafonía es el **ACR-N**. En categoría 6A se añade la **diafonía exógena** (*alien crosstalk*) entre cables adyacentes del mazo.
- **Pérdida de retorno**: reflexiones por desadaptación de impedancia (importante a alta frecuencia).
- **Retardo de propagación y desfase (*delay skew*)**: diferencia de retardo entre pares, crítica cuando los cuatro pares transmiten en paralelo.
- **Resistencia DC y su desequilibrio**: relevante para la alimentación PoE (la revisión 568.2-E incorpora los requisitos de desequilibrio de resistencia).
- **Fibra óptica**: se certifica la **pérdida del enlace** con fuente y medidor (OLTS) en las longitudes de onda de trabajo y, para diagnóstico, con **OTDR** (reflectometría que localiza eventos por distancia); la limpieza e inspección de conectores es la primera causa de problemas.

Buenas prácticas de instalación: respetar el **radio de curvatura** y la tensión máxima de tracción, no destrenzar más de **13 mm** en la terminación, mantener la separación con el cableado eléctrico y las fuentes de interferencia (distancias mínimas de la norma de instalación **EN 50174-2**), no sobrecargar canalizaciones (reserva de ocupación), usar latiguillos de fábrica y probar el 100 % de los enlaces con informe de certificación por toma.

## El cableado del CPD y PoE

El centro de proceso de datos tiene su propia norma de infraestructura (**ANSI/TIA-942**, tratada en el tema [43](43-centros-de-proceso-de-datos.md)) que aplica el modelo estructurado a las áreas del CPD (distribuidor principal MDA, distribuidores horizontales HDA y áreas de equipos EDA), con topologías de conmutación **ToR** (*top of rack*, conmutador en cada armario) o **EoR** (*end of row*). En CPD la práctica actual es **categoría 6A como mínimo** en cobre y fibra **OM4/OS2** con conectividad LC y troncales MPO preconectorizados.

**PoE (Power over Ethernet)** alimenta dispositivos por el propio par trenzado, eliminando tomas eléctricas dedicadas: telefonía IP, puntos de acceso Wi-Fi, cámaras y sensores.

| Estándar | Año | Tipo | Potencia del equipo alimentador (PSE) | Potencia al dispositivo (PD) |
| --- | --- | --- | --- | --- |
| IEEE **802.3af** (PoE) | 2003 | 1 | **15,4 W** | 13 W |
| IEEE **802.3at** (PoE+) | 2009 | 2 | **30 W** | 25,5 W |
| IEEE **802.3bt** (4PPoE) | 2018 | 3 / 4 | **60 / 90 W** | 51 / 71,3 W |

El 802.3bt alimenta por los **cuatro pares** y exige atención al calentamiento de los mazos de cables y al desequilibrio de resistencia DC; con cargas PoE altas se recomienda cableado de categoría 6A y limitar el tamaño de los mazos.

## Supuesto práctico: diseño del cableado estructurado de un edificio

**Enunciado**: una conselleria rehabilita para oficinas un edificio de **4 plantas** de unos **1.000 m²** cada una, con **60 puestos de trabajo por planta**. Además, cada planta necesita **8 puntos de acceso Wi-Fi**, **4 cámaras IP** y unas **8 tomas** para impresoras y salas de reuniones. La telefonía es IP y debe alimentarse por el propio cableado, igual que los AP y las cámaras. A **250 m**, en otro edificio del mismo recinto, está la sala técnica principal con el enlace al CPD corporativo. Se exige una vida útil de al menos **15 años** y la certificación del 100 % de la instalación.

**Se pide**:

- a) Dimensionar las tomas y elegir la categoría del cableado horizontal.
- b) Definir los subsistemas, repartidores y topología.
- c) Diseñar el troncal de edificio y el enlace de campus.
- d) Dimensionar la electrónica de acceso y el PoE.
- e) Establecer el plan de certificación y administración.

**Resolución**:

**a) Tomas y categoría del horizontal**

- **Tomas por planta**: 60 puestos × **2 tomas** (voz IP y datos, la práctica habitual) = 120; más 8 AP con 2 tomas cada uno (16, previendo enlaces agregados futuros), 4 cámaras y 8 tomas comunes: **148 tomas**. Con una **reserva del ~20 %** resultan unas **180 tomas por planta**, parcheadas en **8 paneles de 24 puertos**, y en torno a **720 en el edificio**.
- **Categoría**: **6A / clase EA** (10GBASE-T hasta 100 m), el mínimo razonable en obra nueva con 15-25 años de vida útil; en mazos densos con PoE conviene cable **apantallado (F/UTP)**, que elimina el problema de la diafonía exógena y disipa mejor el calor.
- **Distancias**: con el repartidor centrado en cada planta de 1.000 m², ningún enlace permanente se acerca al límite de **90 m** (canal de 100 m con latiguillos).

**b) Subsistemas y topología**

- **Estrella jerárquica** normalizada (ANSI/TIA-568 e ISO/IEC 11801): acometida de operadores en planta baja; **repartidor de edificio** en la sala técnica de planta baja; un **cuarto de telecomunicaciones por planta** (repartidor de planta) con acceso controlado, alimentación protegida por SAI y ventilación; subsistema horizontal **sin empalmes ni derivaciones** hasta la toma; área de trabajo con latiguillos de fábrica.
- **Armarios**: rack de 19" por planta con paneles de parcheo, guías pasahilos, electrónica de acceso y espacio de reserva; separación de recorridos respecto del cableado eléctrico según **EN 50174-2**.

**c) Troncal y enlace de campus**

- **Troncal vertical**: fibra multimodo **OM4** (sobrada para 10/40 Gbps en distancias de edificio) desde el repartidor de edificio a cada planta, **12 fibras por planta** con conectividad **LC**; no se tiende multipar telefónico porque toda la voz es IP.
- **Enlace de campus (250 m)**: fibra **monomodo OS2** de exterior (holgura para 100 Gbps futuros), tendida por **dos rutas físicas separadas** para tolerar un corte; OM4 alcanzaría (10 Gbps hasta 550 m), pero OS2 es la elección correcta a 15-25 años vista.
- **Puesta a tierra**: sistema de tierra de telecomunicaciones y continuidad de pantallas (*bonding*) en toda la instalación apantallada.

**d) Electrónica de acceso y PoE**

- **Por planta**: para unas 148 tomas activas previstas, **4 conmutadores apilados de 48 puertos** (192 puertos) con uplinks redundantes de **2 × 10 Gbps** (SFP+) hacia el núcleo por caminos físicos distintos.
- **PoE**: teléfonos IP y cámaras con **802.3af** (15,4 W); AP Wi-Fi 6/6E con **802.3at** (30 W) o **802.3bt** los de gama alta (tema [76](76-redes-inalambricas-y-5g.md)). Se comprueba el **presupuesto PoE** de cada conmutador (por ejemplo, 740 W) frente a la suma de cargas, y el SAI del armario se dimensiona incluyendo ese consumo.

**e) Certificación y administración**

- **Cobre**: certificación del **100 % de los enlaces permanentes** a **clase EA** con certificador de campo: mapa de hilos, longitud, pérdida de inserción, NEXT/PS-NEXT, ACR-F, pérdida de retorno, retardo y desfase, resistencia DC y su desequilibrio (crítico con PoE) y **diafonía exógena**; informe por toma como condición de recepción de la obra.
- **Fibra**: pérdida del enlace con **OLTS** en las longitudes de onda de trabajo (850/1300 nm en OM4; 1310/1550 nm en OS2) y **OTDR** para documentar cada tramo del enlace de campus.
- **Administración (ANSI/TIA-606)**: identificador único por toma, panel, cable y armario, etiquetado en ambos extremos, registros *as-built* y actualización obligatoria con cada cambio.

## Fuentes {.unnumbered .unlisted}

- ANSI/TIA-568: TIA-568.0-E/568.1-E y **ANSI/TIA-568.2-E** (cableado de par trenzado, octubre de 2024); ANSI/TIA-606 (administración) y ANSI/TIA-942 (CPD), citadas por edición (normas de pago).
- ISO/IEC 11801-1:2017, *Generic cabling for customer premises*, y serie europea EN 50173 (citadas por edición).
- IEEE 802.3af-2003, 802.3at-2009 y 802.3bt-2018 (Power over Ethernet).
