# Historia clínica digital: HCDSNS, MyHealth@EU y el Espacio Europeo de Datos de Salud

La historia clínica de un paciente se genera en muchos centros y servicios de salud distintos. Para que le siga allá donde sea atendido existen tres capas de interoperabilidad: la **HCDSNS** entre comunidades autónomas, **MyHealth@EU** entre Estados miembros de la UE y, como marco de futuro, el **Espacio Europeo de Datos de Salud (EEDS)**, que convierte ese intercambio en un derecho exigible y regula también el uso secundario de los datos.

## La Historia Clínica Digital del SNS (HCDSNS)

El proyecto HCDSNS, coordinado por el **Ministerio de Sanidad** con las comunidades autónomas, permite que ciudadanos y profesionales accedan a la documentación clínica relevante de un paciente **con independencia de la comunidad autónoma donde se generó**.

- **Base legal**: el **art. 56 de la Ley 16/2003**, de cohesión y calidad del SNS («Intercambio de información en salud»): el Ministerio «coordinará los mecanismos de intercambio electrónico de información clínica y de salud individual, previamente acordados con las comunidades autónomas», para el acceso del interesado y de los profesionales «en los términos estrictamente necesarios». Se apoya en la **tarjeta sanitaria individual** (art. 57) y su base de datos de población protegida para identificar unívocamente al paciente.

**Texto consolidado de la Ley 16/2003 a 31 de octubre de 2024.**

- **Objetivos**: garantizar la continuidad y la calidad asistencial (evitar pruebas y procedimientos repetidos), facilitar el acceso a la información clínica dondequiera que se haya generado y proteger la privacidad (solo profesionales autorizados, con trazabilidad completa de los accesos).
- **Arquitectura descentralizada**: cada comunidad autónoma **custodia sus propios datos clínicos**; todas se interconectan a través de un **nodo central** gestionado por el Ministerio (sobre la red privada del SNS). El nodo central **no almacena información clínica**: guarda únicamente **índices de referencia** que localizan en qué servicio de salud hay documentación de cada paciente y actúa de intermediario en las consultas.
- **Contenidos**: los informes clínicos normalizados del **RD 1093/2010** (tema 84): la **historia clínica resumida** como pieza central, más los informes de alta, de consultas externas, de urgencias, de atención primaria, de resultados de laboratorio, de imagen, de otras pruebas diagnósticas y de cuidados de enfermería.
- **Acceso**: el ciudadano accede desde la sede electrónica de su servicio de salud (con certificado electrónico o Cl@ve) y puede **consultar quién ha accedido** a sus informes y ejercer la **ocultación** de aquellos que no desee mostrar; el profesional solo accede en el marco de una atención sanitaria real y todo acceso queda registrado.

## La receta electrónica interoperable del SNS

La receta electrónica sustituye la prescripción en papel por una anotación en un repositorio electrónico que la farmacia consulta al dispensar. La **interoperabilidad de receta electrónica del SNS** extiende ese esquema a todo el territorio: un paciente puede **retirar su medicación en cualquier farmacia de España**, aunque la receta se haya emitido en otra comunidad autónoma.

- **Funcionamiento**: la farmacia identifica al paciente por su **tarjeta sanitaria**; el sistema localiza su comunidad emisora a través del **nodo central de intercambio** del SNS, recupera el plan de tratamiento vigente y registra la dispensación en origen.
- **Marco normativo**: el **RD 1718/2010, sobre receta médica y órdenes de dispensación**, regula la receta médica pública y privada, en papel y electrónica. <!-- TODO: verificar consolidado del RD 1718/2010 (no está en references/) -->
- **Cobertura**: **todas las comunidades autónomas** (e INGESA, Ceuta y Melilla) están integradas en el intercambio. <!-- TODO: verificar la fecha de compleción (2021) y la situación de las mutualidades (MUFACE, ISFAS, MUGEJU) -->

## MyHealth@EU (eHDSI): el intercambio transfronterizo

**MyHealth@EU** es la marca de los servicios europeos de salud digital transfronterizos, construidos sobre la infraestructura **eHDSI** (*eHealth Digital Service Infrastructure*) de la Comisión Europea y coordinados por la **red de sanidad electrónica** (*eHealth Network*, creada en 2011 al amparo del **art. 14 de la Directiva 2011/24/UE**, de asistencia sanitaria transfronteriza).

- **Servicios en producción**:
    - **Receta electrónica transfronteriza** (*ePrescription/eDispensation*): retirar en una farmacia de otro Estado miembro la medicación prescrita electrónicamente en el país de origen, con registro de la dispensación de vuelta.
    - **Historia clínica resumida** (*Patient Summary*): acceso del profesional de otro Estado miembro a los datos esenciales del paciente (alergias, medicación actual, problemas de salud, intervenciones) en su idioma, en encuentros asistenciales no programados.
