# Sistemas operativos

El sistema operativo es la capa de software que gestiona el hardware y ofrece a las aplicaciones una máquina extendida más simple y segura que el hardware desnudo. Este tema cubre sus conceptos y mecanismos fundamentales (procesos, memoria, ficheros y E/S) y el panorama actual de familias, desde el puesto de trabajo hasta el mainframe. La administración práctica de GNU/Linux y de Windows se desarrolla en los temas 47 y 48.

## Concepto, funciones y estructura

Un sistema operativo cumple dos papeles complementarios: **gestor de recursos** (reparte CPU, memoria y dispositivos entre procesos que compiten) y **máquina extendida** (abstrae el hardware en conceptos manejables: proceso, fichero, socket). Las aplicaciones le piden servicios mediante **llamadas al sistema** (*system calls*).

- **Modos de ejecución**: el núcleo (*kernel*) corre en **modo privilegiado** (acceso total al hardware) y las aplicaciones en **modo usuario**; la frontera se cruza con llamadas al sistema e **interrupciones** (de dispositivo, de reloj y excepciones).
- **Llamadas al sistema**: la interfaz de servicios del núcleo. En POSIX: `fork`/`exec` (crear procesos), `open`/`read`/`write` (ficheros), `kill` (señales); en Windows las expone la API Win32. Las bibliotecas estándar las envuelven para el programador.
- **Arquitectura del núcleo**: **monolítica** (todo el SO en modo núcleo, con módulos cargables: Linux), **microkernel** (servicios mínimos en el núcleo y el resto como procesos servidores: MINIX, QNX) e **híbrida** (Windows, macOS).
- **Componentes clásicos**: gestión de procesos, gestión de memoria, sistema de ficheros, gestión de E/S, red y seguridad (autenticación, control de acceso, auditoría).

## Procesos, hilos y planificación

El **proceso** es un programa en ejecución con su espacio de direcciones propio; su información de control vive en el **PCB** (*process control block*). El **hilo** es la unidad de ejecución dentro de un proceso: los hilos de un mismo proceso comparten memoria, lo que abarata la comunicación y el cambio de contexto.

- **Estados básicos**: **listo, en ejecución y bloqueado** (más nuevo y terminado). El **cambio de contexto** guarda y restaura el estado del procesador al alternar procesos.
- **Planificación de CPU**: **FCFS** (por orden de llegada), **SJF** (el trabajo más corto primero), **Round Robin** (turnos con *quantum* de tiempo, el clásico de tiempo compartido) y por **prioridades** (con envejecimiento para evitar inanición). Se distingue la planificación **apropiativa** (el SO puede expulsar al proceso en ejecución) de la **no apropiativa**.
- **Concurrencia**: el acceso a datos compartidos exige **exclusión mutua** en las secciones críticas, con primitivas como los **semáforos** (Dijkstra), los mutex y los monitores.
- **Interbloqueo** (*deadlock*): situación en la que varios procesos se esperan circularmente. Requiere las **cuatro condiciones de Coffman** (exclusión mutua, retención y espera, no expropiación y espera circular); se trata con prevención, evitación (algoritmo del banquero), detección y recuperación, o ignorándolo (la opción práctica habitual).

## Gestión de memoria

La **memoria virtual** da a cada proceso un espacio de direcciones propio y protegido, traducido a memoria física por la **MMU**; permite ejecutar programas mayores que la RAM llevando a disco las partes inactivas.

- **Paginación**: el espacio virtual se divide en **páginas** de tamaño fijo (típicamente **4 KiB**) que se cargan en marcos físicos; la tabla de páginas traduce direcciones y la **TLB** cachea las traducciones recientes.
- **Fallo de página y reemplazo**: si la página no está en memoria se produce un fallo y hay que traerla de disco, expulsando otra según un algoritmo de reemplazo: **LRU** (la menos recientemente usada, el referente práctico), FIFO, reloj u óptimo (teórico).
- **Segmentación y swapping**: la segmentación divide el espacio en unidades lógicas de tamaño variable (hoy residual frente a la paginación); el **swapping** intercambia procesos o páginas completas con el área de intercambio.
- **Hiperpaginación** (*thrashing*): degradación severa cuando el sistema pasa más tiempo paginando que ejecutando; se combate con más RAM o menos carga (concepto de **conjunto de trabajo**).

