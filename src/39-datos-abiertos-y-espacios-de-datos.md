# Datos abiertos y espacios de datos

Los datos del sector público son un activo económico y democrático: su apertura permite crear servicios y conocimiento, y su compartición controlada entre organizaciones da lugar a los espacios de datos. Este tema repasa el régimen de reutilización de la información del sector público (RISP), los principios y tecnologías de los datos abiertos, la estrategia europea de datos (Data Governance Act y Data Act) y los espacios de datos con sus tecnologías de protección de la confidencialidad. La gobernanza interna del dato (roles, calidad, DAMA) se estudia en el tema 38.

## Reutilización de la información del sector público

La **reutilización** es el uso, por personas físicas o jurídicas, de los documentos elaborados o custodiados por el sector público **con fines distintos del propósito inicial** para el que se produjeron (comerciales o no). Su marco es la **Directiva (UE) 2019/1024**, de datos abiertos y reutilización (refunde las Directivas 2003/98/CE y 2013/37/UE), transpuesta en la **Ley 37/2007**, de reutilización de la información del sector público, reformada en profundidad por el **Real Decreto-ley 24/2021**.

**Ley 37/2007: texto consolidado a 9 de mayo de 2023.**

- **Ámbito subjetivo** (art. 2): AGE, CCAA y entidades locales; organismos y entidades del sector público institucional de interés general sin carácter industrial o mercantil; y determinadas **sociedades mercantiles públicas** (las que operan en los sectores del agua, energía, transportes y postales, o como operadores de servicio público de transporte y aéreo).
- **Ámbito objetivo** (art. 3): quedan excluidos, entre otros, los documentos con acceso prohibido o limitado (Ley 19/2013 y art. 13 de la Ley 39/2015), los afectados por defensa, seguridad, secreto estadístico o confidencialidad comercial, los que exigen interés legítimo, los sujetos a **propiedad intelectual de terceros**, los de radiodifusión y los de instituciones culturales distintas de bibliotecas, museos y archivos. Nunca es reutilizable la información en que prevalezca la protección de datos personales sin disociación previa.
- **Datos de investigación** (art. 3 bis): los financiados con fondos públicos ya publicados en repositorios institucionales o temáticos son reutilizables (ciencia abierta).
- **Conjuntos de datos de alto valor** (art. 3 ter): además de la lista europea, puede aprobarse una **lista nacional** (resolución de la Secretaría de Estado de Digitalización e Inteligencia Artificial, con la División Oficina del Dato). Todos ellos deben estar disponibles **gratuitamente**, ser **legibles por máquina** y suministrarse **por API** y, cuando proceda, por **descarga masiva**.
- **Modalidades de reutilización** (art. 4): puesta a disposición **sin condiciones**; con **licencias-tipo**; **previa solicitud**; y acuerdos exclusivos excepcionales. Las condiciones deben ser claras, justas y transparentes, no discriminatorias y no restringir la competencia. La AGE mantiene el **catálogo nacional de información pública reutilizable**, con el que deben interoperar los demás catálogos.
- **Formatos** (art. 5): principio de **documentos abiertos desde el diseño y por defecto**; formatos abiertos y legibles por máquina con sus metadatos; los **datos dinámicos**, inmediatamente tras su recopilación mediante **API** y descarga masiva.
- **Prohibición de derechos exclusivos** (art. 6): los acuerdos exclusivos solo caben para la prestación de un servicio de interés público, con revisión **al menos cada tres años** y publicidad previa; en la digitalización de recursos culturales la exclusividad no excede, por regla general, de **diez años**.
- **Tarifas** (art. 7): la reutilización es **gratuita** como regla general; solo cabe repercutir los **costes marginales** de reproducción, puesta a disposición, difusión y anonimización, con excepciones tasadas (organismos obligados a autofinanciarse, bibliotecas, museos y archivos, y sociedades mercantiles públicas, que pueden añadir un margen razonable). Los datos de alto valor y los de investigación son siempre gratuitos, con excepciones transitorias muy limitadas.
- **Organización**: cada entidad designa una **unidad responsable de información** (art. 10 bis) y existe un régimen sancionador propio (art. 11).

## Datos abiertos: principios, tecnologías y portales

Los **datos abiertos** (*open data*) son datos que cualquiera puede usar, reutilizar y redistribuir libremente, con la única condición, a lo sumo, de atribución y compartición en igual forma. Los principios clásicos exigen datos **completos, primarios** (máxima desagregación), **oportunos, accesibles, procesables por máquina, no discriminatorios**, en **formatos no propietarios** y con **licencias libres**.

