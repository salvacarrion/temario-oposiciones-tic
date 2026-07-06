# Infraestructuras de datos espaciales

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Definición y Componentes. Arquitectura y Servicios Web de una IDE

**Infraestructuras de Datos Espaciales (IDE):** Son plataformas de interoperabilidad diseñadas para compartir información geográfica de forma eficiente. Integran datos espaciales de diferentes organismos mediante tecnologías, políticas, acuerdos institucionales, datos y servicios estandarizados, facilitando su acceso, manejo, intercambio y distribución a través de Internet.

### Características Principales de una IDE

- **Geoportal o Sitio Web**: Se materializan a través de un portal que ofrece aplicaciones de visualización, catálogos y nomenclátores.
- **Interoperabilidad**: Integran información espacial de diversos orígenes, garantizando su compatibilidad.
- **Accesibilidad**: Permiten el acceso público a datos geográficos actualizados y de calidad.

### Componentes de una IDE

- **Componentes Geográficos**:
    - **Datos**:
        - **De Referencia**: Cartografía, fotografías aéreas, modelos digitales del terreno.
        - **Temáticos**: Información sobre clima, suelo, población, etc.
    - **Metadatos**: Descripciones detalladas que proporcionan información sobre los datos, como su origen, formato, calidad y restricciones de uso.
- **Componentes Tecnológicos**:
    - **Estándares**:
        - **OGC (Open Geospatial Consortium)**: Organismo que desarrolla especificaciones para asegurar la interoperabilidad.
        - **ISO**: Estándares internacionales para la información geográfica.
        - **Grupo de Trabajo IDEE**: En España, coordina la implementación de estándares en las IDE.
    - **Servicios**:
        - **WMS (Web Map Service)**: Proporciona imágenes de mapas georreferenciados.
        - **WMTS (Web Map Tile Service)**: Ofrece mapas mediante teselas para una carga más rápida.
        - **WFS (Web Feature Service)**: Permite el acceso y manipulación de datos vectoriales en formato **GML (Geography Markup Language)**.
        - **WCS (Web Coverage Service)**: Proporciona acceso a datos raster, como imágenes satelitales.
        - **CSW (Catalog Service for the Web)**: Facilita la búsqueda y consulta de metadatos.
        - **Gazetteer (Servicio de Nomenclátor)**: Localiza elementos geográficos por su nombre.
    - **Infraestructura de Comunicaciones**: Red de Internet que soporta la transferencia y acceso a los datos geoespaciales.
- **Componentes Políticos**:
    - **Políticas y Normativas**: Regulaciones que establecen cómo se recolectan, mantienen y usan los datos geográficos.
    - **Acuerdos Institucionales**: Colaboración entre entidades para compartir y gestionar información espacial.
- **Componentes Sociales**:
    - **Usuarios**: Comunidad de profesionales, instituciones y público en general que utilizan y contribuyen a la IDE.

### Legislación Relacionada

- **Directiva INSPIRE**: Norma europea que establece una infraestructura de datos espaciales común en la Unión Europea.
- **Ley 14/2010 (LISIGE)**: Transpone la Directiva INSPIRE al marco legal español, regulando la infraestructura de información geográfica en España.
- **Sistema Cartográfico Nacional (SCN)**: La Generalitat Valenciana se integra en este sistema para coordinar la información geográfica a nivel nacional.

### IDE en España y la Comunitat Valenciana

- **Infraestructura de Datos Espaciales de España (IDEE)**:
    - Integra datos, metadatos y servicios geográficos producidos en España.
    - Gestionada por la **Dirección General del Instituto Geográfico Nacional**.
    - Ofrece un geoportal que centraliza el acceso a la información geoespacial.
- **Infraestructura de Datos Espaciales de la Comunitat Valenciana (IDECV)**:
    - Plataforma que promueve la cooperación entre entidades públicas y privadas para hacer accesible la información geográfica del territorio valenciano.
    - Gestionada por el **Institut Cartogràfic Valencià**.

