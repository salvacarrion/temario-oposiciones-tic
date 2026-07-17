# Programación

## Programación orientada a objetos

La **programación orientada a objetos (POO)** es un paradigma que organiza el software en torno a **objetos**: unidades que combinan **datos** (atributos) y **comportamiento** (métodos) y que colaboran entre sí enviándose mensajes. Es el paradigma dominante en el software de gestión y el que asumen lenguajes como Java, C#, Python o TypeScript.

- **Clase**: define las características comunes de un tipo de objetos: sus atributos y sus métodos. Es la plantilla.
- **Objeto**: instancia concreta de una clase, con identidad propia y residente en memoria.
- **Características de todo objeto**: **identidad** (lo distingue de cualquier otro, aunque tengan el mismo estado), **estado** (los valores de sus atributos en un momento dado) y **comportamiento** (las operaciones que sabe realizar).

**Los cuatro pilares de la POO**:

- **Abstracción**: quedarse con las características esenciales del concepto que se modela e ignorar los detalles irrelevantes para el contexto.
- **Encapsulación**: reunir datos y comportamiento en la misma unidad y **ocultar la información** interna: el objeto solo se manipula a través de su **interfaz** pública, lo que evita cambios de estado inesperados y efectos colaterales.
- **Herencia**: las subclases heredan atributos y métodos de su superclase, especializándolos o extendiéndolos; organiza las clases en jerarquías y habilita la reutilización.
- **Polimorfismo**: un mismo mensaje produce comportamientos distintos según el objeto que lo recibe.

**Tipos de polimorfismo**:

- **De sobrecarga** (*overloading*, polimorfismo ad hoc): varios métodos con el mismo nombre y distinta **signatura** (nombre + tipos de parámetros; el tipo de retorno no forma parte de ella) conviven en una clase, y se selecciona uno u otro según los argumentos. Ejemplo: el operador «+» suma números y concatena cadenas.
- **Paramétrico** (genéricos o plantillas): el código se escribe para un **tipo genérico** y funciona con cualquier tipo concreto sin repetirlo: `List<T>` en Java o C#, `template` en C++.
- **De inclusión o subtipado** (*overriding*): una subclase **redefine** un método de su superclase con la misma signatura, y la llamada se resuelve en ejecución según el tipo real del objeto: ante `pieza.mover()`, un alfil y un caballo se mueven cada uno a su manera.

**Modularidad**: subdividir la aplicación en módulos pequeños e independientes, buscando siempre **bajo acoplamiento** (poca interdependencia entre módulos) y **alta cohesión** (los elementos de cada módulo están funcionalmente relacionados y persiguen un mismo fin).

