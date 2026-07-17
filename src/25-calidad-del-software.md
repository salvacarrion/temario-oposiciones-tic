# Calidad del software

La calidad del software es el grado en que un producto cumple los requisitos especificados y las necesidades de sus usuarios. Este tema repasa el aseguramiento de la calidad (del proceso y del producto), la familia de normas **ISO/IEC 25000 (SQuaRE)** con sus 8 características de calidad, las métricas con que se mide y un caso práctico de complejidad ciclomática.

## Aseguramiento de la calidad del software

Según el vocabulario de **ISO 9000:2015**, la calidad es el «grado en el que un conjunto de características inherentes de un objeto cumple con los requisitos». Aplicada al software, tiene una doble vertiente: la **calidad del proceso** (cómo se desarrolla) y la **calidad del producto** (qué se obtiene), bajo la premisa de que un buen proceso hace más probable un buen producto.

La gestión de la calidad se articula en **tres niveles**:

- **Gestión de la calidad**: define la política de calidad, los objetivos y las responsabilidades en la organización; se documenta en el **plan de calidad** del proyecto (estándares aplicables, revisiones y auditorías previstas, métricas y responsables).
- **Aseguramiento de la calidad (QA)**: conjunto de actividades **planificadas y sistemáticas** para dar confianza en que el proceso y el producto cumplen los requisitos; es **preventivo** y se orienta al proceso.
- **Control de la calidad (QC)**: verificación de productos de trabajo concretos contra sus requisitos; es **detectivo** y se orienta al producto.

Dos matices preguntables: la certificación (por ejemplo, **ISO 9001**) se otorga al **sistema de gestión** de la organización, no al software en sí; y la calidad percibida la juzga en última instancia el usuario según su experiencia y necesidades. En la organización, estas funciones se reparten entre las oficinas de calidad, las oficinas de proyectos (PMO) y los equipos de QA.

### Verificación y validación

La verificación y la validación (V&V) son el núcleo del aseguramiento:

- **Verificación**: ¿estamos construyendo el producto **correctamente**? Comprueba la conformidad de cada producto de trabajo con su especificación. Usa sobre todo **técnicas estáticas** (no ejecutan el código): revisiones técnicas y de gestión (detectan errores en fases tempranas), **inspecciones** (revisión formal con roles y lista de comprobación, método de Fagan), *walkthroughs* y análisis estático.
- **Validación**: ¿estamos construyendo el producto **correcto**? Comprueba que el software satisface las necesidades reales del usuario. Usa **técnicas dinámicas**: las pruebas, que se estudian en el tema 27.
- **Auditorías**: evaluación **independiente** del cumplimiento de procesos, estándares y procedimientos (verificación del cumplimiento normativo).

### Calidad del proceso: ISO 9001, CMMI y SPICE

- **ISO 9001:2015**: norma certificable de sistemas de gestión de la calidad, genérica para cualquier organización.
- **CMMI** (*Capability Maturity Model Integration*, hoy de ISACA; versión vigente **CMMI V3.0, 2023**): modelo de madurez de procesos con **cinco niveles**:
    1. **Inicial**: procesos impredecibles y reactivos.
    2. **Gestionado**: procesos planificados y controlados por proyecto.
    3. **Definido**: procesos estándar de la organización, proactivos.
    4. **Gestionado cuantitativamente**: procesos medidos y controlados estadísticamente.
    5. **En optimización**: mejora continua basada en datos.
- **ISO/IEC 330xx (SPICE)**: familia sucesora de ISO/IEC 15504 para la **evaluación de la capacidad de los procesos** de software, con niveles de capacidad de 0 (incompleto) a 5 (innovador).

### Modelos clásicos de calidad del producto

Antes de SQuaRE, la calidad del producto se estructuró en modelos jerárquicos de factores y criterios:

- **McCall (1977)**: **11 factores** agrupados en tres ejes: operación del producto (corrección, fiabilidad, eficiencia, integridad, usabilidad), revisión (mantenibilidad, flexibilidad, capacidad de prueba) y transición (portabilidad, reusabilidad, interoperabilidad).
- **Boehm (1978)**: árbol de características orientado a la utilidad general, la mantenibilidad y la portabilidad.
- **ISO/IEC 9126** (1991, revisada en 2001): seis características (funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad, portabilidad); es el antecedente directo de la ISO/IEC 25010, que la sustituyó.

## Familia ISO/IEC 25000 (SQuaRE): las 8 características de calidad

La familia **ISO/IEC 25000**, conocida como **SQuaRE** (*System and Software Quality Requirements and Evaluation*), proporciona el marco común para especificar los requisitos de calidad del producto de software y evaluarla. Sustituye a las antiguas ISO/IEC 9126 (modelo de calidad) e ISO/IEC 14598 (evaluación).

### Divisiones de la familia

