# Sistemas de información geográfica

Un sistema de información geográfica (SIG, en inglés GIS) es un sistema de información diseñado para capturar, almacenar, gestionar, analizar y visualizar datos georreferenciados, es decir, datos asociados a una posición sobre el territorio. Combina cartografía digital con bases de datos alfanuméricas, y eso le permite responder no solo «qué» ocurre, sino «dónde» ocurre. Este tema cubre los conceptos básicos (datos raster y vectoriales), los componentes y funcionalidades de un SIG y la incorporación de la componente geográfica a los sistemas de información; los servicios web geográficos (WMS, WFS, CSW) y las infraestructuras de datos espaciales se estudian en el tema [67](67-infraestructuras-de-datos-espaciales.md).

## Conceptos: datos raster y vectoriales

El dato geográfico tiene tres componentes: la **componente espacial** (dónde está: geometría y posición), la **componente temática** (qué es: sus atributos alfanuméricos) y la **componente temporal** (cuándo: el momento o periodo al que se refiere). Un SIG organiza esta información en **capas** temáticas superpuestas sobre un mismo territorio (relieve, hidrografía, vías, usos del suelo, población), de modo que pueden combinarse y analizarse conjuntamente.

- **SIG frente a CAD**: un sistema CAD dibuja geometrías sin atributos asociados ni topología; un SIG vincula cada geometría con datos alfanuméricos y relaciones espaciales, lo que permite consultarla y analizarla, no solo representarla.
- **Problemas que resuelve un SIG** (las preguntas clásicas):
    - **Localización**: ¿qué hay en un lugar determinado?
    - **Condición**: ¿dónde se cumplen ciertas condiciones? (p. ej. parcelas de más de 1 ha a menos de 500 m de una carretera).
    - **Tendencias**: ¿qué ha cambiado en una zona a lo largo del tiempo?
    - **Rutas**: ¿cuál es el camino óptimo entre dos puntos?
    - **Pautas**: ¿qué patrones espaciales existen? (p. ej. concentración de incidencias).
    - **Modelización**: ¿qué pasaría si...? (simulación de escenarios: inundaciones, crecimiento urbano).

### Sistemas de referencia y coordenadas

Para que las capas de distintos orígenes casen entre sí, todas deben expresarse en un sistema de referencia común.

- **Datum geodésico**: modelo de referencia que define la forma y dimensiones de la Tierra (un elipsoide) y su punto de anclaje; sobre él se definen los sistemas de coordenadas.
- **Sistema oficial en España**: el **Real Decreto 1071/2007** adopta **ETRS89** como sistema geodésico de referencia oficial en la Península y Baleares y **REGCAN95** en Canarias, ambos sobre el elipsoide **GRS80**. Toda la cartografía oficial se compila en estos sistemas desde el **1 de enero de 2015** (hasta esa fecha convivió con el antiguo ED50). En la práctica ETRS89 es compatible con el WGS84 que usan los GNSS.
- **Sistema altimétrico**: las altitudes oficiales se refieren al **nivel medio del mar en Alicante** (Península); en las islas, a las referencias mareográficas locales.
- **Coordenadas geográficas y proyectadas**: las geográficas (latitud y longitud, en grados) sitúan el punto sobre el elipsoide; para trabajar sobre un plano se usa una proyección cartográfica, que introduce siempre alguna distorsión.
- **Proyección UTM (Universal Transversa de Mercator)**: divide la Tierra en **60 husos de 6º** de longitud y expresa las coordenadas en metros. El RD 1071/2007 la adopta (como ETRS-Transversa de Mercator) para la cartografía oficial a escalas mayores de 1:500.000; para escalas menores se usa la cónica conforme de Lambert. La España peninsular cae en los husos **29, 30 y 31**; la cartografía oficial de la Comunitat Valenciana usa el **huso 30** (código **EPSG:25830**, ETRS89/UTM 30N).

### El modelo raster

Representa el espacio como una **matriz de celdas (píxeles)**, cada una con un valor. Es el modelo natural para variables continuas y para imágenes.

- **Resolución**: tamaño de la celda sobre el terreno (p. ej. 25 cm/píxel en una ortofoto); a menor celda, más detalle y más volumen de datos.
- **Usos típicos**: ortofotografías e imágenes de satélite, **modelos digitales del terreno (MDT)** y de superficies (MDS: incluye edificios y vegetación), mapas de pendientes, temperatura o precipitación.
- **Formatos comunes**: **GeoTIFF** (.tif), ECW, MrSID (.sid), JPEG2000, ESRI grid.

