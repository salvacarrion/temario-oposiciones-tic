# Computación en la nube y de altas prestaciones

La agregación de recursos de computación ha seguido dos caminos complementarios: el de las **altas prestaciones** (clústeres, grids y supercomputadores, orientados a maximizar la capacidad de cálculo) y el de la **computación en la nube** (orientada a consumir recursos como un servicio elástico y de pago por uso).

## Clúster, grid y computación de altas prestaciones (HPC)

- **Clúster**: grupo de ordenadores (nodos) interconectados mediante una red de alta velocidad que funciona como un único sistema, coordinado por un software de gestión. Los nodos suelen ser homogéneos y estar en la misma ubicación física. Según su finalidad se distinguen:
    - **Clúster de alto rendimiento (HPC)**: paraleliza el cálculo entre los nodos para resolver problemas de cómputo intensivo.
    - **Clúster de alta disponibilidad (HA)**: nodos redundantes que asumen el servicio si otro falla (failover), eliminando puntos únicos de fallo.
    - **Clúster de balanceo de carga**: reparte las peticiones entre los nodos para escalar el servicio y absorber picos de demanda.
- **Grid computing (computación en malla)**: conecta recursos heterogéneos y **distribuidos geográficamente**, pertenecientes a organizaciones distintas y sin control centralizado, mediante un middleware que reparte los trabajos entre los nodos disponibles. Es el modelo de las «organizaciones virtuales» científicas: el **WLCG** (Worldwide LHC Computing Grid, la malla del CERN) o los proyectos de computación voluntaria sobre **BOINC**.
- **De la malla a la nube**: la nube toma del grid la agregación de recursos distribuidos y le añade la **virtualización** (tema [44](44-virtualizacion-y-contenedores.md)), el autoservicio y el pago por uso, consolidando los recursos en grandes centros de datos de proveedor.

| Aspecto | Clúster | Grid | Nube |
| --- | --- | --- | --- |
| Idea básica | Agregación de recursos | Compartición de recursos distribuidos | Consolidación de recursos como servicio |
| Nodos | Homogéneos, misma ubicación | Heterogéneos, distribuidos geográficamente | Heterogéneos, la ubicación no importa |
| Control | Centralizado | Descentralizado (multi-organización) | Del proveedor (autoservicio del cliente) |
| Ejecución de trabajos | Planificada por el gestor del clúster | El middleware asigna subtrabajos a nodos libres | Autogestionada, bajo demanda |
| Virtualización | No es esencial | No es esencial | Es la tecnología clave |
| Modelo típico de uso | Cálculo paralelo, alta disponibilidad | Ciencia distribuida (física, bioinformática) | Servicios TI de propósito general (IaaS, PaaS, SaaS) |
| Acceso a Internet | No requerido | Requerido | Requerido |

### Computación de altas prestaciones (HPC)

La computación de altas prestaciones (*High Performance Computing*) agrega capacidad de cálculo para resolver problemas inabordables por sistemas convencionales: simulación numérica, predicción meteorológica y climática, genómica, dinámica de fluidos o entrenamiento de modelos de inteligencia artificial. Su rendimiento se mide en **FLOPS** (operaciones de coma flotante por segundo).

- **Arquitectura actual**: clústeres masivamente paralelos de miles de nodos, cada vez más **heterogéneos** (CPU + aceleradores GPU), con redes de interconexión de baja latencia (InfiniBand), sistemas de ficheros paralelos (Lustre, IBM Storage Scale/GPFS) y gestores de colas de trabajos (Slurm).
- **Programación paralela**: **MPI** (paso de mensajes entre nodos, memoria distribuida), **OpenMP** (memoria compartida dentro del nodo) y modelos para GPU (CUDA, OpenCL).
- **Escalas**: tras el terascale (10^12 FLOPS) y el petascale (10^15, alcanzado en 2008), la barrera actual es el **exascale** (10^18 FLOPS), superada por primera vez en **2022** por el sistema Frontier (EE. UU.).
- **TOP500**: lista de referencia de los 500 supercomputadores más potentes, actualizada **cada junio y noviembre** con el benchmark **HPL (LINPACK)**, que da el rendimiento sostenido (**Rmax**) frente al pico teórico (Rpeak). La complementan la **Green500** (eficiencia energética, FLOPS/vatio) y el benchmark HPCG. En la lista de junio de 2025, el número 1 es **El Capitan** (LLNL, EE. UU.), con un Rmax de **1,742 exaflops**, y los tres primeros puestos son sistemas exascale estadounidenses (El Capitan, Frontier y Aurora).
- **EuroHPC JU** (Empresa Común Europea de Informática de Alto Rendimiento, creada en 2018): financia y opera la red europea de supercomputación: los sistemas pre-exascale **LUMI** (Finlandia), **Leonardo** (Italia) y **MareNostrum 5** (España), y **JUPITER** (Forschungszentrum Jülich, Alemania), el **primer exascale europeo**, inaugurado en 2025.
- **España**: el **Barcelona Supercomputing Center (BSC-CNS)** opera **MareNostrum 5**, con un rendimiento pico de unos **314 petaflops**; la **Red Española de Supercomputación (RES)**, ICTS coordinada por el BSC, da acceso competitivo a los supercomputadores españoles (MareNostrum, Finisterrae del CESGA, Picasso, Tirant de la Universitat de València, entre otros).

