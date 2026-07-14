# Inteligencia artificial

## Concepto y evolución histórica

La inteligencia artificial (IA) es la rama de la informática que estudia cómo construir sistemas capaces de realizar tareas que, cuando las realiza una persona, exigen inteligencia: percibir, razonar, aprender, comunicarse en lenguaje natural y tomar decisiones. No es una técnica única, sino un campo cuyo enfoque dominante ha ido cambiando: de los sistemas basados en reglas y conocimiento experto de los años 70-80 al aprendizaje a partir de datos que impera desde 2012.

- **IA estrecha (narrow AI)**: sistemas especializados en una tarea o dominio concreto (traducir, detectar fraude, conducir). Toda la IA desplegada hoy es estrecha, incluidos los grandes modelos de lenguaje.
- **IA general (AGI)**: hipotético sistema capaz de desempeñar cualquier tarea intelectual humana con competencia equivalente. Es el objetivo declarado de los grandes laboratorios, pero no existe consenso sobre su definición operativa ni sobre plazos.
- **Relación entre disciplinas**: la IA engloba el **aprendizaje automático** (*machine learning*) y este, a su vez, el **aprendizaje profundo** (*deep learning*). Los grandes modelos de lenguaje son un caso particular de aprendizaje profundo.

Hitos principales:

| Año | Hito |
| --- | --- |
| **1943** | McCulloch y Pitts formulan el primer modelo matemático de neurona artificial |
| **1950** | Turing plantea el test de Turing ("Computing Machinery and Intelligence") |
| **1956** | Conferencia de **Dartmouth**: McCarthy acuña el término *artificial intelligence* |
| **1957** | **Perceptrón** de Rosenblatt: primera neurona artificial entrenable |
| 1974-1980 y 1987-1993 | "Inviernos de la IA": las expectativas incumplidas hunden la financiación |
| **1986** | Rumelhart, Hinton y Williams popularizan la retropropagación |
| **1997** | **Deep Blue** (IBM) derrota a Kaspárov al ajedrez |
| **2012** | **AlexNet** gana la competición ImageNet: comienza la era del aprendizaje profundo |
| **2016** | **AlphaGo** (DeepMind) derrota a Lee Sedol al go mediante aprendizaje por refuerzo |
| **2017** | Google publica la arquitectura **Transformer** ("Attention Is All You Need") |
| **2022** | **ChatGPT** (noviembre) populariza la IA generativa |
| 2024- | Modelos de razonamiento y agentes: la computación se desplaza a la inferencia |

El auge actual se explica por la confluencia de tres factores: **datos masivos** (ImageNet aportó más de **14 millones** de imágenes etiquetadas; la web, billones de palabras), **hardware paralelo** (las GPU abarataron órdenes de magnitud el entrenamiento) y **mejoras algorítmicas** (ReLU, técnicas de regularización, el Transformer). La lectura de fondo la formuló Sutton en *The Bitter Lesson* (2019): a largo plazo, los métodos generales que escalan con la computación acaban superando a los sistemas construidos sobre conocimiento experto codificado a mano.

## Aprendizaje automático (machine learning)

El aprendizaje automático sustituye la programación explícita de reglas por el ajuste de un modelo a partir de ejemplos: sus parámetros se optimizan para minimizar el error sobre los datos de entrenamiento, con el objetivo de que lo aprendido **generalice** a datos nuevos. Según la señal de la que se aprende, se distinguen varios paradigmas:

