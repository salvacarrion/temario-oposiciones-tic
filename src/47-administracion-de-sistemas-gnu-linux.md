# Administración de sistemas GNU/Linux

GNU/Linux combina el núcleo Linux con las herramientas del proyecto GNU y domina el mundo del servidor, la nube y la supercomputación. Este tema recorre su administración: arranque, shell y scripting, servicios con systemd, software, usuarios y permisos, y los servicios de red que integran Linux en una red corporativa, incluido el Directorio Activo.

## Distribuciones, arranque y estructura de directorios

Una **distribución** empaqueta núcleo, herramientas y un gestor de paquetes. Las dos grandes familias son **Debian/Ubuntu** (paquetes `.deb`, gestor APT) y **Red Hat/RHEL/Fedora** (paquetes `.rpm`, gestor DNF), junto a SUSE y derivadas; en servidores corporativos pesan las versiones de **soporte largo (LTS)** y las suscripciones empresariales (RHEL, SLES).

- **Secuencia de arranque**: firmware **UEFI** (con arranque seguro) carga el gestor **GRUB 2**, que carga el **núcleo** y el *initramfs*; el núcleo monta la raíz y lanza el primer proceso, **systemd** (PID 1), que activa el resto según el *target* por defecto.
- **Jerarquía de ficheros (FHS)**: `/etc` (configuración), `/var` (datos variables y logs), `/home` (usuarios), `/usr` (software), `/boot` (núcleo y GRUB), `/dev` y `/proc`/`/sys` (dispositivos y estado del núcleo), `/tmp` (temporales).

## La shell: comandos y scripting

La shell habitual es **bash**: intérprete de comandos que encadena procesos con tuberías (`|`), redirige la entrada y la salida (`>`, `>>`, `2>`, `<`) y automatiza tareas con scripts. Es la herramienta central del administrador.

- **Comandos esenciales**: navegación y ficheros (`ls`, `cp`, `mv`, `rm`, `find`), texto (`grep`, `sed`, `awk`, `sort`), procesos (`ps`, `top`, `kill`), espacio (`df`, `du`), red (`ip`, `ss`, `ping`), archivo y copia remota (`tar`, `rsync`, `ssh`, `scp`).
- **Scripting**: variables, comprobaciones y bucles permiten automatizar la operación diaria:

```bash
#!/bin/bash
# copia diaria de /etc con retención de 7 días
FECHA=$(date +%F)
tar -czf /backup/etc-$FECHA.tar.gz /etc || exit 1
find /backup -name 'etc-*.tar.gz' -mtime +7 -delete
echo "backup OK $FECHA" | logger -t backup
```

- **Programación de tareas**: **cron** (`crontab -e`, campos minuto-hora-día-mes-día de semana) y los *timers* de systemd. Ejemplo: `0 3 * * * /usr/local/bin/backup.sh` ejecuta cada día a las 3:00.

## Servicios y systemd

**systemd** es el sistema de arranque y gestor de servicios de las distribuciones actuales: sustituye los *runlevels* de SysV por **targets** (`multi-user.target`, `graphical.target`) y define cada servicio en una **unidad** declarativa (`.service`, `.timer`, `.mount`, `.socket`) con dependencias y orden de arranque.

```bash
systemctl status nginx          # estado y últimos logs
systemctl enable --now nginx    # habilitar en el arranque y arrancar ya
systemctl daemon-reload         # recargar unidades tras editarlas
journalctl -u nginx --since today   # logs del servicio (journal)
```

El **journal** centraliza los logs binarios con metadatos; convive con syslog (rsyslog) para el reenvío a un servidor central de logs (tema 49).

## Gestión de software y actualizaciones

El software se instala desde **repositorios firmados** con el gestor de paquetes, que resuelve dependencias y permite aplicar de forma sistemática las **actualizaciones de seguridad** (la primera línea de defensa del sistema).

```bash
apt update && apt upgrade       # Debian/Ubuntu: refrescar índices y actualizar
apt install nginx               # instalar un paquete
dnf install nginx               # RHEL/Fedora
dnf check-update --security     # solo parches de seguridad
```

- **Buenas prácticas**: actualizaciones desatendidas para parches de seguridad (`unattended-upgrades`, `dnf-automatic`), repositorios réplica internos en redes grandes, y ventanas de mantenimiento para los reinicios de núcleo (o *live patching*).

## Almacenamiento local: montaje y LVM

Los sistemas de ficheros se montan sobre el árbol único de directorios, de forma manual (`mount`) o persistente en `/etc/fstab` (identificando el dispositivo por **UUID** o etiqueta). El RAID y las cabinas se tratan en el tema 45; en el propio servidor la pieza clave es el gestor de volúmenes lógicos.

- **LVM**: añade una capa flexible entre discos y sistemas de ficheros: los discos o particiones se declaran **volúmenes físicos (PV)**, se agrupan en **grupos de volúmenes (VG)** y de ellos se tallan **volúmenes lógicos (LV)**, que se pueden **redimensionar en caliente** y sacar *snapshots* (útiles antes de un cambio; no son copia de seguridad, tema 45).

