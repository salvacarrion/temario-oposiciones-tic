# Gestión de datos corporativos y Big Data

## Gestión de Datos Corporativos

La gestión de datos corporativos es fundamental en cualquier organización. Los sistemas de información están compuestos por **hardware** (subsistema físico), **software** (subsistema lógico), **datos**, **métodos o procedimientos**, y **personas**.

Estos elementos apoyan tres **niveles de decisión** organizacional:

- **Alta dirección**: Enfocada en decisiones estratégicas.
- **Dirección táctica**: Implementa y supervisa las estrategias.
- **Nivel operativo**: Alinea las operaciones diarias con los objetivos tácticos.

### Fuentes de Información

Las organizaciones utilizan diversas fuentes de información para la toma de decisiones:

- **Bases de datos corporativas**: Pueden ser relacionales, espaciales, temporales, documentales o multimedia.
- **Webs y redes sociales**: Análisis de opiniones y preferencias de usuarios.
- **Fuentes OSINT** (Open Source Intelligence): Datos de fuentes abiertas.
- **Internet de las Cosas (IoT)**: Dispositivos autónomos que recopilan y transmiten datos a través de internet.

### Almacén de Datos (Data Warehouse)

Un **data warehouse** es una colección integrada y no volátil de datos orientada a un ámbito específico. Su estructura facilita la toma de decisiones a través del almacenamiento de **datamarts**, los cuales modelan hechos, atributos y dimensiones.

- **Modelo Multidimensional (Hipercubo)**:
    - **Hechos**: Datos o conceptos de interés (ej.: ventas, personal).
    - **Atributos**: Aspectos medibles de los hechos (ej.: importe, cantidad).
    - **Dimensiones**: Detalles vinculados a los hechos (ej.: tiempo, lugar).
- **Tipos de Modelos**:
    - **Estrella**: Un hecho central rodeado por dimensiones.
    - **Estrella Simple**: Permite un único camino de agregación.
    - ![](media/image59.png)**Copo de Nieve**: Permite múltiples caminos de agregación.

### Datamart

Un **datamart** es un almacén de datos específico, centrado en un área de negocio. **Estructurado** en forma de estrella, facilita la consulta y el análisis de datos para un departamento específico.

**Características**:

- Usuarios limitados.
- Enfoque en un área específica.
- Función de apoyo.

### Data Lake

Un **data lake** es un almacén **no estructurado** de **información en bruto**, accesible y centralizado. Puede contener datos estructurados, semiestructurados (JSON, CSV), no estructurados (emails, tweets) y binarios (fotos, videos). Herramientas como **Apache Hadoop** son esenciales para la gestión de data lakes.

### Arquitecturas OLTP y OLAP

- **OLTP (On-Line Transaction Processing)**: Procesamiento transaccional en tiempo real, optimizado para **transacciones** con bases de datos relacionales, con datos detallados y normalizados.
- **OLAP (On-Line Analytical Processing)**: Procesamiento analítico orientado a consultas complejas para apoyar la toma de decisiones mediante cubos OLAP.

**Operadores OLAP**:

- **Drill**: Desglosa datos por dimensiones.
- **Roll**: Agrega datos por dimensiones.
- **Slice & Dice**: Selecciona y proyecta datos en nuevas vistas.
- **Pivot**: Reorienta dimensiones para recalcular celdas.

**Implementaciones OLAP**:

- **ROLAP (Relational OLAP)**: Construido sobre bases de datos relacionales.
- **MOLAP (Multidimensional OLAP)**: Basado en estructuras multidimensionales.
- **HOLAP (Hybrid OLAP)**: Combina ROLAP y MOLAP.

### Esquemas ROLAP

- **Estrella**: Contiene una tabla de hechos central rodeada de tablas de dimensiones, diseñada para simplicidad y eficiencia.
- **Copo de Nieve**: Implementa dimensiones con múltiples tablas, optimizando espacio pero reduciendo rendimiento.

### Elementos de un Almacén de Datos

- **Metadatos**: Documentan tablas, columnas y tipos de datos.
- **Middleware**: Permite la interoperabilidad en plataformas heterogéneas.
- **ETL (Extraction, Transformation & Load)**:
    - **Extracción**: Obtención de datos en bruto.
    - **Transformación**: Limpieza y estructuración de datos.
    - **Carga**: Creación y llenado de datamarts con información depurada.

### Herramientas de Explotación de Datos

- **Sistemas de Información Ejecutiva (EIS)**: Monitoreo de variables clave.
- **Dashboard o Cuadro de Mando Integral (CMI)**: Reportes y análisis interactivos.
- **Minería de Datos**: Descubrimiento de patrones en grandes volúmenes de datos.

