# E-learning: plataformas y estándares

El *e-learning* es la formación impartida a través de medios electrónicos, con contenidos, actividades, tutoría y evaluación gestionados en plataformas en línea. Es una pieza central de la universidad (docencia virtual e híbrida, campus virtuales) y de la formación de los empleados públicos. El tema sigue los cuatro bloques que piden las convocatorias: conceptos, herramientas, sistemas de implantación y normalización, más los formatos abiertos (MOOC).

## Conceptos y modalidades

El e-learning no se reduce a publicar materiales en internet: combina contenidos digitales, actividades, interacción con el docente y entre estudiantes, y evaluación, todo ello organizado y registrado en una plataforma. Según el grado de presencialidad y el momento en que coinciden docente y estudiante se distinguen varias modalidades.

- **E-learning**: formación completamente en línea, **síncrona** (docente y estudiantes conectados a la vez: videoclase, *webinar*) o **asíncrona** (cada uno a su ritmo: contenidos autoformativos, foros, tareas).
- **B-learning** (*blended learning*): combina sesiones presenciales y en línea. Su variante más conocida es el **aula invertida** (*flipped classroom*): la teoría se estudia antes, en línea, y el tiempo presencial se dedica a la práctica.
- **M-learning**: aprendizaje desde dispositivos móviles (aplicaciones de las plataformas, contenidos adaptables).
- **LMS** (*Learning Management System*): plataforma que organiza la formación: cursos y usuarios, contenidos y actividades, evaluación y calificaciones, comunicación y seguimiento. Se habla también de entorno virtual de aprendizaje o campus virtual.
- **LCMS** (*Learning Content Management System*): sistema centrado en crear, almacenar y reutilizar contenidos formativos; complementa al LMS.
- **LRS** (*Learning Record Store*): almacén de registros de aprendizaje que recibe las sentencias xAPI de cualquier aplicación.
- **Objeto de aprendizaje**: según IEEE LOM, cualquier entidad, digital o no, que pueda utilizarse para el aprendizaje, la educación o la formación. En la práctica, una unidad de contenido reutilizable, empaquetada (SCORM) y descrita con metadatos.
- **Roles**: estudiante; docente o tutor, que dinamiza, resuelve dudas y evalúa; diseñador instruccional; autor de contenidos; administrador de la plataforma; gestor académico.

En la universidad, la modalidad de la enseñanza tiene base legal. La LOSU dispone que «La docencia, preferentemente presencial, podrá impartirse también de manera virtual o híbrida» (art. 6.1), y reconoce al estudiantado el derecho «A ser informado previamente al periodo de matriculación de las modalidades, presencial, virtual o híbrida, de la docencia y la evaluación» (art. 33.d) y a la accesibilidad universal de sus entornos «físicos y virtuales» y de «los materiales educativos y los procesos de enseñanza-aprendizaje y evaluación» (art. 33.q); remisión al tema [103](103-sistema-universitario-losu.md). El RD 822/2021 concreta las modalidades de los títulos oficiales: «Los estudios oficiales de Grado podrán impartirse en modalidad docente presencial, en la híbrida (o semipresencial) y en la virtual (o no presencial)» (art. 14.7; para el Máster remite a esas definiciones el art. 17.5):

| Modalidad | Definición (art. 14.7 RD 822/2021) | Créditos no presenciales |
| --- | --- | --- |
| Presencial | Toda la actividad lectiva se desarrolla de forma presencial, con profesorado y estudiantado en el mismo espacio físico | Ninguno |
| Híbrida (o semipresencial) | Asignaturas o materias presenciales y virtuales, «siempre manteniendo la unidad del proyecto formativo» | **Entre el 40 y el 60 %** de la carga crediticia total |
| Virtual (o no presencial) | Interacción académica que no requiere la presencia física de ambos; se caracteriza por «el uso intensivo de tecnologías digitales de la información y la comunicación» | **Al menos el 80 %** de los créditos ECTS |

