# Administración de sistemas Windows y Directorio Activo

Windows Server es el sistema operativo de servidor de Microsoft y el **Directorio Activo** su pieza central en entornos corporativos: centraliza identidades, equipos y políticas de configuración. Este tema cubre la administración de Windows Server, la estructura lógica y física de AD DS, la autenticación y el DNS, las directivas de grupo, PowerShell y la identidad en la nube con Microsoft Entra ID.

## Windows Server: ediciones, instalación y roles

La versión vigente es **Windows Server 2025** (disponible desde **noviembre de 2024**), en ediciones **Standard** y **Datacenter** (esta con virtualización ilimitada y funciones de nube híbrida; el licenciamiento es por núcleo).

- **Modos de instalación**: **Server Core** (sin interfaz gráfica: menor superficie de ataque y mantenimiento, el recomendado para infraestructuras) y experiencia de escritorio completa.
- **Roles y características**: el servidor se especializa añadiendo roles (AD DS, DNS, DHCP, servicios de archivos, IIS, Hyper-V) desde el Administrador del servidor o PowerShell; la administración moderna usa **Windows Admin Center** (web) y la remota, WinRM/PowerShell.
- **Almacenamiento y permisos**: volúmenes **NTFS** (o ReFS para datos masivos) con permisos por **ACL**, herencia y auditoría; las carpetas compartidas combinan permisos de recurso y NTFS (prevalece el más restrictivo).

## AD DS: estructura lógica

**AD DS (Active Directory Domain Services)** es un directorio jerárquico y replicado que almacena los objetos de la organización (usuarios, grupos, equipos) y da autenticación y autorización centralizadas.

- **Dominio**: unidad básica de administración y replicación, con su base de datos propia y espacio de nombres DNS (`gva.es`).
- **Árbol y bosque**: los dominios con espacio de nombres contiguo forman un **árbol**; el **bosque** agrupa árboles y es la **frontera de seguridad** real (esquema y catálogo global comunes, relaciones de confianza transitivas entre sus dominios).
- **Unidades organizativas (OU)**: contenedores jerárquicos dentro del dominio para ordenar usuarios y equipos, **delegar administración** y vincular directivas de grupo.
- **Esquema**: define las clases de objeto y sus atributos; es único por bosque y sus cambios son delicados (extensiones de aplicaciones como Exchange).
- **Grupos**: de **seguridad** (permisos) o distribución (correo), con ámbitos **global**, **local de dominio** y **universal**; la práctica recomendada anida cuentas en globales, estos en locales de dominio y asigna permisos a estos últimos (patrón AGDLP).
- **Niveles funcionales**: el nivel funcional del dominio y del bosque habilita funciones nuevas y viene limitado por la versión de Windows Server más antigua de los controladores; se eleva cuando todos los DC la superan.
- **Relaciones de confianza**: dentro del bosque son automáticas, **transitivas y bidireccionales** (padre-hijo y raíces de árbol); entre bosques se crean confianzas **de bosque**, y con dominios ajenos, **externas** o de acceso directo (*shortcut*), uni o bidireccionales según la dirección del acceso.

## Estructura física: controladores, sitios y replicación

La estructura física adapta el directorio a la topología de red real.

- **Controladores de dominio (DC)**: servidores que albergan la base de datos del directorio y autentican; la replicación es **multimaestro** (se escribe en cualquier DC). En sedes con seguridad física limitada se usan **RODC** (controladores de solo lectura).
- **Catálogo global**: índice parcial de todos los objetos del bosque, necesario para inicios de sesión y búsquedas entre dominios.
- **Sitios y subredes**: los **sitios** modelan las ubicaciones con buena conectividad; la replicación dentro del sitio es inmediata y entre sitios se comprime y programa por enlaces de sitio.
- **Roles FSMO**: cinco operaciones que solo ejerce un DC a la vez:

| Rol FSMO | Ámbito | Función |
| --- | --- | --- |
| Maestro de **esquema** | Bosque | Cambios en el esquema |
| Maestro de **nombres de dominio** | Bosque | Altas y bajas de dominios |
| Maestro **RID** | Dominio | Reparte bloques de identificadores para nuevos objetos |
| **Emulador PDC** | Dominio | Referencia horaria, cambios de contraseña urgentes, GPO |
| Maestro de **infraestructura** | Dominio | Referencias a objetos de otros dominios |

## Autenticación, LDAP y DNS integrado

