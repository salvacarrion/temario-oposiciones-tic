# Desarrollo de aplicaciones móviles

## Diseño y arquitecturas de aplicaciones móviles

El desarrollo móvil está condicionado por un mercado que es en la práctica un duopolio: **Android** ronda el **70%** de cuota mundial e **iOS** el **29%** (StatCounter, 2026). Los sistemas alternativos desaparecieron (Windows Phone y Windows 10 Mobile fueron descatalogados por Microsoft, con fin de soporte en enero de 2020; BlackBerry OS corrió la misma suerte), de modo que la primera decisión de arquitectura es cómo cubrir esas dos plataformas: con desarrollos nativos separados, con un único código multiplataforma o con la propia web.

**Tipos de aplicación móvil**:

- **Nativa**: desarrollada para una plataforma concreta con sus lenguajes y SDK oficiales (Kotlin/Java en Android; Swift/Objective-C en iOS). Máximo rendimiento, experiencia integrada y acceso completo al hardware (cámara, GPS, sensores, biometría); a cambio, exige un desarrollo y mantenimiento por plataforma.
- **Web móvil**: sitio web con diseño adaptativo que se usa desde el navegador. Un solo desarrollo, sin instalación ni tiendas; pero acceso limitado al dispositivo y dependencia de la conexión.
- **Híbrida**: aplicación web (HTML, CSS, JavaScript) empaquetada en un contenedor nativo que la muestra en un **WebView** y expone el hardware mediante plugins. Se distribuye por las tiendas como una app más.
- **Multiplataforma compilada**: un único código base que se compila para cada plataforma con interfaz renderizada de forma nativa o cuasi nativa (Flutter, React Native, Kotlin Multiplatform, .NET MAUI). Rendimiento próximo al nativo con un solo equipo de desarrollo.
- **Aplicación web progresiva (PWA)**: web instalable con capacidades de app (funcionamiento offline, notificaciones); se desarrolla en la última sección.

| Enfoque | Lenguajes | Rendimiento y hardware | Coste | Distribución |
| --- | --- | --- | --- | --- |
| Nativo | Kotlin/Java, Swift | Máximos | Doble desarrollo | Tiendas |
| Híbrido (WebView) | HTML/CSS/JS | Limitados | Bajo (reutiliza web) | Tiendas |
| Multiplataforma | Dart, JS/TS, Kotlin, C# | Cuasi nativos | Medio (un código) | Tiendas |
| Web móvil / PWA | HTML/CSS/JS | Los del navegador | Bajo | URL (sin tienda) |

**Principios de diseño móvil**: la referencia son las guías oficiales de cada plataforma: **Material Design** (Google) y las **Human Interface Guidelines** (Apple). Seguirlas hace que la aplicación resulte coherente con el resto del sistema.

- **Simplicidad**: pantallas centradas en una tarea, sin elementos superfluos; el contenido manda.
- **Consistencia**: mismos componentes, gestos y comportamientos en toda la aplicación, y alineados con los patrones de la plataforma.
- **Navegación intuitiva**: jerarquía clara y previsible (barra inferior, cajón lateral, pila de pantallas con vuelta atrás).
- **Diseño táctil**: áreas de pulsación suficientes, gestos estándar (deslizar, pellizcar) y respuesta inmediata a cada acción.
- **Tipografía y color**: tipografías sans-serif legibles en pantalla y un sistema cromático consistente y con significado (rojo para errores, verde para confirmaciones), respetando el contraste (accesibilidad, tema [58](58-accesibilidad-y-usabilidad.md)).

**Patrones de presentación**: la evolución fue **MVC** → **MVP** (presentador que aísla la vista) → **MVVM** (modelo-vista-vista-modelo con estado observable), el recomendado por las guías de arquitectura actuales; los frameworks declarativos (Jetpack Compose, SwiftUI) llevan a un **flujo de datos unidireccional**: el estado baja hacia la interfaz y los eventos suben.

**Condicionantes propios del móvil**:

- **Conectividad intermitente**: diseño *offline-first*: caché local y sincronización cuando hay red.
- **Batería y datos**: minimizar peticiones de red y trabajo en segundo plano.
- **Permisos**: declarados por la app y concedidos por el usuario, revocables en cualquier momento.
- **Fragmentación**: multitud de tamaños, densidades de pantalla y versiones de sistema conviviendo; exige diseño adaptable y niveles mínimos de API bien elegidos.
- **Seguridad**: almacenamiento cifrado, autenticación biométrica y protección de las comunicaciones (TLS).

## Aplicaciones nativas: Android

Android es un sistema operativo de código abierto (proyecto **AOSP**) sobre **kernel de Linux**, liderado por **Google**; equipa en torno al **70%** de los móviles del mundo. La versión vigente es **Android 17 (junio de 2026)**, con una versión mayor al año.

**Arquitectura por capas**:

