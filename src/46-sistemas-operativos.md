# Sistemas operativos

El sistema operativo es la capa de software que gestiona el hardware y ofrece a las aplicaciones una máquina extendida más simple y segura que el hardware desnudo. Este tema cubre sus conceptos y mecanismos fundamentales (procesos, memoria, ficheros y E/S) y el panorama actual de familias, desde el puesto de trabajo hasta el mainframe. La administración práctica de GNU/Linux y de Windows se desarrolla en los temas [47](47-administracion-de-sistemas-gnu-linux.md) y [48](48-administracion-de-sistemas-windows-y-directorio-activo.md).

## Concepto, funciones y estructura

Un sistema operativo cumple dos papeles complementarios: **gestor de recursos** (reparte CPU, memoria y dispositivos entre procesos que compiten) y **máquina extendida** (abstrae el hardware en conceptos manejables: proceso, fichero, socket). Las aplicaciones le piden servicios mediante **llamadas al sistema** (*system calls*).

- **Componentes de la distribución del sistema**: el **núcleo** (proporciona la funcionalidad para ejecutar procesos y el acceso protegido al hardware), las **bibliotecas del sistema** (conjunto estándar de funciones con el que las aplicaciones interactúan con el núcleo, como libc) y las **utilidades del sistema** (programas especializados de gestión: shell, editores, herramientas de administración).
- **Modos de ejecución**: el núcleo (*kernel*) corre en **modo privilegiado** (acceso total al hardware) y las aplicaciones en **modo usuario**; la frontera se cruza de forma controlada mediante llamadas al sistema (instrucción de *trap*) e **interrupciones**: de dispositivo (asíncronas), de reloj (base del tiempo compartido) y excepciones (errores del propio programa, como la división por cero o el fallo de página).
- **Llamadas al sistema**: la interfaz de servicios del núcleo. **POSIX** (*Portable Operating System Interface*) estandariza esa interfaz y el entorno (incluido el intérprete de comandos o *shell*) para dar portabilidad entre sistemas UNIX; en Windows la expone la API Win32. Las bibliotecas estándar las envuelven para el programador. Equivalencias clásicas:

| Función | POSIX | Win32 |
| --- | --- | --- |
| Crear proceso | `fork` + `exec` | `CreateProcess` |
| Abrir fichero | `open` | `CreateFile` |
| Leer/escribir | `read`/`write` | `ReadFile`/`WriteFile` |
| Terminar proceso | `kill` (señal) | `TerminateProcess` |
| Esperar a un hijo | `waitpid` | `WaitForSingleObject` |

- **Arquitectura del núcleo**: **monolítica** (todo el SO en modo núcleo, con módulos cargables: Linux), **por capas** (jerarquía de niveles, histórica: THE), **microkernel** (servicios mínimos en el núcleo y el resto como procesos servidores que se comunican por paso de mensajes: MINIX, QNX) e **híbrida** (Windows, macOS). Variantes de investigación y nube: exokernel y **unikernel** (aplicación y SO mínimo enlazados en una sola imagen).
- **Componentes clásicos**: gestión de procesos, gestión de memoria, sistema de ficheros, gestión de E/S, red y seguridad (autenticación, control de acceso, auditoría).
- **Mecanismos de protección**: además del control de acceso a ficheros, el SO moderno endurece la ejecución con **ASLR** (aleatorización del espacio de direcciones), **DEP/NX** (páginas de datos no ejecutables), **arranque seguro** (solo se carga código firmado) y *sandboxing* de aplicaciones; dificultan la explotación de vulnerabilidades (tema [32](32-desarrollo-seguro-de-aplicaciones.md)).
- **Arranque**: el firmware (**UEFI**, antes BIOS) carga el gestor de arranque, este carga el núcleo y el núcleo lanza el primer proceso de usuario (`init`/`systemd` en Linux), que inicia el resto de servicios (detalle práctico en el tema [47](47-administracion-de-sistemas-gnu-linux.md)).

## Procesos, hilos y planificación

El **proceso** es un programa en ejecución con su espacio de direcciones propio; su información de control vive en el **PCB** (*process control block*): estado, contador de programa, registros, memoria, ficheros abiertos. El **hilo** es la unidad de ejecución dentro de un proceso: los hilos de un mismo proceso comparten memoria y recursos, lo que abarata la comunicación y el cambio de contexto.

