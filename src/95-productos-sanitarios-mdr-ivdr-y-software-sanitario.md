# Productos sanitarios: reglamentos MDR e IVDR y software sanitario

Buena parte del software clínico (ayuda al diagnóstico, cálculo de dosis, algoritmos de IA sobre imagen) es, legalmente, un **producto sanitario**: necesita clasificación de riesgo, evaluación de la conformidad y **marcado CE** antes de usarse con pacientes. Este tema recorre el marco regulador europeo (MDR e IVDR) y español (RD 192/2023), la cualificación y clasificación del software, la evaluación de la conformidad, la vía especial del software fabricado por el propio centro sanitario y el encaje de la inteligencia artificial.

## Marco normativo: MDR, IVDR y RD 192/2023

- **Reglamento (UE) 2017/745 (MDR)**, de 5 de abril de 2017, **sobre los productos sanitarios**: deroga las Directivas 90/385/CEE (implantes activos) y 93/42/CEE (productos sanitarios). Aplicable desde el **26 de mayo de 2021** (aplazado un año por el Reglamento (UE) 2020/561 a causa de la pandemia).

**Texto consolidado a 9 de julio de 2024** (incluye el Reglamento (UE) 2024/1860; EUR-Lex lista versiones-fecha de 10 de enero de 2025 y 1 de enero de 2026 que corresponden a la aplicación diferida de disposiciones de ese mismo reglamento).

- **Reglamento (UE) 2017/746 (IVDR)**, sobre los **productos sanitarios para diagnóstico in vitro** (analizadores, reactivos, pruebas genéticas y su software): deroga la Directiva 98/79/CE y es aplicable desde el **26 de mayo de 2022**. Clasifica en cuatro clases de riesgo propias (**A, B, C y D**, de menor a mayor).

**Texto consolidado a 9 de julio de 2024.**

- **Real Decreto 192/2023, de 21 de marzo, por el que se regulan los productos sanitarios**: adapta el ordenamiento español al MDR en lo que este deja a los Estados miembros: régimen de las **instalaciones**, reprocesamiento de productos de un solo uso, organismos notificados, comercialización, distribución y venta, investigaciones clínicas, sistema de vigilancia y control del mercado.
    - **Licencia previa de funcionamiento (art. 7)**: la requieren las personas físicas y jurídicas que se dediquen a la **fabricación, importación, agrupación o esterilización** de productos sanitarios y las instalaciones en que se realicen esas actividades. La otorga la **AEMPS**, que notifica la resolución en un plazo de **tres meses**.

**Texto consolidado: sin modificaciones.**

- **La AEMPS** (Agencia Española de Medicamentos y Productos Sanitarios) es la **autoridad competente** española: designa y supervisa, registra comercializaciones, tramita la vigilancia y puede restringir o retirar productos del mercado.
- **Agentes económicos** (arts. 10-14 MDR): la cadena de responsabilidad sobre el producto.
    - **Fabricante (art. 10)**: responsable principal; mantiene un **sistema de gestión de riesgos** y un sistema de gestión de la calidad, realiza la **evaluación clínica**, elabora y actualiza la **documentación técnica** (Anexos II y III), pasa la evaluación de la conformidad, emite la **declaración UE de conformidad**, coloca el **marcado CE**, cumple las obligaciones de **UDI** y registro, y sostiene el seguimiento poscomercialización.
    - **Representante autorizado (art. 11)**: si el fabricante no está establecido en la UE, solo puede introducir el producto en el mercado si designa un **único representante autorizado**.
    - **Importador (art. 13)**: comprueba antes de introducir el producto que lleva el **marcado CE**, que existe la declaración UE de conformidad, que el fabricante está identificado y tiene representante autorizado, que el etiquetado y las instrucciones acompañan al producto y que tiene **UDI** asignado.
    - **Distribuidor (art. 14)**: verificaciones análogas antes de comercializar, y traslada al fabricante las reclamaciones e incidentes de que tenga noticia.
