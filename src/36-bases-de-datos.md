# Bases de datos

## Sistemas de gestión de bases de datos; el modelo ANSI

Una **base de datos** es un conjunto organizado de datos relacionados entre sí, almacenado con la mínima redundancia posible y accesible de forma concurrente por múltiples usuarios y aplicaciones. Un **sistema de gestión de bases de datos (SGBD o DBMS)** es el software que actúa de intermediario entre los datos, los usuarios y las aplicaciones: define la estructura, controla el acceso y garantiza la integridad y la seguridad.

- **Funciones del SGBD**:
    - **Definición (descripción)**: crear y modificar la estructura de los datos (esquemas, tipos, restricciones) mediante un lenguaje de definición de datos (DDL).
    - **Manipulación**: consultar, insertar, actualizar y borrar datos (DML).
    - **Control**: gestión de usuarios y permisos (DCL), control de concurrencia, transacciones, copias de seguridad y recuperación ante fallos.
- **Ventajas frente a los sistemas de ficheros**: independencia entre datos y aplicaciones, menor redundancia, integridad y consistencia, acceso concurrente controlado y seguridad centralizada.
- **Usuarios**: el **administrador de la base de datos (DBA)**, responsable de esquemas, seguridad y rendimiento; los diseñadores; los desarrolladores de aplicaciones; y los usuarios finales.
- **SGBD relacionales del mercado**: **Oracle Database**, **Microsoft SQL Server** e **IBM Db2** (propietarios); **PostgreSQL**, **MySQL**, **MariaDB** y **SQLite** (libres).

### La arquitectura ANSI/SPARC

El comité **ANSI/SPARC** propuso en **1975** una arquitectura de **tres niveles** que, con variantes, siguen los SGBD actuales. Su objetivo es separar las aplicaciones de usuario de la organización física de los datos.

| Nivel | Esquema | Contenido |
| --- | --- | --- |
| **Externo** | Vistas de usuario | La parte de la base de datos que ve cada usuario o aplicación |
| **Conceptual** | Esquema conceptual | Estructura lógica global: entidades, relaciones y restricciones |
| **Interno** | Esquema interno | Organización física: ficheros, índices y rutas de acceso |

De esta separación derivan las dos independencias de datos:

- **Independencia lógica**: modificar el esquema conceptual sin afectar a los esquemas externos ni a las aplicaciones.
- **Independencia física**: modificar el esquema interno (índices, almacenamiento) sin afectar al esquema conceptual.

### Transacciones y propiedades ACID

Una **transacción** es una unidad de trabajo que agrupa varias operaciones y se ejecuta por completo o no se ejecuta en absoluto. Los SGBD relacionales garantizan las propiedades **ACID**:

- **Atomicidad**: la transacción se confirma entera o se deshace entera (*rollback*).
- **Consistencia**: lleva la base de datos de un estado válido a otro estado válido.
- **Aislamiento** (*isolation*): las transacciones concurrentes no interfieren entre sí.
- **Durabilidad**: los cambios confirmados (*commit*) persisten aunque falle el sistema.

## El modelo relacional: diseño conceptual, lógico y físico

El **modelo relacional**, propuesto por **Edgar F. Codd en 1970**, se basa en la lógica de predicados y la teoría de conjuntos: los datos se representan como relaciones (tablas) y se manipulan con lenguajes formales, el **álgebra relacional** y el **cálculo relacional**, de los que SQL es la materialización práctica.

- **Relación**: término matemático para «tabla».
- **Tupla**: cada fila de la relación.
- **Atributo**: cada columna, asociada a un **dominio** (conjunto de valores permitidos).
- **Grado**: número de atributos (columnas) de la relación.
- **Cardinalidad**: número de tuplas (filas) de la relación.
- **Claves**:
    - **Superclave**: conjunto de atributos que identifica unívocamente cada tupla.
    - **Clave candidata**: superclave mínima (sin atributos superfluos).
    - **Clave primaria**: la candidata elegida como identificador; las restantes son **claves alternativas**.
    - **Clave ajena (foránea)**: atributos que referencian la clave primaria de otra relación.
