# Testeo de software

Las pruebas de software evalúan la calidad del producto y encuentran defectos antes de que lleguen a producción. El marco de referencia de este tema es el programa de estudio **ISTQB CTFL v4.0** (*Certified Tester Foundation Level*, 2023), el estándar de facto de la disciplina, que reformuló principios, niveles y técnicas respecto a la versión 3.1.

## Fundamentos del testeo (ISTQB)

Probar no es solo ejecutar el software: es un **proceso** que incluye actividades estáticas (revisiones, análisis) y dinámicas (ejecución), con objetivos que van más allá de encontrar defectos: evaluar productos de trabajo, dar confianza en el nivel de calidad, reducir el riesgo y aportar información para decidir. La prueba es una forma de control de calidad (QC); el aseguramiento (QA) se orienta al proceso (ver tema [25](25-calidad-del-software.md)).

### Error, defecto y fallo

- **Error (equivocación)**: acción humana que produce un resultado incorrecto.
- **Defecto**: imperfección en un producto de trabajo (código, requisitos, diseño), resultado de un error.
- **Fallo**: comportamiento incorrecto observable del sistema en ejecución, provocado por un defecto (no todo defecto llega a manifestarse como fallo).
- **Causa raíz**: motivo último que originó el error; su análisis permite prevenir defectos similares.

### Los 7 principios de la prueba (CTFL 4.0)

1. **La prueba muestra la presencia de defectos, no su ausencia**: aunque no se encuentren defectos, no queda demostrada la corrección del sistema.
2. **La prueba exhaustiva es imposible**: en lugar de probarlo todo, se usan técnicas, priorización y prueba basada en el riesgo para concentrar el esfuerzo.
3. **La prueba temprana ahorra tiempo y dinero**: los defectos eliminados pronto no se propagan; estáticas y dinámicas deben empezar lo antes posible.
4. **Los defectos se agrupan**: unos pocos componentes concentran la mayoría de los defectos (principio de Pareto); es una entrada clave de la prueba basada en el riesgo.
5. **Las pruebas se desgastan**: repetidas muchas veces pierden eficacia para detectar defectos nuevos y hay que modificarlas (la versión 3.1 lo llamaba «paradoja del pesticida»); la excepción útil es la regresión automatizada.
6. **La prueba depende del contexto**: no hay un enfoque universal.
7. **Falacia de la ausencia de defectos**: probar todos los requisitos y corregir lo encontrado no garantiza un sistema que satisfaga a los usuarios; además de verificación hace falta validación.

### Actividades del proceso de prueba

- **Planificación**: definir los objetivos y el enfoque dentro de las restricciones del contexto.
- **Monitorización y control**: comparar el avance real con el plan y tomar las medidas necesarias.
- **Análisis**: responde a «¿qué probar?»; identifica y prioriza las **condiciones de prueba** a partir de la base de prueba y de los riesgos.
- **Diseño**: responde a «¿cómo probar?»; elabora los **casos de prueba**, identifica los elementos de cobertura y define datos y entorno de prueba.
- **Implementación**: prepara el *testware* (procedimientos, guiones, datos) y monta el entorno.
- **Ejecución**: correr las pruebas, comparar resultados reales y esperados y registrar las anomalías.
- **Compleción**: informe final, archivo del testware y lecciones aprendidas.

### Roles, equipo e independencia

- El programa 4.0 define **dos roles**: el **rol de gestión de prueba** (responsable del proceso y del equipo: planificación, monitorización y control, compleción) y el **rol de prueba** (vertiente de ingeniería: análisis, diseño, implementación y ejecución). Una misma persona puede asumir ambos.
- **Enfoque de equipo completo**: la calidad es responsabilidad compartida de todo el equipo, no solo de los probadores.
- **Independencia de la prueba**: grados crecientes (el propio autor, un compañero, un equipo de prueba independiente, probadores externos). Más independencia detecta más defectos por evitar el sesgo del autor, pero un equipo aislado puede perder colaboración y visión del producto.

## Las pruebas en el ciclo de vida: roles, niveles y tipos

El ciclo de vida de desarrollo condiciona cómo, cuándo y quién prueba. Como buena práctica, **a cada actividad de desarrollo le corresponde una actividad de prueba**, y el análisis y diseño de las pruebas de cada nivel comienza en la fase de desarrollo equivalente.

