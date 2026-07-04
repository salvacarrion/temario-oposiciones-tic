# Análisis y diseño de aplicaciones

## Análisis y diseño de aplicaciones

El análisis y diseño de aplicaciones son etapas fundamentales dentro del desarrollo de sistemas de información. Estas tareas aseguran que el software cumpla con los requisitos definidos, sea funcional y esté preparado para ser implementado de manera efectiva.

### Ciclo de Vida de un Sistema de Información (CVSI)

El **ciclo de vida de un sistema de información (CVSI)** describe las etapas necesarias para el desarrollo, implementación y mantenimiento de un sistema. Estas etapas son:

- **Estudio de factibilidad:** Se analizan los beneficios, costos y soluciones de implantar un nuevo sistema de información, evaluando su viabilidad técnica, económica y operativa.
- **Análisis de requisitos:** Se identifican, especifican y documentan los requisitos funcionales y no funcionales del sistema para garantizar que satisfagan las necesidades del usuario.
- **Diseño:** Se desarrollan representaciones detalladas de las características del sistema, incluyendo diagramas, arquitecturas y especificaciones, para guiar su implementación de manera efectiva.
- **Desarrollo/Implementación:** Se lleva a cabo la programación del sistema, transformando el diseño en código funcional.
- **Pruebas:** Se ejecutan para identificar errores y verificar que el sistema cumple con los requisitos especificados.
- **Instalación:** Incluye la planificación del entorno de hardware y software, la configuración del sistema y su despliegue en producción.
- **Mantenimiento:** Consiste en mantener el sistema operativo y actualizado durante su vida útil para garantizar su rendimiento y fiabilidad.

### Tipos de pruebas

- **Prueba unitaria:** Evalúa módulos o programas individuales a partir de casos específicos para garantizar que cada componente funcione de manera aislada.
- **Prueba de integración:** Verifica la correcta interacción entre dos o más componentes que intercambian información.
- **Pruebas de sistema:** Se realizan en un entorno controlado, distinto al de desarrollo, por personal especializado, y validan el sistema completo.
- **Pruebas de recuperación:** Determinan la capacidad del sistema para recuperarse de fallos de hardware o software.
- **Pruebas de seguridad:** Confirman que el sistema incluye los controles necesarios para evitar brechas de seguridad.
- **Pruebas de estrés:** Simulan condiciones extremas para evaluar el rendimiento del sistema ante altas cargas de trabajo.
- **Pruebas de volumen:** Analizan el impacto de grandes cantidades de datos o usuarios concurrentes y determinan el volumen máximo soportado.
- **Pruebas de rendimiento:** Comparan el desempeño del sistema con otras soluciones similares.
- **Prueba de aceptación final:** Realizada tras la implantación, busca garantizar la calidad técnica y funcional del sistema, evaluando si cumple con los requisitos establecidos.

### Tipos de mantenimiento

- **Mantenimiento correctivo:** Elimina defectos detectados durante el uso del sistema.
- **Mantenimiento adaptativo:** Realiza ajustes para adaptarse a cambios en el entorno externo, como nuevas normativas o tecnologías.
- **Mantenimiento perfectivo:** Añade nuevas funcionalidades para mejorar el sistema.

### Modelos del ciclo de vida o Modelos de Desarrollo de Software

Los modelos del ciclo de vida organizan las etapas del desarrollo de un sistema. Entre los principales modelos se encuentran:

### 1. Ciclo de Vida Clásico o Modelo en Cascada

Es un enfoque **secuencial y sistemático** donde cada etapa del desarrollo se completa antes de iniciar la siguiente.

- **Etapas:** Estudio de factibilidad o planificación, análisis de requisitos, diseño, desarrollo, pruebas y mantenimiento.
- **Ventajas:** Proporciona un desarrollo ordenado y estructurado, siendo adecuado para proyectos con requisitos bien definidos.
- **Inconvenientes:** La validación con el usuario final ocurre solo tras el desarrollo completo, lo que puede resultar en problemas si los requisitos iniciales estaban mal definidos.

### 2. Desarrollo de prototipos

Se basa en un enfoque **iterativo** que permite validar los requisitos mediante prototipos o versiones preliminares del sistema.

- **Ventajas:** Reduce el riesgo de fracaso y facilita la definición de requisitos para productos poco conocidos.
- **Inconvenientes:** Los usuarios pueden confundir el prototipo con el sistema definitivo, consolidando aspectos no óptimos.

### 3. Modelo en espiral