- **Persona responsable del cumplimiento de la normativa (art. 15)**: toda organización fabricante debe contar con al menos una, con cualificación acreditada (**título universitario** en Derecho, Medicina, Farmacia, Ingeniería u otra disciplina científica pertinente **más 1 año de experiencia** en asuntos reglamentarios o gestión de la calidad de productos sanitarios, o bien **4 años de experiencia** en esos ámbitos). Las **microempresas y pequeñas empresas** no están obligadas a tenerla en plantilla, pero sí a **disponer de ella de forma permanente y continua**. Garantiza, como mínimo: la conformidad de cada producto antes de liberarlo, la actualización de la documentación técnica y de la declaración UE de conformidad, el seguimiento poscomercialización y las notificaciones de vigilancia (arts. 87 a 91).
- **Productos «legacy»** (art. 120 MDR, modificado por el Reglamento (UE) 2023/607): los certificados de las Directivas siguen amparando la comercialización hasta el **31 de diciembre de 2027** (clase III y IIb implantables, con excepciones) o el **31 de diciembre de 2028** (resto de IIb, IIa y clase I estéril o con función de medición). También hasta el **31 de diciembre de 2028** los productos que eran **clase I autodeclarada** con la Directiva y que con el MDR **suben de clase** y pasan a requerir organismo notificado: el caso típico es el **software clínico** reclasificado por la regla 11.
- **EUDAMED** (art. 33 MDR): la base de datos europea de productos sanitarios. El art. 33.2 enumera **siete sistemas electrónicos** que la Comisión agrupa en **seis módulos**: registro de actores, UDI y productos (dos sistemas), organismos notificados y certificados, investigaciones clínicas, vigilancia, y vigilancia del mercado. El Reglamento 2024/1860 estableció su **despliegue gradual** (cada módulo se hace obligatorio tras auditarse y declararse funcional); la **Decisión (UE) 2025/2371** (27 de noviembre de 2025) activó los cuatro primeros módulos, **obligatorios desde el 28 de mayo de 2026**. El sistema **UDI** (identificación única de producto) permite la trazabilidad de cada producto en el mercado.

## Producto sanitario y software como producto sanitario (MDSW)

- **Definición de producto sanitario** (art. 2.1 MDR, recortada): «todo instrumento, dispositivo, equipo, **programa informático**, implante, reactivo, material u otro artículo destinado por el fabricante a ser utilizado en personas, por separado o en combinación, con alguna de las siguientes **finalidades médicas específicas**: diagnóstico, prevención, seguimiento, **predicción, pronóstico**, tratamiento o alivio de una enfermedad; diagnóstico, seguimiento, tratamiento, alivio o compensación de una lesión o discapacidad; investigación, sustitución o modificación de la anatomía o de un proceso o estado fisiológico o patológico; obtención de información mediante el examen in vitro de muestras procedentes del cuerpo humano».
- **La finalidad prevista decide**: lo determinante no es la tecnología sino la **finalidad prevista** (*intended purpose*) que el fabricante declara en la etiqueta, las instrucciones y el material promocional. El mismo algoritmo puede ser producto sanitario o no según para qué se destine.
- **MDSW** (*Medical Device Software*, guía **MDCG 2019-11 rev.1**): software destinado por el fabricante, por sí solo o en combinación, a una finalidad médica de las definiciones del MDR o del IVDR, **con independencia de si va embebido en un dispositivo físico o se comercializa aparte** (y de dónde corra: local, móvil o nube).
- **Pasos de decisión para la cualificación** (MDCG 2019-11 rev.1):
    1. ¿Es **software** según la guía (instrucciones que procesan datos de entrada y producen salidas)?
    2. ¿Es un producto del **Anexo XVI** (sin finalidad médica pero regulado) o un **accesorio** de un producto sanitario? En ese caso queda cubierto por el MDR.
    3. ¿Realiza una **acción sobre los datos** distinta del mero **almacenamiento, archivo, comunicación o búsqueda simple**?
    4. ¿Esa acción es **en beneficio de pacientes individuales** (no mera estadística de población o gestión)?
    5. ¿Encaja en la definición de finalidad médica? Entonces es **MDSW**.