## Plataformas LMS

El LMS es el núcleo de cualquier sistema de e-learning. Conviven plataformas de código abierto, que la institución instala y adapta (Moodle, o Sakai, base de PoliformaT en la UPV), con plataformas comerciales que se contratan como servicio en la nube.

- **Funciones de un LMS**: gestión de cursos, usuarios, matrículas, grupos y roles; publicación de contenidos y actividades; evaluación y libro de calificaciones; comunicación (foros, mensajería, avisos, videoconferencia integrada); seguimiento de la actividad, finalización y analítica del aprendizaje; informes; integración con el sistema académico, con la identidad corporativa y con herramientas externas.
- **Moodle**:
    - **Qué es**: LMS de **código abierto** (licencia GPL) creado por Martin Dougiamas; la versión **1.0** se publicó el **20 de agosto de 2002**. Muy extendido en universidades, centros educativos y administraciones.
    - **Arquitectura**: aplicación web en **PHP** con base de datos relacional (PostgreSQL, MySQL, MariaDB o SQL Server; **Oracle no se admite desde la 5.0**), un directorio de datos (`moodledata`) fuera de la parte pública del servidor web y tareas programadas que ejecuta el `cron`. Desde la **5.1**, la raíz del servidor web debe apuntar al subdirectorio `/public`. La 5.2 exige como mínimo **PHP 8.3**.
    - **Organización**: cursos agrupados en categorías y divididos en secciones con **recursos** (archivo, carpeta, página, URL, libro) y **actividades** (tarea, cuestionario, foro, taller, wiki, glosario, lección, H5P, paquete SCORM, herramienta externa LTI, BigBlueButton); libro de calificaciones, finalización de actividades, restricciones de acceso, competencias e insignias.
    - **Roles por contexto**: los permisos se asignan en un contexto (sistema, categoría, curso, actividad) a roles como gestor, creador de cursos, profesor, profesor sin permiso de edición, estudiante o invitado.
    - **Extensibilidad**: **plugins** de muchos tipos (actividades, bloques, temas, autenticación, matriculación, tipos de pregunta, informes) y servicios web para integrarse con otros sistemas; aplicación móvil oficial.
    - **IA**: subsistema de IA con proveedores intercambiables; la 5.1 añadió DeepSeek y la 5.2, Gemini y AWS Bedrock.
    - **Versiones**: dos al año (abril y octubre). Cada dos años, una versión **LTS** (*long-term support*) con tres años de soporte de seguridad:

| Versión | Publicación | Notas |
| --- | --- | --- |
| 4.5 (LTS) | 7 de octubre de 2024 | Soporte de seguridad hasta el 4 de octubre de 2027 |
| 5.0 | 14 de abril de 2025 | Deja de admitir Oracle |
| 5.1 | 6 de octubre de 2025 | Directorio `/public` y nuevo motor de rutas |
| 5.2 | 20 de abril de 2026 | Versión estable a 4 de octubre de 2026; PHP 8.3 como mínimo |
| 5.3 (LTS) | 5 de octubre de 2026 (prevista) | Soporte de seguridad hasta el 1 de octubre de 2029 |

- **Sakai y PoliformaT**: Sakai es un LMS de código abierto de origen universitario, mantenido por la **Fundación Apereo**; su versión **25** (junio de 2025) incorporó al núcleo el reproductor SCORM y la integración con Microsoft 365. Es la base de **PoliformaT**, la plataforma docente corporativa de la **UPV**.
- **Otras plataformas**: **Canvas** (Instructure), **Blackboard Learn** y **D2L Brightspace**, que se ofrecen sobre todo como servicio en la nube (SaaS); **Open edX**, base de muchos portales MOOC; y **Chamilo**, de código abierto.

## Herramientas de e-learning

Alrededor del LMS se usan herramientas especializadas que se integran con él (por LTI, por paquetes SCORM o con conectores propios).

