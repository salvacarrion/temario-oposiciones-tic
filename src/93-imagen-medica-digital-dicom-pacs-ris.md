# Imagen médica digital: DICOM, PACS y RIS

La imagen médica (radiología, TC, resonancia, ecografía, medicina nuclear) es el mayor volumen de datos clínicos de un hospital. Su ecosistema digital se sostiene sobre un estándar, **DICOM**, y dos sistemas: el **PACS**, que archiva y distribuye las imágenes, y el **RIS**, que gestiona el flujo de trabajo del servicio de radiología.

## DICOM: el estándar de la imagen médica

**DICOM** (*Digital Imaging and Communications in Medicine*) nace del comité conjunto **ACR-NEMA** (primera versión en 1983; la tercera versión, de **1993**, adopta el nombre DICOM y es la base de la actual). Lo mantiene NEMA/MITA como la serie **PS3** (una veintena de partes), con **varias ediciones al año** (edición vigente: **2026**); está adoptado como **ISO 12052**. Define a la vez el **formato de los objetos** (imágenes y metadatos), los **servicios de red** para intercambiarlos y el **soporte físico** de almacenamiento.

- **Modelo de información**: jerarquía de cuatro niveles **paciente → estudio → serie → objeto** (instancia). Un estudio es una exploración (un TC de tórax); una serie, cada conjunto de imágenes adquiridas juntas; el objeto, cada imagen o documento individual. Cada nivel se identifica con un **UID** único.
- **Atributos y etiquetas**: cada objeto DICOM lleva sus metadatos embebidos como atributos identificados por una etiqueta `(grupo, elemento)`: por ejemplo, `(0010,0010)` es el nombre del paciente y `(0008,0060)` la modalidad. El conjunto de atributos que define un tipo de objeto es su **IOD** (*Information Object Definition*).
- **Clases SOP**: la unidad funcional de DICOM es la **clase SOP** (*Service-Object Pair*): la combinación de un objeto (IOD) con un servicio (por ejemplo, «almacenamiento de imagen de TC»). Los equipos actúan como **SCU** (*Service Class User*, quien pide el servicio) o **SCP** (*Service Class Provider*, quien lo presta), y declaran qué clases SOP soportan en su **declaración de conformidad** (*conformance statement*), el documento que se revisa antes de integrar cualquier equipo.

## Intercambio de mensajes: los servicios DIMSE

Sobre una asociación de red DICOM, los equipos intercambian comandos **DIMSE** (*DICOM Message Service Element*):

| Servicio | Función |
| --- | --- |
| **C-ECHO** | Verificación de conectividad (el «ping» DICOM) |
| **C-STORE** | Envío de objetos (la modalidad guarda imágenes en el PACS) |
| **C-FIND** | Consulta (buscar estudios por paciente, fecha, modalidad) |
| **C-MOVE / C-GET** | Recuperación de objetos hacia un destino |
| **N-CREATE, N-SET…** | Servicios normalizados (gestión de listas de trabajo, impresión, MPPS) |

- **Flujo de trabajo**: la **Modality Worklist (MWL)** permite a la modalidad descargar del RIS la lista de pacientes citados con sus datos demográficos (evita teclearlos y garantiza identificadores correctos); el **MPPS** (*Modality Performed Procedure Step*) comunica el inicio y fin real de cada exploración.
- **Sintaxis de transferencia**: cada asociación negocia cómo se codifican los datos, incluida la **compresión** (JPEG, JPEG 2000, JPEG-LS, RLE), con o sin pérdida según el uso diagnóstico.
- **Soportes**: la parte 10 define el formato de fichero DICOM y el índice **DICOMDIR** para soportes de intercambio (el clásico CD de imagen que se entrega al paciente).

## DICOMweb: los servicios web

**DICOMweb** es la familia de servicios **REST** de DICOM, pensada para visores web, aplicaciones móviles y arquitecturas en la nube. Sus tres servicios principales son simétricos a los DIMSE:

| Servicio | Equivalente | Función |
| --- | --- | --- |
| **QIDO-RS** | C-FIND | Consulta de estudios/series/instancias (respuesta JSON) |
| **WADO-RS** | C-MOVE/C-GET | Recuperación de objetos, metadatos o renderizados |
| **STOW-RS** | C-STORE | Almacenamiento de objetos vía HTTP POST |

El precursor fue **WADO-URI** (recuperación de una imagen por URL). DICOMweb convive con DIMSE: dentro del hospital domina DIMSE; hacia el exterior (portales de paciente, telerradiología, integración con la HCE) se imponen los servicios web.

## PACS y RIS: los sistemas de imagen

- **PACS** (*Picture Archiving and Communication System*): sistema que **recibe, archiva, distribuye y presenta** las imágenes. Componentes: pasarelas de adquisición desde las modalidades, archivo (en línea y de largo plazo), base de datos de estudios, y estaciones de visualización (diagnósticas, de altas prestaciones, y clínicas, de consulta).
- **VNA** (*Vendor Neutral Archive*): archivo de imagen **neutral respecto al proveedor**, en formatos estándar, que consolida las imágenes de varios PACS o departamentos (incluida la imagen no radiológica: dermatología, endoscopia, anatomía patológica) y evita la dependencia del fabricante del PACS.
- **RIS** (*Radiology Information System*): gestiona el **flujo de trabajo administrativo y clínico** de radiología: agenda y citación, recepción de peticiones, listas de trabajo, dictado e **informe radiológico**, y estadísticas de actividad.
- **Integración RIS-PACS-HIS**: el ciclo completo de una exploración (perfil IHE **Scheduled Workflow**, tema [92](92-normalizacion-en-informatica-sanitaria.md)) encadena los tres sistemas:
    1. El médico solicita la exploración en el HIS/HCE (petición electrónica).
    2. El RIS recibe la petición y **cita** al paciente.
    3. La modalidad descarga la cita por **Modality Worklist** y adquiere las imágenes.
    4. Las imágenes se envían al **PACS** por C-STORE; el MPPS notifica la finalización.
    5. El radiólogo informa en el RIS con las imágenes del PACS en pantalla.
    6. El informe y el enlace a la imagen vuelven al HIS/HCE (mensajería HL7, tema [90](90-integracion-de-sistemas-sanitarios-y-mensajeria-hl7.md)) y quedan disponibles para el clínico peticionario.
- **Tendencias**: visores web «sin cliente» sobre DICOMweb, archivo en la nube, inteligencia artificial de ayuda al diagnóstico integrada en el flujo (remisión al tema [34](34-inteligencia-artificial.md); su encaje regulatorio como producto sanitario, en el tema [95](95-productos-sanitarios-mdr-ivdr-y-software-sanitario.md)).

## Fuentes {.unnumbered .unlisted}

- DICOM PS3, NEMA/MITA (ediciones continuas; edición vigente 2026, verificada online en julio de 2026); ISO 12052.
- DICOMweb: DICOM PS3.18 (servicios web QIDO-RS, WADO-RS, STOW-RS).
- IHE Radiology, perfil Scheduled Workflow (SWF).