- **Aprendizaje supervisado**: entrena con datos etiquetados. Incluye la **clasificación** (asignar categorías: correo *spam* o legítimo) y la **regresión** (predecir un valor continuo: el precio de una vivienda).
- **Aprendizaje no supervisado**: busca estructura en datos sin etiquetar. Ejemplos: *clustering* o agrupamiento (segmentar usuarios por comportamiento) y reducción de dimensionalidad (PCA).
- **Aprendizaje semisupervisado**: combina pocos datos etiquetados con muchos sin etiquetar, cuando etiquetar es caro (transcripciones médicas, imágenes anotadas por expertos).
- **Aprendizaje autosupervisado**: el propio dato genera la etiqueta, sin anotación humana: predecir la palabra siguiente de un texto o la parte oculta de una imagen. Es la base del preentrenamiento de los grandes modelos de lenguaje y lo que permite aprovechar corpus masivos sin etiquetar.
- **Aprendizaje por refuerzo**: un agente aprende por ensayo y error interactuando con un entorno que le devuelve recompensas o penalizaciones. Es la técnica tras **AlphaGo** y, combinado con preferencias humanas (RLHF), parte esencial del ajuste de los asistentes actuales.
- **Aprendizaje por transferencia (transfer learning)**: reutilizar un modelo entrenado en una tarea para adaptarlo (*fine-tuning*) a otra relacionada con muchos menos datos y coste.
    - **Destilación de conocimiento**: entrenar un modelo pequeño (*student*) para imitar a uno grande (*teacher*), reduciendo tamaño y coste de inferencia con una pérdida de calidad limitada.

Conceptos transversales de evaluación, imprescindibles en cualquier proyecto:

- **Partición de datos**: entrenamiento (ajustar parámetros), validación (elegir hiperparámetros) y test (estimar el rendimiento real sobre datos nunca vistos).
- **Sobreajuste (overfitting)**: el modelo memoriza el conjunto de entrenamiento y falla al generalizar; el **infraajuste** es el defecto contrario (modelo demasiado simple). Se combaten con regularización, parada temprana y más datos.
- **Métricas**: exactitud (*accuracy*), precisión, exhaustividad (*recall*) y **F1** (media armónica de las dos anteriores), derivadas de la matriz de confusión. En problemas desbalanceados (fraude, diagnóstico) la exactitud engaña: un clasificador que siempre dice "sano" acierta el 99 % y no sirve para nada.

## Aprendizaje profundo y redes neuronales

El aprendizaje profundo emplea redes de neuronas artificiales organizadas en muchas capas. Cada neurona calcula una suma ponderada de sus entradas y aplica una función de activación no lineal (típicamente **ReLU**); la red se entrena con **retropropagación** y descenso de gradiente, ajustando millones o billones de pesos. Su despegue fue posible porque estas operaciones (multiplicaciones de matrices) se paralelizan de forma natural en GPU. Las familias principales:

- **Perceptrón multicapa (MLP)**: capas totalmente conectadas; la arquitectura básica para clasificación y regresión sobre datos tabulares.
- **Redes convolucionales (CNN)**: explotan la estructura espacial de las imágenes mediante filtros que detectan patrones locales. Son la base de la **visión por computador**: clasificación de imágenes, detección de objetos, segmentación, OCR, reconocimiento facial y análisis de imagen médica.
- **Redes recurrentes (RNN)**: procesan secuencias (texto, voz, series temporales) manteniendo un estado interno. Las variantes **LSTM** (1997) y **GRU** resolvieron su dificultad para retener dependencias largas, pero su naturaleza secuencial limita la paralelización y hoy están desplazadas por el Transformer.
- **Transformer** (2017): elimina la recurrencia y se basa en la **autoatención** (*self-attention*): cada token pondera su relación con todos los demás de la secuencia en paralelo. Esto captura dependencias a cualquier distancia y, sobre todo, permite entrenar a escala masiva en GPU. Sus dos variantes clásicas: *encoder* (BERT, orientado a comprensión) y *decoder* (familia GPT, orientado a generación), hoy la dominante.
- **Embeddings**: representaciones de palabras, frases o documentos como vectores densos en los que la cercanía geométrica captura similitud semántica. Son la base de la búsqueda semántica y de las bases de datos vectoriales empleadas en RAG.

## Grandes modelos de lenguaje: entrenamiento y arquitecturas

Un gran modelo de lenguaje (LLM, *large language model*) es un Transformer de tipo *decoder* con miles de millones de parámetros entrenado para predecir el siguiente **token** (unidad mínima de texto, del orden de una subpalabra: en español, una palabra son ~1,5-2 tokens). De ese objetivo tan simple, aplicado a escala suficiente, emergen capacidades generales: traducción, resumen, clasificación, extracción de información, generación de código o conversación. El entrenamiento moderno tiene fases bien diferenciadas:

