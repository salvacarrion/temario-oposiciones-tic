# Redes de emergencia

## Redes de emergencia

Las **redes de emergencia**, o **PPDR (Public Protection & Disaster Recovery),** son sistemas de comunicación diseñados para ser utilizados en situaciones de emergencia o crisis.

**Definición:** *"Conjunto de nodos y enlaces que proporcionan conexiones entre dos o más puntos definidos para intercambiar información, ya sea mediante un canal de voz, vídeo y/o datos, con el objeto de gestionar operaciones de socorro o alertar catástrofes".*

### Objetivo:

Garantizar la comunicación efectiva entre los diferentes servicios de emergencia, como bomberos, policías y servicios médicos.

### Conceptos Clave

- **Redes PMR (Private Mobile Radio):** Son redes de comunicaciones privadas que utilizan dispositivos móviles equipados con esta tecnología.
    - Estas redes no están conectadas a la red pública y han sido ampliamente utilizadas en entornos de emergencia, aunque son consideradas una tecnología más antigua.
- **Trunking:** Es un sistema moderno de comunicación bidireccional por radio que permite a múltiples usuarios compartir frecuencias de comunicación de forma eficiente.
    - Este enfoque optimiza el uso del espectro de radiofrecuencia, proporcionando mayor capacidad y flexibilidad en comparación con las redes PMR tradicionales.

### Características principales:

- **Uso privado y seguro:** Acceso restringido a usuarios autorizados, garantizando la confidencialidad y seguridad de las comunicaciones.
- **Alta disponibilidad y resistencia:** Diseñadas para operar en condiciones adversas, asegurando el restablecimiento rápido del servicio en caso de fallo.
- **Independencia de redes comerciales:** Funcionan de manera autónoma respecto a las redes públicas para asegurar operatividad en situaciones críticas.
- **Interoperabilidad y trato prioritario:** Capaces de establecer comunicaciones prioritarias y garantizar la interoperabilidad entre las subredes que las conforman.

### Requisitos mínimos:

- **Tratamiento prioritario del tráfico:** Identificación y gestión preferente del tráfico de emergencia.
- **Seguridad y confidencialidad:** Protección contra accesos no autorizados, manipulaciones e intercepciones.
- **Restablecimiento rápido:** Capacidad para reanudar el servicio eficientemente tras una interrupción.
- **Conectividad amplia:** Integración con otras redes para proporcionar cobertura extensa, incluso a nivel internacional.
- **Compatibilidad y movilidad:** Infraestructuras compatibles que faciliten el transporte y despliegue en diferentes ubicaciones.
- **Cobertura ubicua:** Alcance en grandes zonas geográficas para asegurar comunicación en cualquier lugar.
- **Resistencia a catástrofes:** Diseño robusto para mantener operatividad frente a desastres.
- **Transmisión de voz de calidad:** Comunicaciones claras y sin interferencias.
- **Ancho de banda adaptable:** Capacidad elástica para ajustarse a las necesidades en situaciones de emergencia.
- **Fiabilidad y disponibilidad:** Alto grado de confianza en el desempeño continuo del servicio.

### Interfaces de las Redes de Emergencia

Para garantizar la interoperabilidad y funcionalidad de los sistemas, las redes de emergencia utilizan varias interfaces específicas, cada una con un propósito determinado:

- **Radio-Aire (AI)**: Enlace entre los dispositivos terminales y las estaciones base mediante señales de radiofrecuencia.
- **Modo Directo (DMO)**: Permite la comunicación directa entre terminales sin necesidad de infraestructura intermedia.
- **Hombre-Máquina (MMI)**: Interfaz que conecta al usuario con el dispositivo, facilitando la interacción.
- **Equipo Periférico (PEI)**: Conexión con dispositivos externos, como impresoras, escáneres o accesorios.
- **Estación de Línea (RDI)**: Establece la comunicación con estaciones de línea fija.
- **Pasarela**: Enlace entre diferentes redes o sistemas para garantizar la interoperabilidad.
- **Inter-Sistema (ISI)**: Conexión entre redes de diferentes jurisdicciones o tecnologías.
- **Gestión de Red (NMI)**: Interfaz utilizada para la configuración, supervisión y mantenimiento de la red.

### Modos de Operación

- **Circuito/V+D/Troncalizado (TMO)**: Este modo combina la transmisión de voz y datos (V+D) de manera simultánea, garantizando comunicaciones rápidas y efectivas en situaciones críticas.
- **Modo Directo (DMO)**: Ofrece comunicación directa entre dos o más terminales o estaciones sin necesidad de utilizar infraestructura de red. Es ideal para situaciones donde la red centralizada no está disponible.
- **Paquetes Optimizados (PDO)**: Es un modo de operación en circuito diseñado para transmitir únicamente paquetes de datos. Esto optimiza el uso del ancho de banda y mejora la eficiencia de la red.