### La prueba en el ciclo de vida de desarrollo

- **Desplazamiento a la izquierda (*shift-left*)**: iniciar las pruebas cuanto antes: revisar los requisitos, análisis estático en el IDE y en CI, pruebas escritas antes que el código.
- **La prueba como impulsor del desarrollo**: **TDD** (desarrollo guiado por prueba, a nivel de componente), **ATDD/DGPA** (guiado por la prueba de aceptación, desde los criterios de aceptación) y **BDD** (guiado por el comportamiento, con escenarios *Given-When-Then*).
- **DevOps y prueba**: el pipeline CI/CD ejecuta las pruebas automatizadas en cada cambio (ver tema [26](26-control-de-versiones-integracion-continua-y-devops.md)): retroalimentación rápida y regresión constante, a cambio del esfuerzo de definir y mantener la automatización.
- **Retrospectivas**: al cerrar cada iteración o hito se analizan éxitos y mejoras del propio proceso de prueba.

### Niveles de prueba

El CTFL 4.0 define **cinco niveles** (la 3.1 no separaba las dos integraciones):

- **Prueba de componente (unitaria)**: componentes aislados; requiere arneses o marcos de prueba unitaria (xUnit); la realizan normalmente los desarrolladores en su entorno.
- **Prueba de integración de componentes**: interfaces e interacciones entre componentes; depende de la estrategia de integración (**ascendente, descendente o big-bang**).
- **Prueba de sistema**: comportamiento y capacidades del sistema completo, extremo a extremo, funcional y no funcional; suele hacerla un equipo independiente contra las especificaciones del sistema.
- **Prueba de integración de sistemas**: interfaces con otros sistemas y servicios externos; exige entornos similares al de operación.
- **Prueba de aceptación**: validación y preparación para el despliegue: el sistema satisface las necesidades del negocio. Sus formas principales son la **prueba de aceptación de usuario (PAU)**, la **de aceptación operativa**, la **contractual y de regulación** y las pruebas **alfa** (en las instalaciones del desarrollador) y **beta** (en las de los usuarios).

Los niveles se distinguen por su objeto, sus objetivos, su base de prueba, los defectos típicos que detectan y las responsabilidades.

### Tipos de prueba

- **Prueba funcional**: evalúa «qué» hace el sistema (completitud, corrección y pertinencia funcional).
- **Prueba no funcional**: evalúa «lo bien que se comporta»: las características de calidad de **ISO/IEC 25010** (eficiencia de desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad, portabilidad; ver tema [25](25-calidad-del-software.md)).
- **Prueba de caja negra**: se basa en la especificación, sin conocer la estructura interna.
- **Prueba de caja blanca**: se basa en la estructura interna (cobertura de código).
- **Pruebas asociadas al cambio**: la **prueba de confirmación** verifica que un defecto se corrigió; la **prueba de regresión**, que el cambio no ha roto nada existente (candidata prioritaria a la automatización).
- **Prueba de mantenimiento**: sobre sistemas en producción tras cambios correctivos o evolutivos; su alcance lo determina el **análisis de impacto**.

### Prueba estática y revisiones

La **prueba estática** examina productos de trabajo sin ejecutarlos (revisiones y análisis estático) y encuentra defectos pronto y a bajo coste; complementa a la dinámica. El proceso de revisión (detallado en **ISO/IEC 20246**) comprende planificación, inicio, revisión individual, comunicación y análisis, y corrección e informe.

- **Roles en las revisiones**: **gestor** (decide qué se revisa y aporta recursos), **autor** (crea y corrige el producto), **moderador o facilitador** (asegura reuniones eficaces y un entorno seguro), **escriba** (registra anomalías y decisiones), **revisor** (realiza la revisión) y **líder de la revisión** (responsabilidad general: participantes, cuándo y dónde).
- **Tipos de revisión**, de menor a mayor formalidad:
    - **Revisión informal**: sin proceso definido ni salida documentada; busca detectar anomalías.
    - **Revisión guiada (*walkthrough*)**: dirigida por el **autor**; sirve para educar, lograr consenso y detectar anomalías.
    - **Revisión técnica**: revisores técnicamente cualificados dirigidos por un **moderador**; busca consenso y decisiones sobre problemas técnicos.
    - **Inspección**: la más formal, sigue el proceso completo y busca el máximo de anomalías; recopila métricas para mejorar el proceso; el **autor no puede actuar como revisor ni escriba**.