## Big Data

Big Data es un término que describe conjuntos de datos demasiado grandes y complejos para ser procesados por métodos tradicionales. Su gestión se centra en las **5 V's**:

- **Volumen**: Cantidades masivas de datos.
- **Velocidad**: Procesamiento y análisis en tiempo real.
- **Variedad**: Diversidad de formatos y fuentes.
- **Veracidad**: Fiabilidad de los datos.
- **Valor**: Conocimiento obtenido de los datos.

### Infraestructura de Almacenamiento

**Bases de Datos NoSQL**:

- No requieren estructuras fijas.
- No soportan operaciones JOIN.
- No garantizan completamente ACID.
- Escalan horizontalmente.

**Tipos de NoSQL**:

- **Orientadas a Documentos**: Almacenan datos en JSON o XML (ejemplo: MongoDB).
- **Almacenes Clave/Valor**: Pares clave-valor (ejemplo: Redis).
- **Organizadas por Columnas**: Datos en columnas (ejemplo: Cassandra).
- **Basadas en Grafos**: Estructuradas en nodos y relaciones (ejemplo: Neo4j).

### Infraestructura de Procesamiento

Dependiendo de la necesidad de procesamiento:

- **Procesamiento Batch**: Ideal para grandes volúmenes de datos con herramientas como HDFS y MapReduce.
- **Procesamiento Streaming**: Para flujos continuos de datos en tiempo real, usando Apache Kafka y Storm.
- **Procesamiento Híbrido**: Combina batch y streaming, con arquitecturas como Lambda y Kappa.

### Ecosistema Apache Hadoop

Hadoop es un marco de trabajo de código abierto para aplicaciones distribuidas que gestionan grandes volúmenes de datos.

**Componentes Principales**:

- **HDFS**: Sistema de archivos distribuido.
- **MapReduce**: Modelo de programación para computación paralela.
- **YARN**: Gestor de recursos.
- **Spark**: Procesamiento de datos en memoria.
- **Pig y Hive**: Procesamiento basado en consultas.
- **HBase**: Base de datos NoSQL.
- **Mahout y Spark MLlib**: Algoritmos de machine learning.
- **Zookeeper**: Gestión de clústeres.
- **Oozie**: Planificación de trabajos.

## Minería de Datos

La **Minería de Datos** es el proceso de extraer conocimiento útil, comprensible y previamente desconocido a partir de grandes volúmenes de datos almacenados en diversos formatos. Este conocimiento permite identificar patrones, tendencias y relaciones ocultas que pueden ser cruciales para la toma de decisiones estratégicas en una organización.

### Modelo CRISP-DM

El **CRISP-DM** (CRoss Industry Standard Process for Data Mining): Es el modelo estándar más utilizado para estructurar proyectos de minería de datos. Este modelo abierto y flexible consta de seis fases interrelacionadas:

- **Fase 1 - Comprensión del negocio**: Se profundiza en los objetivos y requisitos desde una perspectiva empresarial, identificando problemas y oportunidades donde la minería de datos puede aportar valor.
- **Fase 2 - Comprensión de los datos**: Se exploran y analizan los datos disponibles para evaluar su calidad, relevancia y adecuación a los objetivos planteados, afinando así los objetivos iniciales.
- **Fase 3 - Preparación de los datos**: Implica la recopilación, limpieza, integración y transformación de los datos para construir el conjunto de datos final que se utilizará en la fase de modelado.
- **Fase 4 - Modelado**: Se seleccionan y aplican algoritmos y técnicas de modelado adecuados, ajustando sus parámetros para optimizar el rendimiento de los modelos.
- **Fase 5 - Evaluación**: Se evalúan los modelos construidos no solo desde una perspectiva técnica (precisión, error, etc.), sino también en términos de su aportación al negocio y cumplimiento de los objetivos iniciales.
- **Fase 6 - Distribución**: El conocimiento obtenido se presenta y distribuye en la organización, integrándolo en los procesos de toma de decisiones y asegurando su adopción efectiva.

### Tareas y Tipología de Problemas

- **Predictivas**: Buscan predecir valores o categorías futuras basándose en datos históricos etiquetados. Incluyen:
    - **Clasificación (multiclase / multi-class)**: Asignar una etiqueta de clase a instancias basándose en características predictoras.
    - **Categorización (multietiqueta / multi-label)**: Asignar múltiples etiquetas a cada instancia.
    - **Priorización (ordenación)**: Ordenar instancias según una métrica o criterio específico.
    - **Regresión**: Predecir valores numéricos continuos.
