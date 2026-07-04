# Documento y expediente electrónico. Gestión documental

## Gestión Documental

La **gestión documental** consiste en controlar de manera eficiente y sistemática la creación, recepción, mantenimiento, utilización y disposición de los documentos. Esto abarca desde la generación hasta la eliminación o conservación permanente de los mismos, siguiendo políticas establecidas para asegurar su integridad y accesibilidad.

### Tratamiento de Imágenes y Proceso Electrónico de Documentos

El tratamiento de imágenes dentro del proceso electrónico de documentos incluye:

- **Digitalización**: Consiste en transformar un documento físico en un documento electrónico compuesto por una **imagen electrónica**, metadatos y, opcionalmente, una **firma electrónica**.
- **Imagen Electrónica**: Debe ser válida según las **Normas Técnicas de Interoperabilidad (NTIs)**.
- **Formatos Admitidos**: PNG, RTF, SVG o TIFF.
- **Resolución Mínima**: 200 ppp en blanco y negro, color o grises.
- **Requisitos Adicionales**: La imagen debe respetar la geometría del documento original y no incluir caracteres o gráficos no presentes en el documento fuente.
- **Proceso de Digitalización**: Debe ser automático para garantizar la integridad y evitar manipulación humana, abarcando captura, optimización, asignación de metadatos y firma electrónica si procede.
    - **Captura**: Mediante un proceso fotoeléctrico.
    - **Optimización**: Realizada si es necesario.
    - **Asignación de Metadatos**: Incluye información básica o complementaria como resolución, tamaño, idioma, etc.
    - **Firma Electrónica**: Si se aplica, el documento digitalizado puede sustituir legalmente al original, permitiendo su destrucción.

### Beneficios de la Digitalización

Los beneficios de la digitalización son de naturaleza estratégica, financiera y técnica, mejorando la eficiencia, reduciendo costos y facilitando el acceso y gestión de los documentos.

### Elementos del Sistema de Gestión Documental

Un **gestor documental** es una aplicación que facilita la generación, tratamiento, publicación y conservación de documentos electrónicos. Los elementos clave de un sistema de gestión documental incluyen:

- **Esquema o Cuadro de Clasificación**: Permite la identificación, clasificación y codificación de documentos y expedientes al ser recibidos o producidos.
- **Calendario de Conservación**: Define los periodos de conservación y el destino final de los documentos, determinando cuándo serán eliminados o conservados como archivos permanentes.
- **Sistema de Archivo Corporativo**: Repositorio para la ordenación y preservación de la documentación que no requiere disponibilidad inmediata.
- **Sistema de Acceso a la Información**: Facilita la localización y acceso a la documentación, controlando accesos y gestionando permisos.

**Tipos de Sistemas de Información Asociados**:

- **Modelos Relacionales**.
    - **Datacéntricos**: La información depende del sistema, por ejemplo, bases de datos.
    - **Docucéntricos**: Los documentos son independientes del sistema, como en Alfresco, donde se almacenan en el sistema de ficheros y se relacionan mediante metadatos en la base de datos.

### Productos de Gestión Documental Basados en Modelos Relacionales

- **Content Management Systems (CMS)**: Enfocados en la producción colaborativa de contenidos estructurados, como páginas web.
- **Document Management (DM)**: Administran el flujo de documentos dentro de una organización.
- **Records Management (RM)**: Gestionan registros que son evidencia de las actividades de una empresa.
- **Enterprise Content Management (ECM)**: Gestión global de contenidos que integra CMS, DM, RM, entre otros.

### Requisitos de un Sistema de Gestión Documental (SGD)

- **Metadatos**: Información adjunta a un documento que permite su identificación, autenticación y contextualización, regulados por normas técnicas como las NTIs.
- **Integración**: Debe integrarse con sistemas productores de documentos y sistemas de ficheros, como Microsoft SharePoint, utilizando protocolos como WebDAV, CIFS, NFS, IMAP, etc.
- **Otros Requisitos**: Incluyen indexación, almacenamiento, recuperación, colaboración (flujos de trabajo, control de versiones), publicación y seguridad.

### Gestión de Contenidos o Content Management System (CMS)

Un **CMS** es una aplicación que permite crear estructuras de soporte de información para la creación y gestión posterior de contenidos. Sus características incluyen:

- **Publicación Web**: Permite la difusión de contenidos a través de Internet.
- **Indexación, Revisión, Búsqueda y Recuperación**: Facilitan la gestión eficiente de la información.

### Partes de un CMS

- **Web Pública**: Accesible a través de una URL.
- **Web Privada**: Parte interna que incluye:
    - **CMA (Content Management Application)**: Permite crear, editar y eliminar contenidos.
    - **CDA (Content Dispensing Application)**: Compila y publica la información en el sitio web.

