# Inteligencia artificial aplicada y su regulación

## Procesamiento del lenguaje natural y de documentos

### Procesamiento de Lenguaje Natural (PLN)

El PLN se centra en la interacción entre computadoras y lenguaje humano.

- **Aplicaciones del PLN**:
    - **Traducción Automática**: Google Translate y DeepL ofrecen traducciones en tiempo real entre múltiples idiomas.
    - **Análisis de Sentimiento**: Empresas analizan opiniones en redes sociales para evaluar la percepción de su marca.
    - **Reconocimiento de Voz**: Asistentes como Siri y Alexa transcriben y responden a comandos de voz.
    - **Chatbots y Asistentes Virtuales**: Soporte al cliente automatizado que entiende y responde en lenguaje natural.

### Procesamiento Inteligente de Documentos

Utiliza IA para automatizar la extracción y procesamiento de información de documentos. Combina PLN, visión por computador y aprendizaje automático para manejar documentos como facturas, contratos y formularios.

## IA generativa y grandes modelos de lenguaje

### Inteligencia Artificial General (AGI)

La AGI se refiere a sistemas de IA con capacidad para entender, aprender y aplicar inteligencia de manera general, similar a la humana. A diferencia de la IA estrecha (narrow), que se especializa en tareas específicas, la AGI aspira a manejar cualquier tarea intelectual.

El camino hacia la AGI implica avances significativos en modelos y arquitecturas.

- **Modelos Fundacionales (Foundational models)**: Grandes modelos pre-entrenados en enormes conjuntos de datos, adaptables a múltiples tareas sin necesidad de re-entrenamiento. Eliminan la necesidad de hacer fine-tuning.
- **Modelos Generativos (Generative AI)**: Modelos capaces de generar contenido nuevo (texto, imágenes, audio) a partir de los datos aprendidos.
    - **Riesgo de seguridad**: Puede generar conceptos que no existen en los datos de entrenamiento al poder interpolar entre conceptos conocidos.
- **IA Física (Physical AI):** Permite a las máquinas percibir, entender y realizar acciones complejas en el mundo real (físico).

**Tipos de modelos generativos**: texto-a-texto, texto-a-imagen, texto-a-audio, texto-a-video, texto-a-3d, imagen-a-video, imagen-a-audio, video-a-3d,… (X-a-X)

- **LLMs (Large Language Models)**: Son modelos entrenados para predecir la siguiente palabra en una oración. La innovación se da en la observación de que cuando se entrenan con suficientes datos y complejidad, se convierten en un “autocompletar con esteroides”, capaces de memorizar una gran cantidad de información y de generalizar e interpolar entre conceptos. No generan conocimiento nuevo, solo interpolan entre puntos conocidos.
    - **Ejemplos:** GPT-3 (175B de parámetros – 175GB de VRAM en 32bits), GPT-4 (~1.8T de parametros – 1.8TB VRAM en 32bits)
- **Asistentes**: Modelos de lenguaje (LLM) con los que se interactúa de forma conversacional.
    - **Prompt**: “Eres un asistente virtual. Human: {Hola que tal?}. Response: ”
- **MLLMs (Multimodal Large Language Models)**: Modelos de lenguaje que procesan múltiples tipos de datos, como texto, imágenes y audio. Ejemplo: GPT4o
- **LRMs (Large Reasoning Models)**: Modelos de lenguaje enfocados en mejorar las capacidades de razonamiento y resolución de problemas complejos.
- **Otros**: GANs (Generative Adversarial Networks), GANs (Generative Adversarial Networks), Diffusion Models

### Costes de Entrenamiento e Inferencia

El entrenamiento de modelos grandes es costoso y requiere recursos significativos.

- **Entrenamiento**: Suelen costar cientos de millones (\$/€). Por ejemplo, entrenar GPT-4 se estima que costó unos 100 millones de dólares (solo en costes computacionales).
- **Hardware necesario**: Granjas con cientos de miles de GPUs y TPUs de última generación.
    - **Coste de H200 (single GPU)**: ~30,000-40,000\$
    - **Coste de DGX H200 (Workstation):** ~500,000\$
- **Captura de Datos**: Implica el esfuerzo de miles de empleados para etiquetar datos y mejorar la calidad de las respuestas.

### Problema de las alucinaciones en modelos de lenguaje (LLMs)

Las alucinaciones en los modelos de lenguaje son respuestas generadas que, aunque puedan parecer coherentes y plausibles, no se basan en datos reales o precisos. Este fenómeno ocurre porque los LLMs están diseñados para predecir la siguiente palabra en una secuencia, basándose en patrones aprendidos durante su entrenamiento, sin una comprensión real del mundo o verificación de hechos.

### Causas de las alucinaciones:

- **Limitaciones en los datos de entrenamiento:** Si el modelo no ha sido expuesto a cierta información durante su entrenamiento, puede generar respuestas incorrectas o inventadas.
- **Sesgos y errores en los datos:** Datos de entrenamiento con información errónea o sesgada pueden llevar al modelo a generar respuestas inexactas.
- **Falta de mecanismos de verificación:** Los LLMs no tienen la capacidad intrínseca de verificar la veracidad de sus respuestas en tiempo real.

### Tamaño de las Ventanas Contextuales

La ventana contextual se refiere a la cantidad de información que un modelo puede procesar simultáneamente. Modelos como GPT-4 tienen ventanas contextuales de hasta 32,000 tokens, permitiendo mantener coherencia en textos largos.

### Arquitecturas RAG (Retrieval Augmented Generation)

