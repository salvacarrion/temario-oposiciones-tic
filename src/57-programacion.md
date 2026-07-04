# Programación
## Programación Orientada a Objetos (POO)

**Programación Orientada a Objetos**

La Programación Orientada a Objetos (POO) es un paradigma de
programación que organiza el software en torno a **objetos**, los cuales
representan entidades del mundo real o conceptual. Cada objeto contiene
**datos** (atributos) y **comportamientos** (métodos), interactuando con
otros objetos para resolver problemas de software.

.

**Diseño Orientado a Objetos (DOO)**

Es un enfoque de diseño de software que modela un sistema como un
conjunto de objetos que interactúan. Este diseño se fundamenta en tres
**principios básicos**:

- **Abstracción**: Identificación de las características esenciales de
  un objeto, ignorando los detalles irrelevantes para el contexto.

- **Modularidad**: División del sistema en componentes independientes y
  reutilizables.

- **Ocultamiento de Información**: Garantiza que los detalles internos
  de un objeto queden protegidos, interactuando a través de interfaces
  claramente definidas.

**Características Principales**

- **Abstracción**: Denota las características esenciales de un objeto,
  permitiendo enfocarse en lo relevante y omitir detalles innecesarios.

- **Encapsulamiento**: Reúne todos los elementos que pertenecen a una
  entidad al mismo nivel de abstracción, protegiendo los datos y
  comportamientos internos del objeto.

- **Ocultamiento de Información**: Cada objeto expone una **interfaz**
  para interactuar con otros, evitando que puedan cambiar su estado
  interno de manera inesperada y eliminando efectos secundarios.

- **Polimorfismo**: Permite que métodos con el mismo nombre tengan
  comportamientos diferentes según el objeto que los invoque.

**Tipos de Polimorfismo**

- **Polimorfismo de Sobrecarga (Overloading)**: Métodos con el mismo
  nombre pero diferentes parámetros dentro de la misma clase. El método
  se selecciona automáticamente según los tipos de datos suministrados.

  - **Ejemplo:** 1 + 2, "hello" + "world" (operaciones distintas pero
    comparten el operador “+”)

- **Polimorfismo Paramétrico (Polimorfismo de Plantillas)**: Funciones
  genéricas que funcionan con cualquier tipo de datos.

  - **Ejemplo:** “**object.draw()**” puede referirse a
    “**square.draw()**” o “**circle.draw()**”, dependiendo del objeto.

  - **Function Signature**: Identifica a la función mediante su nombre y
    argumentos (no incluye el tipo de retorno).

- **Polimorfismo de Inclusión, de Redefición o Subtipado (Override)**:
  Una subclase redefine un método existente en la superclase con los
  mismos argumentos.

  - **Ejemplo:** “**piece.move()**” implementado en “**bishop.move()**”
    y “**knight.move()**”

- **Herencia**: Organiza y facilita el polimorfismo y el
  encapsulamiento, permitiendo que las subclases hereden atributos y
  métodos de las superclases.

**Modularidad**

Es la propiedad que permite subdividir una aplicación en partes
independientes más pequeñas, buscando un **bajo acoplamiento** y una
**alta cohesión**.

- **Acoplamiento**: Evalúa la interdependencia entre módulos. Lo ideal
  es tener módulos **poco acoplados** (independientes).

- **Cohesión**: Mide la conexión funcional entre elementos de un módulo.
  Se busca módulos **fuertemente cohesionados** que operen eficazmente
  entre sí.

**Accesibilidad de Miembros (Modificadores de Acceso)**

- **public**: El campo o método es visible desde <u>cualquier clase</u>.

- **protected**: Visible en la clase donde se define y en sus subclases,
  <u>incluso si están en paquetes diferentes</u>.

- **default (package-protected / friendly):** Visible solo dentro del
  <u>mismo paquete</u>.

- **private**: Visible únicamente <u>dentro de la clase</u> donde se
  define.

**Objetos y Clases**

- **Clase**: Define las características de un objeto, incluyendo
  propiedades (atributos) y métodos (comportamientos).

- **Objeto**: Instancia concreta de una clase que reside en memoria y
  puede ser referenciada por un identificador.

**Características Fundamentales de los Objetos**

- **Identidad ("nombre")**: Propiedad que distingue a un objeto de
  otros.

- **Estado ("valores")**: Conjunto de atributos y sus valores en un
  momento dado.