- **Reglas de integridad**:
    - **Integridad de entidad**: ningún atributo de la clave primaria puede ser nulo.
    - **Integridad referencial**: toda clave ajena contiene valores existentes en la relación referenciada, o nulos.
    - **Integridad de dominio**: cada valor pertenece al dominio de su atributo.

### Las 12 reglas de Codd

**Codd estableció 13 reglas** (12 más la regla fundamental) que definen los requisitos para que un SGBD sea considerado verdaderamente relacional:

- **Regla 0. Fundamental**: el SGBD debe gestionar sus bases de datos usando exclusivamente el modelo relacional.
- **Regla 1. Información**: todos los datos se representan como valores en tablas.
- **Regla 2. Acceso garantizado**: todo dato es accesible sabiendo el nombre de la tabla, el valor de la clave primaria y el nombre del atributo.
- **Regla 3. Tratamiento sistemático de valores nulos**: los nulos (dato desconocido o inaplicable) se manejan de forma uniforme.
- **Regla 4. Catálogo dinámico en línea**: los metadatos se almacenan como tablas relacionales y se consultan con el mismo lenguaje.
- **Regla 5. Sublenguaje de datos completo**: debe existir un lenguaje bien definido (como SQL) para definir, manipular y controlar los datos.
- **Regla 6. Actualización de vistas**: toda vista teóricamente actualizable debe ser actualizable por el sistema.
- **Regla 7. Operaciones de alto nivel**: inserción, actualización y borrado deben poder operar sobre conjuntos de filas.
- **Regla 8. Independencia física**: los cambios en el almacenamiento físico no afectan a las aplicaciones.
- **Regla 9. Independencia lógica**: los cambios en las tablas que preserven la información no afectan a las aplicaciones.
- **Regla 10. Independencia de integridad**: las reglas de integridad se definen en el catálogo y las aplica el SGBD, no las aplicaciones.
- **Regla 11. Independencia de distribución**: el usuario no percibe si los datos están distribuidos en varias ubicaciones.
- **Regla 12. No subversión**: no debe ser posible saltarse las reglas del SGBD usando lenguajes de bajo nivel.

### Las fases del diseño

El diseño de una base de datos se divide en **tres fases** sucesivas:

1. **Diseño conceptual**: obtiene el **esquema entidad-relación** a partir de los requisitos, con independencia del SGBD y del modelo de implementación.
2. **Diseño lógico**: traduce el esquema conceptual al modelo de datos elegido (habitualmente el relacional), obteniendo un **esquema relacional normalizado**.
3. **Diseño físico (implementación)**: convierte el esquema lógico en una implementación concreta del SGBD seleccionado (código **DDL**, índices, almacenamiento). Sus objetivos: optimizar los tiempos de respuesta, minimizar el espacio en disco y el consumo de recursos, y conseguir la máxima seguridad.

### El modelo entidad-relación (E/R)

Es el **modelo conceptual** más utilizado. No existe una representación gráfica única, pero los conceptos son estándar:

- **Entidades**: objetos o conceptos del mundo real (sustantivos).
    - **Fuerte**: su existencia no depende de otra entidad.
    - **Débil**: su existencia depende de una entidad fuerte.
- **Atributos**: propiedades de las entidades (adjetivos).
    - **Simples** (indivisibles: color) o **compuestos** (descomponibles: dirección en calle, número, puerta).
    - **Monovaluados** (un solo valor: DNI) o **multivaluados** (varios valores: teléfonos).
    - **Almacenados** (se guardan) o **derivados** (se calculan: edad a partir de la fecha de nacimiento).
    - **Identificador (clave)**: identifica unívocamente cada ocurrencia de la entidad.
- **Relaciones (interrelaciones)**: asociaciones entre entidades (verbos).
    - **Grado**: número de entidades participantes. **Binaria** (grado 2; **reflexiva** si la entidad se relaciona consigo misma), **ternaria** y **n-aria**.
- **Restricciones**:
    - **De cardinalidad**: número de ocurrencias que participan en la relación (**1:1**, **1:N**, **N:M**).
    - **De participación**: **total** (dependencia de existencia: todo empleado pertenece a un departamento) o **parcial** (un cliente puede no tener hipoteca).

