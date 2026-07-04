# Puesto de trabajo TIC

## El puesto de trabajo TIC en una organización

El puesto de trabajo TIC es fundamental para asegurar el correcto funcionamiento y gestión de la infraestructura tecnológica en una organización. Su objetivo principal es garantizar que todos los sistemas y aplicaciones operen de manera eficiente y segura, facilitando así las actividades cotidianas de la empresa.

### Normalización

La normalización implica establecer estándares, políticas y procedimientos para el uso de la tecnología dentro de la organización. Esto garantiza la eficiencia y consistencia en el trabajo, al proporcionar directrices claras sobre cómo deben utilizarse los recursos TIC. Una adecuada normalización facilita la interoperabilidad entre sistemas y simplifica la resolución de problemas.

### Actualización

Mantener los sistemas y aplicaciones actualizados es vital para asegurar su eficiencia y seguridad. Las actualizaciones frecuentes corrigen errores, mejoran el rendimiento y protegen contra nuevas amenazas de seguridad. Una política de actualización regular ayuda a prevenir fallos y a mantener la competitividad tecnológica.

### Seguridad

La seguridad es esencial para proteger los datos e información de la empresa. Se debe garantizar la integridad y disponibilidad de los sistemas y aplicaciones mediante la implementación de medidas como firewalls, contraseñas seguras y protocolos de encriptación. Además, es crucial formar al personal en el uso seguro de los recursos TIC para prevenir vulnerabilidades humanas.

### Gestión

La gestión de los recursos TIC implica planificar, organizar y controlar su uso dentro de la organización. Esto incluye la asignación de tareas y responsabilidades, la planificación de proyectos y la toma de decisiones estratégicas sobre la implementación y uso de tecnologías. Una gestión eficaz maximiza el retorno de inversión y alinea la tecnología con los objetivos empresariales.

## Infraestructura del puesto de trabajo virtual (VDI)

La virtualización de escritorio o VDI permite ejecutar un escritorio virtual en un servidor central y acceder a él desde cualquier dispositivo. Esto independiza el sistema operativo y las aplicaciones del hardware utilizado para acceder, proporcionando flexibilidad y ahorro de costes.

### Componentes del VDI

- **Servidor central**: Aloja los escritorios virtuales y gestiona los recursos compartidos.
- **Cliente de escritorio virtual**: Software que permite a los usuarios acceder a los escritorios virtuales desde sus dispositivos.

### Características del VDI

- **Independencia del hardware**: El escritorio virtual no depende del dispositivo de acceso.
- **Ejecución remota**: El escritorio y las aplicaciones se ejecutan en el servidor, no en el dispositivo local.
- **Conexión de red necesaria**: Requiere una conexión estable para acceder al servidor.
- **Flexibilidad y ahorro**: Reduce costes en hardware y facilita la administración centralizada.

### Ventajas del VDI

- **Aprovechamiento del hardware**: Optimiza el uso de recursos del servidor.
- **Eficiencia energética**: Disminuye el consumo eléctrico al utilizar dispositivos menos potentes.
- **Ahorro de espacio**: Reduce la necesidad de equipos físicos en el puesto de trabajo.
- **Administración simplificada**: Facilita la gestión y actualización de sistemas desde un punto central.
- **Alta disponibilidad y recuperación ante desastres**: Mejora la resiliencia ante fallos del sistema.
- **Alto rendimiento y redundancia**: Proporciona un rendimiento consistente y respaldo en caso de fallos.
- **Seguridad mejorada**: Centraliza los datos, reduciendo el riesgo de pérdida o robo.
- **Reducción de costes**: Disminuye gastos en hardware, mantenimiento y soporte.
- **Escalabilidad**: Permite añadir o reducir recursos según las necesidades.
- **Retrocompatibilidad**: Soporta aplicaciones antiguas en entornos modernos.
- **Clústers virtuales**: Facilita la creación de entornos de prueba y desarrollo.
- **Personalización y flexibilidad**: Adapta los escritorios a las necesidades específicas de cada usuario.

### Otros beneficios del VDI

- **Movilidad y colaboración**: Los trabajadores pueden acceder a su escritorio desde cualquier lugar.
- **Gestión y protección de datos**: Almacena y controla la información de forma centralizada, mejorando la seguridad y cumplimiento normativo.

### Desventajas del VDI

