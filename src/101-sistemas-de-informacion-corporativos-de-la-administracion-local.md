# Sistemas de información corporativos de la administración local

Los ayuntamientos sostienen su gestión interna sobre una familia característica de sistemas de información corporativos: la gestión económico-financiera (contabilidad, facturas y control), la gestión tributaria y recaudatoria, el padrón municipal de habitantes, los recursos humanos y las subvenciones. Este tema los recorre a partir de las normas que fijan qué deben registrar, con qué garantías y con quién deben intercambiar datos. La administración electrónica local (sede, registro, firma y gestor documental) se estudia en el tema [102](102-administracion-electronica-local.md); las **plataformas de ciudad inteligente**, en el [78](78-ciudades-inteligentes.md); y los **SIG y geoportales**, en los temas [66](66-sistemas-de-informacion-geografica.md) y [67](67-infraestructuras-de-datos-espaciales.md).

## Los sistemas de información corporativos de la entidad local

Un sistema de información corporativo da servicio a toda la organización y no a una sola unidad: comparte datos maestros con los demás sistemas de la entidad y con los de otras Administraciones. En un ayuntamiento buena parte de su diseño viene impuesta por normas que fijan registros obligatorios, formatos, plazos y destinatarios de la información.

- **Componentes habituales**:
    - **Sistemas de gestión** (*back-office*): contabilidad y presupuesto, tributos y recaudación, padrón de habitantes, recursos humanos y nómina, subvenciones, y patrimonio e inventario.
    - **Datos maestros compartidos**: la base de **terceros** (vecinos, contribuyentes, proveedores, beneficiarios y empleados) y la **base territorial o callejero** (vías, portales y referencias catastrales), sobre la que se apoyan el padrón, los tributos y los SIG.
    - **Sistemas transversales de administración electrónica**: registro, gestor de expedientes, firma, notificaciones y archivo (tema [102](102-administracion-electronica-local.md)).
- **Patrón de integración**:
    - La tendencia es integrar la gestión económico-financiera, la tributaria, la de personal y la tramitación de expedientes en un **ERP municipal** sobre una base de datos corporativa única, o bien conectar aplicaciones especializadas mediante **servicios web**.
    - En ambos casos se evitan las islas de información y las dobles capturas: la nómina, la recaudación y las subvenciones generan sus operaciones contables directamente en la contabilidad.
- **Apoyo a los municipios pequeños**:
    - La diputación presta «Asistencia en la prestación de los servicios de gestión de la recaudación tributaria, en periodo voluntario y ejecutivo, y de servicios de apoyo a la gestión financiera de los municipios con población inferior a 20.000 habitantes» (**art. 36.1.f LRBRL**).
    - Asume la **gestión informatizada del padrón** de los municipios que no la lleven efectivamente (art. 60.2 del RD 1690/1986).
    - Ofrece a los municipios de **menos de 20.000 habitantes** los medios técnicos para la **factura electrónica** (art. 6.8 de la Ley 25/2013).
- **Requisitos transversales**:
    - Los sistemas que tratan datos personales (padrón, tributos y nómina) se someten al RGPD y a la LOPDGDD (tema [53](53-proteccion-de-datos-personales.md)).
    - Todos ellos quedan sujetos al **ENS** (tema [29](29-esquema-nacional-de-seguridad.md)) y al **ENI** (tema [62](62-esquema-nacional-de-interoperabilidad.md)).

| Sistema municipal | Organismo | Qué se intercambia | Base |
| --- | --- | --- | --- |
| Padrón de habitantes | **INE** | Variaciones del padrón (en tiempo real tras el RD 141/2024) y discrepancias detectadas | Arts. 65-66 RD 1690/1986 |
| Padrón y tributos | **Dirección General del Catastro** | Referencias catastrales; **padrón catastral** del IBI, remitido **antes del 1 de marzo** | Art. 63 RD 1690/1986; art. 77.5 TRLHL |
| Tributos | **AEAT** | **Matrícula del IAE**: gestión censal estatal | Art. 91 TRLHL |
| Tributos | **DGT** (Registro de Vehículos) | Impagos del IVTM al acabar el periodo voluntario | Art. 99.3 TRLHL |
| Facturas | **FACe** o punto de la diputación o de la comunidad autónoma | Facturas electrónicas de los proveedores | Art. 6 y DA 5.ª Ley 25/2013 |
| Contabilidad | **Tribunal de Cuentas** y órgano autonómico de control externo (**Sindicatura de Comptes**) | Cuenta General (al Tribunal de Cuentas, **antes del 15 de octubre**) | Art. 223 TRLHL; reglas 3 y 51 ICAL |
| Control interno | **IGAE** | Informe resumen anual e información contable | Arts. 36-37 RD 424/2017 |
| Subvenciones | **IGAE** (BDNS) | Convocatorias, concesiones, pagos, reintegros y sanciones | Art. 20 LGS; RD 130/2019 |

| Norma | Qué aporta | Texto consolidado a |
| --- | --- | --- |
| **Real Decreto 1690/1986**, Reglamento de Población y Demarcación Territorial de las Entidades Locales | Padrón: datos, gestión electrónica, intercambio con el INE, revisión anual y Consejo de Empadronamiento | 7 de febrero de 2024 |
| **Resolución de 17 de febrero de 2020** (INE y Dirección General de Cooperación Autonómica y Local), instrucciones técnicas sobre la gestión del padrón | Fichero de inscritos, codificación, remisión al INE y caducidades | 8 de febrero de 2023 |
| **Real Decreto Legislativo 2/2004**, texto refundido de la Ley Reguladora de las Haciendas Locales (TRLHL) | Contexto: tributos, contabilidad, Cuenta General y control | 3 de junio de 2026 |
| **Orden HAP/1781/2013**, Instrucción del modelo normal de contabilidad local (ICAL) | SICAL-Normal | 3 de agosto de 2021 |
| **Orden HAP/1782/2013**, Instrucción del modelo simplificado | SICAL-Simplificado | 22 de diciembre de 2018 |
| **Orden EHA/4040/2004**, Instrucción del modelo básico | SICAL-Básico | 3 de octubre de 2013 |
| **Ley 25/2013**, de impulso de la factura electrónica y creación del registro contable de facturas | Punto general de entrada y registro contable de facturas | 13 de junio de 2015 |
| **Real Decreto 424/2017**, control interno en las entidades del sector público local | Control interno y sistemas de información | Sin modificaciones |
| **Ley 58/2003**, General Tributaria (LGT) | Notificación colectiva y periodo de pago | 21 de diciembre de 2024 |
| **Real Decreto Legislativo 5/2015**, TREBEP | Registros de personal | 30 de julio de 2025 |
| **Ley 38/2003**, General de Subvenciones (LGS) | Base de Datos Nacional de Subvenciones | 2 de agosto de 2024 |
| **Real Decreto 130/2019**, BDNS y publicidad de las subvenciones | Suministro y publicidad | 22 de marzo de 2021 |

