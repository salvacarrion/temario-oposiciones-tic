# Adecuación al ENS en las universidades (CCN-STIC 881)

Las universidades públicas forman parte del sector público y sus sistemas de información están sujetos al **Esquema Nacional de Seguridad** (RD 311/2022, tema [29](29-esquema-nacional-de-seguridad.md)). Para facilitar esa adecuación de forma homogénea en todo el sector, el Centro Criptológico Nacional publicó la **guía CCN-STIC 881, de Adecuación al ENS para Universidades** (ed. mayo 2022), elaborada en colaboración con la CRUE, que define un **Perfil de Cumplimiento Específico para Universidades** y un modelo completo de gobernanza y adecuación.

## El ENS y los perfiles de cumplimiento específicos

- **Marco**: el **RD 311/2022** regula el ENS, con sus principios básicos, requisitos mínimos, la categorización de sistemas (**BÁSICA, MEDIA, ALTA**) y las medidas de seguridad del Anexo II (tema [29](29-esquema-nacional-de-seguridad.md)).
- **Perfiles de cumplimiento específicos (art. 30 RD 311/2022)**: conjuntos de medidas de seguridad ajustados a un **colectivo de entidades con riesgos homogéneos** (ayuntamientos, universidades…), que permiten una adecuación «más eficaz y eficiente» sin rebajar la protección exigible. Los **valida y publica el CCN**.
- **Objetivo de la CCN-STIC 881**: proporcionar «un modelo que facilite la adecuación al ENS de los sistemas de las universidades públicas de forma ordenada y efectiva», hasta obtener la **Certificación de Conformidad** con el ENS según el Perfil de Cumplimiento Específico para Universidades. La guía incluye como anexos un modelo de **Política de Seguridad** (Anexo I) y de **Plan de Adecuación** (Anexo II), junto con un catálogo tipo de servicios e información universitarios.

## Modelo de gobernanza de la seguridad

La guía propone un modelo de organización de la seguridad consensuado con la **CRUE**, que cada universidad debe adaptar y recoger en su **Política de Seguridad de la Información**:

- **Comité de Seguridad TIC**: órgano colegiado que **articula** la gobernanza; presidido por el **Rector o persona delegada**, con miembros permanentes y no permanentes; adopta sus decisiones por **consenso de los miembros permanentes**.
- **Oficina de Seguridad TIC**: **gestiona** la seguridad en el día a día; su dirección convoca las reuniones de trabajo y puede funcionar en pleno o en grupos de trabajo.
- **Centro de Operaciones de Ciberseguridad (COCS)**: **implementa** la seguridad en colaboración con el área o servicio de TI, y realiza la **vigilancia continua, detección y respuesta** sobre los sistemas bajo su responsabilidad.
- **Órgano de Auditoría Técnica (OAT)**, opcional según el tamaño: realiza las **revisiones periódicas y auditorías de conformidad**, garantizando la **imparcialidad** (sin conflicto de interés) respecto del personal implantador.
- **Foro de Seguridad TIC**: espacio interuniversitario de colaboración entre los responsables de seguridad de las universidades.

En síntesis: la Oficina y el OAT hacen **prevención proactiva**; el COCS, **vigilancia, detección y respuesta**.

## El Plan de Adecuación al ENS

Documento que recoge el proceso de adecuación, en **cinco pasos**:

1. **Alcance de los sistemas a certificar**: catálogo de los **servicios prestados** y la **información** que manejan, y del sistema que los aloja (la guía aporta un modelo elaborado con la CRUE a partir de las funciones legales de las universidades).
2. **Valoración y categorización del sistema**: impacto de un incidente en las **cinco dimensiones** de seguridad (**confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad**) en niveles **BAJO, MEDIO o ALTO**, conforme al Anexo I del ENS y la guía **CCN-STIC 803** (valoración de sistemas); la determinan los responsables de la información y de los servicios.
3. **Declaración de Aplicabilidad Provisional**: adopción formal del **Perfil de Cumplimiento Específico para Universidades**, identificando sus medidas y refuerzos y, en su caso, las **medidas compensatorias** de igual o superior protección (guía **CCN-STIC 819**).
4. **Análisis de riesgos**: conforme al Anexo II del ENS, con la metodología **MAGERIT** recomendada (tema [30](30-analisis-y-gestion-de-riesgos.md)).
5. **Declaración de Aplicabilidad Definitiva**: el **perfil de cumplimiento validado** para los sistemas de la universidad.

Tras el Plan de Adecuación se elabora el **plan de implantación**: la hoja de ruta priorizada de documentos a elaborar y medidas técnicas a implementar.

## Implantación de las medidas

La guía aterriza en el entorno universitario las medidas del **Anexo II del ENS**, organizadas en sus tres marcos:

| Marco | Familias destacadas en la guía |
| --- | --- |
| Organizativo [org] | Política de seguridad, **normativa de seguridad** (uso correcto de los recursos TIC, usos indebidos, régimen disciplinario; base en la CCN-STIC 821), procedimientos |
| Operacional [op] | Planificación [op.pl], **control de acceso** [op.acc], explotación [op.exp], recursos externos [op.ext], **servicios en la nube** [op.nub], continuidad del servicio [op.cont], monitorización [op.mon] |
| Medidas de protección [mp] | Instalaciones [mp.if], personal [mp.per], equipos [mp.eq], comunicaciones [mp.com], soportes [mp.si], aplicaciones [mp.sw], información [mp.info], servicios [mp.s] |

- **Normativa de seguridad**: debe fijar alcance, vigencia, órganos de aprobación y revisión, el uso correcto de los recursos TIC, qué se considera **uso indebido** y el régimen disciplinario, y difundirse con acciones de **concienciación**.
- **Productos certificados**: cuando se requieran productos de seguridad, se emplean componentes certificados del catálogo **CPSTIC** del CCN; en su defecto, se aplica el art. 19 del RD 311/2022.

## Herramientas para la gobernanza de la ciberseguridad

En consonancia con la **vigilancia continua y la reevaluación periódica** (art. 10 RD 311/2022), el CCN pone a disposición de las universidades sus herramientas de gobernanza:

- **INES**: informe del estado de seguridad y asistente para elaborar y actualizar el **Plan de Adecuación** (alcance, categorización, declaraciones de aplicabilidad, análisis de riesgos), revisar la valoración de servicios e información y la **Política de Seguridad** (revisión normalmente **anual** por el Comité de Seguridad).
- **AMPARO**: apoyo a la **implantación** del ENS y al seguimiento del plan de implantación, la concienciación y formación anual y la revisión de la normativa de seguridad.

El ciclo se cierra con las **auditorías de conformidad** (cada **dos años** en categorías MEDIA y ALTA, conforme al régimen general del ENS, tema [29](29-esquema-nacional-de-seguridad.md)) y la mejora continua de los procesos de seguridad.

## Fuentes {.unnumbered .unlisted}

- CCN-STIC 881, Guía de Adecuación al ENS para Universidades (ed. mayo 2022, con Anexos I Política de Seguridad y II Plan de Adecuación; edición vigente verificada online en julio de 2026).
- Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (texto consolidado; ver tema [29](29-esquema-nacional-de-seguridad.md)).
- Guías CCN-STIC relacionadas citadas por la 881: 803 (valoración de sistemas), 819 (medidas compensatorias), 821 (normas de seguridad) y catálogo CPSTIC.