Las arquitecturas RAG (Generación Aumentada por Recuperación) combinan modelos de lenguaje con sistemas de recuperación de información para mejorar la precisión y relevancia de las respuestas generadas. Este enfoque ayuda a mitigar el problema de las alucinaciones al proporcionar al modelo acceso a información actualizada y verificada durante el proceso de generación.

### Cómo funcionan las arquitecturas RAG:

1. **Consulta del usuario:** El usuario proporciona una entrada o pregunta.
2. **Recuperación de información:** El sistema busca en una base de datos o corpus relevante documentos o fragmentos que puedan contener la respuesta.
3. **Generación de respuesta:** El modelo de lenguaje utiliza tanto la consulta del usuario como la información recuperada para generar una respuesta más precisa y fundamentada.

### Paradigmas: Computación en Tiempo de Entrenamiento vs. Inferencia

- **Computación en Tiempo de Entrenamiento (train-time compute)**: Computación utilizada durante la fase de entrenamiento del modelo.
    - Se enfoca en optimizar los parámetros del modelo para que generalice bien en distintas tareas (“one-shot”).
    - **Ejemplo:** “Ver la disposición de un tablero de ajedrez y decidir qué pieza mover”
- **Computación en Tiempo de Inferencia (test-time compute)**: Computación utilizada durante la fase de inferencia, cuando el modelo responde.
    - Nuevo paradigma que permite al modelo "razonar" usando más tiempo en tareas complejas (similar a un Chain-of-Thought), mejorando su precisión y eficiencia en problemas difíciles mediante un procesamiento adicional
    - **Ejemplo:** “Ver la disposición de un tablero de ajedrez, hacer varias jugadas mentales con las diferentes piezas (de forma no exhaustiva), y luego decidir qué pieza mover”

### Leyes de Escalado (Scaling Laws)

Describen cómo el rendimiento de los modelos mejora al aumentar:

- **Computación**: Mayor poder computacional permite entrenar modelos más complejos.
- **Datos**: Más datos, y de mayor calidad, proporcionan mejor generalización.
- **Parámetros**: Más parámetros permiten capturar patrones más detallados y complejos.

**\*Nota personal sobre las Scaling Laws:** Las leyes de escalado parecen estar alcanzando un "punto muerto" o un "muro", en el que las mejoras de rendimiento se vuelven marginales pese al aumento de computación, la calidad de los datos y/o el tamaño de los modelos. Esto intuitivamente tiene sentido, ya que si nos limitamos a resolver una tarea centrándonos exclusivamente en predecir la siguiente palabra, sin descomponerla en sus componentes principales, acabaremos con una visión local y superficial (limitada a un único nivel de profundidad), lo que dificultará significativamente la resolución de tareas más complejas. En cambio, al incorporar estrategias de computación en tiempo de inferencia, análogo a los algoritmos de búsqueda DFS, podremos explorar estas tareas a diferentes niveles de profundidad, lo que facilitará la resolución y el análisis de problemas más complejos.

### The Bitter Lesson (Rich Sutton)

Un ensayo que argumenta que los mayores avances en IA provienen de métodos que aprovechan el aumento del poder computacional y el aprendizaje automático general, en lugar de incorporar conocimiento específico del dominio.

### Dificultad de Evaluación

- **Benchmarks limitados**: Las pruebas estándar pueden no reflejar las capacidades reales en situaciones del mundo real. Además, muchos modelos se entrenan usando ciertos benchmarks como referencia (overfit), lo que falsea su rendimiento real.
- **Evaluaciones Colaborativas (LMArena)**: Plataformas donde la comunidad contribuye a evaluar y mejorar modelos al usarlos, promoviendo transparencia y colaboración.

### Ejemplos de Modelos Actuales

- **BERT**: Modelo de Google para tareas de comprensión del lenguaje, utilizado en su motor de búsqueda.
- **GPT-3**: Modelo de OpenAI, con 175 mil millones de parámetros, capaz de generar texto coherente y realizar tareas como traducción y resumen.
- **GPT-4o**: Modelo de OpenAI, que puede procesar y generar texto, imágenes y audio de manera nativa.
- **o1**: Modelo de última generación de OpenAI, que estrena nuevo paradigma (test-time), y que dedica más tiempo al razonamiento antes de responder, lo que le permite abordar tareas complejas y resolver problemas más difíciles que modelos anteriores.
- **DALL·E 2**: Genera imágenes a partir de descripciones textuales, combinando procesamiento de lenguaje y visión por computadora.

### 5 Etapas de la AGI

- **Nivel 1 (IA Conversacional / Chatbots):** Mantienen conversaciones avanzadas y responden preguntas en lenguaje natural. (“Autocompletar++”)
    - **Ejemplo:** GPT-4, Claude 3.5
    - **Fecha:** 2020-2022
- **Nivel 2 (Razonadores / Reasoners):** Realizan razonamientos complejos y desglosan problemas paso a paso. (“LLM + DFS”)
    - **Ejemplo:** o1
    - **Fecha:** 2024-2025
- **Nivel 3 (Agentes Autónomos / Agents):** Actúan de manera autónoma en entornos controlados, realizando tareas específicas. (“LLM robusto y confiable”)
    - **Ejemplo:** Claude 3.5/oct24 (experimental)
    - **Fecha:** 2025-2027
- **Nivel 4 (Innovadores / Innovators):** Ayudan en la generación de ideas y soluciones innovadoras para nuevos problemas. (“Generan nuevo conocimiento, derivado composicionalmente a partir del existente”)
    - **Ejemplo:** -
    - **Fecha:** 2028-2032
- **Nivel 5 (Organización Autónoma / Organizations):** IA que puede gestionar y operar una organización de forma autónoma. (“Modelos confiables y altamente integrados en el ecosistema de la organización”)
    - **Ejemplo:** -
    - **Fecha:** 2035-2040