- **¿MDR o IVDR?** Otros **tres pasos** de la guía deciden qué reglamento aplica al MDSW:
    1. ¿La información que proporciona entra en la definición de producto de **diagnóstico in vitro** (procede del examen in vitro de muestras del cuerpo humano)? Si no, MDR.
    2. ¿La genera **solo** a partir de datos de productos de diagnóstico in vitro? Entonces IVDR. Si combina datos in vitro con otras fuentes (imagen, constantes), paso 3.
    3. ¿Su finalidad prevista está **sustancialmente determinada** por las fuentes de datos in vitro? Si sí, IVDR; si pesan más las demás fuentes, MDR.
- **Quedan fuera** (si no tienen finalidad médica propia): la HCE y los HIS como tales, el software de gestión (citación, facturación, almacén), los visores genéricos sin función diagnóstica y las apps de bienestar o estilo de vida. La guía aplica un **enfoque modular**: en un sistema grande, solo los **módulos** con finalidad médica se someten al MDR; el resto no, pero el fabricante debe delimitarlos.
- **Ejemplos de MDSW**: ayuda al diagnóstico por imagen (CAD), cálculo de dosis de fármacos, planificación quirúrgica o de radioterapia, sistemas de soporte a la decisión clínica que recomiendan tratamiento, apps que interpretan señales fisiológicas.

## Clasificación de riesgo: clases y regla 11

El MDR clasifica los productos en cuatro clases de riesgo creciente: **I** (con las variantes **Is** estéril, **Im** con función de medición e **Ir** quirúrgico reutilizable), **IIa**, **IIb** y **III**. La clasificación se rige por el **Anexo VIII**: definiciones (duración del uso: **transitorio** menos de 60 minutos, **a corto plazo** hasta 30 días, **prolongado** más de 30 días; invasividad; producto activo) y **22 reglas** en cuatro bloques (no invasivos, reglas 1-4; invasivos, 5-8; activos, 9-13; reglas especiales, 14-22). El software es un **producto activo** y su regla específica es la **regla 11**.

- **Regla 11 del Anexo VIII (literal)**: «Los programas informáticos destinados a proporcionar información que se utiliza para tomar decisiones con fines terapéuticos o de diagnóstico se clasifican en la **clase IIa**, salvo si estas decisiones tienen un impacto que pueda causar:
    - la muerte o un deterioro irreversible del estado de salud de una persona, en cuyo caso se clasifican en la **clase III**, o
    - un deterioro grave del estado de salud de una persona o una intervención quirúrgica, en cuyo caso se clasifican en la **clase IIb**.

    Los programas informáticos destinados a la **vigilancia de procesos fisiológicos** se clasifican en la **clase IIa**, salvo si se destinan a vigilar **parámetros fisiológicos vitales**, cuando la índole de las variaciones de dichos parámetros sea tal que pudiera dar lugar a un **peligro inmediato** para el paciente, en cuyo caso se clasifican en la **clase IIb**.

    **Todos los demás programas informáticos se clasifican en la clase I.**»

- **La regla 11 en tabla**:

| Software destinado a… | Impacto de la decisión / vigilancia | Clase |
| --- | --- | --- |
| Informar decisiones diagnósticas o terapéuticas | Caso general | **IIa** |
| Informar decisiones diagnósticas o terapéuticas | Puede causar deterioro grave o intervención quirúrgica | **IIb** |
| Informar decisiones diagnósticas o terapéuticas | Puede causar la muerte o deterioro irreversible | **III** |
| Vigilar procesos fisiológicos | Caso general | **IIa** |
| Vigilar parámetros fisiológicos vitales | Variaciones con peligro inmediato para el paciente | **IIb** |
| Cualquier otro software | (resto de casos) | **I** |

