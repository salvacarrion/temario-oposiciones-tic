# Ciberseguridad

La ciberseguridad es el conjunto de actividades dirigidas a proteger el ciberespacio (las redes y sistemas de información y los servicios que dependen de ellos) frente a las ciberamenazas. Este tema presenta el marco normativo e institucional de la ciberseguridad en España: la Estrategia Nacional de Ciberseguridad, los organismos con competencias (CCN, CCN-CERT e INCIBE) y las guías CCN-STIC. El Esquema Nacional de Seguridad se estudia en el tema [29](29-esquema-nacional-de-seguridad.md), la gestión de ciberincidentes en el [31](31-gestion-de-ciberincidentes.md) y la normativa propia de la Generalitat en el [77](77-internet-de-las-cosas-y-redes-de-sensores.md).

## Conceptos y marco de la ciberseguridad

La ciberseguridad se apoya en los conceptos de la seguridad de la información: proteger la **confidencialidad, integridad y disponibilidad** de la información y de los servicios (a las que el ENS añade la **autenticidad** y la **trazabilidad**), reduciendo los riesgos hasta un nivel aceptable mediante un proceso de gestión de riesgos (tema [30](30-analisis-y-gestion-de-riesgos.md)).

- **Ciberespacio**: espacio creado por el uso masivo de las TIC, donde se producen conflictos y agresiones que pueden atentar contra la seguridad nacional, la prosperidad económica y el funcionamiento normal de la sociedad y de las administraciones.
- **Principales ciberamenazas**: el malware y en particular el *ransomware* (secuestro de datos mediante cifrado y extorsión); el *phishing* y la ingeniería social; la denegación de servicio (DoS/DDoS); las amenazas persistentes avanzadas (**APT**, campañas dirigidas y prolongadas, típicas del ciberespionaje); los ataques a la cadena de suministro; y la amenaza interna. La taxonomía oficial de ciberincidentes y su gestión se desarrollan en el tema [31](31-gestion-de-ciberincidentes.md).

### Marco normativo de la Unión Europea

- **Directiva (UE) 2022/2555 (NIS2)**, relativa a las medidas destinadas a garantizar un elevado nivel común de ciberseguridad en toda la Unión: deroga la Directiva NIS de 2016 con efectos desde el **18 de octubre de 2024** (el plazo de transposición venció el **17 de octubre de 2024**). Amplía el ámbito a **entidades esenciales e importantes** de **18 sectores** (**11 sectores de alta criticidad** en el anexo I y **7 sectores críticos** más en el anexo II), refuerza las obligaciones de **gestión de riesgos** y la responsabilidad de los órganos de dirección, y fija plazos de notificación de incidentes significativos: **alerta temprana en 24 horas**, **notificación en 72 horas** e **informe final en un mes**.
- **Reglamento (UE) 2019/881 (Reglamento de Ciberseguridad o *Cybersecurity Act*)**: otorga a **ENISA** (Agencia de la Unión Europea para la Ciberseguridad) un mandato permanente y crea el **marco europeo de certificación de la ciberseguridad** de productos, servicios y procesos TIC.
- **Directiva (UE) 2022/2557 (CER)**, sobre la resiliencia de las entidades críticas: deroga la Directiva 2008/114/CE y desplaza el enfoque desde la protección física de las infraestructuras hacia la **resiliencia de las entidades** que prestan servicios esenciales.

### Marco normativo nacional

- **Ley 36/2015, de Seguridad Nacional**: marco general del **Sistema de Seguridad Nacional** (Consejo de Seguridad Nacional y sus órganos de apoyo), en el que se integra la gobernanza de la ciberseguridad.
- **Real Decreto-ley 12/2018, de seguridad de las redes y sistemas de información** (transposición de la Directiva NIS de 2016; sigue vigente mientras no se apruebe la ley que transponga NIS2):
    - **Ámbito**: los **servicios esenciales** dependientes de las redes y sistemas de información de los sectores estratégicos del anexo de la Ley 8/2011, y los **servicios digitales** (mercados en línea, motores de búsqueda y computación en nube).
    - **Autoridades competentes (art. 9)**: para los operadores críticos, la Secretaría de Estado de Seguridad a través del **CNPIC**; para los demás operadores de servicios esenciales, la autoridad sectorial correspondiente; para los proveedores de servicios digitales, la Secretaría de Estado de Digitalización e Inteligencia Artificial; y para el sector público (ámbito de la Ley 40/2015), el **Ministerio de Defensa a través del CCN**.
    - **CSIRT de referencia (art. 11)**: el **CCN-CERT** para el sector público; el **INCIBE-CERT** para el resto de entidades y la ciudadanía (operado conjuntamente con el CNPIC para los incidentes de operadores críticos); y el **ESPDEF-CERT** (Ministerio de Defensa) en apoyo y para los operadores con incidencia en la Defensa Nacional. En los supuestos de especial gravedad, el **CCN-CERT ejerce la coordinación nacional** de la respuesta técnica.
    - **Obligación de notificar (art. 19)**: los operadores y proveedores notifican a la autoridad competente, **a través del CSIRT de referencia**, los incidentes con **efectos perturbadores significativos** en sus servicios.
