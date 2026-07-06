# Desarrollo de aplicaciones móviles

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Diseño y Desarrollo de Aplicaciones Móviles

El diseño y desarrollo de aplicaciones móviles requiere considerar el tipo de aplicación a crear, los principios de diseño adecuados y los entornos de trabajo disponibles. Las aplicaciones móviles se clasifican en tres categorías principales: **nativas**, **web** e **híbridas**.

**1. Aplicaciones nativas:** Se desarrollan específicamente para un sistema operativo móvil (Android, iOS, etc.) utilizando los lenguajes y herramientas propias de la plataforma. Estas aplicaciones aprovechan al máximo las características y funcionalidades del dispositivo, ofreciendo un rendimiento y experiencia de usuario superiores.

- **Ventajas:**
    - Mayor rendimiento y velocidad de ejecución.
    - Acceso completo a todas las funcionalidades del dispositivo (cámara, GPS, sensores, etc.).
    - Mejor experiencia de usuario.
    - Mayor visibilidad en las tiendas de aplicaciones.
- **Desventajas:**
    - Mayor costo y tiempo de desarrollo, al requerir versiones específicas para cada sistema operativo.
    - Mayor dificultad para actualizar y mantener.
- **Frameworks y lenguajes:**
    - **Android:** Java y Kotlin.
    - **iOS:** Objective-C y Swift.
    - **Multiplataforma:** Xamarin.

**2. Aplicaciones web:** Se ejecutan en un navegador web, permitiendo el acceso desde cualquier dispositivo con conexión a Internet y un navegador compatible. Su desarrollo es independiente del sistema operativo.

- **Ventajas:**
    - Mayor facilidad de desarrollo y mantenimiento.
    - Mayor flexibilidad y escalabilidad.
    - Mayor alcance y visibilidad.
- **Desventajas:**
    - Menor rendimiento y velocidad de ejecución comparado con aplicaciones nativas.
    - Acceso limitado a las funcionalidades del dispositivo.
    - Experiencia de usuario menos fluida y consistente.
- **Frameworks y tecnologías:**
    - HTML5, CSS3 y JavaScript.
    - Frameworks como jQuery Mobile, AngularJS, React y Bootstrap.

**3. Aplicaciones híbridas:** Combinan elementos de aplicaciones nativas y web. Se desarrollan como aplicaciones web pero se empaquetan dentro de un contenedor nativo, permitiendo su distribución a través de las tiendas de aplicaciones y acceso a ciertas funcionalidades del dispositivo.

- **Ventajas:**
    - Desarrollo más rápido y económico al reutilizar código web.
    - Mayor alcance y visibilidad en tiendas de aplicaciones.
    - Flexibilidad y escalabilidad mejoradas.
- **Desventajas:**
    - Rendimiento y velocidad de ejecución inferiores a las aplicaciones nativas.
    - Experiencia de usuario menos fluida y consistente.
    - Acceso limitado a algunas funcionalidades del dispositivo.
- **Frameworks:**
    - Cordova, Ionic y Flutter.

### Principios de Diseño de Aplicaciones Móviles

Un buen diseño de aplicaciones móviles se basa en principios fundamentales como la **simplicidad**, **consistencia** y **navegación intuitiva**. La aplicación debe ser fácil de usar, coherente en su interfaz y reflejar la identidad de la marca.

- **Simplicidad:** Diseño limpio y sin elementos innecesarios que puedan distraer al usuario.
- **Consistencia:** Uso uniforme de elementos y comportamientos a lo largo de la aplicación.
- **Navegación intuitiva:** Estructura lógica que facilita al usuario moverse por la aplicación.

**Patrones de interacción:** Son soluciones probadas para problemas comunes en el diseño de aplicaciones, aplicados en aspectos como navegación, acciones, cuadros de diálogo, notificaciones y gestos.

**Diseño visual:** Debe ser atractivo y funcional, facilitando la interacción del usuario.

- **Tipografía:** En pantallas de baja resolución, es recomendable usar tipografías limpias, abiertas y sin serif (Sans-Serif).
- **Color:** Utilizar un sistema cromático consistente (por ejemplo, rojo para errores, amarillo para avisos y verde para confirmaciones).

