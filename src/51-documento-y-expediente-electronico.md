# Documento y expediente electrónico. Gestión documental

En la tramitación electrónica, el documento y el expediente dejan de ser objetos en papel y pasan a ser objetos digitales con requisitos jurídicos y técnicos propios: validez, firma, metadatos, formatos e intercambio. El marco lo forman las **Leyes 39/2015 y 40/2015**, el **Real Decreto 203/2021** (cuyo Título III regula el documento, las copias, el expediente y el archivo electrónico) y el **Esquema Nacional de Interoperabilidad (RD 4/2010)** con sus Normas Técnicas de Interoperabilidad (NTI). El ENI y el conjunto de las 12 NTI se estudian en su propio tema; la identificación y la firma electrónica, en el suyo.

**Leyes 39/2015 y 40/2015: textos consolidados a 6 de noviembre de 2024 y 2 de agosto de 2024. RD 203/2021: texto consolidado a 2 de abril de 2025. NTI de Documento, Expediente, Digitalización y Copiado auténtico (2011) y de Política de gestión de documentos electrónicos (2012): sin modificaciones.**

## Documento y expediente electrónico

La ley define qué documentos son válidos y cómo se forma el expediente; las NTI concretan sus componentes, estructura y metadatos para que puedan intercambiarse y conservarse entre Administraciones.

### Documento administrativo electrónico

- **Documento público administrativo (art. 26.1 Ley 39/2015)**: «los válidamente emitidos por los órganos de las Administraciones Públicas». Se emiten «por escrito, a través de medios electrónicos, a menos que su naturaleza exija otra forma más adecuada de expresión y constancia».
- **Documento administrativo electrónico (art. 46 RD 203/2021)**: información de cualquier naturaleza en forma electrónica, archivada en un soporte electrónico según un formato determinado susceptible de identificación y tratamiento diferenciado admitido en el ENI, generada, recibida o incorporada por las Administraciones Públicas en el ejercicio de funciones sujetas a Derecho administrativo. La entrega de un ejemplar puede sustituirse por los **datos necesarios para su acceso** por medios electrónicos.
- **Requisitos de validez (art. 26.2 Ley 39/2015)**, todos los siguientes:
    - Contener información de cualquier naturaleza archivada en un soporte electrónico según un formato determinado susceptible de identificación y tratamiento diferenciado.
    - Disponer de los **datos de identificación** que permitan su individualización, sin perjuicio de su posible incorporación a un expediente electrónico.
    - Incorporar una **referencia temporal** del momento en que han sido emitidos.
    - Incorporar los **metadatos mínimos** exigidos.
    - Incorporar las **firmas electrónicas** que correspondan de acuerdo con la normativa aplicable.
- **Excepción de firma (art. 26.3)**: no requieren firma electrónica los documentos publicados con carácter **meramente informativo** y los que **no formen parte de un expediente administrativo**; en todo caso habrá que identificar su origen.
- **Componentes (NTI de Documento electrónico)**: el **contenido** (conjunto de datos o información del documento), la **firma electrónica** (en su caso) y los **metadatos**. Los documentos administrativos electrónicos, y los susceptibles de formar parte de un expediente, tendrán **siempre asociada al menos una firma electrónica**.
- **Referencia temporal (art. 50 RD 203/2021)**: dos modalidades según determinen las normas del procedimiento: **marca de tiempo** (asignación de fecha, y en su caso hora, por medios electrónicos; es la regla general) o **sello electrónico cualificado de tiempo** (con intervención de un prestador cualificado de servicios de confianza; los sellos no cualificados se asimilan a marcas de tiempo).
- **Formato (NTI)**: los ficheros de contenido se ajustan a los formatos de la **NTI de Catálogo de estándares**, eligiendo según la naturaleza de la información; cabe usar otros formatos cuando existan particularidades que lo justifiquen o para asegurar el valor probatorio del documento.
- **Intercambio (NTI)**: se realiza según la estructura XML de su anexo II; excepcionalmente caben otras estructuras por acuerdo previo entre Administraciones (convirtiéndolas a la estructura común si el destinatario es un tercero). Si el intercambio supone **transferencia de custodia** de documentos de conservación permanente, el transferidor verifica antes su autenticidad e integridad.
- **Acceso (NTI)**: al facilitar el acceso por sede electrónica se muestra el contenido (si es representable), la **información básica de cada firma** y la descripción y valor de los **metadatos mínimos obligatorios**.

