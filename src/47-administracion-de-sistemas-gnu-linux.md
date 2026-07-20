# Administración de sistemas GNU/Linux

GNU/Linux combina el núcleo Linux con las herramientas del proyecto GNU y domina el mundo del servidor, la nube y la supercomputación. Este tema recorre su administración: arranque, shell y scripting, servicios con systemd, software, usuarios y permisos, y los servicios de red que integran Linux en una red corporativa, incluido el Directorio Activo.

## Distribuciones, arranque y estructura de directorios

Una **distribución** empaqueta núcleo, herramientas y un gestor de paquetes. En servidores corporativos pesan las versiones de **soporte largo (LTS)** y las suscripciones empresariales con soporte de 10 años (RHEL, SLES).

| Familia | Paquetes | Gestor | Ejemplos (versiones vigentes, jul-2026) |
| --- | --- | --- | --- |
| Debian | `.deb` | APT | **Debian 13** «trixie» (ago-2025); **Ubuntu 24.04 y 26.04 LTS** (abr-2026) |
| Red Hat | `.rpm` | DNF | **RHEL 10** (may-2025) y Fedora; derivadas gratuitas AlmaLinux y Rocky Linux |
| SUSE | `.rpm` | zypper | SLES, openSUSE Leap |

- **Ciclos de soporte**: Ubuntu LTS sale cada 2 años (los `.04` de año par) con **5 años** de soporte (10 con Ubuntu Pro); Debian da **3 años** de soporte pleno más 2 de LTS; RHEL y SLES, **10 años** por versión mayor.
- **Secuencia de arranque**: firmware **UEFI** (con arranque seguro) carga el gestor **GRUB 2** (instalado en la partición de sistema EFI o, en equipos antiguos con BIOS, en el **MBR**; el histórico LILO está abandonado), que carga el **núcleo** y el *initramfs* (raíz mínima en memoria con los controladores para montar el disco); el núcleo monta la raíz y lanza el primer proceso, **systemd** (PID 1), que activa el resto según el *target* por defecto (los sistemas antiguos usaban el init de SysV con `/etc/inittab` y *runlevels*).
- **Reparación y análisis**: desde el menú de GRUB se pueden editar los parámetros del núcleo para arrancar en modo rescate; `systemd-analyze blame` desglosa qué unidades retrasan el arranque.
- **Módulos y parámetros del núcleo**: los módulos se listan y cargan con `lsmod`/`modprobe` (controladores bajo demanda); los parámetros se consultan y ajustan en caliente con `sysctl` (persistentes en `/etc/sysctl.d`, p. ej. `vm.swappiness` o `net.ipv4.ip_forward`).
- **Jerarquía de ficheros (FHS)**: `/etc` (configuración), `/var` (datos variables y logs), `/home` (usuarios), `/root` (home de root), `/usr` (software), `/opt` y `/srv` (aplicaciones de terceros y datos servidos), `/boot` (núcleo y GRUB), `/dev` (dispositivos), `/tmp` (temporales). En servidores, `/var` (y a veces `/home` y `/tmp`) va en partición o disco aparte: un log desbocado o una subida masiva no llenan la raíz.
- **Pseudo-sistemas de ficheros**: `/proc` no existe en disco: expone el estado del núcleo y de cada proceso como ficheros virtuales (`/proc/cpuinfo`, `/proc/meminfo`, `/proc/cmdline`, `/proc/<pid>/`); `/sys` expone dispositivos, buses, módulos y firmware. Son la vía de comunicación con el núcleo que usan muchas herramientas.

## La shell: comandos y scripting

La shell habitual es **bash**: intérprete de comandos que encadena procesos con tuberías (`|`), redirige la entrada y la salida y automatiza tareas con scripts. Es la herramienta central del administrador.

