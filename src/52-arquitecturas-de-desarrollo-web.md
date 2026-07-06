# Arquitecturas de desarrollo web

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Arquitectura de Desarrollo en la Web

La arquitectura web define cómo los componentes de una aplicación web se organizan y comunican entre sí.

- **Modelo Cliente-Servidor**:
    - **Cliente**: Navegador web que realiza solicitudes.
    - **Servidor**: Procesa las solicitudes y devuelve respuestas (páginas web, datos).
- **Capas de Arquitectura**:
    - **Presentación**: Interfaz de usuario (front-end).
    - **Lógica de Negocio**: Procesamiento de datos y reglas de negocio (back-end).
    - **Acceso a Datos**: Interacción con bases de datos.

### Desarrollo Web Front-End

Se enfoca en la creación de la interfaz de usuario y experiencia interactiva.

- **Lenguajes Fundamentales**:
    - **HTML**: Estructura y contenido de la página.
    - **CSS**: Estilos y diseño visual.
    - **JavaScript**: Interactividad y comportamiento dinámico.
- **Frameworks y Librerías**:
    - **React**: Biblioteca para construir interfaces de usuario basadas en componentes.
    - **Angular**: Framework completo para aplicaciones web de una sola página (SPA).
    - **Vue.js**: Framework progresivo para la construcción de interfaces de usuario.
- **Herramientas y Tecnologías**:
    - **TypeScript**: Superset de JavaScript que añade tipado estático.
    - **SASS/LESS**: Preprocesadores CSS para facilitar la escritura de estilos.
    - **Webpack**: Empaquetador de módulos para aplicaciones JavaScript.

### Desarrollo Web en Servidor (Back-End) y Conexión a Bases de Datos

Gestiona la lógica del negocio, procesos del servidor y comunicación con bases de datos.

- **Lenguajes de Programación**:
    - **PHP**: Amplio uso en desarrollo web (WordPress, Laravel).
    - **Python**: Frameworks como Django y Flask.
    - **Java**: Uso empresarial con frameworks como Spring.
    - **Node.js**: Entorno para ejecutar JavaScript en el servidor.
    - **Ruby**: Usado con el framework Ruby on Rails.
- **Bases de Datos**:
    - **Relacionales (SQL)**:
        - **MySQL**: Popular y de código abierto.
        - **PostgreSQL**: Avanzado y extensible.
        - **Oracle**: Orientado a empresas.
    - **NoSQL**:
        - **MongoDB**: Basado en documentos.
        - **Redis**: Almacenamiento en memoria clave-valor.
        - **Cassandra**: Altamente escalable.
- **ORM (Object-Relational Mapping)**:
    - **Hibernate (Java)**, **Entity Framework (.NET)**, **Sequelize (Node.js)**.
- **Servidores Web**:
    - **Apache**: Servidor HTTP de código abierto.
    - **Nginx**: Servidor ligero y de alto rendimiento.
- **Servicios y Arquitecturas**:
    - **Microservicios**: Aplicaciones divididas en pequeños servicios independientes.
    - **SOA (Arquitectura Orientada a Servicios)**: Integración de servicios discretos.

### Interconexión con Sistemas y Servicios

Permite la comunicación y el intercambio de datos entre diferentes aplicaciones y sistemas.

- **APIs y Protocolos**:
    - **RESTful APIs**: Arquitectura para servicios web que utiliza HTTP.
    - **SOAP**: Protocolo basado en XML para intercambio de información.
    - **GraphQL**: Lenguaje de consulta para APIs que permite solicitar exactamente lo necesario.
- **Protocolos y Tecnologías de Comunicación**:
    - **HTTP/HTTPS**: Protocolos base para la comunicación web.
    - **WebSockets**: Comunicación bidireccional en tiempo real.
    - **gRPC**: Protocolo de llamada a procedimiento remoto de alto rendimiento.
- **Servicios en la Nube e Integraciones**:
    - **AWS (Amazon Web Services)**: Amplia gama de servicios en la nube.
    - **Microsoft Azure**: Plataforma en la nube para servicios y aplicaciones.
    - **Google Cloud Platform**: Infraestructura y servicios de computación en la nube.
- **Mensajería y Colas**:
    - **RabbitMQ**, **Apache Kafka**: Sistemas para manejar mensajes y eventos.
- **Autenticación y Autorización**:
    - **OAuth2**, **JWT (JSON Web Tokens)**: Estándares para autenticación segura.
    - **LDAP**: Protocolo para acceso a directorios y servicios de autenticación.

### Lenguajes y Herramientas para la Utilización en Redes Globales

Tecnologías y herramientas esenciales para desarrollar aplicaciones escalables y robustas en un entorno global.

- **Estándares Web Modernos**:
    - **HTML5**: Soporte multimedia y nuevas etiquetas semánticas.
    - **CSS3**: Nuevas características como transiciones, transformaciones y animaciones.
    - **ECMAScript 6+ (ES6+)**: Actualizaciones del estándar JavaScript.
- **Control de Versiones y Colaboración**:
    - **Git**: Sistema de control de versiones distribuido.
    - **Plataformas**: **GitHub**, **GitLab**, **Bitbucket** para alojamiento y colaboración en código.
- **Herramientas de Construcción y Automatización**:
    - **npm** y **Yarn**: Gestores de paquetes para JavaScript.
    - **Webpack**, **Parcel**: Empaquetadores de módulos.
    - **Grunt**, **Gulp**: Herramientas para automatizar tareas.
- **Pruebas y Calidad de Código**:
    - **Jest**, **Mocha**: Frameworks de pruebas para JavaScript.
    - **ESLint**, **Prettier**: Herramientas para análisis estático y formateo de código.
- **Seguridad y Rendimiento en Redes**:
    - **SSL/TLS**: Encriptación para comunicaciones seguras.
    - **HTTP/2** y **HTTP/3**: Protocolos para mejorar la eficiencia y velocidad de carga.
    - **CDN (Content Delivery Network)**: Distribución de contenido a nivel global para reducir latencia.
- **Protocolos y Estándares Internacionales**:
    - **UTF-8**: Codificación de caracteres para soporte multilingüe.
    - **ISO/IEC Estándares**: Normas internacionales para seguridad y calidad.
- **Despliegue y Contenedores**:
    - **Docker**: Plataforma para crear y administrar contenedores.
    - **Kubernetes**: Orquestación de contenedores para despliegue escalable.
- **Servicios y Arquitecturas de Red**:
    - **Microservicios**: Para escalabilidad y mantenimiento.
    - **Serverless Computing**: Ejecución de código sin gestión de servidores (AWS Lambda, Azure Functions).
- **Monitoreo y Logística**:
    - **Prometheus**, **Grafana**: Herramientas para monitoreo y visualización.
    - **ELK Stack (Elasticsearch, Logstash, Kibana)**: Análisis y visualización de logs.
