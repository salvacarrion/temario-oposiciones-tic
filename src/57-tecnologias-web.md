# Tecnologías web

La web se construye sobre tres tecnologías estándar que el navegador interpreta directamente: **HTML** (estructura y contenido), **CSS** (presentación) y **JavaScript** (comportamiento). HTML deriva de los lenguajes de marcado: **SGML** (Standard Generalized Markup Language, ISO 8879) fue el metalenguaje del que nacieron **HTML** (marcado con semántica y formato) y **XML** (descripción de datos). Hoy los estándares los mantienen el **WHATWG** (HTML como *Living Standard*), el **W3C** (CSS y APIs) y **Ecma International** (ECMAScript, la especificación de JavaScript).

## HTML5

HTML5 fue Recomendación del **W3C el 28 de octubre de 2014**; desde el acuerdo W3C-WHATWG de **2019**, HTML es un **estándar vivo** (*HTML Living Standard*) mantenido por el WHATWG, sin números de versión. «HTML5» se usa como etiqueta genérica de la plataforma moderna.

Estructura básica de un documento:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="styles.css">
  <title>Mi página</title>
</head>
<body>
  <h1>Mi primer encabezado</h1>
  <p>Mi primer párrafo.</p>
  <script src="app.js"></script>
</body>
</html>
```

- **Declaración y raíz**: `<!DOCTYPE html>` (activa el modo estándar del navegador) y `<html>`.
- **Elementos del head**: `<meta>` (charset, viewport), `<title>`, `<link>`, `<style>`, `<script>`.
- **Semántica estructural** (novedad clave de HTML5, sustituye a los `<div>` genéricos): `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`/`<figcaption>`. Mejora la accesibilidad y el SEO.

**Texto y agrupación**:

- **Semánticos**: `<em>` (énfasis, cursiva) y `<strong>` (importancia, negrita); preferibles a los presentacionales `<i>`/`<b>`.
- **Listas**: no ordenadas (`<ul>`), ordenadas (`<ol>`) y de definiciones (`<dl>` con `<dt>` término y `<dd>` descripción).
- **Tablas**: `<table>` con filas `<tr>`, celdas de encabezado `<th>` y de datos `<td>`; secciones opcionales `<thead>`, `<tbody>`, `<tfoot>`. Fusión de celdas: `rowspan` (filas) y `colspan` (columnas).

```html
<table>
  <thead>
    <tr><th>Producto</th><th>Precio</th></tr>
  </thead>
  <tbody>
    <tr><td>Teclado</td><td>25</td></tr>
    <tr><td colspan="2">Envío gratuito</td></tr>
  </tbody>
</table>
```

**Formularios**: HTML5 amplió notablemente los formularios con nuevos tipos de entrada y validación nativa.

- **Atributos de `<form>`**: `action` (URL destino), `method` (**GET**: datos en la URL; **POST**: datos en el cuerpo), `enctype` (`multipart/form-data` para subir ficheros).
- **Tipos de `<input>` clásicos**: text, password, checkbox, radio, submit, reset, file, hidden, button.
- **Tipos nuevos de HTML5**: email, url, tel, number, range, date, time, color, search. El navegador aporta controles y validación adecuados a cada tipo.
- **Validación nativa**: atributos `required`, `pattern` (expresión regular), `min`/`max`, `maxlength`, `placeholder`, `autocomplete`; evita JavaScript para las comprobaciones básicas.

```html
<form action="/enviar" method="post">
  <label for="correo">Correo</label>
  <input type="email" id="correo" name="correo" required>
  <input type="submit" value="Enviar">
</form>
```

**Multimedia y gráficos**: HTML5 eliminó la dependencia de plugins (Flash fue retirado por Adobe el **31 de diciembre de 2020**).

- **`<video>` y `<audio>`**: reproducción nativa con controles (`controls`, `autoplay`, `loop`) y varias `<source>` alternativas. Formatos habituales: video/mp4, video/webm; audio/mpeg (MP3), audio/ogg. `<track>` añade subtítulos.
- **`<canvas>`**: superficie de dibujo por JavaScript (mapa de bits): gráficas, juegos.
- **SVG**: gráficos vectoriales escalables en XML, integrables en el documento.
- **`<object>` y `<embed>`**: incrustan recursos externos (p. ej. un PDF); `<embed>` se estandarizó precisamente en HTML5.

```html
<video controls width="640">
  <source src="pelicula.mp4" type="video/mp4">
  <source src="pelicula.webm" type="video/webm">
  <track src="subtitulos.vtt" kind="subtitles" srclang="es">