- **Autoría de contenidos**:
    - **eXeLearning**: editor libre (licencia **AGPL**) para crear recursos educativos abiertos sin saber HTML. Nació en Nueva Zelanda; en España lo coordina el INTEF desde **2010** y hoy el CEDEC, con un equipo de desarrollo en el que participan varias comunidades autónomas, entre ellas la Comunitat Valenciana. Está en la serie **4.x** y exporta a SCORM, HTML y ePub, entre otros formatos.
    - **H5P**: contenido interactivo en HTML5 (vídeos con preguntas, presentaciones, juegos), integrado en Moodle.
    - **Comerciales**: Articulate Storyline, Adobe Captivate.
- **Aula virtual y videoconferencia**: **BigBlueButton** (código abierto, integrado en Moodle), Microsoft Teams, Zoom o Google Meet.
- **Vídeo docente**: plataformas como **Kaltura**, que permiten crear vídeos interactivos con preguntas y medir la participación.
- **Evaluación**: cuestionarios con bancos de preguntas (intercambiables con QTI), rúbricas, detección de plagio y herramientas de supervisión (*proctoring*) de exámenes en línea.
- **Gamificación y contenidos visuales**: **Kahoot!** (cuestionarios en forma de juego) y **Genially** (presentaciones e infografías interactivas).
- **Credenciales digitales**: insignias **Open Badges** que acreditan logros concretos.
- **Analítica del aprendizaje** (*learning analytics*): LRS, cuadros de mando y modelos que predicen el riesgo de abandono a partir de la actividad registrada.
- **Licencias compartidas**: dentro de UNI-DIGITAL, RedIRIS contrató, con el grupo de **Formación Online y Tecnologías Educativas (FOLTE)** de Crue Digitalización, licencias campus de **Kaltura** y **Kahoot!** para **35** universidades y **36.000** licencias de **Genially** para docentes de **37** universidades (tema [106](106-rediris-e-identidad-federada.md)).

## Sistemas de implantación

Implantar el e-learning en una organización no es instalar una plataforma: es un proyecto con fases, decisiones de despliegue e integración y una evaluación de resultados.

- **Fases**:
    1. **Análisis de necesidades**: destinatarios y su competencia digital, objetivos formativos, volumen de usuarios, modalidades, requisitos legales y presupuesto.
    2. **Diseño instruccional**: el modelo clásico es **ADDIE** (análisis, diseño, desarrollo, implementación y evaluación); se definen los objetivos de aprendizaje, las actividades, la evaluación y el papel de la tutoría.
    3. **Selección de la plataforma**, según los criterios que se indican abajo.
    4. **Despliegue**: en infraestructura propia (*on-premise*), en una nube gestionada o en modo SaaS. Hay que dimensionar para los picos (periodos de exámenes) y prever alta disponibilidad, copias de seguridad, un entorno de pruebas y un plan de actualizaciones (preferiblemente sobre versiones LTS).
    5. **Integración**: matrícula automática desde el sistema académico o de gestión de la formación; identidad corporativa con SSO (LDAP, CAS, SAML, OAuth 2.0 u OpenID Connect, tema [106](106-rediris-e-identidad-federada.md)); herramientas externas por LTI; traspaso de calificaciones a las actas.
    6. **Migración de contenidos**: copias de seguridad de curso (en Moodle, ficheros `.mbz`), paquetes Common Cartridge o SCORM.
    7. **Formación y soporte**: a docentes, a estudiantes y a los gestores, con un centro de atención.
    8. **Evaluación y mejora continua**: el modelo de **Kirkpatrick** mide cuatro niveles (reacción, aprendizaje, conducta o transferencia al puesto, y resultados); se siguen indicadores de uso, finalización y abandono, y la calidad puede certificarse con la norma UNE 66181.
