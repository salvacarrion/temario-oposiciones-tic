# Plan de reestructuración del temario

Documento de trabajo (no se publica en el libro). Define el índice objetivo
(85 capítulos en 14 bloques + 3 apéndices) contrastado con los 8 temarios de
`temarios_opos/`, las convenciones de nomenclatura y las fases de ejecución.

**Estado**: la fase 1 (reestructura mecánica) se ejecutó el 4 de julio de
2026: ficheros renumerados a la numeración objetivo, desdobles y fusión
hechos, encabezados normalizados, `_quarto.yml` con `number-depth: 2` y
portada sin numerar. Los capítulos sin contenido aún NO están en
`_quarto.yml` (no se publican esqueletos); por eso hay huecos en los números
de fichero (17, 22, 33, 39, 46, 67, 69, 78-85) y la numeración visible del
libro se compacta hasta que existan.

## 1. Convenciones de normalización

**Títulos de capítulo (H1, = título en `_quarto.yml`):**

- Frase nominal en *sentence case*, sin punto final.
- El título nombra la **materia**, sin normas ni marcos tras dos puntos.
  Excepción: si el capítulo es sí o sí de una sola ley, la ley se añade
  entre paréntesis — «Régimen jurídico del sector público (Ley 40/2015)».
  En capítulos multi-norma o técnicos el título queda genérico y estable
  frente a cambios normativos (p. ej. «La agenda digital valenciana» vale
  para GEN Digital 2025 y su sucesor).

**Subtemas (H2, numerados N.M con `number-depth: 2`):**

- Capítulo dedicado a **una sola norma grande** (Constitución, Estatuto,
  Ley 5/1983, 39/2015, 40/2015, TREBEP, LO 1/2004, Ley 1/2015, LCSP…):
  - La norma va en el título del capítulo (entre paréntesis), no en el x.1.
  - x.1 = «Características y estructura».
  - Subtemas siguientes = **los Títulos oficiales, literales** («Título I.
    De los derechos y deberes fundamentales»), casi uno a uno, porque caen
    preguntas literales. Se respeta la capitalización oficial.
  - Último subtema (opcional) = «Datos más relevantes», a modo de resumen.
  - Los títulos que el temario no pide se despachan brevemente dentro de
    «Características y estructura», salvo en Constitución y Estatuto,
    donde van todos.
- Capítulo con **varias normas**: un H2 por norma («Ley 19/2013, de
  transparencia…»), y los Títulos de cada norma como H3 literales.
- Capítulo técnico: 3-6 H2 de frase nominal; el desglose fino en H3.
- Normas citadas como «Tipo N/AAAA, denominación corta» (nunca
  «Decreto 42/2019 - Condiciones…»).
- Sin negritas ni imágenes dentro de encabezados.
- El caso práctico, si existe, es el último H2: «Caso práctico: …».
- Cierre de capítulo: `## Fuentes {.unnumbered .unlisted}` (pendiente de
  añadir en la mayoría de capítulos; se hace al tocar el contenido).

## 2. Índice objetivo (85 capítulos + 3 apéndices)

Notación: `[nuevo]` = capítulo a escribir (aún sin fichero ni entrada en
`_quarto.yml`); `[← N]` = procede del capítulo N del libro antiguo (63
capítulos); sin marca = existente renumerado/renombrado.

### PARTE I — TEMARIO COMÚN

#### Bloque I — Marco jurídico y administrativo

**1. Jerarquía normativa y fuentes del derecho** [← 1]

- 1.1 El ordenamiento jurídico y la jerarquía normativa
- 1.2 Normas con rango de ley
- 1.3 El reglamento
- 1.4 La iniciativa legislativa
- 1.5 Fuentes del derecho público; los tratados internacionales

**2. La Constitución Española de 1978** [← 2]

- 2.1 Características y estructura
- 2.2 Título preliminar
- 2.3 Título I. De los derechos y deberes fundamentales
- 2.4 Título II. De la Corona
- 2.5 Título III. De las Cortes Generales
- 2.6 Título IV. Del Gobierno y de la Administración
- 2.7 Título V. De las relaciones entre el Gobierno y las Cortes Generales
- 2.8 Título VI. Del Poder Judicial *(pendiente de contenido)*
- 2.9 Título VII. Economía y Hacienda *(pendiente de contenido)*
- 2.10 Título VIII. De la organización territorial del Estado
- 2.11 Título IX. Del Tribunal Constitucional
- 2.12 Título X. De la reforma constitucional
- 2.13 Datos más relevantes

**3. El Estatuto de Autonomía de la Comunitat Valenciana (Ley Orgánica 5/1982)** [← 3]

- 3.1 Características y estructura
- 3.2 Título I. La Comunitat Valenciana
- 3.3 Título II. De los derechos de los valencianos y valencianas
- 3.4 Título III. La Generalitat
- 3.5 Título IV. Las competencias
- 3.6 Título V. Relaciones con el Estado y otras comunidades autónomas
- 3.7 Título VI. Relaciones con la Unión Europea
- 3.8 Título VII. Acción exterior
- 3.9 Título VIII. Administración local
- 3.10 Título IX. Economía y hacienda
- 3.11 Título X. Reforma del Estatuto
- 3.12 Datos más relevantes

**4. El Consell y el gobierno valenciano (Ley 5/1983)** [← 4]