- **Ley 8/2011, de protección de las infraestructuras críticas (LPIC)**, y su reglamento (**RD 704/2011**):
    - Definiciones clave: **servicio esencial** (necesario para el mantenimiento de las funciones sociales básicas), **infraestructuras estratégicas** (instalaciones, redes y sistemas sobre los que descansan los servicios esenciales), **infraestructuras críticas** (las estratégicas cuyo funcionamiento es indispensable y sin alternativa) y **operadores críticos**.
    - Instrumentos: el **Catálogo Nacional de Infraestructuras Estratégicas** (información clasificada, gestionado por el Ministerio del Interior) y los instrumentos de planificación: **Plan Nacional de Protección de las Infraestructuras Críticas, Planes Estratégicos Sectoriales, Plan de Seguridad del Operador, Planes de Protección Específicos y Planes de Apoyo Operativo**.
    - El anexo define **12 sectores estratégicos**: administración, espacio, industria nuclear, industria química, instalaciones de investigación, agua, energía, salud, TIC, transporte, alimentación y sistema financiero y tributario.
    - Órgano responsable: el **CNPIC** (Centro Nacional de Protección de Infraestructuras y Ciberseguridad), dependiente de la **Secretaría de Estado de Seguridad** del Ministerio del Interior.
- **ENS (RD 311/2022)**: principios, requisitos y medidas de seguridad para el sector público (tema [29](29-esquema-nacional-de-seguridad.md)). **Protección de datos**: RGPD y LO 3/2018 (tema [53](53-proteccion-de-datos-personales.md)).
- **Normativa en tramitación** (a julio de 2026): el **Proyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad** (transposición de NIS2, en tramitación parlamentaria; crea el **Centro Nacional de Ciberseguridad**; España recibió en mayo de 2025 un dictamen motivado de la Comisión Europea por el retraso) y el proyecto de ley de **protección y resiliencia de entidades críticas** (transposición de la Directiva CER, que derogará la Ley 8/2011).
- **Ámbito de la Generalitat**: la política y organización de la seguridad de la información (**Decreto 49/2025**) y el uso seguro de medios tecnológicos (**Orden 19/2013**) se estudian en el tema [81](81-seguridad-de-la-informacion-en-la-generalitat.md).

## La Estrategia Nacional de Ciberseguridad

La **Estrategia Nacional de Ciberseguridad 2019**, aprobada por el **Consejo de Seguridad Nacional en abril de 2019**, desarrolla en el ámbito de la ciberseguridad la Estrategia de Seguridad Nacional de 2017, en el marco de la **Ley 36/2015**. Es el documento vigente: el Consejo de Seguridad Nacional aprobó el **24 de abril de 2025** el procedimiento para elaborar una **nueva Estrategia** (Orden PJC/522/2025), todavía en elaboración.

- **Propósito**: fijar las directrices generales de la ciberseguridad en España, reforzando las capacidades de **prevención, detección y respuesta**, fomentando la cultura de ciberseguridad como responsabilidad compartida e impulsando la industria y la I+D+i nacionales para la autonomía estratégica.
- **Principios rectores** (4): **unidad de acción** (respuesta coordinada, gestión centralizada de crisis), **anticipación** (prevención sobre reacción), **eficiencia** (optimización de recursos y sistemas compartidos) y **resiliencia** (disponibilidad y rápido restablecimiento de sistemas e infraestructuras críticas).
- **Objetivo general**: «España garantizará el uso seguro y fiable del ciberespacio, protegiendo los derechos y las libertades de los ciudadanos y promoviendo el progreso socioeconómico».
- **Objetivos específicos** (5):
    - **I**. Seguridad y resiliencia de las redes y sistemas del **sector público y de los servicios esenciales**.
    - **II**. Uso seguro y fiable del ciberespacio frente a su **uso ilícito o malicioso** (lucha contra la cibercriminalidad).
    - **III**. Protección del **ecosistema empresarial y social** y de los ciudadanos.
    - **IV**. **Cultura y compromiso** con la ciberseguridad y potenciación de las capacidades humanas y tecnológicas.
    - **V**. Seguridad del ciberespacio en el **ámbito internacional**.