- **Identidad y contexto del proceso**: la **identidad** la forman el **PID**, las credenciales (UID/GID que determinan sus permisos) y, en Linux, los espacios de nombres; del padre hereda el **vector de argumentos** (línea de comandos) y el **vector de entorno** (parejas nombre=valor). Su **contexto** en un instante dado incluye el contexto de planificación (registros, prioridad), la contabilidad de recursos, la **tabla de ficheros abiertos**, el contexto del sistema de ficheros (directorio actual, raíz), la tabla de tratamiento de señales y el contexto de memoria virtual.
- **Estados básicos**: **listo, en ejecución y bloqueado** (más nuevo y terminado; algunos modelos añaden los estados suspendidos, con el proceso expulsado a disco). El **cambio de contexto** guarda y restaura el estado del procesador al alternar procesos; es tiempo perdido puro, por lo que interesa minimizarlo.
- **Modelos de hilos**: hilos de usuario gestionados por biblioteca frente a hilos de núcleo planificados por el SO. Correspondencias **1:1** (cada hilo de usuario sobre un hilo de núcleo: Linux y Windows), **N:1** (todos sobre uno, hoy residual) y **M:N** (híbrida).
- **Criterios de planificación**: maximizar el uso de CPU y la productividad (*throughput*); minimizar el **tiempo de retorno** (desde que llega hasta que termina), el **tiempo de espera** (suma de estancias en la cola de listos) y el **tiempo de respuesta** (hasta la primera reacción, clave en interactivos).
- **Algoritmos**: **FCFS** (por orden de llegada, penaliza a los cortos: efecto convoy), **SJF** (el trabajo más corto primero, óptimo en tiempo medio de espera; su versión apropiativa es **SRTF**), **Round Robin** (turnos con *quantum* de tiempo, el clásico de tiempo compartido), por **prioridades** (con **envejecimiento** para evitar la inanición de los de baja prioridad) y **colas multinivel** (una cola por clase de proceso; en las realimentadas el proceso cambia de cola según su comportamiento). Se distingue la planificación **apropiativa** (el SO puede expulsar al proceso en ejecución) de la **no apropiativa**.
- **Caso real (Linux)**: planificador **apropiativo por prioridades** con dos rangos: clases de **tiempo real** (prioridades 0-99, absolutas: FIFO o Round Robin) y la clase normal de **tiempo compartido**, gobernada por el valor **nice** (-20 a +19) sobre una cola de ejecución (*runqueue*) por CPU. La clase normal usó desde 2007 el **CFS** (*Completely Fair Scheduler*, reparto equitativo del tiempo de CPU), sustituido por **EEVDF** desde el núcleo 6.6 (2023). Linux además no distingue internamente proceso e hilo: todo son **tareas** creadas con `clone`, que comparten más o menos recursos. Windows planifica por prioridades con 32 niveles.
- **Comunicación entre procesos (IPC)**: **tuberías** (*pipes*, flujo unidireccional entre procesos emparentados; con nombre para procesos independientes), **colas de mensajes**, **memoria compartida** (la más rápida: sin copias a través del núcleo, pero exige sincronización), **señales** (notificación asíncrona de eventos: `SIGTERM`, `SIGKILL`) y **sockets** (comunicación local o por red, base del modelo cliente-servidor).
- **Concurrencia**: el acceso a datos compartidos exige **exclusión mutua** en las secciones críticas, con primitivas como los **semáforos** (Dijkstra), los mutex y los monitores. Problemas clásicos de sincronización: productor-consumidor, lectores-escritores y los filósofos comensales.
- **Interbloqueo** (*deadlock*): situación en la que varios procesos se esperan circularmente. Requiere las **cuatro condiciones de Coffman** (exclusión mutua, retención y espera, no expropiación y espera circular); se trata con prevención (negar alguna condición), evitación (**algoritmo del banquero**), detección y recuperación, o ignorándolo (la opción práctica habitual).

## Gestión de memoria

La **memoria virtual** da a cada proceso un espacio de direcciones propio y protegido, traducido a memoria física por la **MMU**; permite ejecutar programas mayores que la RAM llevando a disco las partes inactivas y cargando las páginas solo cuando se usan (**paginación por demanda**).

