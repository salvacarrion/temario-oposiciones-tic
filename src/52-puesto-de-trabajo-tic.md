# Puesto de trabajo TIC

## El puesto de trabajo TIC: normalización, seguridad y despliegue

El puesto de trabajo TIC es el conjunto de dispositivos (PC, portátil, periféricos) y software con el que el empleado desempeña su trabajo. Gestionarlo a la escala de una organización (miles de equipos) exige normalizar las configuraciones, automatizar el despliegue y aplicar una seguridad homogénea durante todo su ciclo de vida.

### Normalización

- **Puesto tipo**: catálogo cerrado de configuraciones hardware y software definidas por perfiles de usuario (administrativo, técnico, directivo), en lugar de equipos heterogéneos comprados caso a caso.
- **Imagen maestra corporativa**: sistema operativo con sus parches, aplicaciones base, configuración de seguridad y personalización de la organización, a partir de la cual se instalan todos los equipos.
- **Cliente pesado o ligero**: el puesto normalizado puede materializarse en un PC completo (*fat client*), donde se ejecutan localmente sistema y aplicaciones, o en un **thin client** que solo presenta escritorios o aplicaciones remotos (ver la sección de VDI); la elección condiciona coste, mantenimiento y consumo.
- **Beneficios**: soporte y resolución de incidencias más simples, compras y licenciamiento racionalizados, seguridad y cumplimiento homogéneos e interoperabilidad garantizada entre puestos.
- **Ejemplo en la GVA**: además del puesto Windows corporativo (ver más abajo), la Generalitat normaliza el puesto de los centros educativos con **LliureX**, su distribución GNU/Linux propia.

### Despliegue y ciclo de vida

- **Despliegue por imagen**: la maestra se generaliza y se vuelca a los equipos, normalmente con arranque por red **PXE** y herramientas de distribución (Configuration Manager, Clonezilla).
- **Aprovisionamiento moderno**: el equipo llega de fábrica y se autoconfigura por internet al registrarse contra la nube de gestión, sin pasar por maquetación (**Windows Autopilot** con Intune).
- **Ciclo de vida del puesto**: adquisición → despliegue → operación y soporte → renovación (típicamente cada **4-5 años**) → retirada, con **borrado seguro** de los soportes de información antes de la enajenación o destrucción.
- **Gestión de parches**: actualización continua y centralizada del sistema operativo y las aplicaciones; es una de las medidas de higiene de seguridad más eficaces.

### Seguridad del puesto

- **Medidas técnicas habituales**: cifrado de disco completo (BitLocker), protección antimalware/EDR gestionada centralmente, cortafuegos personal, usuarios sin privilegios de administrador, listas de aplicaciones permitidas y bloqueo automático de sesión.
- **Autenticación en el puesto**: en las administraciones es habitual la autenticación robusta con **tarjeta criptográfica** de empleado público o DNIe (certificado electrónico), complementada con biometría o PIN (Windows Hello) y **SSO** (*single sign-on*) hacia las aplicaciones corporativas.
- **El ENS (RD 311/2022, Anexo II)** dedica al puesto la familia **mp.eq, «Protección de los equipos»** (tema [29](29-esquema-nacional-de-seguridad.md)):
    - **mp.eq.1 Puesto de trabajo despejado**: sin material distinto del necesario en cada momento; con refuerzo (desde categoría MEDIA), el material usado se guarda en lugar cerrado.
    - **mp.eq.2 Bloqueo de puesto de trabajo** (dimensión A, desde nivel MEDIO): bloqueo tras un tiempo prudencial de inactividad, exigiendo nueva autenticación; en nivel ALTO, pasado un tiempo superior se cancelan las sesiones.
    - **mp.eq.3 Protección de dispositivos portátiles**: se trata en la sección de movilidad.
    - **mp.eq.4 Otros dispositivos conectados a la red** (dimensión C): multifunción, multimedia, IoT y dispositivos de invitados o personales (BYOD), con configuración de seguridad que controle el flujo de información.

## Administración centralizada y soporte a usuarios

Con cientos o miles de puestos, la administración se centraliza: identidad y políticas comunes, distribución remota de software, inventario permanente y un punto único de soporte.

- **Directorio y políticas**: **Active Directory** (o Entra ID en la nube) centraliza la autenticación; las políticas de grupo (**GPO**) aplican configuraciones y restricciones por unidades organizativas sin tocar equipo a equipo.
- **Gestión unificada de dispositivos (UEM)**:
    - **Microsoft Configuration Manager** (denominación actual desde la versión 2303; antes SCCM y MECM): despliegue de sistemas operativos, distribución de software, parcheo e inventario en entornos locales.
    - **Microsoft Intune**: gestión desde la nube de PC y móviles; es la vía que Microsoft señala como futuro, con **cogestión** para convivir con Configuration Manager.
    - Alternativas de código abierto para inventario y soporte: **OCS Inventory** y **GLPI**.