### Expediente administrativo electrónico

- **Definición (art. 70.1 Ley 39/2015)**: «el conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolución administrativa, así como las diligencias encaminadas a ejecutarla».
- **Formación (art. 70.2)**: los expedientes «tendrán formato electrónico» y se forman mediante la **agregación ordenada** de cuantos documentos, pruebas, dictámenes, informes, acuerdos, notificaciones y demás diligencias deban integrarlos, más un **índice numerado** de todos los documentos cuando se remita. Debe constar la **copia electrónica certificada de la resolución** adoptada.
- **No forma parte del expediente (art. 70.4)**: la información de carácter **auxiliar o de apoyo** (aplicaciones, ficheros y bases de datos, notas, borradores, opiniones, resúmenes, comunicaciones e informes internos o entre órganos, juicios de valor), salvo los informes preceptivos y facultativos solicitados antes de la resolución.
- **Remisión (art. 70.3)**: conforme al ENI y sus NTI, el expediente se envía **completo, foliado, autentificado y con un índice, asimismo autentificado**; la autenticación del índice garantiza la **integridad e inmutabilidad** del expediente y permite su recuperación. Un mismo documento puede formar parte de **distintos expedientes electrónicos**.
- **Componentes (NTI de Expediente electrónico)**: los **documentos electrónicos** (organizados directamente o dentro de carpetas o subexpedientes), el **índice electrónico**, la **firma del índice** por la Administración actuante y los **metadatos** del expediente.
- **Índice electrónico (art. 51 RD 203/2021)**: el foliado se realiza mediante un índice electrónico autenticado que garantiza la integridad y permite la recuperación. Lo firma el **titular del órgano** que conforme el expediente, o se **sella electrónicamente** cuando el expediente se forme de manera automática. En el intercambio, el índice refleja al menos la **fecha de generación** y, por cada documento indizado, su **identificador**, la **huella digital** y la **función resumen** utilizada (opcionalmente, fecha de incorporación y orden), además de la disposición en carpetas o subexpedientes.
- **Estados del expediente (metadato NTI)**: **E01** abierto, **E02** cerrado y **E03** índice para remisión cerrado.
- **Acceso al expediente (art. 52 RD 203/2021)**: el derecho de acceso del interesado (art. 53.1.a Ley 39/2015) se entiende satisfecho con la **puesta a disposición** del expediente en el Punto de Acceso General electrónico o en la sede electrónica, remitiéndole la **dirección electrónica o localizador**; el acceso se garantiza durante el tiempo que fije la política de gestión de documentos conforme al dictamen de la autoridad calificadora.

### Metadatos: de las NTI al e-EMGDE