### Tecnologías utilizadas en telecomunicaciones de emergencia: Redes de radio

En las telecomunicaciones de emergencia se emplean principalmente redes de radio, esenciales para asegurar comunicaciones fiables cuando otras infraestructuras pueden fallar.

### Tipos de redes de radio en Europa:

- **Redes analógicas:** Tienen cobertura limitada y requieren repetidores para ampliar su alcance. Presentan limitaciones en calidad y seguridad.
- **Redes con sistema de acceso troncalizado (Trunking):** Ofrecen servicios de intercomunicación de voz y/o datos para grupos cerrados de usuarios mediante redes independientes de las públicas.
    - **Trunking analógico:** Tecnología obsoleta reemplazada por sistemas digitales.
    - **Trunking digital:** Mejora la calidad de audio, reduce interferencias y permite funcionalidades avanzadas como llamadas en grupo e integración de sistemas de localización.

### Tecnologías de radio digitales usadas en Europa:

- **TETRA (Terrestrial Trunked Radio):** Sistema de radio trunking digital que conecta múltiples puntos y bases de radio, formando redes extensas que pueden cubrir países enteros.
    - **Características:**
        - Protocolo abierto.
        - Transmisión de voz y datos (mensajes de estado, datos cortos y datos en modo paquete).
        - Utiliza multiplexación por división de tiempo (TDMA) con 4 canales en 25 kHz.
        - Operable en España en la banda de 380-400 MHz para servicios de seguridad y emergencia.
    - **Constituido por:**
        - **Emplazamiento Maestro:** Centro de Gestión y Conmutación
        - **Emplazamientos Remotos:** Bases de Cobertura Radio
- **TETRAPOL:** Tecnología europea de radiocomunicaciones digitales adaptada a usuarios profesionales de redes privadas de radio (PMR).
    - **Características:**
        - Funciona en la banda de 380-400 MHz.
        - Cifrado de extremo a extremo, ofreciendo mayor seguridad que TETRA.
        - Protocolo propietario.
- **LTE (Long Term Evolution):** Soporta un amplio rango de frecuencias y proporciona alto rendimiento a altas velocidades, alcanzando tasas de transferencia superiores a 100 Mbps.
    - **Limitaciones:**
        - Menor resiliencia para comunicaciones críticas.
        - Uso en soluciones mixtas (LTE-TETRA) en proyectos puntuales.

### Redes de Comunicaciones de Emergencias de ámbito estatal y autonómico

- **SIRDEE (Sistema de Radiocomunicaciones Digitales de Emergencia del Estado):** Red nacional de radio trunking digital basada en TETRAPOL para las Fuerzas y Cuerpos de Seguridad del Estado.
- **REMER (Red Radio de Emergencia):** Complementaria de la Dirección General de Protección Civil y Emergencias, formada por alrededor de 7.000 radioaficionados.
- **COMDES (Comunicaciones Móviles Digitales de Emergencias y Seguridad de la Comunitat Valenciana):** Red de la Generalitat basada en tecnología TETRA, que ofrece servicios a organizaciones y flotas de emergencias y seguridad en la comunidad.
- **RENEM (Red Nacional de Emergencias):** "Sistema de Sistemas de Información y Telecomunicaciones" que integra sistemas de la Administración General del Estado, Comunidades Autónomas y corporaciones privadas de infraestructuras críticas.
    - **Infraestructura:** Utiliza redes terrestres (Red Iris, Red Sara, WAN PG, Internet) y satelitales (SPAINSAT, XTAR-EU y redes civiles).

## Red COMDES (Comunicaciones Móviles Digitales de Emergencias y Seguridad de la Comunitat Valenciana)

La Red COMDES es la infraestructura de telecomunicaciones que la Generalitat ofrece a organizaciones y flotas de prevención, rescate, emergencias y seguridad en la Comunidad Valenciana.

### Funcionamiento:

- Opera como una red privada virtual para cada flota.
- Permite intercomunicación mediante grupos de comunicación comunes para facilitar la operativa local, comarcal y autonómica.

### Infraestructura:

- **193 estaciones base** que cubren el 98% del territorio y el 99,5% de la población.
- **Capacidad para más de 1.445 comunicaciones** de voz y datos simultáneas.
- **Interconexión con otras redes** públicas y privadas de voz y datos.

### Servicios ofrecidos:

