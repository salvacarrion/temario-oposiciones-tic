# Virtualización y contenedores
## Virtualización

La virtualización es una técnica que permite abstraer un recurso físico
en uno virtual mediante software.

Entre sus **ventajas** destacan la independencia, escalabilidad, alta
disponibilidad, flexibilidad, seguridad, agilidad, protección del medio
ambiente y ahorro de costes. Como **desventaja**, puede presentar un
mayor consumo de recursos y un rendimiento ligeramente inferior, aunque
en la actualidad este impacto es mínimo.

**Funciones comunes:**

- **Operaciones en caliente**: Realizar operaciones sin necesidad de
  apagar la máquina.

- **Migración de máquinas virtuales entre servidores físicos**.

- **Distribución de carga en tiempo real**: Permite optimizar el uso de
  recursos.

**Tipos de virtualización**:

- **Virtualización de servidores**: Permite ejecutar varias máquinas
  virtuales en un solo host físico.

  - **Virtualización completa, de hardware o nativa**: Utiliza un
    software llamado **hipervisor** capaz de crear y gestionar máquinas
    virtuales que emulan varios hosts aislados en un único servidor
    físico.

    - **Host/Anfitrión**: Máquina física donde está el hipervisor.

    - **Invitado/Guest**: Máquinas virtuales.

    - Consiste en un fichero de configuración y un fichero de datastore
      que simula el disco duro virtual.

  - **Virtualización parcial o paravirtualización**: Ofrece mayor
    rendimiento pero requiere sistemas operativos adaptados para
    realizar llamadas directas al hardware físico.

    - Las llamadas, conocidas como **hypercalls**, se realizan mediante
      el API del hipervisor.

    - Las operaciones se envían directamente al hardware físico en lugar
      de ejecutarse en la capa de virtualización.

    - **Ejemplos:** VMware ESXi, Citrix XenServer, Microsoft Hyper-V.

- **Virtualización de sistema operativo**: Permite ejecutar un sistema
  operativo dentro de otro, tomando parte de los recursos del sistema
  operativo anfitrión.

  - **Ejemplos:** VMware Workstation, Oracle VirtualBox, Parallels
    Desktop, Microsoft Virtual PC.

- **Virtualización de escritorio o puesto de trabajo** (*Virtual Desktop
  Infrastructure* - **VDI**): Permite ejecutar un escritorio virtual en
  un servidor y acceder a él desde cualquier dispositivo.

  - **Características**:

    - Independiza el escritorio que utiliza el usuario del hardware que
      usa para su acceso.

    - El escritorio se ejecuta remotamente en un servidor, incluyendo el
      disco duro.

    - Requiere conexión de red.

    - Permite gran flexibilidad y ahorro de costes.

  - **Tipos de escritorios**:

    - **Estático/Dinámico:**

      - **Estático**: Cada usuario se conecta siempre a la misma máquina
        virtual.

      - **Dinámico**: Se crea una nueva máquina virtual para cada
        usuario que se conecta.

    - **Persistente / No-Persistente:**

      - **Persistente**: Los cambios se conservan al reiniciar la
        máquina.

      - **No persistente**: Los cambios no se conservan al reiniciar la
        máquina.

- **Virtualización de aplicaciones**: Permite ejecutar aplicaciones en
  diferentes sistemas operativos o plataformas sin tener que instalarlas
  de manera nativa.

  - Independiza las aplicaciones del entorno donde se ejecutan,
    eliminando problemas de incompatibilidad de librerías con otras
    aplicaciones o el propio sistema operativo.

  - **Ejemplos:** Citrix XenApp, Microsoft App-V, VMware Horizon.

- **Virtualización del almacenamiento**: Permite crear múltiples
  volúmenes lógicos a partir de un espacio de almacenamiento físico.

  - **Mecanismos de implementación**: SAN (*Storage Area Network*) y NAS
    (*Network Attached Storage*).

- **Virtualización de red**: Permite crear múltiples redes lógicas a
  partir de una red física.

- **Virtualización de centros de datos**: Permite virtualizar servidores
  junto con dispositivos de almacenamiento, redes y otros equipos de
  infraestructura.

  - Incluye virtualización de cómputo, de red, de almacenamiento y
    orquestación.

**Otras formas de virtualización:**

- **Emulación**: Permite ejecutar programas en una plataforma diferente
  de aquella para la cual fueron escritos originalmente, imitando o
  suplantando vía software la arquitectura y recursos completos
  (procesador, memoria, conjunto de instrucciones, comunicaciones).

  - Es muy lenta.

  - **Ejemplos:** Bochs, MAME, QEMU, Microsoft Virtual PC y Wine.

- **Simulación**: Reproduce el comportamiento del programa.

**Hypervisor**

El **hipervisor** (o monitor de máquina virtual) es el software
encargado de crear y gestionar máquinas virtuales. Actúa como una capa
de virtualización de hardware que permite utilizar, al mismo tiempo,
diferentes sistemas operativos en una misma computadora.

**Tipos de hipervisores:**

- **Hipervisor Tipo 1 (Nativo, Unhosted o Bare Metal)**: Se ejecutan
  directamente en el hardware del host físico y tienen acceso directo a
  los recursos de la máquina.

  - Son muy rápidos y eficientes en el uso de recursos, pero requieren
    hardware especialmente diseñado para soportarlos.

  - **Ejemplos:** Kernel-based Virtual Machine (**KVM**), Microsoft
    Hyper-V, VMware ESXi, Oracle VM Server.

