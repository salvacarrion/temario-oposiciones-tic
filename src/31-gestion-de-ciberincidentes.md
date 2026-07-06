# Gestión de ciberincidentes

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Gestión de ciberincidentes

### Fases: Preparación, Identificación, Contención, Mitigación, Recuperación y Actuaciones Post-Incidente

La gestión de ciberincidentes implica un ciclo de vida estructurado en varias fases esenciales:

### 1. Preparación

Después de realizar un análisis de riesgos, se identifican y despliegan medidas de seguridad específicas. En esta fase, se forma un Equipo de Respuesta a Ciberincidentes (ERC), dotado de herramientas y recursos necesarios para actuar. La preparación incluye también el desarrollo de políticas de seguridad y la formación continua del personal para que todos conozcan los protocolos de respuesta.

### 2. Identificación

La fase de identificación engloba la detección, análisis y notificación de brechas de seguridad. Este proceso implica monitorear constantemente el entorno para detectar signos de posibles incidentes. Los elementos clave en esta fase son:

- **Precursores**: Indicios de que un incidente podría ocurrir en el futuro, tales como escaneos de puertos, anuncios de nuevos exploits o amenazas inminentes.
- **Indicadores**: Señales de que un incidente ya ha ocurrido o está en curso, incluyendo alertas de antivirus, desbordamientos de memoria (overflows) o tráfico inusual.

### 3,4,5. Contención, Mitigación y Recuperación

Estas fases consisten en:

- **Contención**: Limitar la propagación del incidente para evitar mayores daños. Se aíslan los sistemas comprometidos y se aplican medidas temporales para contener el daño.
- **Mitigación**: Eliminar o neutralizar el incidente. Puede implicar la eliminación de malware, parches de seguridad y restauración de configuraciones.
- **Recuperación**: Restaurar el funcionamiento normal de los sistemas afectados, asegurando que no existan vulnerabilidades residuales que permitan recurrencias del incidente.

### 6. Actuaciones Post-Incidente

Tras resolver el ciberincidente, se realiza un análisis detallado para comprender su causa raíz y los costos asociados. Se redacta un informe exhaustivo que incluye las medidas preventivas recomendadas para evitar incidentes similares en el futuro. La recolección y custodia de evidencias durante esta fase es fundamental para posibles acciones legales y para apoyar el análisis posterior.

### Amenazas y Vectores de Ataque

Las amenazas a la seguridad pueden provenir de diversas fuentes y tomar múltiples formas. La "Guía Nacional de Notificación y Gestión de Ciberincidentes" ofrece un glosario detallado que clasifica los diferentes tipos de amenazas y vectores de ataque, incluidos malware, ataques de denegación de servicio (DDoS), ingeniería social y explotación de vulnerabilidades.

### Clasificación de Ciberincidentes

Los ciberincidentes se clasifican según el tipo y la naturaleza del ataque:

- **Categorías**: Contenido abusivo, dañino, obtención de información, intento de intrusión, disponibilidad, compromiso de información, fraude, vulnerabilidad y otros.
- **Tipos específicos**: Spam, delitos de odio, contenido sexual explícito, escaneo de redes, ingeniería social, explotación de vulnerabilidades, ataques DDoS, mala configuración, sabotaje, entre otros.

### Factores a Valorar en la Clasificación de Incidentes

- **Tipo de amenaza**: Código dañino, intrusiones, fraude, etc.
- **Origen de la amenaza**: Puede ser interna o externa.
- **Categoría de seguridad** de los sistemas afectados, basada en su criticidad y confidencialidad.
- **Perfil de los usuarios afectados**: Según su posición en la estructura organizativa y sus privilegios de acceso a información sensible o confidencial.
- **Número y tipología de sistemas afectados**: Es decir, la extensión y naturaleza de los sistemas comprometidos.
- **Impacto del ciberincidente** sobre la operativa de la organización.
- **Requerimientos legales y regulatorios** que podrían implicar responsabilidades específicas o acciones obligatorias.

### Detección de Ciberincidentes