## La nube: definición y modelos de despliegue

Según la definición de referencia del **NIST (SP 800-145, 2011)**, la computación en la nube es un modelo que habilita el **acceso ubicuo y bajo demanda, a través de la red, a un conjunto compartido de recursos de computación configurables** (redes, servidores, almacenamiento, aplicaciones y servicios) que pueden aprovisionarse y liberarse rápidamente con un esfuerzo mínimo de gestión o de interacción con el proveedor.

El NIST enumera **cinco características esenciales**:

- **Autoservicio bajo demanda**: el cliente aprovisiona recursos por sí mismo, sin intervención humana del proveedor.
- **Amplio acceso a través de la red**: los servicios se consumen por mecanismos estándar desde cualquier tipo de cliente.
- **Agrupación de recursos (resource pooling)**: los recursos del proveedor se comparten entre múltiples clientes (multitenencia) y se asignan dinámicamente.
- **Elasticidad rápida**: los recursos se amplían o reducen con agilidad, incluso automáticamente, dando apariencia de capacidad ilimitada.
- **Servicio medido**: el uso se monitoriza, controla y factura de forma transparente (**pago por uso**).

Sus ventajas e inconvenientes principales:

- **Ventajas**: sin inversión inicial en infraestructura (el gasto pasa de CAPEX a OPEX), despliegue rápido, elasticidad ante picos de demanda, actualizaciones y mantenimiento delegados en el proveedor, y foco de la organización en su negocio.
- **Inconvenientes**: dependencia del proveedor (*lock-in*) y de la conectividad, riesgos de seguridad, privacidad y cumplimiento normativo (localización y jurisdicción de los datos), costes crecientes si no se gobierna el consumo y acuerdos de nivel de servicio (SLA) que hay que negociar y vigilar.

### Modelos de despliegue

El NIST define **cuatro modelos de despliegue**:

- **Nube pública**: la infraestructura es del proveedor y se ofrece abiertamente a cualquier cliente. Evita inversiones y ofrece máxima elasticidad, a cambio de menor control sobre la infraestructura y de depender del contrato y del SLA en materia de seguridad y disponibilidad.
- **Nube privada**: la infraestructura se dedica en exclusiva a una organización, en sus propias instalaciones (*on-premise*) u hospedada por un tercero. Máximo control y privacidad de los datos, a cambio de mayor inversión y menor escalabilidad.
- **Nube comunitaria**: infraestructura compartida por una comunidad de organizaciones con requisitos comunes (por ejemplo, administraciones públicas), que permite especializarla en esos requisitos.
- **Nube híbrida**: combina dos o más de las anteriores, manteniendo lo sensible en la nube privada y aprovechando la pública para lo demás; exige gestionar y conectar ambos entornos.

## Modelos de servicio: IaaS, PaaS, SaaS

Los modelos de servicio se distinguen por el **nivel de abstracción** que ofrecen y por el reparto de responsabilidades entre proveedor y cliente.

