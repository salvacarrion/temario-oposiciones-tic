# Sistemas de almacenamiento

## Arquitecturas DAS, NAS y SAN

Las arquitecturas de almacenamiento se clasifican según cómo se conecta el almacenamiento a los servidores que lo usan. Antes de compararlas conviene distinguir los tres paradigmas de acceso al dato, porque cada arquitectura sirve uno:

- **Acceso a nivel de bloque**: el servidor ve discos «en crudo» (volúmenes de bloques) sobre los que crea su propio sistema de ficheros. Es el acceso de **DAS y SAN**; el que exigen bases de datos e hipervisores.
- **Acceso a nivel de fichero**: el servidor accede a un sistema de ficheros remoto ya montado y compartido. Es el acceso del **NAS**.
- **Acceso a nivel de objeto**: los datos se guardan como objetos con metadatos en un espacio plano, accesibles por API HTTP (el modelo de **Amazon S3**, hoy estándar de facto). Escala masivamente y es el paradigma típico de la nube, el archivado y las copias de seguridad.

### DAS (Direct Attached Storage)

Almacenamiento conectado directamente al servidor, sin red intermedia: los discos internos o una cabina unida por cable directo.

- **Acceso**: a nivel de **bloque**, local y con la latencia más baja.
- **Interfaces**: **SATA**, **SAS** (*Serial Attached SCSI*, la interfaz de servidor habitual) y **NVMe** (*Non-Volatile Memory Express*, para SSD sobre el bus PCIe, sin la sobrecarga del protocolo SCSI); externas: USB, Thunderbolt.
- **Ventajas**: económico, simple, sin dependencia de red.
- **Inconvenientes**: la capacidad queda aislada en cada servidor (no se comparte ni se reasigna el espacio libre) y la escalabilidad y la gestión centralizada son limitadas.

### NAS (Network Attached Storage)

Dispositivo que sirve almacenamiento a nivel de **fichero** a través de la red local TCP/IP: los clientes montan carpetas compartidas.

- **Protocolos**: **NFS** (*Network File System*, mundo Unix/Linux) y **SMB** (*Server Message Block*, mundo Windows, hoy en la versión **3.x** con cifrado; **CIFS** es la denominación del dialecto antiguo SMB 1.0, retirado por inseguro). **Samba** es la implementación libre de SMB para sistemas Unix/Linux.
- **Ventajas**: compartición nativa entre muchos clientes, coste moderado, administración sencilla (permisos, cuotas, snapshots).
- **Inconvenientes**: rendimiento y latencia inferiores a una SAN y dependencia de la LAN; no sirve para cargas que exigen bloque (bases de datos exigentes).

### SAN (Storage Area Network)

Red **dedicada** de almacenamiento, separada de la LAN, que conecta los servidores con las cabinas de discos a nivel de **bloque**: cada servidor ve sus volúmenes (LUN) como si fueran discos locales.

- **Elementos**: cabinas de almacenamiento (*arrays*), conmutadores y directores de la red de almacenamiento, y adaptadores **HBA** (*Host Bus Adapter*) en los servidores. El acceso se controla con *zoning* (en el conmutador) y *LUN masking* (en la cabina).
- **Protocolos**:
    - **Fibre Channel (FC)**: la tecnología clásica de SAN, con generaciones que duplican velocidad: 16 y 32 Gbit/s desplegadas de forma masiva, **64GFC** (Gen 7) y **128GFC** (Gen 8, con productos desde finales de 2025).
    - **iSCSI**: encapsula SCSI sobre TCP/IP y permite montar una SAN sobre Ethernet estándar, con menor coste.
    - **FCoE** (*FC over Ethernet*): FC sobre Ethernet convergente; uso en retroceso.
    - **NVMe-oF** (*NVMe over Fabrics*): extiende NVMe a la red (sobre FC, RDMA o TCP); es la evolución actual para cabinas todo-flash.
- **Ventajas**: máximo rendimiento y disponibilidad, escalabilidad casi ilimitada, consolidación del almacenamiento de muchos servidores y funciones avanzadas (replicación entre cabinas, snapshots).
- **Inconvenientes**: coste de implantación y complejidad de administración elevados.

### Comparativa

| Aspecto | DAS | NAS | SAN |
| --- | --- | --- | --- |
| Nivel de acceso | Bloque | Fichero | Bloque |
| Conexión | Directa (SATA/SAS/NVMe) | LAN TCP/IP | Red dedicada (FC, iSCSI, NVMe-oF) |
| Compartición | No (capacidad cautiva del servidor) | Sí, multicliente | Sí, LUN asignadas por servidor |
| Rendimiento | Alto (local) | Medio | Muy alto |
| Coste y complejidad | Bajos | Medios | Altos |
| Uso típico | Servidor suelto, arranque | Ficheros compartidos, documentación | Bases de datos, virtualización, cargas críticas |

### Virtualización del almacenamiento y volúmenes lógicos

La virtualización del almacenamiento separa la vista lógica del espacio (lo que ven servidores y aplicaciones) de los discos físicos que lo soportan, para ganar flexibilidad de gestión.

