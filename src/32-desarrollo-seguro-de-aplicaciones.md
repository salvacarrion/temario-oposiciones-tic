# Desarrollo seguro de aplicaciones

La seguridad de una aplicación no puede añadirse al final: debe integrarse en todas las fases del ciclo de vida del software. El desarrollo seguro combina un proceso (el ciclo de desarrollo seguro), unos marcos de referencia (ENS y guías CCN, proyectos OWASP, catálogos MITRE) y unas técnicas de verificación (análisis estático y dinámico, pruebas de intrusión) que permiten prevenir, detectar y corregir vulnerabilidades antes de que lleguen a producción.

## El ciclo de desarrollo seguro y las buenas prácticas del CCN

El **ciclo de desarrollo seguro** (SSDLC, *Secure Software Development Life Cycle*) incorpora actividades de seguridad en cada fase del ciclo de vida, en lugar de tratarla como una comprobación final. La idea rectora es el desplazamiento a la izquierda (*shift left*): cuanto antes se detecta un defecto de seguridad, menor es su coste de corrección. Se apoya en dos principios generales:

- **Seguridad desde el diseño (*security by design*)**: la seguridad es un requisito desde la concepción del sistema, no un parche posterior.
- **Seguridad por defecto (*security by default*)**: la configuración inicial del producto debe ser la más restrictiva, de modo que el sistema sea seguro sin intervención del usuario.

**Actividades de seguridad por fase**:

- **Requisitos**: especificación de requisitos de seguridad junto a los funcionales; identificación de requisitos legales (protección de datos, ENS); casos de abuso.
- **Diseño**: modelado de amenazas, revisión de la arquitectura y reducción de la superficie de ataque.
- **Implementación**: normas de codificación segura, revisión de código entre pares y control de las dependencias de terceros.
- **Verificación**: análisis SAST/DAST, análisis de composición y pruebas de intrusión (ver el último apartado).
- **Despliegue**: configuración segura y bastionado de la plataforma; separación de entornos; procedimiento estandarizado de puesta en producción.
- **Mantenimiento**: gestión de vulnerabilidades, aplicación de parches, revisiones periódicas y retirada segura.

**Modelado de amenazas**: identificación y evaluación sistemática de las amenazas sobre el diseño del sistema, para decidir contramedidas antes de programar. El modelo de referencia es **STRIDE** (Microsoft), que cataloga seis tipos de amenaza y la propiedad de seguridad que vulnera cada uno:

| Amenaza | Propiedad vulnerada |
| --- | --- |
| *Spoofing* (suplantación) | Autenticidad |
| *Tampering* (manipulación) | Integridad |
| *Repudiation* (repudio) | No repudio |
| *Information disclosure* (revelación) | Confidencialidad |
| *Denial of service* (denegación de servicio) | Disponibilidad |
| *Elevation of privilege* (elevación de privilegios) | Autorización |

Para priorizar las amenazas identificadas se usan modelos de puntuación como **DREAD** (daño, reproducibilidad, explotabilidad, usuarios afectados, descubribilidad).

**Principios de diseño seguro** (formulados por Saltzer y Schroeder, 1975, y ampliados por la práctica):

- **Mínimo privilegio**: otorgar solo los permisos imprescindibles para cada función.
- **Separación de funciones**: evitar que una misma entidad acumule funciones críticas.
- **Defensa en profundidad**: superponer múltiples capas de seguridad independientes.
- **Fallo seguro**: ante un error, el sistema debe quedar en estado seguro (denegar por defecto).
- **Economía de mecanismo**: diseños simples y pequeños son más fáciles de verificar.
- **Mediación completa**: validar todas las solicitudes de acceso, sin excepciones.
- **Diseño abierto**: la seguridad no debe depender del secreto del diseño (principio de Kerckhoffs).
- **Mínimo mecanismo común**: minimizar los componentes compartidos entre usuarios.
- **Aceptabilidad psicológica**: los mecanismos de seguridad deben ser usables o se eludirán.
- **Eslabón más débil**: la seguridad del conjunto es la de su punto más vulnerable.
- **Reutilización de componentes probados**: preferir soluciones contrastadas a desarrollos propios.

**Marcos de referencia del desarrollo seguro**:

- **NIST SSDF** (*Secure Software Development Framework*, SP 800-218 v1.1, 2022): prácticas agrupadas en preparar la organización, proteger el software, producir software bien asegurado y responder a las vulnerabilidades.
- **Microsoft SDL** (*Security Development Lifecycle*): pionero de los SSDLC corporativos.
- **OWASP SAMM** (*Software Assurance Maturity Model*, v2, 2020): modelo de madurez para evaluar y mejorar el proceso de desarrollo seguro de una organización.