- **El marco IMDRF** (Anexo III de MDCG 2019-11): para posicionar un software concreto dentro de la regla 11, la guía usa el marco del IMDRF, que cruza la **relevancia de la información** que aporta el software a la decisión sanitaria con la **gravedad de la situación** del paciente:

| Situación del paciente | Tratar o diagnosticar | Guía la gestión clínica | Solo informa la gestión clínica |
| --- | --- | --- | --- |
| **Crítica** | Clase **III** | Clase **IIb** | Clase **IIa** |
| **Grave** | Clase **IIb** | Clase **IIa** | Clase **IIa** |
| **No grave** | Clase **IIa** | Clase **IIa** | Clase **IIa** |

- **Lectura práctica**: como casi todo el software clínico «proporciona información para decisiones diagnósticas o terapéuticas», la **clase mínima habitual del MDSW es la IIa**; la clase I queda casi residual.
- **Ejemplos de clasificación** (Anexo IV de MDCG 2019-11, orientativos):

| Software (finalidad prevista) | Clase |
| --- | --- |
| Diagnóstico por análisis de imagen para decidir el tratamiento en ictus agudo | **III** |
| Vigilancia continua de procesos fisiológicos vitales en anestesia, UCI o urgencias | **IIb** |
| App que analiza el ritmo cardiaco y comunica anomalías para orientar el diagnóstico del médico | **IIb** |
| Puntuación (*scoring*) diagnóstica de la depresión a partir de síntomas introducidos | **IIb** |
| Ordenación de opciones de quimioterapia según historia, imagen y características del paciente | **IIa** |
| App de fertilidad que calcula el estado fértil con un algoritmo estadístico validado | **I** |
| App que convierte símbolos en voz para personas con trastornos de la comunicación | **I** |

- **Reglas complementarias**: la regla de implementación **3.3 del Anexo VIII MDR** (idéntica a la **1.4 del Anexo VIII IVDR**) dispone que el software que **sirva para manejar un producto o influya en su utilización** se clasifica en la **misma clase que el producto**, y que si el software es **independiente** de cualquier otro producto «será clasificado por sí mismo». En el IVDR, ese software independiente se clasifica aplicando sus propias reglas 1 a 7 según la finalidad prevista (clases **A a D**).

## Evaluación de la conformidad y marcado CE

- **Requisitos generales de seguridad y funcionamiento** (Anexo I): el software debe diseñarse «con arreglo al estado de la técnica», atendiendo al **ciclo de vida de desarrollo**, la **gestión de riesgos**, la **verificación y validación** y la **seguridad informática** (puntos 17.1 a 17.4: software embebido y programas informáticos por sí mismos; también fija requisitos para el software en plataformas móviles, y obliga al fabricante a declarar los **requisitos mínimos** de hardware, redes y medidas de seguridad TI para ejecutar el software según lo previsto).
- **Normas armonizadas y guías habituales para software**: **EN 62304** (procesos del ciclo de vida del software de dispositivos médicos), **EN ISO 14971:2019** (gestión de riesgos), **IEC 82304-1** (seguridad del *health software* de propósito general) y la guía **MDCG 2019-16 rev.1** (ciberseguridad de productos sanitarios, julio de 2020).
- **Documentación técnica** (Anexos II y III): descripción y especificaciones del producto (incluido el UDI-DI básico), información de diseño y fabricación, análisis beneficio-riesgo y gestión de riesgos, verificación y validación (con los datos específicos del software: entorno, versiones, validación en condiciones reales de uso) y, en el Anexo III, la documentación del seguimiento poscomercialización.
- **Rutas de evaluación de la conformidad**:
    - **Clase I**: autoevaluación y **declaración UE de conformidad** del fabricante, sin organismo notificado (salvo Is, Im e Ir, donde el organismo interviene solo en los aspectos de esterilidad, metrología o reutilización).
    - **Clases IIa, IIb y III**: intervención obligatoria de un **organismo notificado** (entidad independiente designada por un Estado miembro), normalmente por la vía del **Anexo IX** (sistema de gestión de la calidad + evaluación de la documentación técnica) o, alternativamente, Anexos X y XI.
    - **Clase III y ciertos IIb**: escrutinio reforzado (consulta a **paneles de expertos** europeos sobre la evaluación clínica).
