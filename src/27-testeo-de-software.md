# Testeo de software

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Fundamentos del testeo (ISTQB)

El testeo de software es una disciplina crítica dentro del desarrollo de software que permite identificar defectos y verificar que el software cumple con los requisitos establecidos. Según los fundamentos de ISTQB (International Software Testing Qualifications Board), el testeo de software ayuda a validar la funcionalidad del sistema y a mejorar la calidad general del producto antes de su implementación en entornos productivos.

### Errores, Defectos y Fallos

En el proceso de testeo, se distingue entre errores, defectos y fallos:

- **Error (equivocación)**: Es la acción humana que conduce a un problema en el código o diseño.
- **Defecto**: Es el resultado de un error en el código, una imperfección que puede causar un fallo.
- **Fallo**: Es el comportamiento incorrecto del sistema al ejecutar el defecto, evidenciando la presencia de un problema en el software.

### Los 7 Principios de la Prueba

1. **La prueba muestra la presencia de defectos, no su ausencia**.
2. **La prueba exhaustiva es imposible**: No se pueden cubrir todos los casos posibles.
3. **La prueba temprana ahorra tiempo y dinero**: Detectar defectos en etapas tempranas reduce los costos.
4. **Los defectos se agrupan**: La mayoría de los defectos suelen concentrarse en ciertas áreas del software.
5. **Paradoja del pesticida**: Repetir siempre las mismas pruebas reduce su efectividad; es necesario actualizar las pruebas para detectar nuevos defectos.
6. **La prueba depende del contexto**: Las pruebas varían según el tipo de software.
7. **La ausencia de errores es una falacia**: Un sistema sin defectos puede ser inutilizable si no cumple con los requisitos.

### Roles en el Proceso de Revisión

El proceso de revisión, que busca detectar defectos sin ejecutar el software, involucra diferentes roles:

- **Autor**: Persona que ha creado el código o documento revisado.
- **Dirección**: Supervisa la efectividad del proceso.
- **Facilitador**: Coordina el proceso de revisión.
- **Líder de revisión**: Responsable de la planificación y ejecución de la revisión.

### Niveles de Prueba

Los niveles de prueba son conjuntos de actividades de testeo organizadas de manera estructurada:

- **Prueba de Componente**: Evalúa unidades individuales del sistema, como funciones o métodos, de forma aislada.
- **Prueba de Integración**: Verifica la interacción entre componentes, asegurando que funcionen correctamente juntos.
- **Prueba de Sistema**: Prueba el sistema completo para validar su comportamiento general y las tareas de usuario.
- **Prueba de Aceptación**: Valida que el sistema cumple con los requisitos del cliente y se espera que funcione correctamente.
- **Prueba Alfa**: Realizada por clientes en las instalaciones del desarrollador, con este último como observador.
- **Prueba Beta**: Realizada por clientes en sus propias instalaciones para obtener una retroalimentación del uso real.
- **Otras pruebas:** Pruebas de aceptación de usuario, de aceptación operativa, de aceptación contractual y de regulación, y pruebas alfa y beta (pre-releases).

### Tipos de Pruebas de Software

- **Pruebas Funcionales**: Validan que el sistema realice las funciones para las que fue diseñado.
- **Pruebas No Funcionales**: Evalúan características como rendimiento, usabilidad, eficiencia y seguridad.
- **Pruebas de Caja Blanca**: Basadas en el conocimiento de la estructura interna del software; permiten verificar la funcionalidad mediante pruebas directas del código.
- **Pruebas de Caja Negra**: Se realizan sin conocer la estructura interna, evaluando la respuesta del software a diferentes entradas.
- **Pruebas Asociadas al Cambio**:
    - **Pruebas de Confirmación**: Confirman que un defecto ha sido solucionado.
    - **Pruebas de Regresión**: Verifican que nuevas funcionalidades o cambios no introduzcan defectos en áreas previamente correctas.

### Pruebas Dinámicas y Estáticas

- **Pruebas Dinámicas**: Evalúan el comportamiento del software ejecutándolo; incluyen pruebas de caja blanca, caja negra, etc.
- **Pruebas Estáticas**: Analizan el código o documentos sin ejecutarlos, como revisiones manuales o análisis estáticos automatizados.

### Técnicas de Pruebas

Las técnicas de pruebas buscan definir las condiciones y los casos de prueba para garantizar una cobertura exhaustiva:

**Pruebas de Caja Negra**:

- **Partición de Equivalencia**: Divide el conjunto de datos en clases que deben dar el mismo resultado.
- **Análisis de Valores Frontera (AVF)**: Evaluación de los valores límites de cada partición.
- **Prueba de Tabla de Decisión**: Ayuda a documentar reglas complejas de negocio.
- **Prueba de Transición de Estado**: Verifica secuencias de estados en el sistema, como los diferentes niveles de un menú.
- **Prueba de Caso de Uso**: Basada en los requisitos funcionales, enfocada en las interacciones esperadas.

**Pruebas de Caja Blanca**:

- **Cobertura de Sentencia**: Evalúa cada sentencia en el código para garantizar que ha sido ejecutada al menos una vez.
- **Cobertura de Decisión**: Verifica que todas las decisiones (condiciones) posibles en el código se evalúen.

**Pruebas Basadas en la Experiencia**:

- **Predicción de Errores**: Basada en la experiencia previa de los evaluadores.
- **Prueba Exploratoria**: Los evaluadores exploran el software sin un caso de prueba predefinido.
- **Prueba Basada en Listas de Comprobación**: Usa listas para verificar que se cumplen ciertos criterios.