**Modificadores de acceso** (esquema de Java, similar en C# o C++):

- **public**: visible desde cualquier clase.
- **protected**: visible en la propia clase y sus subclases.
- **default** (*package-private*, sin modificador): visible solo dentro del mismo paquete.
- **private**: visible únicamente dentro de la propia clase.

**Interfaces y clases abstractas**:

- **Interfaz**: contrato que declara qué operaciones ofrece un tipo, sin implementarlas; una clase puede implementar varias. Programar «contra interfaces» reduce el acoplamiento.
- **Clase abstracta**: clase que no puede instanciarse, pensada para ser heredada; puede mezclar métodos implementados y abstractos.
- **Composición frente a herencia**: la herencia acopla fuertemente la subclase a la superclase; la recomendación clásica es **favorecer la composición** (construir objetos que contienen otros objetos) y reservar la herencia para verdaderas relaciones «es un».

**Principios SOLID** (recopilados por Robert C. Martin): cinco principios de diseño de clases:

- **S. Responsabilidad única** (*Single Responsibility*): cada clase debe tener una sola razón para cambiar.
- **O. Abierto/cerrado** (*Open/Closed*): abierta a la extensión, cerrada a la modificación.
- **L. Sustitución de Liskov**: cualquier subclase debe poder usarse donde se espera su superclase sin romper el programa.
- **I. Segregación de interfaces**: mejor varias interfaces específicas que una general que obligue a implementar lo que no se usa.
- **D. Inversión de dependencias**: depender de abstracciones, no de implementaciones concretas (es la base de la inyección de dependencias).

## Patrones de diseño

Un **patrón de diseño** es una solución reutilizable y probada a un problema recurrente de diseño, descrita de forma independiente del lenguaje. El catálogo de referencia son los **23 patrones GoF** (por *Gang of Four*: **Gamma, Helm, Johnson y Vlissides**, *Design Patterns*, **1994**), organizados en tres categorías.

**Patrones creacionales** (cómo crear objetos):

- **Abstract Factory**: interfaz para crear **familias** de objetos relacionados sin especificar sus clases concretas.
- **Builder**: separa la construcción de un objeto complejo de su representación, construyéndolo paso a paso.
- **Factory Method**: delega en las subclases la decisión de qué clase concreta instanciar.
- **Prototype**: crea objetos nuevos **clonando** una instancia existente.
- **Singleton**: garantiza **una única instancia** de una clase con un punto de acceso global.

**Patrones estructurales** (cómo componer clases y objetos):

- **Adapter**: hace compatibles interfaces que no lo son, envolviendo una en otra.
- **Bridge**: desacopla una abstracción de su implementación para que evolucionen por separado.
- **Composite**: estructura los objetos en árboles parte-todo y permite tratar igual al objeto simple y al compuesto.
- **Decorator**: añade responsabilidades a un objeto **dinámicamente**, sin modificar su clase.
- **Facade**: ofrece una interfaz unificada y simple sobre un subsistema complejo.
- **Flyweight**: comparte el estado común de multitud de objetos similares para ahorrar memoria.
- **Proxy**: un representante controla el acceso a otro objeto (remoto, costoso o protegido).

**Patrones de comportamiento** (cómo interactúan y se reparten responsabilidades):

- **Chain of Responsibility**: la petición recorre una cadena de receptores hasta que uno la atiende.
- **Command**: encapsula una orden como objeto, lo que permite encolarla, registrarla o deshacerla.
- **Interpreter**: define una gramática y un intérprete para evaluar sentencias de un lenguaje.
- **Iterator**: acceso secuencial a los elementos de una colección sin exponer su estructura interna.
- **Mediator**: centraliza en un objeto la comunicación entre un conjunto de objetos, que dejan de conocerse entre sí.
- **Memento**: captura el estado interno de un objeto para poder restaurarlo, sin violar su encapsulación.
- **Observer**: dependencia uno-a-muchos: cuando el sujeto cambia, notifica automáticamente a sus observadores.
- **State**: el objeto cambia de comportamiento cuando cambia su estado interno.
- **Strategy**: familia de algoritmos intercambiables encapsulados tras una misma interfaz.
- **Template Method**: define en la superclase el esqueleto de un algoritmo y deja pasos concretos a las subclases.
- **Visitor**: añade operaciones nuevas a una jerarquía de objetos sin modificar sus clases.

Aparte del catálogo GoF están los **patrones arquitectónicos**, que operan a nivel de aplicación: **MVC** (modelo-vista-controlador) y sus variantes MVP y MVVM (temas 56 y 59), la arquitectura en capas o los microservicios (tema 60).

**Antipatrones** (Brown et al., *AntiPatterns*, **1998**): prácticas recurrentes y contraproducentes que conviene reconocer:

- **God Object (Todopoderoso)**: un objeto que sabe o hace demasiado y del que depende todo.
- **The Blob**: clases gigantes con decenas de atributos y métodos, difíciles de mantener y probar.
- **Lava Flow**: código muerto o experimental que nadie se atreve a tocar y se fosiliza en el sistema.
- **Poltergeists**: clases efímeras que solo invocan métodos de otras sin aportar funcionalidad.
- **Golden Hammer**: aplicar la tecnología o patrón favorito a cualquier problema («para un martillo, todo son clavos»).
- **Spaghetti Code**: código sin estructura, con flujos enmarañados, incomprensible y frágil.
- **Cut & Paste Programming**: reutilizar copiando código, multiplicando la redundancia y los errores.

## Lenguajes y ecosistemas: visión general

Los lenguajes se caracterizan por unas pocas dimensiones que conviene dominar:

- **Ejecución**: **compilados** a código máquina (C, C++, Go, Rust), **interpretados** (Python, JavaScript) o **híbridos**: compilados a un código intermedio (*bytecode*) que ejecuta una máquina virtual (Java, C#).
- **Tipado**: **estático** (los tipos se comprueban en compilación: Java, C#, TypeScript) frente a **dinámico** (en ejecución: Python, JavaScript); y fuerte frente a débil según se toleren conversiones implícitas.
- **Gestión de memoria**: manual (C/C++), con **recolector de basura** (*garbage collector*: Java, C#, Python, JavaScript) o con propiedad verificada en compilación (Rust).
- **Paradigmas**: los lenguajes generalistas actuales son **multiparadigma**: combinan orientación a objetos, programación funcional (funciones de orden superior, inmutabilidad) e imperativa.

**Java** (1995, hoy de Oracle; ediciones OpenJDK libres):

- **Modelo**: compila a **bytecode** que ejecuta la **JVM** («*write once, run anywhere*»); tipado estático, orientación a objetos con genéricos y rasgos funcionales (lambdas, *streams*).
- **Versionado**: una versión cada **6 meses** y una **LTS cada dos años**: Java 8, 11, 17, **21 (sep-2023)** y **25 (sep-2025)**.
- **Ecosistema**: construcción con Maven/Gradle, framework **Spring/Spring Boot** (tema 56); otros lenguajes sobre la JVM: **Kotlin** (tema 59), Scala.
- **Uso**: el estándar del software corporativo y de las administraciones públicas.

**Python** (1991, Python Software Foundation):

- **Modelo**: interpretado (implementación de referencia CPython), **tipado dinámico** fuerte, sintaxis por indentación, multiparadigma; admite anotaciones de tipos opcionales verificables con herramientas externas.
- **Versionado**: una versión anual cada octubre (3.13 en 2024, **3.14 en oct-2025**); **Python 2 quedó sin soporte el 1 de enero de 2020**.
- **Ecosistema**: paquetes con **pip** desde el repositorio **PyPI**, entornos virtuales; dominio absoluto en **ciencia de datos e IA** (NumPy, pandas, PyTorch, tema 34); web con Django y FastAPI (tema 56); scripting y automatización de sistemas.
- **Uso**: primer lenguaje de los índices de popularidad y lengua franca del análisis de datos.

**JavaScript y TypeScript**: el lenguaje de la web en navegador y, con **Node.js**, también en servidor; TypeScript le añade tipado estático. Tratados en el tema 57.

| | Java | Python | JavaScript/TypeScript |
| --- | --- | --- | --- |
| Ejecución | Bytecode en JVM | Interpretado | Interpretado/JIT (motor V8) |
| Tipado | Estático | Dinámico (hints opcionales) | Dinámico / estático con TS |
| Memoria | Garbage collector | Garbage collector | Garbage collector |
| Gestor de paquetes | Maven/Gradle | pip (PyPI) | npm |
| Dominio típico | Corporativo, AAPP | Datos, IA, scripting | Web, full-stack |

**Otros lenguajes relevantes**: **C#** (Microsoft, plataforma .NET, primo directo de Java), **C y C++** (sistemas, rendimiento extremo, código nativo), **Go** (Google, 2009: simplicidad y concurrencia, común en infraestructura cloud: Docker y Kubernetes están escritos en Go) y **Rust** (seguridad de memoria sin recolector de basura; adoptado en el kernel de Linux y Android para código crítico).

## Plataformas de desarrollo: Java, .NET y PHP

Los temarios piden, además de los lenguajes, sus plataformas: el entorno de ejecución, las bibliotecas y el ecosistema de frameworks con que se construyen las aplicaciones corporativas.

### Java y Jakarta EE

- **Plataforma**: el **JDK** reúne compilador, JVM y biblioteca estándar. Sobre la edición estándar (**Java SE**) se construye la empresarial: **Jakarta EE** (antes Java EE; cedida por Oracle a la **Fundación Eclipse** en 2017; versión **11, de 2025**), un conjunto de especificaciones para aplicaciones corporativas (Servlets, **JPA** de persistencia, CDI de inyección de dependencias, JAX-RS para REST) que implementan los **servidores de aplicaciones** (WildFly, Payara, WebSphere) y, en su parte web, el contenedor **Apache Tomcat**.
- **Spring y Spring Boot**: el framework dominante de facto, basado en **inversión de control e inyección de dependencias**; **Spring Boot** añade autoconfiguración, servidor embebido y métricas (*actuator*). Versión **4.0 (nov-2025)**, con Jakarta EE 11 como base y **Java 17** como mínimo.
- **Persistencia**: **JPA** (Jakarta Persistence) es el estándar ORM; **Hibernate**, su implementación más extendida.
- **Herramientas**: construcción y dependencias con **Maven** o **Gradle**; pruebas con **JUnit 5** (tema 27).

```java
@RestController
public class SaludoController {
    @GetMapping("/saludo/{nombre}")
    public String saludar(@PathVariable String nombre) {
        return "Hola, " + nombre;
    }
}
```

### .NET

- **Plataforma**: la de Microsoft, hoy **libre y multiplataforma** (Windows, Linux, macOS); el **.NET Framework** clásico, solo Windows, quedó congelado en la versión 4.8. Versión anual cada noviembre con **LTS los años impares**: .NET 8 (2023) y **.NET 10 (nov-2025**, con **C# 14**, soporte hasta nov-2028).
- **Modelo**: **C#** (y F#) compilan a un código intermedio (**CIL**) que ejecuta el runtime **CLR**, el equivalente de la JVM.
- **Pila corporativa**: **ASP.NET Core** (web y APIs), **Entity Framework Core** (ORM), **Blazor** (interfaces web con C#), .NET MAUI (móvil, tema 59) y paquetes con **NuGet**.

```csharp
var app = WebApplication.CreateBuilder(args).Build();
app.MapGet("/saludo/{nombre}", (string nombre) => $"Hola, {nombre}");
app.Run();
```

### PHP

- **Plataforma**: lenguaje interpretado de servidor (motor Zend, con **JIT desde PHP 8.0**), ejecutado tras Nginx/Apache mediante **PHP-FPM**. Versión vigente **8.5 (nov-2025)**, con tipado gradual moderno.
- **Ecosistema**: dependencias con **Composer** (repositorio Packagist); frameworks **Laravel** y **Symfony**; base de los grandes CMS (**WordPress**, Drupal; tema 55).
- **Uso**: domina la web de gran volumen (WordPress por sí solo supera el 40 % de los sitios) y es habitual en portales y sedes de las AAPP.

| | Java | .NET | PHP |
| --- | --- | --- | --- |
| Runtime | JVM (bytecode) | CLR (CIL) | Intérprete Zend + JIT |
| Web/API | Spring Boot, JAX-RS | ASP.NET Core | Laravel, Symfony |
| ORM | JPA/Hibernate | EF Core | Eloquent, Doctrine |
| Paquetes | Maven/Gradle | NuGet | Composer |
| Versión vigente | Java 25 LTS (sep-2025) | .NET 10 LTS (nov-2025) | PHP 8.5 (nov-2025) |

## Programación low-code y no-code

Son enfoques de desarrollo sobre **plataformas visuales** que reducen (o eliminan) el código a escribir, para acelerar la entrega y abrir el desarrollo a perfiles no técnicos. Conviene distinguirlos:

- **Low-code**: desarrollo sobre interfaces visuales y componentes preconstruidos, con **algo de código** para la lógica compleja o las integraciones. Destinatario: desarrolladores (más productividad) y perfiles semitécnicos.
- **No-code**: creación de aplicaciones **sin escribir código**, combinando bloques preconfigurados mediante arrastrar y soltar. Destinatario: usuarios de negocio sin experiencia en programación.
- **Citizen developer** (desarrollador ciudadano): empleado no informático que construye aplicaciones para su unidad con estas plataformas, idealmente bajo el gobierno y la supervisión del departamento TIC.

**Plataformas representativas**:

- **Microsoft Power Platform** (Power Apps, Power Automate): la más extendida en entornos corporativos, integrada con Microsoft 365.
- **Google AppSheet**: aplicaciones móviles y web sobre hojas de cálculo y fuentes de datos.
- **OutSystems y Mendix**: low-code empresarial para aplicaciones completas.
- **Zapier y Make**: automatización no-code de flujos entre servicios en la nube.
- **Airtable** (bases de datos colaborativas) y **WordPress** (creación de sitios web sin programar).

**Ventajas**:

- **Velocidad**: prototipos y aplicaciones sencillas en días, no meses.
- **Autonomía** de las unidades de negocio y descarga del departamento TIC.
- **Ahorro** en desarrollos pequeños y **colaboración** entre perfiles técnicos y funcionales.
- **Estandarización**: la plataforma resuelve infraestructura, despliegue y parte de la seguridad.

**Desventajas y riesgos**:

- **Restricciones funcionales**: cuando el requisito se sale del catálogo de bloques, la plataforma se queda corta.
- **Dependencia del proveedor** (*vendor lock-in*): la aplicación no es portable y queda atada a licencias y precios de la plataforma.
- ***Shadow IT***: proliferación de aplicaciones fuera del control del departamento TIC, con riesgos de seguridad, protección de datos y mantenimiento sin dueño.
- **Escalabilidad y rendimiento** limitados para sistemas críticos o de gran volumen.

La frontera actual es el **desarrollo asistido por IA generativa** (GitHub Copilot y asistentes similares), que genera código desde lenguaje natural: no elimina al programador, pero desplaza su trabajo hacia la especificación, la revisión y las pruebas.

## Fuentes {.unnumbered .unlisted}

- E. Gamma, R. Helm, R. Johnson y J. Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison-Wesley, 1994.
- W. Brown, R. Malveau, H. McCormick y T. Mowbray, *AntiPatterns: Refactoring Software, Architectures, and Projects in Crisis*, Wiley, 1998.
- R. C. Martin, *Agile Software Development: Principles, Patterns, and Practices*, Prentice Hall, 2002 (principios SOLID).
- Documentación oficial de Java (Oracle/OpenJDK), Python (PSF) y Microsoft Power Platform (consulta: julio de 2026).
- Documentación y anuncios oficiales de las plataformas: Jakarta EE 11 (Eclipse Foundation, 2025), Spring Boot 4.0 (20-nov-2025), .NET 10 LTS (11-nov-2025) y PHP 8.5 (20-nov-2025), verificados online en julio de 2026.