- 4.1 Características y estructura *(pendiente de contenido)*
- 4.2 Título I. Del President de la Generalitat
- 4.3 Título II. Del Consell
- 4.4 Título III. De las relaciones entre el Consell y Les Corts
- 4.5 Título IV. De la Administración Pública de la Generalitat
- 4.6 Título V. De la responsabilidad de los miembros del Consell y de la Administración Pública de la Generalitat
- 4.7 Datos más relevantes *(pendiente de contenido)*

**5. La Unión Europea** [← 5]

- 5.1 El ordenamiento jurídico de la Unión Europea y sus fuentes
- 5.2 Instituciones y organismos de la Unión Europea
- 5.3 El Tratado de la Unión Europea (TUE): disposiciones comunes
- 5.4 El Tratado de Funcionamiento (TFUE): actos jurídicos y procedimientos de adopción

**6. Leyes de igualdad** [← 6]  *(multi-norma: títulos de cada ley como H3)*

- 6.1 Ley Orgánica 3/2007, para la igualdad efectiva de mujeres y hombres
- 6.2 Ley 9/2003, de la Generalitat, para la igualdad entre mujeres y hombres
- 6.3 Ley 4/2023, de igualdad de las personas trans y derechos LGTBI *(nueva en 9/26)*

**7. Protección integral contra la violencia de género (Ley Orgánica 1/2004)** [← 7]

- 7.1 Características y estructura
- 7.2 Título preliminar
- 7.3 Título I. Medidas de sensibilización, prevención y detección
- 7.4 Título II. Derechos de las mujeres víctimas de violencia de género
- 7.5 Título III. Tutela institucional
- 7.6 Tutela penal y judicial (Títulos IV y V, síntesis)

**8. Transparencia y buen gobierno** [← 8]  *(multi-norma)*

- 8.1 Gobierno abierto: principios y participación ciudadana
- 8.2 Ley 19/2013, de transparencia, acceso a la información pública y buen gobierno
- 8.3 Ley 1/2022, de transparencia y buen gobierno de la Comunitat Valenciana

**9. Régimen jurídico del sector público (Ley 40/2015)** [← 9]  *(la parte pedida es el Título preliminar: capítulos literales como H2)*

- 9.1 Características y estructura
- 9.2 Capítulo I. Disposiciones generales
- 9.3 Capítulo II. De los órganos de las Administraciones Públicas
- 9.4 Capítulo III. Principios de la potestad sancionadora
- 9.5 Capítulo IV. De la responsabilidad patrimonial de las Administraciones Públicas
- 9.6 Capítulo V. Funcionamiento electrónico del sector público
- 9.7 Capítulo VI. De los convenios

**10. El procedimiento administrativo común de las Administraciones Públicas (Ley 39/2015)** [← 10]

- 10.1 Características y estructura
- 10.2 Título preliminar. Disposiciones generales
- 10.3 Título I. De los interesados en el procedimiento
- 10.4 Título II. De la actividad de las Administraciones Públicas
- 10.5 Título III. De los actos administrativos
- 10.6 Título IV. De las disposiciones sobre el procedimiento administrativo común
- 10.7 Título V. De la revisión de los actos en vía administrativa
- 10.8 Título VI. De la iniciativa legislativa y de la potestad para dictar reglamentos y otras disposiciones

**11. Contratos del sector público (Ley 9/2017)** [← 11]

- 11.1 Características y estructura
- 11.2 Objeto, ámbito de aplicación y tipos contractuales (Título preliminar)
- 11.3 Objeto, presupuesto base de licitación, valor estimado y precio (Libro I)
- 11.4 Preparación y adjudicación de los contratos (Libro II)
- 11.5 Contratos menores y órganos de contratación

**12. El Estatuto Básico del Empleado Público (TREBEP)** [← 12, desdoble]

- 12.1 Características y estructura
- 12.2 Título I. Objeto y ámbito de aplicación
- 12.3 Título II. Personal al servicio de las Administraciones Públicas
- 12.4 Título III. Derechos y deberes. Código de conducta de los empleados públicos
- 12.5 Título IV. Adquisición y pérdida de la relación de servicio
- 12.6 Título V. Ordenación de la actividad profesional
- 12.7 Título VI. Situaciones administrativas
- 12.8 Título VII. Régimen disciplinario
- 12.9 Título VIII. Cooperación entre las Administraciones Públicas

**13. Función pública valenciana** [← 12, desdoble]  *(multi-norma: ley + decretos de desarrollo)*

- 13.1 Ley 4/2021, de la función pública valenciana *(sus Títulos como H3)*
- 13.2 Decreto 3/2017, de selección, provisión de puestos y movilidad *(pendiente de contenido)*
- 13.3 Decreto 42/2019, de condiciones de trabajo del personal funcionario
- 13.4 Decreto 49/2021, de regulación del teletrabajo

**14. Hacienda pública de la Generalitat (Ley 1/2015)** [← 13]

- 14.1 Características y estructura
- 14.2 Título I. Del ámbito de aplicación y de la Hacienda Pública de la Generalitat
- 14.3 Título II. De los presupuestos de la Generalitat
- 14.4 Título IX. Sector público instrumental de la Generalitat
- 14.5 Título X. Subvenciones

**15. Prevención de riesgos laborales** [← 14]  *(multi-norma)*

- 15.1 Ley 31/1995, de prevención de riesgos laborales
- 15.2 Real Decreto 488/1997, sobre trabajo con pantallas de visualización

