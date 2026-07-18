# Integración de sistemas sanitarios y mensajería HL7

Un hospital moderno ejecuta decenas de aplicaciones que necesitan compartir datos en tiempo real: el sistema de información hospitalario (HIS), la historia clínica electrónica, el laboratorio (LIS), la radiología (RIS/PACS), la farmacia, la citación o la facturación. La integración de sistemas es la disciplina que hace que ese ecosistema funcione como un todo coherente, y la mensajería HL7 es su estándar de intercambio dominante.

## La interoperabilidad en sanidad

La interoperabilidad es la capacidad de dos o más sistemas de **intercambiar información y de utilizar la información intercambiada**. En sanidad se analiza por niveles (modelo de HIMSS, alineado con el Esquema Nacional de Interoperabilidad y el Marco Europeo de Interoperabilidad, remisión al tema [62](62-esquema-nacional-de-interoperabilidad.md)):

| Nivel | Qué garantiza | Ejemplo sanitario |
| --- | --- | --- |
| **Técnico (fundacional)** | La conexión y el transporte de datos entre sistemas | Red, TCP/IP, MLLP, HTTPS |
| **Sintáctico (estructural)** | Formato y estructura comunes del mensaje | Mensaje HL7 v2, documento XML, JSON |
| **Semántico** | Que el receptor interprete el dato con el mismo significado | Codificar el diagnóstico en SNOMED CT o CIE-10-ES (tema [92](92-normalizacion-en-informatica-sanitaria.md)) |
| **Organizativo** | Procesos, acuerdos y marco legal compartidos | Consentimientos, convenios entre servicios de salud, HCDSNS (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)) |

- **Particularidades del dominio sanitario**: gran heterogeneidad de aplicaciones y proveedores, datos de **categoría especial** (art. 9 RGPD, remisión al tema [53](53-proteccion-de-datos-personales.md)), necesidad de disponibilidad continua (24x7) y una semántica clínica compleja que exige terminologías controladas.
- **Beneficios**: continuidad asistencial (el dato sigue al paciente), eliminación de pruebas duplicadas, seguridad del paciente (menos transcripciones manuales) y explotación secundaria de los datos (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)).

## Integración de aplicaciones sanitarias: patrones y motores de integración

Integrar aplicaciones dos a dos no escala: con *n* sistemas conectados punto a punto se necesitan hasta **n(n-1)/2** interfaces distintas, cada una con su formato, su ciclo de vida y su mantenimiento. La respuesta arquitectónica es centralizar el intercambio.

- **Integración punto a punto**: conexiones directas entre pares de aplicaciones. Simple al principio, inmanejable al crecer («espagueti de interfaces»).
- **Hub-and-spoke / bus de integración (ESB)**: todas las aplicaciones se conectan a un nodo central que enruta y transforma los mensajes. Cada sistema mantiene **una sola interfaz** con el bus.
- **Motor de integración** (*interface engine*): la pieza software que materializa el bus en sanidad. Funciones típicas:
    - **Conectividad**: adaptadores para MLLP, ficheros, bases de datos, servicios web SOAP/REST, colas de mensajes.
    - **Transformación**: mapeo entre formatos y versiones (por ejemplo, HL7 v2.3 a v2.5, o HL7 v2 a FHIR).
    - **Enrutamiento y filtrado**: decidir a qué sistemas se reenvía cada mensaje según su tipo o contenido.
    - **Garantía de entrega**: colas persistentes, reintentos, gestión de acuses de recibo (ACK).
    - **Monitorización y trazabilidad**: registro de todos los mensajes, alertas ante errores o colas paradas.
- **Productos habituales**: **Mirth Connect** (código abierto, muy extendido), **InterSystems** (Ensemble/IRIS for Health), **Rhapsody** e **Infor Cloverleaf**.

## HL7 v2.x: la mensajería clínica

**HL7 International** (Health Level Seven, fundada en **1987**, organización de desarrollo de estándares acreditada por ANSI) toma su nombre del **nivel 7 (aplicación) del modelo OSI**. Su familia v2.x, publicada desde 1989, es el estándar de mensajería sanitaria **más implantado del mundo** (implantaciones en más de 35 países); la última versión publicada es la **v2.9.1** (la v2.9 es de 2019), aunque en producción dominan las versiones 2.3 a 2.5.1. Las versiones 2.x son **retrocompatibles** entre sí.

- **Modelo de intercambio**: mensajería asíncrona dirigida por **eventos disparadores** (*trigger events*): cuando en un sistema ocurre un hecho (un ingreso, un resultado validado), se emite un mensaje a los sistemas interesados, que responden con un acuse **ACK**.
- **Estructura jerárquica del mensaje**: mensaje → **segmentos** (una línea, identificada por 3 letras) → **campos** (separados por `|`) → **componentes** (separados por `^`). Los delimitadores estándar son `| ^ ~ \ &`.
- **Segmentos más comunes**:

| Segmento | Contenido |
| --- | --- |
| **MSH** | Cabecera del mensaje: emisor, receptor, fecha, tipo, versión |
| **EVN** | Tipo de evento disparador |
| **PID** | Identificación del paciente |
| **PV1** | Datos de la visita/episodio (servicio, cama, médico) |
| **ORC/OBR** | Petición (orden) de prueba o servicio |
| **OBX** | Resultado u observación (una por segmento) |
| **NTE** | Notas y comentarios |

- **Tipos de mensaje y eventos**: el tipo se indica como `TIPO^EVENTO` en MSH-9. Los más usados: **ADT** (movimientos de pacientes: A01 ingreso, A02 traslado, A03 alta, A08 actualización de datos), **ORM/OMG** (peticiones), **ORU** (resultados, por ejemplo de laboratorio), **SIU** (citas y agendas) y **MDM** (documentos).

Ejemplo de mensaje ADT^A01 (ingreso de un paciente), simplificado:

```text
MSH|^~\&|HIS|HOSP_LA_FE|LAB|HOSP_LA_FE|20260716123000||ADT^A01|000123|P|2.5.1
EVN|A01|20260716123000
PID|1||12345678^^^SIP||García López^Ana||19800413|F|||C/ Mayor 1^^Valencia
PV1|1|I|MI^301^A|||||1122^Pérez^Juan|MED
```

- **Lectura del ejemplo**: el HIS comunica al laboratorio un ingreso (`ADT^A01`) en la versión **2.5.1**; el PID identifica a la paciente por su número **SIP** y el PV1 la sitúa ingresada (`I`) en la cama A de la habitación 301 de Medicina Interna.
- **Transporte**: el protocolo habitual es **MLLP** (*Minimal Lower Layer Protocol*): el mensaje viaja sobre una conexión TCP delimitado por caracteres de control, normalmente a través del motor de integración.
- **Limitaciones de v2**: semántica débil (muchos campos opcionales y de texto libre), variabilidad entre implantaciones (cada hospital «habla su dialecto» de HL7) y ausencia de un modelo de información formal. Estas carencias motivaron HL7 v3.

## HL7 v3 y el modelo RIM

HL7 v3 (edición normativa inicial en **2005**) replanteó la mensajería desde cero con una metodología dirigida por modelos: todos los mensajes derivan de un modelo de información único, el **RIM** (*Reference Information Model*), y se serializan en **XML**.

- **El RIM**: modelo orientado a objetos con **seis clases nucleares**: tres de contenido, **Act** (todo lo que ocurre: una observación, una prescripción), **Entity** (personas, organizaciones, lugares, cosas) y **Role** (el papel que juega una entidad: paciente, profesional), y tres de enlace, **Participation** (cómo interviene un rol en un acto), **ActRelationship** (relaciones entre actos) y **RoleLink** (relaciones entre roles).
- **Mensajería v3**: los mensajes se derivan del RIM mediante refinamientos sucesivos (D-MIM, R-MIM, HMD) y se agrupan en dominios (administración de pacientes, laboratorio, farmacia).
- **Resultado en la práctica**: la mensajería v3 tuvo una **adopción muy limitada** (complejidad alta, coste de implantación, ecosistema v2 ya consolidado). Su producto derivado de éxito es el estándar de documentos clínicos **CDA**, basado en el RIM, que se estudia en el tema [91](91-estandares-de-interoperabilidad-de-la-hce.md) junto con FHIR, el estándar moderno que recupera la sencillez de v2 con tecnologías web.

| Aspecto | HL7 v2.x | HL7 v3 |
| --- | --- | --- |
| Año | Desde 1989 (última: **2.9.1**) | Edición normativa **2005** |
| Paradigma | Mensajería por eventos, sintaxis propia | Dirigido por modelos (**RIM**), XML |
| Semántica | Débil, negociada por implantación | Formal, vocabularios controlados |
| Adopción | Dominante en hospitales | Muy limitada (sobrevive vía CDA) |
| Coste de implantación | Bajo | Alto |

## Supuesto práctico: integración del laboratorio mediante mensajería HL7

**Enunciado**: un hospital sustituye su sistema de laboratorio (**LIS**). El nuevo LIS debe recibir del **HIS** los movimientos de pacientes, recibir de la historia clínica electrónica (HCE) las peticiones de analítica y devolver los resultados validados, todo a través del **motor de integración** corporativo con mensajería **HL7 v2.5.1**. Durante las pruebas se captura este mensaje emitido por el LIS:

```text
MSH|^~\&|LIS|HOSP_LA_FE|HIS|HOSP_LA_FE|20260718083000||ORU^R01|000456|P|2.5.1
PID|1||12345678^^^SIP||García López^Ana||19800413|F
PV1|1|I|MI^301^A|||||1122^Pérez^Juan|MED
OBR|1|HCE-9871|LAB-4432|2345-7^Glucosa en suero^LN|||20260718073000
OBX|1|NM|2345-7^Glucosa^LN||142|mg/dL|70-110|H|||F
NTE|1||Extracción en ayunas
```

**Se pide**:

- a) Interpretar el mensaje capturado.
- b) Definir los flujos de mensajería del circuito petición-resultado.
- c) Diseñar la integración en el motor.
- d) Señalar los aspectos semánticos y de protección de datos.

**Resolución**:

**a) Interpretación del mensaje**

- **MSH**: el LIS envía al HIS del centro HOSP_LA_FE, el 18-jul-2026 a las 08:30, un mensaje **ORU^R01** (resultado de observación), con id de control 000456, en producción (**P**) y versión **2.5.1**.
- **PID**: paciente Ana García López, nacida el 13-abr-1980, sexo F, identificada por su número **SIP** 12345678.
- **PV1**: ingresada (**I**) en Medicina Interna, habitación 301, cama A; médico responsable 1122 (Pérez, Juan).
- **OBR**: la petición está identificada por el peticionario (*placer*) como **HCE-9871** y por el laboratorio (*filler*) como **LAB-4432**; la prueba «glucosa en suero» va codificada en **LOINC** (`2345-7`, sistema `LN`); la muestra se extrajo a las 07:30.
- **OBX**: un único resultado **numérico (NM)**: **142 mg/dL**, rango de referencia **70-110**, marcado **H** (alto) y en estado **F** (final, validado; sería P si fuera preliminar y C si corrigiera uno anterior).
- **NTE**: nota de texto libre («Extracción en ayunas»).

**b) Flujos de mensajería**

| Flujo | Mensajes HL7 | Sentido |
| --- | --- | --- |
| Sincronización de pacientes y episodios | **ADT**: A01 ingreso, A02 traslado, A03 alta, A08 actualización, **A40 fusión de pacientes** | HIS → LIS |
| Petición de analítica | **ORM^O01** (u OML en perfiles más recientes) | HCE → LIS |
| Respuesta y estado de la petición | ORR, ACK | LIS → HCE |
| Resultados (preliminares, finales y correcciones) | **ORU^R01** | LIS → HCE y HIS |
| Citas de extracción (si aplica) | SIU | Citación → LIS |

Todos los intercambios se confirman con **ACK**. El evento **A40** (fusión de pacientes duplicados) es crítico: si el LIS no lo procesa, quedan resultados colgados de historias duplicadas.

**c) Diseño en el motor de integración**

- **Un canal por flujo** (ADT, peticiones, resultados): entrada y salida por **MLLP** sobre TCP contra cada sistema, de modo que LIS, HIS y HCE mantienen **una única interfaz** con el bus en lugar de integraciones punto a punto.
- **Transformación**: el mapeo entre «dialectos» (versiones 2.3 a 2.5.1, tablas de códigos de servicios y unidades) se hace en el motor, no en las aplicaciones.
- **Enrutamiento**: por tipo y evento (campo MSH-9) y por contenido (por ejemplo, reenviar al LIS solo los ADT de hospitalización).
- **Garantía de entrega**: colas persistentes con reintentos, gestión de los ACK, alertas por cola detenida o tasa anómala de errores, y **trazabilidad** completa de mensajes para auditoría y reenvío.
- **Implantación**: pruebas en preproducción con juegos de mensajes reales **anonimizados**, prueba de carga (pico matinal de extracciones), arranque con plan de contingencia (circuito manual) y marcha atrás definida.

**d) Semántica y protección de datos**

- **Semántica**: catálogo maestro de pruebas codificado en **LOINC** y unidades normalizadas (**UCUM**); diagnósticos en SNOMED CT o CIE-10-ES (tema [92](92-normalizacion-en-informatica-sanitaria.md)). Sin acuerdo semántico la integración sintáctica «funciona», pero los datos no son comparables ni explotables.
- **Protección de datos**: datos de salud, de **categoría especial** (art. 9 RGPD, tema [53](53-proteccion-de-datos-personales.md)): transporte cifrado (MLLP sobre TLS o red segregada), acceso restringido al motor, registro de actividad, minimización de campos y datos anonimizados en los entornos de prueba.
- **Disponibilidad**: el bus es un punto único de fallo: motor de integración en **alta disponibilidad** y monitorización 24x7.

## Fuentes {.unnumbered .unlisted}

- HL7 Messaging Standard v2.x, HL7 International (v2.9 publicada en 2019; última versión v2.9.1; verificado online en julio de 2026).
- HL7 Version 3 Normative Edition, HL7 International (2005, con ediciones posteriores).
- HIMSS, definición de interoperabilidad y sus cuatro niveles (revisión de 2020).