- **Hipervisor Tipo 2 (Hosted)**: Se ejecutan en un sistema operativo
  existente y comparten los recursos del host físico con el sistema
  operativo anfitrión.

  - Son más fáciles de instalar y usar, pero menos eficientes en el uso
    de recursos y menos seguros que los hipervisores de tipo 1.

  - **Ejemplos:** VMware Workstation, Parallels Desktop, VirtualBox,
    VMware Player, QEMU, Bhyve.

- **Hipervisor Tipo Híbrido**: Combinan características de los
  hipervisores de tipo 1 y tipo 2. Se ejecutan en el hardware del host
  físico pero requieren un sistema operativo anfitrión para funcionar.

  - El hipervisor interactúa directamente con el hardware en algunas
    ocasiones y utiliza servicios del sistema operativo anfitrión en
    otras.

  - **Ejemplos:** Microsoft Virtual PC y Microsoft Virtual Server 2005
    R2.

## Contenedores Docker

Herramientas de virtualización a nivel de sistema operativo que permiten
ejecutar aplicaciones de manera aislada y portátil en cualquier entorno.
Gracias a su diseño, los contenedores aseguran que las aplicaciones sean
consistentes en diferentes entornos, desde el desarrollo hasta la
producción.

**Componentes**

- **Imágenes Docker**: Son plantillas que contienen todo lo necesario
  para ejecutar una aplicación, incluyendo el código fuente, librerías,
  configuraciones, entre otros elementos necesarios.

  - Se generan a partir de un archivo **Dockerfile**, que especifica
    paso a paso las instrucciones para construir la imagen.

- **Contenedores Docker**: Representan instancias ejecutables de una
  imagen.

  - Un contenedor puede contener una única aplicación o varias
    aplicaciones que operen conjuntamente.

  - Los contenedores están **aislados** entre sí, lo que significa que
    no tienen acceso ni a los recursos del sistema anfitrión ni a otros
    contenedores. Esto garantiza un alto nivel de seguridad y
    portabilidad.

- **Docker Engine**: Es el motor que gestiona y ejecuta tanto
  contenedores como imágenes. Actúa como el núcleo operativo de Docker.

- **Docker Registry**: Es un repositorio utilizado para almacenar y
  distribuir imágenes Docker.

  - Ejemplo: **Docker Hub**, que es el registro más utilizado y permite
    a los usuarios subir, descargar y compartir imágenes con facilidad.

- **\*Docker Machine**: Herramienta para instalar Docker Engine en
  máquinas virtuales o físicas y gestionarlas desde una única interfaz.

- **\*Docker Compose**: Permite definir y ejecutar aplicaciones
  multicontenedor. Los servicios se describen en un archivo YAML,
  facilitando su configuración y despliegue.

- **\*Docker Swarm**: Es una herramienta de **orquestación de
  contenedores** que permite implementar y gestionar aplicaciones en
  contenedores a escala.

  - Aunque es más sencilla que Kubernetes, su funcionalidad es menos
    avanzada y su uso es menos extendido.

## Plataforma de Kubernetes

Plataforma open-source diseñada para la **orquestación de
contenedores**. Se utiliza para **automatizar** la implementación,
escalado y administración de aplicaciones en contenedores, siendo una de
las herramientas más robustas y populares en este ámbito.

**Componentes de Kubernetes**

- **Nodos**: Son los servidores que ejecutan los contenedores. Cada nodo
  cuenta con un agente llamado **kubelet**, que se encarga de gestionar
  los contenedores en el nodo.

- **Clúster**: Agrupación de nodos que trabajan de manera conjunta para
  ejecutar aplicaciones.

- **Master**: Es el conjunto de componentes encargados de controlar y
  administrar el clúster.

  - Incluye el **controlador**, que supervisa el estado del clúster y
    toma decisiones sobre su gestión.

  - Otros componentes clave son el **API Server**, que actúa como
    intermediario para la comunicación, y el **Scheduler**
    (Planificador), responsable de asignar las tareas a los nodos.

- **Pods (Cápsulas)**: Son las unidades básicas de ejecución en
  Kubernetes. Pueden contener uno o más contenedores junto con los
  recursos compartidos que necesitan.

- **Deployments**: Permiten desplegar y gestionar aplicaciones dentro
  del clúster. Ofrecen mecanismos para el escalado y actualizaciones de
  las aplicaciones.

- **Services**: Proveen un punto de acceso a las aplicaciones a través
  de una dirección IP y un puerto específico, facilitando la
  conectividad entre los componentes.

**Funcionamiento de Kubernetes**

El funcionamiento de Kubernetes se centra en la creación y gestión de
**pods** y **deployments** para ejecutar aplicaciones en el clúster.

- El usuario define un **deployment**, especificando el número de
  réplicas necesarias y los nodos donde deben ejecutarse.

- El **Scheduler** asigna las réplicas a los nodos disponibles, mientras
  que el **Controlador** asegura que se mantenga el número deseado de
  réplicas activas.

- En caso de fallo de un nodo o de un pod, Kubernetes crea
  automáticamente nuevos pods para cumplir con el estado deseado.

- Los **Services** permiten la conexión a las aplicaciones mediante
  direcciones IP y puertos definidos, ofreciendo un acceso consistente
  incluso en escenarios de escalado o fallos.