- **Metadato (anexo ENI)**: «dato que define y describe otros datos». El **metadato de gestión de documentos** es la información estructurada o semiestructurada que hace posible la creación, gestión y uso de documentos a lo largo del tiempo, y sirve para **identificar, autenticar y contextualizar** documentos, personas, procesos y sistemas.
- **Metadatos mínimos obligatorios (anexo I de las NTI)**: el documento electrónico lleva versión NTI, identificador normalizado, órgano (código **DIR3**), fecha de captura, origen (**0** ciudadano, **1** administración), estado de elaboración, nombre de formato, tipo documental y tipo de firma; el expediente lleva versión NTI, identificador, órgano, fecha de apertura, clasificación (código **SIA**), estado, interesado y tipo de firma del índice. Su detalle tabulado se estudia en el tema del ENI.
- **Reglas de gestión (NTI de Documento electrónico)**: los metadatos mínimos están presentes en **cualquier proceso de intercambio** y **no se modifican en ninguna fase posterior** del procedimiento, salvo corrección de errores u omisiones en el valor inicial; pueden asignarse **metadatos complementarios** para necesidades de descripción específicas.
- **Estado de elaboración (valores)**: original; copia electrónica auténtica con cambio de formato; copia electrónica auténtica de documento papel; copia electrónica parcial auténtica; otros.
- **Esquema de Metadatos para la Gestión del Documento Electrónico (e-EMGDE)**: esquema de referencia que recomienda la NTI de Política de gestión de documentos electrónicos para adecuarse a los requisitos de interoperabilidad en gestión documental. Incluye los metadatos mínimos de las NTI más los complementarios de una política de gestión y conservación. Publicado en el PAe por la **Agencia Estatal de Administración Digital (AEAD)**; la versión vigente es la **3.1 (junio de 2025)**, tras la 1.ª (2012), la 2.0 (2016) y la 3.0 (diciembre de 2023).
- **Modelo conceptual multientidad del e-EMGDE**: los metadatos no describen solo documentos, sino cinco tipos de entidad interrelacionados:

| Entidad | Descripción |
| --- | --- |
| **Documento** | Información estructurada en cualquier formato, creada, recibida y mantenida como evidencia por una organización o persona en cumplimiento de obligaciones legales o para actuaciones de gestión |
| **Agente** | Institución o persona física o jurídica responsable o involucrada en la creación, producción, custodia o gestión de documentos |
| **Actividad** | Responsabilidad ejecutada por o asignada a una entidad Agente |
| **Regulación** | Marco normativo, incluidos los requisitos de gestión de documentos (ordenamiento jurídico, normativa, política...) |
| **Relación** | Asociación entre dos o más entidades con relevancia en un contexto de gestión o de gestión de documentos |

- **Elementos de metadatos**: se numeran eEMGDE0 a eEMGDE31; ejemplos preguntables: eEMGDE8-Seguridad (con datos personales y **categoría ENS**), eEMGDE13-Calificación (documentos esenciales, valoración y dictamen), eEMGDE18-Tipo documental, eEMGDE21-Trazabilidad y eEMGDE22-Clasificación.

### Digitalización de documentos

- **Definición (art. 27.3.b Ley 39/2015)**: «el proceso tecnológico que permite convertir un documento en soporte papel o en otro soporte no electrónico en un fichero electrónico que contiene la imagen codificada, fiel e íntegra del documento».
- **Componentes del documento digitalizado (NTI de Digitalización de documentos)**: la **imagen electrónica**, los **metadatos** mínimos obligatorios (y complementarios, en su caso) y, si procede, la **firma** de la imagen. Para que además sea **copia auténtica** deben cumplirse los requisitos de la NTI de copiado auténtico.
- **Requisitos de la imagen electrónica**: aplica los formatos establecidos para **ficheros de imagen** en la NTI de Catálogo de estándares (PDF, PDF/A, PNG, JPEG, TIFF, SVG...); nivel de **resolución mínimo de 200 píxeles por pulgada** en blanco y negro, color o escala de grises; **imagen fiel**: respeta la geometría del documento origen (tamaños y proporciones) y no contiene caracteres o gráficos que no figurasen en él.
- **Proceso de digitalización**: proceso informático que garantiza la integridad de cada paso: digitalización por **medio fotoeléctrico**; si procede, **optimización automática** de la imagen para garantizar su legibilidad (umbralización, reorientación, eliminación de bordes); **asignación de metadatos**; y, si procede, **firma** de la imagen. Incluye operaciones de **mantenimiento preventivo** y comprobaciones rutinarias que aseguren que los dispositivos producen imágenes fieles.

## Copia auténtica, código seguro de verificación y portafirmas