#### Bloque II — Sociedad digital y gestión TIC

**16. La sociedad digital** [← 15]

- 16.1 Tecnología y desarrollo en la sociedad digital
- 16.2 Brecha digital e inclusión
- 16.3 El índice DESI y la medición de la economía digital
- 16.4 La Década Digital de Europa: metas 2030

**17. Gobernanza y planificación estratégica TIC** [nuevo]

- 17.1 Los sistemas de información en las organizaciones
- 17.2 Planificación estratégica TIC y plan de sistemas de información
- 17.3 Gobernanza TIC y cuadro de mando
- 17.4 Organización de un departamento TIC
- 17.5 Sistemas corporativos: ERP y CRM

**18. La gestión de los servicios TIC** [← 17]

- 18.1 La gestión de servicios TIC: conceptos
- 18.2 ITIL 4: sistema de valor del servicio y principios guía
- 18.3 Las cuatro dimensiones y la cadena de valor
- 18.4 Prácticas clave: incidencias, problemas, cambios, nivel de servicio
- 18.5 La mejora continua

**19. Dirección y gestión de proyectos** [← 18]

- 19.1 Fundamentos y áreas de conocimiento (PMBOK)
- 19.2 Metodología PM²
- 19.3 Metodología gvLOGOS
- 19.4 Caso práctico: PERT y CPM

**20. Análisis de procesos** [← 19]

- 20.1 Análisis y modelado de procesos
- 20.2 La notación BPMN
- 20.3 Caso práctico: análisis de procesos

**21. Metodologías ágiles y escalado ágil** [← 20]

- 21.1 Metodologías predictivas frente a ágiles
- 21.2 Scrum
- 21.3 Lean y Kanban
- 21.4 Extreme Programming (XP)
- 21.5 Escalado ágil: SAFe, LeSS, SoS

**22. Contratación pública de bienes y servicios TIC** [nuevo]

- 22.1 Especialidades de la contratación TIC; los pliegos
- 22.2 Criterios de valoración de productos y servicios
- 22.3 Outsourcing y offshoring
- 22.4 Contratación de servicios en la nube y pago por uso

#### Bloque III — Ingeniería del software

**23. Análisis y diseño de aplicaciones** [← 21]

- 23.1 Ciclo de vida del software y sus modelos
- 23.2 Análisis de requisitos: técnicas y gestión
- 23.3 Casos de uso e historias de usuario
- 23.4 Prototipado y diseño
- 23.5 Caso práctico: diagramas de casos de uso y de actividades

**24. Proceso unificado y UML** [← 22]

- 24.1 El proceso unificado de desarrollo
- 24.2 UML: diagramas estructurales y de comportamiento
- 24.3 El Proceso Unificado Racional (RUP)
- 24.4 Métrica v3: visión de síntesis *(pendiente de contenido)*

**25. Calidad del software** [← 23, desdoble]

- 25.1 Aseguramiento de la calidad del software
- 25.2 Familia ISO/IEC 25000 (SQuaRE): las 8 características de calidad
- 25.3 Métricas y evaluación de la calidad
- 25.4 Caso práctico: cálculo de la complejidad ciclomática

**26. Control de versiones, integración continua y DevOps** [← 23, desdoble]

- 26.1 Control de versiones: Git y estrategias de ramas
- 26.2 Integración, entrega y despliegue continuos (CI/CD)
- 26.3 DevOps y DevSecOps
- 26.4 Gestión de la configuración y CMDB

**27. Testeo de software** [← 23, desdoble]

- 27.1 Fundamentos del testeo (ISTQB)
- 27.2 Las pruebas en el ciclo de vida: roles, niveles y tipos
- 27.3 Técnicas de prueba
- 27.4 Gestión y automatización de las pruebas

#### Bloque IV — Seguridad de la información

**28. Ciberseguridad** [← 24, desdoble]

- 28.1 Conceptos y marco de la ciberseguridad
- 28.2 La Estrategia Nacional de Ciberseguridad
- 28.3 Organismos: CCN, CCN-CERT e INCIBE
- 28.4 Las guías CCN-STIC

**29. El Esquema Nacional de Seguridad (Real Decreto 311/2022)** [← 24, desdoble]

- 29.1 Principios básicos y requisitos mínimos
- 29.2 Categorización de los sistemas
- 29.3 Las medidas de seguridad (Anexo II)
- 29.4 Adecuación, conformidad y certificación
- 29.5 Caso práctico: plan de adecuación al ENS

**30. Análisis y gestión de riesgos** [← 25, desdoble]

- 30.1 La gestión de riesgos: conceptos
- 30.2 MAGERIT v3: el método
- 30.3 Catálogo de elementos
- 30.4 Caso práctico: análisis de riesgos con MAGERIT

**31. Gestión de ciberincidentes** [← 25, desdoble + nuevo]

- 31.1 Ciclo de gestión de ciberincidentes (guías CCN)
- 31.2 Taxonomía, peligrosidad y notificación
- 31.3 CERT y CSIRT: CCN-CERT, INCIBE-CERT
- 31.4 Operación de la seguridad: SOC, SIEM, EDR

**32. Desarrollo seguro de aplicaciones** [← 26]

- 32.1 El ciclo de desarrollo seguro; buenas prácticas del CCN
- 32.2 Seguridad en aplicaciones web: OWASP Top 10
- 32.3 Marcos Mitre: CVE y CWE
- 32.4 Técnicas de análisis: SAST, DAST y pruebas de intrusión