- **Descriptivas**: Pretenden descubrir patrones y relaciones en datos no etiquetados, proporcionando una comprensión más profunda del conjunto de datos. Incluyen:
    - **Agrupamiento (clustering)**: Agrupar instancias similares sin predefinir categorías.
    - **Correlación**: Identificar relaciones significativas entre variables.
    - **Reglas de asociación**: Descubrir relaciones frecuentes entre variables en grandes bases de datos.
    - **Detección de anomalías**: Identificar instancias que se desvían significativamente del comportamiento normal.

### Modelos de Representación y Preparación de Datos

- **Extracción de características**: Cada objeto o instancia se representa como un vector de características (atributos) que capturan información relevante para el análisis.
- **Técnicas de preparación**:
    - **Discretización**: Convertir atributos numéricos continuos en categorías discretas (por ejemplo, mediante binning).
    - **Numerización**: Transformar atributos categóricos nominales en representaciones numéricas (como codificación one-hot).
    - **Gestión de valores faltantes**: Imputación de datos o eliminación de instancias incompletas para manejar la ausencia de valores.
    - **Reducción de dimensionalidad**: Simplificar el conjunto de datos reduciendo el número de variables, manteniendo la mayor cantidad posible de información relevante. Técnicas como Análisis de Componentes Principales (PCA), autoencoders o selección basada en ganancia de información.

### Técnicas de Modelado

- **Aprendizaje Perezoso (Lazy Learning)**: Los algoritmos retrasan la generalización hasta el momento de la predicción. No construyen un modelo explícito durante el entrenamiento. Ejemplo:
    - **K-NN (K-Nearest Neighbors)**: Clasifica una instancia basándose en las clases de sus vecinos más cercanos en el espacio de características.
- **Aprendizaje Anticipativo (Eager Learning)**: Los algoritmos construyen un modelo generalizado durante el entrenamiento, que se utiliza para realizar predicciones futuras. Incluye:
    - **Métodos bayesianos**: Utilizan probabilidades para predecir la clase más probable.
    - **Árboles de decisión**: Modelos en forma de árbol que representan decisiones y sus posibles consecuencias.
    - **Redes neuronales**: Modelos inspirados en la estructura del cerebro humano, capaces de capturar relaciones complejas.
    - **Máquinas de vectores de soporte (SVM)**: Algoritmos que buscan el hiperplano que mejor separa las clases en el espacio de características.
    - **Algoritmos evolutivos**: Utilizan principios de evolución biológica para optimizar soluciones.
- **Ensembles o Meta-Clasificadores**: Combinan múltiples modelos para mejorar la precisión y robustez de las predicciones. Estrategias comunes:
    - **Bagging**: Entrenar múltiples modelos en subconjuntos aleatorios del conjunto de datos y promediar sus predicciones.
    - **Boosting**: Construir secuencialmente modelos donde cada uno corrige los errores del anterior.
    - **Stacking**: Combinar las predicciones de varios modelos utilizando un modelo de nivel superior que aprende cómo combinar mejor estas predicciones.

### Evaluación de Modelos

- **Modos de evaluación**:
    - **Split (División simple)**: Separar los datos en conjuntos de entrenamiento y prueba (por ejemplo, 70% y 30%).
    - **Validación Cruzada (k-fold)**: Dividir los datos en k subconjuntos; entrenar y probar el modelo k veces, cada vez con un subconjunto diferente como prueba.
    - **Leave-One-Out (LOOCV)**: Caso especial de validación cruzada donde k es igual al número de instancias; cada instancia se usa una vez como prueba.
    - **Bootstrap**: Muestreo con reemplazo para crear múltiples conjuntos de entrenamiento y evaluar la variabilidad del modelo.
- **Matriz de confusión**: Es una tabla que resume el rendimiento del modelo en términos de verdaderos positivos (TP), verdaderos negativos (TN), falsos positivos (FP) y falsos negativos (FN).

|                   | **Predicción Positiva** | **Predicción Negativa** |
| ----------------- | :---------------------: | :---------------------: |
| **Real Positiva** | Verdadero Positivo (TP) |   Falso Negativo (FN)   |
| **Real Negativa** |   Falso Positivo (FP)   | Verdadero Negativo (TN) |

- **Medidas clave: (Principales)**
    - **Accuracy (Precisión general):** Proporción de predicciones correctas en relación con el total de predicciones.
        - **Fórmula:** (TP + TN) / (TP + TN + FP + FN)
    - **Precision (Precisión o Valor Predictivo Positivo [PV+]):** Indica la proporción de predicciones positivas que son correctas.
        - **Fórmula:** TP / (TP + FP)
    - **Recall (Exhaustividad, Sensibilidad o True Positive Rate [TPR]):** Mide la capacidad del modelo para identificar correctamente los casos positivos.
        - **Fórmula**: TP / (TP + FN)
    - **F-Score (F1):** Media armónica de la precisión y la exhaustividad, equilibrando estas dos métricas.
        - **Fórmula:** 2 * (Precision * Recall) / (Precision + Recall)