Las copias auténticas sustituyen al cotejo tradicional: cualquier Administración puede generar copias con la misma validez que el original, y el CSV permite verificar en sede la autenticidad de las que circulan impresas.

### Copias auténticas

- **Concepto (art. 27.2 Ley 39/2015 y art. 47 RD 203/2021)**: copia, cualquiera que sea su soporte, realizada por los órganos competentes de las Administraciones Públicas «en las que quede garantizada la identidad del órgano que ha realizado la copia y su contenido». Tienen la **misma validez y eficacia que los documentos originales** y se expiden **siempre a partir de un original o de otra copia auténtica**.
- **Eficacia**: las realizadas por una Administración valen en las restantes; las copias auténticas de **documentos privados** surten «únicamente efectos administrativos».
- **Expedición**: mediante **funcionario habilitado** (inscrito en un registro interoperable e interconectado) o mediante **actuación administrativa automatizada**. En el ámbito estatal (art. 48 RD 203/2021) son competentes los órganos que emitieron el original, los de custodia y archivo, los que prevean sus normas y las **oficinas de asistencia en materia de registros**.
- **Reglas según el soporte (art. 27.3 Ley 39/2015)**:
    - **Electrónica de documento electrónico**: con o sin cambio de formato; incluye metadatos que acrediten su condición de copia, visibles al consultarla.
    - **Electrónica de documento papel**: exige digitalización conforme a las NTI, más los metadatos de copia.
    - **Papel de documento electrónico**: debe figurar la condición de copia y un **código generado electrónicamente u otro sistema de verificación** que permita contrastar la autenticidad accediendo a los archivos electrónicos del emisor.
    - **Papel de original en papel**: copia auténtica en papel del documento electrónico en poder de la Administración, o puesta de manifiesto electrónica de la copia auténtica.
    - Las Administraciones publican en su sede los **códigos seguros de verificación** u otros sistemas de verificación utilizados.
- **Solicitud (art. 27.4)**: los interesados pueden pedir copias auténticas «en cualquier momento» al órgano que emitió el original, que las expide en el plazo de **15 días** desde la recepción de la solicitud en el registro (salvo las excepciones de la Ley 19/2013). Las Administraciones están **obligadas** a expedir copia auténtica electrónica de cualquier documento en papel que presenten los interesados y se vaya a incorporar a un expediente. Las copias de documentos notariales, registrales, judiciales y de los diarios oficiales se rigen por su legislación específica (art. 27.6).
- **Copias aportadas en papel (art. 49 RD 203/2021)**: si el interesado presenta en papel una **copia** (no un original), la digitalización genera una copia electrónica con «el mismo valor que la copia presentada en papel».
- **Tipos de copia (NTI de Procedimientos de copiado auténtico y conversión)**, reflejados en el metadato «Estado de elaboración»:

| Tipo | Obtención |
| --- | --- |
| **Copia electrónica auténtica con cambio de formato** | Conversión entre documentos electrónicos conforme a la propia NTI |
| **Copia electrónica auténtica de documento papel** | Digitalización según la NTI de Digitalización de documentos |
| **Copia electrónica parcial auténtica** | Extractos del contenido u otros métodos que preserven la confidencialidad de los datos que no afecten al interesado |
| **Copia papel auténtica de documento electrónico** | Según la normativa aplicable y el acceso a documentos de la NTI de Documento electrónico (verificación de autenticidad) |

- **Conversión entre documentos electrónicos (NTI)**: genera un **nuevo documento** con diferente formato o versión, aplicando procedimientos definidos en el marco de gestión documental, **conservando contenido, contexto y estructura** del origen, y eligiendo un formato del Catálogo de estándares que minimice la pérdida de información. La relación copia-origen se refleja en el metadato **«Identificador del documento origen»**.
- **Conservación y destrucción de lo presentado (art. 53 RD 203/2021)**: los documentos presentados en papel (o en dispositivo electrónico) que no puedan devolverse en el momento se conservan a disposición del interesado durante **6 meses** tras su digitalización o incorporación; después, su destrucción se realiza según las competencias en materia de cultura (estatal o autonómica) y **nunca** si tienen valor histórico o artístico o si las firmas u otras expresiones manuscritas les confieren un valor especial. Los originales que formen parte de expedientes y series de archivo se **restituyen a sus oficinas de origen**. La disposición transitoria 1.ª del RD 203/2021, que regulaba la destrucción de documentos en papel digitalizados, fue **anulada por la STS de 30 de mayo de 2022**. En la Generalitat, la destrucción exige dictamen de la Junta Qualificadora de Documents Administratius (tema de administración electrónica de la GVA).