- **Criterios de selección**:
    - Licencia y coste total de propiedad (licencias, alojamiento, soporte, personal).
    - Escalabilidad y modelo de despliegue.
    - Soporte de estándares: SCORM, xAPI, cmi5, LTI y QTI.
    - **Accesibilidad**: RD 1112/2018 y norma EN 301 549 (tema [58](58-accesibilidad-y-usabilidad.md)).
    - Integración con la identidad corporativa y con los sistemas de gestión.
    - Protección de datos (tema [53](53-proteccion-de-datos-personales.md)) y seguridad conforme al ENS (tema [29](29-esquema-nacional-de-seguridad.md)), con atención a la ubicación de los datos.
    - Comunidad, soporte y hoja de ruta del producto.
- **Riesgos que hay que gestionar**: la analítica y la supervisión de exámenes tratan datos personales, por lo que exigen base jurídica, información y minimización; los materiales necesitan licencias claras (por ejemplo, Creative Commons); y la brecha digital del alumnado obliga a prever alternativas.

## Normalización: estándares de e-learning

Los estándares permiten que un contenido creado con una herramienta funcione en cualquier LMS, que una herramienta externa se integre sin desarrollos a medida y que los datos de aprendizaje sean portables. Los organismos de referencia son:

- **ADL** (*Advanced Distributed Learning*): iniciativa del Departamento de Defensa de EE. UU.; desarrolla SCORM, xAPI y cmi5.
- **1EdTech**: el antiguo IMS Global Learning Consortium, con este nombre desde **mayo de 2022**; mantiene LTI, QTI, Common Cartridge, Open Badges y Caliper.
- **IEEE LTSC**: comité de normas de tecnologías del aprendizaje del IEEE (LOM, xAPI 2.0).
- **ISO/IEC JTC 1/SC 36**: subcomité internacional de tecnologías de la información para el aprendizaje, la educación y la formación. En España, **UNE**.

| Estándar | Organismo | Qué normaliza | Datos clave |
| --- | --- | --- | --- |
| SCORM 1.2 | ADL | Empaquetado del contenido (ZIP con un `imsmanifest.xml`) y su comunicación con el LMS mediante una API JavaScript | **Octubre de 2001**; modelos CAM (empaquetado) y RTE (entorno de ejecución) |
| SCORM 2004 | ADL | Añade la secuenciación y navegación (SN) entre objetos de aprendizaje | **4.ª edición, 2009** |
| xAPI (Experience API o Tin Can) | ADL, IEEE | Registro de experiencias de aprendizaje, dentro y fuera del LMS, como sentencias actor-verbo-objeto guardadas en un LRS | xAPI 2.0 = **IEEE 9274.1.1-2023** (octubre de 2023) |
| cmi5 | ADL | Perfil de xAPI para empaquetar, lanzar y ejecutar contenidos desde el LMS | En normalización como **IEEE P9274.3.1** |
| LTI 1.3 y LTI Advantage | 1EdTech | Integración de herramientas externas con el LMS | **2019**; seguridad con OAuth 2.0, OpenID Connect y JWT; las versiones antiguas perdieron soporte el **30 de junio de 2022** |
| QTI | 1EdTech | Intercambio de preguntas, bancos de preguntas y pruebas | QTI 3.0 (**mayo de 2022**) |
| Common Cartridge | 1EdTech | Paquete de curso completo: contenidos, enlaces LTI y pruebas QTI | Migración de cursos entre LMS |
| Open Badges | 1EdTech | Credenciales digitales (insignias) verificables | Open Badges 3.0 (**junio de 2024**), basada en las credenciales verificables del W3C |
| IEEE LOM | IEEE | Metadatos de objetos de aprendizaje | **1484.12.1-2002**, revisada en **2020**; unos 76 elementos en 9 categorías |

- **SCORM en la práctica**: el paquete contiene uno o varios **SCO** (*Sharable Content Objects*), las unidades que el LMS lanza y que se comunican con él. Al ejecutarse, el SCO busca el objeto que expone el LMS (`API` en SCORM 1.2, `API_1484_11` en SCORM 2004) y le envía el estado de finalización, la puntuación o el tiempo:

