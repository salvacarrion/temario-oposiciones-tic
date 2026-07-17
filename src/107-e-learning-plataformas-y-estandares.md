# E-learning: plataformas y estándares

El *e-learning* es la formación impartida a través de medios electrónicos, con contenidos, actividades y evaluación gestionados en plataformas en línea. Es una pieza central de la universidad (docencia virtual e híbrida, campus virtuales) y de la formación de empleados públicos, y se apoya en dos pilares: las **plataformas LMS** y los **estándares** que hacen interoperables contenidos, herramientas y datos de aprendizaje.

## Conceptos y modalidades

- **e-learning**: formación completamente en línea, síncrona (videoclase, webinar) o asíncrona (contenidos autoformativos, foros).
- **b-learning** (*blended*): combinación de formación presencial y en línea; la variante **aula invertida** (*flipped classroom*) traslada la teoría a casa y la práctica al aula.
- **LMS (Learning Management System)**: plataforma que organiza la docencia en línea: cursos, contenidos y actividades, entregas y evaluación, calificaciones, comunicación (foros, mensajería, videoconferencia integrada) y seguimiento del aprendizaje (*learning analytics*).
- **LCMS**: sistema centrado en la **creación y gestión de contenidos** formativos reutilizables; complementa al LMS.

## Plataformas LMS

- **Moodle**: el LMS de **código abierto** (GPL) de referencia en la universidad española. Versión vigente: **Moodle 5.2** (abril de 2026; la próxima versión LTS será la 5.3). Organiza cada curso en secciones con **recursos** (archivo, página, URL) y **actividades** (tarea, cuestionario, foro, taller, H5P interactivo), con calificaciones, competencias, insignias y roles configurables; es extensible mediante *plugins*.
- **Sakai**: LMS de código abierto de origen universitario; es la base de **PoliformaT**, la plataforma docente corporativa de la **UPV**.
- **Otras plataformas**: Canvas y Blackboard Learn (comerciales en la nube), Open edX (base de los portales MOOC), Chamilo.
- **Criterios de selección**: modelo de licenciamiento y coste total, escalabilidad y despliegue (local o SaaS), cumplimiento de estándares (SCORM, xAPI, LTI), **accesibilidad** (tema 58), integración con la identidad corporativa (SSO, tema 106) y protección de datos (tema 53).

## Estándares de e-learning

Los estándares permiten que un contenido creado con una herramienta funcione en cualquier LMS y que los datos de aprendizaje sean portables. Los mantienen **ADL** (iniciativa del Departamento de Defensa de EE. UU.) y **1EdTech** (el antiguo IMS Global).

| Estándar | Qué normaliza | Claves |
| --- | --- | --- |
| SCORM 1.2 / SCORM 2004 | Empaquetado de contenidos y su comunicación con el LMS | Paquetes reutilizables (imsmanifest); SCORM 2004 añade secuenciación y navegación |
| xAPI (Experience API, «Tin Can») | Registro de experiencias de aprendizaje dentro y fuera del LMS | Sentencias actor-verbo-objeto almacenadas en un **LRS** (Learning Record Store); normalizada como **IEEE 9274.1.1-2023** |
| cmi5 | Perfil de xAPI para contenidos lanzados desde un LMS | Sustituto moderno de SCORM |
| LTI 1.3 y LTI Advantage | Integración de herramientas externas en el LMS | Lanzamiento con seguridad **OAuth 2.0/JWT**; deja obsoletas LTI 1.0/1.1 |
| QTI | Preguntas y tests intercambiables entre plataformas | Bancos de preguntas portables |

Una sentencia xAPI mínima (JSON) tiene la forma actor-verbo-objeto:

```json
{
  "actor": {"mbox": "mailto:alumno@upv.es", "name": "Alumno"},
  "verb": {"id": "http://adlnet.gov/expapi/verbs/completed"},
  "object": {"id": "https://poliformat.upv.es/curso/tema-102"}
}
```

- **SCORM frente a xAPI**: SCORM solo registra la actividad dentro del navegador y del LMS (lecciones, intentos, puntuación); xAPI registra **cualquier experiencia** (simuladores, apps móviles, actividad presencial) mediante sentencias enviadas a un LRS, lo que habilita el *learning analytics*.
- **LTI en la práctica**: permite lanzar desde el LMS herramientas externas (laboratorios virtuales, antiplagio, videoconferencia) con la identidad del alumno ya autenticada y devolver calificaciones al libro de notas (*Assignment and Grade Services* de LTI Advantage).

## MOOC y formatos abiertos

- **MOOC** (*Massive Open Online Course*): cursos en línea **masivos y abiertos**, sin requisitos de acceso, basados en vídeo, autoevaluación y foros; certificación opcional. Se popularizaron a partir de **2012** con las grandes plataformas (edX, Coursera).
- **Variantes**: **SPOC** (*Small Private Online Course*: privado, para grupos reducidos, habitual en formación corporativa) y **NOOC** (nano-curso sobre una competencia concreta).
- **El caso UPV**: la UPV es una de las universidades españolas más activas en MOOC, con su plataforma propia **UPV[X]** (sobre Open edX) y cursos publicados en **edX**.
- **Recursos educativos abiertos (OER)**: materiales docentes con licencias abiertas (Creative Commons); repositorios institucionales y OpenCourseWare universitarios.

## Fuentes {.unnumbered .unlisted}

- Moodle, documentación y calendario oficial de versiones (moodledev.io, consultado en julio de 2026: Moodle 5.2, abril de 2026).
- 1EdTech (LTI 1.3 y LTI Advantage, 2019; QTI); ADL (SCORM 2004, xAPI y cmi5); IEEE 9274.1.1-2023 (xAPI).
- Plataformas institucionales citadas: PoliformaT (poliformat.upv.es) y UPV[X] (upvx.es), consultadas en julio de 2026.