Divide el proyecto en subproyectos iterativos que aportan funcionalidad incremental al sistema final, integrando una mejora constante y validación con el usuario.

- **Ventajas:** Permite determinar la viabilidad técnica del proyecto en fases tempranas y mejora la comunicación con los usuarios.
- **Inconvenientes:** No se mencionan desventajas específicas.

### 4. Desarrollo iterativo e incremental

Este modelo combina iteración e incremento, desarrollando pequeñas secciones del sistema que crecen en funcionalidad y complejidad.

- **Iterativo:** Proporciona una visión global con versiones sucesivas (v0.1, v0.2, v0.3...).
- **Incremental:** Añade funcionalidades en etapas progresivas (1, 2, 3...).

### 5. Desarrollo ágil

Se fundamenta en enfoques iterativos, pero con un enfoque más **ligero y centrado en las personas**, fomentando la flexibilidad y la colaboración constante entre los desarrolladores y los usuarios. Este modelo destaca por su capacidad para adaptarse a cambios de requisitos y su énfasis en la entrega rápida de valor.

## Análisis de Requisitos

El análisis de requisitos es un proceso fundamental en el desarrollo de software que tiene como objetivo definir y comprender las necesidades y expectativas de los clientes y usuarios finales. Este proceso incluye técnicas específicas para la captura, especificación, análisis y validación de los requisitos necesarios para construir un sistema eficaz y ajustado a las necesidades del cliente.

### Requerimientos

Los requerimientos especifican lo que el sistema debe hacer (requisitos funcionales) y cómo debe comportarse en términos de atributos no funcionales como rendimiento, seguridad o portabilidad.

Existen **dos tipos principales** de requisitos:

- **Funcionales**: Definen las funciones y comportamientos específicos del sistema, como los casos de uso.
- **No funcionales**: Definen atributos del sistema, como rendimiento y seguridad.

### Captura de Requerimientos

El proceso de captura de requerimientos tiene como objetivo comprender las expectativas de los clientes y usuarios. A través de entrevistas, reuniones y otros métodos de toma de datos, se busca construir una visión clara de lo que el sistema debe lograr.

### Procesos en la Ingeniería de Requisitos

El proceso de ingeniería de requisitos abarca varias etapas:

- **Estudio de viabilidad**: Evalúa si el proyecto es factible en términos de tecnología, costo y recursos.
- **Obtención y análisis de requerimientos**: Recolecta los requisitos y evalúa su viabilidad y claridad.
- **Especificación de requerimientos**: Documenta los requisitos de forma precisa y verificable.
- **Validación**: Confirma que los requisitos cumplen las expectativas del cliente.

### Especificación de Requerimientos (ERS)

La especificación de requisitos (ERS) es un documento detallado que describe el comportamiento completo del sistema. Contiene:

- **Casos de uso**: Detallan las interacciones entre el usuario y el sistema.
- **Descripción verificable**: El ERS debe ser completo, preciso y verificable, separando funcionalidad de implementación.

### Características de los Requisitos

Los requisitos deben cumplir ciertas características según el estándar IEEE 830-1998:

- **Correctos**: El software debe cumplir con los requisitos.
- **Consistentes**: No debe haber contradicciones entre los requisitos.
- **Completos**: Todos los requisitos necesarios están documentados.
- **Inequívocos**: Deben estar redactados de forma clara.
- **Trazables**: Deben poder seguirse y verificarse a lo largo del proceso de desarrollo.
- **Priorizables**: Los requisitos se ordenan por su importancia.
- **Modificables**: Pueden actualizarse fácilmente.
- **Verificables**: Debe existir un método de prueba para cada requisito.

### Dimensiones de los Requisitos

- **Ambientales**: Aspectos como el entorno de ejecución.
- **Interfaces**: Definen las interacciones del sistema.
- **Factores Humanos**: Consideraciones relacionadas con la usabilidad.
- **Funcionalidad**: Acciones específicas que el sistema debe realizar.
- **Seguridad**: Requisitos para proteger la información.

## Modelo de Casos de Uso

Los casos de uso son herramientas fundamentales para capturar los **requisitos funcionales** de un sistema, especificando las **interacciones** entre el usuario y el sistema. Representan acciones específicas realizadas por el sistema y se detallan a través de un **flujo de eventos** que describe cómo los usuarios y otros sistemas interactúan con él.

### Estructura de un Caso de Uso:

