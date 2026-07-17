# Protección jurídica del software y licencias

En España y en la Unión Europea los programas de ordenador se protegen por **propiedad intelectual** (derechos de autor), no por patente. Este tema cubre el régimen del TRLPI y su Título VII, el control de legalidad del software en las organizaciones, los modelos de licencia (propietarias, libres y de código abierto) y el papel del software libre y la reutilización en las administraciones públicas.

## La propiedad intelectual y el programa de ordenador

El marco español es el **Real Decreto Legislativo 1/1996**, que aprueba el texto refundido de la **Ley de Propiedad Intelectual (TRLPI)**; incorpora la armonización europea de la **Directiva 2009/24/CE**, sobre la protección jurídica de programas de ordenador (versión codificada de la Directiva 91/250/CEE).

**Texto consolidado a 30 de marzo de 2022.**

- **Derechos de autor, no patente**: se protege la **expresión** del programa (el código), no las ideas ni los algoritmos; el Convenio Europeo de Patentes excluye los programas de ordenador «como tales» de la patentabilidad. La protección nace con la creación, sin necesidad de registro.
- **Doble contenido**: derechos **morales** (paternidad, integridad; irrenunciables e inalienables) y derechos de **explotación** (reproducción, distribución, comunicación pública y transformación; transmisibles).
- **Sede normativa**: el **Título VII del Libro I (arts. 95 a 104)** contiene el régimen específico de los programas de ordenador; en lo no previsto rige el resto de la ley (art. 95).

## El Título VII del TRLPI (arts. 95-104)

- **Art. 96. Objeto de la protección**: programa de ordenador es «toda secuencia de instrucciones o indicaciones destinadas a ser utilizadas, directa o indirectamente, en un sistema informático para realizar una función o una tarea o para obtener un resultado determinado, cualquiera que fuere su forma de expresión y fijación». La protección alcanza la **documentación preparatoria**, la técnica y los **manuales de uso**, y exige que el programa sea **original** (creación intelectual propia de su autor); quedan fuera las **ideas y principios**, incluidos los que fundamentan sus **interfaces**. No se protegen las versiones creadas para ocasionar **efectos nocivos**.
- **Art. 97. Titularidad**: es autor la persona natural o grupo que lo crea (o la jurídica en los casos previstos). Cuando un **trabajador asalariado** crea un programa en el ejercicio de sus funciones o por instrucciones del empresario, los derechos de explotación (fuente y objeto) corresponden **exclusivamente al empresario**, salvo pacto en contrario.
- **Art. 98. Duración**: autor persona natural, la regla general de la ley (**70 años** tras la muerte); persona jurídica, **70 años** desde el 1 de enero siguiente a la divulgación lícita (o creación, si no se divulga).
- **Art. 99. Derechos de explotación**: reproducción total o parcial (incluso la carga, presentación, ejecución o almacenamiento que la exijan), traducción/adaptación/transformación y distribución (incluido el alquiler). La cesión de uso se presume **no exclusiva e intransferible** y para las necesidades del usuario; la primera venta en la UE **agota** el derecho de distribución de esa copia (salvo el control del alquiler posterior).
- **Art. 100. Límites**: no requieren autorización la reproducción o transformación (incluida la **corrección de errores**) necesarias para el uso legítimo; la **copia de seguridad**, que el contrato **no puede impedir**; y observar, estudiar y verificar el funcionamiento del programa durante su uso legítimo. El apartado 5 permite la **descompilación** solo si es indispensable para la **interoperabilidad** de un programa creado de forma independiente, con requisitos tasados (usuario legítimo, información no disponible de otro modo, limitada a las partes necesarias) y sin usar lo obtenido para un programa sustancialmente similar.
- **Art. 101. Protección registral**: inscripción **potestativa** en el **Registro de la Propiedad Intelectual** (también de versiones sucesivas y derivados).
- **Art. 102. Infracción**: son infractores quienes, sin autorización, pongan en circulación o **posean con fines comerciales** copias ilegítimas (conociéndolo o pudiendo presumirlo) y quienes circulen o posean instrumentos cuyo **único uso** sea neutralizar las protecciones técnicas del programa.
- **Arts. 103 y 104**: acciones y medidas cautelares del régimen general de la ley; salvaguardia de otras normas (patentes, marcas, competencia desleal, **secretos comerciales**, semiconductores, derecho de obligaciones).

## El control de legalidad del software

El control de legalidad garantiza que todo el software instalado cuenta con licencia válida y en las condiciones pactadas: evita responsabilidad legal, sanciones y riesgos de seguridad (software sin soporte o de origen dudoso).