- **Asignación contigua y fragmentación**: los esquemas históricos de particiones sufren **fragmentación externa** (huecos libres no contiguos, se palía con compactación); la paginación la elimina a costa de **fragmentación interna** (espacio desaprovechado dentro de la última página).
- **Paginación**: el espacio virtual se divide en **páginas** de tamaño fijo (típicamente **4 KiB**) que se cargan en marcos físicos; la tabla de páginas traduce direcciones y añade bits de protección (lectura/escritura/ejecución). En 64 bits la tabla es **multinivel** (4 o 5 niveles en x86-64) y existen **páginas grandes** (*huge pages*, 2 MiB/1 GiB) para reducir fallos de TLB.
- **TLB**: caché de traducciones recientes en la MMU; sin ella cada acceso a memoria exigiría recorrer la tabla de páginas.
- **Fallo de página y reemplazo**: si la página no está en memoria se produce un fallo y hay que traerla de disco, expulsando otra según un algoritmo de reemplazo: **LRU** (la menos recientemente usada, el referente práctico, aproximado con bits de referencia), FIFO, **segunda oportunidad/reloj** u óptimo (teórico, para comparar). FIFO sufre la **anomalía de Belady** (más marcos pueden dar más fallos); Linux usa en la práctica una variante del algoritmo del reloj. El reemplazo puede ser **global** (cualquier página del sistema) o **local** (solo entre las del propio proceso).
- **Zonas de memoria física (Linux)**: el gestor divide la RAM en zonas por sus limitaciones hardware: **ZONE_DMA** (accesible por dispositivos antiguos), **ZONE_NORMAL** y, en 32 bits, ZONE_HIGHMEM (hoy residual); reparte páginas, grupos de páginas y bloques pequeños (*slab allocator*).
- **Copy-on-write**: tras un `fork`, padre e hijo comparten las páginas marcadas de solo lectura y únicamente se copia la página que uno de los dos modifica; abarata la creación de procesos.
- **Segmentación y swapping**: la segmentación divide el espacio en unidades lógicas de tamaño variable (hoy residual frente a la paginación); el **swapping** intercambia procesos o páginas completas con el área de intercambio (*swap*).
- **Hiperpaginación** (*thrashing*): degradación severa cuando el sistema pasa más tiempo paginando que ejecutando; se combate con más RAM o menos carga. El **conjunto de trabajo** (*working set*) es el conjunto de páginas que un proceso necesita tener residentes para no hiperpaginar.

## Sistemas de ficheros y entrada/salida

El sistema de ficheros organiza el almacenamiento persistente en ficheros y directorios con metadatos, permisos y control de integridad.

- **Estructuras**: los sistemas UNIX usan **i-nodos** (metadatos + punteros a bloques) y directorios que asocian nombres a i-nodos (un directorio es un fichero especial); FAT usa una tabla de asignación enlazada; NTFS, la **MFT** (*master file table*). El **superbloque** guarda los metadatos del propio sistema de ficheros (tipo, tamaño, estado) y da acceso a los i-nodos.
- **Tipos de fichero UNIX** (primera letra de `ls -l`): normal (`-`), directorio (`d`), enlace simbólico (`l`), dispositivo de **bloques** (`b`, discos) y de **caracteres** (`c`, terminales), tubería con nombre (`p`) y socket (`s`); «todo es un fichero», incluidos dispositivos y conexiones.
- **Asignación de bloques**: **contigua** (rápida pero con fragmentación externa), **enlazada** (cada bloque apunta al siguiente; FAT centraliza los enlaces en la tabla) e **indexada** (un bloque o i-nodo reúne los punteros; los i-nodos combinan punteros directos e indirectos simples, dobles y triples para cubrir ficheros grandes).
- **Enlaces**: el **enlace duro** es otro nombre para el mismo i-nodo (solo dentro del mismo sistema de ficheros); el **enlace simbólico** es un fichero que contiene una ruta (puede cruzar sistemas de ficheros y quedar roto).
- **VFS y montaje**: el **sistema de ficheros virtual** ofrece a las aplicaciones una interfaz única (abrir, leer, escribir, mapear) sobre sistemas de ficheros distintos (locales, de red, virtuales). En UNIX todo se **monta** en un único árbol de directorios; Windows usa letras de unidad (y puntos de montaje NTFS). Sus cuatro objetos:

| Objeto VFS | Representa |
| --- | --- |
| **Superbloque** | El sistema de ficheros completo (tipo, tamaño, estado) |
| **I-nodo** | Un fichero individual: sus metadatos y punteros a bloques |
| **Fichero** (*file*) | Un fichero abierto: la posición de lectura/escritura del proceso |
| **Entrada de directorio** (*dentry*) | La asociación entre un nombre y su i-nodo |

- **Integridad**: el **journaling** (registro de transacciones que se aplica o descarta tras una caída) protege ext4, XFS y NTFS; los sistemas **copy-on-write** (Btrfs, ZFS, APFS) logran el mismo efecto sin diario clásico, no sobrescribiendo nunca los bloques en uso, y añaden instantáneas y sumas de verificación.

| Sistema de ficheros | Ámbito | Rasgos |
| --- | --- | --- |
| **NTFS** | Windows | Journaling, ACL, cifrado EFS, compresión |
| **ext4** | Linux (por defecto en Debian/Ubuntu) | Journaling, extents |
| **XFS** | Linux (por defecto en RHEL) | Alto rendimiento en ficheros grandes |
| **Btrfs / ZFS** | Linux/BSD | Copy-on-write, instantáneas, sumas de verificación, RAID integrado |
| **APFS** | macOS/iOS | Copy-on-write, instantáneas, cifrado nativo |
| **FAT32 / exFAT** | Intercambio y soportes extraíbles | Sin permisos ni journaling; máxima compatibilidad |

- **Entrada/salida**: el SO media entre dispositivos y procesos con **controladores** (*drivers*) que uniforman el acceso al hardware. Técnicas, de menor a mayor eficiencia: **E/S programada** (la CPU consulta en bucle: *polling*), **por interrupciones** (el dispositivo avisa al terminar) y **DMA** (el controlador transfiere bloques directamente a memoria sin ocupar la CPU, que solo recibe la interrupción final).
- **Optimización**: la **caché de páginas** unificada guarda en la RAM libre los bloques leídos y escritos (lecturas adelantadas, escrituras diferidas), **spooling** (colas para dispositivos no compartibles, como la impresora) y, en discos rotacionales, planificación de brazo (SCAN/elevador).
- **SSD**: sin partes móviles, la planificación de brazo pierde sentido (planificadores none/mq-deadline); el SO añade **TRIM** (avisar de bloques liberados) y el firmware nivela el desgaste de las celdas (*wear leveling*); el borrado se hace por bloques grandes, lo que penaliza la escritura pequeña aleatoria.

## Evolución y panorama actual

De los sistemas **por lotes** (años 50-60) se pasó a la **multiprogramación** y el **tiempo compartido** (UNIX, 1969), al PC (MS-DOS 1981, Windows, Mac), y de ahí a los SO de red, los móviles (iPhone 2007, Android 2008) y la era actual de nube y virtualización (temas [44](44-virtualizacion-y-contenedores.md) y [51](51-computacion-en-la-nube-y-altas-prestaciones.md)), donde el SO de servidor corre mayoritariamente virtualizado o en contenedores.

| Familia | Ejemplos | Ámbito típico |
| --- | --- | --- |
| Windows | Windows 11, **Windows Server 2025** | Puesto de trabajo y servidores corporativos |
| UNIX/Linux | RHEL, Ubuntu, SUSE, Debian; AIX, Solaris | Servidores, nube, supercomputación (el **100 % del TOP500**) |
| macOS | macOS (núcleo XNU híbrido, base Darwin/BSD) | Puesto de trabajo |
| Móviles | **Android** (núcleo Linux) e **iOS** (base Darwin) | Dispositivos móviles (Android, el SO más extendido del mundo) |
| Mainframe | **z/OS** (IBM Z) | Grandes volúmenes transaccionales (banca, seguros) |