- **Declaración UE de conformidad y marcado CE** (arts. 19 y 20): superada la evaluación, el fabricante emite la declaración (asumiendo la responsabilidad del cumplimiento) y coloca el **marcado CE de conformidad** de forma visible, legible e indeleble; cuando interviene organismo notificado, junto al CE figura su **número de identificación**.
- **UDI del software** (art. 27 y Anexo VI, parte C): el UDI se asigna **al nivel de sistema** del programa. Se exige un **nuevo UDI-DI** ante cambios que modifiquen el **funcionamiento original**, la **seguridad o el uso previsto** o la **interpretación de los datos** (algoritmos nuevos o modificados, estructura de base de datos, plataforma, arquitectura, interfaces de usuario, canales de interoperabilidad); las **revisiones menores** (corrección de errores, parches de seguridad, mejoras de manejabilidad) solo requieren nuevo **UDI-PI**.
- **Evaluación clínica** (art. 61 y Anexo XIV): todo producto exige **evidencia clínica** proporcional a su riesgo, mantenida al día con el **seguimiento clínico poscomercialización**; para software, la guía MDCG 2020-1 detalla cómo demostrar la asociación entre la salida del algoritmo y la situación clínica.
- **Seguimiento poscomercialización** (arts. 83-86): el fabricante mantiene un **plan de seguimiento poscomercialización** (art. 84) integrado en su sistema de calidad. Los fabricantes de **clase I** elaboran un informe de seguimiento (art. 85); los de **IIa, IIb y III**, el **informe periódico de seguridad actualizado (PSUR)** del art. 86, que se actualiza como mínimo **cada dos años** en clase IIa y **una vez al año** en IIb y III, y forma parte de la documentación técnica.
- **Vigilancia** (art. 87): el fabricante notifica los **incidentes graves** a más tardar **15 días** después de tener conocimiento; **2 días** si hay **amenaza grave para la salud pública**; **10 días** en caso de **muerte o deterioro grave imprevisto** del estado de salud. Las acciones correctivas de seguridad se comunican antes de emprenderse, salvo urgencia. Todo se tramita por el módulo de vigilancia de EUDAMED.

## Software fabricado y usado en el propio centro sanitario (exención in-house)

Los servicios de salud desarrollan internamente software clínico (y cada vez más algoritmos de IA). El MDR prevé para ese caso una vía específica que evita el marcado CE completo, con condiciones estrictas.

- **Exención de los centros sanitarios (art. 5.5 MDR)**: los requisitos del reglamento, **salvo los requisitos generales de seguridad y funcionamiento del Anexo I**, no se aplican a los productos **fabricados y utilizados exclusivamente en centros sanitarios** establecidos en la Unión, si se cumplen **todas** estas condiciones:
    - que los productos **no se cedan a otra persona jurídica**;
    - que la fabricación y el uso se hagan bajo un **sistema de gestión de la calidad apropiado**;
    - que el centro **justifique en su documentación** que las necesidades específicas del grupo de pacientes destinatario no pueden satisfacerse, o no con el nivel de funcionamiento adecuado, mediante un **producto equivalente comercializado**;
    - que facilite a la autoridad competente, previa solicitud, información sobre el uso, con justificación de la fabricación, la modificación y el uso;
    - que formule una **declaración pública** con el nombre y dirección del centro, la identificación de los productos y la conformidad con el Anexo I (justificando motivadamente los requisitos que no se satisfagan plenamente);
    - que elabore documentación del proceso de producción, el diseño y los datos de funcionamiento (incluida la finalidad prevista) suficiente para que la autoridad evalúe el cumplimiento del Anexo I;
    - que fabrique conforme a esa documentación, y que **revise la experiencia clínica adquirida** y adopte las acciones correctivas necesarias.
    - La exención **no se aplica** a los productos fabricados «a escala industrial».