- **Modelo de 5 estrellas** (Tim Berners-Lee, 2010), acumulativo:

| Nivel | Requisito | Ejemplo |
| --- | --- | --- |
| 1 estrella | Publicado en la web con licencia abierta | PDF |
| 2 estrellas | Datos estructurados | Excel |
| 3 estrellas | Formato no propietario | CSV |
| 4 estrellas | URIs y estándares W3C para identificar los datos | RDF |
| 5 estrellas | Datos enlazados con otros datos (*linked data*) | RDF + enlaces |

- **Tecnologías de la web semántica**: **RDF** (*Resource Description Framework*) representa la información como **tripletas sujeto-predicado-objeto** identificadas por URIs; las **ontologías** definen formalmente los conceptos y relaciones de un dominio mediante **OWL** (*Web Ontology Language*); y **SPARQL** es el lenguaje de consulta sobre grafos RDF. Juntas sustentan los datos enlazados (nivel 5 estrellas).
- **Vocabularios de catalogación**: **DCAT** (W3C) describe catálogos de datos; **DCAT-AP** es su perfil de aplicación europeo, con la extensión **DCAT-AP HVD** para los datos de alto valor; en España, la **NTI de Reutilización de Recursos de Información** (Resolución de 19 de febrero de 2013) fijó el modelo de metadatos, y el perfil **DCAT-AP-ES** (basado en DCAT-AP 2.1.1 más la extensión HVD) lo actualiza como modelo del federador nacional, con una nueva NTI-RISP en tramitación.
- **Portales**: **datos.gob.es** (catálogo nacional e Iniciativa Aporta, gestionado por red.es y la SEDIA), **data.europa.eu** (portal europeo, que federa los nacionales) y los portales autonómicos y locales (en la GVA, el portal de *dades obertes*). Publican catálogos con API y federación de metadatos.
- **Conjuntos de datos de alto valor**: el **Reglamento de Ejecución (UE) 2023/138** (aplicable desde el **9 de junio de 2024**) establece la lista europea en **seis categorías temáticas**: **geoespacial; observación de la Tierra y medio ambiente; meteorología; estadísticas; sociedades y propiedad de sociedades; y movilidad**. Deben publicarse gratuitamente, en formato legible por máquina, mediante **API** y descarga masiva cuando proceda, con licencia **Creative Commons BY 4.0** (o equivalente o menos restrictiva) y metadatos conformes a DCAT-AP; los Estados informan a la Comisión de su aplicación cada dos años.

## La estrategia europea de datos: Data Governance Act y Data Act

La Estrategia Europea de Datos (2020) persigue un **mercado único de datos** con espacios de datos sectoriales. Sus dos reglamentos transversales son:

- **Reglamento (UE) 2022/868, de gobernanza de datos (Data Governance Act, DGA)**, aplicable desde el **24 de septiembre de 2023**. Cuatro pilares:
  - **Reutilización de categorías protegidas** de datos del sector público (confidencialidad comercial o estadística, propiedad intelectual de terceros, datos personales), que la Directiva 2019/1024 no cubre: se permite con salvaguardas (anonimización, seudonimización, **entornos de tratamiento seguros**), sin derechos exclusivos y con un **punto único de información** nacional.
  - **Servicios de intermediación de datos**: prestadores que conectan a titulares y usuarios de datos bajo un régimen de **notificación previa** y **neutralidad** (no pueden usar los datos intercambiados para fines propios y deben prestar el servicio a través de una estructura separada), con etiqueta y registro de la UE.
  - **Altruismo de datos**: cesión voluntaria de datos para fines de interés general a **organizaciones reconocidas de gestión de datos con fines altruistas**, inscritas en registros públicos nacionales y de la Unión, con un formulario europeo común de consentimiento.
  - **Comité Europeo de Innovación en materia de Datos (EDIB)** y reglas sobre el acceso y la transferencia internacionales de datos no personales.