</video>
```

**APIs de la plataforma** (accesibles desde JavaScript): almacenamiento local (**Web Storage**: `localStorage` persistente y `sessionStorage` por pestaña), **geolocalización**, **Web Workers** (hilos en segundo plano), **History API** (navegación de las SPA), arrastrar y soltar, y **WebSocket** (tema [56](56-arquitecturas-de-desarrollo-web.md)).

**Elementos y atributos obsoletos**: su función pasó a CSS.

- **Etiquetas**: `<applet>` (Java), `<center>` (→ text-align), `<font>` (→ font-family), `<s>`/`<strike>`/`<u>` (→ text-decoration), `<frame>`/`<frameset>`.
- **Atributos**: align (→ text-align), background (→ background-image), border (→ border-width), vspace/hspace (→ padding/margin), nowrap (→ white-space).

**Nota histórica: XHTML**. Reformulación de HTML como aplicación XML (documentos bien formados: etiquetas siempre cerradas y en minúsculas, atributos entrecomillados). El W3C abandonó la línea XHTML 2.0 en favor de HTML5; sobrevive como «sintaxis XML» opcional del estándar vivo.

## CSS3

CSS (*Cascading Style Sheets*, hojas de estilo en cascada) describe la presentación de un documento separándola de su estructura. Desde CSS3 el estándar no es un bloque monolítico sino **módulos independientes** del W3C (selectores, flexbox, grid, animaciones...) que evolucionan por separado.

- **Regla CSS**: selector + bloque de declaraciones: `p { color: red; }`.
    - **Selector**: a qué elementos se aplica.
    - **Declaración**: propiedad y valor asignados.
- **Formas de aplicar estilo**: hoja externa (`<link rel="stylesheet" href="styles.css">`, la recomendada), interna (`<style>`) y en línea (atributo `style`).
- **La cascada**: cuando varias reglas afectan a un elemento, gana la de mayor **especificidad** (en orden: estilos en línea > selectores de id > de clase/atributo/pseudoclase > de tipo); a igualdad, la última declarada. `!important` invierte la prioridad (uso desaconsejado). Muchas propiedades se **heredan** de padre a hijo (color, fuente).

**Selectores** principales:

| Ejemplo | Qué selecciona |
| --- | --- |
| `*` | Todos los elementos |
| `p` | Todos los elementos `<p>` |
| `#firstname` | El elemento con id="firstname" |
| `.intro` | Los elementos con class="intro" |
| `p.intro` | Los `<p>` con class="intro" |
| `.name1.name2` | Elementos con ambas clases a la vez |
| `div, p` | Todos los `<div>` y todos los `<p>` |
| `div p` | Los `<p>` descendientes de un `<div>` |
| `div > p` | Los `<p>` hijos directos de un `<div>` |
| `div + p` | El `<p>` inmediatamente posterior a un `<div>` |
| `p ~ ul` | Los `<ul>` hermanos posteriores de un `<p>` |
| `a:hover`, `li:first-child` | Pseudoclases (estado o posición) |
| `p::before`, `p::first-line` | Pseudoelementos (partes del elemento) |
| `input[type="text"]` | Selector de atributo |

**Modelo de caja**: todo elemento es una caja con **contenido + padding (relleno) + border + margin**. Con `box-sizing: border-box`, el ancho declarado incluye padding y borde (el ajuste habitual hoy).

**Unidades**: absolutas (`px`) y relativas: `em` (respecto a la fuente del elemento), `rem` (respecto a la raíz), `%`, `vw`/`vh` (porcentaje del ancho/alto de la ventana). Las relativas son la base del diseño adaptable.

**Maquetación (layout)**:

- **`display`**: block, inline, inline-block, none; y los modos modernos flex y grid.
- **`position`**: static (flujo normal), relative, absolute, fixed, sticky; con `z-index` para el apilamiento.
- **Flexbox** (`display: flex`): maquetación en **una dimensión** (fila o columna): alineación y distribución del espacio entre elementos (`justify-content`, `align-items`, `gap`, `flex-wrap`). Es el estándar para barras, menús y componentes.
- **Grid** (`display: grid`): maquetación en **dos dimensiones** (filas y columnas): `grid-template-columns: 1fr 2fr;` define la retícula y los elementos se colocan en sus celdas o áreas. Es el estándar para la estructura general de la página.
- **Media queries** (`@media (max-width: 768px) { ... }`): aplican reglas según las características del dispositivo (ancho, orientación, esquema de color); son la base del **diseño web adaptativo** (tema [58](58-accesibilidad-y-usabilidad.md)).