### El modelo E/R extendido

Añade conceptos para situaciones de modelado más complejas:

- **Especialización y generalización**: jerarquías de **superclases y subclases** (herencia). Se clasifican según dos criterios independientes:
    - **Disjunta (D)**: una ocurrencia no puede pertenecer a más de una subclase; **solapada (S)**: puede pertenecer a varias.
    - **Total (T)**: toda ocurrencia de la superclase pertenece a alguna subclase; **parcial (P)**: puede no pertenecer a ninguna.
- **Agregación**: permite tratar una relación entre entidades como si fuera una entidad, para relacionarla con otras.

![Generalización total y disjunta (T,D): todo empleado público es funcionario de carrera, funcionario interino o personal laboral, y solo una de las tres cosas](media/image49.png){width=70%}

### Del modelo E/R al relacional

Reglas básicas de transformación del esquema conceptual al lógico:

- **Entidad fuerte**: tabla con su clave primaria.
- **Entidad débil**: tabla cuya clave primaria incluye la de la entidad fuerte de la que depende.
- **Relación 1:1**: clave ajena en cualquiera de las dos tablas (o fusión de ambas).
- **Relación 1:N**: clave ajena en la tabla del lado N.
- **Relación N:M**: tabla intermedia con las claves primarias de ambas entidades.
- **Atributo multivaluado**: tabla propia con clave ajena a la entidad.

### Normalización y formas normales

La **normalización** aplica reglas sucesivas para minimizar la redundancia y evitar **anomalías** de inserción, actualización y borrado. La **desnormalización** introduce redundancia controlada para mejorar el rendimiento de consulta. Se apoya en las dependencias entre atributos:

- **Dependencia funcional (X → Y)**: cada valor de X tiene asociado un único valor de Y. Ejemplo: DNI → Nombre.
- **Dependencia funcional completa**: Y depende de toda la clave compuesta y no de una parte de ella. Ejemplo: con clave (CursoID, Semestre), las plazas ofertadas dependen del par completo; el nombre del curso depende solo de CursoID (dependencia parcial).
- **Dependencia transitiva**: si X → Y e Y → Z, entonces X → Z. Ejemplo: fecha de nacimiento → edad → capacidad para conducir.

Las **formas normales** son estándares acumulativos (cada una exige las anteriores):

- **Primera forma normal (1FN)**: todos los atributos son **atómicos** (un solo valor por celda, sin grupos repetitivos) y la tabla tiene clave primaria sin valores nulos. Incumple la 1FN:

| CursoID | Semestre | Plazas | Notas |
| --- | --- | --- | --- |
| IT101 | 2009-1 | 100 | 7, 8, 9, 10 |
| IT102 | 2009-1 | 200 | 5, 6, 8 |

El atributo Notas guarda varios valores en una celda: se resuelve con una tabla de notas aparte.

- **Segunda forma normal (2FN)**: 1FN y todo atributo no clave depende **de la clave completa** (sin dependencias parciales; solo puede incumplirse con claves compuestas). Incumple la 2FN:

| CursoID | Semestre | Plazas | NombreCurso |
| --- | --- | --- | --- |
| IT101 | 2009-1 | 100 | Programación |
| IT101 | 2009-2 | 100 | Programación |
| IT102 | 2009-1 | 200 | Bases de datos |

Con clave (CursoID, Semestre), NombreCurso depende solo de CursoID: se separa en una tabla de cursos.

- **Tercera forma normal (3FN)**: 2FN y sin dependencias **transitivas** de atributos no clave respecto a la clave primaria. Incumple la 3FN:

| CursoID | Semestre | Plazas | ProfesorID | NombreProfesor |
| --- | --- | --- | --- | --- |
| IT101 | 2009-1 | 100 | 332 | Jones |
| IT102 | 2009-1 | 200 | 495 | Bentley |
| IT102 | 2010-1 | 150 | 332 | Jones |

NombreProfesor depende de ProfesorID (que no es clave): se separa en una tabla de profesores.

