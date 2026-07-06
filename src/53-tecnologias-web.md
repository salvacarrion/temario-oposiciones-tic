# Tecnologías web

!!! warning "Tema pendiente de revisión"
    Este tema **no ha sido revisado** ni actualizado. Su contenido puede estar
    incompleto, desactualizado o contener errores. Úsalo con precaución y
    contrástalo siempre con fuentes oficiales.


## Desarrollo de páginas web

**Lenguajes de marcas o de marcado**: Definen la estructura, la semántica y controlan el procesamiento de un documento digital.

- **SGML** (Standard Generalized Markup Language) → de este derivan **HTML** y **XML**.

Los **lenguajes de marcas** se usan para:

- **Describir contenido** (ej.: Bases de datos).
- **Definir formato** (ej.: Procesadores de texto).
- **Describir contenido y además dar formato** (ej.: HTML).

## HTML5

Estructura básica de un documento HTML5:

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>My First Heading</h1>
  <p>My first paragraph.</p>
</body>
</html>
```

- **Elementos previos**: `<!DOCTYPE html>`, `<html>`.
- **Elementos del head**: `<link>`, `<meta>`.
- **Elementos del body**: `<header>`, `<nav>`, `<section>`, `<aside>`, `<footer>`.

### Formato de texto

- Cursiva: `<em>`.
- Negrita: `<strong>`.

### Listas

Tres tipos principales:

- Listas no ordenadas: `<ul>`.
- Listas ordenadas: `<ol>`.
- Listas de definiciones: `<dl>`, `<dt>`, `<dd>` (recordatorio "LaTiDo").
    - d\_ = description.
    - \_l = list.
    - \_t = term.
    - \_d = details.

### Tablas

Definidas con `<table></table>`.

Opcionalmente se usan `<thead>`, `<tbody>` y `<tfoot>`.

```html
<table>
  <tr>
    <th>col1</th>
    <th>col2</th>
  </tr>
  <tr>
    <td>col1</td>
    <td>col2</td>
  </tr>
</table>
```

### Fusionar celdas:

- rowspan="2": Fusiona filas.
- colspan="2": Fusiona columnas.

### Elemento `<object>`

Representa un recurso externo (imagen, contexto de navegación anidado o recurso manejado por un plugin).

Se puede anidar; si uno falla, se carga el interno.

```html
<object type="application/pdf"
  data="/media/examples/In-CC0.pdf"
  width="250"
  height="200">
</object>
```

### Formularios

**Atributos del** `<form>`:

- action="URL", method="POST/GET", enctype="tipo de codificación", accept="jpg,png,tiff".

**Tipos de** `<input>`:

- text, password, checkbox, radio, submit, reset, file, hidden, image, button.

```html
<form action="enviar.php" method="post" enctype="multipart/form-data">
  Nombre<br/>
  <input type="text" name="nombre" value="" size="20" maxlength="30" />
  <input type="submit" name="enviar" value="Guardar cambios" />
  <input type="reset" name="limpiar" value="Borrar los datos introducidos" />
</form>
```

### Comentarios

```html
<!-- Mi comentario -->
```

### Multimedia

### Etiqueta `<video>`

```html
<video>
  <source src="video.mp4" type="video/mp4">
</video>
```

**MIME types**:

- video/mp4 (mp4).
- video/ogg (ogg).
- video/webM (webM).

### Etiqueta `<audio>`

```html
<audio>
  <source src="audio.mp3" type="audio/mpeg">
