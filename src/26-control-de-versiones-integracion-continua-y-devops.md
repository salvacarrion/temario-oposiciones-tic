# Control de versiones, integración continua y DevOps
## DevOps y CI/CD

DevOps es un conjunto de prácticas que busca integrar los equipos de
desarrollo de software (Dev) y de operaciones de TI (Ops) para acelerar
el ciclo de vida del desarrollo y mejorar la calidad de la entrega. El
objetivo principal de DevOps es fomentar una comunicación fluida,
colaboración y automatización a lo largo del ciclo de desarrollo y
operación del software, promoviendo una cultura de cambio constante y
mejora continua.

**Principios Fundamentales de DevOps**

Los principios de DevOps incluyen:

- **Automatización**: Uso extensivo de herramientas que facilitan la
  gestión, integración, pruebas y despliegue.

- **Colaboración**: Facilitar el trabajo conjunto y la comunicación
  entre los equipos de desarrollo y operaciones.

- **Integración Continua**: Integrar cambios en el código de manera
  frecuente para detectar errores pronto.

- **Entrega Continua**: Automatización del flujo de trabajo para lanzar
  nuevas versiones de software de manera regular y confiable.

DevOps se basa en metodologías ágiles y se centra en el cambio cultural
dentro de la organización.

**Cadena de Herramientas DevOps**

La cadena de herramientas DevOps abarca cada fase del ciclo de vida del
software, apoyando la automatización y facilitando la colaboración:

- **Planificación**: Define requisitos y valores empresariales
  (Herramientas: JIRA, Git).

- **Codificación**: Diseño y desarrollo del código (Herramientas:
  GitHub, GitLab, Bitbucket).

- **Compilación**: Gestión de versiones y compilación (Herramientas:
  Docker, Maven, Puppet).

- **Prueba**: Pruebas continuas para asegurar calidad (Herramientas:
  JUnit, Selenium).

- **Puesta en marcha**: Automatización de tareas de despliegue
  (Herramientas: Jenkins, Kubernetes).

- **Funcionamiento**: Gestión del software en producción (Herramientas:
  Ansible, Chef).

- **Supervisión**: Detección y solución de problemas (Herramientas:
  Grafana, Splunk).

**Ciclo de Vida de DevOps: Prácticas Clave**

El ciclo de vida de DevOps incluye varias prácticas continuas que ayudan
a mejorar la agilidad y la calidad:

- **Desarrollo Continuo**: Incluye planificación y codificación.

- **Integración Continua (CI)**: Integración frecuente de código,
  verificada automáticamente con pruebas.

- **Testing Continuo**: Ejecución constante de pruebas para detectar
  errores de manera temprana.

- **Despliegue Continuo (CD)**: Automatiza el lanzamiento de código en
  producción.

- **Monitorización Continua**: Supervisión constante del software en
  producción.

- **Feedback Continuo**: Retroalimentación inmediata sobre problemas en
  producción.

**Integración Continua (Continuous Integration, CI)**

La integración continua es una práctica en la que los desarrolladores
integran su trabajo frecuentemente en un repositorio central (por
ejemplo, rama “develop”). Cada integración se verifica automáticamente a
través de pruebas unitarias y de integración, permitiendo identificar
errores cuanto antes.

**Componentes de CI**:

- **Compilación automática** del código.

- **Pruebas automatizadas** de cada integración.

- **Notificaciones** sobre el estado de las pruebas.

**Entrega Continua (Continuous Delivery, CD)**

La entrega continua asegura que el software esté listo para ser lanzado
en producción en cualquier momento. En esta práctica, el código pasa por
una serie de pruebas y empaquetado de forma automatizada, aunque la
decisión de desplegar puede requerir intervención humana.

**Despliegue Continuo (Continuous Deployment, CD)**

El despliegue continuo lleva la automatización un paso más allá,
permitiendo que el código se despliegue automáticamente en producción
tras cada integración sin intervención humana. El proceso solo se
interrumpe si fallan las pruebas automáticas.

**CI/CD: Integración y Entrega/Despliegue Continuo**

El término CI/CD hace referencia a la combinación de prácticas de
integración continua, entrega continua y despliegue continuo,
dependiendo del nivel de automatización deseado por el equipo o la
organización. Implementar CI/CD optimiza el flujo de trabajo y asegura
una entrega de software confiable y rápida.

**Ciclo de Despliegue de Aplicaciones**

El ciclo de despliegue puede variar según el autor, pero generalmente
sigue una de estas dos estructuras:

- **Modelo A**: Requerimientos → Diseño → Implementación → Verificación
  → Mantenimiento.

- **Modelo B**: Planificación → Requisitos → Diseño y Prototipado →
  Desarrollo → Pruebas → Despliegue → Operaciones y Mantenimiento.

**Herramienta Destacada en CI/CD: Jenkins**

Jenkins es un servidor de integración continua de código abierto escrito
en Java, ampliamente utilizado para automatizar el desarrollo, las
pruebas y el despliegue. Sus características clave incluyen:

- **Instalación multiplataforma**: Compatible con Windows, MacOS y
  Linux.

- **Configuración**: Realizada a través de una interfaz web.

- **Integración**: Soporta una gran variedad de plugins (JIRA, Slack,
  Maven, etc.).

- **Arquitectura Master-Slave**: Escalable para distribuir el
  procesamiento en múltiples máquinas.