- **Líneas de acción** (7): reforzar las capacidades ante las ciberamenazas; garantizar la seguridad y resiliencia de los activos estratégicos (plena implantación del ENS, desarrollo del Centro de Operaciones de Ciberseguridad de la AGE e impulso de centros análogos autonómicos y locales); reforzar la investigación y persecución de la cibercriminalidad; impulsar la ciberseguridad de ciudadanos y empresas; potenciar la industria española de ciberseguridad y el talento; contribuir a la seguridad del ciberespacio internacional; y desarrollar una cultura de ciberseguridad.
- **Gobernanza** (estructura del Sistema de Seguridad Nacional):
    - **Consejo de Seguridad Nacional (CSN)**: comisión delegada del Gobierno que dirige la política de Seguridad Nacional, asistido por el **Departamento de Seguridad Nacional (DSN)**, punto de contacto único nacional e internacional.
    - **Comité de Situación**: apoyo al CSN en la gestión de situaciones de crisis.
    - **Consejo Nacional de Ciberseguridad**: órgano colegiado de apoyo al CSN; coordina administraciones y sectores público y privado, valora riesgos y coordina los ciberejercicios nacionales.
    - **Comisión Permanente de Ciberseguridad**: coordinación interministerial a nivel operacional, presidida por el DSN.
    - **Foro Nacional de Ciberseguridad**: espacio de colaboración público-privada con la sociedad civil, la academia y el sector empresarial.
    - **CSIRT de referencia nacionales**: **CCN-CERT**, **INCIBE-CERT** y **ESPDEF-CERT** (Mando Conjunto del Ciberespacio), con la **Oficina de Coordinación Cibernética (OCC)** del Ministerio del Interior como enlace con las Fuerzas y Cuerpos de Seguridad del Estado.

## Organismos: CCN, CCN-CERT e INCIBE

- **Centro Criptológico Nacional (CCN)**: adscrito al **Centro Nacional de Inteligencia (CNI)**. La **Ley 11/2002**, reguladora del CNI, encomienda al Centro las funciones de seguridad de las tecnologías de la información (art. 4.e) y de protección de la información clasificada (art. 4.f); el CCN se regula por el **RD 421/2004**. Entre sus actividades: formación del personal especialista, elaboración y difusión de las **guías CCN-STIC**, certificación de productos y coordinación de la respuesta a incidentes en el sector público.
- **CCN-CERT**: capacidad de respuesta a incidentes de seguridad del CCN; es el **CERT gubernamental nacional**, con comunidad de referencia en el **sector público** (ámbito de la Ley 40/2015) y las empresas de interés estratégico. Ejerce la **coordinación nacional de la respuesta técnica** de los CSIRT en los supuestos de especial gravedad. Presta servicios de alerta temprana, vigilancia, informes de amenazas y un catálogo de soluciones propias:

| Solución | Función |
| --- | --- |
| CARMEN | Detección de amenazas persistentes avanzadas (APT) |
| CLAUDIA | Detección de amenazas complejas en el puesto de usuario, complemento de CARMEN |
| microCLAUDIA | Vacunación de equipos frente a ransomware mediante un agente ligero |
| CLARA | Auditoría del cumplimiento de las configuraciones de seguridad (ENS/STIC) |
| ANA | Automatización y normalización de auditorías: gestión centralizada y continua de vulnerabilidades |
| GLORIA | Plataforma de gestión de incidentes y amenazas mediante correlación compleja de eventos (SIEM) |
| LUCIA | Listado Unificado de Coordinación de Incidentes y Amenazas: gestión y notificación de ciberincidentes en el ámbito del ENS |
| INES | Informe Nacional del Estado de Seguridad: recogida de la información para el informe anual del estado de la seguridad (tema [29](29-esquema-nacional-de-seguridad.md)) |
| IRIS | Cuadro de mando del estado de la ciberseguridad del sector público en tiempo casi real |
| REYES | Intercambio de información de ciberamenazas (integrada con CARMEN, GLORIA y LUCIA) |
| PILAR | Análisis y gestión de riesgos conforme a la metodología MAGERIT (tema [30](30-analisis-y-gestion-de-riesgos.md)) |
| SAT | Sistemas de alerta temprana: sondas en las salidas a internet de los organismos (SAT-INET) y en la red SARA (SAT-SARA) |