### Capas del CMS

La **renderización** de un gestor de contenidos se compone de varias capas:

- **Capa de Base de Datos**: Administración, permisos, usuarios, utilizando tecnologías como MySQL.
- **Capa de Programación**: Responde a peticiones y muestra información, utilizando tecnologías como PHP.
- **Capa de Diseño**: Maqueta la página con tecnologías como HTML y CSS.

### Tipos y ejemplos de CMS

Incluyen sistemas como:

- **Learn Management System (LMS)**: Ejemplo, Moodle.
- **Sistemas de Comercio Electrónico**: Ejemplo, Shopify.
- **Blogs, Foros, Wikis**.
- **Sistemas de Difusión de Contenidos Multimedia (DMS)**.

### Archivo Electrónico

Un **archivo electrónico** se encarga del almacenamiento, custodia y conservación de documentos generados electrónicamente, así como de su consulta y recuperación. El **ciclo de vida del documento** incluye todas las etapas desde su identificación hasta su conservación permanente o destrucción reglamentaria.

### Fases del Archivo

- **Fase 1: Archivo Activo o de Gestión**: Reúne documentación en trámite, sometida a uso y consulta administrativa continua. Los documentos están en el gestor documental.
- **Fase 2: Archivo Semi-activo, Central o Intermedio**: Coordina y controla los archivos de gestión, reuniendo documentos una vez finalizado su trámite.
- **Fase 3: Archivo Inactivo o Histórico**: Conserva permanentemente documentos de valor histórico, siguiendo políticas definidas para su preservación o expurgación.

### Fases del Ciclo Vital del Documento

- **Fase de Captura**: Incorporación del documento al sistema de gestión documental.
- **Fase de Mantenimiento y Uso**: Disponibilidad y validez administrativa de los documentos.
- **Fase de Conservación y Selección**: Eliminación reglamentaria de documentos efímeros y conservación de aquellos con valor a largo plazo.

### Archivo Electrónico Longevo

Un **archivo electrónico longevo** asegura el almacenamiento seguro, custodia, preservación, recuperación y consulta de documentos tras la finalización de sus fases activa y semi-activa.

### Roles y Responsabilidades en un Sistema de Gestión Documental

Incluyen la dirección, responsables de procesos de gestión, planificación, implantación y administración del programa de tratamiento de documentos, y responsables de las unidades administrativas que gestionan documentos electrónicos.

### Tipos de Sistemas de Gestión Documental Electrónica

- **Sistema de Gestión de Documentos Electrónicos (SGDE)**: Para documentos que aún no han alcanzado su estado definitivo, permitiendo modificaciones, versionado y borrado.
- **Sistemas de Gestión de Documentos Electrónicos de Archivo (SGDEA)/Archivos Electrónicos Longevos**: Para documentos en su forma definitiva, garantizando su inmutabilidad.

### Procesos de Gestión Documental y Archivo

Incluyen captura, registro, clasificación, descripción, acceso y trazabilidad, calificación, conservación, transferencia, destrucción y eliminación, asignación de metadatos, documentación, formación, supervisión y auditoría, y gestión de la política.

### Otros elementos de la gestión documental en la Adminsitración

### Portafirmas Electrónico

Es una herramienta para firmar electrónicamente documentos utilizando el certificado digital del firmante. **Port@firmas** es una aplicación que integra la firma electrónica en los flujos de trabajo de una organización, facilitando la autenticación y legalidad de los documentos electrónicos.

### CSV (Código Seguro de Verificación)

El **CSV** es un código único que identifica un documento electrónico, garantizando su integridad mediante el cotejo en las sedes electrónicas habilitadas, como Ministerios, Comunidades Autónomas y Entidades Locales.

### InSide (Infraestructuras y Sistemas para el Documento Electrónico)

**InSide** es un sistema para la gestión de documentos y expedientes electrónicos que cumple con los requisitos del ENI. Se utiliza en dos modos:

- **InSide Base**: Permite almacenar y modificar documentos y expedientes en gestores compatibles con el estándar CMIS, gestionando metadatos, asociaciones, índices, validaciones y firmas.
- **G-Inside (Generador de InSide)**: Servicios web en la nube para validar y generar documentos y expedientes según el ENI, incluyendo la generación de PDFs.

### Junta Calificadora de Documentos Administrativos (JCDA)

En la **Generalitat Valenciana (GVA)**, la JCDA dicta sobre la valoración, conservación y eliminación de documentos a conservar por los archivos longevos.

### OAIS (Open Archival Information System)

Es un modelo conceptual destinado a la gestión, archivo y preservación a largo plazo de documentos. Define las funciones, responsabilidades y organización necesarias para preservar la información y garantizar el acceso a una comunidad de usuarios.