## Técnicas de prueba

Las técnicas ayudan a derivar condiciones y casos de prueba con una cobertura medible. El CTFL 4.0 las agrupa en tres familias más los enfoques colaborativos (la «prueba de caso de uso» de la 3.1 desapareció del programa).

### Técnicas de caja negra

- **Partición de equivalencia**: dividir los datos en clases que el sistema trata igual (particiones válidas e inválidas) y probar **un valor de cada partición**.
- **Análisis del valor frontera (AVF)**: probar los **límites** de las particiones ordenadas, donde se concentran los defectos (variantes de 2 y 3 valores por frontera).
- **Prueba de tabla de decisión**: tabular combinaciones de condiciones y sus acciones; adecuada para reglas de negocio complejas.
- **Prueba de transición de estado**: modelar estados, eventos y transiciones; cobertura de todos los estados o de todas las transiciones válidas.

### Técnicas de caja blanca

- **Prueba de sentencia y cobertura de sentencia**: porcentaje de sentencias ejecutadas por las pruebas.
- **Prueba de rama y cobertura de rama**: porcentaje de ramas (condicionales e incondicionales) ejecutadas; el **100 % de cobertura de rama subsume el 100 % de sentencia**. (El programa 3.1 hablaba de «cobertura de decisión».)
- Su valor: detectan defectos en código que la especificación no cubre y miden objetivamente lo probado.

### Técnicas basadas en la experiencia

- **Predicción de errores**: anticipar las equivocaciones típicas del desarrollador (listas de defectos frecuentes, *fault attacks*).
- **Prueba exploratoria**: diseñar, ejecutar y aprender simultáneamente, a menudo en sesiones con objetivos (*session-based testing*); útil con especificaciones pobres o presión de tiempo.
- **Prueba basada en lista de comprobación**: verificar condiciones recogidas en una checklist mantenida por el equipo.

### Enfoques basados en la colaboración

Novedad del 4.0: la calidad se construye en colaboración con negocio y desarrollo, no solo se verifica:

- **Redacción colaborativa de historias de usuario**: las 3 C y los criterios INVEST (ver tema [23](23-analisis-y-diseno-de-aplicaciones.md)).
- **Criterios de aceptación**: en formato escenario (**Given-When-Then**) u orientados a reglas; son la base de prueba de la historia.
- **Desarrollo guiado por la prueba de aceptación (DGPA/ATDD)**: los casos de prueba de aceptación se escriben **antes** de desarrollar, a partir de los criterios de aceptación.

## Gestión y automatización de las pruebas

### Plan de prueba y criterios de entrada y salida

El **plan de prueba** documenta objetivos, alcance, contexto, supuestos y restricciones, implicados, comunicación, gestión del riesgo, enfoque, presupuesto y calendario.

- **Criterios de entrada**: precondiciones para empezar una actividad (recursos disponibles, material de prueba, calidad inicial mínima: por ejemplo, pruebas de humo pasadas). En ágil, **Definición de Preparado** (*Definition of Ready*).
- **Criterios de salida**: qué debe lograrse para dar la actividad por completada (cobertura alcanzada, defectos sin resolver por debajo del umbral, pruebas planificadas ejecutadas). En ágil, **Definición de Hecho** (*Definition of Done*). Agotar tiempo o presupuesto puede ser un criterio de salida válido si los implicados aceptan el riesgo.

### Estimación y priorización

- **Cuatro técnicas de estimación** del esfuerzo de prueba: **basada en proporciones** (ratios históricos de la organización, p. ej. desarrollo:prueba 3:2), **extrapolación** (medidas de las primeras iteraciones del propio proyecto), **Delphi de banda ancha** (iteración de expertos; su variante ágil es el **póker de planificación**) y **estimación de tres puntos** (optimista a, más probable m y pesimista b: E = (a + 4m + b) / 6).
- **Priorización de casos de prueba**: **basada en el riesgo**, **en la cobertura** o **en los requisitos**, condicionada siempre por las dependencias entre casos y la disponibilidad de recursos.

### Pirámide y cuadrantes de prueba