- **Desarrollo español (art. 9 RD 192/2023)**: en España solo pueden acogerse los **hospitales** (definidos según el RD 1277/2003), que **no pueden fabricar por esta vía productos de clase IIb, clase III ni implantables**, ni **subcontratar** la fabricación, ni **vender o entregar** el producto a terceros. Deben designar una **persona responsable** de la actividad y presentar a la **AEMPS** una **comunicación previa de inicio de actividad** (con la persona responsable, la declaración pública del art. 5.5 y la documentación justificativa); cualquier modificación o el cese se comunican también.
- **Lectura para el software**: un hospital puede desarrollar y usar in-house software de **clase I o IIa** (la mayoría del MDSW) cumpliendo el art. 5.5. Si por la regla 11 el software cae en **IIb o III** (decisiones con riesgo de deterioro grave o muerte), la vía in-house está **vedada en España**: el producto exige el circuito completo de fabricante con licencia, organismo notificado y marcado CE.

## IA como producto sanitario: interacción MDR-AI Act

La IA sanitaria queda sujeta a **doble regulación**: el MDR/IVDR como producto sanitario y el **Reglamento (UE) 2024/1689 (AI Act, remisión al tema [35](35-etica-regulacion-inteligencia-artificial.md))** como sistema de IA. Las guías **MDCG 2025-6 y AIB 2025-1** (junio de 2025, primera guía conjunta del MDCG y la Oficina de IA) aclaran el encaje del **MDAI** (*medical device AI*).

- **Calendario del AI Act**: en vigor desde el **1 de agosto de 2024** (DOUE de 12 de julio); aplicación general desde el **2 de agosto de 2026**; las obligaciones para los sistemas de alto riesgo del art. 6.1 (productos armonizados del Anexo I, entre ellos MDR e IVDR) son aplicables **desde el 2 de agosto de 2027** (art. 113).
- **Cuándo es de alto riesgo** (art. 6.1 del AI Act): un sistema de IA es de **alto riesgo** si cumple **las dos condiciones**: (1) es un **componente de seguridad** de un producto cubierto por la legislación armonizada del Anexo I del AI Act (que incluye MDR e IVDR) **o es él mismo ese producto**, y (2) ese producto está sujeto a **evaluación de la conformidad por un organismo notificado**.
- **Consecuencia práctica**: el MDSW con IA de **clase IIa o superior** (que siempre pasa por organismo notificado) **es sistema de IA de alto riesgo**; también las variantes **Is, Im e Ir** de la clase I, porque en ellas interviene organismo notificado. El de **clase I** simple (autoevaluado) **no** lo es por esta vía, y tampoco el **software in-house del art. 5.5** (sin organismo notificado; MDCG 2025-6, Q35), aunque a este le siguen aplicando otras obligaciones del AI Act, como las **prácticas prohibidas**. Por la regla 11, casi toda la IA clínica con finalidad diagnóstica o terapéutica acaba siendo de alto riesgo.
- **La clase no cambia**: el AI Act **no altera** la clase de riesgo del MDR/IVDR; es la clasificación MDR/IVDR la que determina si el sistema de IA es de alto riesgo, no al revés (MDCG 2025-6, Q4).
- **Doble cumplimiento integrado**: los requisitos del AI Act para sistemas de alto riesgo (sección 2, arts. 8 a 15) se verifican **dentro de la misma evaluación de conformidad** del MDR/IVDR (art. 43.3 AI Act), para no duplicar procedimientos, y cabe una **única declaración UE de conformidad** que cubra ambos reglamentos (art. 47.3 AI Act). Los requisitos son: **sistema de gestión de riesgos** (art. 9), **datos y gobernanza de datos** (art. 10: conjuntos de entrenamiento, validación y prueba pertinentes, representativos y en lo posible completos y sin errores), **documentación técnica** (art. 11), **conservación de registros** (art. 12, generación automática de *logs*), **transparencia e información al responsable del despliegue** (art. 13), **supervisión humana** (art. 14) y **precisión, solidez y ciberseguridad** (art. 15).
- **IA que sigue aprendiendo**: los **cambios predeterminados** por el fabricante en el plan evaluado en la evaluación de conformidad inicial (documentación técnica del Anexo IV AI Act) **no constituyen «modificación sustancial»** y no exigen nueva evaluación (art. 43.4 AI Act; MDCG 2025-6, Q30); los cambios fuera de ese plan sí pueden exigirla.
- **El centro sanitario como responsable del despliegue** (*deployer*, art. 26 AI Act): cuando la administración sanitaria **compra y usa** IA de alto riesgo (sin fabricarla), sus obligaciones principales son: utilizarla conforme a las **instrucciones de uso**; encomendar la **supervisión humana** a personas con la competencia, formación y autoridad necesarias; asegurar que los **datos de entrada** sean pertinentes y suficientemente representativos (en la medida en que los controle); **vigilar el funcionamiento**, y si hay riesgo suspender el uso e informar al proveedor y a la autoridad de vigilancia, notificando los **incidentes graves**; conservar los **archivos de registro** generados automáticamente **al menos seis meses**; siendo autoridad pública, comprobar antes de usarlo que el sistema está **registrado en la base de datos de la UE** (si no lo está, no puede usarlo); informar a los **trabajadores afectados** antes de usarlo en el lugar de trabajo; y apoyarse en la información del proveedor para la **evaluación de impacto en protección de datos** (art. 35 del RGPD).
- **Para el examen**: la cadena completa es finalidad prevista → cualificación como MDSW (MDCG 2019-11) → clase de riesgo (regla 11) → ruta de conformidad (con o sin organismo notificado; o vía in-house del art. 5.5) → si lleva IA y pasa por organismo notificado, además, alto riesgo del AI Act (requisitos integrados del fabricante y obligaciones de *deployer* para quien la usa).

