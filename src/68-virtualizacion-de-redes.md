# Virtualización de redes

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Virtualización de redes

Es una tecnología que combina hardware y software para presentar una vista lógica de la red que difiere de la infraestructura física subyacente. Esta técnica permite **combinar múltiples redes físicas en una sola red virtual** o, por el contrario, **dividir una red física en varias redes virtuales independientes**. Cada red virtual puede tener sus propias características y configuraciones, lo que proporciona una gran flexibilidad en la gestión de recursos.

Al **desvincular los servicios de red del hardware subyacente**, la virtualización permite el aprovisionamiento y la administración de la red de forma más eficiente.

### Beneficios principales:

- **Aumento de la productividad** al facilitar el despliegue y la gestión de recursos.
- **Mejora de la eficiencia** en el uso de la infraestructura existente.
- **Ahorro de costes** al reducir la necesidad de hardware adicional.
- **Facilidad de administración** gracias a una gestión centralizada.
- **Mayor flexibilidad** para adaptarse a las necesidades cambiantes del negocio.

### Tipos de virtualización de red:

- **Virtualización externa**: Utiliza dispositivos externos, como routers o switches, para dividir una red física en varias redes virtuales.
- **Virtualización interna**: Emplea componentes internos, como tarjetas de red o placas base, para crear redes virtuales dentro de una misma infraestructura física.

## Redes definidas por software (SDN)

Las **Redes Definidas por Software (SDN)** representan un enfoque innovador en la gestión de redes, donde se utiliza software o interfaces de programación de aplicaciones (**API**) para dirigir el tráfico y comunicarse con el hardware subyacente. La SDN **separa el plano de control de la red del plano de datos**, es decir, las decisiones sobre cómo se enruta el tráfico se separan de los dispositivos que efectúan el enrutamiento.

**Objetivo principal de las SDN:** Facilitar la implementación y gestión de servicios de red de manera **determinista, dinámica y escalable**, evitando que los administradores tengan que gestionar servicios a bajo nivel.

**Características clave**:

- **Centralización del control de la red**, permitiendo una visión global y unificada.
- **Programabilidad**, facilitando la automatización y adaptación de la red.
- **Virtualización y abstracción de la red**, simplificando la gestión de recursos.
- **Separación de planos**: el **plano de control** toma decisiones, mientras que el **plano de datos** ejecuta el reenvío de paquetes.
- **Flexibilidad y actualización en tiempo real**, adaptándose rápidamente a las necesidades cambiantes.

### Arquitectura de SDN:

- **Capa de aplicación**: Proporciona aplicaciones específicas que utilizan la red, comunicando solicitudes de recursos o información sobre el estado global de la red.
    - **Se compone de**: Aplicaciones
- **Capa de control [Plano de control]**: Actúa como el cerebro de la red, tomando decisiones sobre el enrutamiento y configurando los dispositivos de conmutación y enrutamiento según las necesidades de las aplicaciones.
    - **Se compone de**: Controladores
- **Capa de red o infraestructura [Plano de datos / de Reenvío]**: Constituye el plano físico, donde los dispositivos de red ejecutan las instrucciones recibidas, encargándose de la conmutación y el enrutamiento del tráfico.
    - **Se compone de**: Dispositivos de red

**Protocolos de control**:

- **OpenFlow**: Estándar abierto que define un protocolo de comunicaciones entre el plano de control y el plano de datos.
- Otros protocolos y plataformas como **OpenDaylight (ODL)** y **OnePK**.

**Clasificación de modelos de SDN**:

- **Abierta**: Basada en estándares abiertos, favoreciendo la interoperabilidad.
- **Por API**: Utiliza interfaces de programación para interactuar con dispositivos específicos.
- **De superposición**: Crea redes virtuales sobre la infraestructura física existente.
- **Híbrida**: Combina elementos de los modelos anteriores para adaptarse a necesidades específicas.

## Redes de área amplia definidas por software (SD-WAN)

