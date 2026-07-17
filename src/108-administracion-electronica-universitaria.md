# Administración electrónica universitaria

Las universidades públicas son Administraciones Públicas: les aplica el régimen común de administración electrónica de las **Leyes 39/2015 y 40/2015** y del **RD 203/2021** (temas [54](54-administracion-electronica.md) y [82](82-administracion-electronica-y-plataformas-de-la-generalitat.md)), el ENI (tema [62](62-esquema-nacional-de-interoperabilidad.md)) y el ENS (temas [29](29-esquema-nacional-de-seguridad.md) y [105](105-adecuacion-al-ens-en-universidades-ccn-stic-881.md)). Este tema recorre la instanciación universitaria de ese marco: la medición de la digitalización del sistema (UNIVERSITIC), el nodo de interoperabilidad académico **NISUE**, las sedes y servicios electrónicos (con la **UPV** como caso) y la gestión documental universitaria.

## La digitalización del sistema universitario: Crue y UNIVERSITIC

- **Crue Digitalización** (antes Crue-TIC): la comisión sectorial de tecnologías de la información de Crue Universidades Españolas; coordina la estrategia digital del sector, los grupos de trabajo (administración electrónica, seguridad, gestión TI) y los servicios compartidos entre universidades.
- **Informe UNIVERSITIC**: estudio periódico de Crue Digitalización que mide con indicadores cuantitativos el estado de las TIC y la **madurez digital** del sistema universitario español, como herramienta de autodiagnóstico y planificación estratégica. La edición vigente es **UNIVERSITIC 2024**, que analiza el periodo **2020-2024**.
- **Modelo de madurez digital md4u**: base metodológica de UNIVERSITIC, con **21 áreas**, **37 objetivos estratégicos** y más de **300 indicadores** que determinan el grado de digitalización de cada universidad y fijan objetivos de mejora (UNIVERSITIC 2022).
- **Anclajes en la LOSU**: derecho del estudiantado a la formación en **capacidades digitales** y a la seguridad de los medios digitales (art. 33) y obligación de **digitalizar progresivamente archivos y fondos bibliotecarios** (art. 21.4); ver tema [103](103-sistema-universitario-losu.md).

## Interoperabilidad universitaria: NISUE

- **NISUE (Nodo de Interoperabilidad del Sistema Universitario Español)**: punto único de intercambio de **datos académicos** entre las universidades y con el resto de Administraciones Públicas. En producción desde el **30 de enero de 2017**, impulsado por el grupo de trabajo de administración electrónica de **Crue Digitalización** en colaboración con **RedIRIS**; figura como solución en el Centro de Transferencia de Tecnología (CTT).
- **Funcionamiento**: actúa como intermediario integrado con la **Plataforma de Intermediación de Datos (PID)** estatal, empleando el protocolo **SCSP** (Sustitución de Certificados en Soporte Papel, tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)). Los primeros conjuntos de datos ofrecidos fueron la **matrícula universitaria** y los datos de expediente y titulación.
- **Finalidad**: hacer efectivo el principio de **«solo una vez»** (*once-only*): que el ciudadano no aporte títulos, matrículas o certificados que las Administraciones pueden verificar electrónicamente, y que las universidades intercambien expedientes (traslados, acceso a posgrado) sin papel.
- **Marco**: ENI y sus normas técnicas (tema [62](62-esquema-nacional-de-interoperabilidad.md)) y servicios comunes de interoperabilidad estatales (tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)).

## Sedes y servicios electrónicos universitarios: el caso UPV

- **Sede electrónica** (art. 38 Ley 40/2015 y arts. 9-12 RD 203/2021): cada universidad es titular de su sede, responsable de la **integridad, veracidad y actualización** de su contenido, identificada con certificado de sede.
- **Sede electrónica de la UPV** (sede.upv.es): **catálogo de procedimientos y servicios electrónicos** (matrícula, certificados académicos, solicitudes de estudiantes y de personal, convocatorias), **registro electrónico**, tablón oficial y notificaciones por comparecencia.
- **Verificación por CSV**: los documentos emitidos por la universidad incorporan un **Código Seguro de Verificación** que permite contrastar en la sede su **autenticidad e integridad** (copias auténticas y actuación administrativa automatizada, temas [54](54-administracion-electronica.md) y [55](55-documento-y-expediente-electronico.md)).
- **Identificación y firma en la UPV**: certificados electrónicos admitidos (los de la **ACCV** y el certificado de **empleado público**, entre otros), **Cl@ve**, firma con **AutoFirma** y la **clave de firma UPV**: sistema propio de firma centralizada («en la nube») para la comunidad universitaria, que evita instalar el certificado en el dispositivo. Marco eIDAS y plataformas estatales de firma (@firma, FIRe): tema [65](65-identificacion-y-firma-electronica.md).
- **Carné y cuenta corporativa**: la identidad digital universitaria (cuenta única con SSO, tema [106](106-rediris-e-identidad-federada.md)) da acceso a intranet, campus virtual y servicios electrónicos.

## Gestión documental y archivo electrónico universitario

- **Gestor documental corporativo**: da servicio a los aplicativos de tramitación; en muchas universidades se apoya en **Alfresco** u otros gestores de contenidos empresariales.
- **Metadatos**: documentos y expedientes electrónicos conforme a las NTI, con el esquema de metadatos para la gestión del documento electrónico (**e-EMGDE**) y **cuadros de clasificación** funcional de la documentación universitaria (tema [55](55-documento-y-expediente-electronico.md)).
- **Archivo electrónico único** (art. 17 Ley 39/2015): conservación a largo plazo de los expedientes finalizados en formatos que garanticen autenticidad e integridad; algunas universidades emplean soluciones específicas de archivo definitivo (en la UPV, el gestor de archivo **Odilo A3W**).
- **Política de gestión de documentos electrónicos**: clasificación, calificación, plazos de conservación, transferencia y expurgo, alineada con el ENI (tema [62](62-esquema-nacional-de-interoperabilidad.md)).

## Fuentes {.unnumbered .unlisted}

- Crue Digitalización, informe UNIVERSITIC 2024 (y modelo md4u descrito en UNIVERSITIC 2022), tic.crue.org (consultado en julio de 2026).
- NISUE, rediris.es/nisue y solución del CTT (administracionelectronica.gob.es/ctt/nisue), consultadas en julio de 2026.
- Ley 39/2015 y Ley 40/2015 (textos consolidados; ver temas [10](10-procedimiento-administrativo-comun.md) y [9](09-regimen-juridico-del-sector-publico.md)) y RD 203/2021 (ver tema [54](54-administracion-electronica.md)).
- Sede electrónica de la UPV, sede.upv.es (consultada en julio de 2026).
- Ley Orgánica 2/2023, del Sistema Universitario, arts. 21.4 y 33 (texto consolidado, última modificación 2 de agosto de 2024).