### Arquitectura de una IDE

La arquitectura de una IDE se basa en el modelo **Cliente-Servidor** y utiliza estándares abiertos para garantizar la interoperabilidad.

- **Tecnologías Utilizadas**:
    - **XML**: Lenguaje utilizado para la descripción de servicios web y metadatos.
    - **GML**: Basado en XML, describe objetos geográficos para facilitar su intercambio.
- **Bases de Datos**:
    - Almacenan información cartográfica, datos alfanuméricos, imágenes y metadatos geoespaciales.
- **Servicios Web**:
    - **WMS, WFS, WCS, CSW**, entre otros, que permiten el acceso y manipulación de datos geográficos.
- **Tipos de Clientes**:
    - **Clientes Pesados**: Software de escritorio como ArcGIS, gvSIG, QGIS, que ofrecen funcionalidades avanzadas de SIG.
    - **Clientes Ligeros**: Geoportales y visores web que permiten acceder a la información geográfica sin necesidad de instalar software especializado.

### Servicios Web de una IDE

Los servicios web de una IDE están basados en una arquitectura orientada a servicios (**SOA**) y utilizan interfaces estandarizadas para asegurar la interoperabilidad.

- **Servicios de Visualización (de mapas e imágenes)**:
    - **WMS**: Genera imágenes de mapas a partir de datos geográficos.
    - **WMTS**: Mejora la velocidad de carga mediante el uso de teselas pre-renderizadas.
- **Servicios de Catálogo (de metadatos)**:
    - **CSW**: Permite buscar y acceder a metadatos de datos y servicios geográficos, facilitando su localización por temas, palabras clave, área geográfica, fecha, formato, escala u organización.
- **Servicios de Descarga (de objetos geográficos)**:
    - **WFS**: Proporciona acceso directo a datos vectoriales, permitiendo su consulta y edición.
    - **WCS**: Similar al WFS, pero para datos raster, como imágenes y coberturas.
- **Servicios de Geoprocesamiento**:
    - **WPS (Web Processing Service)**: Define una interfaz estándar para publicar y ejecutar procesos geoespaciales, como análisis y modelos, sobre datos georreferenciados.
- **Servicios de Observación (de Sensores)**:
    - **SOS (Sensor Observation Service)**: Facilita el acceso a datos de sensores, permitiendo solicitar, filtrar y recuperar observaciones y descripciones de sistemas de sensores.
- **Servicio de Nomenclátor**:
    - **Gazetteer**: Permite encontrar la ubicación geográfica de un lugar a partir de su nombre, proporcionando sus coordenadas y otra información relevante.

### Aplicaciones Geoespaciales Asociadas

- **Clientes SIG de Escritorio**:
    - **ArcGIS**, **gvSIG**, **QGIS**, **Geomedia**: Herramientas avanzadas para el análisis y gestión de datos geoespaciales.
- **Aplicaciones SIG en la Nube**:
    - **ArcGIS Online**, **CartoDB**, **MapBox**, **My Maps**: Plataformas que ofrecen funcionalidades SIG a través de servicios web.
- **Clientes Ligeros Web**:
    - **OpenLayers**, **MapBender**, **MapFish**: Frameworks y bibliotecas para desarrollar aplicaciones web de mapas.
- **Bases de Datos Geográficas**:
    - **ArcSDE**, **PostGIS**, **MySQL Spatial**: Sistemas de gestión de bases de datos que soportan datos espaciales.
- **Servidores Web Geoespaciales**:
    - **ArcGIS for Server**, **MapServer**, **MapGuide**, **GeoServer**: Software que permite publicar y administrar servicios web geoespaciales.
- **Catálogos de Metadatos**:
    - **GeoNetwork**, **PyCSW**: Aplicaciones para la gestión y distribución de metadatos geográficos.
- **Bibliotecas Geoespaciales**:
    - **GDAL (Geospatial Data Abstraction Library)**, **Sextante**: Conjuntos de herramientas para el procesamiento y análisis de datos geoespaciales.