- **Caso de uso**: Describe una función específica que realiza el sistema.
- **Actor**: Representa al usuario o sistema que interactúa con el caso de uso.
- **Subsistemas**: Unidades independientes que forman parte del sistema general.
- **Relaciones**: Enlaces entre casos de uso y actores que especifican cómo interactúan.

### Niveles de estructuración de casos de uso

1. **Diagrama de contexto**: Define los límites del sistema e identifica su entorno.
2. **Diagrama inicial**: Detalla el diagrama de contexto, incluyendo los principales casos de uso y funcionalidades clave.
3. **Modelo de casos de uso**: Profundiza en las interacciones entre actores y sistemas, mostrando las relaciones y detalles específicos.

### Plantillas de descripción de casos de uso

Para uniformar la documentación, se utiliza una plantilla estructurada que incluye:

- **Título del caso de uso**.
- **Actores** implicados.
- **Resumen**: Breve descripción del propósito del caso de uso.
- **Precondiciones**: Condiciones que deben cumplirse antes de ejecutar el caso de uso.
- **Postcondiciones**: Resultados esperados tras la ejecución del caso de uso.
- **Relaciones**: Como "Incluye", "Entiende", o "Hereda de".
- **Flujo de eventos Actor-Sistema**: Pasos detallados que describen la interacción entre el actor y el sistema.

### Normas de aplicación de casos de uso

El lenguaje empleado debe evitar tecnicismos y enfocarse en trabajar en colaboración con los clientes. Cada caso de uso se centra en una única **meta o tarea**, describiendo las características del sistema de forma clara y accesible.

## Caso práctico: Diagrama de Casos de Uso y de Actividades

### Contexto

La Generalitat Valenciana quiere implementar un **sistema de gestión de una biblioteca digital** para su red de bibliotecas públicas. El sistema debe permitir a los usuarios registrarse, buscar libros, reservarlos y leerlos en línea o descargarlos si la licencia lo permite. Además, los bibliotecarios deben poder añadir nuevos libros, gestionar reservas, generar informes de uso y descargarlos.

### Requisitos Funcionales

1. **Usuarios**:
    - Registrarse en el sistema con un nombre de usuario y contraseña.
    - Buscar libros por título, autor, género o palabras clave.
    - Reservar libros para leer en línea o descargarlos si es posible.
    - Cancelar una reserva.
    - Ver el historial de libros leídos y reservas activas.
2. **Bibliotecarios**:
    - Añadir nuevos libros al sistema con metadatos como título, autor, género y licencia.
    - Eliminar libros que ya no están disponibles.
    - Gestionar reservas, aprobándolas o rechazándolas.
    - Generar y descargar informes de uso, como los libros más populares.
3. **Sistema**:
    - Enviar notificaciones por correo electrónico para confirmar reservas o avisar de próximas expiraciones.
    - Mantener un registro de actividades para auditorías.

### Actividad Práctica

1. **Crea un Diagrama de Casos de Uso** mostrando las relaciones entre actores y casos de uso clave.
2. **Dibuja un Diagrama de Actividades** para el flujo del proceso de "Reserva de un libro".

### Solución: (Faltan cosas)

### 1. Diagrama de Casos de Uso

### Elementos clave:

- **Actores:** Usuario, Bibliotecario, Sistema de Correo Electrónico.
- **Casos de uso:** Registrar usuario, Buscar libro, Leer libro, Descargar libro, Reservar libro, Gestionar reservas, Generar informe.

### Relaciones:

- **Asociación:** Usuario → Registrase, Buscar libro, Reservar/cancelar libro, Leer/Descargar libro, Ver historial
- **Extensión:** Reservar/Cancelar libro ← Notificar reserva/cancelación
- **Inclusión:** Gestionar reservas → Generar informe → Descargar informe

> ![](media/image21.png)

### 2. Diagrama de Actividades de Flujo

### Ejemplo de proceso: Reserva de un libro

1. El usuario busca un libro.
2. El sistema muestra los resultados de búsqueda.
3. El usuario selecciona un libro y solicita la reserva.
4. El sistema verifica la disponibilidad y la licencia.
    - Si el libro está disponible, se confirma la reserva y se notifica al usuario.
    - Si no está disponible, se rechaza la solicitud.
5. El sistema actualiza el estado del libro y el registro de reservas.

### Elementos clave:

- **Actividades:** Buscar libro, Solicitar reserva, Verificar disponibilidad, Confirmar reserva, Notificar usuario.
- **Decisiones:** Libro disponible (Sí/No).

![](media/image22.png)
