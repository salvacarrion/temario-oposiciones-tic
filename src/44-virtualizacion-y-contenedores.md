# Virtualización y contenedores

## Virtualización e hipervisores

La virtualización es la técnica que permite abstraer un recurso físico (servidor, almacenamiento, red, escritorio) y presentarlo como uno o varios recursos lógicos independientes mediante una capa de software. Es la base de la consolidación de servidores, del centro de datos definido por software (tema 47) y de la computación en la nube.

- **Ventajas**: consolidación de servidores y ahorro de costes (menos máquinas físicas, menor consumo energético), aislamiento entre entornos, agilidad de aprovisionamiento, escalabilidad, alta disponibilidad y recuperación ante desastres (una máquina virtual son ficheros: se copia, se migra y se restaura), entornos de prueba baratos.
- **Inconvenientes**: cierta sobrecarga de rendimiento (hoy mínima gracias a la asistencia hardware), el host físico como punto único de fallo si no se trabaja en clúster, y complejidad añadida de gestión y licenciamiento.

### Conceptos y funciones de plataforma

Terminología y capacidades comunes a las plataformas de virtualización empresariales (vSphere, Hyper-V, KVM/Proxmox):

- **Host o anfitrión**: máquina física sobre la que se ejecuta el hipervisor.
- **Guest o invitado**: cada máquina virtual (VM) que se ejecuta sobre el anfitrión, con su propio sistema operativo.
- **Máquina virtual como ficheros**: una VM se materializa en un fichero de configuración más uno o varios discos virtuales alojados en un *datastore*.
- **Operaciones en caliente**: añadir CPU, memoria o disco a una VM encendida, sin parada de servicio.
- **Snapshot**: foto del estado de una VM (disco y, opcionalmente, memoria) a la que poder volver; útil antes de cambios arriesgados, no sustituye a la copia de seguridad.
- **Migración en caliente**: mover una VM en ejecución de un host a otro sin cortar el servicio (**vMotion** en VMware, **Live Migration** en Hyper-V y KVM).
- **Balanceo dinámico de carga**: redistribución automática de las VM entre los hosts del clúster según su carga (**DRS** en VMware).
- **Alta disponibilidad (HA)**: si cae un host, sus VM se rearrancan automáticamente en el resto del clúster.
- **Sobresuscripción (overcommit)**: asignar entre todas las VM más recursos virtuales que los físicos disponibles, confiando en que no los usen a la vez; en memoria se apoya en técnicas como el **ballooning** (el hipervisor reclama memoria poco usada de unas VM para dársela a otras).
- **Thin provisioning**: los discos virtuales solo ocupan el espacio realmente escrito, no el tamaño nominal asignado.

### Tipos de virtualización

- **Virtualización de servidores**: ejecutar varias máquinas virtuales sobre un mismo host físico.
    - **Virtualización completa (nativa)**: el hipervisor presenta un hardware virtual completo y el sistema operativo invitado se ejecuta sin modificar. Hoy se apoya en la **virtualización asistida por hardware**: extensiones del procesador **Intel VT-x** y **AMD-V** (estándar en cualquier CPU actual), traducción de direcciones en hardware (**EPT/RVI**) y virtualización de E/S (**VT-d/AMD-Vi**, **SR-IOV**).
    - **Paravirtualización**: el sistema operativo invitado se modifica para colaborar con el hipervisor, sustituyendo las instrucciones privilegiadas por llamadas a su API (**hypercalls**). Gana rendimiento a costa de exigir kernels adaptados. El ejemplo clásico es **Xen** en modo PV; hoy la técnica pervive sobre todo en los drivers paravirtualizados (**virtio** en KVM, VMware Tools, servicios de integración de Hyper-V).
    - **Virtualización a nivel de sistema operativo**: un único kernel anfitrión ejecuta varios espacios de usuario aislados, los **contenedores** (LXC, Docker, *jails* de FreeBSD, zonas de Solaris). No hay hipervisor ni sistema operativo invitado completo (se desarrolla en la sección siguiente).