La detección puede basarse en **precursores** o **indicadores**:

- **Precursor**: Señales de que un incidente podría ocurrir en el futuro.
    - **Ejemplos:** Escaneo de puertos, Anuncios de nuevos exploits o amenazas conocidas.
- **Indicador**: Evidencias de que un incidente está ocurriendo o ya ha ocurrido.
    - **Ejemplos:** Alertas del antivirus, Tráfico de red inusual, Overflows y comportamientos anómalos en sistemas o aplicaciones.

### Peligrosidad de los Ciberincidentes

La peligrosidad se clasifica en cinco niveles: BAJO, MEDIO, ALTO, MUY ALTO y CRÍTICO, y su nivel de impacto se evalúa según el Esquema Nacional de Seguridad (ENS).

### Seguimiento por parte del CCN-CERT

El seguimiento de incidentes de seguridad en España se realiza mediante la herramienta LUCIA, que permite coordinar y monitorizar los ciberincidentes. La notificación al CCN-CERT es obligatoria en casos de incidentes de peligrosidad ALTA, MUY ALTA o CRÍTICA.

### Métricas para la Gestión de Incidentes

Existen varias métricas para evaluar la efectividad en la resolución de ciberincidentes:

- **Métricas de implantación, resolución y recursos**.
- **Métricas específicas de gestión de incidentes**, como la **M5** y **M6**:
    - **M5**: Estado de cierre de incidentes. Método: Número de incidentes cerrados sin respuesta / Total notificados.
    - **M6**: Estado de cierre de incidentes con peligrosidad MUY ALTA/CRÍTICA. Método: Número de incidentes cerrados sin respuesta / Total notificados.

### Recolección y Custodia de Evidencias

Es esencial para la resolución de incidentes y su validez legal. La recolección cuidadosa de evidencias permite apoyar tanto las acciones de respuesta como la posible persecución judicial del responsable del incidente.

### LUCIA: Herramienta de Coordinación de Incidentes y Amenazas

LUCIA (Listado Unificado de Coordinación de Incidentes y Amenazas) es una herramienta de gestión de tickets que permite a los organismos del ámbito del ENS gestionar sus ciberincidentes. Facilita la integración y sincronización de los incidentes registrados con el CCN-CERT, permitiendo una consolidación y coordinación en el Nodo de Coordinación del CCN-CERT.

**Nota:** Estudiar las “novias” del ENS (ej.: CARMEN, CLARA, CLAUDIA, IRIS, LUCIA,...)

### Funciones de un CERT/CSIRT

Los equipos de respuesta ante emergencias informáticas (CERT, por sus siglas en inglés, o CSIRT) son responsables de dar soporte en la gestión de ciberincidentes:

- **CCN-CERT**: Es el CERT del Centro Criptológico Nacional, parte del Centro Nacional de Inteligencia (CNI).
- **INCIBE-CERT**: Está gestionado por el Instituto Nacional de Ciberseguridad de España.
- **CNPIC**: Forma parte del Centro Nacional de Protección de Infraestructuras y Ciberseguridad.
- **ESP-DEF-CERT**: Pertenece al Mando Conjunto de Ciberdefensa.

### Metodología de Reporte

El sistema de reporte se organiza mediante una **ventanilla única** que sigue los siguientes pasos:

1. **Notificación inicial** al CERT/CSIRT de referencia.
2. **Sincronización** con el organismo receptor o la autoridad competente.
3. **Inicio de la investigación** interna.
4. **Notificación completa** mediante el formulario específico.
5. **Investigación policial o judicial** si se considera necesario.

### Tipos de Seguridad: Activa y Pasiva

- **Seguridad Activa**: Medidas que buscan evitar la ocurrencia de un ataque, tales como contraseñas seguras, encriptación de datos, antivirus actualizados, auditorías de seguridad y formación continua del personal.
- **Seguridad Pasiva**: Acciones que mitigan los efectos de un ataque una vez que ha ocurrido, como copias de seguridad, uso de servicios en la nube, hardware resistente a fallos y particiones lógicas del disco duro.