- **Gestión de activos de software (SAM)**: inventario automatizado de instalaciones, reconciliación con las licencias adquiridas y métricas de uso; normalizada en **ISO/IEC 19770-1** (sistemas de gestión de activos de TI).
- **Modelos de licencia propietaria**: por **dispositivo**, por **usuario**, por **núcleo de CPU** (habitual en servidores y bases de datos), licencias de acceso de cliente (**CAL**) y, de forma creciente, **suscripción** con soporte incluido; el mantenimiento y las auditorías del fabricante se pactan en contrato.
- **Buenas prácticas**: catálogo de software autorizado, despliegue centralizado (temas 47, 48 y 52), revisiones periódicas y cláusulas de auditoría controladas en los contratos (la contratación TIC se trata en el tema 22).

## Software libre y de código abierto

El **software libre** (definición de la Free Software Foundation) respeta las **cuatro libertades**: usar el programa con cualquier propósito, **estudiarlo** y adaptarlo (exige acceso al código fuente), **redistribuir** copias y **mejorar** el programa publicando las mejoras. El **código abierto** (definición de la **Open Source Initiative**, 10 criterios) coincide en la práctica; «abierto» no significa gratuito ni sin condiciones: la licencia sigue siendo un contrato.

| Licencia | Familia | Rasgo distintivo |
| --- | --- | --- |
| **GPL v3** (2007) | Copyleft fuerte | Las obras derivadas deben distribuirse bajo la misma licencia |
| **AGPL v3** | Copyleft de red | Extiende la obligación al software usado como servicio (SaaS) |
| **LGPL** | Copyleft débil | Permite enlazar la biblioteca desde software propietario |
| **MIT / BSD** | Permisivas | Reutilización casi sin condiciones, citando la autoría |
| **Apache 2.0** | Permisiva | Añade concesión expresa de **patentes** |
| **EUPL 1.2** | Copyleft (UE) | Licencia pública de la Unión Europea, compatible con GPL |

- **Compatibilidad y cumplimiento**: combinar componentes exige comprobar la compatibilidad de licencias (el copyleft «contamina» el derivado); las organizaciones lo gestionan con análisis de composición de software (SCA) en la cadena de desarrollo (tema 26).
- **Aplicaciones consolidadas**: en servidores (Linux, Apache/Nginx, PostgreSQL), en ofimática (**LibreOffice**, con el formato abierto **ODF**, norma **ISO/IEC 26300**) y en la mayoría de las herramientas de desarrollo y datos.

## El software en las administraciones públicas

Las administraciones combinan software propietario, libre y desarrollos propios; el marco jurídico favorece expresamente la **reutilización** y los estándares abiertos (ENI, tema 62).

- **EUPL 1.2** (licencia pública de la Unión Europea, **Decisión (UE) 2017/863**, de 18 de mayo de 2017): licencia copyleft creada por la Comisión para liberar software del sector público, con **valor jurídico en las 23 lenguas** oficiales y lista de licencias compatibles (GPL, AGPL, OSL...).
- **Ley 40/2015, arts. 157 y 158**: las Administraciones **ponen a disposición** de las demás las aplicaciones cuyos derechos posean, pudiendo declararlas **de fuentes abiertas**; antes de adquirir o desarrollar deben **consultar el directorio general de aplicaciones** y, si existe solución reutilizable, están **obligadas a usarla** salvo justificación de eficiencia (art. 7 de la LO 2/2012). La AGE mantiene el directorio general en el **Centro de Transferencia de Tecnología (CTT)** del PAe, con las soluciones y servicios comunes reutilizables (tema 63).
- **Titularidad en la contratación**: los pliegos de desarrollo a medida deben prever la **entrega del código fuente** y la titularidad pública de los derechos de explotación (tema 22), condición para poder reutilizar y liberar después.

## Fuentes {.unnumbered .unlisted}

- Real Decreto Legislativo 1/1996, texto refundido de la Ley de Propiedad Intelectual (texto consolidado, última modificación 30 de marzo de 2022).
- Directiva 2009/24/CE, sobre la protección jurídica de programas de ordenador (DOUE 5-may-2009).
- Ley 40/2015, de Régimen Jurídico del Sector Público, arts. 157-158 (texto consolidado, última modificación 2 de agosto de 2024).
- Decisión de Ejecución (UE) 2017/863 de la Comisión, de 18 de mayo de 2017 (EUPL v1.2).
- GNU GPL v3 (FSF, 2007), Open Source Definition (OSI) e ISO/IEC 19770-1:2017 (SAM).