- **Disminución del rendimiento**: Puede haber latencia o retardos si la infraestructura no es adecuada.
- **Punto único de fallo**: Si el servidor central falla, todos los escritorios pueden verse afectados.
- **Dependencia de la solución elegida**: Limitaciones según el proveedor y el sistema operativo anfitrión.
- **Requisitos de hardware y vídeo**: La aceleración 3D y aplicaciones gráficas intensivas pueden ser problemáticas.
- **Limitaciones en el número de máquinas virtuales**: Depende de la capacidad del servidor.
- **Complejidad añadida**: Requiere personal especializado para su implementación y mantenimiento.
- **Dependencia de una conexión a internet de alta velocidad**: Sin una conexión adecuada, el acceso puede ser deficiente.
- **Coste de mantenimiento y actualización**: La infraestructura de VDI puede ser costosa de mantener y actualizar.

### Planificación de la virtualización

- **Análisis de roles y requisitos de usuario**: Identificar las necesidades específicas de cada perfil.
- **Evaluación de requisitos de aplicaciones**: Determinar qué software es esencial y sus demandas.
- **Evaluación de la topología de datos**: Comprender cómo se gestionan y almacenan los datos.
- **Servicios de directorio funcionando correctamente**: Asegurar que la autenticación y autorizaciones están operativas.
- **Evaluación de la infraestructura actual**: Identificar limitaciones y áreas de mejora.
- **Verificación de necesidades de seguridad**: Establecer medidas para proteger la información.
- **Establecimiento de expectativas con los usuarios**: Comunicar los cambios y beneficios esperados.
- **Medición del tamaño de almacenamiento**: Planificar el espacio necesario para los datos y sistemas.
- **Requisitos de soporte técnico**: Asegurar recursos para mantenimiento y resolución de problemas.
- **Evaluación del TCO y el ROI**: Analizar los costes totales y el retorno de la inversión.

### Tipos de escritorios virtuales

- **Estático / Dinámico:**
    - **Estático**: Cada usuario accede siempre a la misma máquina virtual, permitiendo personalización persistente.
    - **Dinámico**: Se crea una nueva máquina virtual para cada sesión, ideal para tareas genéricas.
- **Persistente / No-Persistente:**
    - **Persistente**: Los cambios realizados por el usuario se conservan después de reiniciar.
    - **No persistente**: Los cambios no se guardan, manteniendo un entorno limpio en cada inicio.

### Soluciones comerciales de VDI

- **Oracle Secure Global Desktop**: Acceso seguro desde cualquier ubicación, virtualización de escritorio y aplicaciones, compatible con cualquier cliente.
- **Oracle VM VirtualBox**: Virtualización local con capacidad de teletransportar máquinas virtuales entre hosts sin interrupción.
- **Microsoft Hyper-V**: Hipervisor para sistemas de 64 bits con soporte para AMD-V o Intel VT.
- **Citrix XenDesktop y XenApp**: Soluciones comerciales líderes en virtualización de escritorio y aplicaciones.
- **QVD**: Herramienta de código abierto para Linux con hypervisor KVM, compatible con cualquier cliente.
- **Red Hat Enterprise Virtualization**: Virtualización basada en servidores Red Hat Enterprise Linux con hypervisor KVM (no soporta clientes MacOS).
- **VMware**
    - **VMware vSphere**: Virtualización de servidores.
    - **VMware NSX**: Virtualización de redes.
    - **VMware Horizon**: Virtualización de escritorios.
        - **Horizon 7**: Distribución segura de escritorios y aplicaciones en cualquier dispositivo y ubicación.
        - **Horizon Apps**: Acceso a aplicaciones publicadas, SaaS y móviles.
        - **Horizon FLEX**: Trabajo en escritorios virtuales en PC o Mac sin conexión de red, con control centralizado y alta seguridad.
        - **Horizon Cloud**
            - **On-Premises Infrastructure**: Implementación en local o nube privada.
            - **Hosted Infrastructure**: Implementación en la nube pública de VMware.

### Conceptos adicionales

- **SGD Gateway**: Servidor proxy diseñado para ubicarse en una zona desmilitarizada (DMZ), permitiendo que Oracle Secure Global Desktop resida en la red interna. Todas las conexiones se autentican en la DMZ, mejorando la seguridad.
- **Prevención de ejecución de datos (DEP)**: Tecnologías de hardware y software que realizan comprobaciones adicionales en la memoria para proteger contra código malicioso y vulnerabilidades.
- **DMZ (Demilitarized Zone)**: Red local ubicada entre la red interna de una organización y una red externa (Internet). Protege la red interna de ataques al aislar los servidores expuestos al público. Las conexiones desde la red externa a la DMZ están permitidas, mientras que desde la DMZ a la red interna no lo están. Esto evita que un ataque comprometido en la DMZ afecte a la red interna.