## Gestión económico-financiera: el SICAL

Las entidades locales y sus organismos autónomos están sometidos al **régimen de contabilidad pública**, que lleva consigo la obligación de rendir cuentas al **Tribunal de Cuentas** (arts. 200-201 TRLHL). El Ministerio de Hacienda, a propuesta de la **IGAE**, aprueba las normas contables (art. 203), y a la **Intervención** le corresponde llevar la contabilidad (art. 204). Las normas vigentes son tres Instrucciones de contabilidad, y cada una define un modelo del **sistema de información contable para la Administración local (SICAL)**. El TRLHL solo se cita aquí como contexto.

### Los modelos de contabilidad local

| Modelo | Norma | Ámbito (regla 1) | Método |
| --- | --- | --- | --- |
| **Normal** (SICAL-Normal) | Orden HAP/1781/2013 | Municipios con presupuesto superior a **3.000.000 €**; municipios de más de **300.000 €** y hasta 3.000.000 € con población superior a **5.000 habitantes**; demás entidades locales con presupuesto superior a 3.000.000 € | Partida doble |
| **Simplificado** (SICAL-Simplificado) | Orden HAP/1782/2013 | Municipios con presupuesto hasta **300.000 €**; municipios de más de 300.000 € y hasta 3.000.000 € con población **no superior a 5.000 habitantes**; demás entidades locales hasta 3.000.000 € | Partida doble |
| **Básico** (SICAL-Básico) | Orden EHA/4040/2004 | **Opcional** para entidades con presupuesto hasta **300.000 €**, salvo que dependan de ellas organismos autónomos, sociedades mercantiles o entidades públicas empresariales | **Partida simple** |

- **Cómo se mide**: el presupuesto es el de las **previsiones iniciales de ingresos** del último presupuesto aprobado definitivamente (con el estado de consolidación de sus organismos autónomos); la población, la de la **última revisión del padrón** (regla 1).
- **Opciones**: las entidades del modelo simplificado pueden aplicar el normal, y los **organismos autónomos** aplican siempre la misma Instrucción que la entidad de la que dependen.
- **Salida del modelo básico**: si una entidad que lo aplica aprueba un presupuesto superior a 300.000 €, solo pasa al simplificado o al normal si la circunstancia se mantiene **tres ejercicios consecutivos** (regla 1.2 de la Orden EHA/4040/2004).
- **Vigencia del básico**: la reforma de 2013 no lo derogó; la Orden HAP/1782/2013 solo lo modificó y la Orden HAP/1781/2013 explica que se mantuvo «su simplicidad».

### El SICAL como sistema de información

Las Instrucciones regulan la contabilidad como un sistema de información y fijan requisitos para su configuración informática. Las reglas que siguen son las del modelo normal; los modelos simplificado y básico siguen el mismo esquema.

- **Definición (regla 11)**: la contabilidad de las entidades locales y sus organismos autónomos se configura como «un sistema de registro, elaboración y comunicación de información sobre la actividad económico-financiera y presupuestaria desarrollada durante el ejercicio contable».
- **Objeto (regla 12)**: «registrar todas las operaciones de naturaleza presupuestaria, económica, financiera y patrimonial» y mostrar, mediante estados e informes, «la imagen fiel» del patrimonio, de la situación financiera, del resultado económico-patrimonial y de la ejecución del presupuesto.
    - Se configura como «un conjunto integrado de subsistemas o áreas contables» que garantiza la «concordancia, exactitud y automatismo» de los registros de cada operación en todos los subsistemas a los que afecte.
    - Debe permitir, al menos, registrar el balance y el resultado económico-patrimonial; el presupuesto (créditos, modificaciones, ejecución del gasto y del ingreso, presupuestos cerrados y ejercicios posteriores, **gastos con financiación afectada**, proyectos de gasto y **remanente de tesorería**); las operaciones no presupuestarias y las de administración de recursos de otros entes públicos; la tesorería; el inmovilizado, el patrimonio público del suelo, las inversiones financieras y el endeudamiento; los **terceros**; los **pagos a justificar** y los **anticipos de caja fija**; y los valores en depósito.
- **Fines (regla 13)**:
    - suministrar información para la **toma de decisiones**, política y de gestión;
    - determinar el **coste y rendimiento** de los servicios públicos;
    - formar y rendir la **Cuenta General** y las cuentas que se remitan a los órganos de control externo;
    - posibilitar los **controles de legalidad, financiero y de eficacia**;
    - aportar datos a las **cuentas nacionales** del sector de las Administraciones públicas y a las estadísticas del Ministerio de Hacienda;
    - informar a otros destinatarios (asociaciones, empresas y ciudadanos).
- **Configuración informática (regla 14)**:
    - orientada al objeto y los fines del sistema;
    - debe garantizar «la integridad, coherencia, exactitud y automatismo de las anotaciones» en todos los subsistemas afectados y la concordancia entre la información agregada y la de detalle;
    - debe propiciar la simplificación de los procedimientos contables mediante «la aplicación intensiva de procedimientos y medios electrónicos, informáticos y telemáticos»;
    - y debe aplicar las medidas de seguridad de la normativa de datos personales.
- **Soporte (regla 15)**:
    - Los registros están soportados informáticamente y constituyen «el soporte único y suficiente» que garantiza su conservación.
    - «Las bases de datos del sistema informático donde residan los registros contables constituirán soporte suficiente para la llevanza de la contabilidad», **sin que sea obligatorio** obtener y conservar libros de contabilidad, ni en papel ni en soporte electrónico.
    - Los registros se expresan en **euros**.
