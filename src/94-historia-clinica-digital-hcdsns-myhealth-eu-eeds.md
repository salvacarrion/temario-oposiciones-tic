# Historia clínica digital: HCDSNS, MyHealth@EU y el Espacio Europeo de Datos de Salud

La historia clínica de un paciente se genera en muchos centros y servicios de salud distintos. Para que le siga allá donde sea atendido existen tres capas de interoperabilidad: la **HCDSNS** entre comunidades autónomas, **MyHealth@EU** entre Estados miembros de la UE y, como marco de futuro, el **Espacio Europeo de Datos de Salud (EEDS)**, que convierte ese intercambio en un derecho exigible y regula también el uso secundario de los datos.

## La Historia Clínica Digital del SNS (HCDSNS)

El proyecto HCDSNS, coordinado por el **Ministerio de Sanidad** con las comunidades autónomas, permite que ciudadanos y profesionales accedan a la documentación clínica relevante de un paciente **con independencia de la comunidad autónoma donde se generó**.

- **Base legal**: el **art. 56 de la Ley 16/2003**, de cohesión y calidad del SNS («Intercambio de información en salud»): el Ministerio «coordinará los mecanismos de intercambio electrónico de información clínica y de salud individual, previamente acordados con las comunidades autónomas», para el acceso del interesado y de los profesionales «en los términos estrictamente necesarios». Se apoya en la **tarjeta sanitaria individual** (art. 57) y su base de datos de población protegida para identificar unívocamente al paciente.

**Texto consolidado de la Ley 16/2003 a 31 de octubre de 2024.**

- **Objetivos**: garantizar la continuidad y la calidad asistencial (evitar pruebas y procedimientos repetidos), facilitar el acceso a la información clínica dondequiera que se haya generado y proteger la privacidad (solo profesionales autorizados, con trazabilidad completa de los accesos).
- **Arquitectura descentralizada**: cada comunidad autónoma **custodia sus propios datos clínicos**; todas se interconectan a través de un **nodo central** gestionado por el Ministerio (sobre la red privada del SNS). El nodo central **no almacena información clínica**: guarda únicamente **índices de referencia** que localizan en qué servicio de salud hay documentación de cada paciente y actúa de intermediario en las consultas.
- **Contenidos**: los informes clínicos normalizados del **RD 1093/2010** (tema [89](89-documentacion-clinica-normalizada.md)): la **historia clínica resumida** como pieza central, más los informes de alta, de consultas externas, de urgencias, de atención primaria, de resultados de laboratorio, de imagen, de otras pruebas diagnósticas y de cuidados de enfermería.
- **Acceso**: el ciudadano accede desde la sede electrónica del **Ministerio de Sanidad** (servicio HCDSNS y **Carpeta Ciudadana**) o desde la de su servicio de salud, identificándose con certificado electrónico o Cl@ve; puede **consultar quién ha accedido** a sus informes y ejercer la **ocultación** de aquellos que no desee mostrar; el profesional solo accede en el marco de una atención sanitaria real y todo acceso queda registrado.
- **Despliegue**: es progresivo y desigual por comunidad autónoma y por tipo de informe (no todas publican todos los documentos del RD 1093/2010); el Ministerio mantiene un mapa de situación con los informes disponibles en cada servicio de salud.

## La receta electrónica interoperable del SNS

La receta electrónica sustituye la prescripción en papel por una anotación en un repositorio electrónico que la farmacia consulta al dispensar. La **interoperabilidad de receta electrónica del SNS** extiende ese esquema a todo el territorio: un paciente puede **retirar su medicación en cualquier farmacia de España**, aunque la receta se haya emitido en otra comunidad autónoma.

### Marco normativo: el RD 1718/2010

El **RD 1718/2010, de 17 de diciembre, sobre receta médica y órdenes de dispensación** regula la receta médica pública y privada, en soporte papel y electrónico, y las órdenes de dispensación (el documento equivalente de los profesionales enfermeros). Su **Capítulo IV** es el de la receta médica electrónica oficial del SNS.

**Texto consolidado a 23 de diciembre de 2015.**

