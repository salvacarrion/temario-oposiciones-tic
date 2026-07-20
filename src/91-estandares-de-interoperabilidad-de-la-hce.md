# Estándares de interoperabilidad de la historia clínica electrónica: CDA, FHIR y openEHR

La historia clínica electrónica (HCE) reúne la información clínica de un paciente generada a lo largo de su vida por sistemas y organizaciones distintos. Para que esa información pueda intercambiarse y entenderse existen tres grandes familias de estándares, cada una con un paradigma propio: el **documento clínico** (CDA), el **recurso web** (FHIR) y el **arquetipo** (openEHR y la ISO 13606, tema [92](92-normalizacion-en-informatica-sanitaria.md)).

## La HCE interoperable y sus modelos

Cada paradigma responde a una pregunta distinta sobre cómo representar la información clínica:

| Paradigma | Unidad de intercambio | Estándar | Idea central |
| --- | --- | --- | --- |
| Documental | El documento clínico completo | **HL7 CDA** | Replicar el informe clínico firmado, legible por personas |
| Recursos | Piezas pequeñas y componibles | **HL7 FHIR** | API web moderna: la HCE como conjunto de recursos REST |
| Arquetipos | El concepto clínico modelado | **openEHR / ISO 13606** | Separar el conocimiento clínico del software (modelo dual) |

- **No son excluyentes**: un sistema puede persistir con openEHR, intercambiar informes como CDA y exponer una API FHIR. Los tres comparten la necesidad de **terminologías** comunes (SNOMED CT, LOINC, tema [92](92-normalizacion-en-informatica-sanitaria.md)) para la interoperabilidad semántica.

## HL7 CDA: el documento clínico

**CDA** (*Clinical Document Architecture*, release 2 de **2005**, adoptada también como **ISO/HL7 27932:2009**) es el estándar HL7 para representar documentos clínicos en **XML**, derivado del modelo RIM de HL7 v3 (tema [90](90-integracion-de-sistemas-sanitarios-y-mensajeria-hl7.md)). Es el formato de los informes de la HCDSNS y de la historia clínica resumida europea (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)).

- **Seis características definitorias del documento clínico**: persistencia, gestión por una organización responsable (*stewardship*), susceptibilidad de autenticación (firma), contexto, integridad (*wholeness*) y **legibilidad humana**: todo CDA debe poder leerse en un navegador con una hoja de estilo.
- **Estructura**: una **cabecera** (*header*) con metadatos obligatorios (paciente, autor, custodio, tipo de documento codificado en LOINC, fechas) y un **cuerpo** (*body*) con el contenido clínico organizado en secciones.
- **Actores de la cabecera**: `recordTarget` (el paciente), `author` (persona o dispositivo) y `custodian` (la organización responsable de custodiar el documento) son obligatorios; `legalAuthenticator` (quien firma legalmente) e `informationRecipient` son opcionales.
- **Niveles de conformidad** (interoperabilidad incremental):
    - **Nivel 1**: cuerpo no estructurado o narrativo (incluso un PDF embebido); solo la cabecera es procesable.
    - **Nivel 2**: cuerpo organizado en **secciones codificadas** (por ejemplo, con códigos LOINC de sección).
    - **Nivel 3**: las secciones contienen **entradas** (*entries*) totalmente estructuradas y codificadas, procesables por máquina dato a dato.
- **Plantillas y conformidad**: el elemento `templateId` declara las plantillas que el documento cumple; las guías de implementación fijan mediante plantillas qué secciones y entradas son obligatorias para cada tipo de informe.

Esqueleto mínimo de un CDA (simplificado):

```xml
<ClinicalDocument xmlns="urn:hl7-org:v3">
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
  <templateId root="..."/>                 <!-- plantilla que cumple -->
  <code code="18842-5" codeSystem="2.16.840.1.113883.6.1"/>
                                           <!-- tipo LOINC: informe de alta -->
  <recordTarget>...</recordTarget>         <!-- paciente -->
  <author>...</author>
  <custodian>...</custodian>               <!-- organizacion responsable -->
  <component>
    <structuredBody>
      <component>
        <section>
          <code code="10160-0" codeSystem="2.16.840.1.113883.6.1"/>
          <text>Paracetamol 1 g cada 8 horas</text>  <!-- narrativa legible -->
          <entry>...</entry>               <!-- dato codificado (nivel 3) -->
        </section>
      </component>
    </structuredBody>
  </component>
</ClinicalDocument>
```

