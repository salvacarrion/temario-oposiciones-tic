# Productos sanitarios: reglamentos MDR e IVDR y software sanitario

Buena parte del software clínico (ayuda al diagnóstico, cálculo de dosis, algoritmos de IA sobre imagen) es, legalmente, un **producto sanitario**: necesita clasificación de riesgo, evaluación de la conformidad y **marcado CE** antes de usarse con pacientes. Este tema recorre el marco regulador europeo (MDR e IVDR) y español (RD 192/2023), la cualificación y clasificación del software y el encaje de la inteligencia artificial.

## Marco normativo: MDR, IVDR y RD 192/2023

- **Reglamento (UE) 2017/745 (MDR)**, de 5 de abril de 2017, **sobre los productos sanitarios**: deroga las Directivas 90/385/CEE (implantes activos) y 93/42/CEE (productos sanitarios). Aplicable desde el **26 de mayo de 2021** (aplazado un año por el Reglamento (UE) 2020/561 a causa de la pandemia).

**Texto consolidado a 9 de julio de 2024** (incluye el Reglamento (UE) 2024/1860; EUR-Lex lista versiones-fecha de 10 de enero de 2025 y 1 de enero de 2026 que corresponden a la aplicación diferida de disposiciones de ese mismo reglamento).

- **Reglamento (UE) 2017/746 (IVDR)**, sobre los **productos sanitarios para diagnóstico in vitro** (analizadores, reactivos, pruebas genéticas y su software): deroga la Directiva 98/79/CE y es aplicable desde el **26 de mayo de 2022**. Clasifica en cuatro clases de riesgo propias (**A, B, C y D**, de menor a mayor).

**Texto consolidado a 9 de julio de 2024.**

- **Real Decreto 192/2023, de 21 de marzo, por el que se regulan los productos sanitarios**: adapta el ordenamiento español al MDR: régimen de las **instalaciones** (licencia previa de funcionamiento), distribución y venta, publicidad, y actuaciones de la autoridad competente.

**Texto consolidado: sin modificaciones.**

- **La AEMPS** (Agencia Española de Medicamentos y Productos Sanitarios) es la **autoridad competente** española: designa y supervisa, registra comercializaciones, tramita la vigilancia y puede restringir o retirar productos del mercado.
- **Productos «legacy»** (art. 120 MDR, modificado por el Reglamento (UE) 2023/607): los certificados de las Directivas siguen amparando la comercialización hasta el **31 de diciembre de 2027** (clase III y IIb implantables, con excepciones) o el **31 de diciembre de 2028** (resto de IIb, IIa y clase I estéril o con función de medición). También hasta el **31 de diciembre de 2028** los productos que eran **clase I autodeclarada** con la Directiva y que con el MDR **suben de clase** y pasan a requerir organismo notificado: el caso típico es el **software clínico** reclasificado por la regla 11.
- **EUDAMED** (art. 33 MDR): la base de datos europea de productos sanitarios, con **seis módulos**: registro de actores, UDI y productos, organismos notificados y certificados, investigaciones clínicas, vigilancia, y vigilancia del mercado. El Reglamento 2024/1860 estableció su **despliegue gradual** (cada módulo se hace obligatorio tras auditarse y declararse funcional); la **Decisión (UE) 2025/2371** (27 de noviembre de 2025) activó los cuatro primeros módulos, **obligatorios desde el 28 de mayo de 2026**. El sistema **UDI** (identificación única de producto) permite la trazabilidad de cada producto en el mercado.

## Producto sanitario y software como producto sanitario (MDSW)