- **Preentrenamiento**: predicción del siguiente token sobre corpus de billones de tokens (texto web curado, código, libros). Produce un **modelo base**: un "autocompletar erudito" que continúa texto pero no sigue instrucciones.
- **Post-entrenamiento**: convierte el modelo base en asistente útil y seguro.
    - **Ajuste supervisado (SFT)**: se afina con ejemplos de pares instrucción-respuesta de alta calidad.
    - **Aprendizaje por refuerzo con retroalimentación humana (RLHF)**: se entrena un modelo de recompensa a partir de preferencias humanas entre respuestas y se optimiza el LLM contra él. Variantes: **DPO** (optimización directa de preferencias, sin modelo de recompensa explícito) y RLAIF (retroalimentación generada por otra IA).
- **Ajuste eficiente (PEFT/LoRA)**: en lugar de reentrenar todos los pesos, se insertan adaptadores de bajo rango sobre el modelo congelado. Permite especializar un modelo a un dominio (jurídico, sanitario) entrenando <1 % de los parámetros, con una fracción mínima del coste.
- **In-context learning y prompting**: el modelo también "aprende" en tiempo de inferencia a partir de los ejemplos e instrucciones incluidos en el propio contexto, sin modificar ningún parámetro.

Arquitecturas y capacidades actuales:

- **Mixture-of-Experts (MoE)**: la red se divide en "expertos" y cada token activa solo unos pocos; se obtiene la capacidad de un modelo enorme con el coste de inferencia de uno mediano (DeepSeek-V3: **671.000 M** de parámetros totales, ~**37.000 M** activos por token).
- **Modelos multimodales**: procesan y generan texto, imagen y audio de forma nativa. Habilitan el **procesamiento inteligente de documentos** (IDP): extracción automática de datos de facturas, formularios y expedientes combinando visión y lenguaje. Fuera del lenguaje, la generación de imagen y vídeo se apoya en **modelos de difusión** (antes, GAN).
- **Ventana de contexto**: cantidad de tokens que el modelo maneja en una consulta. Ha pasado de ~**2.000** tokens (GPT-3, 2020) a **128.000-1.000.000+** en los modelos actuales: caben expedientes completos, bases de código o libros enteros.

Las **leyes de escalado** (Kaplan et al., 2020) mostraron que el rendimiento mejora de forma predecible al aumentar parámetros, datos y computación; el estudio **Chinchilla** (2022) las refinó: para un presupuesto dado conviene entrenar modelos más pequeños con más datos (~**20 tokens por parámetro**). El preentrenamiento puro muestra hoy rendimientos decrecientes, y la frontera se ha desplazado al post-entrenamiento, el razonamiento en inferencia y los agentes.

Por último, el mercado se divide entre modelos **de pesos abiertos** (Llama, Mistral, Qwen, DeepSeek), descargables y ejecutables en infraestructura propia, y modelos **cerrados** servidos por API (GPT, Claude, Gemini). Pesos abiertos no equivale a *open source*: rara vez se publican los datos y la receta de entrenamiento. La dimensión de **soberanía tecnológica** es creciente: en España, la iniciativa pública **ALIA** (Gobierno de España y Barcelona Supercomputing Center, sobre el superordenador MareNostrum 5) desarrolla modelos abiertos entrenados en castellano y lenguas cooficiales.

## Modelos de razonamiento y panorama actual

La última generación de modelos añade un ingrediente nuevo: antes de responder, el modelo "piensa". Genera una cadena de razonamiento interna en la que planifica, prueba enfoques, se verifica y se corrige, y solo después emite la respuesta visible. Ese bucle de pensamiento no se programa: se entrena.

