# Computación en la nube y de altas prestaciones

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Cluster computing, Grid computing, Cloud computing

### Clúster

Un clúster es un grupo de ordenadores interconectados mediante una red de alta velocidad que funciona como un único sistema. Cada nodo, o equipo individual, realiza la misma tarea, controlada y planificada por software especializado. Este enfoque potencia la **paralelización de tareas**, optimizando el rendimiento y la eficiencia en el procesamiento de datos.

### Grid Computing

La **computación en malla** o grid computing conecta múltiples clústeres entre sí, donde los recursos no están sujetos a un control centralizado. Cada nodo puede realizar tareas diferentes, lo que promueve la **distribución de tareas** y garantiza la **escalabilidad**. Este modelo permite un comportamiento dinámico y un dimensionamiento en tiempo real, siendo ideal para atender productividades sostenidas.

### Virtualización

La virtualización es una tecnología que permite la creación de recursos virtuales, facilitando la distribución de la carga de trabajo de manera más sencilla que en la computación grid. Al combinar grid computing con virtualización, se obtiene el **cloud computing**, que ofrece mayores niveles de eficiencia y flexibilidad en la gestión de recursos.

### Cloud Computing

La computación en la nube (Cloud Computing) es un paradigma que proporciona acceso a recursos y servicios informáticos bajo demanda a través de internet, eliminando la necesidad de gestión activa por parte del usuario. Este modelo destaca por su **flexibilidad, escalabilidad, elasticidad, autoservicio, abstracción y acceso sin restricciones,** adaptándose a las necesidades cambiantes de las organizaciones con un modelo de **pago por uso.**

### Ventajas del Cloud Computing

- **Económicas**: Reducción de costes de mantenimiento y flexibilidad en la inversión.
- **Tecnológicas**: Facilita el despliegue e implantación, mejora la seguridad y elasticidad, delegación de responsabilidades y mayor respeto al medio ambiente.
- **Organizativas**: Disminuye la dimensión y orientación del departamento de TI, requiere de personal menos cualificado, ofrece oportunidades de cambio y promueve la estandarización.

### Desventajas del Cloud Computing

- **Económicas**: Los costes pueden incrementarse si no se gestionan adecuadamente.
- **Tecnológicas**: Mayores riesgos y vulnerabilidades al trasladar información a una red pública, falta de privacidad y cobertura legal, ausencia de control ante incidentes informáticos, falta de estandarización y problemas de interoperabilidad. Acuerdos de nivel de servicio (SLA) mal definidos y reticencia al cambio.
- **Organizativas**: Centralización excesiva y dependencia del proveedor, lo que puede limitar la libertad y creatividad.

### Tabla comparativa de modelos de computación

| Aspecto                      | Cluster Computing                                                                                                             | Grid Computing                                                                                                | Cloud Computing                                                                                      |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Idea básica                  | Agregación de recursos.                                                                                                       | Segregación de recursos.                                                                                      | Consolidación de recursos.                                                                           |
| Procesos en ejecución        | Los mismos procesos se ejecutan en todos los equipos del cluster al mismo tiempo.                                             | El trabajo se divide en subtrabajos, cada uno asignado a una CPU libre para que se ejecuten concurrentemente. | Depende de la provisión del servicio. Qué equipo ofrece un servicio y lo proporciona a los clientes. |
| Sistema operativo            | Todos los nodos deben ejecutar el mismo sistema operativo.                                                                    | No hay restricciones sobre el sistema operativo.                                                              | No hay restricciones sobre el sistema operativo.                                                     |
| Ejecución de trabajos (Jobs) | La ejecución depende de la programación de los trabajos. Los trabajos esperan hasta que se les asigne un tiempo de ejecución. | La ejecución es escalable de manera que un trabajo puede moverse a un procesador (nodo) libre.                | Autogestionado.                                                                                      |
| Apropiado para apps          | Tareas en cascada. Si una tarea depende de otra.                                                                              | No es adecuado para tareas en cascada.                                                                        | Provisión de servicios bajo demanda.                                                                 |
| Ubicación de los nodos       | Físicamente en la misma ubicación.                                                                                            | Distribuidos geográficamente por todo el mundo.                                                               | La ubicación no importa.                                                                             |
| Homo/Heterogeneidad          | Homogéneo.                                                                                                                    | Heterogéneo.                                                                                                  | Heterogéneo.                                                                                         |
| Virtualización               | Ninguna.                                                                                                                      | Ninguna.                                                                                                      | La virtualización es clave.                                                                          |
| Transparencia                | Sí.                                                                                                                           | Sí.                                                                                                           | Sí.                                                                                                  |
| Seguridad                    | Alta.                                                                                                                         | Alta, pero no alcanza el nivel de Cluster Computing.                                                          | Menor que ambos tipos.                                                                               |
| Interoperabilidad            | Sí.                                                                                                                           | Sí.                                                                                                           | No.                                                                                                  |
| Dominios de aplicación       | Sector industrial, centros de investigación, salud y centros que ofrecen servicios a nivel nacional.                          | Sector industrial, centros de investigación, salud y centros que ofrecen servicios a nivel nacional.          | Banca, seguros, predicción meteorológica, exploración espacial, negocios, IaaS, PaaS, SaaS.          |
| Implementación               | Fácil.                                                                                                                        | Difícil.                                                                                                      | Difícil - debe ser realizada por el host.                                                            |
| Gestión                      | Fácil.                                                                                                                        | Difícil.                                                                                                      | Difícil.                                                                                             |
| Gestión de recursos          | Centralizada (localmente).                                                                                                    | Distribuida.                                                                                                  | Tanto centralizada como distribuida.                                                                 |
| Internet                     | No se requiere acceso a Internet.                                                                                             | Requerido.                                                                                                    | Requerido.                                                                                           |