- **Captura de los datos (reglas 34-36)**:
    - Todo hecho contable debe acreditarse con su **justificante**, en papel o por medios electrónicos que aseguren su validez y eficacia jurídica.
    - Los datos se incorporan por **captura directa** del justificante o del documento contable, o por **medios electrónicos** desde otros sistemas, una a una o mediante **incorporación masiva**.
    - Los **documentos contables** los establece cada entidad según sus necesidades.
- **Autorización y toma de razón (reglas 37-38)**:
    - Si los datos llegan por medios electrónicos, las diligencias, firmas manuscritas y sellos pueden sustituirse por «autorizaciones y controles establecidos en las propias aplicaciones informáticas» que garanticen la identificación y la competencia de quien autoriza.
    - La **toma de razón** es una diligencia del responsable de la contabilidad con la fecha, el número de asiento y el importe. Puede hacerse por **certificación mecánica** del equipo informático y, si la operación llega por medios electrónicos, se sustituye por los **procesos de validación** del sistema.
- **Conservación (reglas 39-40)**:
    - Justificantes y registros se conservan **seis años** desde la remisión de las cuentas anuales a los órganos de control externo.
    - Las copias obtenidas de soportes electrónicos tienen la validez y eficacia de los originales.
    - La **destrucción** exige comunicarla antes al órgano de control externo y que este no ponga impedimentos.
- **Información que produce (reglas 41-43)**:
    - Las cuentas anuales.
    - La información periódica al Pleno (art. 207 TRLHL).
    - El avance de la liquidación del presupuesto.
    - La información para la gestión, el control interno y otras Administraciones.
    - El responsable de la contabilidad «únicamente responde de la identidad entre la misma y la existente en las bases de datos del sistema».

### La Cuenta General y su rendición

La **Cuenta General** pone de manifiesto la gestión económica, financiera, patrimonial y presupuestaria del ejercicio (art. 208 TRLHL). Se forma a partir del SICAL y se rinde por medios telemáticos.

- **Composición (art. 209 TRLHL; reglas 44-45)**:
    - La integran la cuenta de la propia entidad, la de sus **organismos autónomos** y las de las **sociedades mercantiles** de capital íntegramente local (la Instrucción añade las de las entidades públicas empresariales).
    - Las cuentas anuales de la entidad y de cada organismo autónomo son el balance, la cuenta del resultado económico-patrimonial, el estado de cambios en el patrimonio neto, el estado de flujos de efectivo, el estado de liquidación del presupuesto y la memoria.

| Trámite | Órgano | Plazo |
| --- | --- | --- |
| Rendición de los estados y cuentas | **Presidente** de la entidad (cuentadante) | Antes del **15 de mayo** del ejercicio siguiente |
| Formación de la Cuenta General | **Intervención** | |
| Informe | **Comisión Especial de Cuentas** | Antes del **1 de junio** |
| Exposición pública | | **15 días**, para examinarla y presentar reclamaciones, reparos u observaciones |
| Aprobación | **Pleno** | Antes del **1 de octubre** |
| Rendición al Tribunal de Cuentas | **Presidente** | Antes del **15 de octubre** (art. 223.2) |

- **Plazos de la ley y de la Instrucción**: los del cuadro son los de los arts. 212 y 223 TRLHL. La regla 49.2 de la Instrucción conserva aún «quince días, durante los cuales y ocho más» para las reclamaciones, pero ese añadido desapareció de la ley con la **Ley 11/2020** (Presupuestos para 2021, DF 19.ª).
- **Rendición aunque se rechace**: desde esa misma reforma, «Una vez que el Pleno se haya pronunciado sobre la Cuenta General, aprobándola o rechazándola, el presidente de la corporación la rendirá al Tribunal de Cuentas» (art. 212.5).
- **Control externo autonómico**: rinden también al órgano de control externo de su comunidad autónoma (regla 3), que en la Comunitat Valenciana es la **Sindicatura de Comptes** (art. 39 del Estatut).
- **Rendición telemática (regla 51.3)**: cuando los órganos de control externo tienen procedimientos electrónicos, las cuentas se obtienen «mediante la generación de ficheros» cuyo contenido y estructura fijan esos órganos.
    - La regla aún cita la LOPD de 1999 y las Leyes 30/1992 y 11/2007, hoy derogadas.
    - El canal es la **Plataforma de Rendición de Cuentas de las Entidades Locales**, que gestionan el Tribunal de Cuentas y la mayoría de los órganos autonómicos de control externo. Por convenio, la rendición por ella vale en un solo acto ante ambos.

### Factura electrónica y registro contable de facturas

La **Ley 25/2013** generalizó la factura electrónica con las Administraciones y creó el registro contable de facturas; su régimen completo se estudia en el tema [68](68-comercio-electronico-y-factura-electronica.md). Aquí interesan sus piezas locales y su encaje con el SICAL.

- **Punto general de entrada (art. 6)**:
    - Cada entidad local dispone de un punto general de entrada de facturas electrónicas o se adhiere al que proporcione su **diputación**, su **comunidad autónoma** o el **Estado** (**FACe**).
    - La adhesión al punto de la AGE es voluntaria, pero la no adhesión debe justificarse en términos de eficiencia (DA 5.ª).
    - La presentación produce una entrada automática en un registro electrónico, con **acuse de recibo** y la fecha y hora de presentación.
- **Registro contable de facturas (arts. 8-9)**:
    - Cada entidad dispone de uno, cuya gestión corresponderá «al órgano o unidad administrativa que tenga atribuida la función de contabilidad».
    - Está «interrelacionado o integrado con el sistema de información contable».
    - La anotación asigna un **código de identificación**, que después identifica la factura en la propuesta u orden de pago.