- **ISO/IEC 2500n. División de gestión de calidad**: términos, definiciones y guía de la familia (25000) y planificación y gestión de la evaluación (25001).
- **ISO/IEC 2501n. División de modelo de calidad**: modelos de calidad del producto (**25010**), de los datos (**25012**), de la calidad en uso (**25019:2023**) y su extensión para sistemas de inteligencia artificial (**25059:2023**).
- **ISO/IEC 2502n. División de medición de calidad**: modelo de referencia de medición y medidas de calidad en uso (25022), del producto (25023) y de los datos (25024).
- **ISO/IEC 2503n. División de requisitos de calidad**: especificación de requisitos de calidad (**25030**).
- **ISO/IEC 2504n. División de evaluación de calidad**: proceso de evaluación (**25040**) y guías asociadas.
- **ISO/IEC 25050-25099**: extensiones, como la 25051 (requisitos de calidad de producto software comercial, RUSP/COTS).

### ISO/IEC 25010: las 8 características de calidad del producto

La edición clásica, **ISO/IEC 25010:2011**, define el modelo de calidad del producto con **8 características** y sus subcaracterísticas:

| Característica | Subcaracterísticas |
| --- | --- |
| **Adecuación funcional** | Completitud, corrección y pertinencia funcional |
| **Eficiencia de desempeño** | Comportamiento temporal, utilización de recursos, capacidad |
| **Compatibilidad** | Coexistencia, interoperabilidad |
| **Usabilidad** | Inteligibilidad, aprendizabilidad, operabilidad, protección frente a errores de usuario, estética de la interfaz, accesibilidad |
| **Fiabilidad** | Madurez, disponibilidad, tolerancia a fallos, capacidad de recuperación |
| **Seguridad** | Confidencialidad, integridad, no repudio, responsabilidad, autenticidad |
| **Mantenibilidad** | Modularidad, reusabilidad, analizabilidad, modificabilidad, capacidad de ser probado |
| **Portabilidad** | Adaptabilidad, facilidad de instalación, capacidad de ser reemplazado |

La misma edición define además el modelo de **calidad en uso**, con cinco características: efectividad, eficiencia, satisfacción, ausencia de riesgo y cobertura de contexto.

Dos actualizaciones a tener presentes:

- La revisión **ISO/IEC 25010:2023** pasa el modelo del producto a **9 características**: renombra usabilidad como **capacidad de interacción** (*interaction capability*) y portabilidad como **flexibilidad** (que incorpora la **escalabilidad** como subcaracterística), y añade la **seguridad física** (*safety*, ausencia de daño a personas o al entorno). La calidad en uso se traslada a la norma **ISO/IEC 25019:2023**. El modelo de 8 características de 2011 sigue siendo el más citado en exámenes.
- La **ISO/IEC 25059:2023** extiende el modelo a los **sistemas de inteligencia artificial**, con aspectos como la adaptabilidad funcional, la transparencia o la capacidad de intervención del usuario.

### ISO/IEC 25012: calidad de datos

Define **15 características** de calidad de los datos en **tres grupos**:

- **Inherentes (5)**: exactitud, completitud, consistencia, credibilidad y actualidad.
- **Inherentes y dependientes del sistema (7)**: accesibilidad, conformidad, confidencialidad, eficiencia, precisión, trazabilidad y comprensibilidad.
- **Dependientes del sistema (3)**: disponibilidad, portabilidad y recuperabilidad.

### ISO/IEC 25040: proceso de evaluación

La ISO/IEC 25040 (edición de 2011, revisada en 2024 como marco de evaluación de la calidad) describe el proceso de evaluación en **cinco actividades**:

1. **Establecer los requisitos de la evaluación**: propósito, características a evaluar y rigor.
2. **Especificar la evaluación**: medidas, criterios de decisión y umbrales.
3. **Diseñar la evaluación**: plan de evaluación (actividades, recursos, calendario).
4. **Ejecutar la evaluación**: aplicar las medidas y los criterios.
5. **Concluir la evaluación**: informe de resultados y realimentación al proceso.

## Métricas y evaluación de la calidad

Medir es la base de la mejora: sin métricas no puede evaluarse si el producto o el proceso alcanzan los niveles de calidad exigidos. Conviene distinguir tres conceptos:

- **Medida**: valor de un atributo obtenido por medición directa (por ejemplo, 12.000 líneas de código).
- **Métrica**: relación entre medidas que caracteriza un atributo (defectos por KLOC).
- **Indicador**: métrica o combinación de métricas con un criterio de interpretación que permite tomar decisiones (tendencia de la densidad de defectos por versión).

Según su objeto, las métricas son **de producto** (atributos del software), **de proceso** (eficacia del desarrollo: densidad de defectos, eficiencia de eliminación) o **de proyecto** (esfuerzo, coste, plazos).

### Métricas de tamaño y de función

- **Orientadas al tamaño**: usan las **líneas de código (LOC/KLOC)** como base (defectos/KLOC, coste/KLOC). Simples de obtener, pero dependen del lenguaje y penalizan el código conciso.
- **Orientadas a la función**: los **puntos de función** (Albrecht, **1979**; método IFPUG, normalizado como ISO/IEC 20926) miden el **tamaño funcional** desde los requisitos, con independencia del lenguaje. Se cuentan **cinco componentes**: entradas externas, salidas externas, consultas externas, ficheros lógicos internos y ficheros de interfaz externos; cada uno se pondera por complejidad (simple, media, alta) y el total se ajusta con **14 características generales del sistema** (factor de ajuste de ±35 %). Permiten estimar esfuerzo y productividad (PF por persona-mes) en fases tempranas.