- **Forma normal de Boyce-Codd (FNBC)**: en toda dependencia funcional no trivial, el determinante es una **clave candidata**.
- **Cuarta forma normal (4FN)**: FNBC y sin dependencias **multivaluadas** no triviales.
- **Quinta forma normal (5FN)**: 4FN y sin dependencias de **reunión (join)** no triviales que no se deriven de las claves candidatas.

En la práctica, un esquema en **3FN o FNBC** se considera suficientemente normalizado; la 4FN y la 5FN eliminan redundancias complejas en relaciones muchos a muchos.

## El lenguaje SQL

**SQL** (*Structured Query Language*) es el lenguaje **declarativo** estándar para definir, manipular y controlar bases de datos relacionales: se indica qué se quiere obtener, no cómo. Está normalizado como **ISO/IEC 9075**; se estandarizó por primera vez en **1986** (ANSI) y **1987** (ISO), y la edición vigente es **SQL:2023**, que incorpora consultas sobre grafos de propiedades (SQL/PGQ) y mejora el soporte de **JSON**.

| Sublenguaje | Función | Sentencias |
| --- | --- | --- |
| **DDL** (definición) | Estructura de los objetos | CREATE, ALTER, DROP, TRUNCATE |
| **DML** (manipulación) | Datos | SELECT, INSERT, UPDATE, DELETE |
| **DCL** (control) | Permisos | GRANT, REVOKE |
| **TCL** (transacciones) | Transacciones | COMMIT, ROLLBACK, SAVEPOINT |

Algunas clasificaciones separan SELECT en un sublenguaje propio de consulta (DQL).

- **Estructura de la consulta**: `SELECT ... FROM ... [WHERE] [GROUP BY] [HAVING] [ORDER BY]`. **WHERE** filtra filas antes de agrupar; **HAVING** filtra grupos después de agrupar.
- **Funciones de agregación**: COUNT, SUM, AVG, MIN, MAX.

```sql
SELECT genero, COUNT(*) AS total
FROM libro
WHERE anio_publicacion >= 2000
GROUP BY genero
HAVING COUNT(*) > 5
ORDER BY total DESC;
```

- **Composición de tablas (JOIN)**:
    - **INNER JOIN**: solo las filas con correspondencia en ambas tablas.
    - **LEFT / RIGHT OUTER JOIN**: todas las filas de la tabla izquierda/derecha, con nulos donde no hay correspondencia.
    - **FULL OUTER JOIN**: todas las filas de ambas tablas.
    - **CROSS JOIN**: producto cartesiano.

```sql
SELECT s.nombre, COUNT(p.id_prestamo) AS prestamos
FROM socio s
LEFT JOIN prestamo p ON p.numero_socio = s.numero_socio
GROUP BY s.nombre;
```

- **Otros objetos**:
    - **Vistas** (CREATE VIEW): consultas almacenadas que se usan como tablas virtuales; simplifican el acceso y aplican seguridad por columnas o filas.
    - **Índices** (CREATE INDEX): estructuras (habitualmente árboles B) que aceleran las búsquedas a costa de más espacio y escrituras más lentas.
    - **Procedimientos almacenados** y **disparadores (triggers)**: lógica ejecutada en el servidor; el trigger se dispara automáticamente ante INSERT, UPDATE o DELETE.
- **Transacciones**: `BEGIN / START TRANSACTION ... COMMIT` (confirma) o `ROLLBACK` (deshace). El estándar define **cuatro niveles de aislamiento** (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE) que gradúan el equilibrio entre concurrencia y consistencia.

## Bases de datos NoSQL y no estructuradas

Según su estructura, los datos se clasifican en:

- **Estructurados**: se ajustan a un esquema fijo (tablas relacionales).
- **Semiestructurados**: estructura flexible y autodescriptiva (**JSON**, **XML**).
- **No estructurados**: sin esquema definido (documentos ofimáticos, correos, imágenes, audio, vídeo). Constituyen la gran mayoría de los datos de una organización.

Las bases de datos **NoSQL** (*not only SQL*) surgen con la web a gran escala para cubrir necesidades que el modelo relacional resuelve mal: volúmenes masivos, **escalado horizontal** (añadir nodos en lugar de crecer verticalmente), esquemas flexibles o cambiantes y alta disponibilidad global.