</audio>
```

**MIME types**:

- audio/mpeg (mp3).
- audio/ogg (ogg).
- audio/wav (wav).

### Etiqueta `<embed>`

Incluye una aplicación externa o contenido interactivo.

```html
<embed src="helloworld.swf">
<embed src="giphy.gif" height="200" width="300"></embed>
```

### Etiquetas y atributos obsoletos (deprecated)

### Etiquetas:

- (applet, embed) → `<object>`.
- center → text-align.
- font → font-family.
- (s, strike, u) → text-decoration.

### Atributos:

- align → text-align.
- background → background-image.
- border → border-width.
- (vspace, hspace) → padding.
- nowrap → white-space.

### XHTML

Una versión más estricta y basada en XML de HTML.

**XHTML** significa **eXtensible HyperText Markup Language**.

Definido como una aplicación XML y soportado por todos los navegadores principales.

**Nota**: **W3C decidió abandonar XHTML en favor de HTML**.

### Reglas

- Los elementos deben estar correctamente anidados: `<b><i>aaaaa</i></b>`.
- Los elementos deben cerrarse siempre: `<p></p>`.
- Los elementos vacíos deben cerrarse: `<br />`.
- Los elementos y atributos deben estar en minúsculas: `<html>`, class="".
- Los valores de los atributos deben estar entre comillas: href="https://..".
- La minimización de atributos está prohibida: checked="checked".

## CSS3 / Hojas de Estilo en Cascada

Mecanismo para describir cómo se mostrará un documento en pantalla, móvil o impresora.

### Aplicable a cualquier documento XML.

CSS funciona con reglas compuestas por:

- **Selector** y **Declaración**: p { color: red }.
    - **Selector**: Especifica los elementos afectados.
    - **Declaración**: Especifica las propiedades asignadas.

### Formas de uso

- `<link rel="stylesheet" href="styles.css">`.
- `<style></style>`.
- Estilo en línea con style="".

| Ejemplo       | Descripción del ejemplo                                                                 |
| ------------- | --------------------------------------------------------------------------------------- |
| #firstname    | Selecciona el elemento con id="firstname"                                               |
| .intro        | Selecciona todos los elementos con class="intro"                                        |
| .name1.name2  | Selecciona todos los elementos que tienen tanto name1 como name2 en su atributo class   |
| .name1 .name2 | Selecciona todos los elementos con name2 que son descendientes de un elemento con name1 |
| \*            | Selecciona todos los elementos                                                          |
| p             | Selecciona todos los elementos `<p>`                                                    |
| p.intro       | Selecciona todos los elementos `<p>` con class="intro"                                  |
| div, p        | Selecciona todos los elementos `<div>` y todos los elementos `<p>`                      |
| div p         | Selecciona todos los elementos `<p>` dentro de elementos `<div>`                        |
| div > p       | Selecciona todos los elementos `<p>` cuyo elemento padre es un `<div>`                  |
| div + p       | Selecciona el primer elemento `<p>` que está inmediatamente después de elementos `<div>` |
| p ~ ul        | Selecciona todos los elementos `<ul>` precedidos por un elemento `<p>`                  |

## JavaScript

- **JavaScript** : un lenguaje de programación imperativo, débilmente tipado, dinámico y basado en prototipos.
- Dialecto del estándar **ECMAScript** .

### Características de ECMAScript 2020

### Funciones de flecha

Una forma concisa de escribir funciones en JavaScript.

```javascript
const functionName = (arg1, arg2, ...) => {
  // body of the function
};
```

### Operador de propagación ( ...)

Expande iterables (matrices o cadenas) en lugares donde se esperan múltiples argumentos.

```javascript
let num1 = [40, 50, 60];
let num2 = [10, 20, 30, ...num1, 70, 80, 90, 100];
// Result: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

### Parámetros REST

Representa parámetros indefinidos como una matriz.

```javascript
function show(...args) {
  let sum = 0;
  for (let i of args) {
    sum += i;
  }
  console.log("Sum = " + sum);
}
```

### Literales de plantilla

Permite la creación de cadenas multilínea.

```javascript
let str1 = "Hello";
let str2 = "World";
let str = `${str1} ${str2}`;
```

### Asignación de desestructuración

Extrae datos de objetos y matrices en variables separadas.

```javascript
let fullname = ['Alan', 'Rickman'];
let [fname, lname] = fullname;
console.log(fname, lname);
```

### Clases

Define clases en JavaScript.

```javascript
class ClassName {
  // methods and constructor
}
```

### Funciones del generador

Funciones que pueden pausar y reanudar la ejecución.

```javascript
function* gen() {
  yield 100;
  yield;
  yield 200;
}

let mygen = gen();
console.log(mygen.next().value); // 100
console.log(mygen.next().value); // undefined
console.log(mygen.next().value); // 200
```

### Parámetros predeterminados

Inicializa los parámetros nombrados con valores predeterminados.

```javascript
var show = (a, b = 200) => {
  console.log(a + " " + b);
};
```

### IIFE (Expresiones de función invocadas inmediatamente)

Funciones que se ejecutan tan pronto como se definen.

```javascript
(function() {
  console.log("Hello World");
})();
```

### Bucle for...in

Itera a través de las propiedades de un objeto.

```javascript
function Mobile(model_no) {
  this.Model = model_no;
  this.Color = 'White';
  this.RAM = '4GB';
}

let Samsung = new Mobile("Galaxy");
for (let prop in Samsung) {
  console.log(prop + " : " + Samsung[prop]);
}
```

### Bucle for...of

Itera a través de objetos iterables (matrices, cadenas, etc.).

```javascript
let fruits = ['Apple', 'Banana', 'Mango', 'Orange'];
for (let value of fruits) {
  console.log(value);
}
```

### Conjunto

Crea una colección de valores únicos.

```javascript
let colors = new Set(['Green', 'Red', 'Orange', 'Yellow', 'Red']);
```

### Mapa

Crea un diccionario ordenado.