- **IaaS (Infrastructure as a Service)**: el proveedor ofrece la infraestructura básica (capacidad de proceso, almacenamiento y red) de forma elástica; el cliente gestiona el sistema operativo y todo lo superior. Es el modelo de mayor control y flexibilidad. Ejemplos: **Amazon EC2**, Google Compute Engine, Azure Virtual Machines.
- **PaaS (Platform as a Service)**: el proveedor ofrece una plataforma completa para desarrollar, probar, desplegar y mantener aplicaciones (entorno de ejecución, middleware, bases de datos), y el cliente se centra solo en su aplicación. Ejemplos: **Google App Engine**, AWS Elastic Beanstalk, Azure App Service, Heroku, Red Hat OpenShift.
- **SaaS (Software as a Service)**: el proveedor ofrece la aplicación final, accesible desde un cliente ligero (normalmente el navegador), y gestiona todo lo demás. Ejemplos: correo web, **Microsoft 365**, Google Workspace, Salesforce, Dropbox.

Reparto de responsabilidades (modelo de **responsabilidad compartida**):

| Capa | IaaS | PaaS | SaaS |
| --- | :---: | :---: | :---: |
| Aplicaciones | Cliente | Cliente | Proveedor |
| Entorno de ejecución y middleware | Cliente | Proveedor | Proveedor |
| Sistema operativo | Cliente | Proveedor | Proveedor |
| Virtualización, servidores, almacenamiento y red | Proveedor | Proveedor | Proveedor |

Los **datos, su clasificación y el control de accesos son siempre responsabilidad del cliente**, sea cual sea el modelo.

Otros modelos derivados (**XaaS**, «todo como servicio»):

- **FaaS (Function as a Service)**: ejecución de funciones dirigida por eventos, base del serverless (ver tendencias).
- **CaaS (Containers as a Service)**: contenedores y su orquestación gestionados por el proveedor (tema [44](44-virtualizacion-y-contenedores.md)).
- **DBaaS, DRaaS...**: bases de datos gestionadas, recuperación ante desastres y otros servicios especializados.
- **Almacenamiento en la nube**: se ofrece en tres tipos: **de bloques** (discos para máquinas virtuales), **de ficheros** (carpetas compartidas) y **de objetos**, el modelo nativo de la nube por su escalabilidad (Amazon S3, Azure Blob Storage).

## Centro de datos definido por software (SDDC)

El SDDC (*Software-Defined Data Center*) es la arquitectura en la que **todos los elementos de la infraestructura (computación, red, almacenamiento y seguridad) se virtualizan y se entregan como servicio**, con la gestión del centro completamente automatizada por software. Es la base tecnológica de la nube privada y de los grandes proveedores cloud.

Sus pilares:

- **Computación virtualizada**: hipervisores que abstraen los servidores físicos (tema [44](44-virtualizacion-y-contenedores.md)).
- **Redes definidas por software (SDN)**: separan el plano de control del plano de datos y permiten crear y configurar redes por software (tema [73](73-virtualizacion-de-redes.md)).
- **Almacenamiento definido por software (SDS)**: abstrae el almacenamiento del hardware y lo agrega en pools gestionados por políticas.
- **Capa de gestión y automatización**: orquestación, autoservicio e **infraestructura como código**, que aplican políticas de forma consistente en todo el centro.

La **infraestructura hiperconvergente (HCI)** es su materialización comercial más habitual (tema [43](43-centros-de-proceso-de-datos.md)). Ventajas: agilidad en la provisión, consistencia de la configuración y eficiencia operativa; retos: complejidad de la implantación inicial, necesidad de personal especializado y consideraciones de seguridad y cumplimiento.

## Tendencias: serverless y edge computing

- **Serverless computing**: el proveedor asume por completo el aprovisionamiento, el escalado y la administración de los servidores; el cliente paga **solo por la ejecución real** de su código, no por capacidad reservada. Su modelo principal es el **FaaS**: el código se empaqueta en funciones que se ejecutan como respuesta a eventos, con escalado automático (incluso a cero instancias). Ejemplos: AWS Lambda, Azure Functions, Google Cloud Functions.
    - **Ventajas**: coste proporcional al uso, sin administración de infraestructura, escalado inmediato.
    - **Inconvenientes**: latencia de arranque en frío, límites de tiempo y memoria por ejecución y fuerte dependencia del proveedor.
- **Edge computing (computación en el borde)**: lleva el procesamiento y el almacenamiento **cerca de donde se generan los datos**, en lugar de depender solo de centros de datos remotos: reduce la **latencia** y el consumo de ancho de banda, y es clave para IoT, el análisis en tiempo real y las redes 5G (temas [76](76-redes-inalambricas-y-5g.md) y [77](77-internet-de-las-cosas-y-redes-de-sensores.md)). El **fog computing** es la capa intermedia que conecta el borde con la nube, y los micro-CPD su soporte físico (tema [43](43-centros-de-proceso-de-datos.md)).
- **Multicloud y nube híbrida**: combinación de varios proveedores y de nube propia para evitar la dependencia de un único proveedor y cumplir requisitos de soberanía del dato; su reto es la gestión y la seguridad unificadas de entornos heterogéneos.