- **Uso real**: plantillas nacionales de informes clínicos (en España, los informes del RD 1093/2010, tema [89](89-documentacion-clinica-normalizada.md)), guías de implementación como C-CDA en EE. UU. y los documentos transfronterizos de MyHealth@EU (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)).
- **Compartición**: el CDA define el documento, no su transporte; para publicarlo y localizarlo entre organizaciones se usan los perfiles IHE de compartición de documentos (XDS, tema [92](92-normalizacion-en-informatica-sanitaria.md)).

## HL7 FHIR: recursos y API REST

**FHIR** (*Fast Healthcare Interoperability Resources*) es el estándar moderno de HL7: combina la semántica clínica de los estándares previos con las tecnologías web (REST, JSON, OAuth). Versiones: **R4 (diciembre de 2018)**, la primera con contenido normativo y hoy la más desplegada; **R5 (marzo de 2023)**, la última publicada; **R6 en preparación** (en balotaje normativo durante 2026, aún no publicada).

- **Recursos**: unidades pequeñas y componibles de información (unos **150 tipos**): `Patient`, `Encounter`, `Condition`, `Observation`, `MedicationRequest`, `DiagnosticReport`… Cada recurso tiene una estructura definida, se serializa en **JSON, XML o RDF** y se enlaza a otros por referencias.
- **Estructura común del recurso**: identificador lógico `id`, metadatos `meta` (versión, `lastUpdated`, perfiles declarados), una **narrativa** legible opcional (`text`) y **extensiones** declaradas para lo que el recurso base no cubre.

```json
{
  "resourceType": "Patient",
  "id": "ejemplo",
  "identifier": [{ "system": "http://gva.es/sip", "value": "12345678" }],
  "name": [{ "family": "García López", "given": ["Ana"] }],
  "gender": "female",
  "birthDate": "1980-04-13"
}
```

- **API REST**: cada recurso se expone en una URL y se manipula con los verbos HTTP estándar (GET lee, POST crea, PUT actualiza, DELETE borra), con **búsqueda** por parámetros (incluidos comunes como `_id` o `_lastUpdated`, la inclusión de recursos referenciados con `_include` y el encadenamiento `patient.name=garcia`) y **paquetes** (`Bundle`) para agrupar recursos. El servidor declara sus capacidades en el recurso `CapabilityStatement` (endpoint `/metadata`).

```text
GET [base]/Patient/ejemplo
GET [base]/Observation?patient=ejemplo&category=laboratory&date=ge2026-01-01
```

- **Interacciones y versionado**: además de las CRUD, `vread` e `history` recuperan versiones anteriores (cada recurso guarda su historial), los `Bundle` de tipo `transaction` agrupan operaciones que se ejecutan de forma atómica y las **operaciones** con `$` encapsulan lógica de servidor (p. ej. `Patient/[id]/$everything` devuelve toda la información del paciente).
- **Paradigmas de intercambio**: FHIR no es solo REST: define **cuatro paradigmas** con los mismos recursos: API **REST**, **documentos** (`Bundle` de tipo `document` encabezado por una `Composition`, análogo al CDA), **mensajería** (`Bundle` de tipo `message`, análogo a v2) y **servicios** personalizados.
- **Terminología**: recursos propios para la semántica: `CodeSystem` (sistemas de códigos), `ValueSet` (conjuntos de valores admitidos en un elemento) y `ConceptMap` (equivalencias entre terminologías), servidos típicamente por un servidor terminológico.
- **Madurez**: cada recurso lleva un nivel **FMM 0-5** (*FHIR Maturity Model*); los más estables (`Patient`, `Observation`, `CapabilityStatement`…) son ya **normativos** y no cambiarán de forma incompatible entre versiones.
- **Los 80/20**: FHIR estandariza lo que usa la mayoría (el 80 %) y deja el resto a **extensiones** declaradas, evitando la explosión de campos opcionales de v2.
- **Perfiles y guías de implementación**: un **perfil** (`StructureDefinition`) restringe un recurso para un caso de uso (cardinalidades, terminologías obligatorias); las **guías de implementación** empaquetan perfiles para un ámbito. La más relevante internacionalmente es **IPS** (*International Patient Summary*). La seguridad se resuelve típicamente con **SMART on FHIR** (OAuth 2.0 / OpenID Connect, con permisos del tipo `patient/Observation.read`).
- **Uso masivo de datos**: la guía **Bulk Data Access** (*flat FHIR*) define la exportación asíncrona de poblaciones completas (`$export`, formato NDJSON) para uso secundario: investigación, salud pública, entrenamiento de modelos (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)).
- **Adopción**: es el estándar exigido para las API de acceso del paciente en EE. UU., la base técnica prevista del formato europeo de intercambio de HCE en el EEDS (tema [94](94-historia-clinica-digital-hcdsns-myhealth-eu-eeds.md)) y el estándar de facto para apps y servicios de salud digital.