```css
/* Flexbox: una dimensión (barra de navegación) */
.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

/* Grid: dos dimensiones (estructura de página) */
.pagina {
  display: grid;
  grid-template-columns: 200px 1fr;
}

/* Media query: en pantallas estrechas, una sola columna */
@media (max-width: 768px) {
  .pagina { grid-template-columns: 1fr; }
}
```

**Efectos dinámicos**:

- **Transiciones** (`transition`): animan el cambio de una propiedad (color, tamaño) entre dos estados.
- **Transformaciones** (`transform`): trasladan, rotan y escalan sin alterar el flujo del documento.
- **Animaciones** (`@keyframes` + `animation`): secuencias con fotogramas clave, sin JavaScript.

**Variables y funciones**: las **propiedades personalizadas** permiten centralizar valores en cascada; `calc()` mezcla unidades:

```css
:root { --color-primario: #003366; }

.boton {
  color: var(--color-primario);
  width: calc(100% - 2rem);
  transition: background-color 0.3s ease;
}
.boton:hover { transform: scale(1.05); }
```

**Preprocesadores**: **Sass** y **LESS** compilan a CSS añadiendo anidamiento, mixins y funciones; siguen siendo comunes, aunque las variables y funciones nativas de CSS han reducido su necesidad.

## JavaScript y TypeScript

**JavaScript** es el lenguaje de programación de la web: interpretado, **dinámico y débilmente tipado**, multiparadigma (imperativo, funcional y orientado a objetos) y **basado en prototipos**. Es un dialecto del estándar **ECMAScript** (**ECMA-262**), con ediciones anuales desde 2015; la vigente es **ECMAScript 2026 (17.ª edición, aprobada el 30 de junio de 2026)**. «ES6» (ES2015) marcó la modernización del lenguaje.

**Fundamentos**:

- **Declaración de variables**: `let` (ámbito de bloque) y `const` (constante) sustituyen al antiguo `var` (ámbito de función).
- **Tipos primitivos**: number, string, boolean, null, undefined, symbol, bigint; y los objetos (incluidas funciones y arrays).
- **Prototipos**: cada objeto hereda de un prototipo; las «clases» de ES6 son azúcar sintáctico sobre este mecanismo.

**Sintaxis moderna (ES6+)**:

- **Funciones flecha**: forma concisa que no redefine `this`: `const suma = (a, b) => a + b;`
- **Literales de plantilla**: cadenas con interpolación y multilínea: `` `Hola ${nombre}` ``.
- **Desestructuración**: extrae valores de arrays u objetos: `const [x, y] = punto; const { id } = usuario;`
- **Spread y rest** (`...`): expande iterables (`[...a, ...b]`) o agrupa argumentos (`function f(...args)`).
- **Parámetros por defecto**: `function saluda(nombre = "mundo")`.
- **Clases**: `class Persona { constructor(nombre) { this.nombre = nombre; } }` con herencia (`extends`, `super`).
- **Módulos**: `export` / `import` con carga nativa en el navegador (`<script type="module">`).
- **Colecciones**: `Set` (valores únicos) y `Map` (diccionario con claves de cualquier tipo).
- **Iteración**: `for...of` recorre valores de iterables (arrays, cadenas); `for...in`, propiedades de un objeto.
- **Generadores**: funciones que pausan y reanudan su ejecución (`function*` + `yield`).

```javascript
const usuarios = [
  { id: 1, nombre: "Ana" },
  { id: 2, nombre: "Luis" }
];

// Flecha, desestructuración y literal de plantilla
const saludar = ({ nombre }) => `Hola, ${nombre}`;

// Spread: copia ampliada sin mutar el original
const ampliados = [...usuarios, { id: 3, nombre: "Eva" }];

// Clases con herencia
class Empleado {
  constructor(nombre) { this.nombre = nombre; }
  presentarse() { return `Soy ${this.nombre}`; }
}
class Funcionario extends Empleado {
  presentarse() { return super.presentarse() + " (funcionario)"; }
}

// Set y Map
const unicos = new Set([1, 2, 2, 3]);        // {1, 2, 3}
const cargos = new Map([["ana", "jefa"]]);   // cargos.get("ana")
```

