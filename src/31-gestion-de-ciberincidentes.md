# Gestión de ciberincidentes

Un ciberincidente es un suceso que afecta (o puede afectar) a la seguridad de las redes y sistemas de información. La gestión de ciberincidentes es el conjunto ordenado de acciones para prevenir su ocurrencia en lo posible y, cuando ocurren, restaurar los niveles normales de operación lo antes posible. Es la continuación natural del análisis de riesgos (tema 30): el incidente es el riesgo materializado. El marco institucional de la ciberseguridad española se estudia en el tema 28.

## Ciclo de gestión de ciberincidentes

En el sector público la gestión de ciberincidentes está regulada por el ENS y desarrollada por las guías del CCN:

- **Real Decreto 311/2022 (ENS)**. **Texto consolidado a 6 de noviembre de 2024.**
    - **Art. 8. Prevención, detección, respuesta y conservación** (principio básico): la seguridad del sistema contempla la prevención (que puede incorporar disuasión y reducción de la superficie de exposición), la detección (descubrir la presencia del ciberincidente) y la respuesta en tiempo oportuno (restaurar la información y los servicios afectados).
    - **Art. 33. Capacidad de respuesta a incidentes de seguridad**: el CCN articula la respuesta en torno al **CCN-CERT**; las entidades del sector público **notificarán al CCN los incidentes con impacto significativo**, conforme a la **ITS de Notificación de Incidentes de Seguridad**; el CCN ejerce la **coordinación nacional de la respuesta técnica** de los CSIRT del sector público; tras un incidente, el CCN-CERT determina técnicamente el **riesgo de reconexión** del sistema afectado. Las organizaciones privadas que presten servicios a entidades públicas notifican al **INCIBE-CERT**, que lo pone inmediatamente en conocimiento del CCN-CERT (art. 33.7).
    - **Art. 34**: servicios del CCN-CERT al sector público, empezando por el soporte y la coordinación para el tratamiento de vulnerabilidades y la resolución de incidentes.
    - **Medida op.exp.7 Gestión de incidentes** (marco operacional): exige un **proceso integral** frente a los incidentes, con criterios de clasificación y escalado de la notificación, y respeto al RGPD y la LOPDGDD cuando afecten a datos personales. Refuerzos: **R1** ventanilla única de notificación al CCN-CERT (categorías MEDIA y ALTA), **R2** detección y respuesta (medidas urgentes, recursos para investigar, informar a los responsables afectados y prevenir la repetición), **R3** reconfiguración dinámica ante ataques (categoría ALTA) y **R4** prevención y respuesta automáticas.
    - **Medida op.exp.9 Registro de la gestión de incidentes**: en todas las categorías se registran los reportes inicial, intermedio y final, las actuaciones de emergencia y las evidencias que puedan dirimirse en un ámbito jurisdiccional; el análisis de los incidentes revisa los eventos auditables.
- **Guías**: la **CCN-STIC 817, Gestión de Ciberincidentes en el ENS** (ed. abril 2020, la vigente, alineada con la Guía Nacional) y la **Guía Nacional de Notificación y Gestión de Ciberincidentes**, aprobada por el **Consejo Nacional de Ciberseguridad el 21 de febrero de 2020**, que unifica taxonomía, niveles y ventanilla única para todos los ámbitos (público, privado, infraestructuras críticas y defensa). Las obligaciones de los operadores de servicios esenciales (RD-ley 12/2018) se tratan en el tema 28.

La gestión de un ciberincidente sigue un ciclo de **seis fases** (Guía Nacional):

- **Preparación**: estar listos antes de que ocurra, sobre tres pilares: **personas, procedimientos y tecnología**. Incluye la información de contacto actualizada, políticas y procedimientos al día (gestión de incidentes, evidencias, análisis forense, recuperación), herramientas, formación del **equipo de respuesta a ciberincidentes (ERC)**, el **análisis de riesgos** con su plan de tratamiento (tema 30) y la ejecución de **ciberejercicios**.
- **Identificación**: detectar el incidente con la menor dilación posible mediante monitorización de redes, sistemas y aplicaciones (no todo evento o alerta es un incidente). Los indicios provienen de dos fuentes:
    - **Precursores**: indicios de que un incidente puede ocurrir en el futuro (resultados de un escáner de vulnerabilidades en los logs, anuncio de un nuevo exploit, amenazas explícitas de un grupo organizado).
    - **Indicadores**: indicios de que un incidente está ocurriendo o ya ha ocurrido (alertas del sensor de intrusión o del antivirus, intentos de login fallidos reiterados desde sistemas desconocidos, cambios de configuración no previstos, desviaciones inusuales del tráfico).