**33. Auditoría informática** [nuevo]

- 33.1 Concepto, tipos y áreas de la auditoría informática
- 33.2 Marcos de referencia: COBIT e ISO 27001/27002
- 33.3 La auditoría en la Administración: auditoría del ENS

#### Bloque V — Datos, IA y tecnologías emergentes

**34. Inteligencia artificial y aprendizaje automático** [← 28, desdoble]

- 34.1 Conceptos básicos
- 34.2 Aprendizaje automático (machine learning)
- 34.3 Deep learning y redes neuronales
- 34.4 IA distribuida y federada
- 34.5 Evolución histórica de la IA

**35. Inteligencia artificial aplicada y su regulación** [← 28, desdoble + nuevo]

- 35.1 Procesamiento del lenguaje natural y de documentos
- 35.2 Visión por computador *(pendiente de contenido)*
- 35.3 IA generativa y grandes modelos de lenguaje
- 35.4 Ética y regulación: el Reglamento europeo de IA *(pendiente de contenido)*

**36. Bases de datos** [← 29]

- 36.1 Sistemas de gestión de bases de datos; el modelo ANSI
- 36.2 El modelo relacional: diseño conceptual, lógico y físico
- 36.3 El lenguaje SQL
- 36.4 Bases de datos NoSQL y no estructuradas
- 36.5 Caso práctico: diseño de una base de datos

**37. Gestión de datos corporativos y Big Data** [← 30]

- 37.1 Almacén de datos (data warehouse) y OLAP
- 37.2 Procesos ETL, data lake y espacios de compartición
- 37.3 Big Data: el ecosistema Hadoop/Spark
- 37.4 Minería de datos
- 37.5 Caso práctico: clasificación

**38. Gobernanza del dato** [← 31]

- 38.1 El gobierno del dato: calidad, linaje, metadatos, CDO
- 38.2 El marco DAMA-DMBOK
- 38.3 Modelos estratégico, operativo y organizativo
- 38.4 El gobierno del dato en el sector público

**39. Datos abiertos y espacios de datos** [nuevo]

- 39.1 Reutilización de la información pública: Ley 37/2007 y RDL 24/2021
- 39.2 Datos abiertos: portales, RDF y SPARQL
- 39.3 Espacios de datos y Gaia-X; la estrategia europea del dato

**40. APIs y apificación** [← 32]

- 40.1 Qué es una API; REST y OpenAPI
- 40.2 Gestión y gobierno de APIs
- 40.3 La apificación en la Administración

**41. Automatización robótica de procesos (RPA)** [← 33]

- 41.1 Concepto, beneficios y niveles de automatización
- 41.2 Procesos automatizables en la Administración
- 41.3 Plataformas y automatización inteligente (RPA + IA)

**42. Blockchain y otras tecnologías emergentes** [← 34]

- 42.1 Blockchain: fundamentos y funcionamiento
- 42.2 Tipos de redes y smart contracts
- 42.3 Organizaciones descentralizadas (DAO) y casos de uso en la Administración
- 42.4 Realidad extendida y metaversos *(pendiente de contenido)*

#### Bloque VI — Sistemas e infraestructuras

**43. Centros de proceso de datos** [← 35]

- 43.1 Diseño de un CPD: infraestructura física y lógica
- 43.2 Infraestructura convergente e hiperconvergente
- 43.3 Monitorización, gestión y tendencias
- 43.4 Caso práctico: diseño de un CPD

**44. Virtualización y contenedores** [← 36]

- 44.1 Virtualización e hipervisores
- 44.2 Contenedores: Docker
- 44.3 Orquestación: Kubernetes

**45. Sistemas de almacenamiento** [← 37]

- 45.1 Arquitecturas DAS, NAS y SAN
- 45.2 RAID
- 45.3 Respaldo y recuperación: políticas de copias de seguridad *(pendiente de contenido)*

**46. Sistemas operativos y administración de sistemas** [nuevo]

- 46.1 Sistemas operativos: conceptos, evolución y tipos
- 46.2 Windows Server y Directorio Activo
- 46.3 GNU/Linux: administración y shell scripting
- 46.4 Servidores web y de aplicaciones
- 46.5 Automatización y monitorización de infraestructura
- 46.6 Software libre y de código abierto

**47. Computación en la nube y de altas prestaciones** [← 38]

- 47.1 Cluster, grid y computación de altas prestaciones (HPC)
- 47.2 La nube: modelos de despliegue (pública, privada, híbrida)
- 47.3 Modelos de servicio: IaaS, PaaS, SaaS
- 47.4 Tendencias: serverless y edge computing *(pendiente de contenido)*
- 47.5 Centro de datos definido por software (SDDC) *(hoy en cap. 43; mover al retocar)*

**48. Puesto de trabajo TIC** [← 39]

- 48.1 El puesto de trabajo TIC: normalización, seguridad y despliegue
- 48.2 Administración centralizada y soporte a usuarios
- 48.3 Virtualización del escritorio: VDI y Remote Desktop Services
- 48.4 Movilidad y BYOD *(pendiente de contenido)*

#### Bloque VII — Protección de datos y administración electrónica

**49. Protección de datos personales** [← 40]  *(multi-norma)*