## Tipos de Nubes

### Nube Pública

Los servicios ofrecidos están en entornos públicos no propietarios, abiertos al público y gestionados por proveedores externos.

- **Características**: Abiertas al público y gestionadas por los proveedores.
- **Ventajas**: Evita grandes inversiones en equipos y mantenimiento, proporciona flexibilidad y garantías de privacidad, seguridad y disponibilidad.
- **Desventajas**: Dependencia de los servicios en línea y del acceso a través de internet.

### Nube Privada

Los servicios y datos son propiedad de una organización específica, ofreciendo privacidad de datos y gestión personalizada.

- **Características**: Privacidad de datos y gestión localizada.
- **Ventajas**: Mayor seguridad y privacidad de los datos, gestión personalizada.
- **Desventajas**: Mayor inversión en personal, equipos y mantenimiento, menor escalabilidad y posible disminución de la seguridad por gestión no especializada.

### Nube Híbrida

Combina servicios de nubes públicas y privadas, permitiendo aprovechar las ventajas de ambas.

- **Características**: Privacidad de datos y menor coste.
- **Ventajas**: Menor inversión inicial, mantenimiento del control y privacidad de los datos, y beneficios de las nubes públicas.
- **Desventajas**: Requiere el mantenimiento de dos nubes diferentes.

### Nube de Comunidad

Servicios compartidos en una comunidad cerrada de entidades con objetivos comunes, como organizaciones gubernamentales.

- **Características**: Infraestructura compartida por varias organizaciones.
- **Ventajas**: Permite crear una nube especializada según los requisitos de las organizaciones.
- **Desventajas**: Variables según las necesidades y acuerdos entre las entidades.

## Aspectos varios de la computación en la Nube

### Almacenamiento en la Nube

Modelo de servicio donde los datos generados se almacenan, administran y respaldan de forma remota en servidores gestionados por un proveedor. Los tipos de almacenamiento en la nube incluyen:

- **Público**
- **Privado**
- **Híbrido**

### Software On-Premise vs Off-Premise

- **Software On-Premise**: Software instalado localmente en los servidores de la organización.
- **Software Off-Premise**: Software alojado en la nube (SaaS), gestionado por un proveedor externo.

### Serverless Computing

El **serverless computing** es un modelo donde las empresas pagan solo por el uso efectivo de los recursos informáticos, permitiendo reducir costes y mejorar la eficiencia. El proveedor asume la responsabilidad de ejecutar, escalar y administrar los servidores necesarios para ejecutar el código de las aplicaciones, sin que el usuario tenga que preocuparse por la infraestructura subyacente ni por la demanda de carga de trabajo.

- **Características**: Pago por tiempo de ejecución del código y recursos utilizados.

### Edge Computing

La **computación en el borde** o edge computing busca llevar el procesamiento de datos lo más cerca posible del usuario o del lugar donde se generan los datos, reduciendo la latencia y mejorando la velocidad de procesamiento.

- **Beneficios**: Reducción de latencia y ancho de banda necesarios, ideal para aplicaciones que requieren respuestas rápidas o en tiempo real.

### Contenedores, Orquestación y Microservicios

- **Contenedores**: Permiten empaquetar y distribuir aplicaciones de manera rápida y sencilla, aislando el software en entornos independientes.
- **Orquestación**: Gestión automatizada de contenedores en la nube, facilitando su implementación y escalado.
- **Microservicios**: Enfoque de desarrollo de aplicaciones basado en crear pequeños servicios independientes que pueden integrarse y escalarse de manera eficiente.

## Infraestructuras, Plataformas y Software como Servicio (IaaS, PaaS, SaaS)

### Tipos de Servicio en el Cloud Computing

### Software as a Service (SaaS)

Modelo donde el proveedor ofrece aplicaciones a través de internet. El usuario accede a estas aplicaciones mediante una conexión web, sin necesidad de instalar nada localmente. El proveedor se encarga de toda la gestión y mantenimiento del software.

- **Características**: No requiere conocimientos técnicos, pero implica pérdida de control sobre seguridad y privacidad. Se accede mediante un "thin-client" como un navegador web.
- **Ejemplos**: Correo electrónico, CRM, plataformas colaborativas como Slack, GitHub, Google Drive, Dropbox o Salesforce.

### Platform as a Service (PaaS)

El proveedor ofrece una plataforma para desarrollar, probar, ejecutar y mantener aplicaciones. El usuario no se preocupa por la infraestructura necesaria, enfocándose únicamente en el desarrollo de la aplicación. El proveedor gestiona y actualiza la infraestructura.

- **Ejemplos**: Microsoft Azure, Google App Engine, Amazon Web Services (AWS).

### Infrastructure as a Service (IaaS)

Permite a las organizaciones adaptar sus recursos de procesamiento y almacenamiento de manera elástica y eficiente, pagando solo por lo que utilizan. El proveedor ofrece servicios de infraestructura como almacenamiento, procesamiento y redes, encargándose de su gestión y mantenimiento.

- **Ejemplos**: GoGrid, Amazon EC2 (Elastic Compute Cloud), Google Compute Engine.

### Comparación entre IaaS, PaaS y SaaS

- **Nivel de Control**: IaaS ofrece el mayor control sobre los recursos de TI, seguido por PaaS y luego SaaS.
- **Responsabilidades de Gestión**: En IaaS, el cliente gestiona sistemas operativos y aplicaciones; en PaaS, se enfoca en las aplicaciones; en SaaS, el proveedor gestiona todo.
- **Flexibilidad**: IaaS proporciona la máxima flexibilidad para personalizar entornos; PaaS equilibra flexibilidad y facilidad de uso; SaaS ofrece soluciones estándar listas para usar.