**Asincronía**: JavaScript ejecuta en un **único hilo** con un **bucle de eventos** (*event loop*): las operaciones de entrada/salida no bloquean, sino que encolan su continuación.

- **Promesas** (*Promises*): objeto que representa un resultado futuro; se encadenan con `.then()` y `.catch()`.
- **async/await** (ES2017): sintaxis secuencial sobre promesas; `await` espera el resultado dentro de una función `async`.
- **fetch**: API estándar para peticiones HTTP, sucesora de `XMLHttpRequest`:

```javascript
async function cargar() {
  const respuesta = await fetch("/api/datos");
  if (respuesta.ok) {
    const datos = await respuesta.json();
    console.log(datos);
  }
}
```

La misma petición con promesas encadenadas (el estilo previo a async/await):

```javascript
fetch("/api/datos")
  .then(respuesta => respuesta.json())
  .then(datos => console.log(datos))
  .catch(error => console.error(error));
```

- **AJAX**: nombre histórico (2005) de esta técnica: intercambiar datos con el servidor en segundo plano y actualizar la página sin recargarla. Entonces se hacía con `XMLHttpRequest` y XML; hoy, con `fetch` y JSON.

**DOM y eventos**: el navegador expone el documento como árbol de objetos (**DOM**) manipulable desde JavaScript; los manejadores de eventos reaccionan a las acciones del usuario. **JSON** (`JSON.parse` / `JSON.stringify`) es el formato de intercambio nativo (tema [60](60-soa-servicios-web-y-microservicios.md)).

```javascript
const boton = document.querySelector("#enviar");
boton.addEventListener("click", () => {
  document.querySelector(".resultado").textContent = "Enviado";
});
```

**TypeScript** (Microsoft, 2012, código abierto): **superconjunto tipado de JavaScript** que se **transpila** a JavaScript estándar; todo programa JavaScript válido es TypeScript válido.

- **Tipado estático opcional**: anotaciones (`function suma(a: number, b: number): number`), inferencia de tipos y comprobación en compilación: detecta errores antes de ejecutar.
- **Construcciones propias**: interfaces (`interface Usuario { id: number; nombre: string; }`), genéricos (`Array<T>`), enums, tipos unión (`string | null`).
- **Herramientas**: compilador `tsc` configurado con `tsconfig.json`; los editores aprovechan los tipos para autocompletar y refactorizar.
- **Adopción**: estándar de facto en proyectos medianos y grandes; **obligatorio en Angular** y mayoritario en React y Node.js.

```typescript
interface Usuario {
  id: number;
  nombre: string;
  rol?: "admin" | "editor";    // propiedad opcional con tipo unión
}

function buscar<T>(lista: T[], criterio: (x: T) => boolean): T | undefined {
  return lista.find(criterio);
}

const u: Usuario = { id: 1, nombre: "Ana" };
```

## Frameworks y entornos: Angular, React, Vue y Node.js

Las aplicaciones web actuales se construyen con frameworks de **componentes** reutilizables con estado. Los tres principales son Angular, React y Vue; Node.js lleva JavaScript al servidor. Los modelos de aplicación que habilitan (SPA, renderizado en cliente y servidor) se tratan en el tema [56](56-arquitecturas-de-desarrollo-web.md).

- **Angular** (Google): framework **completo y opinado**: incluye de serie todo lo que React delega en su ecosistema.
    - **AngularJS frente a Angular**: **AngularJS (1.x, 2010)**, el del patrón MVC con `$scope` y directivas `ng-*`, fue **descontinuado por Google en enero de 2022**; las aplicaciones que lo usan deben migrarse. **Angular (v2+, 2016)** es una reescritura total en TypeScript, incompatible con la anterior: son productos distintos pese al nombre.
    - **Arquitectura**: componentes con plantillas HTML, **servicios** compartidos mediante **inyección de dependencias**, enrutador y formularios (template-driven y reactivos) integrados; programación reactiva con **RxJS** (observables) y, desde las versiones recientes, **signals** como modelo de reactividad y componentes **standalone** (sin módulos NgModule) por defecto.
    - **Herramientas**: **Angular CLI** genera, compila, prueba y actualiza los proyectos (`ng new`, `ng update`).
    - **Versionado**: **dos versiones mayores al año** con 18 meses de soporte (6 activo + 12 LTS); la actual es **Angular 22 (mayo de 2026)**.
    - **Uso**: muy implantado en entornos corporativos y administraciones públicas, donde pesan la uniformidad, el TypeScript obligatorio y el soporte predecible.
