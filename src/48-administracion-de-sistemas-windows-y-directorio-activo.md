# Administración de sistemas Windows y Directorio Activo

Windows Server es el sistema operativo de servidor de Microsoft y el **Directorio Activo** su pieza central en entornos corporativos: centraliza identidades, equipos y políticas de configuración. Este tema cubre la administración de Windows Server, la estructura lógica y física de AD DS, la autenticación y el DNS, las directivas de grupo, PowerShell y la identidad en la nube con Microsoft Entra ID.

## Windows Server: ediciones, instalación y roles

La versión vigente es **Windows Server 2025** (disponible desde **noviembre de 2024**), en ediciones **Standard**, **Datacenter** (virtualización ilimitada y funciones de nube híbrida) y **Datacenter: Azure Edition**; el licenciamiento es por núcleo, más licencias de acceso de cliente (CAL).

- **Modos de instalación**: **Server Core** (sin interfaz gráfica: menor superficie de ataque y mantenimiento, el recomendado para infraestructuras) y experiencia de escritorio completa.
- **Despliegue automatizado**: el instalador arranca sobre **WinPE** (entorno de preinstalación); las instalaciones personalizadas se generalizan con **sysprep** (elimina identidad y SID de una imagen de referencia) y un fichero de respuestas `unattend.xml`, y se sirven por red con **WDS**/MDT o, en el puesto de trabajo moderno, con Autopilot/Intune (tema [52](52-puesto-de-trabajo-tic.md)).
- **Activación por volumen**: **KMS** (servicio de activación en la propia red, con umbral mínimo de equipos), claves **MAK** (activación individual contra Microsoft) y **activación basada en AD** (el equipo se activa al unirse al dominio).
- **Diagnóstico del sistema**: **Visor de eventos** (registros de Sistema, Seguridad y Aplicación), Monitor de rendimiento y de recursos, y reparación de ficheros del sistema con `sfc /scannow` y **DISM**; la configuración persistente vive en el **Registro** (colmenas HKLM y HKCU) y las tareas programadas, en el Programador de tareas (equivalente de cron).
- **Roles y características**: el servidor se especializa añadiendo roles (AD DS, DNS, DHCP, servicios de archivos, IIS, Hyper-V) desde el Administrador del servidor o PowerShell; la administración moderna usa **Windows Admin Center** (web) y la remota, WinRM/PowerShell o las consolas **RSAT** instaladas en el puesto del administrador (nunca iniciando sesión interactiva en los servidores).
- **Actualizaciones**: Windows Update, centralizado tradicionalmente con **WSUS** (sin desarrollo activo desde 2024, aunque sigue soportado) y en la estrategia actual con **Azure Update Manager**; el **hotpatching** (parches de seguridad sin reinicio) llega con Azure Edition o por suscripción vía Azure Arc.
- **Almacenamiento y permisos**: volúmenes **NTFS** (o ReFS para datos masivos) con permisos por **ACL**, herencia y auditoría; las carpetas compartidas combinan permisos de recurso y NTFS (prevalece el más restrictivo).
- **Servicios de archivos**: cuotas y filtrado por tipo de fichero con **FSRM**, instantáneas **VSS** («versiones anteriores» para el usuario) y cifrado de volumen con **BitLocker**.

## AD DS: estructura lógica

**AD DS (Active Directory Domain Services)** es un directorio jerárquico y replicado que almacena los objetos de la organización (usuarios, grupos, equipos) y da autenticación y autorización centralizadas. Es el principal de los roles de la familia Active Directory, junto a **AD CS** (autoridad de certificación), **AD FS** (federación de identidades), **AD LDS** (directorio ligero para aplicaciones) y **AD RMS** (protección de documentos).