- Llamadas individuales y de grupo.
- Configuración dinámica de grupos de comunicación intra e inter flotas.
- Autenticación de terminales y encriptación de comunicaciones.
- Envío de mensajes de texto y posicionamiento GPS.
- Comunicaciones de datos y aplicaciones instalables en terminales y servicios centrales.
- Comunicaciones de voz y datos con redes externas.

### Organización:

- **Operador de red:**
    - **Funciones:** Planificación, gestión y supervisión técnica, operativa y administrativa de la red.
    - **Entidad responsable:** Dirección General de Tecnologías de la Información y las Comunicaciones.
- **Usuarios:**
    - **Funciones:** Gestión operativa y uso de la red como apoyo a sus servicios.
    - **Incluye:**
        - Servicios de intervención: Sanitarios, bomberos, protección civil.
        - Servicios de seguridad: Policías locales y nacionales.
        - Centro de Coordinación de Emergencias de la Comunidad Valenciana: Elabora protocolos y organiza comunicaciones.
- **Proveedores externos:**
    - **Funciones:** Mantenimiento de equipamiento y servicios relacionados.
    - **Incluye:** Empresas contratadas por el operador de red o usuarios para mantenimiento, suministro de terminales, plataformas externas (ej.: 112) y aplicaciones.

## Estándar TETRA (Terrestrial Trunked Radio)

El estándar TETRA es un sistema de comunicación digital móvil desarrollado para redes de emergencia y servicios críticos, mejorando la calidad y seguridad respecto a sistemas analógicos.

### Características:

- **Frecuencia utilizada:** 380-400 MHz.
- **Cobertura extendida:** Usa bandas más bajas que GSM para mayor alcance.
- **Infraestructura independiente:** Separada de redes de telefonía móvil, asegurando operatividad en situaciones donde estas pueden fallar.
- **Modo directo (terminal a terminal):** Comunicación sin necesidad de infraestructura intermedia.
- **Calidad de sonido superior a GSM:** Comunicaciones claras y sin interferencias.
- **Modos de comunicación:** Semidúplex (como radios) y dúplex (como teléfonos).
- **Baja saturación:** Menor riesgo de congestión, garantizando capacidad en alta demanda.
- **Comunicaciones grupales:** Facilita coordinación entre múltiples usuarios.

### Arquitectura del sistema TETRA:

- **Terminales móviles:** Dispositivos de usuario final para comunicación en la red.
- **Estaciones base:** Transmiten y reciben señales de terminales, cubriendo áreas específicas.
- **Sistema de control:** Gestiona la red, llamadas y acceso.
- **Sistema de red:** Conectividad entre componentes, asegurando interoperabilidad.

### Servicios ofrecidos por TETRA:

- **Servicios de voz y datos:** Comunicación eficiente y segura.
- **Llamadas individuales y grupales:** Flexibilidad en comunicaciones.
- **Mensajes de texto y estado:** Información rápida y discreta.
- **Servicios de localización y seguimiento:** Integración GPS para posicionamiento.
- **Acceso a bases de datos y sistemas de información:** Información en tiempo real.

### Seguridad en TETRA:

- **Encriptación de comunicaciones:** Protege contra escuchas no autorizadas.
- **Autenticación de usuarios:** Asegura acceso exclusivo a usuarios autorizados.
- **Protección contra ataques:** Prevención y detección de intrusiones o interferencias.

### Aplicaciones de TETRA:

- **Servicios de emergencia:** Coordinación en policías, bomberos y servicios médicos.
- **Empresas y eventos masivos:** Comunicación interna en corporaciones y gestión de eventos.
- **Transporte y logística:** Comunicación en transporte público y gestión de flotas.

### Evolución y tendencias para servicios de datos en banda ancha

La creciente demanda de datos en tiempo real en servicios de emergencia impulsa la evolución de TETRA hacia la integración con tecnologías de banda ancha.

### Tendencias actuales:

- **Integración con LTE y 5G:** Combinación de la fiabilidad de TETRA con la alta velocidad de datos de redes móviles avanzadas.
- **Desarrollo de estándares abiertos:** Facilita interoperabilidad y reduce dependencia de tecnologías propietarias.
- **Soluciones híbridas:** Sistemas que utilizan TETRA para voz crítica y LTE para datos de banda ancha.
- **Avances en seguridad:** Incorporación de ciberseguridad avanzada para proteger comunicaciones en redes más complejas.

### Desafíos:

- **Resiliencia y fiabilidad:** Mantener altos estándares de disponibilidad en nuevas tecnologías.
- **Compatibilidad e interoperabilidad:** Asegurar interacción con infraestructuras existentes.
- **Asignación de espectro:** Necesidad de frecuencias dedicadas para servicios de emergencia en bandas aptas para banda ancha.