- **Seguimiento (art. 10)**: el órgano contable dirige requerimientos periódicos sobre las facturas pendientes de reconocimiento de la obligación. Elabora además un **informe trimestral** de las que llevan **más de tres meses** anotadas sin reconocimiento y lo remite al órgano de control interno en los **quince días** siguientes a cada trimestre natural.
- **Control (art. 12)**:
    - La intervención tiene acceso al registro y a la contabilidad «en cualquier momento».
    - Elabora un **informe anual de morosidad**, que en las entidades locales se eleva al **Pleno**.
    - Realiza una **auditoría de sistemas anual** del registro contable de facturas. Verifica que no quedan facturas retenidas y analiza los **tiempos medios de inscripción** y el número y las causas de las **facturas rechazadas**.

### Control interno y sistemas de información

El control interno de la gestión económica local se ejerce en las modalidades de «función interventora, función de control financiero, incluida la auditoría de cuentas de las entidades que se determinen reglamentariamente, y función de control de la eficacia» (art. 213 TRLHL). Lo desarrolla el **RD 424/2017**, que contiene varias previsiones sobre los sistemas de información.

- **Revisión de los sistemas**:
    - El órgano interventor dispone de «la facultad de revisión de los sistemas informáticos de gestión» (art. 6.1).
    - Los funcionarios del control financiero «podrán revisar los sistemas informáticos de gestión que sean precisos» (art. 6.7).
    - En la auditoría pública puede encargarse «Verificar la seguridad y fiabilidad de los sistemas informáticos que soportan la información económico-financiera y contable» (art. 33.4.e).
- **Reparos y discrepancias (art. 15)**:
    - La **IGAE** gestiona una **base de datos** con sus informes sobre discrepancias, a la que acceden los órganos de control interno locales.
    - El órgano interventor eleva al **Pleno** el informe anual de las resoluciones contrarias a los reparos.
    - Con ocasión de la Cuenta General, las remite al **Tribunal de Cuentas** (art. 218 TRLHL).
- **Publicidad (art. 36.2)**: la información contable y los informes de auditoría de cuentas se publican en las **sedes electrónicas** y se remiten a la IGAE para el **registro de cuentas anuales del sector público**.
- **Informe resumen (arts. 37-38)**:
    - Es anual y se remite al Pleno y a la **IGAE** «en el curso del primer cuatrimestre de cada año».
    - Con él, el Presidente formaliza un **plan de acción** en un máximo de **3 meses**.
- **Expediente electrónico (DA 7.ª)**: la fiscalización de expedientes tramitados electrónicamente debe ser coherente con los criterios que fije la IGAE para su ámbito y no puede alterar los requisitos de fiscalización.

## Gestión tributaria y recaudación

La gestión de los tributos locales es una de las aplicaciones de mayor volumen de un ayuntamiento. Mantiene los censos de cada tributo (padrones fiscales), liquida, emite los documentos de cobro y gestiona la recaudación voluntaria y ejecutiva. Buena parte de sus datos de partida llega de otras Administraciones.

- **Tributos que gestiona (art. 59 TRLHL)**:
    - Los impuestos **obligatorios** sobre Bienes Inmuebles (**IBI**), Actividades Económicas (**IAE**) y Vehículos de Tracción Mecánica (**IVTM**).
    - Los **potestativos** sobre Construcciones, Instalaciones y Obras (**ICIO**) y sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana (**IIVTNU**).
    - Además, tasas, contribuciones especiales y precios públicos.
    - La potestad reglamentaria se ejerce mediante **ordenanzas fiscales** y «Ordenanzas generales de gestión, recaudación e inspección» (art. 106.2 LRBRL).
- **Gestión compartida con el Estado**:
    - **IBI**: la liquidación y la recaudación son «competencia exclusiva de los ayuntamientos» (art. 77.1). El impuesto se gestiona a partir del **padrón catastral** que elabora la **Dirección General del Catastro**: se forma anualmente para cada término y se remite a las entidades gestoras **antes del 1 de marzo** (art. 77.5). Sus datos deben figurar en las listas cobratorias, documentos de ingreso y justificantes de pago (art. 77.6).
    - **IAE**: la formación de la **matrícula**, la calificación de las actividades, el señalamiento de las cuotas «y, en general, la gestión censal del tributo» corresponden a la **Administración tributaria del Estado** (art. 91.1); los ayuntamientos liquidan y recaudan (art. 91.2).
    - **IVTM**: lo gestiona el ayuntamiento del **domicilio que conste en el permiso de circulación** (art. 97) y puede exigirse en **autoliquidación** (art. 98). Al terminar el periodo voluntario, los ayuntamientos «comunicarán informáticamente al Registro de Vehículos de la Dirección General de Tráfico el impago». Tráfico no tramita el cambio de titularidad sin acreditar el pago del año anterior (art. 99).
- **Cobro periódico por recibo**:
    - Notificada la liquidación del alta en el registro, padrón o matrícula, «podrán notificarse colectivamente las sucesivas liquidaciones mediante edictos que así lo adviertan» (art. 102.3 LGT).
    - Si su norma no fija otro plazo, el periodo voluntario de estas deudas va del **1 de septiembre al 20 de noviembre**. La Administración puede modificarlo siempre que el plazo no sea **inferior a dos meses** (art. 62.3 LGT).
    - Con ello el sistema genera el **calendario fiscal**, las listas cobratorias y los recibos, incluidos los domiciliados.
- **Delegación (art. 7 TRLHL)**:
    - Las entidades locales pueden delegar en la comunidad autónoma o en otras entidades locales en cuyo territorio estén integradas (en la práctica, la diputación) «las facultades de gestión, liquidación, inspección y recaudación tributarias».
    - El acuerdo es del **Pleno**, fija el alcance de la delegación y se publica en los boletines oficiales de la provincia y de la comunidad autónoma.
    - La delegación la ampara el art. 106.3 LRBRL; la asistencia de la diputación en la recaudación de los municipios de menos de 20.000 habitantes es otra cosa, la del art. 36.1.f.
- **Municipios de gran población (art. 135 LRBRL)**:
    - El Pleno puede crear un **órgano de gestión tributaria** para «una gestión integral del sistema tributario municipal».
    - Sus competencias mínimas: la gestión, liquidación, inspección, recaudación y revisión de los actos tributarios; la recaudación ejecutiva de los demás ingresos de derecho público; los expedientes sancionadores tributarios; y el análisis de la política de ingresos.
    - Las reclamaciones económico-administrativas las resuelve el órgano del art. 137, que en València es el **Jurat Tributari** (tema [96](96-bases-del-regimen-local-ley-7-1985.md)).