- **Comandos esenciales**: navegación y ficheros (`ls`, `cp`, `mv`, `rm`, `find`), texto (`grep`, `sed`, `awk`, `sort`), procesos (`ps`, `top`, `kill`), espacio (`df`, `du`), red (`ip`, `ss`, `ping`), archivo y copia remota (`tar`, `rsync`, `ssh`, `scp`).
- **Utilidades de ficheros**: empaquetado y compresión (`tar -czf copia.tar.gz dir` crea, `tar -xzf` extrae; algoritmos gzip, bzip2, xz y zstd), enlaces (`ln` duro, `ln -s` simbólico), búsqueda con acción (`find /var -name '*.log' -mtime +30 -exec rm {} \;`), localización de ejecutables (`which`, `whereis`), visualización (`cat`, `less`) y metadatos (`stat`).
- **Redirección y encadenado**: `>` sobrescribe, `>>` añade, `2>` desvía los errores, `2>&1` los combina con la salida y `<` toma la entrada de un fichero; `&&` y `||` encadenan según el **código de salida** del comando anterior (`$?`, **0 = éxito**) y `;` ejecuta en secuencia incondicionalmente. Las **variables de entorno** se publican con `export` (`PATH`, `HOME`, `LANG`) y se retiran con `unset`.
- **Expansión de nombres**: los comodines `*` (cualquier cadena) y `?` (un carácter) se expanden antes de ejecutar el comando; `\` escapa caracteres especiales y las comillas simples suprimen toda expansión.
- **Control de trabajos**: `&` lanza en segundo plano, `Ctrl-Z` suspende, `jobs` lista, `fg`/`bg` reanudan en primer o segundo plano, y `nohup`/`disown` evitan que el proceso muera al cerrar la terminal.
- **Procesos y señales**: `kill -15` (SIGTERM, terminación ordenada, la señal por defecto) frente a `kill -9` (SIGKILL, inmediata e inignorable); la prioridad se ajusta con `nice`/`renice` (valores -20 a +19).
- **Ayuda y edición**: el manual se consulta con `man` (secciones **1** comandos, **5** formatos de fichero, **8** administración) e `info`; los editores de referencia en consola son `vi`/`vim` y `nano`.
- **Estructuras de control**: condicionales `if [ -f /etc/app.conf ]; then …; fi` (con `test`/`[ ]` para ficheros, cadenas y números), bucles `for`/`while`, selección `case` y sustitución de comandos `$(comando)`.
- **Scripting**: variables, comprobaciones y bucles permiten automatizar la operación diaria:

```bash
#!/bin/bash
# copia diaria de /etc con retención de 7 días
FECHA=$(date +%F)
tar -czf /backup/etc-$FECHA.tar.gz /etc || exit 1
find /backup -name 'etc-*.tar.gz' -mtime +7 -delete
echo "backup OK $FECHA" | logger -t backup
```

- **Programación de tareas**: **cron** (`crontab -e`, campos minuto-hora-día-mes-día de semana; tareas de sistema en `/etc/cron.d` y `cron.daily`) y los *timers* de systemd, que añaden logs en el journal y recuperación de ejecuciones perdidas (como anacron). Ejemplo: `0 3 * * * /usr/local/bin/backup.sh` ejecuta cada día a las 3:00.
- **Automatización a escala**: cuando los servidores se cuentan por decenas, los scripts ceden ante la gestión de configuración: **Ansible** (sin agente, opera por SSH) describe el estado deseado en **playbooks** YAML idempotentes (aplicarlos dos veces no cambia nada); las plantillas de máquina virtual se personalizan en el primer arranque con **cloud-init**.

```yaml
# playbook: asegurar nginx instalado y arrancado en todos los web
- hosts: web
  become: true
  tasks:
    - ansible.builtin.package: {name: nginx, state: present}
    - ansible.builtin.service: {name: nginx, state: started, enabled: true}
```

## Servicios y systemd

**systemd** es el sistema de arranque y gestor de servicios de las distribuciones actuales: sustituye los *runlevels* de SysV por **targets** (`multi-user.target` ≈ antiguo runlevel 3, `graphical.target` ≈ 5, `rescue.target` ≈ modo monousuario) y define cada servicio en una **unidad** declarativa (`.service`, `.timer`, `.mount`, `.socket`) con dependencias y orden de arranque:

```ini
# /etc/systemd/system/app.service
[Unit]
Description=Servicio de la aplicacion
After=network-online.target

[Service]
Type=simple
User=app
ExecStart=/opt/app/bin/app
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Las dependencias se declaran en la unidad: `After=`/`Before=` fijan el **orden**, `Requires=`/`Wants=` la **dependencia** (dura o débil); `systemctl isolate` cambia de target en caliente.

```bash
systemctl status nginx          # estado y últimos logs
systemctl enable --now nginx    # habilitar en el arranque y arrancar ya
systemctl daemon-reload         # recargar unidades tras editarlas
journalctl -u nginx --since today   # logs del servicio (journal)
```