### Métricas de complejidad y mantenimiento

- **Complejidad ciclomática** (McCabe, **1976**): número de caminos linealmente independientes del flujo de control (ver caso práctico).
- **Métricas de Halstead (1977)**: derivan del recuento de operadores y operandos el volumen, la dificultad y el esfuerzo del programa.
- **COCOMO II** (Boehm, **2000**): modelo algorítmico de **estimación del esfuerzo**: a partir del tamaño estimado (miles de líneas de código o puntos de función convertidos) calcula el esfuerzo en **persona-mes** y el plazo, corregidos por factores de escala y multiplicadores de coste (experiencia del equipo, fiabilidad exigida, herramientas). Actualiza el COCOMO original (1981) a los ciclos de vida modernos.
- **Cobertura de código**: proporción del código ejercitada por las pruebas (por sentencias, ramas o caminos).
- **Índice de mantenibilidad**: combina Halstead, complejidad ciclomática y LOC en un valor único de facilidad de mantenimiento.
- **Deuda técnica**: coste futuro de corregir los atajos tomados durante el desarrollo (metáfora de Ward Cunningham). Se gestiona de forma continua con herramientas de análisis estático como **SonarQube**, que calculan el ratio de deuda técnica y la calificación del proyecto.

## Caso práctico: cálculo de la complejidad ciclomática

La **complejidad ciclomática V(G)** mide el número de caminos linealmente independientes del grafo de flujo de control de un programa, y equivale al número mínimo de casos de prueba necesarios para cubrir todas sus ramas (*basis path testing*). McCabe recomendó mantenerla **por debajo de 10** por módulo.

**Enunciado**: calcular la complejidad ciclomática del siguiente método:

```java
public String clasificar(boolean urgente, int dias, boolean recurrido) {
    String tipo;
    if (urgente && dias > 30) {
        tipo = "prioritario";
    } else if (recurrido) {
        tipo = "recurso";
    } else {
        tipo = "ordinario";
    }
    return tipo;
}
```

**Paso 1. Construir el grafo de flujo de control**: los **nodos** son bloques de código secuenciales y las **aristas**, los flujos de control entre ellos. El método tiene **7 nodos**: evaluación de `urgente` (N1), evaluación de `dias > 30` (N2, solo se alcanza si `urgente` es cierto, por el cortocircuito del operador `&&`), asignación «prioritario» (N3), evaluación de `recurrido` (N4), asignación «recurso» (N5), asignación «ordinario» (N6) y el `return` final (N7). Las **9 aristas** son: N1→N2, N1→N4, N2→N3, N2→N4, N3→N7, N4→N5, N4→N6, N5→N7 y N6→N7.

**Paso 2. Calcular V(G) por los tres métodos** (deben coincidir):

- **Por aristas y nodos**: V(G) = E − N + 2 = 9 − 7 + 2 = **4**.
- **Por nodos predicado**: V(G) = P + 1 = 3 + 1 = **4**. Los nodos de decisión son las condiciones `urgente`, `dias > 30` y `recurrido`: cada operando de una condición compuesta con `&&` o `||` cuenta como decisión propia.
- **Por regiones**: el grafo plano encierra 3 regiones internas que, sumadas a la región exterior, dan **4**.

**Paso 3. Interpretar el resultado**: V(G) = 4 exige un mínimo de **4 casos de prueba** para cubrir los caminos independientes: (1) urgente con más de 30 días (prioritario), (2) urgente con 30 días o menos y recurrido (recurso), (3) no urgente y recurrido (recurso) y (4) no urgente y no recurrido (ordinario). El valor queda en la franja de riesgo bajo:

| V(G) | Valoración |
| --- | --- |
| **1-10** | Programa simple, riesgo bajo |
| **11-20** | Complejidad moderada |
| **21-50** | Programa complejo, riesgo alto |
| **> 50** | Prácticamente intestable, riesgo muy alto |

## Fuentes {.unnumbered .unlisted}

- ISO/IEC 25000:2014, *Guide to SQuaRE*; ISO/IEC 25010:2011 y su revisión 25010:2023 (modelo de calidad del producto); ISO/IEC 25019:2023 (calidad en uso); ISO/IEC 25012:2008 (calidad de datos); ISO/IEC 25040:2011, revisada en 2024 (evaluación); ISO/IEC 25059:2023 (sistemas de IA).
- ISO 9000:2015 e ISO 9001:2015, sistemas de gestión de la calidad.
- CMMI V3.0, ISACA, 2023; ISO/IEC 33001:2015 (SPICE).
- McCabe, T., «A Complexity Measure», *IEEE Transactions on Software Engineering*, 1976.
- Albrecht, A., «Measuring Application Development Productivity», IBM, 1979; IFPUG, ISO/IEC 20926:2009.
- Pressman, R. y Maxim, B., *Software Engineering: A Practitioner's Approach*, 9.ª ed., McGraw-Hill, 2020.
