# Integración de sistemas sanitarios y mensajería HL7

Un hospital moderno ejecuta decenas de aplicaciones que necesitan compartir datos en tiempo real: el sistema de información hospitalario (HIS), la historia clínica electrónica, el laboratorio (LIS), la radiología (RIS/PACS), la farmacia, la citación o la facturación. La integración de sistemas es la disciplina que hace que ese ecosistema funcione como un todo coherente, y la mensajería HL7 es su estándar de intercambio dominante.

## La interoperabilidad en sanidad

La interoperabilidad es la capacidad de dos o más sistemas de **intercambiar información y de utilizar la información intercambiada**. En sanidad se analiza por niveles (modelo de HIMSS, alineado con el Esquema Nacional de Interoperabilidad y el Marco Europeo de Interoperabilidad, remisión al tema 62):

| Nivel | Qué garantiza | Ejemplo sanitario |
| --- | --- | --- |
| **Técnico (fundacional)** | La conexión y el transporte de datos entre sistemas | Red, TCP/IP, MLLP, HTTPS |
| **Sintáctico (estructural)** | Formato y estructura comunes del mensaje | Mensaje HL7 v2, documento XML, JSON |
| **Semántico** | Que el receptor interprete el dato con el mismo significado | Codificar el diagnóstico en SNOMED CT o CIE-10-ES (tema 92) |
| **Organizativo** | Procesos, acuerdos y marco legal compartidos | Consentimientos, convenios entre servicios de salud, HCDSNS (tema 94) |

- **Particularidades del dominio sanitario**: gran heterogeneidad de aplicaciones y proveedores, datos de **categoría especial** (art. 9 RGPD, remisión al tema 53), necesidad de disponibilidad continua (24x7) y una semántica clínica compleja que exige terminologías controladas.
- **Beneficios**: continuidad asistencial (el dato sigue al paciente), eliminación de pruebas duplicadas, seguridad del paciente (menos transcripciones manuales) y explotación secundaria de los datos (tema 94).

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
- **Resultado en la práctica**: la mensajería v3 tuvo una **adopción muy limitada** (complejidad alta, coste de implantación, ecosistema v2 ya consolidado). Su producto derivado de éxito es el estándar de documentos clínicos **CDA**, basado en el RIM, que se estudia en el tema 91 junto con FHIR, el estándar moderno que recupera la sencillez de v2 con tecnologías web.

| Aspecto | HL7 v2.x | HL7 v3 |
| --- | --- | --- |
| Año | Desde 1989 (última: **2.9.1**) | Edición normativa **2005** |
| Paradigma | Mensajería por eventos, sintaxis propia | Dirigido por modelos (**RIM**), XML |
| Semántica | Débil, negociada por implantación | Formal, vocabularios controlados |
| Adopción | Dominante en hospitales | Muy limitada (sobrevive vía CDA) |
| Coste de implantación | Bajo | Alto |

## Fuentes {.unnumbered .unlisted}

- HL7 Messaging Standard v2.x, HL7 International (v2.9 publicada en 2019; última versión v2.9.1; verificado online en julio de 2026).
- HL7 Version 3 Normative Edition, HL7 International (2005, con ediciones posteriores).
- HIMSS, definición de interoperabilidad y sus cuatro niveles (revisión de 2020).