### El modelo vectorial

Representa los objetos geográficos mediante **puntos, líneas y polígonos** definidos por coordenadas, con una tabla de atributos asociada a cada entidad. Es el modelo natural para objetos discretos (parcelas, vías, hidrantes, límites administrativos).

- **Topología**: relaciones espaciales entre entidades (conectividad, adyacencia, contención) que el SIG puede almacenar y validar; imprescindible para análisis de redes y para garantizar la coherencia de la cartografía (p. ej. que las parcelas no se solapen).
- **Formatos comunes**: **shapefile** (.shp, de ESRI, el formato de intercambio clásico), **GeoPackage** (.gpkg, estándar OGC sobre SQLite, su sustituto moderno), **GeoJSON** (RFC 7946, habitual en web), **GML** (Geography Markup Language, XML del OGC), KML (Google Earth), formatos CAD (DXF, DWG, DGN) y bases de datos espaciales.

| Aspecto | Raster | Vectorial |
| --- | --- | --- |
| Estructura | Matriz de celdas con un valor | Puntos, líneas y polígonos con atributos |
| Representa bien | Variables continuas (relieve, imágenes) | Objetos discretos (parcelas, redes) |
| Precisión posicional | Limitada por el tamaño de celda | Alta (coordenadas exactas) |
| Volumen de datos | Alto (crece con la resolución) | Menor para la misma extensión |
| Análisis típico | Álgebra de mapas, superficies | Redes, topología, consultas por atributos |
| Formatos | GeoTIFF, ECW, MrSID | Shapefile, GeoPackage, GeoJSON, GML |

## Componentes y funcionalidades de un SIG

Un SIG completo tiene cinco componentes: hardware, software, datos, personas y procedimientos. Los datos suelen ser el componente más costoso de obtener y mantener.

- **Hardware**: estaciones de trabajo, servidores, dispositivos de captura (GNSS, drones, escáneres) y de salida (plóteres).
- **Software**: el conjunto de programas que capturan, gestionan, analizan y publican la información:
    - **SIG de escritorio**: **QGIS** (software libre, el más extendido), **gvSIG Desktop**, **ArcGIS Pro** (ESRI, comercial).
    - **Bases de datos espaciales**: **PostGIS** (extensión espacial de PostgreSQL), Oracle Spatial, SQL Server y MySQL con tipos espaciales.
    - **Bibliotecas geoespaciales**: **GDAL/OGR** (lectura, escritura y conversión de formatos raster y vectoriales), PROJ (transformación entre sistemas de referencia), GeoTools (Java).
    - **SIG en la nube**: ArcGIS Online, CARTO; ofrecen almacenamiento, visores y análisis como servicio.
- **Datos**: cartografía de referencia y capas temáticas, propias o de terceros (ver fuentes de datos más abajo).
- **Personas**: administradores, técnicos SIG, desarrolladores y usuarios finales.
- **Procedimientos**: métodos y normas de captura, actualización, control de calidad y explotación.

El **proyecto gvSIG** merece mención propia: nació en la **Generalitat Valenciana** en **2004**, dentro de la migración a software libre de la entonces Conselleria de Infraestructuras y Transporte, y desde **2010** lo gestiona la **Asociación gvSIG** (empresas, universidades y administraciones). Es software libre (licencia GPL), basado en estándares OGC. La suite actual comprende **gvSIG Desktop** (versión 2.7, enero de 2026), **gvSIG Online** (plataforma en la nube para infraestructuras de datos espaciales y geoportales) y **gvSIG Mapps** (desarrollo de aplicaciones móviles con componente geográfica).

### Funcionalidades

- **Captura y edición**: digitalización sobre pantalla, importación de formatos, levantamientos con GNSS, edición con validación topológica.
- **Almacenamiento y gestión**: bases de datos espaciales con índices espaciales, gestión de metadatos, versionado de la cartografía.
- **Consulta y medición**: consultas por atributos (alfanuméricas) y espaciales (por localización, proximidad o intersección); medición de distancias, áreas y perímetros.
- **Análisis espacial** (el corazón de un SIG):
    - **Superposición de capas** (*overlay*): intersección, unión y recorte entre capas (p. ej. cruzar planeamiento con parcelario).
    - **Áreas de influencia** (*buffer*): zonas a una distancia dada de un elemento (p. ej. franja de 100 m alrededor de un cauce).
    - **Análisis de redes**: rutas óptimas, instalación más cercana, áreas de servicio sobre redes viarias o de suministro.
    - **Análisis del terreno**: pendientes, orientaciones, cuencas hidrológicas y visuales a partir de un MDT.
    - **Interpolación y geoestadística**: estimar una variable continua a partir de puntos de muestreo.
    - **Álgebra de mapas**: operaciones celda a celda entre capas raster.