El **journal** centraliza los logs binarios con metadatos (persistente con `Storage=persistent` en `journald.conf`); convive con syslog (rsyslog) para el reenvío a un servidor central de logs (tema [49](49-servicios-de-infraestructura.md)).

## Gestión de software y actualizaciones

El software se instala desde **repositorios firmados** con el gestor de paquetes, que resuelve dependencias y permite aplicar de forma sistemática las **actualizaciones de seguridad** (la primera línea de defensa del sistema).

```bash
apt update && apt upgrade       # Debian/Ubuntu: refrescar índices y actualizar
apt install nginx               # instalar un paquete
dnf install nginx               # RHEL/Fedora
dnf check-update --security     # solo parches de seguridad
dpkg -l | grep nginx            # consultar lo instalado (Debian/Ubuntu)
rpm -qa | grep nginx            # consultar lo instalado (RHEL)
```

- **Repositorios**: se definen en `/etc/apt/sources.list(.d)` (Debian/Ubuntu) o `/etc/yum.repos.d/*.repo` (RHEL) y se validan con **claves GPG**; las versiones críticas se fijan con *pinning* de APT o `versionlock` de DNF.
- **Formatos autocontenidos**: **Flatpak** y **Snap** empaquetan la aplicación con sus dependencias, aisladas del sistema y con actualización propia; habituales en escritorio, marginales en servidor.
- **Buenas prácticas**: actualizaciones desatendidas para parches de seguridad (`unattended-upgrades`, `dnf-automatic`), repositorios réplica internos en redes grandes, y ventanas de mantenimiento para los reinicios de núcleo (o *live patching*).

## Almacenamiento local: montaje y LVM

Los sistemas de ficheros se montan sobre el árbol único de directorios, de forma manual (`mount`) o persistente en `/etc/fstab` (identificando el dispositivo por **UUID** o etiqueta: `UUID=… /datos xfs defaults 0 2`). El RAID y las cabinas se tratan en el tema [45](45-sistemas-de-almacenamiento.md); en el propio servidor la pieza clave es el gestor de volúmenes lógicos.

- **Nomenclatura de dispositivos**: los discos SATA/SAS/USB aparecen como `/dev/sda`, `/dev/sdb`… y sus particiones como `/dev/sda1`, `/dev/sda2`; los NVMe, como `/dev/nvme0n1` (partición `/dev/nvme0n1p1`); los virtualizados, como `/dev/vda`. La cadena completa es disco → partición → (opcional) volumen LVM → sistema de ficheros.
- **Particionado y formato**: los discos llevan tabla de particiones **GPT** (sustituye al MBR: discos de más de **2 TB**, hasta **128 particiones**, copia de respaldo de la tabla), se particionan con `parted`/`fdisk` y se formatean con `mkfs.ext4`/`mkfs.xfs`.
- **Comprobación**: `fsck` diagnostica y repara un sistema de ficheros dañado tras una caída (se lanza automáticamente si el montaje detecta un estado sucio); **nunca sobre un sistema de ficheros montado** en escritura.
- **LVM**: añade una capa flexible entre discos y sistemas de ficheros: los discos o particiones se declaran **volúmenes físicos (PV)**, se agrupan en **grupos de volúmenes (VG)** y de ellos se tallan **volúmenes lógicos (LV)**, que se pueden **redimensionar en caliente** y sacar *snapshots* (útiles antes de un cambio; no son copia de seguridad, tema [45](45-sistemas-de-almacenamiento.md)). Ojo al sistema de ficheros: ext4 puede crecer y encoger (esto último desmontado), pero **XFS solo crece**.

```bash
pvcreate /dev/sdb                     # disco nuevo como volumen físico
vgextend vg_datos /dev/sdb            # ampliar el grupo
lvextend -r -L +50G /dev/vg_datos/lv_app   # crecer LV y su sistema de ficheros
```

- **Espacio y salud**: vigilancia de ocupación (`df -h`, `du -sh`), inodos (`df -i`) y estado SMART de los discos; las **cuotas de disco** por usuario o grupo se fijan con `edquota` (límites blando y duro con periodo de gracia).
- **Swap**: el área de intercambio se define en la instalación (partición o fichero); la regla clásica del **doble de la RAM** hoy se matiza (en servidores con mucha memoria basta una fracción, ajustando `vm.swappiness`).
- **Copias locales**: `tar` y `rsync` son la base actual (el clásico `dump/restore` por niveles **0-9**, donde el nivel N copia lo cambiado desde el N-1, dio nombre al esquema completo/incremental); políticas y soportes en el tema [45](45-sistemas-de-almacenamiento.md).