- **macOS**: núcleo **XNU** (híbrido: microkernel Mach + BSD) sobre la base Darwin; protección del sistema con **SIP** (*System Integrity Protection*) y **Gatekeeper** (solo aplicaciones firmadas/notarizadas); en empresa se administra por **MDM** (tema [52](52-puesto-de-trabajo-tic.md)) y puede unirse a Directorio Activo o federarse con Entra ID (Platform SSO).
- **Sistemas operativos móviles**: modelo de seguridad de **aislamiento por aplicación** (*sandbox*), permisos declarados y concedidos por el usuario, distribución por tiendas firmadas y actualizaciones OTA; el desarrollo de aplicaciones se trata en el tema [59](59-desarrollo-de-aplicaciones-moviles.md).
    - **Android**: núcleo Linux con capas propias (runtime **ART**, servicios del sistema, SELinux en modo estricto); actualizaciones del sistema por **particiones A/B** (se instala en la copia inactiva y se conmuta al reiniciar).
    - **iOS**: base Darwin compartida con macOS; cadena de arranque firmada y claves protegidas por el coprocesador **Secure Enclave**.
- **Software libre**: GNU/Linux se distribuye bajo la licencia **GPL** (libertades de uso, estudio, modificación y redistribución); licencias y protección jurídica del software en el tema [50](50-proteccion-juridica-del-software-y-licencias.md).
- **El mainframe y z/OS**: alta disponibilidad y particiones lógicas (**LPAR**) con virtualización nativa (z/VM); procesamiento transaccional (CICS) y por lotes (JCL); sigue sosteniendo cargas críticas de banca y administraciones. Versión vigente: **z/OS 3.2** (disponible desde el **30-sep-2025**, diseñada para el mainframe IBM z17 y la inferencia de IA integrada).
- **Tendencias**: contenedores como unidad de despliegue (tema [44](44-virtualizacion-y-contenedores.md)), SO inmutables y mínimos para nube (CoreOS, Bottlerocket), **WSL** (subsistema Linux en Windows) y el uso creciente de Linux en el escritorio de la Administración europea.

## Supuesto práctico: planificación de procesos

Cuatro procesos llegan a la cola de listos con estas ráfagas de CPU (tiempos en unidades):

| Proceso | Llegada | Ráfaga |
| --- | --- | --- |
| P1 | 0 | 6 |
| P2 | 1 | 4 |
| P3 | 2 | 2 |
| P4 | 3 | 4 |

Se pide el orden de ejecución y los tiempos medios de espera y retorno con FCFS, SJF no apropiativo y Round Robin con *quantum* 2. Recordatorio: **retorno = fin - llegada**; **espera = retorno - ráfaga**.

- **FCFS**: orden de llegada: P1 (0-6), P2 (6-10), P3 (10-12), P4 (12-16). Esperas: 0, 5, 8, 9 → **media 5,5**. Retornos: 6, 9, 10, 13 → **media 9,5**.
- **SJF no apropiativo**: en t=0 solo está P1 (0-6); al acabar esperan P2 (4), P3 (2) y P4 (4): entra la más corta, P3 (6-8), y luego P2 (8-12) y P4 (12-16) (empate a 4, desempata el orden de llegada). Esperas: 0, 7, 4, 9 → **media 5,0**. Retornos: 6, 11, 6, 13 → **media 9,0**.
- **Round Robin (q=2)**: turnos P1 (0-2), P2 (2-4), P3 (4-6, termina), P1 (6-8), P4 (8-10), P2 (10-12, termina), P1 (12-14, termina), P4 (14-16, termina). Esperas: 8, 7, 2, 9 → **media 6,5**. Retornos: 14, 11, 4, 13 → **media 10,5**.

Conclusión de examen: **SJF minimiza el tiempo medio de espera** (es óptimo en ese criterio), FCFS penaliza a los procesos cortos que llegan tras uno largo (efecto convoy) y Round Robin empeora los tiempos medios a cambio de un **tiempo de respuesta** corto y equitativo (ningún proceso espera más de un ciclo de turnos), que es lo que importa en sistemas interactivos.

## Fuentes {.unnumbered .unlisted}

- Tanenbaum, A. S. y Bos, H., *Modern Operating Systems*, 5.ª ed., Pearson, 2022.
- Silberschatz, A., Galvin, P. B. y Gagne, G., *Operating System Concepts*, 10.ª ed., Wiley, 2018.
- Documentación oficial de Microsoft Learn (Windows Server 2025), kernel.org e IBM (z/OS 3.2, sep-2025), consultadas en julio de 2026.