- **Módulos típicos del sistema**:
    - censos y padrones fiscales;
    - liquidaciones y autoliquidaciones;
    - beneficios fiscales;
    - emisión de recibos y cartas de pago;
    - recaudación voluntaria (entidades colaboradoras, domiciliaciones y pago en la sede electrónica);
    - recaudación ejecutiva (providencias de apremio y embargos);
    - inspección;
    - contabilización de los ingresos en el SICAL.

## Gestión del padrón municipal de habitantes

El padrón es «el registro administrativo donde constan los vecinos de un municipio» y sus datos prueban la residencia y el domicilio habitual (art. 53.1 del RD 1690/1986, Reglamento de Población y Demarcación Territorial de las Entidades Locales). Su régimen sustantivo (empadronamiento, vecindad, variaciones y bajas de oficio) se estudia en el tema [96](96-bases-del-regimen-local-ley-7-1985.md). Aquí interesa su gestión como sistema de información, que el **RD 141/2024** reformó para digitalizarla por completo.

- **Datos obligatorios (art. 57.1)**:
    - nombre y apellidos, sexo, nacionalidad, y lugar y fecha de nacimiento;
    - **domicilio habitual**, con la **referencia catastral** cuando el domicilio la tenga (novedad del RD 141/2024);
    - **DNI** o, para los extranjeros, el **número de identidad de extranjero** o, en su defecto, el del documento de identidad o pasaporte;
    - certificado o título escolar o académico;
    - y los datos necesarios para el **censo electoral**.
- **Datos voluntarios (art. 57.2)**: representante a efectos padronales, **teléfono** y **correo electrónico**.
- **Gestión electrónica (art. 60)**:
    - La formación, actualización, revisión y custodia corresponden al **ayuntamiento**.
    - «Todos los padrones municipales se gestionarán por medios electrónicos y estarán interconectados con el Instituto Nacional de Estadística».
    - Las diputaciones (y las comunidades autónomas uniprovinciales, diputaciones forales, cabildos y consejos insulares) **apoyan técnica y económicamente** a los municipios. **Asumen la gestión informatizada** de los padrones de los que, por su menor capacidad económica y de gestión, no la lleven efectivamente.
    - El ayuntamiento conserva las hojas de inscripción y las comunicaciones de los vecinos, o reproducciones que garanticen su autenticidad.
- **Hoja padronal (arts. 58-59)**: en formato físico o electrónico, firmada de forma manuscrita o con los sistemas de firma admitidos en la tramitación electrónica por todos los vecinos que figuren en ella.
- **Certificaciones y volantes (art. 61)**:
    - Las **certificaciones** son documento público y fehaciente. Las expide la persona que ocupe la **Secretaría** o el habilitado nacional que la sustituya, y pueden expedirse por **actuación administrativa automatizada** (arts. 41-42 de la Ley 40/2015 y RD 203/2021).
    - Los **volantes** son «documentos de carácter puramente informativo», sin las formalidades de las certificaciones. Quien modifique sus datos puede pedir uno en cuanto se haya hecho el cambio.
- **Actualización continua (arts. 62-69)**:
    - Los organismos de la AGE remiten las variaciones de los datos obligatorios a cada ayuntamiento **a través del INE** (art. 63):
        - el **Registro Civil**, los nacimientos, defunciones y cambios de nombre, apellidos, sexo y nacionalidad;
        - el **Ministerio del Interior**, las expediciones de DNI y de documentos de extranjeros;
        - ambos, **al menos mensualmente**;
        - los ministerios de educación y universidades, las titulaciones;
        - el **Catastro**, las referencias catastrales.
    - Los ayuntamientos remiten al INE sus variaciones «por medio de un sistema de intercambio de datos en tiempo real» (art. 65). El INE les comunica las **discrepancias** detectadas, y la **Oficina del Censo Electoral**, las variaciones del censo (art. 66).
    - Si un ayuntamiento no mantiene actualizado su padrón, el INE, previo informe del Consejo de Empadronamiento, puede acudir a la **ejecución sustitutoria** (art. 62).
    - Cada vecino debe poder conocer sus datos padronales **al menos una vez cada cinco años** (art. 69.3).
- **Transición al tiempo real (DT única del RD 141/2024)**:
    - Se fijó un periodo transitorio **hasta el 31 de agosto de 2026** para implantar el intercambio en tiempo real.
    - Mientras no esté habilitado, se mantienen los intercambios **mensuales**. Cuando el INE lo habilite, los ayuntamientos se incorporan **progresivamente**, coexistiendo ambos sistemas.
    - La **referencia catastral** del domicilio se incorpora de forma paulatina y es obligatoria desde la puesta en marcha del sistema en tiempo real.
    - El censo electoral se sigue actualizando mensualmente hasta que se reforme la LOREG.
- **Financiación**: la **Orden TER/1235/2023** convocó **64.117.540 euros** del PRTR (Componente 11, Inversión 3), en concurrencia no competitiva.
    - Beneficiarias: las diputaciones, cabildos, consejos insulares y comunidades autónomas uniprovinciales.
    - Destinatarios: los municipios de **menos de 20.000 habitantes**.
    - Actuaciones financiadas: una base de datos de viviendas **unificada a nivel nacional**, identificadas por su referencia catastral, y el nuevo sistema de intercambio en tiempo real con el INE.
- **Instrucciones técnicas (Resolución de 17 de febrero de 2020, modificada en 2023)**: las dictan el INE y la Dirección General de Cooperación Autonómica y Local a propuesta del Consejo de Empadronamiento. Son anteriores al RD 141/2024 y describen todavía el envío mensual.
    - El padrón lo forman la relación de **hojas padronales** y un **fichero informatizado de inscritos**, con los diseños de registro publicados en la aplicación web del INE **IDA-Padrón**.
    - Las hojas padronales se conservan, como norma general, «por un período no inferior a 100 años», porque el vecino puede pedir certificaciones de todo su historial.
    - Las variaciones se remiten por IDA-Padrón con certificados electrónicos reconocidos por **@firma**, con un fichero de **parte negativo** cuando no hay movimientos.
    - El INE devuelve al ayuntamiento:
        - los errores;
        - las discrepancias con otros padrones;
        - las altas en otros municipios, para que el de procedencia dé la baja;
        - los nacimientos y defunciones del Registro Civil;
        - los **preavisos de caducidad**.
    - Todas las comunicaciones de padrón y censo electoral usan una **tabla de caracteres normalizada**, en códigos EBCDIC y ASCII.
    - Las inscripciones de extranjeros no comunitarios sin autorización de residencia de larga duración (**ENCSARP**) se renuevan **cada dos años** (art. 54 bis); el INE avisa de las que caducan en **tres meses**.