- **INCIBE** (Instituto Nacional de Ciberseguridad): sociedad estatal dependiente de la **Secretaría de Estado de Digitalización e Inteligencia Artificial**; atiende a la **ciudadanía, las empresas** (en especial pymes y autónomos) y los sectores estratégicos privados. Opera el **INCIBE-CERT** (CSIRT de referencia para entidades privadas y ciudadanía, conjuntamente con el CNPIC para los operadores críticos), la **línea de ayuda en ciberseguridad 017**, y programas de talento y concienciación.
- **Otros organismos**: el **CNPIC** (protección de infraestructuras críticas, Ministerio del Interior), la **OCC** (enlace con las FCSE para la cibercriminalidad), el **ESPDEF-CERT** del Mando Conjunto del Ciberespacio (Defensa) y la **AEPD** en materia de datos personales. En el ámbito autonómico valenciano, el **CSIRT-CV** es el centro de operaciones de ciberseguridad de la Generalitat (tema [81](81-seguridad-de-la-informacion-en-la-generalitat.md)).

## Las guías CCN-STIC

Las guías **CCN-STIC** son el conjunto de normas, instrucciones, guías y recomendaciones que el **CCN** elabora y difunde para garantizar la seguridad de los sistemas TIC de la Administración, en cumplimiento de sus funciones (Ley 11/2002 y RD 421/2004). En el marco del **ENS**, la disposición adicional segunda del RD 311/2022 encarga al CCN la elaboración de estas guías como apoyo para el mejor cumplimiento de sus requisitos (las **instrucciones técnicas de seguridad**, de obligado cumplimiento, se estudian en el tema [29](29-esquema-nacional-de-seguridad.md)).

- Se organizan en **series temáticas**; para las administraciones públicas destacan la **serie 800**, dedicada al ENS, y las series de **bastionado** de entornos y productos concretos (aplicables a cualquier organización).
- Guías relevantes de la **serie 800**:
    - **CCN-STIC 800**: glosario de términos y abreviaturas del ENS.
    - **CCN-STIC 801**: responsabilidades y funciones (roles de seguridad; es la referencia del Decreto 49/2025 de la GVA, tema [81](81-seguridad-de-la-informacion-en-la-generalitat.md)).
    - **CCN-STIC 803**: valoración de sistemas en el ENS.
    - **CCN-STIC 804**: medidas de implantación del ENS.
    - **CCN-STIC 817**: gestión de ciberincidentes (tema [31](31-gestion-de-ciberincidentes.md)).
    - **CCN-STIC 818**: herramientas de seguridad en el ENS.
    - **CCN-STIC 823**: utilización de servicios en la nube.
    - **CCN-STIC 836**: seguridad en redes privadas virtuales (VPN).

## Fuentes {.unnumbered .unlisted}

- Estrategia Nacional de Ciberseguridad 2019 (Departamento de Seguridad Nacional, abril de 2019). Nueva estrategia en elaboración: Orden PJC/522/2025, de 23 de mayo (BOE de 26 de mayo de 2025).
- Directiva (UE) 2022/2555 (NIS2), de 14 de diciembre de 2022 (DOUE de 27 de diciembre de 2022).
- Real Decreto-ley 12/2018, de 7 de septiembre, de seguridad de las redes y sistemas de información (texto consolidado, última modificación 30 de marzo de 2022).
- Ley 8/2011, de 28 de abril, de protección de las infraestructuras críticas (texto consolidado, última modificación 29 de julio de 2022).
- Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024).
- CCN-STIC 818, Herramientas de seguridad en el ENS (ed. octubre 2012), para la base legal del CCN.
- Portal CCN-CERT (ccn-cert.cni.es), catálogo de soluciones de ciberseguridad, e INCIBE (incibe.es), consultados en julio de 2026.
- Estado de tramitación de las transposiciones NIS2 y CER: Departamento de Seguridad Nacional y prensa especializada, consultado en julio de 2026.
