# Control de versiones, integración continua y DevOps

Este tema recorre la cadena que lleva el código desde el commit hasta la producción: el control de versiones con Git y sus estrategias de ramas, la automatización CI/CD, la cultura DevOps (y su extensión de seguridad, DevSecOps) y la gestión de la configuración que da soporte a todo el ciclo.

## Control de versiones: Git y estrategias de ramas

Un **sistema de control de versiones (VCS)** registra la historia de cambios de un conjunto de ficheros: permite trabajar en paralelo, comparar y recuperar versiones anteriores y saber quién cambió qué y cuándo. Se distinguen dos arquitecturas:

- **Centralizados (CVCS)**: un único repositorio en un servidor central del que los desarrolladores obtienen copias de trabajo (CVS, **Subversion/SVN**). Requieren conexión para casi toda operación y el servidor es un punto único de fallo.
- **Distribuidos (DVCS)**: cada clon es un repositorio completo con todo el historial (**Git**, Mercurial). Las operaciones son locales y rápidas y se puede trabajar sin conexión, sincronizando después con los remotos.

### Git

**Git** fue creado por **Linus Torvalds en 2005** para el desarrollo del núcleo Linux y es hoy el estándar de facto. Almacena instantáneas (*snapshots*) del proyecto, identifica cada versión con un hash criptográfico y hace que crear y fusionar ramas sea barato y rápido.

- **Las tres áreas**: el **directorio de trabajo** (ficheros que se editan), el **área de preparación** (*staging* o índice, donde se selecciona qué entrará en la próxima confirmación) y el **repositorio** (la base de datos de commits en `.git`).
- **Conceptos clave**: **commit** (instantánea confirmada con autor, fecha y mensaje), **rama** (puntero móvil a un commit; `HEAD` señala la rama activa), **tag** (etiqueta fija sobre un commit, usada para versiones) y **remoto** (repositorio en red, habitualmente `origin`).
- **Integración de cambios**: **merge** fusiona dos ramas creando, si hay divergencia, un commit de fusión (o avanzando el puntero sin más: *fast-forward*); **rebase** reaplica los commits propios sobre otra base y produce un historial lineal, pero no debe usarse sobre historia ya publicada. Si ambas ramas tocan las mismas líneas se produce un **conflicto** que se resuelve a mano.

Flujo básico de trabajo:

```bash
git clone https://git.example.org/gva/expedientes.git
git switch -c feature/busqueda        # crea la rama de trabajo
git add . && git commit -m "Añade búsqueda por NIF"
git push -u origin feature/busqueda   # publica la rama
git switch main && git pull           # actualiza la rama principal
git merge feature/busqueda            # integra (o vía pull request)
git tag -a v1.2.0 -m "Versión 1.2.0"
```

### Estrategias de ramas

La estrategia de ramas define cómo se organiza el trabajo paralelo y cómo llega a producción:

- **Git Flow** (Driessen, **2010**): dos ramas permanentes, **main** (producción) y **develop** (integración), y tres tipos de ramas de apoyo: **feature/** (nacen y mueren en develop), **release/** (estabilización de una versión) y **hotfix/** (corrección urgente desde main). Ordenado para versiones planificadas; demasiado pesado para entrega continua.
- **GitHub Flow**: una única rama principal siempre desplegable y ramas de funcionalidad de vida corta que se integran mediante **pull request**; se despliega tras fusionar. Simple y orientado al despliegue continuo.
- **GitLab Flow**: variante que añade ramas de entorno (producción, preproducción) o de versión para controlar cuándo llega cada cambio a cada entorno.
- **Trunk-based development**: todo el equipo integra en el tronco (main) al menos a diario, con ramas de vida muy corta; exige CI sólida y *feature flags*. Es la práctica que los informes DORA asocian al alto rendimiento.
- **Pull/merge requests**: petición de integración que dispara la **revisión de código** por pares y las comprobaciones automáticas antes de fusionar; es la base de la colaboración en las plataformas **GitHub, GitLab y Bitbucket**.

## Integración, entrega y despliegue continuos (CI/CD)

CI/CD automatiza el camino del código desde el commit hasta la producción mediante un pipeline que compila, prueba y despliega cada cambio. Los tres términos marcan grados crecientes de automatización:

- **Integración continua (CI)**: los desarrolladores integran su trabajo en la rama compartida de forma frecuente (al menos diaria); cada integración dispara automáticamente la **compilación** y las **pruebas**, con **notificación** inmediata del resultado. Detecta los errores de integración cuanto antes.
- **Entrega continua (*continuous delivery*)**: el software está **siempre listo para desplegar**: cada cambio que supera el pipeline produce un artefacto desplegable, pero el paso a producción es una **decisión manual**.
- **Despliegue continuo (*continuous deployment*)**: un paso más allá: cada cambio que supera todas las pruebas se despliega en producción **automáticamente**, sin intervención humana; el proceso solo se detiene si falla el pipeline.

### El pipeline

Etapas típicas de un pipeline CI/CD:

1. **Commit**: un push o pull request dispara el pipeline.
2. **Construcción**: compilación y empaquetado del artefacto (JAR, imagen de contenedor).
3. **Pruebas**: unitarias y de integración; suites más lentas (aceptación, rendimiento) en etapas posteriores.
4. **Análisis de calidad**: análisis estático y quality gates (SonarQube).
5. **Publicación**: el artefacto versionado se sube a un repositorio (Nexus, Artifactory, registro de contenedores).
6. **Despliegue por entornos**: desarrollo, preproducción y producción, con promoción del **mismo artefacto** entre entornos.

El propio pipeline se define como código versionado junto a la aplicación (*pipeline as code*: `Jenkinsfile`, `.gitlab-ci.yml`, workflows YAML de GitHub Actions).

### Estrategias de despliegue

- **Recreate (big bang)**: se detiene la versión antigua y se sustituye por la nueva; implica ventana de corte.
- **Rolling**: sustitución gradual instancia a instancia, sin parada total del servicio.
- **Blue-green**: dos entornos idénticos; se despliega en el inactivo y se **conmuta el tráfico** de golpe; la vuelta atrás es inmediata (reconmutar).
- **Canary**: la nueva versión se libera primero a un **porcentaje pequeño** de usuarios y se amplía gradualmente si las métricas acompañan.
- **Feature flags**: la funcionalidad se activa o desactiva por configuración sin redesplegar; separa el despliegue técnico del lanzamiento funcional.

### Herramientas

- **Jenkins**: servidor CI/CD de código abierto escrito en Java; se configura vía web, tiene un ecosistema enorme de plugins y escala con su arquitectura **controller/agent** (denominación que sustituyó a la antigua «master/slave» en 2020) para repartir las ejecuciones entre nodos.
- **GitHub Actions**: workflows YAML integrados en GitHub, ejecutados en *runners* hospedados o propios.
- **GitLab CI/CD**: pipeline nativo de GitLab definido en `.gitlab-ci.yml`.
- Otros: Azure DevOps Pipelines, Bitbucket Pipelines, Tekton, Argo CD (GitOps).

## DevOps y DevSecOps

**DevOps** es un movimiento cultural y un conjunto de prácticas que integra los equipos de desarrollo (Dev) y operaciones (Ops) para acortar el ciclo de vida del software y entregar valor de forma continua y fiable. El término nace en **2009** (Patrick Debois, primeras *devopsdays*). Se apoya en las metodologías ágiles y pone el acento en el cambio cultural: comunicación, responsabilidad compartida («*you build it, you run it*») y automatización extremo a extremo. Su ciclo se representa como un **bucle infinito**: planificar, codificar, construir y probar (Dev); liberar, desplegar, operar y monitorizar (Ops), con realimentación constante hacia el principio.

- **Modelo CALMS**: **C**ultura (colaboración sin silos), **A**utomatización (del pipeline completo), **L**ean (flujo de valor, eliminar desperdicio), **M**edición (decisiones basadas en datos) y **S**haring (compartir conocimiento y responsabilidad).
- **Las tres vías** (*The DevOps Handbook*): optimizar el **flujo** de Dev a Ops, amplificar la **realimentación** de Ops a Dev y crear una cultura de **experimentación y aprendizaje** continuos.
- **Métricas DORA** (informes *State of DevOps*; *Accelerate*, 2018), las cuatro métricas clave del rendimiento de entrega:
    1. **Frecuencia de despliegue** en producción.
    2. **Lead time de cambios**: tiempo del commit a producción.
    3. **Tasa de fallo de los cambios**: porcentaje de despliegues que causan incidencias.
    4. **Tiempo de restauración del servicio (MTTR)** tras un fallo.
- **Infraestructura como código (IaC)**: la infraestructura se describe en ficheros declarativos versionados en Git y se aprovisiona automáticamente (**Terraform**, **Ansible**), lo que hace los entornos reproducibles y auditables (ver temas 44 y 51).
- **SRE** (*Site Reliability Engineering*, Google): aplica ingeniería de software a la operación; define objetivos de nivel de servicio (**SLO**) sobre indicadores (**SLI**) y gestiona el riesgo con el **presupuesto de error**.

### Cadena de herramientas DevOps

| Fase | Propósito | Herramientas habituales |
| --- | --- | --- |
| Planificación | Requisitos, backlog, seguimiento | Jira, Confluence |
| Código | Desarrollo y control de versiones | Git (GitHub, GitLab, Bitbucket) |
| Construcción | Compilación y empaquetado | Maven, Gradle, Docker |
| Pruebas | Pruebas automatizadas | JUnit, Selenium |
| Liberación y despliegue | Pipeline CI/CD | Jenkins, GitHub Actions, GitLab CI/CD |
| Configuración y operación | IaC, orquestación | Ansible, Puppet, Terraform, Kubernetes |
| Monitorización | Observabilidad, alertas | Prometheus, Grafana, ELK, Splunk |

### DevSecOps

**DevSecOps** integra la seguridad en todo el ciclo DevOps en lugar de dejarla como comprobación final: es el enfoque ***shift-left*** (desplazar la seguridad a la izquierda, hacia las fases tempranas), con la seguridad como **responsabilidad compartida** de todo el equipo. En la práctica añade controles automáticos al pipeline:

- **SAST**: análisis estático del código fuente en cada commit.
- **SCA**: análisis de composición (vulnerabilidades de dependencias y licencias).
- **DAST**: pruebas dinámicas contra la aplicación desplegada en entornos de prueba.
- **Escaneo de secretos** (credenciales en el repositorio) y de **imágenes de contenedor** antes de publicarlas.

El detalle de estas técnicas y del ciclo de desarrollo seguro se estudia en el tema 32.

## Gestión de la configuración y CMDB

La **gestión de la configuración** es la disciplina que identifica y controla los elementos que componen un sistema y sus versiones, manteniendo su integridad y trazabilidad durante todo el ciclo de vida. Tiene una vertiente de ingeniería del software (SCM) y otra de gestión de servicios (ITIL).

### Gestión de la configuración del software (SCM)

Según el estándar **IEEE 828-2012**, sus actividades son:

- **Identificación de la configuración**: determinar los **elementos de configuración** (código, documentos, esquemas, herramientas) y su esquema de versionado.
- **Control de cambios**: toda modificación de una línea base sigue un proceso formal de solicitud, evaluación de impacto y aprobación por un **comité de control de cambios (CCB)**.
- **Informes de estado**: registrar y comunicar el estado de los elementos y de las solicitudes de cambio.
- **Auditorías de configuración**: verificar que lo entregado se corresponde con lo especificado (auditoría funcional) y que los elementos son completos y correctos (auditoría física).
- **Líneas base**: configuraciones aprobadas que sirven de referencia estable (por ejemplo, la línea base de una release); solo cambian mediante el control formal.

El control de versiones (Git) es la herramienta que materializa la SCM del código; los pipelines y la IaC extienden ese control a los artefactos y a los entornos.

### CMDB y CMS (ITIL)

En la gestión de servicios TI (**ITIL 4**, práctica de gestión de la configuración del servicio):

- **Elemento de configuración (CI)**: cualquier componente que deba gestionarse para entregar un servicio (servidores, aplicaciones, licencias, documentación, el propio servicio).
- **CMDB** (*Configuration Management Database*): base de datos que almacena los CI con sus atributos y, sobre todo, sus **relaciones** (qué depende de qué), lo que permite el análisis de impacto de cambios e incidencias.
- **CMS** (*Configuration Management System*): conjunto de herramientas, datos e información que integra una o varias CMDB con otras fuentes (descubrimiento automático, inventario).

La CMDB da soporte a las prácticas de incidencias, problemas y cambios (ver tema 18). En entornos modernos se alimenta con **descubrimiento automático** y converge con el enfoque **GitOps**: el repositorio Git como única fuente de verdad del estado deseado de aplicaciones e infraestructura, que herramientas como Argo CD reconcilian continuamente con el estado real.

## Fuentes {.unnumbered .unlisted}

- Chacon, S. y Straub, B., *Pro Git*, 2.ª ed., Apress, 2014 (git-scm.com).
- Driessen, V., «A successful Git branching model» (Git Flow), nvie.com, 2010.
- Humble, J. y Farley, D., *Continuous Delivery*, Addison-Wesley, 2010.
- Kim, G., Humble, J., Debois, P. y Willis, J., *The DevOps Handbook*, 2.ª ed., IT Revolution, 2021.
- Forsgren, N., Humble, J. y Kim, G., *Accelerate*, IT Revolution, 2018 (métricas DORA).
- IEEE 828-2012, *Standard for Configuration Management in Systems and Software Engineering*.
- ITIL 4 Foundation, AXELOS/PeopleCert, 2019 (gestión de la configuración del servicio).