- **Revisión anual y cifras oficiales (arts. 81-82)**:
    - Los ayuntamientos aprueban la revisión de su padrón **con referencia al 1 de enero** de cada año y remiten al INE la cifra resultante y una copia de los datos obligatorios.
    - Si el INE no está de acuerdo, formula **reparos** y, sin acuerdo, somete la discrepancia al Consejo de Empadronamiento.
    - El **Presidente del INE**, con el informe favorable del Consejo, eleva al Gobierno la propuesta de **cifras oficiales de población**, que se aprueban por **real decreto** publicado en el BOE.
- **Cesión de datos e interoperabilidad (arts. 53.2 y 83)**:
    - Los datos obligatorios se ceden a otras Administraciones **sin consentimiento** del afectado «solamente cuando les sean necesarios para el ejercicio de sus respectivas competencias, y exclusivamente para asuntos en los que la residencia o el domicilio sean datos relevantes». Los datos voluntarios no se ceden salvo en los supuestos legales.
    - Los ayuntamientos pueden **consultar por vía telemática** los datos de sus padrones que obran en el INE.
    - Los datos del INE «no podrán servir de base para la expedición de certificaciones o volantes de empadronamiento», pero sí pueden usarse en las **plataformas de intermediación de datos** y en la **pasarela digital única** de la Unión Europea para acreditar la residencia. Se ponen además a disposición del ciudadano en la **Carpeta Ciudadana** del sector público estatal.
    - Para el propio ayuntamiento, el padrón es un dato en su poder que no necesita intermediación (tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md)). En la Comunitat Valenciana, la PAI ofrece a las entidades locales un servicio de consulta unificada del padrón (tema [82](82-administracion-electronica-y-plataformas-de-la-generalitat.md)).
- **Consejo de Empadronamiento (arts. 84-87)**: órgano colegiado de colaboración entre la AGE y los entes locales en materia padronal, adscrito al **Ministerio de Economía, Comercio y Empresa**, con **Secciones Provinciales**.
    - **Funciones (art. 85)**:
        - elevar a la decisión del **Presidente del INE** una **propuesta vinculante** de resolución de las discrepancias;
        - informar **con carácter vinculante** las cifras oficiales de población y las altas y bajas de oficio;
        - informar preceptivamente la acción sustitutoria del INE;
        - y proponer las instrucciones técnicas de gestión, «en especial sobre intercambios de información entre Administraciones, precisión de datos padronales, operaciones de muestreo, operaciones de actualización, sistemas de gestión, normalización de documentos».
    - **Composición (art. 86)**: lo preside el **Presidente del INE**. Son vocales:
        - **dos** del INE y **uno** de la Oficina del Censo Electoral;
        - **uno** del Ministerio de Política Territorial y Memoria Democrática y **uno** del Ministerio de Asuntos Exteriores;
        - **uno** de la **Secretaría General de Administración Digital** (suprimida en 2025; la sucede la **Agencia Estatal de Administración Digital**, que se subroga en sus funciones según el RD 1118/2024);
        - y **siete** de las entidades locales, designados por la asociación de municipios de ámbito estatal con mayor implantación.
    - La secretaría la ejerce un funcionario del INE.

## Gestión de recursos humanos

El sistema de recursos humanos une la gestión administrativa del personal con la nómina y con las obligaciones frente a la Seguridad Social y la Hacienda estatal. Su base legal es el registro de personal que cada Administración debe tener. El régimen del personal local (plantilla, RPT y retribuciones) se estudia en el tema [98](98-personal-al-servicio-de-las-entidades-locales.md).

- **Registro de personal y gestión integrada (art. 71 TREBEP)**:
    - «Cada Administración Pública constituirá un Registro» en el que se inscriben los datos de su personal, y que puede incluir información agregada del resto de su sector público.
    - Los contenidos mínimos comunes y los criterios de **intercambio homogéneo** entre Administraciones se fijan **mediante convenio de Conferencia Sectorial**.
    - Las Administraciones «impulsarán la gestión integrada de recursos humanos».
    - Si las entidades locales no tienen suficiente capacidad financiera o técnica, la AGE y las comunidades autónomas **cooperarán** con ellas.
- **Plantilla y relación de puestos de trabajo**:
    - La plantilla se aprueba **anualmente, a través del presupuesto**, y comprende todos los puestos reservados a funcionarios, personal laboral y eventual (art. 90.1 LRBRL).
    - Las corporaciones forman también la **relación de puestos de trabajo** (art. 90.2).
    - Aprobadas, se remite copia a la AGE y a la comunidad autónoma en **treinta días** y se publican íntegras en el **Boletín Oficial de la Provincia** junto con el resumen del presupuesto (art. 127 TRRL).
    - El sistema las mantiene como datos maestros de puestos.
- **Módulos típicos**:
    - **expediente personal**: situaciones administrativas, antigüedad, formación, vacaciones y permisos;
    - **estructura de puestos**, con sus complementos;
    - **nómina**: retribuciones básicas y complementarias (RD 861/1986), retenciones del IRPF y cotizaciones a la Seguridad Social;
    - **control horario** y turnos;
    - **selección y provisión**, con las convocatorias y bolsas publicadas en la sede electrónica;
    - **portal del empleado**: nóminas, certificados y solicitudes;
    - prevención de riesgos laborales y acción social.
- **Integraciones**:
    - con la **contabilidad**: la nómina genera la operación de gasto del capítulo 1 del presupuesto (gastos de personal);
    - con la **Tesorería General de la Seguridad Social** (cotizaciones por el **Sistema RED**) y con la **AEAT** (retenciones del IRPF);
    - con el gestor de expedientes y el portafirmas para los actos de personal.