## Aplicaciones Nativas: Android

Las aplicaciones nativas para Android se desarrollan utilizando lenguajes como Java y Kotlin, ofreciendo una integración completa con el sistema operativo y el hardware.

### Ventajas:

- No requieren conexión a Internet para funcionar.
- Acceso completo a características hardware (cámara, GPS, etc.).
- Permiten notificaciones push.
- Distribución a través de la Play Store.

**Android:** Sistema operativo basado en Linux diseñado para dispositivos móviles, con una cuota de mercado superior al 80%.

### Arquitectura de Android:

- **Kernel de Linux:** Servicios básicos y manejo de hardware.
- **Hardware Abstraction Layer (HAL):** Interfaz estándar para acceder al hardware.
- **Android Runtime (ART):** Entorno de ejecución con compilación JIT.
- **Librerías Nativas (C/C++):** Funcionalidades básicas como gráficos y bases de datos.
- **Framework de API Java:** Acceso a componentes del sistema.
- **Aplicaciones del Sistema:** Aplicaciones preinstaladas.

**Java:** Compila a bytecodes ejecutables en cualquier JVM.

**Android SDK:** Herramientas de desarrollo incluyendo un depurador, bibliotecas y un emulador.

- **IDE oficial:** Android Studio.
- Las aplicaciones se empaquetan como .apk y se almacenan en /data/app.

### Principales clases para desarrollo:

- **ActivityManager:** Controla el ciclo de vida de las actividades.
- **View:** Construcción de interfaces.
- **NotificationManager:** Muestra avisos al usuario.
- **ContentProvider:** Intercambio estandarizado de datos.
- **ResourceManager:** Gestiona recursos no codificados.

### Tipos de aplicaciones:

- **Apps de primer plano:** Muestran una interfaz y pueden perder el foco.
- **Apps de segundo plano (Servicios):** Continúan ejecutándose tras cerrar la aplicación.
- **Widgets:** Interfaces pequeñas en el escritorio que se actualizan periódicamente.

**AndroidManifest.xml:** Declara metadatos y permisos requeridos, que deben ser concedidos por el usuario.

**Kotlin:** Lenguaje desarrollado por JetBrains, compatible con Java y oficial para Android.

- **Características:**
    - Funciones con parámetros por defecto.
    - Variables no nulas por defecto.
    - Sobrecarga de operadores.
    - Soporte para programación funcional.

**Construcción de UI:** Uso del patrón Modelo-Vista-Presentador (MVP).

- **Modelo:** Define datos y lógica.
- **Presentador:** Conecta modelo y vista.
- **Vista:** Muestra datos y gestiona la interacción del usuario.

### Frameworks adicionales:

- **Titanium SDK:** Desarrollo multiplataforma con JavaScript.
- **Corona SDK (Solar2D):** Desarrollo en Lua para aplicaciones 2D.

### Dalvik Virtual Machine (VM)

La **Dalvik VM** es la máquina virtual utilizada en versiones anteriores de Android para ejecutar aplicaciones, ejecutando bytecode en formato .dex.

- **Características:**
    - Optimizada para dispositivos con recursos limitados.
    - Permite múltiples instancias con bajo consumo de memoria.

Reemplazada por **ART (Android Runtime)** en versiones recientes.

## Aplicaciones Nativas: iOS

Las aplicaciones nativas para iOS se desarrollan en Objective-C o Swift, integrándose completamente con el sistema y hardware.

**iOS:** Sistema operativo basado en macOS, derivado de Unix, con una cuota de mercado del 10-15%.

### Arquitectura de iOS:

- **Core OS Layer:** Servicios de bajo nivel y hardware.
- **Core Services Layer:** Servicios básicos como bases de datos.
- **Media Layer:** Capacidades gráficas y multimedia.
- **Cocoa Touch Layer:** Frameworks para desarrollo de interfaces.

**Objective-C:** Lenguaje orientado a objetos, superconjunto de C.

- **Características:**
    - Envío de mensajes a objetos.
    - Inclusión de código C.