### El desarrollo seguro en el ENS (RD 311/2022)

**Texto consolidado a 6 de noviembre de 2024.**

En el sector público, las buenas prácticas de desarrollo seguro son obligación normativa: el Anexo II del **Real Decreto 311/2022** (Esquema Nacional de Seguridad) las recoge en el grupo de medidas de protección de las aplicaciones informáticas (**mp.sw**), y el CCN las desarrolla en sus guías de la serie **CCN-STIC 800**, en particular la **CCN-STIC 812, Seguridad en entornos y aplicaciones web** (ed. junio 2023, adaptada al RD 311/2022).

- **mp.sw.1 Desarrollo de aplicaciones**: no aplica en categoría **BÁSICA**; en **MEDIA** y **ALTA** se exige con los refuerzos **R1 a R4**. Requisito base: el desarrollo se realizará sobre un **sistema diferente y separado del de producción**, sin herramientas ni datos de desarrollo en producción, ni datos de producción en desarrollo. Refuerzos:
    - **R1 Mínimo privilegio**: las aplicaciones accederán solo a los recursos imprescindibles y con los privilegios indispensables.
    - **R2 Metodología de desarrollo seguro**: aplicar una metodología reconocida que considere la seguridad en todo el ciclo de vida, incluya normas de programación segura (control de asignación y liberación de memoria, desbordamiento), trate los datos de prueba y permita la inspección del código fuente.
    - **R3 Seguridad desde el diseño**: los mecanismos de identificación y autenticación, la protección de la información tratada y las pistas de auditoría serán parte integral del diseño.
    - **R4 Datos de pruebas**: preferiblemente no se probará con datos reales; si es necesario, se garantizará su nivel de seguridad.
    - **R5 Lista de componentes software**: relación formal y actualizada de los componentes de terceros (identificación, fabricante y versión), con histórico por versiones. Es el equivalente ENS del SBOM.
- **mp.sw.2 Aceptación y puesta en servicio**: aplica desde categoría **BÁSICA** (MEDIA y ALTA añaden **R1**). Antes de pasar a producción se comprobará que se cumplen los **criterios de aceptación en materia de seguridad** y que no se deteriora la seguridad de otros componentes del servicio. Refuerzos: **R1**, pruebas en un entorno aislado (preproducción); **R2**, auditoría de código fuente.

## Seguridad en aplicaciones web: OWASP

**OWASP** (*Open Worldwide Application Security Project*) es una fundación sin ánimo de lucro dedicada a mejorar la seguridad del software. Sus proyectos son la referencia de facto en seguridad de aplicaciones web: el **Top 10** (concienciación sobre riesgos), la **WSTG** (guía de pruebas), el **ASVS** (estándar de verificación), **SAMM** (madurez del proceso) y herramientas como **ZAP**.

### OWASP Top 10:2025

El **OWASP Top 10** es la lista de consenso de los riesgos de seguridad más críticos en aplicaciones web, elaborada a partir de datos de pruebas reales y encuestas a la comunidad. La edición vigente es el **Top 10:2025** (la octava, publicada entre noviembre de 2025 y enero de 2026), que sustituye a la de 2021:

| Código | Riesgo | Idea clave |
| --- | --- | --- |
| **A01:2025** | *Broken Access Control* | Fallos en la autorización (acceso a recursos ajenos, elevación de privilegios). Repite como 1.er puesto y absorbe la antigua SSRF. |
| **A02:2025** | *Security Misconfiguration* | Configuraciones inseguras, valores por defecto, servicios innecesarios. Sube del 5.º al 2.º puesto. |
| **A03:2025** | *Software Supply Chain Failures* | Nueva: compromisos de la cadena de suministro (dependencias, sistemas de *build*, distribución). Amplía la antigua «componentes vulnerables y obsoletos». |
| **A04:2025** | *Cryptographic Failures* | Criptografía ausente, débil o mal aplicada que expone datos sensibles. |
| **A05:2025** | *Injection* | Datos no confiables interpretados como código: SQL, LDAP, comandos del sistema; incluye XSS desde 2021. |
| **A06:2025** | *Insecure Design* | Fallos de diseño y arquitectura, no de implementación. |
| **A07:2025** | *Authentication Failures* | Autenticación y gestión de credenciales deficientes (renombrada). |
| **A08:2025** | *Software or Data Integrity Failures* | No verificar la integridad de código, actualizaciones o datos (deserialización insegura). |
| **A09:2025** | *Security Logging & Alerting Failures* | Registro y, sobre todo, alertado insuficientes para detectar y responder a ataques (renombrada). |
| **A10:2025** | *Mishandling of Exceptional Conditions* | Nueva: tratamiento indebido de errores y condiciones anómalas, errores lógicos, fallo en abierto (*fail open*). |