- **Virtualización de escritorio (VDI)**: el escritorio del usuario se ejecuta como VM en el CPD y se accede a él por red desde cualquier dispositivo; escritorios persistentes o no persistentes. Se desarrolla en el tema 48.
- **Virtualización de aplicaciones**: la aplicación se empaqueta y ejecuta aislada del sistema operativo donde corre, eliminando conflictos de librerías (Citrix Virtual Apps, VMware ThinApp).
- **Virtualización del almacenamiento**: presenta el almacenamiento físico como volúmenes lógicos independientes de los dispositivos (tema 45).
- **Virtualización de red**: crea redes lógicas independientes de la topología física; su evolución son las redes definidas por software, SDN y NFV (tema 68).
- **Virtualización del CPD (SDDC)**: cómputo, red y almacenamiento virtualizados y orquestados por software (temas 43 y 47).
- **Emulación**: reproducir por software una arquitectura hardware completa distinta de la real (procesador incluido), lo que permite ejecutar binarios de otra plataforma a costa de un gran coste de rendimiento. Ejemplos: **QEMU** (en modo emulación), Bochs, MAME. Wine no es un emulador sino una capa de compatibilidad (reimplementa las API de Windows sobre Linux).

### El hipervisor

El hipervisor o monitor de máquina virtual (VMM) es el software que crea, ejecuta y gestiona las máquinas virtuales, repartiendo entre ellas los recursos físicos del host y manteniéndolas aisladas entre sí.

- **Tipo 1 (bare metal o nativo)**: se ejecuta directamente sobre el hardware, sin sistema operativo anfitrión. Máximo rendimiento y seguridad; es el habitual en el CPD.
    - **Ejemplos**: VMware **ESXi** (núcleo de la plataforma vSphere), Microsoft **Hyper-V**, **KVM** (integrado en el kernel Linux; base de Proxmox VE, oVirt y OpenStack) y **Xen** (base de XenServer 8, antes Citrix Hypervisor, y de XCP-ng).
- **Tipo 2 (hosted o alojado)**: se ejecuta como una aplicación sobre un sistema operativo anfitrión con el que comparte recursos. Más sencillo de instalar y usar; orientado a escritorio, pruebas y desarrollo.
    - **Ejemplos**: VMware Workstation/Fusion, Oracle **VirtualBox**, Parallels Desktop, QEMU.
- **El caso KVM**: la frontera entre tipos es difusa. KVM se carga como un módulo sobre un Linux ya instalado (parecería tipo 2), pero convierte al propio kernel en hipervisor con acceso directo al hardware, por lo que se clasifica como **tipo 1**.

## Contenedores: Docker

Los contenedores son virtualización a nivel de sistema operativo: empaquetan una aplicación con todas sus dependencias (binarios, librerías, configuración) en una unidad ligera y portable que se ejecuta aislada pero **compartiendo el kernel del anfitrión**. Garantizan que la aplicación se comporte igual en desarrollo, pruebas y producción, y son la unidad de despliegue natural de los microservicios (tema 56).

- **Base tecnológica (kernel Linux)**:
    - **Namespaces**: dan a cada contenedor una vista privada del sistema: procesos (pid), red (net), sistema de ficheros (mnt), nombre de máquina (uts), comunicación entre procesos (ipc) y usuarios (user).
    - **cgroups** (*control groups*): limitan y contabilizan los recursos que consume cada contenedor (CPU, memoria, E/S).
    - **Refuerzo de seguridad**: *capabilities*, seccomp y AppArmor/SELinux restringen lo que el contenedor puede pedirle al kernel.
- **Contenedor frente a máquina virtual**: al compartir kernel, el aislamiento del contenedor es menor que el de una VM (es pregunta habitual):