- **React** (Meta, 2013, código abierto): **biblioteca** de interfaces de usuario, no framework completo: se centra en la capa de vista.
    - **Modelo**: componentes como funciones, sintaxis **JSX** (HTML dentro de JavaScript), **DOM virtual** (calcula la diferencia mínima a aplicar sobre el DOM real) y **flujo de datos unidireccional**.
    - **Hooks** (desde 16.8, 2019): estado y ciclo de vida en componentes de función: `useState`, `useEffect`.
    - **React 19 (diciembre de 2024)**: componentes de servidor (*Server Components*) y *Actions*, integrando el renderizado en servidor en el modelo.
    - **Ecosistema**: enrutado (React Router), estado global (Redux, Zustand), metaframework **Next.js**; **React Native** para móvil (tema [59](59-desarrollo-de-aplicaciones-moviles.md)).
    - **Uso**: el más extendido de la industria; máxima oferta de talento y de bibliotecas.
- **Vue** (Evan You, 2014, comunitario): framework **progresivo**: puede adoptarse desde una sola página mejorada hasta una SPA completa.
    - **Modelo**: componentes de fichero único (`.vue` con plantilla, script y estilo), reactividad automática y **Composition API** desde **Vue 3 (2020)**; ecosistema Nuxt (metaframework) y Pinia (estado).
    - **Uso**: curva de entrada suave; popular en proyectos medianos y en Asia.

Un mismo componente (un contador) en los tres frameworks ilustra sus sintaxis:

```javascript
// React: componente de función con el hook useState y JSX
function Contador() {
  const [valor, setValor] = useState(0);
  return (
    <button onClick={() => setValor(valor + 1)}>
      Pulsado {valor} veces
    </button>
  );
}
```

```typescript
// Angular: clase decorada con @Component y plantilla propia
@Component({
  selector: "app-contador",
  template: `<button (click)="incrementar()">Pulsado {{ valor }} veces</button>`
})
export class ContadorComponent {
  valor = 0;
  incrementar() { this.valor++; }
}
```

```html
<!-- Vue: componente de fichero único (.vue) con Composition API -->
<script setup>
import { ref } from "vue";
const valor = ref(0);
</script>

<template>
  <button @click="valor++">Pulsado {{ valor }} veces</button>
</template>
```

| | Angular | React | Vue |
| --- | --- | --- | --- |
| Naturaleza | Framework completo | Biblioteca de UI | Framework progresivo |
| Respaldo | Google (2016; AngularJS 2010) | Meta (2013) | Comunidad (2014) |
| Lenguaje | TypeScript obligatorio | JavaScript/TypeScript (JSX) | JavaScript/TypeScript |
| Rasgos | DI, RxJS, signals, CLI | DOM virtual, hooks, JSX | Reactividad, ficheros .vue |
| Versión | v22 (may-2026), semestral | 19 (dic-2024) | 3.x |

- **Node.js** (Ryan Dahl, 2009): **entorno de ejecución de JavaScript en el servidor** sobre el motor **V8** de Chrome.
    - **Modelo**: un solo hilo con bucle de eventos y **entrada/salida no bloqueante**: muy eficiente atendiendo muchas conexiones concurrentes; menos indicado para cálculo intensivo.
    - **npm**: su gestor de paquetes y el mayor registro de software del mundo; proyectos definidos por `package.json`.
    - **Frameworks de servidor**: **Express** (minimalista) y **NestJS** (estructurado, TypeScript, inspirado en Angular).
    - **Versionado**: versiones **LTS pares** (20, 22, 24...) con unos 30 meses de soporte; también ejecuta las herramientas del front-end (Vite, Angular CLI). Alternativas emergentes: Deno y Bun.

Un servicio HTTP mínimo con Express:

```javascript
import express from "express";

const app = express();
app.get("/api/saludo", (req, res) => res.json({ mensaje: "Hola" }));
app.listen(3000);
```

## Fuentes {.unnumbered .unlisted}

- HTML Living Standard (WHATWG, consulta: julio de 2026); HTML5, Recomendación W3C de 28 de octubre de 2014.
- Módulos CSS del W3C y MDN Web Docs (Mozilla), consulta: julio de 2026.
- ECMA-262, 17.ª edición (ECMAScript 2026, aprobada el 30 de junio de 2026).
- Documentación oficial de Angular (v22), React (19), Vue (3), TypeScript y Node.js (consulta: julio de 2026); anuncio de fin de soporte de AngularJS (Google, enero de 2022).