- **Pirámide de prueba** (Cohn, 2009): las capas bajas contienen pruebas pequeñas, aisladas y rápidas (**unitarias**: muchas), las intermedias pruebas de **servicio/integración** y la cúspide pocas pruebas de **extremo a extremo/interfaz** lentas y complejas. Guía el reparto del esfuerzo de automatización.
- **Cuadrantes de prueba** (Marick; Crispin y Gregory): cruzan dos ejes (orientación a negocio o a tecnología; apoyar al equipo o criticar el producto):
    - **Q1** (tecnología, apoya al equipo): componente e integración de componentes; automatizadas en CI.
    - **Q2** (negocio, apoya al equipo): funcionales, historias de usuario, API, prototipos; manuales o automatizadas.
    - **Q3** (negocio, critica el producto): exploratoria, usabilidad, PAU; normalmente manuales.
    - **Q4** (tecnología, critica el producto): no funcionales salvo usabilidad, y pruebas de humo; automatizadas.

### Riesgos y gestión de defectos

- El **riesgo** combina la probabilidad de un suceso adverso y su impacto. Los **riesgos de proyecto** afectan a la gestión (plazos, recursos, personas); los **riesgos de producto**, a la calidad (funcionalidad ausente, rendimiento pobre). La **prueba basada en el riesgo** usa el análisis del riesgo de producto para decidir dónde y con qué rigor probar.
- La **gestión de defectos** define el flujo de cada anomalía desde el descubrimiento hasta el cierre: registrar, analizar y clasificar, decidir la respuesta (corregir, aplazar, rechazar) y cerrar. Un **informe de defecto** típico incluye: identificador único, título, fecha y autor, objeto y entorno de prueba, contexto, descripción que permita reproducirlo, **resultados esperado y real**, **severidad** (impacto) y **prioridad** (urgencia de corrección), estado y referencias (plantillas en **ISO/IEC/IEEE 29119-3**).
- La monitorización se apoya en métricas de avance (casos ejecutados y pasados), cobertura, defectos (densidad, encontrados frente a corregidos) y riesgo residual, comunicadas en informes de avance y en el **informe de compleción** final.

### Herramientas y automatización

El programa agrupa las herramientas de apoyo en: gestión (pruebas, defectos, configuración), prueba estática, diseño e implementación de pruebas, **ejecución y cobertura**, pruebas no funcionales, DevOps (CI/CD), colaboración y escalado de entornos (máquinas virtuales, contenedores). Ejemplos habituales: **JUnit** (unitarias en Java), **Selenium** y **Playwright** (interfaz web), **Postman** (API), **JMeter** (rendimiento) y **SonarQube** (análisis estático), integradas en el pipeline (ver tema [26](26-control-de-versiones-integracion-continua-y-devops.md)).

Una prueba unitaria con JUnit 5 sobre el método `clasificar` del caso práctico del tema [25](25-calidad-del-software.md):

```java
@Test
void expedienteNoUrgenteNiRecurridoEsOrdinario() {
    Clasificador c = new Clasificador();
    assertEquals("ordinario", c.clasificar(false, 10, false));
}
```

- **Ventajas de la automatización**: reduce el trabajo manual repetitivo y los errores humanos (consistencia y repetibilidad), aporta medidas objetivas (cobertura), acelera la retroalimentación (detección más temprana, menor *time-to-market*) y libera a los probadores para diseñar pruebas nuevas y más profundas.
- **Riesgos**: expectativas poco realistas, subestimar el coste de introducir la herramienta y mantener los guiones, automatizar cuando lo manual es más apropiado, confiar en exceso en la herramienta (sin pensamiento crítico), dependencia del proveedor o abandono del proyecto de código abierto e incompatibilidades con la plataforma.

## Fuentes {.unnumbered .unlisted}

- ISTQB, *Probador Certificado del ISTQB. Programa de Estudio. Nivel Básico (CTFL) v4.0*, 21 de abril de 2023; traducción oficial al español del SSTQB.
- ISO/IEC 20246 (revisiones de productos de trabajo) e ISO/IEC/IEEE 29119-3 (documentación de pruebas), citados donde el programa remite a ellos.
- Cohn, M., *Succeeding with Agile*, Addison-Wesley, 2009 (pirámide de prueba).
- Crispin, L. y Gregory, J., *Agile Testing*, Addison-Wesley, 2008 (cuadrantes de prueba, sobre Marick, 2003).