- **Ámbito (art. 2)**: la asistencia sanitaria y atención farmacéutica del SNS, incluidos los regímenes especiales de **MUFACE**, **ISFAS** y **MUGEJU**, y las entidades y consultas privadas. La receta médica «es válida en todo el territorio nacional» y «garantizará que el tratamiento prescrito pueda ser dispensado al paciente en cualquier oficina de farmacia del territorio nacional».
- **Interoperabilidad (art. 7.2)**: para garantizarla entre servicios de salud, las recetas electrónicas de cada Administración sanitaria deben incorporar **necesariamente** el **código identificador unívoco de usuarios del SNS** y, **con carácter exclusivo**, el código de identificación del medicamento o producto sanitario y los parámetros del tratamiento «que figuren en el **Nomenclátor oficial de productos farmacéuticos del SNS**».
- **Custodia (art. 7.4)**: las Administraciones sanitarias públicas son las responsables de la gestión de los sistemas de receta electrónica y garantizan la custodia de las bases de datos de prescripción y dispensación.
- **Plazo de validez (art. 10)**: **diez días naturales** para la primera dispensación, desde la fecha de prescripción o del visado. En segundas y sucesivas, el plazo se inicia **diez días naturales antes** de la fecha de finalización de la medicación anterior y termina al finalizar el tratamiento.
- **Confidencialidad (art. 11)**: la información solo es accesible desde la oficina de farmacia a efectos de dispensación, **reside de forma permanente en los sistemas gestionados por las Administraciones sanitarias** y no puede almacenarse en repositorios ajenos una vez hecha la facturación.
- Lo modificó el **RD 81/2014**, por el que se establecen normas para garantizar la asistencia sanitaria transfronteriza (reconocimiento mutuo de recetas expedidas en otro Estado miembro).

### El proyecto RESNS: funcionamiento y despliegue

La **interoperabilidad de receta electrónica del SNS (RESNS)**, liderada y coordinada por el **Ministerio de Sanidad**, tiende puentes entre los sistemas autonómicos de receta.

- **Arquitectura**: un **nodo central (nodo SNS)** en el Ministerio actúa de plataforma de intercambio entre comunidades, con estándares **IHE/HL7** para la transmisión. Los datos de prescripción siguen residiendo en la comunidad emisora.
- **Servicios (cuatro)**: identificación del paciente, obtención del listado de medicamentos dispensables, obtención del detalle del medicamento a dispensar y consolidación de la dispensación. Ofrece además anulación de dispensaciones, bloqueo cautelar, confidencialidad y tratamiento activo.
- **Identificación y normalización**: el paciente por el código de identificación personal del SNS (**CIPSNS**) leído de la tarjeta sanitaria, más el código de su comunidad o proveedor (**CITE**); los centros por su código **REGCESS**; los medicamentos por **código nacional (CN)** o **SNOMED CT**.
- **Requisitos del proyecto**: adaptación de los sistemas autonómicos y del software de las oficinas de farmacia, unificación de funcionalidades y normalización de la información de la prescripción.
- **Cronología**: pilotaje iniciado en **2013** y finalizado en **julio de 2015** (primera dispensación en Canarias a una paciente extremeña); la interoperabilidad entre todas las comunidades se completó con la incorporación de la **Comunidad de Madrid en marzo de 2019**. Las mutualidades de opción pública (**MUFACE**, **ISFAS** y **MUGEJU**) se incorporaron entre **octubre de 2020** y **enero de 2023**.

## MyHealth@EU (eHDSI): el intercambio transfronterizo

**MyHealth@EU** (denominación oficial en español del Reglamento EEDS: **MiSalud@UE**) es la marca de los servicios europeos de salud digital transfronterizos, construidos sobre la infraestructura **eHDSI** (*eHealth Digital Service Infrastructure*) de la Comisión Europea y coordinados por la **red de sanidad electrónica** (*eHealth Network*), red voluntaria de autoridades de salud digital creada al amparo del **art. 14 de la Directiva 2011/24/UE**, de asistencia sanitaria transfronteriza.

