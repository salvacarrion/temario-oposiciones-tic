# Ciberseguridad

## Marco normativo de la ciberseguridad

La ciberseguridad en la Administración de la Generalitat se basa en una serie de normativas que establecen los principios y requisitos para proteger adecuadamente la información y los servicios prestados.

### Normativas básicas:

- **RGPD (Reglamento UE 2016/679)**: Reglamento General de Protección de Datos que establece las directrices para el tratamiento y protección de datos personales en la Unión Europea.
- **LOPD-GDD (Ley Orgánica 3/2018)**: Ley Orgánica de Protección de Datos Personales y Garantía de los Derechos Digitales, que adapta el RGPD al marco legal español y garantiza los derechos digitales de la ciudadanía.
- **ENS (Real Decreto 311/2022)**: **Esquema Nacional de Seguridad** que establece los principios básicos y requisitos mínimos para una protección adecuada de la información y servicios electrónicos en el sector público.
- **LPIC (Ley 8/2011)**: Ley de Protección de Infraestructuras Críticas que regula las medidas necesarias para proteger las infraestructuras esenciales para la sociedad.
- **NIS (Real Decreto 12/2018)**: Norma que transpone la Directiva NIS sobre la seguridad de las redes y sistemas de información en la Unión Europea.

La **normativa de la Generalitat Valenciana (GVA)** incluye:

- **Política de Seguridad (Decreto 66/2012)**: Establece las directrices y principios para la seguridad de la información en la GVA.
- **Organización de la Seguridad (Decreto 130/2012)**: Define la estructura organizativa y responsabilidades en materia de seguridad de la información.
- **Uso Seguro de Medios Tecnológicos (Orden 19/2013)**: Regula el uso seguro y adecuado de los medios tecnológicos por parte del personal de la GVA.
- **Resoluciones**: Como la estandarización del **Puesto de Trabajo Normalizado (PTN)**, que unifica criterios y medidas de seguridad en los puestos de trabajo.

### Proceso de Seguridad basado en la Gestión de Riesgos

El proceso de seguridad se fundamenta en la **gestión de riesgos**, siguiendo estos pasos:

1. **Identificación de activos**: Reconocer y catalogar los activos de información y servicios que deben protegerse.
2. **Valoración de activos**: Evaluar la importancia y criticidad de cada activo.
3. **Análisis de Riesgos y Amenazas**: Identificar posibles amenazas y vulnerabilidades, y evaluar el riesgo asociado.
4. **Implementación de Salvaguardas y Riesgo Residual**: Aplicar medidas de seguridad para mitigar riesgos y determinar el riesgo residual aceptable.
5. **Mejora continua**: Realizar revisiones periódicas y actualizar las medidas de seguridad según sea necesario.

**Protección de Datos:** LOPD-GDD (Ley Orgánica 3/2018) y RGPD (Reglamento UE 2016/679)

En complemento al ENS, la normativa de **Protección de Datos** es esencial para la ciberseguridad:

- **Objeto**: Proteger los derechos y libertades fundamentales de las personas físicas, en particular su **derecho a la protección de datos personales**.
- **Finalidad**: Garantizar los **derechos digitales** de la ciudadanía.
- **Obliga**: A todo aquel que trate datos de carácter personal.
- **Derechos de los ciudadanos**: (Mnemo: ARSULIPO)
    - **Acceso**
    - **Rectificación**
    - **Supresión**
    - **Limitación**
    - **Portabilidad**
    - **Oposición**

### Esquema Nacional de Seguridad (ENS): Real Decreto 311/2022

El **ENS** tiene como objetivo establecer los principios y requisitos para proteger adecuadamente la información y los servicios electrónicos en el sector público. Su finalidad es **generar confianza en los medios electrónicos de la administración**.

**Funciones y Roles clave en el ENS**:

- **Responsable de Información (RINFO)**: Determina la **categoría del sistema** en función de la información manejada. Esta función es **indelegable**.
- **Responsable de Servicio (RSER)**: Determina los **requisitos de los servicios** prestados.
- **Responsable de Seguridad (RSEG)**:
    - Toma decisiones de seguridad basándose en los requisitos del RINFO y RSER.
    - Firma la **Declaración de Aplicabilidad**, que contiene las medidas de seguridad seleccionadas.
    - Analiza los informes de **Autoevaluación** y **Auditoría**.
- **Responsable del Sistema (RSIS)**: Implementa las medidas de seguridad definidas por el RSEG.

### Seguridad en los Proyectos TIC

Para garantizar la seguridad en los proyectos de Tecnologías de la Información y la Comunicación (TIC), se siguen estos pasos:

1. **Cumplimiento normativo**: Asegurar que el proyecto cumple con el **ENS**, el **RGPD** y la **LOPDGDD**.
2. **Categorización del Sistema**: El **Responsable de Información** (y el **Responsable de Servicio**, si aplica) determina la categoría del sistema.
3. **Establecimiento de Requisitos de Seguridad**: El RINFO define los requisitos funcionales y no funcionales de seguridad.
4. **Análisis de Riesgos**: Utilizar metodologías como **MAGERIT** y herramientas como **PILAR** para identificar y evaluar riesgos.
5. **Desarrollo seguro**: Aplicar prácticas de desarrollo seguro utilizando guías como **gvLOGOS-seg** y recursos de **OWASP**.
6. **Verificación de Seguridad**: Realizar auditorías estáticas y dinámicas, así como **tests de intrusión**, para verificar la eficacia de las medidas de seguridad implementadas.

### Roles de la Nueva Política de Seguridad

- **Gobierno**: Establece los **requisitos de seguridad** que deben cumplirse.
- **Supervisión**: Toma las decisiones necesarias para satisfacer los requisitos de seguridad.
- **Operaciones**: Se encarga de la **implantación de las medidas de seguridad**.

### Proceso de Seguridad basado en la Gestión de Riesgos

El proceso de seguridad se basa en los siguientes pasos:

- **Identificación de Activos**: Determinar qué información y servicios deben ser protegidos.
- **Valoración de Activos**: Evaluar los activos según las dimensiones **DICTA**.
- **Análisis de Riesgos y Amenazas**: Calcular el riesgo como el producto del **Impacto** por la **Probabilidad** de ocurrencia.
- **Implementación de Salvaguardas y Riesgo Residual**: Aplicar medidas de seguridad y determinar el riesgo que permanece después de dichas medidas.
- **Revisión y Mejora**: Realizar **auditorías** y ajustes continuos para mejorar el sistema de seguridad.

### Herramientas de Ciberseguridad

Para apoyar el proceso de seguridad, la GVA utiliza diversas herramientas:

- **CLAUDIA**: Herramienta para la detección de amenazas complejas en el puesto de usuario.
- **microCLAUDIA**: Cliente ligero de CLAUDIA para dispositivos con recursos limitados.
- **SAT INET**: **Sistema de Alerta Temprana de Internet**, que monitorea y alerta sobre amenazas emergentes.
- **CARMEN**: Herramienta para la detección de **Ataques Avanzados Persistentes (APT)**.
- **GLORIA**: Plataforma para la gestión integral de incidentes y amenazas de ciberseguridad.
- **Argos**: Módulo de GLORIA dedicado a la monitorización y recolección de eventos de seguridad.
- **LUCIA**: **Listado Unificado de Coordinación de Incidentes y Amenazas**, centraliza la información sobre incidentes.
- **PILAR**: Herramienta para el análisis y gestión de riesgos en sistemas de información, siguiendo la metodología **MAGERIT**.
- **IRIS**: **Indicadores Relacionados para Informar de la Situación**, proporciona métricas y estadísticas sobre ciberseguridad.
- **REYES**: **Repositorio Común y Estructurado de Amenazas y Código Dañino**, almacena información sobre amenazas conocidas.
