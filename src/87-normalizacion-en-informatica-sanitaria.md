# Normalización en informática sanitaria: ISO/EN 13606, terminologías clínicas y perfiles IHE

Además de los estándares de HL7 y openEHR (temas 85 y 86), la interoperabilidad sanitaria se apoya en la normalización formal (ISO y CEN), en las terminologías y clasificaciones que dan significado común a los datos, y en los perfiles IHE que indican cómo combinar todos estos estándares en escenarios reales.

## La normalización en informática sanitaria: ISO/TC 215 y CEN/TC 251

- **ISO/TC 215 «Health informatics»** (creado en **1998**): comité técnico de ISO para la informática sanitaria. De él salen, entre otras, la **ISO 13606** (comunicación de la HCE), la ISO/HL7 27932 (CDA), la **ISO 13940** (ContSys, sistema de conceptos para la continuidad asistencial) y la **ISO 12967** (HISA, arquitectura de servicios de los sistemas de información sanitarios).
- **CEN/TC 251**: el comité europeo equivalente, pionero en la materia (la 13606 nació como norma europea EN 13606 antes de adoptarse en ISO). Muchas normas se publican en paralelo como **EN ISO**.
- **En España**: el comité espejo de UNE adopta estas normas como **UNE-EN ISO**; el Ministerio de Sanidad lidera la interoperabilidad semántica del SNS (centro de referencia de SNOMED CT y edición de CIE-10-ES, ver más abajo).

## ISO/EN 13606: comunicación de la historia clínica electrónica

La **ISO/EN 13606** («Electronic health record communication», revisión vigente de **2019**) normaliza la **comunicación de extractos de HCE** (*EHR extracts*): cómo un sistema envía a otro una parte o la totalidad de la historia de un paciente conservando fielmente su significado y su contexto. No pretende normalizar la base de datos interna de cada sistema, sino el intercambio.

- **Las cinco partes de la norma**:
    - **Parte 1. Modelo de referencia**: las estructuras genéricas del extracto.
    - **Parte 2. Especificación de intercambio de arquetipos**: el modelo de objetos de arquetipo (AOM) y el lenguaje ADL.
    - **Parte 3. Arquetipos de referencia y listas de términos**.
    - **Parte 4. Seguridad**: control de acceso, consentimiento y auditoría del extracto.
    - **Parte 5. Especificación de interfaces**: interfaces de petición y entrega de extractos.
- **Modelo dual**: adopta el enfoque de openEHR (tema 86): un modelo de referencia estable más **arquetipos** que expresan el conocimiento clínico. La jerarquía del extracto es: `EHR_EXTRACT` → `FOLDER` (carpetas) → `COMPOSITION` (composición, p. ej. un informe) → `SECTION` (secciones) → `ENTRY` (entradas, la observación clínica) → `CLUSTER`/`ELEMENT` (estructuras y elementos con el valor del dato).
- **Uso**: ha servido de referencia en proyectos europeos y españoles de comunicación de HCE entre organizaciones; en el examen suele preguntarse su objeto («comunicación de la HCE»), sus 5 partes y su relación con openEHR.

## Terminologías y clasificaciones clínicas

Para que el dato clínico viaje con su significado hay que codificarlo con vocabularios comunes. Conviene distinguir **terminologías clínicas** (muy granulares, pensadas para registrar la asistencia: SNOMED CT) de **clasificaciones** (agrupan casos en categorías excluyentes para estadística y gestión: CIE).

- **SNOMED CT**: la terminología clínica integral **más completa del mundo**, mantenida por **SNOMED International**. Estructura: **conceptos** (con identificador numérico único), **descripciones** (términos sinónimos en cada idioma) y **relaciones** entre conceptos (jerárquicas «IS_A» y de atributo), organizados en jerarquías (hallazgo clínico, procedimiento, estructura corporal, fármaco…).
    - **En España**: es la **terminología clínica de referencia del SNS**. El **Ministerio de Sanidad** actúa como **Centro Nacional de Referencia** (distribución en exclusiva para el territorio) y publica dos extensiones nacionales: la **extensión para España del SNS** (actualización **semestral**) y la **extensión de medicamentos** (actualización **mensual**).