- 49.1 El Reglamento General de Protección de Datos (RGPD)
- 49.2 Ley Orgánica 3/2018, de protección de datos personales y garantía de los derechos digitales (LOPDGDD)
- 49.3 El delegado de protección de datos en las AAPP *(pendiente de contenido)*
- 49.4 La AEPD y las autoridades autonómicas *(pendiente de contenido)*

**50. Administración electrónica** [← 41, desdoble]

- 50.1 El funcionamiento electrónico del sector público (marco general)
- 50.2 Real Decreto 203/2021, de actuación y funcionamiento del sector público por medios electrónicos
- 50.3 Actuación administrativa automatizada *(pendiente de contenido)*
- 50.4 Simplificación administrativa y reducción de cargas *(pendiente de contenido)*

**51. Documento y expediente electrónico. Gestión documental** [← 49]

- 51.1 Documento y expediente electrónico; metadatos (eEMGDE)
- 51.2 Gestión documental y de contenidos (DMS y CMS)
- 51.3 Copia auténtica, CSV y portafirmas
- 51.4 Archivo electrónico longevo y conservación

#### Bloque VIII — Desarrollo web y de aplicaciones

**52. Arquitecturas de desarrollo web** [← 42]

- 52.1 Arquitectura multicapa y modelo de aplicaciones web
- 52.2 Desarrollo front-end
- 52.3 Desarrollo en servidor y conexión a bases de datos
- 52.4 Interconexión con sistemas y servicios

**53. Tecnologías web** [← 43]

- 53.1 HTML5
- 53.2 CSS3
- 53.3 JavaScript y TypeScript
- 53.4 Frameworks y entornos: Angular, React, Vue, Node.js *(sustituir AngularJS)*

**54. Accesibilidad y usabilidad** [← 44]

- 54.1 Normativa: RD 1112/2018, WCAG y EN 301 549
- 54.2 W3C/WAI y diseño universal
- 54.3 Experiencia de usuario (UX) e interfaz de usuario (UI)
- 54.4 Diseño web adaptativo

**55. Desarrollo de aplicaciones móviles** [← 45]

- 55.1 Diseño y arquitecturas de aplicaciones móviles
- 55.2 Aplicaciones nativas: Android e iOS
- 55.3 Aplicaciones híbridas y multiplataforma
- 55.4 Aplicaciones web progresivas (PWA) *(pendiente de contenido)*

**56. SOA, servicios web y microservicios** [← 46 + 47, fusión]

- 56.1 La arquitectura orientada a servicios (SOA); el ESB
- 56.2 Servicios web y estándares (SOAP, WSDL, UDDI)
- 56.3 Servicios REST
- 56.4 Arquitectura de microservicios
- 56.5 Formatos de intercambio: XML y JSON

**57. Programación** [← 48]

- 57.1 Programación orientada a objetos
- 57.2 Patrones de diseño *(pendiente de contenido)*
- 57.3 Lenguajes y ecosistemas: visión general (Java, Python, JavaScript) *(pendiente de contenido)*
- 57.4 Programación low-code y no-code

#### Bloque IX — Interoperabilidad y confianza digital

**58. El Esquema Nacional de Interoperabilidad** [← 50, desdoble]

- 58.1 Real Decreto 4/2010, del Esquema Nacional de Interoperabilidad (ENI)
- 58.2 Normas Técnicas de Interoperabilidad (NTI)
- 58.3 Interoperabilidad europea, nacional y autonómica (EIF)
- 58.4 Intercambio de datos entre AAPP: el protocolo SCSP *(pendiente de contenido)*

**59. Infraestructuras y servicios comunes de interoperabilidad** [← 50, desdoble + nuevo]

- 59.1 Identificación, registro y directorios: SIA, DIR3, SIR y Cl@ve
- 59.2 Intermediación de datos: la PID
- 59.3 Notificaciones y documentos: DEHú, Notific@, INSIDE, ARCHIVE
- 59.4 Redes de las AAPP: SARA y sTESTA *(pendiente de contenido)*

**60. Criptografía** [← 51]

- 60.1 Cifrado simétrico y asimétrico
- 60.2 Funciones hash
- 60.3 Infraestructura de clave pública (PKI) y ciclo de vida de certificados
- 60.4 Protocolos seguros: TLS

**61. Identificación y firma electrónica** [← 52]

- 61.1 Marco europeo y nacional: eIDAS, eIDAS2 y Ley 6/2020
- 61.2 Certificados digitales; claves privadas, públicas y concertadas
- 61.3 Formatos de firma (AdES) y sellado de tiempo
- 61.4 Plataformas: @firma, FIRe y Cl@ve Firma
- 61.5 Identificación y firma biométricas; servicios de directorio

**62. Sistemas de información geográfica** [← 53]

- 62.1 Conceptos: datos raster y vectoriales
- 62.2 Componentes y funcionalidades de un SIG
- 62.3 La componente geográfica en los sistemas de información

**63. Infraestructuras de datos espaciales** [← 54]

- 63.1 Definición y componentes de una IDE
- 63.2 Servicios web: WMS, WFS y CSW
- 63.3 Marco normativo: INSPIRE y LISIGE

#### Bloque X — Redes y comunicaciones

**64. Modelos OSI y TCP/IP** [← 55]

- 64.1 El modelo de referencia OSI
- 64.2 El modelo TCP/IP
- 64.3 Comparativa entre modelos