- **Reglamento (UE) 2023/2854, de datos (Data Act)**, en vigor desde el 11 de enero de 2024 y **aplicable desde el 12 de septiembre de 2025**. Contenidos principales:
  - **Datos de la internet de las cosas**: los usuarios de **productos conectados y servicios relacionados** pueden acceder a los datos que generan y compartirlos con terceros (accesibilidad desde el diseño); el fabricante no puede explotarlos sin acuerdo.
  - **Equidad contractual B2B**: nulidad de las **cláusulas abusivas** impuestas unilateralmente sobre el acceso y uso de datos.
  - **B2G**: puesta de datos a disposición de organismos públicos en caso de **necesidad excepcional** (emergencias).
  - **Cambio entre servicios de tratamiento de datos** (nube): derecho a cambiar de proveedor con plazos y asistencia, **eliminación progresiva de los costes de cambio** y requisitos de interoperabilidad (contra el *lock-in*, ver temas 22 y 51).
  - Salvaguardas frente al **acceso internacional ilícito** a datos no personales y no aplicación del derecho *sui generis* de las bases de datos a los datos de IoT.

## Espacios de datos

Un **espacio de datos** es una infraestructura federada para compartir datos de forma **soberana**: los datos permanecen en su origen y se intercambian entre participantes identificados, bajo reglas comunes de gobernanza, semántica y seguridad, conservando el titular el control sobre las condiciones de uso.

- **Arquitectura y componentes**: **conectores** en cada participante (punto de intercambio que aplica las políticas de uso; implementación de referencia: Eclipse Dataspace Components), **catálogos** y vocabularios comunes (DCAT, ontologías), servicios de **identidad y confianza** (identificación de participantes, certificación), **contratos de datos** con políticas de uso legibles por máquina (ODRL) y servicios de compensación (*clearing*).
- **IDS**: la asociación **IDSA** (*International Data Spaces Association*) publica el modelo de referencia **IDS-RAM**, con los roles de proveedor y consumidor de datos, intermediario (*broker*), cámara de compensación, tienda de aplicaciones y proveedor de identidad.
- **Gaia-X** (2020): iniciativa europea (asociación AISBL con sede en Bruselas) para una infraestructura federada de datos y nube conforme a los valores europeos; define un **marco de confianza** (*Trust Framework*) con especificaciones y etiquetas de conformidad para servicios cloud y espacios de datos, articulada en *hubs* nacionales (Gaia-X Hub España).
- **Espacios de datos sectoriales europeos**: la Comisión impulsa **espacios comunes europeos de datos** en sectores estratégicos: salud (el EEDS, primer espacio regulado por reglamento, ver tema 94), movilidad, energía, agricultura, administraciones públicas, Pacto Verde, industria o competencias, con el middleware **Simpl** y un centro de soporte (*Data Spaces Support Centre*). En España los impulsa la SEDIA (Oficina del Dato) con fondos del Plan de Recuperación.
- **Tecnologías de protección de la confidencialidad (PET**, *Privacy-Enhancing Technologies*): permiten explotar datos sin exponerlos, y habilitan la compartición en espacios de datos y la reutilización de datos protegidos de la DGA:
  - **Anonimización y seudonimización** (agregación, k-anonimato) y **privacidad diferencial** (adición de ruido calibrado con un presupuesto de privacidad).
  - **Aprendizaje federado**: el modelo se entrena donde están los datos y solo viajan los parámetros.
  - **Computación multiparte segura (SMPC)** y **cifrado homomórfico**: cálculo conjunto o sobre datos cifrados sin revelarlos.
  - **Entornos de ejecución confiables (TEE)** y entornos de tratamiento seguros: enclaves y salas de datos controladas donde el análisis se realiza sin extraer los microdatos.

## Fuentes {.unnumbered .unlisted}

- Ley 37/2007, de reutilización de la información del sector público (texto consolidado, última modificación 9 de mayo de 2023).
- Directiva (UE) 2019/1024, de datos abiertos y reutilización de la información del sector público (DOUE de 26 de junio de 2019).
- Reglamento de Ejecución (UE) 2023/138, conjuntos de datos de alto valor (DOUE de 20 de enero de 2023).
- Reglamento (UE) 2022/868, de gobernanza de datos (DGA), y Reglamento (UE) 2023/2854, de datos (Data Act), DOUE.
- NTI de Reutilización de Recursos de Información (Resolución de 19 de febrero de 2013); DCAT-AP y DCAT-AP-ES (datos.gob.es, consultado en julio de 2026).
- Berners-Lee, T., *Linked Data: 5 star scheme* (2010); especificaciones W3C de RDF, OWL y SPARQL.
- IDS-RAM (IDSA) y documentación de Gaia-X y del Data Spaces Support Centre (webs oficiales, consultadas en julio de 2026).