- **Contención**: máxima prioridad tras la identificación: evitar la propagación a otros sistemas y la extracción de información. En esta fase se realiza el **triaje**: clasificar y priorizar el incidente según su tipo y la criticidad de la información y sistemas afectados.
- **Mitigación**: eliminar la causa. Según el tipo de incidente: identificar y eliminar el software del atacante (a menudo la mayor garantía es el replataformado completo de la máquina), recuperar la última copia de seguridad limpia e identificar los servicios legítimos utilizados durante el ataque.
- **Recuperación**: devolver la operación a su estado normal, sin precipitarse en la puesta en producción y con un periodo de monitorización reforzada de los sistemas afectados.
- **Actuaciones post-incidente**: las **lecciones aprendidas**: análisis de la causa raíz y de los costes, informe de cierre con las medidas preventivas recomendadas y mejora del propio proceso de gestión.

La **recolección y custodia de evidencias** atraviesa todo el ciclo: conviene empezar el acopio en cuanto se detecta el incidente y obtener una instantánea del sistema atacado antes de manipularlo (trabajando después sobre copias). Debe mantenerse un registro detallado (identificación de equipos, quién ha manejado cada evidencia, fecha y hora de cada tratamiento y ubicación de custodia) conforme a normas aprobadas por el organismo, considerando la persecución del delito, la retención de datos y el coste de la custodia; la evidencia con posible recorrido judicial exige asesoramiento legal especializado (op.exp.9.2).

## Taxonomía, peligrosidad y notificación

La Guía Nacional y la CCN-STIC 817 comparten una **taxonomía de diez categorías** de ciberincidentes:

| Clasificación | Tipos de incidente (ejemplos) |
| --- | --- |
| **Contenido abusivo** | Spam, delito de odio, contenido sexual o violento inadecuado |
| **Contenido dañino** | Sistema infectado, servidor de mando y control (C&C), distribución o configuración de malware |
| **Obtención de información** | Escaneo de redes, análisis de paquetes (*sniffing*), ingeniería social |
| **Intento de intrusión** | Explotación de vulnerabilidades conocidas (CVE), intento de vulneración de credenciales (fuerza bruta), ataque desconocido |
| **Intrusión** | Compromiso de cuenta (con o sin privilegios), compromiso de aplicaciones (inyección SQL), robo (intrusión física) |
| **Disponibilidad** | DoS y DDoS, mala configuración, sabotaje, interrupciones externas |
| **Compromiso de la información** | Acceso o modificación no autorizados de información, pérdida de datos |
| **Fraude** | Uso no autorizado de recursos, derechos de autor, suplantación, *phishing* |
| **Vulnerable** | Criptografía débil, amplificador DDoS, servicios con acceso potencial no deseado, revelación de información, sistema vulnerable |
| **Otros** | Todo lo demás; incluye las **APT** (amenazas persistentes avanzadas: ataques dirigidos, sofisticados y persistentes) |

- **Nivel de peligrosidad**: amenaza potencial que supondría la materialización del incidente; se determina por la tipología de la amenaza y su comportamiento, en **cinco niveles**: **BAJO, MEDIO, ALTO, MUY ALTO y CRÍTICO**. La guía asigna cada tipo a un nivel: las **APT** son CRÍTICO; la distribución o configuración de malware, el robo, el sabotaje y las interrupciones, MUY ALTO; el sistema infectado, el C&C, los compromisos de aplicaciones o de cuentas con privilegios, el DoS/DDoS, los accesos y modificaciones no autorizados y el *phishing*, ALTO; la ingeniería social, la explotación de vulnerabilidades conocidas o la suplantación, MEDIO; el spam, el escaneo y el *sniffing*, BAJO. Si un suceso encaja en más de un tipo, se asigna al de **mayor peligrosidad**.
- **Nivel de impacto**: consecuencias que el incidente ha tenido en las funciones de la organización, sus activos o los individuos afectados; se evalúa en **seis niveles** (los cinco anteriores más **SIN IMPACTO**) con criterios como la afectación a la Seguridad Nacional o ciudadana, a infraestructuras críticas o a sistemas clasificados, el porcentaje de sistemas afectados, la interrupción del servicio, el esfuerzo de resolución, las pérdidas económicas (en % del PIB), la extensión geográfica y los daños reputacionales. Umbrales orientativos por nivel:

| Nivel | Sistemas afectados | Interrupción del servicio | Resolución | Otros criterios |
| --- | --- | --- | --- | --- |
| CRÍTICO | >90 % | >24 h y >50 % de usuarios | >100 jornadas-persona | Seguridad Nacional, infraestructura crítica, sistemas SECRETO |
| MUY ALTO | >75 % | >8 h y >35 % de usuarios | 30-100 jornadas-persona | Servicio esencial, sistemas RESERVADO |
| ALTO | >50 % | >1 h y >10 % de usuarios | 5-30 jornadas-persona | Daños reputacionales de difícil reparación |
| MEDIO | >20 % | >5 % de usuarios | 1-5 jornadas-persona | Eco mediático apreciable |
| BAJO | Afectación puntual | Interrupción de un servicio | <1 jornada-persona | Daños puntuales sin eco mediático |

La **notificación es obligatoria** para los incidentes de nivel **ALTO, MUY ALTO o CRÍTICO** (de peligrosidad o de impacto). En el sector público (ámbito ENS) se notifica al **CCN-CERT**; el sistema de **ventanilla única** de la Guía Nacional evita notificaciones múltiples: el afectado notifica solo a su **CSIRT de referencia**, que la traslada a quien corresponda (al **CNPIC** si afecta a una infraestructura crítica, a la **AEPD** si afecta a datos personales, al **ESPDEF-CERT** si afecta a la Defensa Nacional, a la autoridad competente NIS en su caso).

- **Ventana temporal de reporte**: la **notificación inicial** es **inmediata** en los tres niveles obligatorios; para nivel CRÍTICO, la intermedia a las **24/48 horas** y la final a los **20 días**; para MUY ALTO, intermedia a las **72 horas** y final a los **40 días**. Los tiempos de intermedia y final se cuentan desde la inicial.
- **Estados y cierre**: el incidente permanece **abierto** desde la notificación hasta su cierre; se cierra como resuelto (con o sin respuesta del organismo), sin impacto, falso positivo o sin resolución. Los sistemas de alerta temprana cierran automáticamente los incidentes **sin respuesta** a los **120/90/45/30/21 días naturales** (CRÍTICO/MUY ALTO/ALTO/MEDIO/BAJO), enviando recordatorios previos.
- **LUCIA** (Listado Unificado de Coordinación de Incidentes y Amenazas): herramienta de tickets del CCN-CERT para los organismos del ámbito del ENS; documenta el desarrollo del ciberincidente (detección, contención, erradicación y recuperación), usa la taxonomía y los niveles de la guía y sincroniza los incidentes de cada organismo con el CCN-CERT. Se alimenta también de los **sistemas de alerta temprana** del CCN-CERT: **SAT-SARA** (red SARA), **SAT-INET** (salidas a internet) y **SAT-ICS** (sistemas de control industrial). Anualmente cada organización remite al CCN-CERT un **resumen anual** de sus ciberincidentes.
- **Métricas e indicadores** (Anexo A de la CCN-STIC 817), para evaluar la implantación, eficacia y eficiencia del proceso:

| Métrica | Indicador | Objetivo |
| --- | --- | --- |
| **M1** implantación | Alcance del sistema de gestión (servicios bajo control) | 100 % |
| **M2/M3** resolución | Tiempo de cierre T(50) y T(90) de incidentes de impacto alto/medio | Resolución inmediata |
| **M4** recursos | Horas dedicadas a incidentes / horas contratadas de seguridad TIC | <20 % |
| **M5** gestión | Incidentes cerrados sin respuesta / total notificados | <10 % |
| **M6** gestión | Ídem, solo de peligrosidad MUY ALTA o CRÍTICA | 0 % |

## CERT y CSIRT: CCN-CERT, INCIBE-CERT