- **Dominio**: unidad básica de administración y replicación, con su base de datos propia y espacio de nombres DNS (`gva.es`).
- **Árbol y bosque**: los dominios con espacio de nombres contiguo forman un **árbol**; el **bosque** agrupa árboles y es la **frontera de seguridad** real (esquema y catálogo global comunes, relaciones de confianza transitivas entre sus dominios).
- **Unidades organizativas (OU)**: contenedores jerárquicos dentro del dominio para ordenar usuarios y equipos, **delegar administración** y vincular directivas de grupo.
- **Esquema**: define las clases de objeto y sus atributos; es único por bosque y sus cambios son delicados (extensiones de aplicaciones como Exchange).
- **Base de datos y particiones**: el directorio vive en el fichero **NTDS.dit** de cada controlador, organizado en particiones de **esquema** y **configuración** (comunes al bosque), de **dominio** y de **aplicación** (p. ej. las zonas DNS integradas); **SYSVOL** replica entre controladores los scripts y las plantillas de las GPO (recursos compartidos `SYSVOL` y `NETLOGON`).
- **Grupos**: de **seguridad** (permisos) o distribución (correo); la práctica recomendada anida cuentas en globales, estos en locales de dominio y asigna permisos a estos últimos (patrón AGDLP). Ámbitos:

| Ámbito | Miembros habituales | Dónde se usa |
| --- | --- | --- |
| **Global** | Cuentas y globales de su dominio | En todo el bosque |
| **Local de dominio** | Cuentas, globales y universales de cualquier dominio | Solo en recursos de su dominio |
| **Universal** | Cuentas y globales de cualquier dominio (se replica al catálogo global) | En todo el bosque |

- **Niveles funcionales**: el nivel funcional del dominio y del bosque habilita funciones nuevas y viene limitado por la versión de Windows Server más antigua de los controladores; se eleva cuando todos los DC la superan. El nivel **Windows Server 2025** es el primero nuevo desde 2016 (habilita, entre otros, las páginas de base de datos de 32K).
- **Relaciones de confianza**: dentro del bosque son automáticas, **transitivas y bidireccionales** (padre-hijo y raíces de árbol); entre bosques se crean confianzas **de bosque**, y con dominios ajenos, **externas** o de acceso directo (*shortcut*), uni o bidireccionales según la dirección del acceso.

## Estructura física: controladores, sitios y replicación

La estructura física adapta el directorio a la topología de red real.

- **Controladores de dominio (DC)**: servidores que albergan la base de datos del directorio y autentican; la replicación es **multimaestro** (se escribe en cualquier DC). Todo dominio debe tener **al menos dos DC** (redundancia del servicio); en sedes con seguridad física limitada se usan **RODC** (controladores de solo lectura).
- **Catálogo global**: índice parcial de todos los objetos del bosque, necesario para inicios de sesión y búsquedas entre dominios.
- **Sitios y subredes**: los **sitios** modelan las ubicaciones con buena conectividad; la replicación dentro del sitio es inmediata y entre sitios se comprime y programa por enlaces de sitio.
- **Topología de replicación**: la calcula y mantiene automáticamente el **KCC** (*Knowledge Consistency Checker*) en cada DC; la replicación entre sitios se canaliza por **servidores cabeza de puente** (*bridgehead*).
- **Roles FSMO**: cinco operaciones que solo ejerce un DC a la vez:

| Rol FSMO | Ámbito | Función |
| --- | --- | --- |
| Maestro de **esquema** | Bosque | Cambios en el esquema |
| Maestro de **nombres de dominio** | Bosque | Altas y bajas de dominios |
| Maestro **RID** | Dominio | Reparte bloques de identificadores para nuevos objetos |
| **Emulador PDC** | Dominio | Referencia horaria, cambios de contraseña urgentes, GPO |
| Maestro de **infraestructura** | Dominio | Referencias a objetos de otros dominios |

- **Traslado de roles FSMO**: en caliente se **transfieren** entre DC (consolas o `Move-ADDirectoryServerOperationMasterRole`); si el titular se ha perdido, se **capturan** (*seize*, con `ntdsutil`) y el DC antiguo no debe volver a la red.
- **Diagnóstico de la replicación**: **dcdiag** ejecuta la batería de pruebas de salud de un DC; **repadmin /replsummary** resume el estado y los fallos de replicación entre controladores.

## Autenticación, LDAP y DNS integrado