- **Kernel de Linux**: procesos, memoria, seguridad y controladores de hardware.
- **HAL (Hardware Abstraction Layer)**: interfaz estándar entre el hardware y las APIs del sistema.
- **ART (Android Runtime)**: ejecuta el bytecode **DEX** de las aplicaciones. Introdujo la compilación **AOT** (anticipada, al instalar) en Android 5 y desde Android 7 combina **AOT + JIT guiada por perfiles de uso**. Sustituyó a la **Dalvik VM** original (solo JIT), optimizada para dispositivos con pocos recursos.
- **Bibliotecas nativas en C/C++**: gráficos (OpenGL/Vulkan), SQLite, WebView.
- **Framework de APIs (Java/Kotlin)**: los servicios del sistema que usan las apps: gestión de actividades, notificaciones, recursos, proveedores de contenido.
- **Aplicaciones del sistema**: preinstaladas (teléfono, ajustes, navegador).

**Lenguajes**: **Kotlin** (JetBrains) es el lenguaje **oficial desde 2017 y preferente desde 2019** («Kotlin-first»): conciso, interoperable con Java, tipos no nulos por defecto y corrutinas para asincronía. **Java** sigue soportado (gran base de código existente) y el **NDK** permite C/C++ para partes críticas.

**Componentes de una aplicación** (los cuatro bloques del modelo Android; se activan mediante *intents*):

- **Activity**: una pantalla con interfaz; tiene ciclo de vida gestionado por el sistema (onCreate, onPause...).
- **Service**: trabajo en segundo plano sin interfaz (música, sincronización).
- **Broadcast receiver**: reacciona a anuncios del sistema o de otras apps (batería baja, arranque).
- **Content provider**: expone datos de la app a otras mediante una interfaz estándar (los contactos, por ejemplo).

**Manifiesto y permisos**: `AndroidManifest.xml` declara los componentes, los metadatos y los **permisos** que la app necesita; desde Android 6, los permisos peligrosos (cámara, ubicación, contactos) se conceden **en tiempo de ejecución** y el usuario puede revocarlos.

**Herramientas y bibliotecas**:

- **Android Studio**: IDE oficial (basado en IntelliJ), con emulador, depurador y perfilado; construcción con **Gradle**.
- **Jetpack**: conjunto de bibliotecas oficiales que resuelven ciclo de vida, navegación, persistencia (Room) o trabajo en segundo plano.
- **Jetpack Compose**: toolkit **declarativo** de interfaces en Kotlin (estable desde 2021), recomendado para desarrollo nuevo frente a las vistas XML clásicas.

**Empaquetado y distribución**: el instalable es el **APK**; para publicar en **Google Play** es obligatorio desde agosto de 2021 el **AAB (Android App Bundle)**, del que la tienda genera APKs optimizados por dispositivo. Android admite además tiendas alternativas e instalación directa (*sideloading*).

## Aplicaciones nativas: iOS

iOS es el sistema operativo móvil de **Apple**, derivado de macOS (núcleo **Darwin**, base Unix) y exclusivo de su hardware; ronda el **29%** de cuota mundial, mayor en países de renta alta. La versión vigente es **iOS 26**: desde 2025 Apple numera las versiones por año, de modo que a iOS 18 le siguió directamente iOS 26.

**Arquitectura en capas**:

- **Core OS**: núcleo, seguridad, gestión de energía y comunicación con el hardware.
- **Core Services**: servicios fundamentales: Foundation (tipos y colecciones), red, persistencia (Core Data), localización.
- **Media**: gráficos (Metal, Core Animation), audio y vídeo.
- **Cocoa Touch**: la capa de interacción: frameworks de interfaz y eventos táctiles, con **UIKit** al frente.

**Lenguajes**:

- **Swift** (2014): lenguaje compilado y multiparadigma de Apple, de **código abierto**; sintaxis moderna, gestión segura de memoria y de valores nulos (*optionals*). Es el estándar para desarrollo nuevo.
- **Objective-C**: superconjunto orientado a objetos de C basado en envío de mensajes; hoy es código heredado, plenamente soportado.

**Frameworks de interfaz**: **UIKit** es el framework imperativo clásico; **SwiftUI** (2019) es el toolkit **declarativo** recomendado para proyectos nuevos, común a todas las plataformas Apple (iOS, iPadOS, watchOS, macOS).

**Herramientas**: **Xcode** (IDE oficial, disponible solo en macOS) con el simulador y el gestor de dependencias Swift Package Manager; **TestFlight** para distribuir betas.

**Distribución**: la **App Store** con revisión previa de Apple era el único canal; en aplicación del **Reglamento (UE) 2022/1925 (DMA, Ley de Mercados Digitales)**, desde **marzo de 2024** (iOS 17.4) Apple debe permitir en la UE **tiendas de aplicaciones alternativas** y la distribución fuera de su tienda.

## Aplicaciones híbridas y multiplataforma

El objetivo común es escribir el código una vez y ejecutarlo en Android e iOS. Hay dos familias con arquitecturas muy distintas: las híbridas basadas en WebView y las multiplataforma compiladas.

**Híbridas (WebView)**: la aplicación es una web que corre dentro de un contenedor nativo; los plugins hacen de puente con el hardware.

