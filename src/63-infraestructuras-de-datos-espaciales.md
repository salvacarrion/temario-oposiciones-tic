# Infraestructuras de datos espaciales

Una infraestructura de datos espaciales (IDE) es el conjunto de datos georreferenciados, metadatos, servicios web estandarizados, acuerdos y normas que permite a productores y usuarios compartir información geográfica a través de Internet de forma interoperable. Si el tema 62 trata cómo se produce y analiza la información geográfica (los SIG), este trata cómo se publica y se comparte: la definición y componentes de una IDE, sus servicios web (WMS, WFS, CSW) y el marco normativo que las regula en Europa (INSPIRE) y en España (LISIGE).

## Definición y componentes de una IDE

La LISIGE define la infraestructura de información geográfica (art. 3.1.a) como «aquella estructura virtual en red integrada por datos georreferenciados y servicios interoperables de información geográfica distribuidos en diferentes sistemas de información, accesible vía Internet con un mínimo de protocolos y especificaciones normalizadas», que incluye además los metadatos, las tecnologías de búsqueda y acceso, las normas para su producción, gestión y difusión, los acuerdos de puesta en común entre productores y usuarios y los mecanismos de coordinación y seguimiento.

- **Qué resuelve una IDE**: cada organismo produce y custodia sus propios datos, pero los publica con estándares comunes; el usuario los localiza, visualiza y combina sin copiarlos ni conocer su sistema de origen. Se evita duplicar la producción cartográfica y se aumenta el valor de los datos.
- **Materialización**: cada nodo (organismo) publica servicios web sobre sus datos, y un **geoportal** agrega el acceso: visor cartográfico, catálogo de metadatos y nomenclátor.

### Componentes

- **Datos**:
    - **De referencia**: proporcionan la localización precisa y permiten cruzar fuentes (cartografía básica, ortofotos, modelos digitales del terreno, límites administrativos, direcciones).
    - **Temáticos**: desarrollan un aspecto concreto sobre la referencia (medio ambiente, población, riesgos, planeamiento).
- **Metadatos**: descripción normalizada de datos y servicios (origen, calidad, condiciones de uso, sistema de referencia) que hace posible localizarlos, inventariarlos y utilizarlos. Norma de referencia: **ISO 19115**; en España, el perfil recomendado por el Consejo Superior Geográfico es el **Núcleo Español de Metadatos (NEM)**.
- **Estándares**: garantizan la interoperabilidad; los elaboran el **OGC (Open Geospatial Consortium)**, consorcio internacional que especifica los servicios web geográficos, y el comité **ISO/TC 211** (familia **ISO 19100** de información geográfica).
- **Marco organizativo y político**: normativa (INSPIRE, LISIGE, normas de ejecución), acuerdos institucionales de puesta en común y órganos de coordinación (en España, el Consejo Superior Geográfico y el CODIIGE; ver marco normativo).
- **Usuarios**: administraciones, empresas, profesionales y ciudadanos que consumen los datos y servicios.

### Arquitectura

Una IDE sigue una arquitectura cliente-servidor distribuida, orientada a servicios y basada en estándares abiertos.

- **Lado servidor (cada nodo)**: bases de datos espaciales (tema 62), un **servidor de mapas** que publica los datos como servicios OGC (**GeoServer**, **MapServer**) y un **catálogo de metadatos** consultable vía CSW (**GeoNetwork**).
- **Clientes ligeros**: geoportales y visores web construidos con bibliotecas como **OpenLayers** o **Leaflet**; no requieren instalar software.
- **Clientes pesados**: los SIG de escritorio (QGIS, gvSIG, ArcGIS; tema 62), que consumen los servicios de la IDE como capas remotas.
- **Formatos de intercambio**: **GML** (Geography Markup Language, XML del OGC, norma **ISO 19136**) para objetos geográficos, además de GeoJSON en entornos web.

## Servicios web: WMS, WFS y CSW

Los servicios web de una IDE siguen una arquitectura orientada a servicios (SOA) con interfaces estandarizadas por el OGC. La LISIGE (art. 11) obliga a las Administraciones a gestionar una red con cinco tipos de servicios: **localización** (búsqueda mediante metadatos), **visualización** (mostrar, navegar, superponer datos y consultar leyendas), **descarga** (obtener copias de los datos o acceder a su contenido), **transformación** (adaptar los datos para su interoperabilidad) y **provisión de acceso** a los anteriores.

- **Servicios de visualización**:
    - **WMS (Web Map Service)**: genera al vuelo imágenes de mapa georreferenciadas a partir de los datos. Versión **1.3.0**, adoptada como norma **ISO 19128**. Operaciones principales: GetCapabilities (describe el servicio), GetMap (devuelve la imagen) y GetFeatureInfo (consulta los atributos de un punto).
    - **WMTS (Web Map Tile Service)**: sirve teselas prerrenderizadas y cacheables; sacrifica flexibilidad por velocidad de carga.