## La nube en las administraciones públicas

El uso de servicios en la nube por el sector público está condicionado por el **Esquema Nacional de Seguridad (RD 311/2022**, tema [29](29-esquema-nacional-de-seguridad.md)), que le dedica una medida específica del Anexo II:

- **op.nub.1 (Protección de servicios en la nube)**: los sistemas que suministren un servicio en la nube a organismos del sector público deberán cumplir las medidas de seguridad **en función del modelo de servicio (SaaS, PaaS, IaaS)** definidas en las guías CCN-STIC de aplicación. Cuando se utilicen servicios de terceros, sus sistemas deberán ser **conformes con el ENS** o cumplir una guía CCN-STIC con requisitos de auditoría de pruebas de penetración, transparencia, cifrado y gestión de claves y **jurisdicción de los datos**.
    - **Refuerzo R1** (categorías media y alta): los servicios deberán estar **certificados** bajo una metodología reconocida por el Organismo de Certificación del Esquema Nacional de Evaluación y Certificación de la Seguridad de las TI.
    - **Refuerzo R2** (categoría alta): configuración conforme a las guías CCN-STIC de configuración de seguridad específicas, para usuario y proveedor.
- **Conformidad exigible en la contratación**: los proveedores deben poder exhibir la **Declaración de Conformidad** con el ENS (sistemas de categoría básica) o la **Certificación de Conformidad** (categorías media y alta), también respecto de los sistemas del proveedor final cuando se contrata a través de intermediarios.
- **CCN-STIC 823, «Utilización de servicios en la nube»** (edición de diciembre de 2019, revisada en septiembre de 2020; anterior al RD 311/2022): guía del CCN con los riesgos, el clausulado contractual y los SLA, y un **decálogo de recomendaciones** que sintetiza el proceso: categorizar el sistema y elaborar la declaración de aplicabilidad, realizar el análisis de riesgos, acogerse a un perfil de cumplimiento específico si procede, fijar las condiciones contractuales antes de contratar (en pliegos: servicio, registros de actividad, gestión de incidentes, copias de seguridad y finalización del servicio), supervisar el cumplimiento del proveedor (CSP), hacer seguimiento periódico de los **SLA** y de la información del servicio, y aprobar una normativa de seguridad específica para los usuarios de la nube.
- **Nube de la Administración**: la AEAD ofrece a las AAPP servicios de nube privada/comunitaria sobre la Red SARA (nubeSARA), que se estudian con los servicios comunes de interoperabilidad (tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)).

## Supuesto práctico: migración a la nube de los servicios de un organismo

**Enunciado**: un organismo autonómico debe abandonar en **18 meses** el CPD que ocupa en un edificio que va a venderse. Su inventario de servicios: **correo y ofimática** (1.800 buzones en servidores propios), **portal web y sede electrónica** (aplicaciones Java con datos personales), un **sistema de gestión de expedientes** cliente-servidor legado sobre base de datos Oracle, **entornos de desarrollo y preproducción**, y las **copias de seguridad**. El sistema de información está categorizado en el ENS como de **categoría MEDIA**. Construir un CPD propio se estima en **1,4 M€** de inversión más su operación; la dirección pide evaluar la **migración a la nube**.

**Se pide**:

- a) Asignar a cada carga un modelo de servicio (IaaS/PaaS/SaaS) y una estrategia de migración.
- b) Elegir y justificar el modelo de despliegue.
- c) Determinar los requisitos de seguridad y cumplimiento (ENS, RGPD, contrato).
- d) Analizar el impacto económico, los riesgos y el gobierno del gasto.

**Resolución**:

**a) Modelo de servicio y estrategia por carga**

Las estrategias de migración habituales son las «**6 R**»: *rehost* (mover tal cual), *replatform* (ajustes menores), *refactor* (rediseñar para la nube), *repurchase* (sustituir por SaaS), *retire* (eliminar) y *retain* (mantener donde está).