**65. Protocolos de comunicaciones** [← 56]

- 65.1 Capa de internet: IPv4, IPv6, ICMP, ARP
- 65.2 Capa de transporte: TCP y UDP
- 65.3 Capa de aplicación: DNS, HTTP, SMTP, FTP, DHCP, SSH

**66. Redes de computadores** [← 57]

- 66.1 Componentes, topologías y dispositivos de interconexión
- 66.2 Redes de área local: VLAN y DMZ
- 66.3 Redes de área extensa (WAN)
- 66.4 Direccionamiento IP y subredes
- 66.5 Caso práctico: cálculo de subredes

**67. Cableado estructurado y medios de transmisión** [nuevo]

- 67.1 Medios de transmisión: cobre, fibra óptica e inalámbricos
- 67.2 Sistemas de cableado estructurado: subsistemas y categorías
- 67.3 Normalización y certificación

**68. Virtualización de redes** [← 58]

- 68.1 Redes definidas por software (SDN)
- 68.2 SD-WAN
- 68.3 Orquestación y gestión centralizada; administración de red (SNMP)

**69. Redes de transporte, voz y audiovisuales** [nuevo]

- 69.1 Redes de transporte: MPLS y GPON
- 69.2 VoIP, telefonía IP y comunicaciones unificadas
- 69.3 Radiodifusión: TDT, múltiplex autonómico y DAB
- 69.4 Videoconferencia y streaming

**70. Redes de emergencia** [← 59]

- 70.1 Redes de emergencia y misión crítica
- 70.2 El estándar TETRA
- 70.3 La red COMDES

**71. Redes inalámbricas y 5G** [← 60]

- 71.1 Wi-Fi: la familia IEEE 802.11
- 71.2 Generaciones de telefonía móvil; redes 5G
- 71.3 Otras tecnologías de transmisión

**72. Internet de las cosas y redes de sensores** [← 61]

- 72.1 IoT: concepto y arquitectura
- 72.2 Redes de corto alcance: BLE, NFC y RFID
- 72.3 Redes de largo alcance (LPWAN): LoRaWAN, Sigfox, NB-IoT, LTE-M
- 72.4 Sensórica e inteligencia artificial

**73. Ciudades inteligentes** [← 62]

- 73.1 Concepto, arquitectura y gobierno
- 73.2 Plataformas de ciudad: FIWARE
- 73.3 Protocolos: MQTT y CoAP
- 73.4 Gemelos digitales

**74. Seguridad en las comunicaciones** [← 63]

- 74.1 Seguridad perimetral: NGFW, IDS/IPS y anti-DDoS
- 74.2 Autenticación, autorización y accounting (AAA)
- 74.3 Control de acceso a la red (NAC) y seguridad inalámbrica
- 74.4 Acceso remoto seguro: VPN e IPSec

### PARTE II — TEMAS ESPECÍFICOS POR ADMINISTRACIÓN

#### Bloque XI — Administración de la Generalitat

**75. La agenda digital valenciana** [← 16]  ⚠ *reescribir sobre GEN Digital 2025 (ref. disponible); hoy el contenido es ADCV/COM Digital*

- 75.1 Antecedentes: de la ADCV a GEN Digital
- 75.2 GEN Digital 2025: estructura, ejes y objetivos

**76. Seguridad de la información en la Generalitat** [← 27]  ⚠ *Decreto 49/2025 sustituye a los D 66/2012 y 130/2012 que cita el capítulo*

- 76.1 Decreto 49/2025, de política de seguridad de la información
- 76.2 Orden 19/2013, de uso seguro de medios tecnológicos

**77. Administración electrónica y plataformas de la Generalitat** [← 41 + 50-PAI]  ⚠ *Decreto 54/2025 sustituye al D 220/2014 que cita el capítulo*

- 77.1 Decreto 54/2025, de simplificación administrativa y transformación digital
- 77.2 La Plataforma Autonómica de Interoperabilidad (PAI)
- 77.3 Sede electrónica y servicios comunes de la GVA

#### Bloque XII — Sanidad

**78. Organización sanitaria y normativa** [nuevo]

- 78.1 El Sistema Nacional de Salud y su cartera de servicios
- 78.2 Ley 41/2002, de autonomía del paciente
- 78.3 La historia clínica: documentos, conservación y conjunto mínimo de datos
- 78.4 Ordenación sanitaria valenciana y Estatuto Marco

**79. Interoperabilidad sanitaria** [nuevo]

- 79.1 Integración de sistemas sanitarios: el bus de integración
- 79.2 Mensajería HL7 y FHIR
- 79.3 openEHR e ISO 13606
- 79.4 DICOM e imagen médica
- 79.5 HCDSNS y el proyecto europeo eHDSI

**80. Seguridad y protección de datos en sanidad** [nuevo]

- 80.1 Los datos de salud como categoría especial (RGPD)
- 80.2 Organización de la seguridad de la información en sanidad
- 80.3 Medidas de seguridad para sistemas de categoría alta

#### Bloque XIII — Administración local

**81. Régimen local** [nuevo]

- 81.1 El municipio: término, población y padrón
- 81.2 Organización y competencias; municipios de gran población
- 81.3 Formas de actividad de las entidades locales
- 81.4 La función pública local
- 81.5 Delitos contra la Administración pública

**82. Sistemas de información municipales** [nuevo]