- **Servicios de descarga**:
    - **WFS (Web Feature Service)**: acceso a los objetos geográficos vectoriales, codificados en GML; permite consulta por filtros y, en su variante transaccional (WFS-T), edición remota. Versión **2.0**, adoptada como **ISO 19142**.
    - **WCS (Web Coverage Service)**: análogo al WFS para coberturas raster (MDT, imágenes multibanda), con acceso a los valores originales, no a una imagen pintada.
- **Servicios de localización (catálogo)**:
    - **CSW (Catalogue Service for the Web)**: búsqueda y consulta de metadatos de datos y servicios por palabras clave, área geográfica, fecha, escala u organismo; es la interfaz que ofrecen los catálogos como GeoNetwork (versión más extendida: **2.0.2**).
- **Otros servicios OGC**:
    - **WPS (Web Processing Service)**: publicación y ejecución remota de geoprocesos (análisis, modelos) sobre datos georreferenciados.
    - **SOS (Sensor Observation Service)**: acceso a observaciones de redes de sensores (meteorología, calidad del aire).
    - **Nomenclátor (gazetteer)**: localiza un elemento geográfico a partir de su nombre (topónimo) y devuelve sus coordenadas.
- **OGC API**: familia moderna de especificaciones (OGC API Features, Maps, Tiles, Records) que reformula los servicios anteriores como APIs REST con JSON/GeoJSON; convive con los servicios clásicos y es la línea de evolución de las IDE.

## Marco normativo: INSPIRE y LISIGE

### Directiva 2007/2/CE (INSPIRE)

**Texto vigente con las modificaciones del Reglamento (UE) 2019/1010 y la Decisión (UE) 2024/2829.**

La **Directiva 2007/2/CE, de 14 de marzo de 2007** (INSPIRE, *Infrastructure for Spatial Information in Europe*), establece una infraestructura de información espacial en la Unión Europea orientada a las políticas de medio ambiente y a las que puedan incidir en él, construida sobre las infraestructuras de los Estados miembros.

- **Principios**: los datos se recogen una sola vez y se mantienen donde puedan gestionarse con mayor eficacia; deben poder combinarse sin fisuras entre fuentes y escalas; disponibles en condiciones que no restrinjan su uso extensivo; fáciles de localizar y de evaluar para cada necesidad.
- **Ámbito**: **34 temas** de datos espaciales repartidos en sus anexos: **Anexo I** (9 temas: sistemas de referencia, cuadrículas, nombres geográficos, unidades administrativas, direcciones, parcelas catastrales, redes de transporte, hidrografía, lugares protegidos), **Anexo II** (4 temas: elevaciones, cubierta terrestre, ortoimágenes, geología) y **Anexo III** (21 temas ambientales y socioeconómicos).
- **Obligaciones**: crear metadatos, armonizar los datos y establecer servicios de red de localización, visualización, descarga y transformación, accesibles a través del **Geoportal INSPIRE** de la UE.
- **Normas de ejecución** (reglamentos directamente aplicables): **Reglamento (CE) 1205/2008** (metadatos), **Reglamento (CE) 976/2009** (servicios de red) y **Reglamento (UE) 1089/2010** (interoperabilidad de conjuntos y servicios de datos espaciales).
- **Modificaciones**: el **Reglamento (UE) 2019/1010** (arts. 21 y 23: seguimiento e informes) y la **Decisión (UE) 2024/2829, de 23 de octubre**, que simplifica las obligaciones de presentación de información. La directiva está además en proceso de revisión dentro de la iniciativa **GreenData4All** de la Estrategia Europea de Datos, sin propuesta aprobada a julio de 2026.

### Ley 14/2010, sobre las infraestructuras y los servicios de información geográfica en España (LISIGE)

**Texto consolidado a 24 de mayo de 2018.**

La **Ley 14/2010, de 5 de julio (LISIGE)** transpone la Directiva INSPIRE y complementa la organización de los servicios de información geográfica, en el marco definido junto con la **Ley 7/1986, de Ordenación de la Cartografía**. Su única modificación es la de la **Ley 2/2018, de 23 de mayo** (arts. 2.5, 3.1.a, 4.2, 6.2 y Anexo I).

- **Objeto (art. 1)**: fijar «las normas generales para el establecimiento de infraestructuras de información geográfica en España orientadas a facilitar la aplicación de políticas basadas en la información geográfica», especialmente las de medio ambiente. La **Infraestructura de Información Geográfica de España** la constituyen las infraestructuras y servicios interoperables de información geográfica sobre el territorio nacional, el mar territorial, la zona contigua, la plataforma continental y la zona económica exclusiva.
- **Ámbito subjetivo (art. 2)**: las Administraciones y organismos del sector público (los definidos en la Ley 37/2007, de reutilización); también quienes participen en funciones públicas o servicios públicos relacionados con el medio ambiente. Es «tercero» cualquier otra persona física o jurídica.
- **Estructura**: 5 capítulos (disposiciones generales; coordinación y dirección; datos y servicios; infraestructura de la AGE; organización de los servicios de información geográfica) y **3 anexos**.
- **Gobernanza**:
    - El **Consejo Superior Geográfico** (art. 19) es el órgano colegiado de dirección del Sistema Cartográfico Nacional, adscrito al Ministerio de Fomento (hoy Transportes y Movilidad Sostenible), con función consultiva y de planificación de la información geográfica y la cartografía oficial. Dirige y coordina la Infraestructura de Información Geográfica de España y es el **punto de contacto con la Comisión Europea** para INSPIRE (art. 4).
    - El **Consejo Directivo de la Infraestructura de Información Geográfica de España (CODIIGE)** (art. 4.3) reúne a los tres niveles de administración y expertos, y coordina técnicamente la infraestructura.
    - La **Secretaría Técnica** del Consejo la ejerce la **Dirección General del Instituto Geográfico Nacional**.