| Carga | Modelo | Estrategia |
| --- | --- | --- |
| Correo y ofimática | **SaaS** | *Repurchase*: suite en nube; desaparecen los servidores y su administración |
| Portal y sede electrónica | **PaaS**/CaaS | *Replatform*: contenedores sobre plataforma gestionada (tema [44](44-virtualizacion-y-contenedores.md)) |
| Gestión de expedientes (legado) | **IaaS** | *Rehost* (*lift and shift*): VM equivalentes; su modernización se aborda después, sin atarla al plazo del traslado |
| Desarrollo y preproducción | IaaS/PaaS | *Rehost* con **apagado programado** fuera de horario e infraestructura como código |
| Copias de seguridad | Almacenamiento **de objetos** | Copia externa **inmutable** de la regla 3-2-1 (tema [45](45-sistemas-de-almacenamiento.md)), en niveles de acceso esporádico |

**b) Modelo de despliegue**

- **Nube híbrida** con predominio de **nube pública** de un proveedor con **región en la UE**: es la que aporta la elasticidad, los servicios gestionados y la velocidad que exige el plazo de 18 meses con un equipo reducido.
- La **nube privada** (reconstruir infraestructura propia) reproduce el problema que se quiere evitar; la **comunitaria** (nubeSARA o la nube autonómica, tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)) se valora para cargas administrativas estables si su catálogo las cubre.
- Mientras conviven entornos durante la migración por olas, la conectividad privada es imprescindible: enlaces dedicados o VPN con las sedes y acceso a la **Red SARA**.

**c) Seguridad y cumplimiento**

- **ENS, medida op.nub.1**: en categoría **MEDIA** aplica el **refuerzo R1**: los servicios en la nube deben estar **certificados**; en la contratación se exige la **Certificación de Conformidad con el ENS** de los servicios del proveedor (también del proveedor final si se contrata a través de intermediarios).
- **CCN-STIC 823**: seguir su decálogo: categorización y declaración de aplicabilidad previas, **análisis de riesgos** (tema [30](30-analisis-y-gestion-de-riesgos.md)), condiciones fijadas **en los pliegos antes de contratar** (SLA, registros de actividad, gestión de incidentes, copias de seguridad y **reversibilidad al finalizar el servicio**), supervisión continua del proveedor y normativa de seguridad específica para los usuarios de la nube.
- **RGPD**: el proveedor actúa como **encargado del tratamiento** (contrato del art. 28 RGPD); datos y copias en la **UE**, garantías frente a transferencias internacionales, cifrado en tránsito y en reposo y gestión de claves documentada (tema [53](53-proteccion-de-datos-personales.md)).
- **Responsabilidad compartida**: los **datos, su clasificación y el control de accesos son siempre responsabilidad del organismo**; en IaaS lo son también el sistema operativo, su bastionado y sus parches.

**d) Economía, riesgos y gobierno del gasto**

- **De CAPEX a OPEX**: se evita la inversión de 1,4 M€ y el gasto pasa a ser operativo y proporcional al uso; la comparación correcta es el **TCO a 4-5 años** (computando personal, licencias, comunicaciones y salida de datos), no la cuota mensual contra la inversión.
- **Palancas de ahorro**: *rightsizing* de las VM migradas (el legado suele estar sobredimensionado), **capacidad reservada** para las cargas estables (descuentos típicos del 30-60 % sobre el precio bajo demanda), apagado de los entornos no productivos y niveles fríos para el archivo.
- **Riesgos**: ***lock-in*** del proveedor (mitigado con contenedores, estándares abiertos y plan de reversibilidad contractual), **costes de salida de datos** (*egress*), dependencia de la conectividad (enlaces redundantes) y gasto descontrolado (gobierno **FinOps**: etiquetado de recursos por servicio, presupuestos y alertas de consumo).
- **Plan por olas**: primero el correo (SaaS) y los entornos no productivos; después el portal y la sede (PaaS); por último el legado (IaaS), cuya modernización queda como proyecto posterior ya en la nube.

## Fuentes {.unnumbered .unlisted}

- NIST Special Publication 800-145, The NIST Definition of Cloud Computing (septiembre de 2011).
- Real Decreto 311/2022, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024): Anexo II, medida op.nub.1.
- CCN-STIC 823, Utilización de servicios en la nube (edición diciembre de 2019, revisión septiembre de 2020).
- TOP500 (lista de junio de 2025; se actualiza cada junio y noviembre) y EuroHPC JU.
- Portales del BSC-CNS y de la Red Española de Supercomputación (RES).