- **Medidas clave: (Principales 2)**
    - **True Positive Rate (TPR) o Sensibilidad:** Proporción de casos positivos correctamente identificados por el modelo, también conocida como Recall.
        - **Fórmula:** TP / (TP + FN)
    - **False Positive Rate (FPR) o Tasa de Falsos Positivos:** Proporción de casos negativos que el modelo clasifica incorrectamente como positivos.
        - **Fórmula:** FP / (FP + TN)
    - **False Negative Rate (FNR) o Tasa de Falsos Negativos:** Proporción de casos positivos que el modelo no detecta (clasifica como negativos).
        - **Fórmula:** FN / (TP + FN)
    - **True Negative Rate (TNR) o Especificidad:** Proporción de casos negativos que el modelo clasifica correctamente como negativos.
        - **Fórmula:** TN / (TN + FP)
- **Otras métricas:** Hay más métricas de estas pero con el mareo de nombres que hay, suficiente. (Nota: Ojo con las traducciones!)
    - **Ver tabla:** <https://es.wikipedia.org/wiki/Curva_ROC>
- **Curva ROC (Receiver Operating Characteristic):** Muestra el rendimiento de un clasificador binario comparando la Tasa de Verdaderos Positivos (Recall) y la Tasa de Falsos Positivos para distintos umbrales.
    - Permite visualizar cómo el modelo equilibra estos dos aspectos al variar el umbral de decisión.
    - Una curva que se acerca al vértice superior izquierdo indica un mejor rendimiento.
- **Área Bajo la Curva (AUC - Area Under the Curve):** Métrica que cuantifica el rendimiento general del modelo en la Curva ROC.
    - Un AUC de 1 representa un modelo perfecto, mientras que un AUC de 0.5 indica un modelo sin capacidad de clasificación (aleatorio).
    - Cuanto mayor sea el AUC, mejor será la capacidad del modelo para separar las clases correctamente.
- **Evaluación de modelos de regresión**: Se utilizan métricas como:
    - **MSE (Mean Squared Error)**: Promedio de los cuadrados de los errores.
    - **RMSE (Root Mean Squared Error)**: Raíz cuadrada del MSE, proporciona una medida en las mismas unidades que la variable objetivo.
    - **MAE (Mean Absolute Error)**: Promedio de los valores absolutos de los errores.
    - **RSE (Residual Standard Error)**: Medida de la calidad de un modelo de regresión.
    - **Coeficiente de correlación de Pearson (r)**: Indica la fuerza y dirección de la relación lineal entre dos variables.
- **Evaluación de modelos de agrupamiento**: Se pueden utilizar medidas como:
    - **Verosimilitud (Likelihood)**: Evalúa qué tan probable es que los datos se generen a partir del modelo propuesto.
    - **Índice de Silueta (Silhouette)**: Mide qué tan similar es una instancia a su propio cluster en comparación con otros clusters.
    - **Coeficiente de Dunn**: Evalúa la compacidad y separación de los clusters.
- **Evaluación de modelos de reglas de asociación**:
    - **Soporte (Cobertura)**: Proporción de instancias donde la regla es aplicable.
    - **Confianza**: Probabilidad de que la consecuencia de la regla sea cierta cuando la antecedente es cierta.
    - **Lift**: Medida de la importancia de una regla, calculada como la razón entre la confianza de la regla y la probabilidad de la consecuencia.

**Diferencias entre Verosimilitud y Probabilidad**:

- **Probabilidad**: Mide la posibilidad de que ocurra un evento dado un modelo o distribución conocida.
- **Verosimilitud (Likelihood)**: Mide qué tan bien un modelo explica un conjunto de datos observado. En modelado estadístico, se utiliza para estimar parámetros que maximizan la verosimilitud de observar los datos dados.

### Difusión y Estándares

La **explicabilidad** de los modelos es crucial para su adopción en entornos empresariales. Modelos interpretables facilitan la confianza y comprensión por parte de los usuarios finales y stakeholders.

El **PMML (Predictive Model Markup Language)** es un estándar basado en XML que permite definir y compartir modelos de minería de datos entre diferentes herramientas y plataformas. Al proporcionar un formato común, facilita la integración de modelos en sistemas de producción sin necesidad de reimplementarlos, acelerando su despliegue y uso efectivo en la organización.