- **Protección de datos**: el sistema trata **categorías especiales de datos**, como la salud en las bajas o la afiliación sindical (art. 9 del RGPD, tema [53](53-proteccion-de-datos-personales.md)).

## Gestión de subvenciones: la BDNS

La actividad de fomento local (tema [100](100-formas-de-actividad-y-servicios-publicos-locales.md)) se apoya en un sistema de gestión de subvenciones conectado con la **Base de Datos Nacional de Subvenciones (BDNS)**. La BDNS es a la vez base de datos y canal obligatorio de publicidad de convocatorias y concesiones.

- **Régimen aplicable** (tema [100](100-formas-de-actividad-y-servicios-publicos-locales.md)):
    - A las entidades locales se les aplica la **LGS entera**, también sus preceptos no básicos (DF 1.ª.2).
    - Las bases reguladoras se aprueban en el marco de las **bases de ejecución del presupuesto**, mediante una **ordenanza general de subvenciones** o una específica (art. 17.2).
    - El control financiero corresponde a los órganos o funcionarios que lo tengan atribuido en la corporación (DA 14.ª).
- **La BDNS en la LGS**:
    - **Finalidades (art. 20.1)**: «promover la transparencia, servir como instrumento para la planificación de las políticas públicas, mejorar la gestión y colaborar en la lucha contra el fraude de subvenciones y ayudas públicas».
    - **Contenido (art. 20.2)**: bases reguladoras, convocatoria, programa y crédito presupuestario, objeto, beneficiarios, importes otorgados y percibidos, reintegros y sanciones. Recoge también a quienes tengan **prohibido obtener subvenciones** (art. 13.2.a y h), inscritos hasta **10 años** después de terminar la prohibición.
    - **Administración (art. 20.3)**: la **IGAE** es el órgano responsable de su «administración y custodia».
    - **Responsable del suministro en las entidades locales (art. 20.4.c)**: «la Intervención u órgano que designe la propia Entidad Local».
    - **Carácter reservado (art. 20.5)**: solo se cede para los fines tasados por la ley, como la colaboración con otras Administraciones y con la Administración tributaria, la persecución de delitos o el Tribunal de Cuentas.
    - **Sistema nacional de publicidad (arts. 18.1 y 20.8)**:
        - La BDNS «operará como sistema nacional de publicidad de subvenciones».
        - En el sector público local, la BDNS da traslado al **diario oficial** del **extracto** de la convocatoria, cuya publicación es **gratuita**.
        - «La convocatoria de una subvención sin seguir el procedimiento indicado será causa de anulabilidad de la convocatoria».