| Aspecto | Máquina virtual | Contenedor |
| --- | --- | --- |
| Aislamiento | Hardware virtual y SO completo por VM (fuerte) | Procesos que comparten el kernel del host (más débil) |
| Tamaño | Gigabytes (SO invitado completo) | Megabytes (aplicación y dependencias) |
| Arranque | Minutos | Segundos o menos |
| Densidad por host | Decenas | Cientos |
| Sistema operativo | Cualquiera, distinto del host incluso | Ligado al kernel del host |
| Sobrecarga | Hipervisor + SO invitado | Mínima |

### Docker

Docker (2013) popularizó los contenedores al estandarizar el formato de imagen y simplificar su construcción y distribución. Tiene arquitectura cliente-servidor.

- **Arquitectura**:
    - **Cliente `docker`**: interfaz de línea de comandos que habla con el demonio a través de su API REST.
    - **Docker Engine (`dockerd`)**: demonio que construye imágenes y gestiona contenedores, redes y volúmenes. Desde **Docker Engine 29** (2026) usa por defecto el almacén de imágenes de containerd.
    - **containerd**: runtime de alto nivel que gestiona el ciclo de vida de los contenedores; delega la creación efectiva en **runc**, el runtime de bajo nivel de referencia.
- **Componentes**:
    - **Imagen**: plantilla inmutable de solo lectura, construida por **capas** reutilizables; se define en un **Dockerfile**.
    - **Contenedor**: instancia en ejecución de una imagen, a la que se añade una capa superior de escritura efímera.
    - **Registro (registry)**: repositorio para almacenar y distribuir imágenes: **Docker Hub** es el público de referencia; en entornos corporativos se usan registros privados (Harbor, GitLab Container Registry).
    - **Docker Compose**: define y ejecuta aplicaciones multicontenedor descritas en un fichero YAML (`compose.yaml`), típicamente para desarrollo y entornos pequeños.
    - **Docker Swarm**: orquestador propio de Docker, más sencillo que Kubernetes pero de uso minoritario.
- **Estándares OCI** (*Open Container Initiative*, Linux Foundation, **2015**): garantizan que imágenes y runtimes sean interoperables entre herramientas (Docker, Podman, Kubernetes):
    - **runtime-spec** (v1.3.0, 2024): cómo ejecutar un contenedor ya desempaquetado.
    - **image-spec** (v1.1.1, 2025): formato de la imagen y sus capas.
    - **distribution-spec** (v1.1.1, 2025): API de los registros para subir y bajar imágenes.
    - Gracias a OCI existen alternativas compatibles como **Podman** (sin demonio y *rootless*, orientado a seguridad) o CRI-O.

Ejemplo de Dockerfile mínimo:

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

- **Comandos básicos**: `docker build -t miapp:1.0 .` (construir la imagen), `docker run -d -p 80:8000 miapp:1.0` (ejecutar publicando el puerto), `docker ps` (contenedores activos), `docker images`, `docker pull` / `docker push` (bajar/subir del registro), `docker logs` y `docker exec -it <id> bash` (entrar en un contenedor).

## Orquestación: Kubernetes

Cuando se pasa de unos pocos contenedores a decenas o cientos repartidos en varios servidores, hace falta un **orquestador**: software que automatiza su despliegue, escalado, red, balanceo y autorreparación. **Kubernetes** (K8s), creado por Google a partir de su sistema interno Borg y donado a la **CNCF** (*Cloud Native Computing Foundation*) en **2015**, es el estándar de facto; publica **tres versiones al año** (vigente: **v1.36**, abril de 2026).

### Arquitectura del clúster

Un clúster de Kubernetes se compone de un plano de control y un conjunto de nodos de trabajo. La denominación «master» está retirada del proyecto: hoy se habla de **plano de control** (*control plane*).

- **Plano de control**:
    - **kube-apiserver**: puerta de entrada del clúster; expone la API REST con la que interactúan usuarios, componentes y controladores.
    - **etcd**: almacén clave-valor distribuido y consistente donde se guarda todo el estado del clúster.
    - **kube-scheduler**: decide en qué nodo se ejecuta cada pod según recursos disponibles y restricciones (afinidad, *taints*).
    - **kube-controller-manager**: ejecuta los bucles de control que reconcilian el estado real con el declarado.