### Código seguro de verificación (CSV)

- **Concepto (art. 42.b Ley 40/2015)**: sistema de firma para la **actuación administrativa automatizada**: código «vinculado a la Administración Pública, órgano, organismo público o entidad de Derecho Público», que permite «en todo caso la comprobación de la integridad del documento mediante el acceso a la sede electrónica correspondiente».
- **Garantías del sistema (art. 21.2 RD 203/2021)**:
    - El **origen e integridad** de los documentos mediante el acceso a la sede electrónica.
    - El **carácter único** del código generado para cada documento.
    - Su **vinculación** con el documento generado y, en su caso, con el firmante; el CSV y la dirección de la sede se integran **preferentemente en todas las páginas** del documento, y cualquier modificación da lugar a un nuevo documento con un CSV diferente.
    - La posibilidad de **verificar el documento en la sede** durante el plazo fijado, mediante un procedimiento **directo y gratuito**.
    - Un **acceso restringido** al documento a quien disponga del código.
- **Utilización en el ámbito estatal (art. 21.4)**: requiere resolución de la Subsecretaría del Ministerio (o presidencia/dirección del organismo), previo informe del **Centro Criptológico Nacional** y de la Administración digital estatal. La resolución fija las actuaciones, los órganos responsables, la sede de verificación y el **plazo de disponibilidad, al menos de 5 años**; transcurrido este, la verificación se solicita al órgano emisor.
- **Interoperabilidad (art. 21.3)**: en comunicaciones a otros órganos puede superponerse al CSV un **sello electrónico** como mecanismo de verificación automática de origen e integridad.

### Portafirmas electrónico

- **Concepto**: aplicación que organiza el **flujo de firma** de documentos en una organización: bandeja de solicitudes de firma o visto bueno, revisión del documento, firma individual o **en bloque**, delegación y sustitución de firmantes, y trazabilidad de cada petición. Se integra con las plataformas de firma electrónica (@firma, FIRe, AutoFirma), estudiadas en el tema de identificación y firma.
- **Port@firmas**: portafirmas electrónico de la suite @firma, ofrecido como servicio compartido reutilizable en el CTT por la **AEAD**.
- **GVA**: el **portafirmas corporativo** es servicio común del anexo I del Decreto 54/2025 (tema de administración electrónica de la GVA).

## Gestión documental y de contenidos

La gestión documental es el campo de gestión responsable del **control eficaz y sistemático** de la creación, recepción, mantenimiento, uso y disposición de los documentos, de modo que sirvan de **evidencia** de las actividades de la organización (UNE-ISO 15489-1:2016). En las Administraciones se instrumenta mediante una política de gestión de documentos electrónicos normalizada por el ENI.

### Política de gestión de documentos electrónicos (NTI)

La **NTI de Política de gestión de documentos electrónicos** (Resolución de 28 de junio de 2012) establece las directrices para definir políticas de gestión y conservación.