## Diagnóstico y rendimiento

El diagnóstico sigue la cadena recursos-procesos-logs: qué recurso satura (CPU, memoria, disco, red), qué proceso lo consume y qué cuentan los registros.

- **Sistema y sesiones**: `uname -a` (núcleo, versión y arquitectura), `hostnamectl`, `uptime` y `who`/`w` (quién tiene sesión abierta y qué ejecuta).
- **Carga y CPU**: `top`/`htop` y la **media de carga** (*load average* a 1/5/15 min; orientativamente, sostenida por encima del número de núcleos indica saturación).
- **Memoria**: `free -h` distinguiendo la memoria **disponible** de la usada por caché de disco (que se libera sola); presión real cuando el sistema pagina (*swap in/out* en `vmstat`).
- **Disco y E/S**: `iostat -x` (utilización y latencias; un **%iowait** alto delata cuello de E/S), `lsof` para ver qué ficheros usa un proceso.
- **Red**: `ip a` y `ip route` (interfaces y rutas; la suite `ip` sustituye a los históricos ifconfig/route), `ss -tulpn` (puertos en escucha; sustituye a netstat), `ping`/`traceroute`, y para nombres `dig` (también `host` y `nslookup`) y `whois` (titularidad de un dominio).
- **Análisis y auditoría de red**: `tcpdump` captura el tráfico en línea de comandos (Wireshark en gráfico) y `nmap` escanea los puertos abiertos de los propios servidores para contrastarlos con lo esperado (seguridad de red en el tema [79](79-seguridad-en-las-comunicaciones.md)).
- **Histórico y trazado**: `sar` (paquete sysstat) guarda series históricas de todos los recursos; `strace` traza las llamadas al sistema de un proceso que falla sin logs.
- **Logs**: `journalctl -p err -b` (errores del arranque actual), `dmesg` (mensajes del núcleo, hardware) y los logs de cada servicio.

## Usuarios, permisos y seguridad local

Linux es multiusuario: las cuentas se definen en `/etc/passwd`, las contraseñas cifradas en `/etc/shadow` y los grupos en `/etc/group`; el esqueleto del home nuevo sale de `/etc/skel` y la autenticación se articula con **PAM** (módulos conectables).

- **Permisos**: cada fichero tiene propietario, grupo y permisos **rwx** para propietario/grupo/resto, expresables en octal (**755** = `rwxr-xr-x`, **644** = `rw-r--r--`); `umask` fija los permisos por defecto. Bits especiales: **setuid/setgid** (ejecutar con los privilegios del propietario o grupo) y **sticky bit** (en `/tmp`, solo el dueño borra sus ficheros). Para permisos más finos existen **ACL** (`setfacl`/`getfacl`).
- **Administración delegada**: **sudo** concede privilegios por usuario/comando con registro de auditoría (`/etc/sudoers`, editado con `visudo`); la cuenta root no se usa de forma interactiva.
- **Política de contraseñas**: caducidad y avisos con `chage`, bloqueo de cuenta con `passwd -l`, requisitos de complejidad vía PAM (`pam_pwquality`) y bloqueo por intentos fallidos (`pam_faillock`).

```bash
useradd -m -G sudo maria        # crear usuario y añadir a un grupo
chown -R www-data:www-data /var/www     # propietario (chgrp solo el grupo)
chmod 640 /etc/app/config       # octal: rw- r-- ---
chmod u+x deploy.sh             # simbólico: ejecución para el dueño (a+x, todos)
setfacl -m u:backup:r /etc/app/config   # ACL: lectura para un usuario extra
```

- **Control de acceso obligatorio**: **SELinux** (RHEL, políticas por etiquetas de contexto sobre procesos y ficheros, visibles con `ls -Z`) y **AppArmor** (Ubuntu/SUSE, perfiles por programa) confinan procesos más allá de los permisos clásicos. SELinux opera en modo **enforcing** (aplica), **permissive** (solo registra) o disabled; se consulta con `getenforce` y se afina con booleanos (`setsebool -P httpd_can_network_connect on`) sin escribir políticas.
- **Cortafuegos local**: el filtrado lo hace el marco **netfilter** del núcleo, con tablas de **filtrado** (filter), **NAT** (traducción de direcciones, p. ej. *masquerade* para dar salida a una red interna) y **mangle** (alteración de paquetes). La interfaz actual es **nftables** (sucesor de iptables, hoy legado) y se administra con **firewalld** (RHEL/SUSE, zonas y servicios: `firewall-cmd --permanent --add-service=https`) o **ufw** (Ubuntu: `ufw allow 443/tcp`).
- **SSH**: acceso remoto cifrado; se endurece con autenticación por **claves** (`ssh-keygen`, `ssh-copy-id`; `ssh-agent`/`ssh-add` guardan la clave descifrada en la sesión), prohibiendo el login de root y limitando usuarios/orígenes en `sshd_config`. Además de terminal ofrece copia (`scp`/`sftp`) y **túneles** (`-L`/`-R`, reenvío de puertos sobre el canal cifrado).