Un **CSIRT** (*Computer Security Incident Response Team*) es un equipo de respuesta a incidentes de seguridad informática: previene, detecta, responde y coordina, y presta a su comunidad servicios de alerta temprana, avisos de vulnerabilidades, análisis y formación. **CERT** es el término histórico equivalente (marca registrada de la Universidad Carnegie Mellon, cuyo uso se licencia). La capacidad pública española de respuesta se articula en los **CSIRT de referencia** (Guía Nacional, RD-ley 12/2018 y art. 33 del ENS):

- **CCN-CERT** (Centro Criptológico Nacional, CNI): comunidad de referencia en el **sector público** (estatal, autonómico y local) y los sistemas con información clasificada. Ejerce la **coordinación nacional de la respuesta técnica** en los supuestos de especial gravedad y presta el soporte del art. 34 del ENS (tratamiento de vulnerabilidades y resolución de incidentes, con la máxima celeridad).
- **INCIBE-CERT** (INCIBE): referencia para la **ciudadanía y el sector privado**; presta también los servicios de respuesta a las instituciones afiliadas a **RedIRIS** (red académica y de investigación), en coordinación con el CCN-CERT para los organismos públicos. Para los incidentes de operadores críticos se opera conjuntamente con el CNPIC.
- **ESPDEF-CERT** (**Mando Conjunto del Ciberespacio, MCCE**): redes y sistemas de las Fuerzas Armadas y las que afecten a la **Defensa Nacional**, en apoyo de los operadores con incidencia en ella.
- **CNPIC** (Centro Nacional de Protección de Infraestructuras y Ciberseguridad, Ministerio del Interior): autoridad competente para los operadores críticos; su **Oficina de Coordinación de Ciberseguridad (OCC)** canaliza la coordinación cuando un operador esencial designado crítico sufre un incidente (art. 33.3 del ENS).

El detalle institucional de estos organismos y el catálogo de soluciones del CCN-CERT (GLORIA, REYES, INES, los SAT o la propia LUCIA) se desarrollan en el tema 28; el **CSIRT-CV** de la Generalitat, en el tema 81.

## Operación de la seguridad: SOC, SIEM, EDR

La gestión de incidentes descansa sobre una operación de seguridad continua. El ENS la recoge en el marco operacional de **monitorización del sistema (op.mon)**: detección de intrusión (**op.mon.1**), sistema de métricas (**op.mon.2**) y vigilancia (**op.mon.3**).

- **SOC (*Security Operations Center*)**: centro de operaciones de seguridad; unidad (propia o externalizada) que **monitoriza en continuo (24x7)** la infraestructura, hace el **triaje de alertas** en niveles escalonados de analista (N1 filtrado, N2 investigación, N3 análisis avanzado y *threat hunting*), gestiona vulnerabilidades y ejecuta la primera respuesta. El SOC vigila en continuo; el CSIRT/ERC responde al incidente declarado (en la práctica suelen integrarse). En el ámbito valenciano, el **CSIRT-CV** ejerce este papel para la Generalitat (tema 81).
- **SIEM (*Security Information and Event Management*)**: plataforma que **agrega y correlaciona en tiempo real** los eventos y logs de múltiples fuentes (red, sistemas, aplicaciones, seguridad perimetral), genera alertas, cuadros de mando e informes, y conserva los registros para el análisis forense y el cumplimiento (medida **op.exp.8**, registro de la actividad). Es la herramienta central del SOC; en el sector público, **GLORIA** (CCN) cumple esta función (tema 28).
- **EDR (*Endpoint Detection and Response*)**: agente en el puesto y el servidor que recoge telemetría de comportamiento, **detecta anomalías** (no solo firmas, superando al antivirus tradicional) y permite **responder a distancia**: aislar el equipo de la red, terminar procesos o revertir cambios. El **XDR** extiende la detección y correlación al correo, la red, la identidad y la nube.
- **SOAR (*Security Orchestration, Automation and Response*)**: orquesta las herramientas anteriores y **automatiza mediante playbooks** las respuestas repetitivas (enriquecer alertas, bloquear indicadores, abrir tickets), en línea con el refuerzo **op.exp.7 R4** (prevención y respuesta automáticas) del ENS.
- **Inteligencia de amenazas (CTI)**: consumo y compartición de **indicadores de compromiso (IOC)** (hashes, direcciones IP, dominios) y de tácticas, técnicas y procedimientos (TTP, catalogados en MITRE ATT&CK, tema 32). En el sector público se comparte a través de **REYES** (tema 28). Sobre ella se apoya el ***threat hunting***: búsqueda proactiva de amenazas no detectadas por las alertas.