- **Definición de producto sanitario** (art. 2.1 MDR, recortada): «todo instrumento, dispositivo, equipo, **programa informático**, implante, reactivo, material u otro artículo destinado por el fabricante a ser utilizado en personas, por separado o en combinación, con alguna de las siguientes **finalidades médicas específicas**: diagnóstico, prevención, seguimiento, **predicción, pronóstico**, tratamiento o alivio de una enfermedad; diagnóstico, seguimiento, tratamiento, alivio o compensación de una lesión o discapacidad; investigación, sustitución o modificación de la anatomía o de un proceso o estado fisiológico o patológico; obtención de información mediante el examen in vitro de muestras procedentes del cuerpo humano».
- **La finalidad prevista decide**: lo determinante no es la tecnología sino la **finalidad prevista** (*intended purpose*) que el fabricante declara en la etiqueta, las instrucciones y el material promocional. El mismo algoritmo puede ser producto sanitario o no según para qué se destine.
- **MDSW** (*Medical Device Software*, guía **MDCG 2019-11 rev.1**): software destinado por el fabricante, por sí solo o en combinación, a una finalidad médica de las definiciones del MDR o del IVDR, **con independencia de si va embebido en un dispositivo físico o se comercializa aparte** (y de dónde corra: local, móvil o nube).
- **Pasos de decisión para la cualificación** (MDCG 2019-11 rev.1):
    1. ¿Es **software** según la guía (instrucciones que procesan datos de entrada y producen salidas)?
    2. ¿Es un producto del **Anexo XVI** (sin finalidad médica pero regulado) o un **accesorio** de un producto sanitario? En ese caso queda cubierto por el MDR.
    3. ¿Realiza una **acción sobre los datos** distinta del mero **almacenamiento, archivo, comunicación o búsqueda simple**?
    4. ¿Esa acción es **en beneficio de pacientes individuales** (no mera estadística de población o gestión)?
    5. ¿Encaja en la definición de finalidad médica? Entonces es **MDSW** (y otros tres pasos deciden si le aplica el MDR o el IVDR, según si la información procede de pruebas in vitro).
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

- **Lectura práctica**: como casi todo el software clínico «proporciona información para decisiones diagnósticas o terapéuticas», la **clase mínima habitual del MDSW es la IIa**; la clase I queda casi residual (la guía MDCG 2019-11 acompaña la regla con el marco del IMDRF que cruza la **relevancia de la información**, tratar/diagnosticar, guiar la gestión clínica o solo informar, con la **gravedad de la situación** del paciente). Ejemplos orientativos: un software de triaje de urgencias o de cálculo de dosis suele caer en **IIb**; la ayuda al diagnóstico en patologías con riesgo vital, en **IIb o III**; un software que planifica citas de rehabilitación, en clase I o fuera del MDR.
- **Reglas complementarias**: si el software **hace funcionar un producto** o influye en su uso, se clasifica en la misma clase que el producto (regla de implementación 3.3 del Anexo VIII); en el IVDR el software sigue la clase del producto in vitro al que sirve (clases A a D).

## Evaluación de la conformidad y marcado CE

- **Requisitos generales de seguridad y funcionamiento** (Anexo I): el software debe diseñarse «con arreglo al estado de la técnica», atendiendo al **ciclo de vida de desarrollo**, la **gestión de riesgos**, la **verificación y validación** y la **seguridad informática** (puntos 17.1 a 17.4: software embebido y programas informáticos por sí mismos; también fija requisitos para el software en plataformas móviles y la interoperabilidad).
- **Normas armonizadas habituales para software**: **EN 62304** (procesos del ciclo de vida del software de dispositivos médicos), **EN ISO 14971:2019** (gestión de riesgos) e **IEC 82304-1** (seguridad del *health software* de propósito general).
- **Rutas de evaluación de la conformidad**:
    - **Clase I**: autoevaluación y **declaración UE de conformidad** del fabricante, sin organismo notificado (salvo Is, Im e Ir, donde el organismo interviene solo en los aspectos de esterilidad, metrología o reutilización).
    - **Clases IIa, IIb y III**: intervención obligatoria de un **organismo notificado** (entidad independiente designada por un Estado miembro), normalmente por la vía del **Anexo IX** (sistema de gestión de la calidad + evaluación de la documentación técnica) o, alternativamente, Anexos X y XI.
    - **Clase III y ciertos IIb**: escrutinio reforzado (consulta a **paneles de expertos** europeos sobre la evaluación clínica).