**Principales ataques a aplicaciones web** que materializan estos riesgos:

- **Inyección SQL**: inserción de sentencias SQL a través de entradas no validadas, con acceso o manipulación de la base de datos.
- **Cross-site scripting (XSS)**: inyección de scripts que se ejecutan en el navegador de la víctima; variantes reflejada, almacenada y basada en DOM.
- **Cross-site request forgery (CSRF)**: el atacante induce al navegador autenticado de la víctima a ejecutar acciones no deseadas.
- **Secuestro de sesión (*session hijacking*)**: obtención del identificador de sesión de la víctima; la variante *session fixation* fija de antemano la sesión que la víctima usará.
- **Server-side request forgery (SSRF)**: se fuerza al servidor a realizar peticiones a destinos internos no previstos.
- **Desbordamiento de búfer (*buffer overflow*)**: escritura fuera de los límites de memoria reservada que puede alterar el flujo del programa y ejecutar código malicioso (*shellcode*); propio de código nativo.

### La guía de pruebas WSTG

La **OWASP Web Security Testing Guide (WSTG) v4.2** (diciembre de 2020) es el marco de referencia para planificar y ejecutar pruebas de seguridad de aplicaciones y servicios web. Distingue dos fases:

- **Pruebas pasivas**: se examina el funcionamiento y la lógica de la aplicación (navegación, documentación, respuestas) para comprender su superficie de ataque, sin atacarla.
- **Pruebas activas**: se ejecutan las pruebas propiamente dichas sobre los vectores identificados.

Las pruebas activas se organizan en **12 categorías** (más de **100 pruebas**, con identificadores del tipo WSTG-INFO-01): recopilación de información (INFO), gestión de la configuración y el despliegue (CONF), gestión de identidades (IDNT), autenticación (ATHN), autorización (ATHZ), gestión de sesiones (SESS), validación de entradas (INPV), tratamiento de errores (ERRH), criptografía débil (CRYP), lógica de negocio (BUSL), lado del cliente (CLNT) y pruebas de API (APIT, nueva en la v4.2).

### ASVS y WAF

- **OWASP ASVS** (*Application Security Verification Standard*, v5.0.0, mayo de 2025): estándar de requisitos verificables de seguridad de aplicaciones (unos 350 requisitos en 17 capítulos), con **tres niveles de verificación** (L1 a L3) según la criticidad de la aplicación. Sirve como base contractual y de auditoría: el Top 10 conciencia, el ASVS verifica.
- **WAF (*Web Application Firewall*)**: cortafuegos de capa de aplicación que filtra el tráfico HTTP/HTTPS frente a ataques web conocidos (inyección, XSS). Es una medida complementaria: mitiga, pero no sustituye al desarrollo seguro.

## Marcos MITRE: CVE y CWE

La corporación **MITRE** mantiene los catálogos públicos que dan a la comunidad un lenguaje común para identificar vulnerabilidades, debilidades y comportamientos de los atacantes. Son la base de la gestión de vulnerabilidades y de las herramientas de análisis.

- **CVE (*Common Vulnerabilities and Exposures*)**: registro público de vulnerabilidades concretas de productos, cada una con un identificador único **CVE-AAAA-NNNNN** asignado por las entidades autorizadas (**CNA**, *CVE Numbering Authorities*). Ejemplo: **CVE-2021-44228** (*Log4Shell*, ejecución remota de código en la librería Log4j). La **NVD** (*National Vulnerability Database*, del NIST) enriquece cada registro con métricas de severidad y referencias.
- **CVSS (*Common Vulnerability Scoring System*)**: métrica estándar de severidad de vulnerabilidades, mantenida por **FIRST** (no por MITRE); versión vigente **CVSS v4.0** (2023). Puntúa de 0 a 10: **baja** (0,1-3,9), **media** (4,0-6,9), **alta** (7,0-8,9) y **crítica** (9,0-10,0).
- **CWE (*Common Weakness Enumeration*)**: catálogo de los **tipos** de debilidad del software (la causa raíz, no el caso concreto): **CWE-89** (inyección SQL), **CWE-79** (XSS), **CWE-787** (escritura fuera de límites). Cada CVE se clasifica según el CWE que lo origina.
- **CWE Top 25**: lista anual (MITRE con CISA) de las debilidades más peligrosas. La edición **2025** (diciembre de 2025, sobre 39 080 registros CVE) encabezada por **CWE-79 (XSS)**, **CWE-89 (inyección SQL)**, **CWE-352 (CSRF)**, CWE-862 (falta de autorización) y CWE-787 (escritura fuera de límites).
- **CAPEC** (*Common Attack Pattern Enumeration and Classification*): catálogo de patrones de ataque conocidos, complementario del CWE.
- **MITRE ATT&CK**: base de conocimiento de **tácticas y técnicas** de adversarios observadas en el mundo real, organizada en matrices (Enterprise, Mobile, ICS); se usa para modelar amenazas, evaluar defensas y clasificar incidentes. La antigua matriz **PRE-ATT&CK se retiró en octubre de 2020**: su ámbito se integró en la matriz Enterprise como las tácticas de reconocimiento (*Reconnaissance*) y desarrollo de recursos (*Resource Development*).