- 82.1 Gestión económica y tributaria, padrón, RRHH y subvenciones
- 82.2 Administración electrónica local: sede y carpeta ciudadana
- 82.3 Registro, digitalización certificada y gestión documental

**83. Ciudad inteligente municipal** [nuevo]

- 83.1 Plataforma de ciudad; estrategias local, nacional y europea
- 83.2 BIM, gemelos digitales y citiverso
- 83.3 SIG municipal y geoportales

#### Bloque XIV — Universidades

**84. Marco universitario y su gobernanza TIC** [nuevo]

- 84.1 La Ley Orgánica del Sistema Universitario (LOSU)
- 84.2 El ENS en universidades: guía CCN-STIC 881

**85. Servicios TIC universitarios** [nuevo]

- 85.1 RedIRIS
- 85.2 Identidad federada: eduroam y eduGAIN
- 85.3 Interoperabilidad universitaria: NISUE
- 85.4 Plataformas de e-learning

### Apéndices

- **A. Referencias** (actual `src/referencias.md`)
- **B. Correspondencia temarios ↔ capítulos** [nuevo]: una tabla por
  convocatoria (las 8 de `temarios_opos/`) mapeando tema oficial → capítulos.
  Es la pieza clave de "reconocibilidad" para opositores de otras
  administraciones.
- **C. Mapa normativo** [nuevo]: norma → capítulo → versión consolidada usada.

### Decisiones tomadas

- Capítulo de una sola ley → la ley entre paréntesis en el título,
  «Características y estructura» como x.1 y Títulos literales como H2.
  Capítulos multi-norma o técnicos → título de materia genérico y estable;
  una norma por H2 con sus títulos como H3.
- ENS (cap. 29) y ENI (cap. 58) como temas propios.
- Herramientas de producto de Sanidad/UPV (Informix, Oracle 19c, PL/SQL,
  APEX, JEE, Jenkins, JIRA…) sin capítulo: se cubren a nivel conceptual en
  36, 46 y 57 (son material de curso, no de temario de repaso).
- Ley 4/2021 FPV en el bloque común (cap. 13) porque la piden también UPV y
  local; los decretos GVA como subtemas del mismo capítulo.
- E-learning solo como subtema 85.4; Métrica v3 solo como 24.4; telefonía
  clásica resumida en 69.2; RV/RA/metaversos como 42.4.

## 3. Diagnóstico de contenido (por capítulo nuevo)

Veredictos heredados del diagnóstico original (que usaba la numeración
antigua), re-mapeados a la numeración nueva. Convenciones: **OK** — solo
retoques; **Mejorable** — faltan puntos concretos; **Incompleto** — alcance
insuficiente; **Desactualizado** — cita normativa sustituida; **Formato** —
tablas/`<img>` HTML que no salen en el PDF.