- **Características**: esquema flexible (*schema-less*), replicación y particionado (**sharding**) nativos, API sencillas; renuncian en general al JOIN y a las transacciones ACID completas.
- **Teorema CAP** (Brewer, 2000): un sistema distribuido no puede garantizar a la vez **consistencia** (todas las réplicas ven el mismo dato), **disponibilidad** (toda petición recibe respuesta) y **tolerancia a particiones** (funciona aunque se pierda la comunicación entre nodos). Ante una partición hay que elegir: sistemas **CP** (sacrifican disponibilidad) o **AP** (sacrifican consistencia).
- **Modelo BASE** (frente a ACID): *Basically Available, Soft state, Eventual consistency*. El sistema prioriza estar disponible y las réplicas convergen con el tiempo (**consistencia eventual**).

Los cuatro tipos principales de bases NoSQL:

| Tipo | Modelo de datos | Usos típicos | Ejemplos |
| --- | --- | --- | --- |
| **Clave-valor** | Pares clave-valor opaco | Caché, sesiones, colas | **Redis**, Amazon DynamoDB |
| **Documental** | Documentos JSON/BSON | Catálogos, contenido, APIs web | **MongoDB**, CouchDB |
| **Columnar** | Familias de columnas | Series temporales, escrituras masivas | **Apache Cassandra**, HBase |
| **Grafos** | Nodos y aristas con propiedades | Redes sociales, fraude, recomendación | **Neo4j**, JanusGraph |

Otras familias relacionadas:

- **NewSQL**: combinan la escalabilidad horizontal NoSQL con SQL y transacciones ACID (Google **Spanner**, **CockroachDB**).
- **Bases de datos vectoriales**: almacenan *embeddings* (vectores) y buscan por similitud; se han popularizado con la IA generativa como soporte de la generación aumentada por recuperación (RAG). Ejemplos: Milvus, Qdrant o la extensión **pgvector** de PostgreSQL.
- **Motores de búsqueda**: indexación y consulta de texto completo (**Elasticsearch**, Apache Solr).

## Supuesto práctico: diseño de una base de datos

### Planteamiento

Una biblioteca pública desea implantar un sistema de gestión de sus operaciones diarias:

- **Gestión de libros**: título, autores, género, año de publicación e ISBN.
- **Control de ejemplares**: varias copias de un mismo libro, con código único de ejemplar.
- **Registro de socios**: nombre, dirección, teléfono y número de socio.
- **Gestión de préstamos**: préstamo y devolución de ejemplares, con fechas.
- **Reservas**: los socios pueden reservar libros no disponibles.

### Diseño conceptual

Del análisis de requisitos se identifican las entidades LIBRO, AUTOR, EJEMPLAR, SOCIO, PRÉSTAMO y RESERVA, y sus relaciones: un libro puede tener varios autores y un autor varios libros (N:M); un libro tiene varios ejemplares (1:N); un socio realiza varios préstamos y reservas (1:N).

![Diagrama entidad-relación del sistema de gestión de la biblioteca](media/image51.png){width=85%}

### Diseño lógico

El esquema E/R se transforma en un esquema relacional normalizado (notación: CP = clave primaria, CAj = clave ajena). La relación N:M entre LIBRO y AUTOR genera la tabla intermedia LIBRO_AUTOR; las relaciones 1:N se resuelven con claves ajenas en el lado N.

```text
AUTOR (ID_Autor, Nombre, Apellidos)
    CP: ID_Autor
LIBRO (ISBN, Título, Año_Publicación, Género)
    CP: ISBN
LIBRO_AUTOR (ISBN, ID_Autor)
    CP: (ISBN, ID_Autor)
    CAj: ISBN → LIBRO; ID_Autor → AUTOR
EJEMPLAR (Código_Ejemplar, ISBN, Localización)
    CP: Código_Ejemplar
    CAj: ISBN → LIBRO
SOCIO (Número_Socio, Nombre, Dirección, Teléfono)
    CP: Número_Socio
PRÉSTAMO (ID_Préstamo, Código_Ejemplar, Número_Socio, Fecha_Préstamo, Fecha_Devolución)
    CP: ID_Préstamo
    CAj: Código_Ejemplar → EJEMPLAR; Número_Socio → SOCIO
RESERVA (ID_Reserva, ISBN, Número_Socio, Fecha_Reserva)
    CP: ID_Reserva
    CAj: ISBN → LIBRO; Número_Socio → SOCIO
```