- **Comportamiento ("métodos")**: Operaciones que el objeto puede
  realizar o respuestas a mensajes de otros objetos.

**Patrones y Antipatrones**

- **Patrones**: Soluciones reutilizables para problemas comunes en
  diseño de software.

- **Antipatrones**: Prácticas contraproducentes que deben evitarse por
  sus consecuencias negativas conocidas.

**Patrones de Diseño Orientado a Objetos**

**1. Patrones Creacionales**

- **Factoría Abstracta (Abstract Factory o Kit)**: Define una interfaz
  para crear familias de objetos relacionados sin especificar sus clases
  concretas.

- **Factory Method (Fábrica de Objetos)**: Centraliza en una clase la
  creación de objetos de subtipos específicos, ocultando al usuario los
  detalles de instanciación.

- **Prototype (Prototipo)**: Crea nuevos objetos clonando una instancia
  existente.

- **Singleton**: Garantiza que una clase tenga **una única instancia** y
  proporciona un punto de acceso global a ella.

**2. Patrones Estructurales**

- **Adapter (Adaptador)**: Permite que clases con interfaces
  incompatibles trabajen juntas mediante una interfaz común.

- **Bridge (Puente)**: Desacopla una abstracción de su implementación,
  permitiendo modificarlas independientemente.

- **Composite**: Compone objetos en estructuras de árbol para
  representar jerarquías parte-todo, permitiendo tratar objetos
  individuales y compuestos de manera uniforme.

- **Contenedor**: Objeto que **contiene** otros objetos.

- **Decorator (Decorador)**: Añade dinámicamente funcionalidades a un
  objeto sin modificar su estructura original.

- **Facade (Fachada)**: Proporciona una interfaz unificada y
  simplificada para un conjunto de interfaces más complejas.

- **Flyweight (Peso Ligero)**: Reduce la redundancia de objetos
  similares compartiendo su estado común para ahorrar memoria y mejorar
  rendimiento.

- **Proxy**: Ofrece un sustituto o representante de otro objeto para
  controlar el acceso a este.

**3. Patrones de Comportamiento**

- **Chain of Responsibility (Cadena de Responsabilidades)**: Pasa una
  petición a lo largo de una cadena de objetos receptores hasta que uno
  la maneja.

- **Command (Comando)**: Encapsula una solicitud como un objeto,
  permitiendo parametrizar clientes con diferentes solicitudes y encolar
  o registrar solicitudes.

- **Functor**: Objeto que actúa como una función o método, permitiendo
  tratar funciones como objetos de primera clase.

- **Interpreter (Intérprete)**: Define una representación para la
  gramática de un lenguaje y un intérprete que usa dicha representación
  para interpretar sentencias en el lenguaje.

- **Iterator (Iterador)**: Proporciona un modo de acceder
  secuencialmente a los elementos de un objeto agregado sin exponer su
  representación interna.

- **Memento**: Permite capturar y externalizar el estado interno de un
  objeto sin violar la encapsulación, para poder restaurarlo
  posteriormente.

- **MVC (Modelo Vista Controlador)**: Separa la aplicación en tres
  componentes interrelacionados:

  - **Modelo**: Gestiona los datos y la lógica de negocio.

  - **Vista**: Presenta la información al usuario.

  - **Controlador**: Maneja la interacción del usuario y actualiza el
    modelo y la vista.

- **Mediator (Mediador)**: Define un objeto que encapsula cómo
  interactúan un conjunto de objetos, promoviendo un acoplamiento débil.

- **Observer (Observador)**: Establece una dependencia uno a muchos
  entre objetos, de manera que cuando uno cambia de estado, notifica
  automáticamente a sus dependientes.

- **State (Estado)**: Permite a un objeto alterar su comportamiento
  cuando su estado interno cambia.

- **Strategy (Estrategia)**: Define una familia de algoritmos, encapsula
  cada uno y los hace intercambiables según las necesidades del cliente.

**4. Otros “patrones”**

- **Inmutable**: Objeto creado con un estado fijo que no puede cambiar
  durante su ciclo de vida.

- **De Primera Clase**: Objeto que puede ser utilizado sin
  restricciones, como pasarlo como parámetro, asignarlo a variables o
  retornarlo en funciones.

- **Metaobjeto**: Objeto que define el comportamiento y características
  de otros objetos, similar a una clase pero puede ser un objeto en sí
  mismo.

**Antipatrones de Diseño**