- **El RD 130/2019, que la desarrolla**:
    - **Ámbito (arts. 2-3)**: todas las subvenciones y ayudas públicas, incluidas las ayudas en especie, los avales y préstamos y los beneficios fiscales que sean ayuda de Estado. Abarca las que conceden la AGE, las comunidades autónomas, «Las entidades que integran la administración local» y el sector público institucional, aunque se tramiten mediante entidades colaboradoras.
    - **Qué se suministra (art. 4)**: normativa reguladora, convocatorias, concesiones, pagos, resoluciones de reintegro y sanciones firmes. No es obligatorio suministrar las concesiones cuando el importe anual otorgado por el mismo órgano a un mismo beneficiario **no supere 100 euros**.
    - **Cómo y cuándo (art. 5)**: a través del sistema de información que determine la IGAE y con **certificado electrónico reconocido**. Las concesiones, pagos, reintegros y sanciones se suministran de forma continuada y, en todo caso, «antes de que finalice el mes siguiente al de su producción».
    - **Convocatoria (art. 6)**:
        - Aprobadas las bases, «Inmediatamente antes de la publicación en el oportuno diario oficial» se registra la información en la BDNS con el texto de la convocatoria y su **extracto**.
        - La BDNS pone el extracto a disposición del diario oficial firmado con **sello electrónico**, y «La eficacia de la convocatoria se producirá con la publicación del extracto en el diario oficial».
        - El extracto debe incluir el **código de identificación** asignado por la BDNS.
        - Los datos se transmiten en formatos de la NTI de **Catálogo de estándares**.
    - **Publicidad (art. 7)**:
        - Se hace en [www.subvenciones.gob.es](https://www.subvenciones.gob.es) y [www.infosubvenciones.es](https://www.infosubvenciones.es).
        - Las concesiones permanecen publicadas los **cuatro años** naturales siguientes al de la concesión; las otorgadas a **personas físicas**, solo el año de concesión y el siguiente.
        - No se publican las que revelen **categorías especiales de datos** ni las que agraven la situación de personas en protección especial, como las **víctimas de violencia de género**.
        - La BDNS ofrece a las entidades locales que lo soliciten un **servicio particularizado** de publicación para cumplir la Ley 19/2013 (art. 7.9).
    - **Cesión (art. 8.3)**: la IGAE atiende las peticiones de información más frecuentes de otros órganos a través de la **Plataforma de Intermediación de Datos**.
    - **Responsabilidades (arts. 9-10)**:
        - Cada Administración mantiene la propiedad y la responsabilidad de lo que suministra.
        - En cada entidad local se designa un **único Administrador Institucional**, interlocutor con la IGAE.
        - La falta de suministro es **infracción** administrativa del art. 57 LGS.
- **El sistema municipal de subvenciones** gestiona el ciclo completo:
    - plan estratégico, bases y convocatoria, con su registro en la BDNS;
    - solicitudes por la sede electrónica;
    - comprobación de requisitos, como estar al corriente con la AEAT y la Seguridad Social mediante la PID (tema [63](63-infraestructuras-y-servicios-comunes-de-interoperabilidad.md));
    - valoración, concesión y pago;
    - **justificación**, control y **reintegro**.
    - Se integra con la BDNS por servicios web y con el SICAL para las fases contables del gasto.

## Aplicación en el Ayuntamiento de València

El **Reglamento Orgánico de Gobierno y Administración** (ROGA, 2021) reparte entre varios órganos directivos las funciones que soportan estos sistemas.

- **Intervención General (art. 54)**: ejerce el control y fiscalización interna de la gestión económico-financiera y presupuestaria «en su triple acepción de función interventora, función de control financiero y función de control de eficacia», con «completo acceso a la contabilidad».
- **Intervención de Contabilidad y Presupuestos (art. 55)**:
    - «Llevar y desarrollar la contabilidad financiera y la de ejecución del presupuesto de la Entidad Local».
    - «Formar la Cuenta General de la Entidad Local».
    - «Organizar un adecuado sistema de archivo y conservación de toda la documentación e información contable».
    - «La gestión del registro contable de facturas y su seguimiento para cumplir los objetivos que determine la normativa sobre morosidad».
    - Prepara además el proyecto de **presupuesto general**.
- **Tesorería Municipal (art. 56)**: ejerce «Las funciones de Tesorería, Gestión Tributaria y Recaudación». Dirige los servicios de gestión tributaria y recaudación, autoriza los **pliegos de cargo de valores** y dicta las **providencias de apremio**.
- **Juntas Municipales de Distrito (art. 72)**: pueden asumir la ordenación del **Registro General de Entrada**, la «supervisión y corrección del censo y del padrón municipal y emisión de certificados» y la gestión de la información tributaria.

## Fuentes {.unnumbered .unlisted}

- Real Decreto 1690/1986, de 11 de julio, por el que se aprueba el Reglamento de Población y Demarcación Territorial de las Entidades Locales: arts. 53-54 bis, 57-69, 81-87 (texto consolidado, última modificación 7 de febrero de 2024; coincidente con el BOE a 3 de octubre de 2026).
- Real Decreto 141/2024, de 6 de febrero, por el que se modifica el Reglamento de Población y Demarcación Territorial de las Entidades Locales: disposición transitoria única (BOE de 7 de febrero de 2024).
- Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital: disposición adicional primera y disposición final primera (texto consolidado, última modificación 12 de junio de 2026).
- Resolución de 17 de febrero de 2020, de la Presidencia del Instituto Nacional de Estadística y de la Dirección General de Cooperación Autonómica y Local, por la que se dictan instrucciones técnicas a los Ayuntamientos sobre la gestión del Padrón municipal: apartados 6 y 9-13 (texto consolidado, última modificación 8 de febrero de 2023).
- Orden TER/1235/2023, de 15 de noviembre, de subvenciones para la transformación digital y modernización de los sistemas de gestión del padrón municipal de las entidades locales, en el marco del Plan de Recuperación, Transformación y Resiliencia: arts. 1, 3 y 5 (BOE).
- Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local: arts. 36.1.f, 90, 106 y 135 (texto consolidado, última modificación 3 de junio de 2026).
- Real Decreto Legislativo 2/2004, de 5 de marzo, por el que se aprueba el texto refundido de la Ley Reguladora de las Haciendas Locales: arts. 7, 59, 77, 91, 97-99, 200-204, 208-213, 218 y 223 (texto consolidado, última modificación 3 de junio de 2026; el Real Decreto-ley 26/2026, que modificaba los arts. 72 y 107.4, fue derogado por el Congreso por Resolución de 2 de octubre de 2026). Ley 11/2020, de 30 de diciembre, de Presupuestos Generales del Estado para el año 2021, disposición final 19.ª (versiones del art. 212 en la API de datos abiertos del BOE).
- Orden HAP/1781/2013, de 20 de septiembre, por la que se aprueba la Instrucción del modelo normal de contabilidad local: preámbulo y reglas 1, 3 y 11-51 (texto consolidado, última modificación 3 de agosto de 2021).
- Orden HAP/1782/2013, de 20 de septiembre, por la que se aprueba la Instrucción del modelo simplificado de contabilidad local: regla 1 (texto consolidado, última modificación 22 de diciembre de 2018).
- Orden EHA/4040/2004, de 23 de noviembre, por la que se aprueba la Instrucción del modelo básico de contabilidad local: reglas 1, 4 y 7 (texto consolidado, última modificación 3 de octubre de 2013).
- Ley 25/2013, de 27 de diciembre, de impulso de la factura electrónica y creación del registro contable de facturas en el Sector Público: arts. 6 y 8-12 y disposición adicional 5.ª (texto consolidado, última modificación 13 de junio de 2015).
- Real Decreto 424/2017, de 28 de abril, por el que se regula el régimen jurídico del control interno en las entidades del Sector Público Local: arts. 6, 15, 33, 36-38 y disposición adicional 7.ª (texto consolidado, sin modificaciones).
- Ley 58/2003, de 17 de diciembre, General Tributaria: arts. 62.3 y 102.3 (texto consolidado, última modificación 21 de diciembre de 2024).
- Real Decreto Legislativo 781/1986, de 18 de abril, texto refundido de las disposiciones legales vigentes en materia de Régimen Local: art. 127 (texto consolidado, última modificación 9 de noviembre de 2024).
- Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido de la Ley del Estatuto Básico del Empleado Público: art. 71 (texto consolidado, última modificación 30 de julio de 2025).
- Ley 38/2003, de 17 de noviembre, General de Subvenciones: arts. 17.2, 18, 20, disposición adicional 14.ª y disposición final 1.ª (texto consolidado, última modificación 2 de agosto de 2024).
- Real Decreto 130/2019, de 8 de marzo, por el que se regula la Base de Datos Nacional de Subvenciones y la publicidad de las subvenciones y demás ayudas públicas: arts. 2-10 (texto consolidado, última modificación 22 de marzo de 2021, por la Sentencia del Tribunal Constitucional 37/2021, que anula un inciso del art. 3.1 sin efecto en el ámbito local).
- Ley Orgánica 5/1982, de 1 de julio, de Estatuto de Autonomía de la Comunitat Valenciana: art. 39 (texto consolidado, última modificación 28 de diciembre de 2022).
- Reglamento Orgánico de Gobierno y Administración del Ayuntamiento de València, aprobado el 28 de enero de 2021 (texto con la modificación de 2023, sede.valencia.es): arts. 54-56 y 72.
- Plataforma de Rendición de Cuentas de las Entidades Locales (rendiciondecuentas.es), consultada en octubre de 2026.