- **Volúmenes físicos**: las unidades reales (HDD, SSD) o las LUN que presenta una cabina.
- **Volúmenes lógicos**: abstracciones creadas sobre los físicos, redimensionables y movibles sin tocar el hardware.
- **LVM** (*Logical Volume Manager*, el gestor clásico en Linux): los volúmenes físicos (PV) se agrupan en un grupo de volúmenes (VG), del que se tallan volúmenes lógicos (LV) donde se crean los sistemas de ficheros; permite redimensionar en caliente y hacer snapshots.
- **Funciones asociadas**: *thin provisioning* (el espacio se consume según se escribe), *tiering* (datos calientes en SSD, fríos en HDD) y cabinas unificadas que sirven bloque y fichero a la vez.

![Estructura de LVM: los volúmenes físicos forman un grupo de volúmenes del que se crean los volúmenes lógicos](media/image66.png){width=70%}

## RAID

RAID (*Redundant Array of Independent Disks*) combina varios discos en una sola unidad lógica para ganar tolerancia a fallos, rendimiento o capacidad, según el nivel elegido. Protege la **disponibilidad** frente al fallo físico de discos.

- **Soporte hardware**: controladora dedicada con caché propia (protegida por batería o *flash*); descarga a la CPU y es lo habitual en servidores y cabinas.
- **Soporte software**: lo gestiona el sistema operativo (mdadm en Linux, Storage Spaces en Windows) o el sistema de ficheros (**ZFS**, Btrfs); hoy es plenamente competitivo en rendimiento y más flexible, a costa de consumir CPU del host.

### Niveles RAID estándar

- **RAID 0 (striping, volumen dividido)**: reparte los datos entre dos o más discos sin redundancia alguna.
    - Suma capacidades y rendimientos (lecturas y escrituras en paralelo).
    - **Sin tolerancia a fallos**: si falla un disco se pierde todo el conjunto; solo apto para datos prescindibles o temporales.
- **RAID 1 (mirroring, espejo)**: duplica los mismos datos en dos (o más) discos.
    - Tolera el fallo de todos los discos menos uno; lectura más rápida (se lee de cualquiera) y escritura ligeramente penalizada (se escribe en todos).
    - **Capacidad útil: el 50 %** (limitada además al disco más pequeño).
- **RAID 5 (striping con paridad distribuida)**: reparte datos y paridad entre todos los discos.
    - Mínimo **3 discos**; capacidad útil **N−1**; tolera el fallo de **1 disco**.
    - Equilibrio clásico entre capacidad, rendimiento y protección; las escrituras pagan la **penalización de paridad** (cada escritura implica leer y reescribir dato y paridad).
    - Con discos actuales de gran capacidad, la **reconstrucción** tras un fallo dura horas o días, y un segundo fallo durante ella pierde el conjunto: por eso en producción se prefiere RAID 6.
- **RAID 6 (doble paridad)**: como RAID 5 pero con dos bloques de paridad.
    - Mínimo **4 discos**; capacidad útil **N−2**; tolera **2 fallos** simultáneos.
    - Es el estándar actual para volúmenes de gran capacidad.
- **Niveles en desuso**: RAID 2 y 3 no se emplean en la práctica; **RAID 4** usa un disco de paridad dedicado que se convierte en cuello de botella de escritura.

![Esquema de RAID 4: los datos se reparten en bandas y la paridad (Ap, Bp, Cp, Dp) se concentra en un disco dedicado](media/image370.png){width=60%}

### Niveles RAID anidados

Los niveles pueden combinarse aplicando uno sobre conjuntos del otro.

- **RAID 0+1 (espejo de divisiones)**: se crean dos conjuntos RAID 0 y se espejan entre sí. Alto rendimiento, pero un fallo degrada un lado entero del espejo.
- **RAID 1+0 o RAID 10 (división de espejos)**: primero se crean espejos y sobre ellos se hace striping. Tolera varios fallos simultáneos mientras no caigan los dos discos de un mismo espejo; es la opción preferida frente a 0+1 y la habitual para bases de datos (mínimo **4 discos**, capacidad útil 50 %).
- **Otros**: RAID 50 (striping de conjuntos RAID 5), RAID 60, RAID 100, para grandes volúmenes con requisitos mixtos.

![Esquema de RAID 0+1: dos conjuntos en striping espejados entre sí](media/image140.png){width=60%}

### Resumen y advertencias

| Nivel | Mín. discos | Capacidad útil | Fallos tolerados | Uso típico |
| --- | --- | --- | --- | --- |
| RAID 0 | 2 | 100 % | Ninguno | Rendimiento puro, datos prescindibles |
| RAID 1 | 2 | 50 % | N−1 | Discos de sistema |
| RAID 5 | 3 | N−1 | 1 | Uso general, lectura intensiva |
| RAID 6 | 4 | N−2 | 2 | Volúmenes grandes |
| RAID 10 | 4 | 50 % | 1 por espejo | Bases de datos, E/S intensiva |