```bash
pvcreate /dev/sdb                     # disco nuevo como volumen físico
vgextend vg_datos /dev/sdb            # ampliar el grupo
lvextend -r -L +50G /dev/vg_datos/lv_app   # crecer LV y su sistema de ficheros
```

- **Espacio y salud**: vigilancia de ocupación (`df -h`, `du -sh`), inodos (`df -i`) y estado SMART de los discos; el área de intercambio (*swap*) se define en la instalación o como fichero.

## Diagnóstico y rendimiento

El diagnóstico sigue la cadena recursos-procesos-logs: qué recurso satura (CPU, memoria, disco, red), qué proceso lo consume y qué cuentan los registros.

- **Carga y CPU**: `top`/`htop` y la **media de carga** (*load average* a 1/5/15 min; orientativamente, sostenida por encima del número de núcleos indica saturación).
- **Memoria**: `free -h` distinguiendo la memoria **disponible** de la usada por caché de disco (que se libera sola); presión real cuando el sistema pagina (*swap in/out* en `vmstat`).
- **Disco y E/S**: `iostat -x` (utilización y latencias; un **%iowait** alto delata cuello de E/S), `lsof` para ver qué ficheros usa un proceso.
- **Red**: `ip a`, `ss -tulpn` (puertos en escucha), `ping`/`traceroute` y `dig` para resolución de nombres.
- **Logs**: `journalctl -p err -b` (errores del arranque actual), `dmesg` (mensajes del núcleo, hardware) y los logs de cada servicio.

## Usuarios, permisos y seguridad local

Linux es multiusuario: las cuentas se definen en `/etc/passwd`, las contraseñas cifradas en `/etc/shadow` y los grupos en `/etc/group`; la autenticación se articula con **PAM** (módulos conectables).

- **Permisos**: cada fichero tiene propietario, grupo y permisos **rwx** para propietario/grupo/resto, expresables en octal (**755** = `rwxr-xr-x`, **644** = `rw-r--r--`); `umask` fija los permisos por defecto. Bits especiales: **setuid/setgid** (ejecutar con los privilegios del propietario o grupo) y **sticky bit** (en `/tmp`, solo el dueño borra sus ficheros). Para permisos más finos existen **ACL** (`setfacl`/`getfacl`).
- **Administración delegada**: **sudo** concede privilegios por usuario/comando con registro de auditoría (`/etc/sudoers`, editado con `visudo`); la cuenta root no se usa de forma interactiva.

```bash
useradd -m -G sudo maria        # crear usuario y añadir a un grupo
chown -R www-data:www-data /var/www
chmod 640 /etc/app/config       # rw- r-- ---
setfacl -m u:backup:r /etc/app/config   # ACL: lectura para un usuario extra
```

- **Control de acceso obligatorio**: **SELinux** (RHEL, políticas por etiquetas) y **AppArmor** (Ubuntu/SUSE, perfiles por programa) confinan procesos más allá de los permisos clásicos.
- **SSH**: acceso remoto cifrado; se endurece con autenticación por **claves** (`ssh-keygen`, `ssh-copy-id`), prohibiendo el login de root y limitando usuarios/orígenes en `sshd_config`.

## Servicios de red e integración con Directorio Activo

Sobre un Linux de servidor se despliegan los servicios de compartición e identidad que lo integran en la red corporativa (los servidores web, de correo y proxy se tratan en el tema 49).

- **Samba**: implementa el protocolo **SMB/CIFS**: comparte ficheros e impresoras con clientes Windows y puede actuar como miembro de dominio (o incluso como controlador de dominio compatible con AD).
- **NFS**: el sistema de ficheros en red nativo de UNIX, habitual entre servidores Linux (exportaciones en `/etc/exports`).
- **OpenLDAP**: servidor de **directorio LDAP** de código abierto para autenticación centralizada y cuentas de red en entornos Linux (esquema *posixAccount*); el concepto de directorio se desarrolla en el tema 49.
- **Integración con Directorio Activo**: el patrón actual usa **realmd/adcli** para unir la máquina al dominio y **SSSD** como cliente de identidad (autenticación **Kerberos**, búsqueda LDAP, caché offline y reglas de acceso); la vía clásica es **winbind** (Samba). Con ello los usuarios del AD inician sesión en los servidores Linux con su cuenta corporativa:

```bash
realm join --user=admin dominio.gva.es   # alta en el dominio (realmd + SSSD)
id 'DOMINIO\maria'                       # verificar resolución de usuarios AD
```

- **Otros servicios habituales**: DHCP y DNS (BIND, dnsmasq), NTP/chrony (sincronización horaria, crítica para Kerberos) y servidores de impresión (CUPS).

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Debian/Ubuntu y Red Hat Enterprise Linux (guías de administración), systemd (freedesktop.org), Samba, OpenLDAP y SSSD, consultadas en julio de 2026.
- Nemeth, E. et al., *UNIX and Linux System Administration Handbook*, 5.ª ed., Addison-Wesley, 2017.
- Tanenbaum, A. S. y Bos, H., *Modern Operating Systems*, 5.ª ed., Pearson, 2022.