## Servicio de Gestión del Puesto de Trabajo

El **Servicio de Gestión del Puesto de Trabajo** es un componente clave para garantizar el correcto funcionamiento de los dispositivos informáticos dentro de la Administración de la Generalitat. Su objetivo principal es estandarizar, mantener y gestionar los recursos informáticos, asegurando la seguridad, calidad y disponibilidad de los mismos.

### Funciones del Servicio de Gestión del Puesto de Trabajo

- **Gestión y soporte al CAU-TIC**: Asegura la atención y resolución de incidencias tecnológicas a través del Centro de Atención al Usuario TIC.
- **Gestión, mantenimiento y administración del material informático**: Incluye el inventario, actualización y mantenimiento de hardware y software.
- **Definición, estandarización, homogeneización y evolución del Puesto de Trabajo Normalizado (PTN)**: Se asegura de que los dispositivos sigan estándares técnicos comunes, optimizando su uso.
- **Implantación de medidas técnicas y organizativas de seguridad**: Garantiza la seguridad, calidad, disponibilidad, integridad y uso adecuado de los dispositivos asignados.

### Puesto de Trabajo Normalizado (PTN)

El **Puesto de Trabajo Normalizado (PTN)** es la configuración estandarizada y personalizada del sistema operativo y aplicaciones base diseñada por la **DGTIC**. Esta configuración está destinada a todos los dispositivos gestionados en la organización, asegurando uniformidad y eficiencia.

- **Nomenclatura de dispositivos**:
    - Sobremesa: **"PC" + Código de Inventario (CI)**
    - Sobremesa externo: **"XPC" + CI**
    - Portátil: **"PO" + CI**
- **Aplicaciones base incluidas**:
    - Navegadores web: **Google Chrome y Microsoft Edge**
    - Seguridad: **Antivirus**
    - Herramientas adicionales: **Java, Autofirma**, entre otras.
- **Ciclo de actualización**: Las configuraciones y actualizaciones del PTN se revisan y despliegan anualmente durante el **primer trimestre**.

### Despliegue de Actualizaciones y Configuraciones

Se realiza mediante dos herramientas principales:

- **Microsoft Endpoint Configuration Manager (MECM)**: Analiza las necesidades de cada sistema según el perfil profesional del usuario, desplegando las configuraciones y actualizaciones pertinentes.
- **Botiga de Software**: Permite al usuario instalar software autorizado de manera autónoma.

### Medidas de Seguridad del PTN

- **Política de seguridad**: Configuraciones a nivel de dominio para proteger el entorno informático.
- **Antivirus y cortafuegos**: Soluciones centralizadas para prevenir amenazas.
- **Cifrado de disco**: Asegura la protección de la información almacenada en los dispositivos.
- **Actualizaciones de seguridad**: Garantizan la corrección de vulnerabilidades y el cumplimiento de normativas.

### Perfiles de Usuarios

El **PTN base** se adapta a las necesidades y el ámbito profesional de cada usuario. Esta personalización permite optimizar los recursos y mejorar la experiencia del usuario en su entorno laboral.

### Composición del Puesto de Trabajo Normalizado

- **Hardware (HW)**:
    - Unidad central de procesamiento (CPU)
    - Pantalla de visualización
    - Teclado
    - Dispositivo señalador: Ratón, trackball, tableta, entre otros.
- **Software (SW)**:
    - Sistema operativo
    - Paquete ofimático estándar
    - Aplicaciones homologadas por la **DGTIC**: Navegadores web, compresores, visores, desarrollos propios, scripts, etc.
    - Servicios finalistas: **Antivirus**, herramientas de seguridad, entre otros.

### Proceso de Actualización de Windows Update for Business

El mecanismo de actualizaciones sigue un flujo optimizado para aprovechar recursos locales y minimizar el tráfico hacia servidores externos:

1. El **PC** solicita a Microsoft (CDN) la lista de actualizaciones pendientes.
2. Las configuraciones necesarias ya han sido distribuidas previamente por el **MECM/SCCM**.
3. El **PC** busca las actualizaciones en otros equipos de su red local. Si no las encuentra, solicita los datos al servidor **Microsoft Connected Cache**.
4. Si el **Microsoft Connected Cache** no dispone de las actualizaciones, las solicita al **CDN de Microsoft** y las proporciona al **PC**.
5. En caso de no encontrar actualizaciones, el **PC** se conecta directamente al **CDN de Microsoft**.
6. Una vez descargadas, el **PC** pone las actualizaciones a disposición del resto de equipos de la red.