- **Apache Cordova** (heredero de PhoneGap): el contenedor clásico, hoy en declive; su relevo es **Capacitor** (del equipo de Ionic, 2019), con mejor integración nativa.
- **Ionic**: biblioteca de componentes de interfaz web con aspecto móvil que funciona con Angular, React o Vue sobre Capacitor o Cordova.
- **Balance**: coste mínimo si ya existe la web y el equipo es web; el rendimiento y la sensación de uso no alcanzan a los nativos.

**Multiplataforma compiladas**:

- **Flutter** (Google, 2018): lenguaje **Dart** y motor de renderizado propio (**Impeller**) que dibuja toda la interfaz (*widgets*) con idéntico resultado en cualquier plataforma; *hot reload* para ver los cambios al instante; alcanza también web y escritorio.
- **React Native** (Meta, 2015): JavaScript/TypeScript con el modelo de componentes de React, pero renderizando **componentes nativos reales**; su nueva arquitectura (comunicación directa JSI, sin el «puente» clásico) es la opción por defecto desde 2024; **Expo** simplifica la cadena de herramientas.
- **Kotlin Multiplatform (KMP)** (JetBrains, estable desde noviembre de 2023): comparte la **lógica de negocio** en Kotlin entre Android, iOS y otros destinos, manteniendo interfaces nativas (o comunes con Compose Multiplatform).
- **.NET MAUI** (Microsoft): sucesor multiplataforma de **Xamarin**, cuyo soporte terminó el **1 de mayo de 2024**; desarrollo en C#/.NET integrado con Visual Studio.

| Framework | Promotor | Lenguaje | Interfaz | Rasgo distintivo |
| --- | --- | --- | --- | --- |
| Flutter | Google | Dart | Motor propio (widgets) | Píxel idéntico en todas partes |
| React Native | Meta | JS/TS (React) | Componentes nativos | Ecosistema React |
| Kotlin Multiplatform | JetBrains | Kotlin | Nativa (o Compose) | Comparte solo la lógica |
| .NET MAUI | Microsoft | C# | Controles nativos | Sucesor de Xamarin |
| Ionic + Capacitor | Ionic | HTML/CSS/JS | WebView | Reutiliza la web tal cual |

**Criterios de elección**: máximo rendimiento y acceso al hardware → nativo; presupuesto ajustado y equipo web → híbrido o PWA; equilibrio entre coste y calidad → Flutter o React Native; lógica compleja compartida con experiencia 100% nativa → KMP.

## Aplicaciones web progresivas (PWA)

Una **PWA (Progressive Web App)** es una aplicación web que el navegador puede **instalar** en el dispositivo y que funciona **sin conexión**, acercando la experiencia web a la de una aplicación nativa sin pasar por las tiendas. El término lo acuñó Google en **2015**.

**Requisitos técnicos** (los tres pilares):

- **HTTPS**: contexto seguro obligatorio.
- **Web App Manifest**: fichero JSON con nombre, iconos, colores y modo de presentación (*standalone*, sin interfaz de navegador); es lo que permite «añadir a pantalla de inicio» con apariencia de app.
- **Service worker**: script que actúa de **proxy entre la aplicación y la red**: cachea recursos con distintas estrategias (*cache-first*, *network-first*), da servicio **offline**, sincroniza en segundo plano y recibe **notificaciones push**.

**Capacidades**: instalable y ligera, actualización instantánea (se sirve siempre la última versión desde el servidor), enlazable e indexable por buscadores, y con acceso creciente al dispositivo (cámara, geolocalización, almacenamiento). **Límites**: menos integración profunda que una nativa, y soporte desigual en **iOS/Safari** (notificaciones push solo desde iOS 16.4, en 2023, y con restricciones).

**PWA frente a aplicación de tienda**: un solo desarrollo web, sin revisión ni comisiones de tienda y con distribución por URL; a cambio se renuncia a la visibilidad de las tiendas y a parte del hardware. Para servicios de información y tramitación (el caso típico de una Administración) suele ser suficiente y evita mantener dos aplicaciones nativas.

El diseño adaptativo y la accesibilidad se tratan en el tema [58](58-accesibilidad-y-usabilidad.md); las tecnologías web subyacentes, en el [53](53-proteccion-de-datos-personales.md).

## Fuentes {.unnumbered .unlisted}

- Documentación oficial de Android (developer.android.com) y de Apple (developer.apple.com: Human Interface Guidelines, Swift, SwiftUI), consulta: julio de 2026.
- StatCounter Global Stats, cuota mundial de sistemas operativos móviles (consulta: julio de 2026).
- Documentación oficial de Flutter, React Native, Kotlin Multiplatform, .NET MAUI e Ionic/Capacitor (consulta: julio de 2026); fin de soporte de Xamarin (Microsoft, 1 de mayo de 2024).
- web.dev (Google) y MDN Web Docs: Progressive Web Apps (consulta: julio de 2026).
- Reglamento (UE) 2022/1925 (Ley de Mercados Digitales), aplicación por Apple desde iOS 17.4 (marzo de 2024).