## Sistemas de ficheros y entrada/salida

El sistema de ficheros organiza el almacenamiento persistente en ficheros y directorios con metadatos, permisos y control de integridad.

- **Estructuras**: los sistemas UNIX usan **i-nodos** (metadatos + punteros a bloques) y directorios que asocian nombres a i-nodos; FAT usa una tabla de asignación enlazada; NTFS, la **MFT** (*master file table*).
- **Journaling**: registro de transacciones que evita la corrupción ante caídas, presente en todos los sistemas de ficheros modernos.

| Sistema de ficheros | Ámbito | Rasgos |
| --- | --- | --- |
| **NTFS** | Windows | Journaling, ACL, cifrado EFS, compresión |
| **ext4** | Linux (por defecto en Debian/Ubuntu) | Journaling, extents |
| **XFS** | Linux (por defecto en RHEL) | Alto rendimiento en ficheros grandes |
| **Btrfs / ZFS** | Linux/BSD | Copy-on-write, instantáneas, sumas de verificación, RAID integrado |
| **APFS** | macOS/iOS | Copy-on-write, instantáneas, cifrado nativo |
| **FAT32 / exFAT** | Intercambio y soportes extraíbles | Sin permisos ni journaling; máxima compatibilidad |

- **Entrada/salida**: el SO media entre dispositivos y procesos con **controladores** (*drivers*), *buffering* y caché de disco, **DMA** (transferencia directa a memoria sin ocupar la CPU) e interrupciones; en discos rotacionales añade planificación de brazo (SCAN/elevador), irrelevante en SSD.

## Evolución y panorama actual

De los sistemas **por lotes** (años 50-60) se pasó a la **multiprogramación** y el **tiempo compartido** (UNIX, 1969), al PC (MS-DOS 1981, Windows, Mac), y de ahí a los SO de red, los móviles (iPhone 2007, Android 2008) y la era actual de nube y virtualización (temas 44 y 51), donde el SO de servidor corre mayoritariamente virtualizado o en contenedores.

| Familia | Ejemplos | Ámbito típico |
| --- | --- | --- |
| Windows | Windows 11, **Windows Server 2025** | Puesto de trabajo y servidores corporativos |
| UNIX/Linux | RHEL, Ubuntu, SUSE, Debian; AIX, Solaris | Servidores, nube, supercomputación (el **100 % del TOP500**) |
| macOS | macOS (núcleo XNU híbrido, base Darwin/BSD) | Puesto de trabajo |
| Móviles | **Android** (núcleo Linux) e **iOS** (base Darwin) | Dispositivos móviles (Android, el SO más extendido del mundo) |
| Mainframe | **z/OS** (IBM Z) | Grandes volúmenes transaccionales (banca, seguros) |

- **Sistemas operativos móviles**: modelo de seguridad de **aislamiento por aplicación** (*sandbox*), permisos declarados y concedidos por el usuario, distribución por tiendas firmadas y actualizaciones OTA; el desarrollo de aplicaciones se trata en el tema 59.
- **El mainframe y z/OS**: alta disponibilidad y particiones lógicas (**LPAR**) con virtualización nativa (z/VM); procesamiento transaccional (CICS) y por lotes (JCL); sigue sosteniendo cargas críticas de banca y administraciones.
- **Tendencias**: contenedores como unidad de despliegue (tema 44), SO inmutables y mínimos para nube (CoreOS, Bottlerocket), **WSL** (subsistema Linux en Windows) y el uso creciente de Linux en el escritorio de la Administración europea.

## Fuentes {.unnumbered .unlisted}

- Tanenbaum, A. S. y Bos, H., *Modern Operating Systems*, 5.ª ed., Pearson, 2022.
- Silberschatz, A., Galvin, P. B. y Gagne, G., *Operating System Concepts*, 10.ª ed., Wiley, 2018.
- Documentación oficial de Microsoft Learn (Windows Server 2025), kernel.org e IBM (z/OS), consultadas en julio de 2026.