- **Kerberos**: el protocolo de autenticación del dominio, basado en **tickets**: el cliente obtiene un **TGT** del KDC (todo DC lo es) y con él tickets de servicio (TGS) para cada recurso, sin reenviar la contraseña; cada servicio se identifica en el directorio por su **SPN** (*service principal name*). La **delegación** permite a un servicio actuar ante otros en nombre del usuario (no restringida, restringida y basada en recursos; solo esta última se recomienda hoy). **NTLM** pervive solo como legado: **NTLMv1 desaparece en Windows Server 2025** y NTLMv2 queda declarado en desuso (Microsoft recomienda Negotiate, que prefiere Kerberos).
- **LDAP**: el protocolo de acceso al directorio (puertos **389** y **636** con TLS), usado por aplicaciones y sistemas Linux para consultar e integrarse con AD; el **catálogo global** se consulta por los puertos **3268/3269**.
- **DNS integrado en AD**: imprescindible: los clientes localizan los controladores mediante **registros SRV** (`_ldap._tcp...`); las zonas integradas en AD se replican con el propio directorio y admiten actualizaciones dinámicas seguras. La **sincronización horaria** (jerarquía del emulador PDC) es crítica: Kerberos tolera por defecto **5 minutos** de desfase.
- **Administración del DNS**: lo no resuelto localmente se delega en **reenviadores** (generales o **condicionales** por dominio, típicos entre bosques que confían); las zonas pueden ser **secundarias** (copia de solo lectura por transferencia) o **de rutas internas** (*stub*: solo los NS de la zona); la **limpieza** (*scavenging*) purga los registros dinámicos caducados. Tipos de registro en el tema [70](70-protocolos-de-comunicaciones.md).

## Directivas de grupo (GPO)

Las **GPO** aplican configuración centralizada de seguridad, software y escritorio a usuarios y equipos: contraseñas y bloqueo, scripts, redirección de carpetas, plantillas administrativas del registro, restricciones de software.

- **Ámbito y herencia**: se vinculan a sitio, dominio y OU, y se aplican en el orden **local, sitio, dominio, OU** (LSDOU): la más cercana al objeto prevalece, salvo vínculos **forzados** (*enforced*) o bloqueo de herencia; el filtrado por seguridad o WMI afina los destinatarios.
- **GPO predefinidas**: **Default Domain Policy** (política de contraseñas y bloqueo de cuenta del dominio) y **Default Domain Controllers Policy** (derechos de usuario en los DC); la buena práctica es no sobrecargarlas con otras configuraciones.
- **Directivas y preferencias**: las directivas se imponen y reaplican; las **preferencias** (unidades de red, impresoras, accesos directos) fijan un valor inicial que el usuario puede cambiar. Las plantillas administrativas (**ADMX**) se centralizan en el **almacén central** de SYSVOL para que todas las consolas vean las mismas.
- **Procesamiento**: la configuración de **equipo** y la de **usuario** se procesan por separado (el modo *loopback* aplica las de usuario según el equipo: aulas, quioscos, RDS); los equipos las refrescan periódicamente (por defecto cada **90 minutos** con desfase aleatorio); diagnóstico con `gpupdate /force` y `gpresult /r`.
- **Buenas prácticas**: pocas GPO y bien nombradas, separar las de equipo y usuario, y probar en OU piloto antes de extender al dominio.

## Copia de seguridad, recuperación y seguridad del directorio

El directorio es el servicio más crítico del dominio: su pérdida o compromiso afecta a toda la organización.