- **Arquitectura**: cada Estado miembro despliega un **punto de contacto nacional de sanidad electrónica (NCPeH)** que traduce entre los sistemas nacionales y el formato europeo común (documentos **CDA** con perfiles IHE de intercambio entre comunidades, temas 86 y 87). En España el NCPeH lo opera el **Ministerio de Sanidad** (servicio «Mi Salud@UE»), conectado a la HCDSNS y a la receta interoperable del SNS.
- **Despliegue**: progresivo por países y por servicio; España fue de los primeros Estados en operar la receta transfronteriza. <!-- TODO: verificar en la revisión la lista actual de países conectados con España -->

## El Espacio Europeo de Datos de Salud (Reglamento (UE) 2025/327)

El **Reglamento (UE) 2025/327, de 11 de febrero de 2025, relativo al Espacio Europeo de Datos de Salud** (EEDS; modifica la Directiva 2011/24/UE y el Reglamento (UE) 2024/2847) es el primer espacio común europeo de datos sectorial. Convierte el intercambio de datos de salud en obligaciones jurídicas directamente aplicables, tanto para la asistencia (**uso primario**) como para la investigación y las políticas públicas (**uso secundario**).

**Publicado en el DOUE L de 5 de marzo de 2025 (texto original, sin modificaciones).**

- **Uso primario (Capítulo II)**: derechos de las personas sobre sus **datos de salud electrónicos personales**: acceso **inmediato y gratuito**, obtención de copia en el **formato europeo de intercambio de historiales médicos electrónicos**, inserción de datos y rectificación, portabilidad, restricción del acceso de los profesionales y conocimiento de los accesos realizados.
- **Categorías prioritarias de datos** (art. 14.1, literal):
    - a) las historias clínicas resumidas de los pacientes;
    - b) las recetas electrónicas;
    - c) las dispensaciones electrónicas;
    - d) los estudios de diagnóstico por imagen y los informes de imágenes correspondientes;
    - e) los resultados de pruebas diagnósticas, incluidos los resultados de laboratorio y otros resultados de diagnóstico e informes correspondientes, y
    - f) los informes de altas hospitalarias.
- **Sistemas de HCE (Capítulo III)**: los **sistemas de historiales médicos electrónicos** que traten categorías prioritarias deberán incorporar **componentes armonizados** de interoperabilidad y de registro, con autocertificación del fabricante y **marcado CE de conformidad**.
- **MyHealth@EU obligatorio**: los Estados miembros deberán conectarse a la infraestructura transfronteriza y ofrecer al menos las categorías prioritarias.
- **Uso secundario (Capítulo IV)**: los titulares de datos deberán poner a disposición datos de salud electrónicos (historias clínicas, registros, datos genómicos, reclamaciones…) para finalidades permitidas (investigación, innovación, salud pública, políticas, IA) y nunca para finalidades prohibidas (publicidad, primas de seguro, decisiones en perjuicio del interesado). El acceso se canaliza a través de **organismos de acceso a los datos de salud** nacionales, que emiten **permisos de datos** y solo entregan los datos **anonimizados o seudonimizados** dentro de **entornos de tratamiento seguros**; el ciudadano dispone de un derecho de **autoexclusión** (*opt-out*). La infraestructura transfronteriza de uso secundario es **HealthData@EU**.
- **Entrada en vigor y aplicación (art. 105)**: en vigor a los veinte días de su publicación en el DOUE; **aplicable a partir del 26 de marzo de 2027**, con un calendario escalonado:

| Fecha | Qué se aplica |
| --- | --- |
| **26-mar-2027** | Aplicación general del Reglamento |
| **26-mar-2029** | Derechos de uso primario para las categorías **a), b) y c)** del art. 14.1 y sus sistemas de HCE; Capítulo IV (uso secundario) con carácter general |
| **26-mar-2031** | Derechos de uso primario para las categorías **d), e) y f)** y sus sistemas de HCE; Capítulo III para sistemas ya en servicio |
| **26-mar-2035** | Art. 75, apartado 5 (últimas obligaciones de uso secundario) |

## Fuentes {.unnumbered .unlisted}

- Ley 16/2003, de 28 de mayo, de cohesión y calidad del Sistema Nacional de Salud (texto consolidado, última modificación 31 de octubre de 2024), art. 56 y 57.
- Reglamento (UE) 2025/327, de 11 de febrero de 2025, relativo al Espacio Europeo de Datos de Salud (DOUE L de 5 de marzo de 2025).
- Real Decreto 1093/2010 (contenidos de la HCDSNS; tema 84).
- Ministerio de Sanidad, páginas oficiales de la HCDSNS y de «Mi Salud@UE» / receta electrónica europea (consultadas en julio de 2026).
- Directiva 2011/24/UE, de asistencia sanitaria transfronteriza (art. 14, red de sanidad electrónica).