- **Cadena de pensamiento (*chain-of-thought*)**: razonar paso a paso por escrito antes de dar la respuesta final. Se descubrió como técnica de *prompting* (Wei et al., 2022): pedir al modelo que muestre sus pasos mejora drásticamente el rendimiento en problemas complejos. Hoy es un comportamiento entrenado y en gran parte interno.
- **Recompensas verificables (RLVR)**: el razonamiento se entrena con aprendizaje por refuerzo sobre problemas cuya solución puede comprobarse automáticamente (matemáticas con resultado exacto, código que pasa pruebas): el modelo explora estrategias y se refuerzan las cadenas que conducen a la respuesta correcta, sin necesidad de anotadores humanos. Lo estrenó **o1** (OpenAI, **2024**); **DeepSeek-R1** (**enero de 2025**) publicó la receta con pesos abiertos y demostró que era reproducible a una fracción del coste.
- **Presupuesto de pensamiento (*thinking budget*)**: la computación dedicada a razonar es configurable: más tokens de pensamiento mejoran los problemas difíciles a cambio de latencia y coste (*test-time compute*). Es el segundo eje de escalado: además de entrenar modelos mayores, dejarles pensar más en inferencia. Los modelos actuales son híbridos: deciden (o se les indica) cuánto pensar según la dificultad.
- **Benchmarks**: los clásicos (MMLU) están saturados por los modelos de frontera; las referencias actuales son **SWE-bench Verified** (resolver *issues* reales de GitHub), **GPQA Diamond** (ciencia de nivel de doctorado), **HLE** (*Humanity's Last Exam*, conocimiento experto multidisciplinar) y **ARC-AGI-2** (razonamiento abstracto).

En cuanto al panorama concreto (foto a **mediados de 2026**; el ritmo de reemplazo es de meses), conviene saber que desde GPT-4 los laboratorios cerrados no publican el número de parámetros de sus modelos: para **GPT-4** la estimación filtrada (nunca confirmada) fue de **~1,8 billones** con arquitectura MoE, y la escala de los modelos abiertos actuales es coherente con esa cifra. Todos los modelos de frontera son hoy MoE, razonadores y multimodales, con contextos de **1-2 millones** de tokens.

| Modelo | Laboratorio | Pesos | Parámetros (totales / activos) |
| --- | --- | --- | --- |
| GPT-5.5 | OpenAI | Cerrados | No publicados |
| Gemini 3.1 Pro | Google | Cerrados | No publicados |
| Claude Fable 5 / Opus 4.8 | Anthropic | Cerrados | No publicados |
| Grok 4 | xAI | Cerrados | No publicados |
| DeepSeek V4 | DeepSeek | Abiertos | ~1.600.000 M / ~49.000 M |
| Kimi K2 | Moonshot AI | Abiertos | 1.000.000 M / 32.000 M |
| Llama 4 Maverick | Meta | Abiertos | 400.000 M / 17.000 M |
| Qwen3-235B | Alibaba | Abiertos | 235.000 M / 22.000 M |

La lección estable (los nombres caducan; las tendencias no): la arquitectura dominante es MoE, el razonamiento en inferencia es el segundo eje de escalado, los pesos abiertos siguen a la frontera cerrada con 6-12 meses de retraso y una fracción del coste, y la competición se ha desplazado del modelo aislado al sistema completo (herramientas, agentes, integración).

## Infraestructura, consumo y costes

Detrás de cada modelo hay una infraestructura de escala industrial: entrenar un modelo de frontera moviliza decenas de miles de aceleradores durante meses, y servirlo a millones de usuarios exige flotas de inferencia optimizadas al milímetro. Los elementos clave:

- **Aceleradores**: GPU de centro de datos (NVIDIA H100/B200), TPU (Google) y, en el extremo cliente, NPU integradas. Lo escaso no son los FLOPS sino la memoria **HBM** apilada junto al chip: su capacidad y ancho de banda dictan qué modelos caben y a qué velocidad responden.
- **Hardware heterogéneo**: la CPU orquesta, la GPU calcula y las DPU/SmartNIC mueven datos; incluso las dos fases de la inferencia (*prefill*, que procesa el contexto, y *decode*, que genera token a token) se sirven en grupos de hardware distintos por tener perfiles opuestos.
- **Interconexión**: NVLink (~**900 GB/s** por GPU) dentro del nodo e InfiniBand o Ethernet de 400-800 Gb/s entre nodos. El entrenamiento distribuido vale lo que valga su red: miles de GPU sincronizando gradientes constantemente.
- **Racks y refrigeración**: de los ~5-10 kW por rack del centro de datos clásico se ha pasado a **40-120+ kW** en racks de IA (un rack GB200 NVL72 ronda los **120 kW**), lo que obliga a refrigeración líquida y rediseño eléctrico completo.

Los cuellos de botella reales del sector, por orden de dureza:

- **Memoria ("memory wall")**: la inferencia es *memory-bound*: generar cada token exige releer todos los pesos desde la HBM, así que limita el ancho de banda, no la capacidad de cálculo.
- **Energía**: los centros de datos consumieron ~**415 TWh en 2024** (en torno al **1,5 %** de la electricidad mundial) y la IEA proyecta que la cifra casi se duplique en 2030. La disponibilidad de potencia eléctrica (no de chips) es ya el principal límite de crecimiento.
- **Datos**: el texto público de calidad es finito; la frontera depende cada vez más de datos sintéticos y de una curación agresiva.

Para abaratar la inferencia se combinan varias técnicas:

- **Cuantización**: reducir la precisión numérica de los pesos: FP32 (4 bytes/parámetro) → FP16/BF16 (2) → INT8 (1) → INT4 (0,5). Hasta 8 bits la pérdida de calidad es mínima; a 4 bits, moderada. Divide la memoria necesaria y multiplica la velocidad. Puede aplicarse tras el entrenamiento (PTQ) o durante él (QAT).
- **KV cache**: memoriza los cálculos de atención de los tokens ya procesados para no repetirlos; su tamaño crece con la longitud de contexto y el número de usuarios concurrentes, y compite por la misma memoria que los pesos.
- ***Batching* continuo y decodificación especulativa**: agrupar peticiones de muchos usuarios para amortizar cada lectura de pesos, y usar un modelo pequeño que "borra" varios tokens que el grande verifica de golpe.

En cuanto a costes: un entrenamiento de frontera supera los **100 millones de dólares** solo en computación (estimación para GPT-4); una GPU de centro de datos cuesta decenas de miles de euros y un servidor de 8 GPU, varios cientos de miles. A escala, la flota de inferencia acaba costando bastante más que el entrenamiento. Sobre esta base se plantea la decisión de despliegue **on-premise frente a nube/API**, con dos matices que suelen pasarse por alto:

- **El valor ya no está en los pesos, sino en el ecosistema.** Descargar un modelo abierto proporciona un motor, no un coche: la utilidad real viene del sistema que lo rodea (herramientas y agentes, RAG, evaluaciones continuas, filtros de seguridad, actualizaciones, integraciones), que los proveedores renuevan a un ritmo que una instalación aislada no puede seguir.
- **Operar inferencia competitiva es extraordinariamente difícil.** Exprimir la utilización de una flota de GPU (kernels optimizados, planificación de *batching*, servicio desagregado, monitorización) es un problema de ingeniería en el que fallan incluso grandes organizaciones; los proveedores de API amortizan esa ingeniería entre millones de clientes.

El criterio práctico para una Administración: API o nube para capacidad general, modelos de pesos abiertos on-premise cuando la sensibilidad de los datos o la soberanía lo exijan, y arquitecturas híbridas como norma.

Sobre sostenibilidad conviene manejar números y no titulares:

- **Energía por consulta**: una consulta de texto mediana consume ~**0,24-0,34 Wh** (mediciones de Google, agosto de 2025, y estimaciones de OpenAI): como una bombilla LED de 10 W encendida unos dos minutos. El impacto relevante no es la consulta individual, sino el agregado del sector y, sobre todo, el entrenamiento y el vídeo generativo.
- **El consumo de agua**: los titulares de "medio litro por conversación" mezclan agua directa (refrigeración evaporativa) con agua indirecta (la usada en generar la electricidad) y parten de estimaciones antiguas. La medición directa actual ronda **0,26 ml por consulta** mediana (unas cinco gotas). El problema real es local y agregado: dónde se ubican los centros (zonas con estrés hídrico) y qué tecnología de refrigeración usan; los circuitos cerrados de refrigeración líquida apenas consumen agua.
- **PUE** (*Power Usage Effectiveness*): ratio entre la energía total del centro y la consumida por el equipamiento TI; los centros hiperescala modernos operan en torno a **1,1**.

## Alucinaciones y su mitigación

Una alucinación es contenido falso o inventado que el modelo presenta con total seguridad y fluidez. No es un defecto puntual corregible, sino una consecuencia del objetivo de entrenamiento: el modelo optimiza la verosimilitud del texto, no su verdad, y además la mayoría de las evaluaciones puntúan mejor arriesgar una respuesta que admitir "no lo sé", con lo que el propio proceso de entrenamiento premia adivinar (OpenAI, *Why Language Models Hallucinate*, 2025). Sus causas: el objetivo de predicción del siguiente token, lagunas y errores del corpus, incentivos de evaluación mal diseñados y la decodificación estocástica.

La mitigación más extendida es **RAG** (*retrieval-augmented generation*): recuperar documentos relevantes de una base de conocimiento (habitualmente vía búsqueda semántica sobre embeddings) e inyectarlos en el contexto para que el modelo responda apoyándose en ellos. Conviene ser preciso sobre qué resuelve y qué no:

- **RAG mitiga**: las lagunas de conocimiento del modelo, la desactualización (información posterior a su entrenamiento) y el acceso a datos privados de la organización; además permite citar las fuentes usadas.
- **RAG no mitiga**: los errores de razonamiento; la infidelidad al contexto (el modelo puede contradecir o distorsionar lo que se le ha dado); los fallos del propio recuperador (si se recupera el documento equivocado, la respuesta será errónea con apariencia de fundamentada); ni los conflictos entre fuentes. RAG reduce las alucinaciones; no las elimina.

El resto del arsenal realista:

- **Citación verificable**: obligar a que cada afirmación enlace con el fragmento de la fuente que la sustenta, de modo que un humano pueda auditarla.
- **Abstención calibrada**: diseñar el sistema (y sus evaluaciones) para que rechazar o escalar una pregunta dudosa sea mejor que inventar.
- **Verificación externa**: dar al modelo herramientas cuya salida es comprobable (ejecutar código, consultar una base de datos, buscar) en lugar de fiar el resultado a su memoria; o contrastar varias generaciones o modelos entre sí.
- **Guardrails y validación de salidas**: esquemas estructurados, reglas de negocio y filtros que comprueban la respuesta antes de usarla.
- **Supervisión humana** en decisiones con efectos sobre terceros: en el sector público no es solo prudencia, sino exigencia del régimen de actuación administrativa automatizada y del Reglamento europeo de IA (tema 35).

Igual de importante es saber qué **no** funciona: el *fine-tuning* especializa el estilo y el dominio, pero no convierte al modelo en veraz; fijar la temperatura a 0 lo hace determinista, no exacto; y prohibir las alucinaciones en el *prompt* es papel mojado.

## Agentes de IA

Un agente es un modelo de lenguaje que opera en bucle sobre un objetivo: no responde y termina, sino que trabaja hasta completar la tarea. Supone el salto del "modelo que responde" al "sistema que trabaja", y es el patrón dominante desde 2025.

- **Bucle agéntico**: razonar sobre el estado de la tarea → planificar el siguiente paso → actuar mediante una herramienta → observar el resultado → reflexionar y corregir el plan; y vuelta a empezar hasta completar el objetivo o escalarlo a un humano. Lo formalizó el patrón **ReAct** (Yao et al., **2022**): intercalar trazas de razonamiento y acciones funciona mejor que razonar o actuar por separado.

Sus componentes:

- **Modelo**: el motor de razonamiento y planificación; los modelos de razonamiento del apartado anterior son su base natural.
- **Herramientas** (*tool use / function calling*): buscar, leer y escribir ficheros, ejecutar comandos y código, consultar APIs y bases de datos. El **Model Context Protocol (MCP)**, estándar abierto publicado por Anthropic en **2024** y adoptado de forma transversal, normaliza cómo se conectan modelos, herramientas y fuentes de datos; su complemento **A2A** (*Agent2Agent*, Google, **2025**, cedido a la Linux Foundation) normaliza la comunicación entre agentes de distintos proveedores.
- **Contexto y memoria**: la ventana de contexto es la memoria de trabajo (instrucciones, historial de acciones y observaciones). Como es finita, los agentes de sesiones largas la compactan (resumen del trabajo hecho) y mantienen memoria persistente fuera de ella (ficheros de notas, bases vectoriales) que releen entre sesiones.
- **Entorno**: el espacio sobre el que actúa, típicamente un repositorio de ficheros versionado.

Patrones de diseño (Anthropic, "Building Effective Agents", **2024**); la regla práctica es usar la solución más simple que funcione:

- ***Workflows***: cuando el problema es predecible, el LLM ocupa pasos fijos de un flujo predefinido: encadenamiento de *prompts*, enrutado, paralelización, orquestador-trabajadores y evaluador-optimizador.
- **Agente autónomo**: el modelo dirige su propio proceso; se reserva para tareas abiertas donde no puede preverse el número de pasos.
- **Multiagente**: un orquestador descompone el trabajo y lo delega en subagentes especializados con permisos y contexto acotados.

El ejemplo de referencia de la categoría es **Claude Code** (Anthropic), un agente de terminal: explora un repositorio, edita ficheros, ejecuta comandos y pruebas, usa git y verifica su propio trabajo. Aunque nació para programar, cualquier corpus de trabajo estructurado como texto plano y versionado (código, pero también contratos, expedientes o temarios) se convierte en un espacio de trabajo agéntico; el rendimiento depende tanto de la estructura del repositorio (convenciones documentadas, fuentes de verdad explícitas, verificaciones automatizables) como del modelo.

La **evaluación** de agentes no puntúa respuestas, sino tareas completadas de principio a fin: **SWE-bench Verified** (resolver *issues* reales de GitHub), **GAIA** (asistencia general con herramientas y web) y **OSWorld** (manejar un ordenador por su interfaz gráfica) son las referencias.

Los agentes introducen un riesgo de seguridad específico: la **inyección de instrucciones** (*prompt injection*). Un contenido no confiable que el agente procesa (una página web, un correo, un documento adjunto) puede contener instrucciones maliciosas que el modelo ejecute como si vinieran del usuario legítimo. Las defensas son arquitectónicas, no solo de modelo: mínimo privilegio en las herramientas, aislamiento (*sandboxing*), aprobación humana para acciones destructivas o con efectos externos, separación entre instrucciones y datos, y trazabilidad completa de las acciones.

## IA distribuida y federada

Bajo esta etiqueta conviven dos ideas complementarias: sistemas de múltiples agentes que cooperan, y entrenamiento repartido allí donde están los datos.

- **IA distribuida clásica**: sistemas multiagente en los que agentes autónomos, posiblemente dispersos geográficamente, cooperan o compiten para resolver un problema (robótica de enjambre, simulación, optimización logística).
- **Aprendizaje federado** (Google, **2017**, algoritmo FedAvg): entrenar un modelo común sin centralizar nunca los datos. Cada nodo (un hospital, un móvil) entrena localmente y comparte solo actualizaciones de pesos, que un servidor agrega en rondas sucesivas. Casos típicos: teclados predictivos móviles y colaboración entre hospitales sin ceder historias clínicas. Retos: heterogeneidad de datos y dispositivos, coste de comunicación y una privacidad que no es absoluta (las actualizaciones pueden filtrar información, por lo que se combina con agregación segura y privacidad diferencial).
- **Edge AI**: ejecución de modelos compactos directamente en el dispositivo (NPU de móviles y portátiles), que aporta latencia mínima, funcionamiento sin conexión y privacidad por diseño.

## Caso práctico: dimensionamiento del despliegue de un LLM

*Enunciado*: una Administración quiere un asistente interno sobre documentación sensible que no puede salir de su infraestructura. Se plantea servir on-premise un modelo de pesos abiertos de **70.000 millones de parámetros** (clase Llama 70B) para ~50 usuarios con contextos de hasta 32.000 tokens. Dimensionar memoria, hardware y consumo, y comparar con el uso de una API externa.

1. **Memoria de pesos**: la regla básica es "memoria ≈ n.º de parámetros × bytes por parámetro". En FP16 (2 bytes): 70.000 M × 2 = **140 GB**. Cuantizado a INT8: **70 GB**; a INT4: **~35 GB**.
2. **KV cache**: en esta clase de modelo, la caché de atención ocupa ~**0,3 MB por token** en FP16, es decir, ~**10 GB por conversación** de 32.000 tokens. Con una decena de conversaciones largas simultáneas en lote, la caché puede ocupar tanto como los propios pesos (se mitiga cuantizándola y con *paged attention*).
3. **Elección de GPU**: en FP16, solo los pesos ya exigen dos GPU de 80 GB; para servir con margen de caché y lote, lo razonable es un nodo de **4 × 80 GB** (320 GB). Cuantizando a INT8/INT4 bastarían 1-2 GPU, sacrificando algo de calidad y concurrencia.
4. **Consumo**: 4 GPU × ~700 W más el resto del nodo ≈ **3,5 kW** sostenidos. En servicio continuo: 3,5 kW × 720 h ≈ **2.500 kWh/mes**; aplicando un PUE de 1,3, ~3.300 kWh/mes, que a 0,15 €/kWh son ~**500 €/mes** de electricidad.
5. **Coste total**: la electricidad no es el coste dominante. Un nodo de 4 GPU de gama alta ronda los **150.000-200.000 €**, unos **3.000-4.000 €/mes** amortizado a 4 años, más el personal necesario para operarlo y optimizarlo.
6. **Comparación con API**: 50 usuarios intensivos generan del orden de 100 M de tokens/mes que, a precios típicos de mercado (entre décimas de euro y unos pocos euros por millón de tokens), cuestan **100-300 €/mes**: hasta 20 veces menos que el despliegue propio, siempre actualizado y sin operación.

*Conclusión*: con esta carga, el on-premise solo se justifica por la confidencialidad de los datos o por requisitos de soberanía, no por coste; el punto de equilibrio exige una utilización alta y sostenida de la infraestructura. Y la lección de fondo: dimensionar las GPU es la parte fácil del problema; construir y mantener el sistema completo de inferencia (colas y *batching*, observabilidad, evaluación continua de la calidad, actualización de modelos y seguridad) es donde se concentra el esfuerzo real del proyecto.

## Fuentes {.unnumbered .unlisted}

- Vaswani et al., "Attention Is All You Need" (2017): arquitectura Transformer.
- Kaplan et al., "Scaling Laws for Neural Language Models" (2020) y Hoffmann et al., "Training Compute-Optimal Large Language Models" (Chinchilla, 2022).
- Sutton, R., "The Bitter Lesson" (2019).
- Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022).
- DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2025).
- Panorama de modelos: anuncios y fichas técnicas de los laboratorios, consultados en julio de 2026; estimaciones de parámetros de modelos cerrados según Epoch AI, base de datos "Notable AI Models".
- Kalai et al. (OpenAI), "Why Language Models Hallucinate" (2025).
- Agencia Internacional de la Energía (IEA), informe "Energy and AI" (abril de 2025): consumo eléctrico de los centros de datos.
- Google, "Measuring the Environmental Impact of Delivering AI at Google Scale" (agosto de 2025): energía y agua por consulta.
- McMahan et al. (Google), "Communication-Efficient Learning of Deep Networks from Decentralized Data" (2017): aprendizaje federado.
- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022).
- Anthropic, "Building Effective Agents" (diciembre de 2024).
- Model Context Protocol, especificación abierta (Anthropic, 2024): modelcontextprotocol.io.
- Protocolo Agent2Agent (A2A), especificación abierta (Google / Linux Foundation, 2025).
- Gobierno de España / BSC-CNS, iniciativa ALIA: alia.gob.es.