- **Evaluación clínica** (art. 61 y Anexo XIV): todo producto exige **evidencia clínica** proporcional a su riesgo, mantenida al día con el **seguimiento clínico poscomercialización**; para software, la guía MDCG 2020-1 detalla cómo demostrar la asociación entre la salida del algoritmo y la situación clínica.
- **Tras el marcado CE**: el fabricante mantiene un sistema de **seguimiento poscomercialización** (plan y, para IIa o superior, **informe periódico de seguridad actualizado, PSUR**), registra el producto y su **UDI** en EUDAMED y notifica los **incidentes graves** y las acciones correctivas de seguridad a través del módulo de vigilancia en los plazos tasados del MDR.

## IA como producto sanitario: interacción MDR-AI Act

La IA sanitaria queda sujeta a **doble regulación**: el MDR/IVDR como producto sanitario y el **Reglamento (UE) 2024/1689 (AI Act, remisión al tema 35)** como sistema de IA. Las guías **MDCG 2025-6 y AIB 2025-1** (junio de 2025, primera guía conjunta del MDCG y la Oficina de IA) aclaran el encaje del **MDAI** (*medical device AI*):

- **Cuándo es de alto riesgo** (art. 6.1 del AI Act): un sistema de IA es de **alto riesgo** si cumple **las dos condiciones**: (1) es un **componente de seguridad** de un producto cubierto por la legislación armonizada del Anexo I del AI Act (que incluye MDR e IVDR) **o es él mismo ese producto**, y (2) ese producto está sujeto a **evaluación de la conformidad por un organismo notificado**.
- **Consecuencia práctica**: el MDSW con IA de **clase IIa o superior** (que siempre pasa por organismo notificado) **es sistema de IA de alto riesgo**; el de **clase I** (autoevaluado, sin organismo notificado) **no** lo es por esta vía. Por la regla 11, casi toda la IA clínica con finalidad diagnóstica o terapéutica acaba siendo de alto riesgo.
- **Doble cumplimiento integrado**: los requisitos del AI Act para alto riesgo (gobernanza de datos de entrenamiento, documentación técnica, transparencia, **supervisión humana**, precisión, robustez y ciberseguridad) se verifican **dentro de la misma evaluación de conformidad** del MDR/IVDR, para no duplicar procedimientos; las obligaciones para estos sistemas de alto riesgo del art. 6.1 son aplicables **desde el 2 de agosto de 2027**.
- **Para el examen**: la cadena completa es finalidad prevista → cualificación como MDSW (MDCG 2019-11) → clase de riesgo (regla 11) → ruta de conformidad (con o sin organismo notificado) → si lleva IA y pasa por organismo notificado, además, alto riesgo del AI Act.

## Fuentes {.unnumbered .unlisted}

- Reglamento (UE) 2017/745 (MDR), texto consolidado a 9 de julio de 2024 (CELEX 02017R0745; las versiones-fecha de 10 de enero de 2025 y 1 de enero de 2026 listadas en EUR-Lex corresponden a la aplicación diferida del Reglamento (UE) 2024/1860, verificado online en julio de 2026).
- Reglamento (UE) 2017/746 (IVDR), texto consolidado a 9 de julio de 2024.
- Real Decreto 192/2023, de 21 de marzo (texto consolidado, sin modificaciones).
- MDCG 2019-11 rev.1, «Guidance on qualification and classification of software» (junio de 2025).
- MDCG 2025-6 / AIB 2025-1, «Interplay between the MDR/IVDR and the AI Act» (junio de 2025).
- Decisión (UE) 2025/2371 (EUDAMED: cuatro primeros módulos obligatorios desde el 28 de mayo de 2026; verificada online en julio de 2026).
- Reglamento (UE) 2024/1689 (AI Act), DOUE local (fecha de aplicación del art. 6.1 verificada); EN 62304, EN ISO 14971:2019 e IEC 82304-1 citadas por edición.