- **Nodos de trabajo**:
    - **kubelet**: agente de cada nodo; garantiza que los contenedores de sus pods estén en ejecución y sanos.
    - **kube-proxy**: mantiene las reglas de red que hacen funcionar los Services.
    - **Runtime de contenedores**: containerd o CRI-O, integrados mediante la interfaz **CRI** (*Container Runtime Interface*); el soporte directo de Docker (dockershim) se eliminó en la **v1.24**.
- **Modelo declarativo**: el estado deseado se describe en manifiestos YAML y los controladores lo reconcilian de forma continua: si un pod muere se recrea, si cae un nodo sus pods se reprograman en otros.

### Objetos principales

- **Pod**: unidad mínima de despliegue: uno o más contenedores que comparten red (IP) y almacenamiento.
- **ReplicaSet**: mantiene en ejecución un número fijo de réplicas de un pod.
- **Deployment**: gestiona ReplicaSets y aporta despliegue declarativo, actualización continua (*rolling update*) y vuelta atrás (*rollback*); es el objeto habitual para aplicaciones sin estado.
- **StatefulSet**: para aplicaciones con estado (bases de datos): da a cada réplica identidad y almacenamiento estables.
- **DaemonSet**: asegura una copia del pod en cada nodo (agentes de monitorización, logs).
- **Job y CronJob**: tareas que se ejecutan hasta terminar, puntuales o planificadas.
- **Service**: IP virtual y nombre DNS estables para acceder a un conjunto de pods; tipos **ClusterIP** (interno), **NodePort** (puerto fijo en cada nodo) y **LoadBalancer** (balanceador externo, típico en nube).
- **Ingress**: enrutamiento HTTP/HTTPS de entrada al clúster por host y ruta, con terminación TLS; requiere un controlador. El controlador Ingress NGINX se retiró en marzo de 2026 y el proyecto evoluciona hacia la **Gateway API**.
- **ConfigMap y Secret**: configuración y credenciales desacopladas de la imagen del contenedor.
- **Namespace**: partición lógica del clúster para separar equipos o entornos.
- **PersistentVolume (PV) y PersistentVolumeClaim (PVC)**: volumen de almacenamiento persistente y solicitud que hace de él una aplicación.

Ejemplo de manifiesto (Deployment con 3 réplicas):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: miapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: miapp
  template:
    metadata:
      labels:
        app: miapp
    spec:
      containers:
        - name: miapp
          image: miapp:1.0
          ports:
            - containerPort: 8000
```

- **Comandos básicos**: `kubectl apply -f deployment.yaml` (aplicar un manifiesto), `kubectl get pods` (estado), `kubectl scale deployment miapp --replicas=5` (escalar), `kubectl rollout undo deployment/miapp` (rollback), `kubectl logs` y `kubectl describe` (diagnóstico).

### Ecosistema y distribuciones

- **Helm**: gestor de paquetes de Kubernetes; los *charts* empaquetan y versionan conjuntos de manifiestos parametrizables.
- **Autoescalado**: **HPA** (horizontal: más pods según carga), **VPA** (vertical: más CPU/memoria por pod) y Cluster Autoscaler (más nodos).
- **Distribuciones empresariales**: Red Hat **OpenShift** (muy extendida en administraciones públicas), SUSE Rancher y **k3s** (ligera, para edge), VMware Tanzu.
- **Servicios gestionados en nube**: Amazon **EKS**, Microsoft **AKS** y Google **GKE**: el proveedor opera el plano de control y el cliente gestiona las cargas.

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Docker, docs.docker.com (Docker Engine 29), consulta de julio de 2026.
- Documentación oficial de Kubernetes, kubernetes.io (v1.36, abril de 2026), consulta de julio de 2026.
- Especificaciones OCI (opencontainers.org): runtime-spec v1.3.0 (noviembre de 2024), image-spec v1.1.1 (marzo de 2025) y distribution-spec v1.1.1 (enero de 2025).