- **Contenido de la política**: definición de alcance y ámbito; **roles de los actores**; directrices para estructurar los procedimientos de gestión documental; acciones de **formación**; actuaciones de **supervisión y auditoría**; y proceso de **revisión** de la propia política.
- **Actores involucrados**: la **alta dirección** (aprueba e impulsa la política); los **responsables de los procesos de gestión** (la aplican en sus procesos); el **personal responsable del programa de tratamiento** (cualificado e instruido en gestión y conservación documental); y el **personal implicado** en tareas de gestión de documentos electrónicos.
- **Programa de tratamiento de documentos electrónicos**: concreta los procesos, técnicas y operaciones, y se aplica de manera **continua sobre todas las etapas del ciclo de vida** de documentos y expedientes, garantizando su **autenticidad, integridad, confidencialidad, disponibilidad y trazabilidad**, y la protección, recuperación y conservación física y lógica.
- **Procesos de gestión de documentos electrónicos** (mínimos):
    1. **Captura** (con los metadatos mínimos de la NTI de Documento electrónico).
    2. **Registro** (y digitalización de lo presentado en papel).
    3. **Clasificación** (formación de expedientes y clasificación funcional según el **cuadro de clasificación** de la organización).
    4. **Descripción** (asignación de metadatos; posible esquema institucional).
    5. **Acceso** (regulación y **trazabilidad** de las acciones sobre cada documento).
    6. **Calificación**: determinación de los **documentos esenciales**, **valoración** y plazos de conservación, y **dictamen de la autoridad calificadora**.
    7. **Conservación** según el valor y el dictamen, mediante **calendarios de conservación**.
    8. **Transferencia** entre repositorios, con sus responsabilidades de custodia.
    9. **Destrucción o eliminación**, conforme a la normativa de **Patrimonio Documental** y a las medidas del ENS de protección de soportes ([mp.si]) y limpieza de documentos ([mp.info]).
- **Instrumentos típicos del sistema de gestión documental**: el **cuadro de clasificación** (identificación y codificación funcional de documentos y expedientes), el **calendario de conservación** (períodos de conservación y destino final), el repositorio o archivo corporativo y el control de acceso a la información.

### Sistemas de gestión documental y de contenidos

- **Gestor documental (DMS, *Document Management System*)**: aplicación que da soporte al ciclo de vida del documento: captura e **indexación**, almacenamiento, búsqueda y recuperación, **control de versiones**, flujos de trabajo (*workflow*), seguridad y auditoría, y publicación. Se integra con los sistemas productores mediante estándares como **CMIS**, WebDAV o API REST. Según dónde reside el contenido, hay diseños **datacéntricos** (todo en la base de datos) y **docucéntricos** (ficheros en el sistema de almacenamiento y metadatos en la base de datos, como hace Alfresco).
- **Tipos de sistemas de gestión de contenidos**:

| Tipo | Orientación | Ejemplos |
| --- | --- | --- |
| **DMS** (gestión documental) | Documentos de trabajo y su ciclo de vida | Alfresco, OpenText Documentum, SharePoint |
| **CMS/WCM** (gestión de contenidos web) | Producción colaborativa y publicación de contenidos web | Drupal, WordPress, Liferay |
| **RM** (*records management*) | Documentos definitivos con valor de evidencia, inmutables | Módulos *records* de los ECM, Archive |
| **ECM** (*Enterprise Content Management*) | Gestión global de contenidos corporativos: integra DM, WCM, RM, colaboración | Alfresco, OpenText, IBM FileNet |

- **CMIS (*Content Management Interoperability Services*)**: estándar **OASIS** (v1.1, 2013) de interoperabilidad entre repositorios de contenido; permite a las aplicaciones consultar y gestionar documentos de distintos gestores con una interfaz común (es el estándar que usa InSide).
- **Arquitectura de un CMS**: separa la **aplicación de gestión de contenidos (CMA)**, donde los editores crean y mantienen los contenidos, de la **aplicación de entrega de contenidos (CDA)**, que compila y publica en el sitio web. El contenido se separa de la presentación mediante **plantillas**, con roles editoriales y un flujo de publicación (borrador, revisión, publicación) y soporte multisitio y multiidioma. Existen variantes especializadas (LMS de aprendizaje como Moodle, comercio electrónico, wikis, portales).

## Archivo electrónico longevo y conservación