## Tabla de nomenclaturas comunes

| Término en Inglés   | Término en Español           | Definición                                                                        |
| ------------------- | ---------------------------- | --------------------------------------------------------------------------------- |
| Accuracy            | Precisión                    | Proporción de predicciones correctas.                                             |
| Precision           | Valor Predictivo Positivo    | Proporción de verdaderos positivos entre todos los positivos predichos.           |
| Recall              | Sensibilidad o Exhaustividad | Proporción de verdaderos positivos detectados sobre el total de positivos reales. |
| Specificity         | Especificidad                | Proporción de verdaderos negativos detectados sobre el total de negativos reales. |
| F-Score             | Puntaje F                    | Media armónica de la precisión y la exhaustividad.                                |
| True Positive (TP)  | Verdadero Positivo           | Instancias correctamente predichas como positivas.                                |
| True Negative (TN)  | Verdadero Negativo           | Instancias correctamente predichas como negativas.                                |
| False Positive (FP) | Falso Positivo               | Instancias incorrectamente predichas como positivas.                              |
| False Negative (FN) | Falso Negativo               | Instancias incorrectamente predichas como negativas.                              |

### Fuentes:

<https://es.wikipedia.org/wiki/Curva_ROC>

## Caso práctico: clasificación

### Caso práctico 1: Clasificador para Detección de Cáncer

Supón un clasificador que detecta cáncer (sí/no) con un **accuracy del 99%**. Si la tasa de personas con cáncer es muy baja, un clasificador que siempre predice "no" puede obtener este alto accuracy al fallar en identificar los casos positivos.

Por otro lado, un clasificador con un **recall del 99%** detecta casi todos los casos de cáncer, pero puede tener falsos positivos altos, lo que implica realizar pruebas innecesarias.

Un clasificador con **precisión del 99%** se enfoca en minimizar falsos positivos, asegurando que la mayoría de diagnósticos positivos son correctos. Este ejemplo ilustra cómo las métricas deben seleccionarse en función de la importancia de identificar verdaderos positivos o reducir falsos positivos.

### Caso práctico 2: Clasificador para Detección de Cáncer (con cálculo)

Imaginemos un clasificador para detectar cáncer en un conjunto de datos con 1,000 pacientes, donde solo 10 realmente tienen cáncer. Esto significa que hay **10 casos positivos** y **990 casos negativos**.

Supongamos que evaluamos dos clasificadores en este conjunto de datos:

1. **Clasificador con alto “Accuracy” pero bajo “Precision” y “Recall”**\ Este clasificador ciego predice que TODOS los pacientes NO tienen cáncer. Así, tendría una precisión general (accuracy) alta debido al bajo número de casos positivos:
    - **TP (Verdaderos Positivos)**: 0 (no identificó ningún caso positivo correctamente)
    - **TN (Verdaderos Negativos)**: 990
    - **FP (Falsos Positivos)**: 0
    - **FN (Falsos Negativos)**: 10 (falló en detectar todos los casos de cáncer)

**Cálculo de métricas**:

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)\ = (0 + 990) / (0 + 990 + 0 + 10)\ = 990 / 1000\ = 0.99 o **99%**

Aunque el **accuracy es del 99%**, este modelo es poco útil para detectar cáncer, ya que **no identifica ningún caso positivo** (0% recall y precisión).

1. **Clasificador con alto “Recall” pero menor “Precision”**\ Otro clasificador se centra en identificar todos los casos de cáncer, aunque genere algunos falsos positivos. Este clasificador detecta 9 de los 10 pacientes con cáncer, pero también clasifica erróneamente a 20 pacientes sanos como positivos.
    - **TP (Verdaderos Positivos)**: 9
    - **TN (Verdaderos Negativos)**: 970
    - **FP (Falsos Positivos)**: 20
    - **FN (Falsos Negativos)**: 1

**Cálculo de métricas**:

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)\ = (9 + 970) / (9 + 970 + 20 + 1)\ = 979 / 1000\ = 0.979 o **97.9%**
- **Precision** = TP / (TP + FP)\ = 9 / (9 + 20)\ = 9 / 29\ = 0.31 o **31%**
- **Recall** = TP / (TP + FN)\ = 9 / (9 + 1)\ = 9 / 10\ = 0.9 o **90%**

Aunque el **accuracy** es del 97.9%, similar al primer clasificador, este modelo es más efectivo en la detección de casos positivos gracias a un **recall del 90%**, capturando casi todos los casos de cáncer. Sin embargo, su **precisión es baja** (31%), lo que significa que solo el 31% de los diagnósticos positivos son realmente correctos.