- **Geoportal IDEE (art. 5)**: la DG del IGN constituye y mantiene el **Geoportal de la Infraestructura de Datos Espaciales de España** (idee.es); todos los nodos de las Administraciones deben ser accesibles a través de él, y sirve de punto de acceso nacional a efectos de la Directiva.
- **Metadatos (arts. 9-10)**: las Administraciones deben crear y actualizar metadatos de los datos y servicios de los tres anexos (conformidad, condiciones de acceso, calidad, responsable, limitaciones), en los plazos de las normas de ejecución de INSPIRE.
- **Acceso (art. 13)**: el acceso a los servicios es público, con limitaciones tasadas (confidencialidad, defensa, seguridad pública, propiedad intelectual, datos personales, protección ambiental).
- **Anexos**:
    - **Anexo I. Información Geográfica de Referencia**: el **Equipamiento Geográfico de Referencia Nacional** (sistema de referencia geodésico, sistema oficial de coordenadas, cuadrículas, toponimia del **Nomenclátor Geográfico Básico de España**, delimitaciones territoriales del Registro Central de Cartografía, inventario de referencias municipales), la **parcela catastral**, altimetría y modelos digitales de elevaciones, redes de transporte, hidrografía, ocupación del suelo, direcciones y entidades de población.
    - **Anexo II. Datos Temáticos Fundamentales**: 21 temas (unidades estadísticas, edificios, suelo y usos del suelo, salud, servicios públicos, demografía, zonas de riesgo, meteorología, hábitats y biotopos, energía y recursos minerales, entre otros).
    - **Anexo III. Datos Temáticos Generales**: la cartografía temática militar, aeronáutica, forestal o agrícola, estadística y urbanística.
- **Sistema Cartográfico Nacional (art. 17)**: modelo de actuación que coordina a los operadores públicos con competencias cartográficas. Sus instrumentos: el Equipamiento Geográfico de Referencia Nacional, el **Plan Cartográfico Nacional**, el **Registro Central de Cartografía**, la propia Infraestructura de Información Geográfica de España y el Consejo Superior Geográfico. La AGE forma parte de él; las comunidades autónomas y entidades locales se integran voluntariamente. Lo desarrolla el **RD 1545/2007, de 23 de noviembre** (vigente, sin modificaciones).

### El despliegue: IDEE e IDEV

- **IDEE (Infraestructura de Datos Espaciales de España)**: integra los nodos IDE de la AGE, las comunidades autónomas y las entidades locales. Su geoportal (idee.es), mantenido por el **IGN/CNIG**, ofrece catálogo de metadatos, visor, nomenclátor y directorio de servicios de todos los nodos.
- **IDEV (Infraestructura Valenciana de Dades Espacials)**: la IDE de la Comunitat Valenciana, gestionada por el **Institut Cartogràfic Valencià (ICV)** a través del geoportal **idev.gva.es**: visor cartográfico, catálogo de metadatos (GeoNetwork), nomenclátor y servicios **WMS, WMTS, WFS, WPS y CSW** sobre la información geográfica del territorio valenciano. Es el nodo valenciano de la IDEE y cumple las normas de ejecución INSPIRE.

## Fuentes {.unnumbered .unlisted}

- Ley 14/2010, de 5 de julio, sobre las infraestructuras y los servicios de información geográfica en España (texto consolidado, última modificación 24 de mayo de 2018; contrastado online en julio de 2026).
- Directiva 2007/2/CE (INSPIRE), texto vigente con las modificaciones del Reglamento (UE) 2019/1010 y la Decisión (UE) 2024/2829 (EUR-Lex, contrastada online en julio de 2026).
- Reglamentos (CE) 1205/2008 (metadatos), (CE) 976/2009 (servicios de red) y (UE) 1089/2010 (interoperabilidad).
- Real Decreto 1545/2007, de 23 de noviembre, del Sistema Cartográfico Nacional (sin modificaciones; contrastado online).
- Estándares OGC/ISO: WMS 1.3.0 (ISO 19128), WFS 2.0 (ISO 19142), GML (ISO 19136), ISO 19115 (metadatos).
- Geoportales oficiales idee.es (IGN/CNIG) e idev.gva.es (ICV) (consulta: julio de 2026).
