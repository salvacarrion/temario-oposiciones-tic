# Inteligencia artificial y aprendizaje automático
## Conceptos básicos

La inteligencia artificial (IA) es una rama de la informática que busca
crear sistemas capaces de realizar tareas que normalmente requieren
inteligencia humana. Esto incluye actividades como el aprendizaje, el
razonamiento, la percepción, la comprensión del lenguaje natural y la
toma de decisiones. La IA ha revolucionado múltiples industrias, desde
la medicina hasta las finanzas y la logística.


## Aprendizaje automático (machine learning)
**Aprendizaje Automático (Machine Learning)**

El aprendizaje automático es una subdisciplina de la IA que permite a
las máquinas aprender de datos y mejorar con la experiencia sin ser
explícitamente programadas.

- **Aprendizaje Supervisado (Supervised)**: Los algoritmos se entrenan
  con datos etiquetados. Por ejemplo, un modelo que clasifica correos
  electrónicos como "spam" o "no spam" basándose en ejemplos
  preclasificados.

  - **Aprendizaje Semisupervisado (Semi-supervised)**: Combina una
    pequeña cantidad de datos etiquetados con una gran cantidad de datos
    no etiquetados. Por ejemplo, en reconocimiento de voz, donde solo
    algunas grabaciones están transcritas.

  - **Aprendizaje Autosupervisado (Self-supervised)**: Los modelos
    generan sus propias etiquetas a partir de los datos. Por ejemplo,
    los modelos de lenguaje, en donde se trata de predecir la palabra
    siguiente dada las anteriores

- **Aprendizaje No Supervisado (Unsupervised)**: Trabaja con datos no
  etiquetados para encontrar estructuras ocultas. Un ejemplo es el
  agrupamiento de clientes en segmentos de mercado basándose en
  comportamientos de compra.

- **Aprendizaje por Refuerzo (RL)**: Los agentes aprenden mediante
  ensayo y error, recibiendo recompensas o penalizaciones. Un caso
  famoso es AlphaGo de DeepMind, que aprendió a jugar Go a nivel
  superhumano.

- **Aprendizaje en contexto (In-context Learning):** Técnica en la que
  un modelo (generalmente LLM) puede “aprender” a realizar tareas
  específicas a partir de los ejemplos proporcionados y sin necesitar
  reentrenamiento. Esto se realiza en tiempo de inferencia, por lo que
  **en ningún se modifican sus parámetros.**

- **Aprendizaje de Transferencia (Transfer Learning / Fine-tuning):**
  Consiste en reutilizar un modelo entrenado en una tarea diferente
  (pero similar), para ajustarlo a una nueva tarea usando menos datos
  aunque más específicos. Reduce significativamente el tiempo de
  aprendizaje

  - **Destilado de conocimiento (Knowledge distillation):** Técnica para
    transferir el conocimiento de un modelo grande (**teacher model**) a
    uno más pequeño (**student model**), reduciendo su tamaño y
    complejidad sin comprometer significativamente la precisión


## Deep learning y redes neuronales
**Deep Learning y Tipos de Redes Neuronales**

El aprendizaje profundo utiliza redes neuronales con múltiples capas
para modelar y entender patrones complejos en datos.

- **Perceptrón Multicapa (MLP)**: Consiste en capas completamente
  conectadas. Se utiliza en tareas de clasificación y regresión simples.

- **Redes Neuronales Convolucionales (CNN)**: Especializadas en procesar
  datos con estructura de cuadrícula, como imágenes. Son fundamentales
  en reconocimiento facial y análisis de imágenes médicas.

- **Redes Neuronales Recurrentes (RNN)**: Adecuadas para datos
  secuenciales, como texto y audio. Por ejemplo, en la generación de
  subtítulos automáticos.

  - **GRU (Gated Recurrent Unit)** y **LSTM (Long Short-Term Memory)**:
    Variantes que superan limitaciones de las RNN estándar, permitiendo
    recordar información a largo plazo.

- **Transformers**: Introducidos para manejar dependencias a largo plazo
  sin recurrencia. Utilizan mecanismos de atención y son la base de
  modelos de lenguaje avanzados como GPT-3 y GPT-4.

**Modelo de Atención**

El mecanismo de atención permite a los modelos enfocarse en partes
específicas de la entrada, asignando pesos a diferentes elementos.


## IA distribuida y federada
**Inteligencia Artificial Distribuida**

La inteligencia artificial distribuida se refiere a sistemas donde
múltiples agentes inteligentes colaboran para resolver problemas
complejos. Estos agentes pueden estar geográficamente dispersos y
comunicarse a través de redes. Este enfoque es esencial en sistemas
multiagente, redes neuronales distribuidas y robótica en enjambre.


## Evolución histórica de la IA
**Principios Matemáticos y Evolución de la IA**

Los fundamentos matemáticos de las redes neuronales y el aprendizaje
automático datan de 1957, con el perceptrón de Frank Rosenblatt. Sin
embargo, varias limitaciones técnicas llevaron a períodos conocidos como
"invierno de la IA", donde el interés y la inversión disminuyeron.

**Factores que han impulsado la IA Moderna**:

- **Almacenamiento Masivo de Datos**: La disponibilidad de grandes
  conjuntos de datos como ImageNet (con más de 14 millones de imágenes)
  permitió entrenar modelos más precisos.

- **Computación de Alto Rendimiento**: El avance en hardware,
  especialmente GPUs, hizo posible entrenar redes neuronales profundas
  de manera eficiente.

- **Redescubrimiento y Mejora de las Redes Neuronales**: Innovaciones
  como las funciones de activación ReLU, técnicas de regularización y
  optimizadores avanzados renovaron la confianza en las redes
  neuronales.

**Referencias Históricas Clave**

- **1805-1809:** Legendre y Gauss utilizaron la regresión lineal por
  mínimos cuadrados para encontrar un buen ajuste lineal aproximado a un
  conjunto de puntos para predecir el movimiento planetario.

- **1957**: Introducción del perceptrón por Frank Rosenblatt, marcando
  el inicio de las redes neuronales.

- **Años 70 y 80**: Primer "invierno de la IA" debido a limitaciones
  técnicas y sobreexpectativas.

- **2012**: AlexNet gana la competición ImageNet, demostrando el poder
  de las redes neuronales profundas y reavivando el interés en el
  aprendizaje profundo.

- **Actualidad**: Proliferación de modelos avanzados, aumento
  exponencial en parámetros y capacidades, IA generativa, y debates
  éticos sobre el futuro de la IA.