## Servicios de red e integración con Directorio Activo

Sobre un Linux de servidor se despliegan los servicios de compartición e identidad que lo integran en la red corporativa (los servidores web y proxy y el correo con **Postfix**, sucesor del histórico Sendmail, se tratan en el tema [49](49-servicios-de-infraestructura.md); los protocolos, en el [70](70-protocolos-de-comunicaciones.md)).

- **Configuración de red del servidor**: **NetworkManager** (`nmcli`) en RHEL y escritorios, **netplan** en Ubuntu Server (YAML en `/etc/netplan`); IP estática, pasarela y DNS (`/etc/resolv.conf`, gestionado por systemd-resolved) y nombre de equipo con `hostnamectl`.
- **Samba**: implementa el protocolo **SMB/CIFS**: comparte ficheros e impresoras con clientes Windows y puede actuar como miembro de dominio (o incluso como controlador de dominio compatible con AD). Cliente: `smbclient -L servidor` lista los recursos y `mount -t cifs` los monta.
- **NFS**: el sistema de ficheros en red nativo de UNIX, habitual entre servidores Linux (exportaciones en `/etc/exports`). Los montajes **hard** reintentan indefinidamente si el servidor cae (coherencia a costa de bloqueos); los **soft** devuelven error tras varios reintentos.
- **DNS y DHCP**: **BIND** es el servidor DNS de referencia (zonas con primario y secundarios; **dnsmasq** como caché/DHCP ligero para redes pequeñas); el servidor DHCP reparte direcciones por **rangos** con **reservas** por MAC para los equipos fijos. Protocolo, registros y funcionamiento en el tema [70](70-protocolos-de-comunicaciones.md).
- **OpenLDAP**: servidor de **directorio LDAP** de código abierto para autenticación centralizada y cuentas de red en entornos Linux (esquema *posixAccount*); sustituyó al histórico **NIS** («páginas amarillas») en ese papel. El concepto de directorio se desarrolla en el tema [49](49-servicios-de-infraestructura.md).
- **Integración con Directorio Activo**: el patrón actual usa **realmd/adcli** para unir la máquina al dominio y **SSSD** como cliente de identidad (autenticación **Kerberos**, búsqueda LDAP, caché offline y reglas de acceso, con `realm permit` para limitar quién entra); la vía clásica es **winbind** (Samba). Con ello los usuarios del AD inician sesión en los servidores Linux con su cuenta corporativa:

```bash
realm join --user=admin dominio.gva.es   # alta en el dominio (realmd + SSSD)
id 'DOMINIO\maria'                       # verificar resolución de usuarios AD
```

- **Transferencia de ficheros**: el FTP clásico (servidor **vsftpd**; modos activo/pasivo en el tema [70](70-protocolos-de-comunicaciones.md)) está desplazado por **SFTP** sobre SSH, que cifra y no necesita puertos extra.
- **Impresión**: **CUPS** gestiona las colas (*spooler*) con el protocolo **IPP** (herencia de los comandos `lpr`/`lpq`/`lprm` del histórico LPD); la impresora recibe el trabajo en un lenguaje de descripción de página (**PDL**: PostScript, PCL).
- **Otros servicios habituales**: NTP/chrony (sincronización horaria, crítica para Kerberos).

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Debian/Ubuntu y Red Hat Enterprise Linux (guías de administración), systemd (freedesktop.org), Samba, OpenLDAP y SSSD, consultadas en julio de 2026.
- Nemeth, E. et al., *UNIX and Linux System Administration Handbook*, 5.ª ed., Addison-Wesley, 2017.
- Tanenbaum, A. S. y Bos, H., *Modern Operating Systems*, 5.ª ed., Pearson, 2022.