## Técnicas de análisis: SAST, DAST y pruebas de intrusión

La verificación de la seguridad combina análisis automatizados, integrados en el ciclo de desarrollo, con pruebas manuales especializadas. En un enfoque **DevSecOps**, los análisis se ejecutan de forma continua en el *pipeline* de integración y entrega (véase el tema de control de versiones, integración continua y DevOps).

| Técnica | Qué analiza | Enfoque | Herramientas |
| --- | --- | --- | --- |
| **SAST** (*Static Application Security Testing*) | El código fuente, *bytecode* o binario, sin ejecutarlo | Caja blanca; desde las primeras fases | SonarQube, Fortify |
| **DAST** (*Dynamic Application Security Testing*) | La aplicación en ejecución, desde el exterior | Caja negra; sobre entornos de prueba | OWASP ZAP, Burp Suite, Acunetix |
| **IAST** (*Interactive Application Security Testing*) | La aplicación instrumentada desde dentro, durante las pruebas funcionales | Caja gris | Contrast Security |
| **SCA** (*Software Composition Analysis*) | Las dependencias de terceros: CVE conocidos y licencias | Continuo | OWASP Dependency-Check, Dependency-Track |

- **SBOM (*Software Bill of Materials*)**: inventario formal de los componentes de un software (formatos estándar **SPDX** y **CycloneDX**). Es el insumo del análisis SCA y responde tanto al riesgo de cadena de suministro (A03:2025) como al refuerzo R5 de mp.sw.1 del ENS.
- **RASP (*Runtime Application Self-Protection*)**: protección embebida en la propia aplicación que detecta y bloquea ataques en tiempo de ejecución.

**Pruebas de intrusión (*pentesting*)**: simulación controlada y autorizada de ataques reales para descubrir y explotar vulnerabilidades, evaluando su impacto efectivo.

- **Enfoques según la información disponible**: **caja negra** (sin información previa, como un atacante externo), **caja gris** (información parcial, por ejemplo credenciales de usuario) y **caja blanca** (acceso completo a código y arquitectura).
- **Fases habituales**: reconocimiento, enumeración y análisis de vulnerabilidades, explotación, post-explotación y elaboración del informe.
- **Metodologías**: la **WSTG** para aplicaciones web; PTES y OSSTMM como marcos generales de pruebas de intrusión.
- **Informe de resultados** (estructura de la WSTG): **informe ejecutivo** (visión no técnica de los resultados), **informe de pruebas** (alcance, pruebas realizadas y limitaciones) e **informe de hallazgos** (problemas encontrados, evidencias y recomendaciones de mitigación).

## Fuentes {.unnumbered .unlisted}

- Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (texto consolidado, última modificación 6 de noviembre de 2024), Anexo II, medidas mp.sw.
- OWASP Top 10:2025 (owasp.org/Top10/2025, consultado el 13 de julio de 2026).
- OWASP Web Security Testing Guide v4.2 (diciembre de 2020).
- OWASP Application Security Verification Standard v5.0.0 (mayo de 2025).
- CCN-STIC 812, Seguridad en entornos y aplicaciones web (ed. junio 2023); referenciada por edición, verificada en ccn-cert.cni.es en julio de 2026.
- MITRE: cve.org, cwe.mitre.org (CWE Top 25, ed. diciembre de 2025) y attack.mitre.org, consultados el 13 de julio de 2026.
- NIST SP 800-218, Secure Software Development Framework v1.1 (febrero de 2022).