### Diseño físico

El esquema lógico se implementa en el SGBD elegido (aquí MySQL) con código DDL, decidiendo tipos de datos, índices y restricciones:

```sql
CREATE TABLE Autor (
    ID_Autor INT NOT NULL PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellidos VARCHAR(50)
);

CREATE TABLE Libro (
    ISBN VARCHAR(13) NOT NULL PRIMARY KEY,
    Titulo VARCHAR(100),
    Anio_Publicacion YEAR,
    Genero VARCHAR(30)
);

CREATE TABLE Libro_Autor (
    ISBN VARCHAR(13) NOT NULL,
    ID_Autor INT NOT NULL,
    PRIMARY KEY (ISBN, ID_Autor),
    FOREIGN KEY (ISBN) REFERENCES Libro(ISBN),
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);

CREATE TABLE Ejemplar (
    Codigo_Ejemplar INT NOT NULL PRIMARY KEY,
    ISBN VARCHAR(13) NOT NULL,
    Localizacion VARCHAR(30),
    FOREIGN KEY (ISBN) REFERENCES Libro(ISBN)
);

CREATE TABLE Socio (
    Numero_Socio INT NOT NULL PRIMARY KEY,
    Nombre VARCHAR(50),
    Direccion VARCHAR(100),
    Telefono VARCHAR(15)
);

CREATE TABLE Prestamo (
    ID_Prestamo INT NOT NULL PRIMARY KEY,
    Codigo_Ejemplar INT NOT NULL,
    Numero_Socio INT NOT NULL,
    Fecha_Prestamo DATE,
    Fecha_Devolucion DATE,
    FOREIGN KEY (Codigo_Ejemplar) REFERENCES Ejemplar(Codigo_Ejemplar),
    FOREIGN KEY (Numero_Socio) REFERENCES Socio(Numero_Socio)
);

CREATE TABLE Reserva (
    ID_Reserva INT NOT NULL PRIMARY KEY,
    ISBN VARCHAR(13) NOT NULL,
    Numero_Socio INT NOT NULL,
    Fecha_Reserva DATE,
    FOREIGN KEY (ISBN) REFERENCES Libro(ISBN),
    FOREIGN KEY (Numero_Socio) REFERENCES Socio(Numero_Socio)
);
```

### Optimización

- **Índices** sobre las claves ajenas y los campos de búsqueda frecuente, por ejemplo: `CREATE INDEX idx_prestamo_socio ON Prestamo (Numero_Socio);`.
- **Restricciones adicionales**: NOT NULL en los campos obligatorios, UNIQUE donde proceda y CHECK (por ejemplo, `Fecha_Devolucion >= Fecha_Prestamo`).
- **Desnormalización selectiva** si el rendimiento lo exige (por ejemplo, un contador de ejemplares disponibles en LIBRO), asumiendo el coste de mantener la redundancia.

## Fuentes {.unnumbered .unlisted}

- E. F. Codd, «A Relational Model of Data for Large Shared Data Banks», *Communications of the ACM*, vol. 13, n.º 6, junio de 1970.
- E. F. Codd, «Is Your DBMS Really Relational?» y «Does Your DBMS Run By the Rules?», *ComputerWorld*, octubre de 1985 (las 12 reglas).
- ANSI/X3/SPARC Study Group on Data Base Management Systems, informe provisional de 1975 (arquitectura de tres niveles).
- ISO/IEC 9075:2023, *Information technology. Database languages SQL* (SQL:2023, junio de 2023).
- R. Elmasri y S. B. Navathe, *Fundamentals of Database Systems*, 7.ª ed., Pearson, 2016.
- E. Brewer, «Towards Robust Distributed Systems», PODC, 2000 (teorema CAP).