- **Servicios en producción**:
    - **Receta electrónica transfronteriza** (*ePrescription/eDispensation*): retirar en una farmacia de otro Estado miembro la medicación prescrita electrónicamente en el país de origen, con registro de la dispensación de vuelta.
    - **Historia clínica resumida** (*Patient Summary*): acceso del profesional de otro Estado miembro a los datos esenciales del paciente (alergias, medicación actual, problemas de salud, intervenciones) en su idioma, en encuentros asistenciales no programados.
- **Arquitectura**: cada Estado miembro despliega un **punto de contacto nacional de sanidad electrónica (NCPeH)** que traduce entre los sistemas nacionales y el formato europeo común (documentos **CDA** con perfiles IHE de intercambio entre comunidades, temas [91](91-estandares-de-interoperabilidad-de-la-hce.md) y [92](92-normalizacion-en-informatica-sanitaria.md)). En España el NCPeH lo opera el **Ministerio de Sanidad** (servicio «MiSalud@UE»), conectado a la HCDSNS y a la receta interoperable del SNS. El Reglamento EEDS lo denomina **punto de contacto nacional para la salud digital** (art. 12).
- **Despliegue**: progresivo por países y por servicio (un Estado puede emitir, recibir o ambas cosas). España fue de los primeros en operar la receta transfronteriza, junto a Croacia, Estonia, Finlandia, Polonia y Portugal, y el número de Estados conectados crece de forma continua, por lo que conviene consultar el mapa de situación del Ministerio y el marco de seguimiento (KPI) de eHDSI antes de dar una lista por cerrada. En España el despliegue es también progresivo por comunidad autónoma: en **junio de 2023** se cerraron los acuerdos para incorporar a **todas las comunidades y ciudades autónomas** a ambos servicios.
- **Del voluntariado a la obligación**: eHDSI nació como infraestructura voluntaria. El Reglamento EEDS la convierte en obligatoria y traslada la gobernanza al **Consejo del EEDS**; en coherencia, su **art. 103 suprime el art. 14 de la Directiva 2011/24/UE con efectos a partir del 26 de marzo de 2031**, con lo que la red de sanidad electrónica se extingue como tal.

## El Espacio Europeo de Datos de Salud (Reglamento (UE) 2025/327)

El **Reglamento (UE) 2025/327, de 11 de febrero de 2025, relativo al Espacio Europeo de Datos de Salud** (EEDS; modifica la Directiva 2011/24/UE y el Reglamento (UE) 2024/2847) es el primero de los espacios sectoriales de datos previstos por la **Estrategia Europea de Datos (2020)** que llega a reglamento. Convierte el intercambio de datos de salud en obligaciones jurídicas directamente aplicables, tanto para la asistencia (**uso primario**) como para la investigación y las políticas públicas (**uso secundario**).

**Publicado en el DOUE L de 5 de marzo de 2025 (texto original, sin modificaciones).**

- **Uso primario (Capítulo II)**: derechos de las personas sobre sus **datos de salud electrónicos personales**: acceso **inmediato y gratuito**, obtención de copia en el **formato europeo de intercambio de historias clínicas electrónicas**, inserción de datos y rectificación, portabilidad, restricción del acceso de los profesionales y conocimiento de los accesos realizados.
- **Categorías prioritarias de datos** (art. 14.1, literal):
    - a) las historias clínicas resumidas de los pacientes;
    - b) las recetas electrónicas;
    - c) las dispensaciones electrónicas;
    - d) los estudios de diagnóstico por imagen y los informes de imágenes correspondientes;
    - e) los resultados de pruebas diagnósticas, incluidos los resultados de laboratorio y otros resultados de diagnóstico e informes correspondientes, y
    - f) los informes de altas hospitalarias.