```javascript
let colors = new Map([
  ['1', 'Red'],
  ['2', 'Green'],
  ['3', 'Yellow'],
  ['4', 'Violet']
]);
```

### Prototipo

Agrega propiedades y métodos a los objetos.

```javascript
var myBook = new Book("Perl", "Tom");
Book.prototype.price = 100; // myBook.price == 100
```

### AJAX (JavaScript asíncrono y XML)

No es un lenguaje de programación, sino una técnica para intercambiar datos con un servidor detrás de escena utilizando XMLHttpRequest.

```javascript
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      processMyXMLObject(this);
    }
  };
  xhttp.open("GET", "ajax_info.txt", true);
  xhttp.send();
}
```

## AngularJS

- **AngularJS** : un marco de JavaScript desarrollado y mantenido por **Google** para crear aplicaciones del lado del cliente utilizando el patrón **MVC** (Modelo-Vista-Controlador).

### Directivas clave

- **ng-app** : inicia la aplicación y define el elemento raíz.
- **$scope** : se refiere al contexto de ejecución; conecta la vista, el modelo y el controlador.
- **ng-controller** : define el alcance del controlador y lo vincula con $scope.
- **ng-model** : vincula un campo de formulario (entrada, selección, área de texto) a la $scope vista.
- **ng-bind** : vincula los datos del modelo a la vista.

### Extensiones de AngularJS

- **ng-app** : define una aplicación AngularJS (elemento raíz).
- **ng-model** : vincula los valores de control HTML a los datos de la aplicación.
- **ng-bind** : vincula los datos de la aplicación a la vista HTML.

### Ejemplos

### Ejemplo 1

```html
<div ng-app="">
  <p>Name: <input type="text" ng-model="name"></p>
  <p ng-bind="name"></p>
</div>
```

### Ejemplo 2

```html
<div ng-app="myApp" ng-controller="myCtrl">
  First Name: <input type="text" ng-model="firstName"><br>
  Last Name: <input type="text" ng-model="lastName"><br>
  <br>
  Full Name: {{firstName + " " + lastName}}
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
  $scope.firstName = "John";
  $scope.lastName = "Doe";
});
</script>
```

### Expresiones en AngularJS

Las expresiones de AngularJS no admiten condicionales, bucles ni excepciones.

```html
<span>{{ quantity }}</span>
<span ng-bind="quantity"></span>
```

### Inicialización

```html
<div ng-app="" ng-init="points=[1,15,19,2,40]">
  <p>The third result is {{ points[2] }}</p>
</div>
```

### Directiva ng-repeat

Repite un elemento HTML.

```html
<div ng-app="" ng-init="names=['Jani','Hege','Kai']">
  <ul>
    <li ng-repeat="x in names">
      {{ x }}
    </li>
  </ul>
</div>
```

### Creación de directivas personalizadas

```html
<body ng-app="myApp">

<w3-test-directive></w3-test-directive>
<div w3-test-directive></div>
<div class="w3-test-directive"></div>
<!-- directive: w3-test-directive -->

<script>
var app = angular.module("myApp", []);
app.directive("w3TestDirective", function() {
  return {
    restrict: "EA", // E: Element, A: Attribute
    template: "<h1>Made by a directive!</h1>"
  };
});
</script>

</body>
```

### Otras directivas y filtros

- **Directivas** : ng-empty, ng-not-empty, ng-touched, ng-untouched, ng-valid, ng-invalid, ng-dirty, ng-pending, ng-pristine.
- **Filters**: currency, date, filter, json, limitTo, lowercase, number, orderBy, uppercase.

```html
<p>The name is {{ lastName | uppercase }}</p>
<li ng-repeat="x in names | filter : 'i'">{{ x }}</li>
```

### Componentes de una aplicación AngularJS

- **Vista**: El HTML.
- **Modelo**: Datos disponibles para la vista
- **Controlador**: Funciones JavaScript que manipulan los datos.

### Scope como el Modelo

- Objeto de JavaScript con propiedades y metodos disponibles para la Vista y el Controlador.

### Servicios

- Función u objeto disponible dentro de la aplicación de AngularJS.

```javascript
function($scope, $location) {
  // Use the $location service
}
```

- **$http Service**: Hace peticiones al servidor y gestiona las respuestas.

```javascript
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
  $http.get("welcome.htm").then(function(response) {
    $scope.myWelcome = response.data;
  });
});
```

### Input Field States

- $untouched: Sin tocar.
- $touched: Tocado.
- $pristine: No modificado.
- $dirty: Modificado.
- $invalid: Contenido inválido.
- $valid: Contenido válido.

### Routing in AngularJS

- Convierte la aplicación en un **Single Page Application (SPA)**.
- El contenedor para el enrutado de contenido se define con la directiva ng-view.