- **Hot spare**: disco de reserva en línea que entra automáticamente en el conjunto cuando falla uno, iniciando la reconstrucción sin intervención.
- **RAID no es copia de seguridad**: protege frente al fallo físico de un disco, pero no frente a borrados accidentales, corrupción lógica, ransomware o desastres que afecten a todo el sistema. Para eso están las copias de seguridad.

## Respaldo y recuperación: políticas de copias de seguridad

La copia de seguridad (*backup*) es la última línea de defensa de la información: permite recuperar los datos perdidos por error humano, fallo hardware, corrupción o ataque. Una política de respaldo define qué se copia, con qué frecuencia, dónde se guarda, cuánto se retiene y cómo se comprueba.

- **Objetivos de recuperación** (fijan el diseño de la política):
    - **RPO** (*Recovery Point Objective*): pérdida máxima de datos admisible, medida en tiempo (cuánto trabajo se puede perder desde la última copia).
    - **RTO** (*Recovery Time Objective*): tiempo máximo admisible hasta restaurar el servicio.

### Tipos de copia

- **Completa (full)**: copia todos los datos cada vez. Restauración más rápida y simple; máximo consumo de espacio y ventana de copia.
- **Incremental**: copia solo lo cambiado desde la **última copia de cualquier tipo**. Mínimo espacio y ventana; restaurar exige la completa más toda la cadena de incrementales.
- **Diferencial**: copia lo cambiado desde la **última completa**. Restaurar solo exige la completa más la última diferencial; ocupa más que la incremental y crece con los días.

| Tipo | Espacio y ventana de copia | Restauración |
| --- | --- | --- |
| Completa | Máximos | La más rápida (una sola copia) |
| Incremental | Mínimos | La más lenta (completa + cadena entera) |
| Diferencial | Intermedios (crece hasta la siguiente completa) | Rápida (completa + última diferencial) |

- **Esquema habitual**: completa periódica (por ejemplo, semanal) combinada con incrementales o diferenciales diarias. Las herramientas modernas añaden la **completa sintética** (se construye a partir de la última completa y sus incrementales, sin releer el origen).

### Políticas y buenas prácticas

- **Regla 3-2-1**: al menos **3** copias de los datos, en **2** soportes distintos, con **1** fuera de las instalaciones (*offsite*).
    - Ampliación **3-2-1-1-0** frente al ransomware: además **1** copia *offline* o **inmutable** (aislada por *air gap* o bloqueada contra escritura) y **0** errores en las pruebas de restauración.
- **Rotación y retención**: el esquema clásico es **GFS** (*Grandfather-Father-Son*, abuelo-padre-hijo): copias diarias (hijo), semanales (padre) y mensuales o anuales (abuelo), cada una con su plazo de retención.
- **Medios de respaldo**:
    - **Cinta LTO**: el medio de archivado por excelencia: bajo coste por TB, larga vida y *air gap* natural (la cinta extraída está fuera de línea). Generaciones vigentes: **LTO-9** (18 TB nativos) y **LTO-10** (2025, cartuchos de **30 y 40 TB** nativos).
    - **Disco o cabina dedicada**: rapidez de copia y restauración; los appliances aplican **deduplicación** para multiplicar la capacidad efectiva.
    - **Nube**: almacenamiento de objetos como destino externo, con opciones de inmutabilidad (bloqueo de objetos) y clases frías para archivado.
- **Snapshots y replicación no son backup**: el snapshot vive en la misma cabina que protege, y la replicación copia también los borrados y el cifrado malicioso al destino. Son complementos que reducen el RPO, no sustitutos de la copia de seguridad.
- **Verificación**: las copias se prueban restaurando de forma periódica (la copia que no se ha probado a restaurar no puede darse por buena) y se supervisan los trabajos fallidos.

### Las copias de seguridad en el ENS

El **RD 311/2022** (ENS, tema 29) exige las copias de seguridad como medida de protección de la información, **mp.info.6** (Anexo II), sobre la dimensión de **disponibilidad**:

- Se realizarán copias que permitan **recuperar datos perdidos, accidental o intencionadamente**; periodicidad y plazos de retención según la normativa interna de la organización.
- Los procedimientos de respaldo indicarán: la **frecuencia** de las copias, los requisitos de almacenamiento **en el propio lugar** y **en otros lugares**, y los **controles de acceso autorizado** a las copias.
- Refuerzos por nivel: **R1, pruebas de recuperación** periódicas (exigido desde nivel MEDIO) y **R2, protección de las copias**: al menos una copia separada en lugar diferente, de modo que un incidente no afecte a la vez al original y a la copia (nivel ALTO).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, Esquema Nacional de Seguridad, texto consolidado, última modificación 6 de noviembre de 2024 (Anexo II, medida mp.info.6).
- LTO Program (lto.org): especificación LTO-10 (agosto de 2025), consulta de julio de 2026.
- Fibre Channel Industry Association (fibrechannel.org): FC-PI-8 / 128GFC, consulta de julio de 2026.
- Documentación técnica de fabricantes y proyectos citados (SNIA, Linux LVM, mdadm), consulta de julio de 2026.