- **Sistemas HCE (Capítulo III)**: los **sistemas de historia clínica electrónica** («sistemas HCE» en el Reglamento) que traten categorías prioritarias deberán incorporar **componentes armonizados** de interoperabilidad y de registro, con autocertificación del fabricante y **marcado CE de conformidad**. Los fabricantes de productos con elementos digitales que sean sistemas HCE demuestran la conformidad con el Reglamento de Ciberresiliencia por este mismo procedimiento (art. 104, que modifica el Reglamento (UE) 2024/2847).
- **MiSalud@UE obligatorio (art. 12)**: la Comisión establece la **plataforma central de interoperabilidad** y cada Estado miembro designa un **punto de contacto nacional para la salud digital**, pasarela organizativa y técnica conectada a los demás y a la plataforma central; su identidad se comunica a la Comisión **a más tardar el 26 de marzo de 2027**, y puede designarse dentro de la autoridad de salud digital.
- **Gobernanza**: cada Estado designa una o varias **autoridades de salud digital** (art. 19, también antes del **26 de marzo de 2027**), responsables del uso primario, que publican un **informe bienal de actividad** (art. 20); y uno o varios **organismos de acceso a datos de salud** para el uso secundario. A escala de la Unión, el **Consejo del EEDS** (art. 92) coordina y armoniza las prácticas.
- **Uso secundario (Capítulo IV)**: los titulares de datos deberán poner a disposición datos de salud electrónicos (historias clínicas, registros, datos genómicos, reclamaciones…) para finalidades permitidas (investigación, innovación, salud pública, políticas, IA) y nunca para finalidades prohibidas (publicidad, primas de seguro, decisiones en perjuicio del interesado). El acceso se canaliza a través de **organismos de acceso a datos de salud** nacionales, que emiten **permisos de datos** y solo entregan los datos **anonimizados o seudonimizados** dentro de **entornos de tratamiento seguros**; el ciudadano dispone de un derecho de **autoexclusión** (*opt-out*). La infraestructura transfronteriza de uso secundario es **DatosSalud@UE** (HealthData@EU).
- **Entrada en vigor y aplicación (art. 105)**: en vigor a los veinte días de su publicación en el DOUE; **aplicable a partir del 26 de marzo de 2027**, con un calendario escalonado:

| Fecha | Qué se aplica |
| --- | --- |
| **26-mar-2027** | Aplicación general del Reglamento (y designación de autoridades de salud digital y del punto de contacto nacional) |
| **26-mar-2029** | Derechos de uso primario para las categorías **a), b) y c)** del art. 14.1 y sus sistemas de HCE; Capítulo IV (uso secundario) con carácter general |
| **26-mar-2031** | Derechos de uso primario para las categorías **d), e) y f)** y sus sistemas de HCE; Capítulo III para sistemas ya en servicio |
| **26-mar-2035** | Art. 75, apartado 5 (últimas obligaciones de uso secundario) |

## Fuentes {.unnumbered .unlisted}

- Ley 16/2003, de 28 de mayo, de cohesión y calidad del Sistema Nacional de Salud (texto consolidado, última modificación 31 de octubre de 2024), arts. 56 y 57.
- Reglamento (UE) 2025/327, de 11 de febrero de 2025, relativo al Espacio Europeo de Datos de Salud (DOUE L de 5 de marzo de 2025), arts. 12, 14, 19, 20, 103, 104 y 105.
- Real Decreto 1718/2010, de 17 de diciembre, sobre receta médica y órdenes de dispensación (texto consolidado, última modificación 23 de diciembre de 2015), arts. 1, 2, 7, 10 y 11.
- Real Decreto 81/2014, de 7 de febrero, por el que se establecen normas para garantizar la asistencia sanitaria transfronteriza (modifica el RD 1718/2010).
- Real Decreto 1093/2010 (contenidos de la HCDSNS; tema [89](89-documentacion-clinica-normalizada.md)).
- Directiva 2011/24/UE, de asistencia sanitaria transfronteriza (art. 14, red de sanidad electrónica; suprimido con efectos desde el 26 de marzo de 2031).
- Ministerio de Sanidad, páginas oficiales de la HCDSNS, de la interoperabilidad de receta electrónica del SNS y de «MiSalud@UE» (consultadas en julio de 2026).
- SEIS (Sociedad Española de Informática de la Salud), Aula SEIS: «La receta electrónica interoperable en el SNS y en Europa», 2023 (arquitectura y servicios del RESNS).