| Cap. nuevo | Veredicto | Trabajo pendiente principal |
|---|---|---|
| 1 | Mejorable | Ampliar fuentes del derecho (Ayto T7) |
| 2 | OK + Formato | 1 tabla HTML; faltan Títulos VI y VII |
| 3 | OK | — |
| 4 | Mejorable | Verificar reformas recientes Ley 5/1983; añadir 4.1 y 4.7 |
| 5 | Incompleto | TUE/TFUE: actos jurídicos y procedimientos (9/26 T10) |
| 6 | Mejorable | Falta Ley 4/2023 (trans/LGTBI) |
| 7 | Incompleto | Ampliar Títulos preliminar/I/II |
| 8 | OK | Contrastar Ley 1/2022; añadir gobierno abierto (8.1) |
| 9 | Incompleto | Faltan capítulos III-VI del Título preliminar |
| 10 | OK | Añadir 10.1 características |
| 11 | Incompleto | Tipos contractuales, preparación, menores |
| 12 | Mejorable | Faltan Títulos I-II como H2 propios y IV, V, VIII |
| 13 | Mejorable | Falta Decreto 3/2017; la Ley 4/2021 ya está (corregido: el diagnóstico antiguo la daba por ausente) |
| 14 | Incompleto | Reescribir por títulos de la Ley 1/2015 |
| 15 | OK | — |
| 16 | Incompleto | DESI, brecha digital, Década Digital 2030 |
| 18 | Incompleto | Reescribir sobre ITIL 4 (SVS, prácticas) |
| 19 | OK + Formato | 1 tabla HTML; añadir áreas PMBOK |
| 20 | OK + Formato | 1 tabla HTML |
| 21 | Reenfocar | Añadir XP y escalado SAFe/LeSS/SoS |
| 23 | Mejorable | Historias de usuario, prototipos |
| 24 | Formato crítico | 4 tablas y 14 imágenes HTML; nota Métrica v3 |
| 25 | OK | Ya desdoblado; revisar métricas |
| 26 | Incompleto | Añadir Git/ramas y gestión de configuración (hoy solo DevOps) |
| 27 | Mejorable | Ampliar niveles/tipos/técnicas (ref. ISTQB CTFL 4.0) |
| 28 | Incompleto | Reescribir marco (estrategia, CCN/INCIBE, guías); quitar decretos GVA obsoletos |
| 29 | OK + Formato | 2 tablas HTML; revisar orden interno |
| 30 | OK + Formato | 1 tabla HTML (pendiente ref. MAGERIT v3) |
| 31 | Mejorable | Añadir SOC/SIEM/EDR y taxonomía CCN |
| 32 | Mejorable | Mitre CVE/CWE, prácticas CCN, SAST/DAST |
| 34 | OK | Desdoblado; revisar nivel |
| 35 | Incompleto | Falta visión por computador, ética, AI Act |
| 36 | Mejorable | Modelo ANSI, SQL, NoSQL |
| 37 | OK | Verificar Hadoop, ETL, data lake |
| 38 | Mejorable | Detallar DAMA-DMBOK |
| 40 | Incompleto | Reescribir entero (el más corto del libro) |
| 41 | Incompleto | Niveles, beneficios, tecnologías de ampliación |
| 42 | Mejorable | Smart contracts, casos de uso, RV/RA |
| 43 | OK | Mover SDDC al cap. 47 al retocar |
| 44 | Mejorable | Ampliar hipervisores y Kubernetes |
| 45 | Incompleto | Falta respaldo y recuperación |
| 47 | Mejorable | Añadir serverless/edge; recibir SDDC |
| 48 | OK | — |
| 49 | OK + Formato | 1 tabla HTML; añadir DPD y AEPD |
| 50 | Incompleto | Solo RD 203/2021; añadir 50.1/50.3/50.4 |
| 51 | Incompleto | Documento/expediente electrónico, eEMGDE, archivo longevo |
| 52 | Incompleto | Front-end, servidor, conexión BD |
| 53 | Desactualizado + Formato | AngularJS obsoleto; 2 tablas HTML |
| 54 | Incompleto | RD 1112/2018, WCAG, EN 301 549; sin estructura interna |
| 55 | Mejorable | PWA y multiplataforma |
| 56 | OK | Fusión hecha; hacer explícito REST |
| 57 | Mejorable | Patrones de diseño |
| 58 | OK | Añadir SCSP |
| 59 | Incompleto | Ampliar servicios (DEHú, Notific@, SARA); *el hueco más importante del libro* |
| 60 | Incompleto | Simétrico/asimétrico, hash, PKI, TLS |
| 61 | Mejorable | eIDAS2, @firma, FIRe, Cl@ve |
| 62 | Incompleto | Conceptos, componente geográfica en SI |
| 63 | Mejorable | WMS/WFS/CSW, INSPIRE/LISIGE |
| 64 | OK + Formato | 1 tabla HTML |
| 65 | OK | Separar capa de transporte |
| 66 | OK | VLAN, DMZ |
| 68 | Mejorable | Ya incluye orquestación; revisar |
| 70 | OK | — |
| 71 | Mejorable + Formato | Ampliar 5G, WiFi 6/7; 1 tabla HTML |
| 72 | Incompleto | BLE, NFC, RFID, LoRa, Sigfox, NB-IoT, LTE-M |
| 73 | Incompleto | FIWARE, MQTT/CoAP, arquitectura |
| 74 | OK | Reordenar según 9/26 T40-41 |
| 75 | Desactualizado | Reescribir sobre GEN Digital 2025 |
| 76 | Desactualizado | D 66/2012 y 130/2012 → **D 49/2025** |
| 77 | Desactualizado | D 220/2014 → **D 54/2025** |

## 4. Plan de ejecución por fases

1. ~~**Reestructura mecánica**~~ — **HECHA** (4 jul 2026): renumeración,
   desdobles (12→12+13, 23→25/26/27, 24→28+29, 25→30/31, 28→34/35,
   41→50+77, 50→58/59+77), fusión (46+47→56), encabezados normalizados
   (Títulos literales como H2 en leyes, sin negritas/imágenes en headings),
   `_quarto.yml` nuevo con `number-depth: 2`, portada sin numerar.
   `quarto render --to html` verifica sin errores.
2. **Actualizaciones normativas urgentes** (afectan a GVA 9/26, convocatoria
   viva): caps. 76 (D 49/2025), 77 (D 54/2025), 13 (D 3/2017), 6 (Ley
   4/2023), 61 (eIDAS2), 59 (DEHú y servicios comunes), 32 (CVE/CWE).
   Contrastar cada dato con `references/`.
3. **Incompletos de la parte común**, por prioridad 9/26: 59, 18 (ITIL),
   40 (APIs), 41 (RPA), 72 (IoT), 73 (smart cities), 54 (accesibilidad),
   60 (criptografía), 62 (SIG), 52 (desarrollo web), 45 (almacenamiento),
   14 (hacienda), 9 (Ley 40/2015), 11 (LCSP), 5 (UE), 16 (sociedad
   digital), 7 (violencia de género), 28 (marco ciberseguridad),
   50 (admin-e común), 51 (documento electrónico).
4. **Capítulos nuevos comunes**: 17, 22, 33, 39, 46, 67, 69 (al escribirlos,
   añadirlos a `_quarto.yml`).
5. **Bloques por administración**: XI listo tras fase 2; XII-XIV (78-85)
   contenido nuevo.
6. **Deuda de formato**: tablas HTML → markdown en caps. nuevos 2, 19, 20,
   24, 29, 30, 49, 53, 64, 71; imágenes HTML del 24.
7. **Apéndices B y C** al final, cuando el índice esté estable. Añadir
   `## Fuentes {.unnumbered .unlisted}` a cada capítulo al tocarlo.

Pendientes de referencia (ver `references/README.md`): MAGERIT v3, OWASP
Top 10 2021, Ley 37/2007 consolidada, Ley 55/2003, CCN-STIC 803/804.