**Cocoa Touch:** API para acceso a funciones del sistema.

- **Frameworks:**
    - **UIKit:** Manejo de la capa gráfica.
    - **Foundation Framework:** Clases básicas y servicios.
    - **AppKit:** Interfaz gráfica.
    - **Swift Standard Library:** Librería estándar para Swift.

**iOS SDK:** Herramientas para desarrollo de terceros.

**Swift:** Lenguaje compilado y multiparadigma para iOS y macOS.

- **Características:**
    - Sintaxis moderna.
    - Seguridad en gestión de memoria.
    - Programación orientada a objetos y funcional.

## Aplicaciones Nativas: Windows

Microsoft desarrolló sistemas operativos móviles como Windows Mobile, Windows Phone y Windows 10 Mobile, actualmente descontinuados.

- **Pocket PC / Windows Mobile:** Desarrollo en C++ o .NET.
- **Windows Phone:** Desarrollo en C#, Visual Basic .NET o C++.
- **Windows 10 Mobile:** Plataforma unificada, ahora abandonada.

## Aplicaciones Web

Al desarrollar aplicaciones web para móviles, se puede optar por crear una web específica o utilizar un diseño responsive que se adapte a diferentes tamaños de pantalla.

### Reglas de usabilidad:

- Reducir la cantidad de contenido para facilitar la lectura en pantallas pequeñas.
- Utilizar una sola columna para presentar la información.
- Ocultar menús y elementos no esenciales.
- Minimizar las llamadas al servidor para mejorar el rendimiento.

### Tecnologías usadas:

- **HTML5:** Proporciona estructuras semánticas y capacidades multimedia sin necesidad de plugins.
- **CSS3:** Permite estilizar y adaptar el diseño a diferentes dispositivos.
- **JavaScript:** Añade interactividad y dinamismo.

### Principales frameworks:

- **jQuery Mobile:** Ofrece compatibilidad con una amplia gama de dispositivos, asegurando una experiencia consistente.
    - **Formas de crear páginas:**
        - Múltiples ficheros HTML con enlaces.
        - Un único fichero HTML con enlaces internos.
    - **Precarga de páginas:** Uso del atributo data-prefetch para mejorar el rendimiento.
- **AngularJS:** Framework para crear aplicaciones del lado del cliente usando el patrón MVC.
    - **Principales directivas:**
        - ng-app: Inicializa la aplicación.
        - \$scope: Contexto de ejecución de variables.
        - ng-controller: Define el ámbito del controlador.
        - ng-model: Enlaza campos de formulario con el ámbito.
        - ng-bind: Enlaza datos del modelo con la vista.
- **Bootstrap:** Framework frontend para diseño responsive.
    - Utiliza hojas de estilo LESS.
    - Basado en una cuadrícula estándar de 940 píxeles de ancho.

## Aplicaciones Híbridas

Las aplicaciones híbridas combinan una aplicación web dentro de un contenedor nativo, utilizando un WebView para mostrar contenido y acceder a APIs nativas.

- **Ventajas:**
    - Desarrollo más rápido y económico.
    - Código reutilizable entre plataformas.
    - Distribución en tiendas de aplicaciones.
- **Desventajas:**
    - Rendimiento inferior al de aplicaciones nativas.
    - Experiencia de usuario menos fluida.
    - Acceso limitado a funcionalidades del dispositivo.

### Frameworks:

- **Ionic:** Basado en Angular y Cordova para acceso nativo.
- **Xamarin:** Genera aplicaciones nativas usando .NET y C#.
    - **Características:**
        - Código compartido en lógica de negocio.
        - Interfaces programadas independientemente.
        - **IDEs:** Xamarin Studio y Visual Studio.
- **Flutter:** SDK multiplataforma de Google usando Dart.
    - **Características:**
        - Alto rendimiento con motor gráfico propio.
        - Desarrollo rápido con Hot Reload.
- **React Native:** Framework de Facebook usando JavaScript y React.
    - **Características:**
        - Código nativo para mejor rendimiento.
        - Código compartido entre plataformas.