```javascript
// SCORM 1.2 (simplificado): el SCO usa el objeto API del LMS
var api = window.parent.API;
api.LMSInitialize("");
api.LMSSetValue("cmi.core.lesson_status", "completed");
api.LMSSetValue("cmi.core.score.raw", "85");
api.LMSCommit("");
api.LMSFinish("");

// SCORM 2004: otro objeto, otros métodos y otro modelo de datos
var api04 = window.parent.API_1484_11;
api04.Initialize("");
api04.SetValue("cmi.completion_status", "completed");
api04.SetValue("cmi.success_status", "passed");
api04.SetValue("cmi.score.scaled", "0.85");
api04.Terminate("");
```

- **Lectura**: SCORM 1.2 mezcla en `lesson_status` la finalización y el resultado (*passed*, *completed*, *failed*, *incomplete*…), mientras que SCORM 2004 los separa en `completion_status` y `success_status`, y expresa la puntuación escalada entre −1 y 1.
- **xAPI en la práctica**: cualquier aplicación (simulador, app móvil, LMS, incluso un registro de formación presencial) envía al LRS, mediante una API REST (recurso `statements`), sentencias JSON con la forma **actor-verbo-objeto**, a las que se puede añadir el resultado, el contexto y la marca de tiempo:

```json
{
  "actor": {"objectType": "Agent", "name": "Ana García",
            "mbox": "mailto:ana.garcia@universidad.es"},
  "verb": {"id": "http://adlnet.gov/expapi/verbs/completed",
           "display": {"es-ES": "completó"}},
  "object": {"objectType": "Activity",
             "id": "https://campus.universidad.es/ciberseguridad/simulador-phishing"},
  "result": {"success": true, "score": {"scaled": 0.85}, "duration": "PT25M"},
  "timestamp": "2026-10-04T09:30:00Z"
}
```

- **SCORM frente a xAPI**: SCORM solo registra lo que ocurre dentro del navegador, en una sesión lanzada por el LMS; xAPI registra **cualquier experiencia**, con o sin conexión y fuera del LMS, y alimenta la analítica del aprendizaje. cmi5 recupera de SCORM la idea de un contenido lanzado y controlado por el LMS, pero usando xAPI.
- **LTI en la práctica**: el LMS (plataforma) lanza una herramienta externa (laboratorio virtual, antiplagio, editor de vídeo) con el usuario ya autenticado: un inicio de sesión de terceros de OpenID Connect seguido de un JWT firmado con la identidad, el rol y el contexto del curso. LTI Advantage añade tres servicios: **Names and Role Provisioning Services** (lista de participantes), **Deep Linking** (elegir contenido de la herramienta e insertarlo en el curso) y **Assignment and Grade Services** (devolver calificaciones al libro de notas).
- **Calidad: UNE 66181:2012**, *Gestión de la calidad. Calidad de la formación virtual* (aprobada el 18 de julio de 2012; sustituye a la versión de 2008). Sirve a los compradores de formación para comparar ofertas y a los proveedores para mejorarlas, y es la base de la certificación de calidad de la formación virtual de AENOR. Estructura:
    - **Tres factores**: reconocimiento de la formación para la empleabilidad; metodología de aprendizaje; y accesibilidad.
    - **Subfactores** de la metodología: diseño didáctico-instruccional; recursos formativos y actividades de aprendizaje; tutoría; y entorno tecnológico-digital de aprendizaje. Los de la accesibilidad: hardware, software y web.
    - **Niveles**: de 1 a 5 estrellas, acumulativos (cada nivel incluye los requisitos de los anteriores).

## MOOC y formatos abiertos

Los MOOC (*Massive Open Online Courses*) son cursos en línea **masivos** (sin límite de plazas) y **abiertos** (sin requisitos de acceso y, en general, gratuitos), basados en vídeos, actividades autocorregidas y foros. El término lo acuñó Dave Cormier en **2008** a raíz del curso CCK08 (*Connectivism and Connective Knowledge*, de George Siemens y Stephen Downes), y el formato se popularizó en **2012** con plataformas como Coursera y edX.