- **Inventario y CMDB**: el parque de puestos alimenta la base de datos de gestión de la configuración, ligada a las prácticas ITIL (tema [18](18-gestion-de-los-servicios-tic.md)).
- **Impresión corporativa**: colas de impresión centralizadas sobre equipos multifunción compartidos, con **impresión segura** (*pull printing*: el trabajo se libera al autenticarse el usuario en el dispositivo), cuotas y auditoría; los multifunción son dispositivos de red a securizar (mp.eq.4 del ENS).
- **Soporte a usuarios (CAU / service desk)**: punto único de contacto para incidencias y peticiones, organizado por niveles: **N1** (atención inicial y resolución de incidencias conocidas), **N2** (técnicos de microinformática y sistemas) y **N3** (especialistas o fabricante). Se apoya en herramientas ITSM de tickets, asistencia remota y acuerdos de nivel de servicio (SLA).
    - **Escalado**: funcional (a un nivel con más conocimiento) o jerárquico (a la cadena de mando, por impacto o incumplimiento de plazos).
    - **Métricas habituales**: resolución en primer contacto (FCR), tiempos de primera respuesta y de resolución frente a SLA, y volumen por categorías; la base de conocimiento reduce reincidencias. Las prácticas de gestión de incidencias y peticiones se desarrollan en ITIL (tema [18](18-gestion-de-los-servicios-tic.md)).

### El puesto de trabajo en la Generalitat: PTN y CAU-TIC

Práctica interna de la **DGTIC** para el puesto de trabajo de la Administración de la Generalitat.

- **Servicio de Gestión del Puesto de Trabajo**: estandariza, mantiene y gestiona los dispositivos; sus funciones incluyen el soporte al **CAU-TIC** (centro de atención al usuario TIC), la gestión del material informático y la definición y evolución del puesto normalizado.
- **Puesto de Trabajo Normalizado (PTN)**: configuración estandarizada del sistema operativo y las aplicaciones base definida por la DGTIC para todos los dispositivos gestionados.
    - **Composición**: hardware (unidad central, pantalla, teclado, dispositivo señalador) y software (sistema operativo, paquete ofimático, navegadores, aplicaciones homologadas y servicios de seguridad como el antivirus).
    - **Nomenclatura**: «PC» + código de inventario (sobremesa), «XPC» (sobremesa externo), «PO» (portátil).
    - **Ciclo**: la configuración del PTN se revisa y despliega **anualmente**, durante el primer trimestre.
- **Despliegue de software**: Configuration Manager (MECM) distribuye configuraciones y aplicaciones según el perfil profesional del usuario; la **Botiga de Software** permite al usuario autoinstalarse aplicaciones autorizadas.
- **Actualizaciones (Windows Update for Business con Connected Cache)**: el PC consulta a Microsoft las actualizaciones pendientes y las descarga por orden de preferencia de los equipos de su propia red local, del servidor **Microsoft Connected Cache** o, en último término, de la CDN de Microsoft; una vez descargadas, las comparte con el resto de equipos (optimización de entrega).
- **Seguridad del PTN**: políticas de dominio, antivirus y cortafuegos centralizados, cifrado de disco y actualizaciones de seguridad.

## Virtualización del escritorio: VDI y Remote Desktop Services

En el escritorio virtualizado, el puesto deja de ejecutarse en el dispositivo del usuario y pasa al CPD (tema [44](44-virtualizacion-y-contenedores.md)): al cliente solo viajan la pantalla y las pulsaciones, y el dato nunca abandona el centro de datos.

- **VDI** (*Virtual Desktop Infrastructure*): cada usuario recibe **su propia máquina virtual** de escritorio, alojada en los servidores.
- **RDS** (*Remote Desktop Services*, el antiguo Terminal Services de Windows Server): los usuarios comparten **sesiones** sobre un mismo servidor (Remote Desktop Session Host). Mayor densidad y menor coste que VDI, a cambio de menos aislamiento y personalización; también publica aplicaciones individuales (RemoteApp).
- **DaaS** (*Desktop as a Service*): el escritorio virtual contratado como servicio de nube: **Azure Virtual Desktop** y **Windows 365** (Cloud PC) de Microsoft, o las modalidades cloud de Citrix y Omnissa.

### Componentes de una plataforma VDI

- **Hipervisor**: aloja las máquinas virtuales de escritorio (tema [44](44-virtualizacion-y-contenedores.md)).
- **Broker de conexión**: autentica al usuario, le asigna su escritorio y gestiona los *pools*.
- **Protocolo de visualización**: transporta pantalla, teclado, ratón y periféricos con compresión y tolerancia a la latencia: **RDP** (Microsoft), **HDX/ICA** (Citrix) y **Blast** (Omnissa).
- **Imagen maestra y pools**: los escritorios se clonan de una *golden image*; las actualizaciones se hacen sobre la maestra y se recomponen los clones.
- **Cliente de acceso**: PC o tableta con software cliente, o terminales dedicados (**thin client** y *zero client*), más baratos y longevos.