Terminado el trámite, el reto pasa a ser conservar documentos **auténticos, íntegros y legibles durante décadas**, sobrevivientes a la obsolescencia de formatos, soportes y firmas. La normativa impone un archivo electrónico único por Administración y la planificación de la preservación.

### El archivo electrónico en la normativa

- **Archivo electrónico de documentos (art. 46 Ley 40/2015)**: todos los documentos utilizados en las actuaciones administrativas «se almacenarán por medios electrónicos, salvo cuando no sea posible»; los que contengan actos que afecten a derechos o intereses de particulares se conservan en soporte electrónico, en el formato original u otro que asegure la identidad e integridad de la información; se asegura el traslado a otros formatos y soportes. Los soportes deben contar con medidas de seguridad conforme al **ENS**.
- **Archivo de documentos (art. 17 Ley 39/2015)**: cada Administración mantiene un **archivo electrónico único** de los documentos de **procedimientos finalizados**; los documentos se conservan en un formato que garantice su autenticidad, integridad y conservación, y su consulta **con independencia del tiempo transcurrido**; la **eliminación** debe ser autorizada conforme a la normativa aplicable.
- **Conservación de documentos electrónicos (art. 54 RD 203/2021)**: se conservan en soporte electrónico **todos los documentos de los expedientes** y los de **valor probatorio** creados al margen de un procedimiento. La copia electrónica auténtica tiene la consideración de **patrimonio documental** (Ley 16/1985, del Patrimonio Histórico Español). Cada Administración regula los **períodos mínimos de conservación**; si hay **procedimientos judiciales** que afecten a los documentos, se conservan hasta la terminación firme. La conservación comprende, como mínimo, **identificación, contenido, metadatos, firma, estructura y formato**; se planifican actuaciones de **preservación digital** y, bajo supervisión de los responsables de seguridad, custodia y unidades productoras, la **migración** de datos a otros formatos y soportes cuando el formato deje de figurar entre los admitidos por el ENI.
- **Archivo electrónico único (art. 55 RD 203/2021)**: «el conjunto de sistemas y servicios que sustenta la gestión, custodia y recuperación de los documentos y expedientes electrónicos, así como de otras agrupaciones documentales o de información, una vez finalizados los procedimientos administrativos». En la AGE serán accesibles todos los documentos y expedientes del sector público estatal en los plazos que determine la **Comisión Superior Calificadora de Documentos Administrativos**. Su gestión garantiza la **autenticidad, conservación, integridad, confidencialidad, disponibilidad y cadena de custodia**, conforme al ENI, el ENS, la normativa de transparencia y la legislación de archivos y patrimonio.
- **GVA**: el **Archivo electrónico de la Generalitat** (fase inactiva) y los dictámenes de la **Junta Qualificadora de Documents Administratius** se estudian en el tema de administración electrónica de la GVA.

### Fases del archivo y ciclo de vida del documento

- **Archivo de gestión (activo)**: documentación en trámite o de consulta administrativa continua, en manos de la unidad tramitadora y su gestor documental.
- **Archivo central o intermedio (semiactivo)**: reúne y controla los documentos una vez finalizado su trámite, a la espera de su destino definitivo.
- **Archivo histórico (inactivo)**: conserva **permanentemente** los documentos con valor histórico, tras la valoración y expurgo correspondientes.

El **ciclo de vida** del documento encadena su **captura** en el sistema de gestión, su **mantenimiento y uso** (vigencia administrativa) y su **selección y disposición** final (conservación permanente o eliminación reglada, según el calendario de conservación). A cada momento corresponde un tipo de sistema:

- **SGDE (sistema de gestión de documentos electrónicos)**: documentos que aún no han alcanzado su estado definitivo; admite modificación, versionado y borrado.
- **SGDEA (sistema de gestión de documentos electrónicos de archivo)**: documentos en su forma definitiva; garantiza su **inmutabilidad** y conservación a largo plazo (archivo electrónico longevo).