- **CIE (Clasificación Internacional de Enfermedades)**: clasificación estadística de la **OMS**.
    - **CIE-10-ES**: la modificación clínica española de la CIE-10 (diagnósticos y procedimientos), obligatoria para codificar los episodios asistenciales del SNS (CMBD/RAE-CMBD) desde **2016**. Edición vigente: **6.ª edición (enero de 2026)**, consultable en la herramienta **eCIE-Maps** del Ministerio.
    - **CIE-11**: adoptada por la OMS en 2019 y **en vigor internacionalmente desde el 1 de enero de 2022**; nativa digital (entidades con URI, herramienta de codificación en línea). En España la codificación oficial continúa en CIE-10-ES.
- **LOINC** (*Logical Observation Identifiers Names and Codes*): terminología del **Regenstrief Institute** que identifica **pruebas de laboratorio y observaciones clínicas** (el «qué se mide»: analito, propiedad, sistema, escala, método). Se usa en los mensajes de resultados (OBX-3 de HL7 v2), en FHIR (`Observation.code`) y para codificar secciones de documentos CDA. Dos versiones al año; la vigente es la **2.82 (2026)**.

| Vocabulario | Organismo | Tipo | Uso principal |
| --- | --- | --- | --- |
| **SNOMED CT** | SNOMED International | Terminología clínica | Registrar la asistencia con detalle |
| **CIE-10-ES** | OMS / Ministerio de Sanidad | Clasificación | Codificación de episodios (CMBD), estadística |
| **CIE-11** | OMS | Clasificación | Sucesora digital de la CIE-10 |
| **LOINC** | Regenstrief Institute | Terminología | Identificar pruebas y observaciones |

## Perfiles IHE

**IHE** (*Integrating the Healthcare Enterprise*, iniciativa creada en **1998** por RSNA y HIMSS) no desarrolla estándares nuevos: publica **perfiles de integración** que especifican cómo usar los estándares existentes (HL7, DICOM, terminologías) para resolver un escenario asistencial concreto, definiendo **actores** y **transacciones**. La conformidad se prueba en maratones de interoperabilidad (*connectathons*).

- **Organización por dominios**: infraestructura TI (ITI), radiología, laboratorio, cardiología, farmacia…
- **Perfiles clásicos del dominio ITI** (los más preguntables):

| Perfil | Nombre | Qué resuelve |
| --- | --- | --- |
| **XDS.b** | Cross-Enterprise Document Sharing | Compartir documentos clínicos entre organizaciones (registro de índices + repositorios) |
| **PIX** | Patient Identifier Cross-referencing | Cruzar los identificadores de un mismo paciente entre dominios |
| **PDQ** | Patient Demographics Query | Consultar datos demográficos de pacientes |
| **XCA** | Cross-Community Access | Acceso a documentos entre comunidades XDS distintas |
| **ATNA** | Audit Trail and Node Authentication | Auditoría centralizada y autenticación de nodos |
| **CT** | Consistent Time | Sincronización horaria de los sistemas |
| **XUA** | Cross-Enterprise User Assertion | Aserciones de identidad del usuario (SAML) entre organizaciones |
| **BPPC** | Basic Patient Privacy Consents | Gestión básica de consentimientos de privacidad |

- **Relevancia práctica**: la infraestructura europea MyHealth@EU (tema 89) y muchas plataformas autonómicas de HCE se construyen sobre perfiles IHE (XCA, XCPD, ATNA); en imagen médica, el perfil **SWF** (*Scheduled Workflow*) orquesta RIS, PACS y modalidades (tema 88).

## Fuentes {.unnumbered .unlisted}

- UNE-EN ISO 13606, partes 1 a 5 (revisión de 2019).
- SNOMED CT, SNOMED International; Centro Nacional de Referencia para España: Ministerio de Sanidad (extensión del SNS semestral y extensión de medicamentos mensual; verificado online en julio de 2026).
- CIE-10-ES, 6.ª edición (enero de 2026), Ministerio de Sanidad (eCIE-Maps); CIE-11, OMS (en vigor desde el 1 de enero de 2022).
- LOINC, Regenstrief Institute (versión 2.82, 2026; v2.81 de agosto de 2025).
- IHE International, perfiles de integración del dominio IT Infrastructure (ediciones continuas).