Las **Redes de Área Amplia Definidas por Software (SD-WAN)** son una evolución de las redes WAN tradicionales, que incorporan automatización y programabilidad para **encaminar el tráfico de forma dinámica y segura**. Basándose en políticas de aplicación, condiciones de la red o prioridades de los circuitos WAN, las SD-WAN optimizan el enrutamiento sin necesidad de redirigir el tráfico a ubicaciones centrales, lo que **reduce costes y mejora la eficiencia**.

### Beneficios de las SD-WAN:

- **Simplificación de la red**, facilitando su gestión y configuración.
- **Mejora del rendimiento y la fiabilidad**, al optimizar el uso de los enlaces disponibles.
- **Control avanzado del tráfico de datos**, permitiendo priorizar aplicaciones críticas.
- **Flexibilidad en la conexión de dispositivos**, utilizando diversos tipos de enlaces como banda ancha, líneas privadas y conexiones a internet.
- **Actualizaciones y cambios de configuración sin reemplazo de hardware**, gracias a su naturaleza definida por software.

La **SD-WAN basada en Inteligencia Artificial (IA)** añade una capa adicional de inteligencia, proporcionando:

- **Conocimientos basados en IA** para optimizar el rendimiento.
- **Detección de anomalías** y **resolución automatizada de problemas**, reduciendo el tiempo de inactividad.
- **Mejora de la experiencia del usuario final**, al garantizar un servicio de red más estable y eficiente.
- **Reducción de la carga operativa** para el personal de TI, al automatizar tareas rutinarias.

Finalmente, el concepto de **SASE (Secure Access Service Edge)** integra las funcionalidades de SD-WAN con servicios de seguridad en la nube. Esta solución ofrece:

- **Seguridad de red unificada**, tanto física como basada en la nube, en todos los puntos del perímetro de la red.
- **Acceso seguro y eficiente** a recursos corporativos desde cualquier ubicación.
- **Simplificación de la arquitectura de seguridad**, consolidando múltiples servicios en una sola plataforma.

## Orquestación y Gestión Centralizada de Dispositivos de Comunicaciones

La **orquestación y gestión centralizada** son prácticas clave para administrar dispositivos de red de manera eficiente mediante tecnologías como las **redes definidas por software (SDN)**. Permiten un **control centralizado**, optimizando el tráfico, la configuración y el rendimiento de toda la infraestructura de red.

### Redes Definidas por Software (SDN)

- Separan el control de la red del hardware, gestionándolo mediante software.
- Ofrecen **flexibilidad**, permitiendo ajustes rápidos en políticas y configuraciones.
- Aseguran **escalabilidad**, adaptándose a las necesidades cambiantes de la red.

### Visión Global y Control Centralizado

- **Monitoreo en tiempo real**: Supervisión continua del rendimiento y estado de los dispositivos.
- **Resolución rápida de problemas**: Identificación y mitigación eficiente de fallos.
- **Gestión del tráfico**: Priorización de aplicaciones críticas y optimización del ancho de banda.
- **Seguridad uniforme**: Aplicación de políticas de seguridad en toda la red.

### Orquestación

- **Automatización**:
    - Configuración masiva mediante scripts y plantillas.
    - Reducción de errores humanos.
- **Despliegue rápido**:
    - Integración eficiente de nuevos dispositivos con configuraciones predefinidas.
- **Actualización centralizada**:
    - Distribución uniforme de parches y actualizaciones de firmware.

### Gestión Centralizada

- **Consola única**:
    - Control y supervisión unificada de todos los dispositivos.
- **Análisis y reportes**:
    - Generación de informes detallados sobre rendimiento y uso.
- **Configuración centralizada**:
    - Cambios y ajustes uniformes desde un único punto.
- **Seguridad integrada**:
    - Protección y monitorización proactiva contra amenazas.

### Beneficios Clave

- **Eficiencia**: Automatización y centralización reducen costos y tiempos de gestión.
- **Flexibilidad**: Adaptación rápida a nuevas necesidades o tecnologías.
- **Seguridad mejorada**: Protección uniforme y actualizada.
- **Mayor disponibilidad**: Menor tiempo de inactividad por fallos o ataques.
- **Optimización de recursos**: Uso eficiente del ancho de banda y priorización inteligente.