### Conservación a largo plazo: estrategias y modelo OAIS

- **Riesgos de la preservación digital**: obsolescencia de los **soportes** (degradación física, hardware descatalogado), de los **formatos** (aplicaciones que desaparecen) y de las **firmas** (algoritmos criptográficos que se debilitan y certificados que caducan).
- **Estrategias**: **refresco y migración de soportes**; **conversión de formatos** a estándares abiertos y longevos (señaladamente **PDF/A**, ISO 19005, el formato de conservación por excelencia); **emulación** del entorno original; y **firmas longevas** (formatos AdES avanzados con sellos de tiempo y resellado periódico, tratados en el tema de firma electrónica).
- **Modelo OAIS (*Open Archival Information System*, ISO 14721)**: modelo de referencia conceptual para repositorios de preservación a largo plazo, desarrollado por el CCSDS; la edición vigente es **ISO 14721:2025** (anteriores: 2003 y 2012). Define:
    - **El entorno**: los **productores** entregan la información, la **gerencia** fija la política y los **consumidores** (la «comunidad designada») la reutilizan.
    - **Los paquetes de información**: **SIP** (*Submission Information Package*, lo que entrega el productor), **AIP** (*Archival Information Package*, lo que se preserva con su información de representación) y **DIP** (*Dissemination Information Package*, lo que se sirve al consumidor).
    - **Las funciones**: ingesta, almacenamiento archivístico, gestión de datos, administración, **planificación de la preservación** y acceso.

### Herramientas de la AGE: InSide y Archive

- **InSide (Infraestructura y Sistemas de Documentación Electrónica)**: sistema para la **gestión de documentos y expedientes electrónicos conforme al ENI** durante su fase de tramitación. Permite almacenarlos en cualquier gestor documental compatible con **CMIS**, gestionar índices, metadatos y asociaciones de documentos a expedientes, y validar, visualizar y firmar. **G-InSide** ofrece servicios web para **validar y generar** documentos y expedientes ENI.
- **Archive**: aplicación web de **archivo definitivo** de los expedientes y documentos ENI de **procedimientos finalizados**; sigue el modelo **OAIS** y da soporte a la transferencia desde los sistemas de gestión (como InSide), la organización en centros y fondos, y la calificación, conservación y eliminación con los dictámenes correspondientes.
- Ambas son soluciones reutilizables de la **AEAD**, disponibles en el Centro de Transferencia de Tecnología (CTT).

## Fuentes {.unnumbered .unlisted}

- Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (texto consolidado, última modificación 6 de noviembre de 2024). Arts. 17, 26-28, 53 y 70.
- Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (texto consolidado, última modificación 2 de agosto de 2024). Arts. 42 y 46.
- Real Decreto 203/2021, de 30 de marzo, Reglamento de actuación y funcionamiento del sector público por medios electrónicos (texto consolidado, última modificación 2 de abril de 2025). Arts. 21 y 46-55.
- Resoluciones de 19 de julio de 2011, por las que se aprueban las NTI de Documento electrónico, Expediente electrónico, Digitalización de documentos y Procedimientos de copiado auténtico y conversión (textos consolidados, sin modificaciones; contrastadas online en julio de 2026).
- Resolución de 28 de junio de 2012, NTI de Política de gestión de documentos electrónicos (texto consolidado, sin modificaciones).
- Resolución de 3 de octubre de 2012, NTI de Catálogo de estándares (texto consolidado, para los formatos admitidos).
- Esquema de Metadatos para la Gestión del Documento Electrónico (e-EMGDE), versión 3.1 (AEAD, 4.ª edición electrónica, junio de 2025).
- UNE-ISO 15489-1:2016, Información y documentación. Gestión de documentos. Parte 1: Conceptos y principios.
- ISO 14721:2025, modelo de referencia OAIS.
- Fichas de InSide y Archive del PAe/CTT (consulta: julio de 2026; el portal bloquea el acceso automatizado y se verificaron mediante extractos oficiales indexados).