- **Todopoderoso**: Objeto que "sabe demasiado o hace demasiado",
  centralizando excesiva funcionalidad y creando dependencia.

- **The Blob ("Clases Gigantes")**: Clases con muchos atributos u
  operaciones, difíciles de mantener, reutilizar y probar, rompiendo las
  ventajas de la POO.

- **Lava Flow ("Código Muerto")**: Código no óptimo entregado antes de
  estar terminado o suficientemente probado, que no puede ser modificado
  una vez expuesto.

- **Poltergeists ("Clases Fantasma")**: Objetos de ciclo de vida corto
  cuya única función es invocar métodos de otros objetos sin aportar
  funcionalidad real.

- **Golden Hammer ("Para un martillo, todo son clavos")**: Uso
  inapropiado de una tecnología o patrón para resolver cualquier
  problema, incluso cuando no es adecuado.

- **Spaghetti Code ("Código Espagueti")**: Código mal estructurado con
  excesivos **if** o **switch**, dificultando su comprensión y
  mantenimiento.

- **Cut & Paste Programming ("Cortar y Pegar Código")**: Reutilización
  de código mediante copia directa, lo que puede generar redundancia y
  errores difíciles de rastrear.

## Programación Low-Code y No-Code

**Programación No-Code**

Técnica diseñada para que usuarios con conocimientos básicos de
programación puedan desarrollar aplicaciones y soluciones de software.
Este enfoque se basa en el uso de **interfaces visuales** y una mínima
cantidad de código, lo que **reduce la complejidad** del desarrollo y
permite que los usuarios se concentren en la **solución de problemas** y
la **definición de requisitos funcionales**.

Su audiencia principal son personas con **nociones básicas** de
programación, quienes pueden aprovechar estas herramientas para crear
soluciones personalizadas sin la necesidad de ser programadores
profesionales.

**Programación No-Code**

Permite la creación de aplicaciones y soluciones de software sin
escribir código en absoluto. Se basa en **plataformas intuitivas** que
ofrecen **bloques de construcción preconfigurados** y componentes
reutilizables que los usuarios pueden combinar mediante herramientas de
arrastrar y soltar.

Está dirigida a personas **sin experiencia previa en programación**,
democratizando el acceso al desarrollo de software y fomentando la
creatividad en usuarios sin conocimientos técnicos.

**Plataformas más conocidas**

Algunas de las plataformas más utilizadas en estos enfoques son:

- **WordPress**, popular para la creación de sitios web.

- **Honeycode**, para el desarrollo de aplicaciones.

- **AppSheet**, centrada en la construcción de aplicaciones móviles y
  web.

- **PowerApps**, que permite la integración con el ecosistema de
  Microsoft.

- **Figma**, orientada al diseño y prototipado de interfaces web y
  aplicaciones.

Estas herramientas se han consolidado como opciones líderes debido a su
facilidad de uso y capacidad de adaptación a diferentes casos de uso.

**Ventajas**

Las principales ventajas de la programación Low-Code y No-Code incluyen:

- **Agilidad**: Permite crear aplicaciones en menos tiempo.

- **Autonomía**: Usuarios no técnicos pueden desarrollar sin depender de
  programadores.

- **Ahorro**: Reduce costes al minimizar la necesidad de desarrolladores
  especializados.

- **Colaboración**: Fomenta el trabajo conjunto entre departamentos
  técnicos y no técnicos.

- **Facilidad de uso**: Interfaces intuitivas accesibles para usuarios
  con poca o ninguna formación.

- **Velocidad de desarrollo**: Ideal para prototipos o aplicaciones que
  deben desarrollarse rápidamente.

- **Mayor eficiencia**: Automatiza tareas repetitivas y simplifica el
  desarrollo.

**Desventajas**

A pesar de sus ventajas, estos enfoques presentan **limitaciones** que
deben considerarse:

- **Restricciones funcionales**: Las aplicaciones creadas pueden carecer
  de flexibilidad o funcionalidades avanzadas.

- **Dependencia de la herramienta**: Los usuarios quedan atados a las
  capacidades y licencias de la plataforma utilizada.

- **Conocimientos técnicos limitados**: Puede dificultar la
  personalización profunda o la resolución de problemas complejos.

- **Problemas de seguridad**: Algunas plataformas pueden no cumplir con
  estándares robustos de seguridad, exponiendo riesgos en aplicaciones
  críticas.