- **Visualización y producción cartográfica**: simbología, mapas temáticos (coropletas, símbolos proporcionales), composición de planos para impresión, vistas 3D.

### Fuentes de datos geográficos

- **Teledetección**: sensores a bordo de satélites o aeronaves; destaca el programa europeo **Copernicus** y sus satélites Sentinel, con imágenes multiespectrales gratuitas.
- **Fotogrametría**: obtención de cartografía a partir de fotografías aéreas (aviones o drones). En España, el **Plan Nacional de Ortofotografía Aérea (PNOA)** del IGN produce ortofotos y, con vuelos **LiDAR**, modelos digitales del terreno de alta resolución.
- **GNSS**: levantamiento directo de posiciones sobre el terreno (GPS, Galileo).
- **Organismos oficiales**: el **Instituto Geográfico Nacional (IGN)** y su Centro Nacional de Información Geográfica (CNIG), la **Dirección General del Catastro** (parcelario) y, en la Comunitat Valenciana, el **Institut Cartogràfic Valencià (ICV)**, productor de la cartografía oficial autonómica.

## La componente geográfica en los sistemas de información

Gran parte de la información que manejan las administraciones lleva asociada una localización: domicilios del padrón, parcelas catastrales, expedientes urbanísticos, infraestructuras, incidencias en la vía pública. Incorporar esa componente geográfica a los sistemas de información corporativos (en lugar de mantener un SIG aislado) permite explotarla en los propios procesos de gestión.

- **Georreferenciación**: asignar coordenadas en un sistema de referencia conocido a información que carece de ellas (p. ej. un plano escaneado que se ajusta sobre la cartografía mediante puntos de control).
- **Geocodificación directa**: convertir una dirección postal o un identificador (referencia catastral, portal) en coordenadas; es el paso que permite mapear los registros administrativos.
- **Geocodificación inversa**: obtener la dirección o entidad territorial correspondiente a unas coordenadas (p. ej. localizar el municipio y la calle desde la posición de un móvil en una llamada al 112).
- **Bases de datos espaciales en el SI corporativo**: los SGBD con tipos de dato geométricos y funciones espaciales estándar (especificación *Simple Features* del OGC/ISO) permiten mezclar en una misma consulta criterios alfanuméricos y espaciales («expedientes abiertos en parcelas a menos de 200 m del dominio público marítimo-terrestre»), sin salir de la base de datos corporativa.
- **Casos de uso en la Administración**: padrón y gestión tributaria (domicilios y direcciones normalizadas), catastro y urbanismo (parcelario, planeamiento, licencias), emergencias (localización de llamadas, despliegue de recursos), servicios municipales (rutas de recogida de residuos, alumbrado, mantenimiento), planificación de equipamientos (análisis de cobertura y demanda por zonas).
- **Visores y APIs de mapas**: las aplicaciones de gestión incorporan mapas mediante bibliotecas web (OpenLayers, Leaflet) o APIs comerciales, consumiendo cartografía publicada como servicios web.

La publicación y compartición de esta información mediante servicios web estandarizados (WMS, WFS, CSW) y su organización en infraestructuras de datos espaciales (INSPIRE, LISIGE, IDEE, IDECV) se estudian en el tema [67](67-infraestructuras-de-datos-espaciales.md).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 1071/2007, de 27 de julio, por el que se regula el sistema geodésico de referencia oficial en España (BOE de 29 de agosto de 2007; sin modificaciones posteriores, contrastado online en julio de 2026).
- OGC GeoPackage Encoding Standard; GeoJSON (RFC 7946, agosto de 2016); OGC/ISO Simple Features.
- Portal del proyecto gvSIG, Asociación gvSIG (suite gvSIG: Desktop 2.7 de enero de 2026, Online y Mapps; consulta: julio de 2026).
- Portales oficiales del IGN/CNIG (PNOA, Copernicus) y del Institut Cartogràfic Valencià (consulta: julio de 2026).
