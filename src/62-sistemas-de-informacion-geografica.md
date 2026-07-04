# Sistemas de información geográfica
## Sistemas de Información Geográfica (SIG)

Son herramientas esenciales para la gestión y análisis de datos
geográficos, integrando información gráfica y alfanumérica. Estos
sistemas permiten trabajar con planos digitales y datos asociados,
ofreciendo múltiples funcionalidades y aplicaciones prácticas.

- **Concepto**: Sistemas diseñados para gestionar bases de datos
  geográficas, combinando mapas digitales con datos alfanuméricos.

- **Visualización y estructura**: Se asemejan a una serie de mapas
  superpuestos que representan diferentes capas de información
  (altitudes, redes fluviales, tipos de suelo, etc.).

- **Funcionalidades principales**:

  - Consulta y visualización de información geográfica.

  - Medición de distancias, áreas y perímetros.

  - Edición y actualización de datos.

  - Búsqueda y análisis espacial.

  - Explicación de fenómenos y predicción de sucesos.

  - Planificación estratégica y soporte en la toma de decisiones.

- **Problemas que resuelven**:

  - **Localización**: Identificación de la posición exacta de un objeto
    o fenómeno.

  - **Condiciones**: Determinación de características y atributos
    asociados a un lugar.

  - **Tendencias**: Análisis de cambios temporales en el espacio
    geográfico.

  - **Rutas**: Identificación de caminos óptimos.

  - **Pautas**: Detección de patrones espaciales y relaciones.

  - **Modelación**: Simulación de escenarios basados en datos
    geográficos.

**Datos en un SIG**

La información gestionada en los SIG se organiza según formatos y
representaciones específicas, dependiendo de su naturaleza y propósito.

- **Sistemas de coordenadas**:

  - Uso del **Sistema Universal Transversal de Mercator (UTM)**, que
    divide la Tierra en 60 husos de 6º de longitud. En la Comunidad
    Valenciana se utiliza el huso 30N.

  - Las coordenadas se expresan en metros y son precisas al nivel del
    mar.

- **Representación de objetos geográficos**:

  - **Modelo raster**: Divide el espacio en una matriz de celdas o
    píxeles. Usos: imágenes satelitales, modelos digitales del terreno
    (MDT), fotografías aéreas.

    - **Formatos comunes**: geoTIFF (.tif), Enhanced Compression Wavelet
      (.ecw), mrSID (.sid), imagen raster (.img), JPEG Georreferenciado
      (.jpg) y ESRI grid.

  - **Modelo vectorial**: Representa objetos mediante puntos, líneas y
    polígonos.

    - **Formatos comunes**: Shapefile (SHP), bases de datos espaciales
      (MySQL, Oracle Spatial), formatos CAD (DXF, DWG, DGN), Cobertura,
      GML/XML (Geography Markup Language), KML (Google Earth).

- **Fuentes de datos geográficos**:

  - **Fotogrametría**: Uso de drones o aviones para tomar imágenes
    aéreas.

  - **Teledetección**: Obtención de datos mediante sensores en satélites
    o aviones no tripulados.

  - **Institut Cartogràfic Valencià (ICV)**: Fuente principal de datos
    cartográficos en la Comunidad Valenciana.

**Proyecto gvSIG**

El **Proyecto gvSIG** es una iniciativa de la Generalitat Valenciana
para proporcionar herramientas SIG de código abierto adaptadas a las
necesidades de los usuarios.

- **Características destacadas**:

  - Portable y modular.

  - De código abierto, bajo licencia GPL.

  - Sin costos de licencias.

  - Interoperable con soluciones preexistentes.

  - Basado en estándares internacionales.

- **Plataformas disponibles**:

  - **gvSIG Desktop**: Herramienta para uso en ordenadores.

  - **gvSIG Mobile**: Versión optimizada para dispositivos móviles.

**Incorporación de la componente geográfica en los Sistemas de
Información**

La integración de datos geográficos en sistemas de información permite
ampliar sus capacidades y aplicaciones.

- **Geocodificación**: Proceso de asignar coordenadas geográficas a
  objetos previamente no georreferenciados. Se basa en direcciones u
  otros identificadores espaciales.

- **Datum geodésico**: Sistema de referencia que describe la forma y
  tamaño de la Tierra. Define un origen para los sistemas de coordenadas
  y permite una representación precisa del espacio geográfico.