## openEHR: el modelo dual y los arquetipos

**openEHR** (especificaciones abiertas mantenidas por openEHR International) aborda otro problema: cómo **almacenar** una HCE completa y perdurable sin que cada avance de la medicina obligue a cambiar el software. Su solución es el **modelo dual** (*two-level modelling*):

- **Nivel 1, el modelo de referencia (RM)**: un modelo de información pequeño y estable con las estructuras genéricas (composición, sección, entrada, tipos de dato clínicos). Es lo único que implementa el software.
- **Nivel 2, los arquetipos**: definiciones formales y reutilizables de conceptos clínicos («presión arterial», «diagnóstico», «informe de alta») expresadas en el lenguaje **ADL** (*Archetype Definition Language*; la versión 1.4 es la implantada, ADL 2 la sustituye gradualmente), creadas y gobernadas por profesionales clínicos, no por programadores. Se publican en repositorios como el **CKM** (*Clinical Knowledge Manager*), con gobernanza internacional y localizaciones nacionales.
- **Plantillas** (*templates*): combinan y restringen arquetipos para un formulario o caso de uso concreto (el informe de urgencias de un hospital), y de ellas se generan artefactos operativos.
- **Tipos de entrada del RM**: las entradas clínicas se clasifican según el ciclo de investigación clínica: **OBSERVATION** (lo que se observa o mide), **EVALUATION** (los juicios: diagnósticos, alergias, riesgos), **INSTRUCTION** (lo que se ordena: una prescripción, una petición) y **ACTION** (lo que se ejecuta: la administración, la intervención).
- **Jerarquía de persistencia**: el objeto **EHR** de cada paciente agrupa **composiciones** (la unidad clínica atómica que se firma y se versiona: un informe, una anotación), organizables en carpetas y con auditoría completa de versiones.
- **Consulta**: el lenguaje **AQL** (*Archetype Query Language*) permite consultar los datos por su estructura de arquetipo, con independencia de la base de datos física.
- **Posición en el ecosistema**: openEHR es fuerte como **persistencia clínica** (repositorios de datos independientes del proveedor, *vendor-neutral*); FHIR es fuerte como **interfaz de intercambio**. La norma ISO/EN 13606 (tema [92](92-normalizacion-en-informatica-sanitaria.md)) toma de openEHR el modelo dual para la comunicación de extractos de HCE.

| Aspecto | CDA | FHIR | openEHR |
| --- | --- | --- | --- |
| Año/versión | R2, **2005** | **R4** 2018, **R5** 2023 | Especificaciones continuas |
| Formato | XML | JSON, XML | Neutral (ADL para modelos) |
| Unidad | Documento | Recurso | Composición/arquetipo |
| Fuerte en | Informes firmados, intercambio documental | API, apps, integración web | Persistencia clínica a largo plazo |
| Semántica | RIM + plantillas | Perfiles + terminologías | Arquetipos + terminologías |

## Fuentes {.unnumbered .unlisted}

- HL7 CDA Release 2, HL7 International (2005; ISO/HL7 27932:2009).
- HL7 FHIR R5 (HL7 International, marzo de 2023); R4 (diciembre de 2018). R6 en balotaje normativo, no publicada (verificado online en julio de 2026).
- Especificaciones openEHR, openEHR International (RM, ADL 2, AQL; ediciones continuas).
- International Patient Summary (HL7 FHIR IG «IPS»).