Las tecnologías de protección de red que alimentan esta operación (cortafuegos, IDS/IPS, honeypots) se estudian en el tema 79.

## Continuidad de negocio y recuperación ante desastres

La gestión de incidentes se completa con la pregunta de qué pasa cuando el incidente interrumpe el servicio: la **gestión de la continuidad de negocio** (*Business Continuity Management*, BCM) prepara a la organización para seguir prestando sus servicios esenciales durante una interrupción grave y recuperar la normalidad después. Su sistema de gestión se especifica en la norma **ISO 22301:2019** (requisitos, certificable), complementada por la **ISO 22313:2020** (directrices).

- **Análisis de impacto en el negocio** (*Business Impact Analysis*, BIA): identifica los procesos y servicios críticos, sus dependencias (personas, sistemas, proveedores) y el impacto de su interrupción a lo largo del tiempo. De él salen los objetivos de recuperación:
    - **RTO** (*Recovery Time Objective*): tiempo máximo admisible hasta recuperar el servicio.
    - **RPO** (*Recovery Point Objective*): pérdida máxima admisible de datos; determina la frecuencia de las copias de seguridad (tema 45).
    - **MTPD** (*Maximum Tolerable Period of Disruption*): periodo máximo tolerable de interrupción; el RTO debe quedar por debajo.
- **Plan de continuidad de negocio (PCN)**: establece las acciones para mantener los servicios esenciales durante la interrupción: funciones y responsabilidades, activación y comunicación, y medios alternativos. Se apoya en:
    - **Plan de contingencia TIC o de recuperación ante desastres (DRP)**: la vertiente tecnológica; restauración de sistemas y datos dentro de los objetivos RTO/RPO, normalmente sobre un centro de respaldo (tema 43).
    - **Plan de emergencia**: la respuesta inmediata a la crisis (protección de las personas, evaluación inicial de daños).
- **Pruebas y mejora continua**: los planes se prueban periódicamente (del ejercicio de mesa al simulacro completo de conmutación) y se revisan tras cada prueba, incidente real o cambio relevante.

En el ENS, la continuidad es el bloque **op.cont (continuidad del servicio)** del marco operacional (Anexo II del RD 311/2022), que aplica según el nivel de la dimensión de **disponibilidad**:

| Medida | Contenido | Aplica |
| --- | --- | --- |
| **op.cont.1** Análisis de impacto | determinar los requisitos de disponibilidad de cada servicio y los elementos críticos para prestarlo | **MEDIO y ALTO** |
| **op.cont.2** Plan de continuidad | acciones ante la interrupción: funciones y responsabilidades, entrada en servicio de los medios alternativos, acuerdos o contratos con proveedores, formación; integrado con los demás planes de continuidad de la organización. Refuerzos R1 (plan de emergencia y contingencia) y R2 (comprobación de integridad tras una caída) | solo **ALTO** |
| **op.cont.3** Pruebas periódicas | localizar y corregir errores o deficiencias del plan de continuidad | solo **ALTO** |
| **op.cont.4** Medios alternativos | servicios de terceros, instalaciones, personal, equipamiento y comunicaciones alternativos, con **tiempo máximo de entrada en funcionamiento** y las mismas garantías de seguridad que los originales; refuerzo R1 (transición automática) | solo **ALTO** |

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024), arts. 8, 33 y 34 y Anexo II (op.exp.7, op.exp.8, op.exp.9, op.cont, op.mon).
- ISO 22301:2019, Security and resilience. Business continuity management systems. Requirements; ISO 22313:2020 (directrices).
- Resolución de 13 de abril de 2018, de la Secretaría de Estado de Función Pública, por la que se aprueba la Instrucción Técnica de Seguridad de Notificación de Incidentes de Seguridad.
- CCN-STIC 817, Esquema Nacional de Seguridad. Gestión de Ciberincidentes (ed. abril 2020; edición vigente a julio de 2026).
- Guía Nacional de Notificación y Gestión de Ciberincidentes, aprobada por el Consejo Nacional de Ciberseguridad el 21 de febrero de 2020.