## Fuentes {.unnumbered .unlisted}

- Reglamento (UE) 2017/745 (MDR), texto consolidado a 9 de julio de 2024 (CELEX 02017R0745; las versiones-fecha de 10 de enero de 2025 y 1 de enero de 2026 listadas en EUR-Lex corresponden a la aplicación diferida del Reglamento (UE) 2024/1860). Modificaciones posteriores verificadas online en julio de 2026: Reglamentos Delegados (UE) 2026/1359 y 2026/1451 (marzo de 2026, listas de tecnologías consolidadas exentas de investigación clínica o de evaluación producto a producto en implantables y clase III), sin efecto sobre lo tratado en este tema.
- Reglamento (UE) 2017/746 (IVDR), texto consolidado a 9 de julio de 2024 (la versión EUR-Lex de 10 de enero de 2025 corresponde a la aplicación diferida del Reglamento (UE) 2024/1860; verificado online en julio de 2026).
- Real Decreto 192/2023, de 21 de marzo (texto consolidado, sin modificaciones; verificado online en julio de 2026).
- MDCG 2019-11 rev.1, «Guidance on qualification and classification of software» (junio de 2025).
- MDCG 2025-6 / AIB 2025-1, «Interplay between the MDR/IVDR and the AI Act» (junio de 2025).
- MDCG 2020-1 (evaluación clínica de software) y MDCG 2019-16 rev.1 (ciberseguridad de productos sanitarios, julio de 2020).
- Reglamento (UE) 2024/1689 (AI Act), DOUE de 12 de julio de 2024 (PDF local; arts. 6, 26, 43, 47 y 113 contrastados).
- Decisión (UE) 2025/2371 (EUDAMED: cuatro primeros módulos obligatorios desde el 28 de mayo de 2026; verificada online en julio de 2026).
- EN 62304, EN ISO 14971:2019 e IEC 82304-1, citadas por edición.