- **Tolerancia a fallos del servidor**: en disco, **Storage Spaces** agrupa discos físicos en pools con resiliencia simple, en **espejo** o con **paridad** (RAID por software; cabinas y RAID hardware en el tema [45](45-sistemas-de-almacenamiento.md)); en servicio, el **clúster de conmutación por error** (*Failover Clustering*) mueve roles entre nodos con testigo de **quórum** (típico bajo Hyper-V, SQL Server o servidores de archivos). Si el sistema no arranca, **WinRE** (entorno de recuperación) permite reparar el arranque o restaurar una imagen.
- **Copia de seguridad**: se protege el **estado del sistema** (*system state*) de los controladores (base de datos NTDS, SYSVOL, registro), p. ej. con Windows Server Backup (`wbadmin`); la restauración de objetos borrados usa la **papelera de reciclaje de AD** (si está habilitada y dentro de la vida del objeto eliminado, **180 días** por defecto) o una restauración **autoritativa** (marca los objetos restaurados para que la replicación no los vuelva a borrar), frente a la no autoritativa (el DC se pone al día replicando). Las restauraciones del directorio exigen arrancar el DC en **DSRM** (*Directory Services Restore Mode*, con la contraseña propia fijada al promoverlo).
- **Buenas prácticas de seguridad**: separar cuentas de usuario y de administración por **niveles** (*tiering*: los administradores de dominio solo inician sesión en DC), **LAPS** (contraseñas de administrador local únicas y rotadas), **gMSA** (cuentas de servicio administradas con contraseña automática), grupo *Protected Users*, mínimo de servicios en los DC y parcheo prioritario; auditoría de cambios y vigilancia de ataques típicos al directorio (Kerberoasting, pass-the-hash, tema [28](28-ciberseguridad.md)), con detección especializada tipo Microsoft Defender for Identity.
- **Tras un compromiso**: además de restaurar desde copia **aislada** (el ransomware busca los DC), se restablece **dos veces** la contraseña de la cuenta **krbtgt** (invalida los tickets Kerberos robados, los *golden tickets*) y se rotan las credenciales privilegiadas (respuesta a incidentes en el tema [31](31-gestion-de-ciberincidentes.md)).

## PowerShell y administración moderna

**PowerShell** es la shell de administración de Windows: orientada a **objetos** (los cmdlets devuelven objetos, no texto) con nomenclatura *verbo-sustantivo*, canalizaciones y módulos para cada producto (ActiveDirectory, DNS, IIS). Se autodocumenta con `Get-Command` y `Get-Help`, simula cambios con `-WhatIf`, y permite administración remota masiva (`Invoke-Command`) y configuración declarativa (DSC).

```powershell
Get-Service | Where-Object Status -eq 'Stopped'
Get-ADUser -Filter 'Enabled -eq $false' | Select-Object Name
New-ADUser -Name "maria" -Path "OU=Personal,DC=gva,DC=es" -Enabled $true
Get-ADDomainController -Filter * | Select-Object Name,Site
Install-WindowsFeature AD-Domain-Services   # instalar el rol AD DS
Install-ADDSForest -DomainName "gva.es"     # promover el primer DC del bosque
```

- **Línea de comandos clásica**: sigue siendo el diagnóstico rápido universal:

| Comando | Uso |
| --- | --- |
| `ipconfig /all` | Configuración de red completa del equipo |
| `nslookup` | Consultas DNS |
| `netstat` | Conexiones y puertos en escucha |
| `sc query` / `net use` | Estado de servicios / unidades de red |
| `robocopy` | Copia masiva robusta de ficheros (reanudable, con ACL) |
| `gpupdate /force`, `gpresult /r` | Refresco y diagnóstico de GPO |

- **Microsoft Entra ID** (renombrado desde **Azure AD** en 2023): el directorio **en la nube** de Microsoft, base de identidad de Microsoft 365. No es un AD DS en la nube: no usa Kerberos/LDAP ni GPO, sino protocolos web (**OAuth 2.0, OpenID Connect, SAML**) y acceso condicional; la gestión de dispositivos se hace con Intune (tema [52](52-puesto-de-trabajo-tic.md)).
- **Identidad híbrida**: **Entra Connect** sincroniza las identidades locales con la nube (sincronización de hash de contraseña o autenticación federada), dando **inicio de sesión único** a los servicios cloud con la cuenta corporativa; es el escenario habitual en las administraciones. Los dispositivos se relacionan con Entra en tres grados: **unidos a Entra** (solo nube), **unidos híbridos** (dominio AD + Entra) y **registrados** (dispositivo personal BYOD).
- **Integración con Linux**: los servidores Linux se unen al dominio con SSSD/realmd o winbind (tema [47](47-administracion-de-sistemas-gnu-linux.md)), y Samba ofrece recursos compartidos a clientes Windows.

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Microsoft Learn: Windows Server 2025, Active Directory Domain Services, directivas de grupo, PowerShell y Microsoft Entra ID (consultada en julio de 2026).
- Desmond, B. et al., *Active Directory*, 5.ª ed., O'Reilly, 2013 (estructura lógica y FSMO).