- **Kerberos**: el protocolo de autenticación del dominio, basado en **tickets**: el cliente obtiene un **TGT** del KDC (todo DC lo es) y con él tickets de servicio (TGS) para cada recurso, sin reenviar la contraseña. **NTLM** pervive solo como legado y tiende a deshabilitarse.
- **LDAP**: el protocolo de acceso al directorio (puertos **389** y **636** con TLS), usado por aplicaciones y sistemas Linux para consultar e integrarse con AD.
- **DNS integrado en AD**: imprescindible: los clientes localizan los controladores mediante **registros SRV** (`_ldap._tcp...`); las zonas integradas en AD se replican con el propio directorio y admiten actualizaciones dinámicas seguras. La **sincronización horaria** (jerarquía del emulador PDC) es crítica: Kerberos tolera por defecto **5 minutos** de desfase.

## Directivas de grupo (GPO)

Las **GPO** aplican configuración centralizada de seguridad, software y escritorio a usuarios y equipos: contraseñas y bloqueo, scripts, redirección de carpetas, plantillas administrativas del registro, restricciones de software.

- **Ámbito y herencia**: se vinculan a sitio, dominio y OU, y se aplican en el orden **local, sitio, dominio, OU** (LSDOU): la más cercana al objeto prevalece, salvo vínculos **forzados** (*enforced*) o bloqueo de herencia; el filtrado por seguridad o WMI afina los destinatarios.
- **Procesamiento**: los equipos las refrescan periódicamente (por defecto cada **90 minutos** con desfase aleatorio); diagnóstico con `gpupdate /force` y `gpresult /r`.
- **Buenas prácticas**: pocas GPO y bien nombradas, separar las de equipo y usuario, y probar en OU piloto antes de extender al dominio.

## Copia de seguridad, recuperación y seguridad del directorio

El directorio es el servicio más crítico del dominio: su pérdida o compromiso afecta a toda la organización.

- **Copia de seguridad**: se protege el **estado del sistema** (*system state*) de los controladores (base de datos NTDS, SYSVOL, registro); la restauración de objetos borrados usa la **papelera de reciclaje de AD** (si está habilitada) o una restauración **autoritativa** (marca los objetos restaurados para que la replicación no los vuelva a borrar), frente a la no autoritativa (el DC se pone al día replicando).
- **Buenas prácticas de seguridad**: separar cuentas de usuario y de administración por **niveles** (*tiering*: los administradores de dominio solo inician sesión en DC), **LAPS** (contraseñas de administrador local únicas y rotadas), **gMSA** (cuentas de servicio administradas con contraseña automática), grupo *Protected Users*, mínimo de servicios en los DC y parcheo prioritario; auditoría de cambios y vigilancia de ataques típicos al directorio (Kerberoasting, pass-the-hash, tema 28).

## PowerShell y administración moderna

**PowerShell** es la shell de administración de Windows: orientada a **objetos** (los cmdlets devuelven objetos, no texto) con nomenclatura *verbo-sustantivo*, canalizaciones y módulos para cada producto (ActiveDirectory, DNS, IIS). Permite administración remota masiva (`Invoke-Command`) y configuración declarativa (DSC).

```powershell
Get-Service | Where-Object Status -eq 'Stopped'
Get-ADUser -Filter 'Enabled -eq $false' | Select-Object Name
New-ADUser -Name "maria" -Path "OU=Personal,DC=gva,DC=es" -Enabled $true
Get-ADDomainController -Filter * | Select-Object Name,Site
```

- **Microsoft Entra ID** (renombrado desde **Azure AD** en 2023): el directorio **en la nube** de Microsoft, base de identidad de Microsoft 365. No es un AD DS en la nube: no usa Kerberos/LDAP ni GPO, sino protocolos web (**OAuth 2.0, OpenID Connect, SAML**) y acceso condicional; la gestión de dispositivos se hace con Intune (tema 52).
- **Identidad híbrida**: **Entra Connect** sincroniza las identidades locales con la nube (sincronización de hash de contraseña o autenticación federada), dando **inicio de sesión único** a los servicios cloud con la cuenta corporativa; es el escenario habitual en las administraciones.
- **Integración con Linux**: los servidores Linux se unen al dominio con SSSD/realmd o winbind (tema 47), y Samba ofrece recursos compartidos a clientes Windows.

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Microsoft Learn: Windows Server 2025, Active Directory Domain Services, directivas de grupo, PowerShell y Microsoft Entra ID (consultada en julio de 2026).
- Desmond, B. et al., *Active Directory*, 5.ª ed., O'Reilly, 2013 (estructura lógica y FSMO).