- **cMOOC y xMOOC**: los primeros MOOC, conectivistas (**cMOOC**), se basaban en la red de participantes y en contenidos abiertos y remezclables; los posteriores (**xMOOC**) siguen la estructura de un curso tradicional, con vídeos y pruebas automáticas, a menudo con licencias cerradas pero acceso gratuito.
- **Modelo habitual**: acceso libre al contenido y certificado verificado de pago; algunas universidades reconocen créditos.
- **Variantes**:
    - **SPOC** (*Small Private Online Course*): curso privado para un grupo reducido, por ejemplo los matriculados en una asignatura o la plantilla de una organización.
    - **NOOC** (*Nano Open Online Course*): formato del INTEF de **2016**; nano curso de entre **1 y 20 horas** de dedicación sobre un elemento concreto de una competencia.
- **UPV[X]**: plataforma MOOC de la **UPV**, construida sobre **Open edX**; la UPV publica también cursos en edX.
- **Recursos educativos abiertos (REA)**: materiales docentes con licencias abiertas, como Creative Commons, que permiten usarlos, adaptarlos y redistribuirlos. El término (*Open Educational Resources*) se acuñó en un foro de la UNESCO en **2002**, y la UNESCO aprobó su Recomendación sobre los REA en **2019**. Se publican en repositorios institucionales y portales OpenCourseWare.
- **Proyectos interuniversitarios de UNI-DIGITAL** alojados en la nube de RedIRIS: una plataforma común basada en Open edX, **POA** (portal de objetos de aprendizaje para seis universidades), **DigiRepo** (repositorio colaborativo de contenidos multimedia), **MADAI** (modelo y analítica de datos de aprendizaje) y **ADAPLEARN** (aprendizaje personalizado y adaptativo).

## Fuentes {.unnumbered .unlisted}

- Ley Orgánica 2/2023, de 22 de marzo, del Sistema Universitario (texto consolidado, última modificación 2 de agosto de 2024): arts. 6.1 y 33.
- Real Decreto 822/2021, de 28 de septiembre, por el que se establece la organización de las enseñanzas universitarias y del procedimiento de aseguramiento de su calidad (texto consolidado, última modificación 8 de octubre de 2025): arts. 14.7 y 17.5.
- Moodle, calendario de versiones y notas de las versiones 5.0, 5.1 y 5.2 (moodledev.io), consultados el 4 de octubre de 2026.
- Apereo, notas de la versión Sakai 25 (2025); PoliformaT (poliformat.upv.es) y UPV[X] (upvx.es), consultados el 4 de octubre de 2026.
- eXeLearning, web del proyecto (exelearning.net: historia del proyecto y versión 4.0.1), consultada el 4 de octubre de 2026.
- ADL: SCORM 1.2 (2001), SCORM 2004 4.ª ed. (2009) y cmi5; IEEE 9274.1.1-2023 (xAPI 2.0); grupo de trabajo IEEE P9274.3.1 (cmi5); IEEE 1484.12.1-2020 (LOM).
- 1EdTech: LTI 1.3 y LTI Advantage, con su marco de seguridad (2019) y el calendario de fin de soporte de las versiones antiguas; QTI 3.0 (2022); Open Badges 3.0 (2024); Common Cartridge.
- UNE 66181:2012, Gestión de la calidad. Calidad de la formación virtual (AENOR; norma de pago, estructura contrastada con la documentación de certificación de AENOR y con Baldomero y Salmerón, *Educación XX1*, 18(2), 2015).
- RedIRIS, e-Boletín núm. 18 (mayo de 2025): licencias de docencia híbrida contratadas con UNI-DIGITAL; presentación corporativa (junio de 2026): proyectos interuniversitarios en la nube.
- INTEF, formación en abierto: NOOC (2016); UNESCO, Recomendación sobre los Recursos Educativos Abiertos (2019).