### Tipos de escritorios virtuales

- **Dedicado (estático)**: el usuario se conecta siempre a la misma máquina virtual. / **Flotante (dinámico)**: se le asigna una VM libre del pool en cada sesión.
- **Persistente**: los cambios del usuario se conservan entre sesiones. / **No persistente**: el escritorio se regenera limpio en cada inicio (aulas, atención al público).

### Ventajas e inconvenientes

- **Ventajas**: administración y seguridad centralizadas (los datos no salen del CPD), despliegue y reversión rápidos desde la imagen maestra, acceso desde cualquier lugar y dispositivo (movilidad y teletrabajo), continuidad y recuperación ante desastres, alargamiento de la vida del hardware cliente y menor consumo energético en el puesto.
- **Inconvenientes**: inversión inicial y complejidad de la plataforma, dependencia total de la red y del CPD (punto único de fallo si no se diseña redundante), sensibilidad a la latencia y limitaciones con gráficos exigentes (mitigables con **vGPU**), licenciamiento adicional y necesidad de dimensionar bien los picos (tormentas de arranque).

### Soluciones actuales

| Solución | Fabricante | Notas |
| --- | --- | --- |
| Citrix Virtual Apps and Desktops / Citrix DaaS | Citrix (Cloud Software Group) | Antes XenDesktop/XenApp; protocolo HDX |
| Omnissa Horizon 8 | Omnissa (la antigua división EUC de VMware, vendida a KKR en 2024) | Protocolo Blast |
| Azure Virtual Desktop y Windows 365 | Microsoft | DaaS sobre Azure; RDS para despliegues locales |
| UDS Enterprise / OpenUDS | Virtual Cable (España) | Broker de conexiones de código abierto, extendido en universidades y administraciones públicas |

## Movilidad y BYOD

El puesto de trabajo ya no es solo el PC de la oficina: portátiles, móviles y tabletas acceden a los servicios corporativos desde cualquier red, y el teletrabajo lo ha convertido en la norma. Eso obliga a decidir de quién es el dispositivo y cómo se gestiona y protege.

- **Modelos de provisión de dispositivos**:
    - **BYOD** (*Bring Your Own Device*): el empleado usa su dispositivo personal para el trabajo.
    - **CYOD** (*Choose Your Own Device*): el empleado elige entre un catálogo de dispositivos corporativos.
    - **COPE** (*Corporate-Owned, Personally Enabled*): corporativo con uso personal permitido.
    - **COBO** (*Corporate-Owned, Business Only*): corporativo de uso exclusivamente profesional.
- **Gestión de la movilidad**:
    - **MDM** (*Mobile Device Management*): gestiona el dispositivo completo: políticas de seguridad, cifrado, inventario, localización y **borrado remoto**.
    - **MAM** (*Mobile Application Management*): gestiona solo las aplicaciones corporativas y sus datos, con **contenedores o perfiles de trabajo** que separan lo personal de lo profesional y permiten el **borrado selectivo**; es el enfoque adecuado para BYOD.
    - **UEM** (*Unified Endpoint Management*): consola única para todos los dispositivos (PC, móviles, tabletas): Microsoft Intune, Omnissa Workspace ONE, Jamf (ecosistema Apple).
- **Riesgos y medidas**: pérdida o robo del dispositivo, redes no confiables, mezcla de datos personales y corporativos y *shadow IT*; se mitigan con cifrado, bloqueo y borrado remotos, autenticación multifactor, contenedores de trabajo y control de acceso a la red.
- **El ENS**: la medida **mp.eq.3, «Protección de dispositivos portátiles»**, exige un **inventario** de portátiles con su responsable identificado y control regular, un procedimiento para **comunicar pérdidas o sustracciones** al servicio de gestión de incidentes, y que las conexiones remotas por redes que no controle la organización limiten la información y los servicios accesibles a los **mínimos imprescindibles**, con autorización previa de los responsables afectados (refuerzos adicionales en categoría ALTA).
- **Teletrabajo**: el acceso remoto se resuelve con **VPN** corporativa o, de forma creciente, con modelos **ZTNA** (*Zero Trust Network Access*: acceso por aplicación con verificación continua de usuario y dispositivo); los escritorios VDI/DaaS son otra vía segura, porque el dato no sale del CPD. En la Generalitat, el teletrabajo del personal se regula en el **Decreto 49/2021** (tema [13](13-funcion-publica-valenciana.md)).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, Esquema Nacional de Seguridad, texto consolidado, última modificación 6 de noviembre de 2024 (Anexo II, familia mp.eq).
- Documentación de Microsoft Learn (Configuration Manager e Intune, Windows Autopilot, Azure Virtual Desktop y Windows 365, optimización de entrega), consulta de julio de 2026.
- Documentación oficial de Citrix, Omnissa y Virtual Cable (UDS Enterprise), consulta de julio de 2026.
