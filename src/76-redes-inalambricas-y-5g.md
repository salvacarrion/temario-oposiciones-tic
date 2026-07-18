# Redes inalámbricas y 5G

Las redes inalámbricas conectan nodos mediante ondas electromagnéticas, sin cableado, y son la base de la movilidad: desde la red local de una oficina (Wi-Fi) hasta la cobertura nacional de la telefonía móvil (5G). Este tema cubre la familia IEEE 802.11, las generaciones de telefonía móvil con el 5G en detalle y otras tecnologías de transmisión inalámbrica. Los dispositivos y el direccionamiento de red se estudian en el tema [71](71-redes-de-computadores.md), las redes de emergencia en el 71, las redes IoT de corto y largo alcance (Bluetooth, LPWAN) en el 73 y la seguridad inalámbrica (WEP/WPA/WPA3, 802.1X) en el 75.

## Wi-Fi: la familia IEEE 802.11

Las redes inalámbricas se clasifican por su alcance, en paralelo a las redes cableadas (PAN/LAN/MAN/WAN):

| Tipo | Alcance típico | Tecnologías |
| --- | --- | --- |
| **WPAN** (área personal) | 10-100 m | Bluetooth, ZigBee, NFC, RFID (tema [77](77-internet-de-las-cosas-y-redes-de-sensores.md)) |
| **WLAN** (área local) | ~100 m | **Wi-Fi (IEEE 802.11)** |
| **WMAN** (área metropolitana) | 1-50 km | WiMAX (IEEE 802.16, hoy legado) |
| **WWAN** (área extensa) | regional/global | Telefonía móvil (2G-5G), satélite |

Dentro del proyecto **IEEE 802** (estándares de redes de área local y metropolitana), los grupos de trabajo relevantes son: **802.1** (puentes, VLAN 802.1Q y autenticación 802.1X: temas [71](71-redes-de-computadores.md) y [79](79-seguridad-en-las-comunicaciones.md)), **802.3** (Ethernet cableada), **802.11** (WLAN, la base de Wi-Fi), **802.15** (WPAN: Bluetooth en 802.15.1, ZigBee sobre 802.15.4) y **802.16** (WMAN: WiMAX). La marca **Wi-Fi** la otorga la **Wi-Fi Alliance**, que certifica la interoperabilidad de los equipos 802.11.

- **Arquitectura 802.11**:
    - **Estación (STA)**: cualquier dispositivo con interfaz 802.11.
    - **Punto de acceso (AP)**: hace de puente entre el medio radio y la red cableada.
    - **BSS (Basic Service Set)**: grupo de estaciones que se comunican entre sí; puede ser **independiente** (ad hoc, sin AP) o de **infraestructura** (a través de un AP).
    - **ESS (Extended Service Set)**: unión de varios BSS interconectados por un **sistema de distribución (DS)**, normalmente la LAN cableada; permite la **itinerancia (roaming)** de las estaciones entre AP sin perder la conexión.
    - **SSID**: nombre lógico de la red que comparten los AP de un mismo ESS.
- **Acceso al medio**: **CSMA/CA** (acceso múltiple con escucha de portadora y **prevención de colisiones**): la estación escucha el canal, espera un tiempo aleatorio (*backoff*) y transmite; el receptor confirma con **ACK**. Como una estación no puede detectar colisiones mientras transmite (a diferencia del CSMA/CD de Ethernet), se previenen con el intercambio opcional **RTS/CTS**, que además mitiga el problema del **nodo oculto**. El medio es compartido y semidúplex.
- **Bandas de frecuencia**: **2,4 GHz** (banda ISM, 13 canales en Europa, solo 3 sin solape: mayor alcance, más interferencias), **5 GHz** (más canales y anchura, menor alcance) y **6 GHz** (5945-6425 MHz en Europa, abierta para Wi-Fi 6E/7).

Las generaciones comerciales de Wi-Fi (numeradas por la Wi-Fi Alliance desde 2018) y sus estándares IEEE:

| Generación | Estándar IEEE | Año | Bandas (GHz) | Velocidad máxima teórica |
| --- | --- | --- | --- | --- |
| (legado) | 802.11 | 1997 | 2,4 | 2 Mbps |
| (Wi-Fi 1) | 802.11b | 1999 | 2,4 | 11 Mbps |
| (Wi-Fi 2) | 802.11a | 1999 | 5 | 54 Mbps |
| (Wi-Fi 3) | 802.11g | 2003 | 2,4 | 54 Mbps |
| **Wi-Fi 4** | **802.11n** | 2009 | 2,4/5 | 600 Mbps |
| **Wi-Fi 5** | **802.11ac** | 2013 | 5 | 6,9 Gbps |
| **Wi-Fi 6 / 6E** | **802.11ax** | 2021 | 2,4/5 (+**6** en 6E) | 9,6 Gbps |
| **Wi-Fi 7** | **802.11be** | 2024 | 2,4/5/6 | ~**46 Gbps** |

- **Wi-Fi 4 (802.11n)**: introduce **MIMO** (varias antenas y flujos espaciales), canales de 40 MHz y agregación de tramas.
- **Wi-Fi 5 (802.11ac)**: solo 5 GHz, canales de 80/160 MHz, modulación 256-QAM y MU-MIMO descendente (varios usuarios a la vez).
- **Wi-Fi 6 (802.11ax)**: diseñada para la **eficiencia en entornos densos** más que para la velocidad punta: **OFDMA** (subdivide cada canal entre varios usuarios), MU-MIMO ascendente y descendente, 1024-QAM, coloración de BSS (reduce interferencias entre redes vecinas) y **TWT (Target Wake Time)**, que agenda las transmisiones para ahorrar batería en dispositivos IoT. La certificación exige **WPA3**. **Wi-Fi 6E** extiende lo anterior a la banda de **6 GHz**.
- **Wi-Fi 7 (802.11be, *Extremely High Throughput*)**: certificación desde enero de **2024** (estándar IEEE 802.11be-2024, publicado en julio de 2025): canales de **320 MHz**, 4096-QAM y **MLO (Multi-Link Operation)**, que agrega varias bandas simultáneamente; hasta ~**46 Gbps** teóricos y latencias bajas orientadas a realidad virtual/aumentada y juego en red.
- **Wi-Fi 8 (802.11bn, *Ultra High Reliability*)**: en desarrollo, prevista para **2028**; prioriza la fiabilidad (latencia estable, continuidad en movilidad) sobre el aumento de velocidad.
- **Seguridad**: la enmienda **802.11i** (2004) introdujo WPA2 en sustitución del WEP original, y **802.11w** (2009) protegió las tramas de gestión; el estándar actual de cifrado es **WPA3** (2018). Se desarrollan en el tema [79](79-seguridad-en-las-comunicaciones.md).

## Generaciones de telefonía móvil y redes 5G

La telefonía móvil ha evolucionado por generaciones, aproximadamente una por década, desde la voz analógica hasta la plataforma de conectividad universal que es el 5G:

| Generación | Década | Tecnologías | Acceso radio | Aporta |
| --- | --- | --- | --- | --- |
| **1G** | 1980 | NMT, AMPS, TACS | FDMA (analógico) | Voz analógica, sin datos |
| **2G** | 1990 | **GSM**, GPRS (2.5G), EDGE | TDMA sobre FDMA | Voz digital, **SMS**, itinerancia; primeros datos (GPRS ~114 kbps, EDGE ~384 kbps) |
| **3G** | 2000 | **UMTS** (W-CDMA), HSPA/HSPA+ | CDMA | Datos móviles e internet (hasta 42 Mbps con HSPA+) |
| **4G** | 2010 | **LTE**, LTE-Advanced | OFDMA | Banda ancha móvil **todo IP** (100 Mbps a 1 Gbps) |
| **5G** | 2020 | **5G NR** (3GPP Rel-15, 2018) | OFDMA con numerología escalable | Banda ancha extrema, latencia de 1 ms, IoT masivo |

La quinta generación (**5G**) no es solo más velocidad: se define para tres familias de casos de uso muy distintas y evoluciona mediante *releases* del **3GPP**, el consorcio que la normaliza (junto a la UIT, que fija los requisitos **IMT-2020**, y el ETSI). Se la describe como «la quinta generación para las personas y la primera para las máquinas».

- **Características básicas (requisitos IMT-2020)**:
    - **Velocidad máxima**: **20 Gbps** de bajada y **10 Gbps** de subida.
    - **Latencia**: hasta **1 ms**.
    - **Disponibilidad**: **99,999 %**.
    - **Densidad de tráfico**: hasta **10 Tb/s por km²**.
    - **Densidad de dispositivos**: hasta **1 millón por km²** (IoT masivo), con baterías de hasta **10 años**.
    - **Eficiencia energética**: reducción del **90 %** del consumo respecto a 4G.
- **Bandas de frecuencia** («bandas pioneras» en Europa, ya asignadas en España):
    - **700 MHz** (694-790 MHz): grandes coberturas rurales y penetración en interiores.
    - **3,5 GHz** (3,4-3,8 GHz): banda principal, equilibrio entre capacidad y cobertura.
    - **26 GHz** (24,25-27,5 GHz): ondas milimétricas para máxima capacidad en zonas densas y despliegues localizados.
    - El estándar las agrupa en **FR1** (bandas bajas y medias, hasta 7,125 GHz) y **FR2** (milimétricas, desde 24,25 GHz).
- **Tipos de comunicaciones**:
    - **eMBB (*enhanced Mobile Broadband*)**: banda ancha móvil mejorada, alta velocidad en movilidad (vídeo 4K/8K, RV).
    - **URLLC (*Ultra-Reliable Low-Latency Communications*)**: comunicaciones críticas con latencia de 1-10 ms y fiabilidad del 99,999 % (vehículo conectado, cirugía remota, industria).
    - **mMTC (*massive Machine Type Communications*)**: IoT masivo de bajo coste y consumo, hasta 1 millón de nodos por km².
- **Modos de despliegue**:
    - **5G NSA (*Non Stand Alone*)**: primer paso de la migración: acceso radio 5G con **núcleo (core) 4G**; el plano de control va por 4G y los datos de usuario por 5G. Aprovecha la inversión 4G existente.
    - **5G DSS (*Dynamic Spectrum Sharing*)**: variante transitoria que comparte dinámicamente una frecuencia 4G para cursar tráfico 5G; despliegue casi inmediato a costa de menores prestaciones.
    - **5G SA (*Stand Alone*)**: la red 5G completa (acceso y núcleo 5G); habilita toda la capacidad: latencia mínima, *network slicing* y millones de dispositivos.
- **Tecnologías habilitadoras**:
    - **Network slicing (segmentación de red)**: crea redes virtuales sobre la misma red física, cada una con niveles de servicio a medida (latencia, velocidad, seguridad) para casos de uso distintos; se apoya en SDN/NFV (tema [73](73-virtualizacion-de-redes.md)) y requiere 5G SA.
    - **MIMO masivo y beamforming**: antenas activas con decenas o centenares de elementos que combinan multiplexación espacial (varios flujos simultáneos) y conformación del haz (dirigir la energía hacia cada usuario, «siguiéndolo» y reduciendo interferencias).
    - **MEC (*Multi-access Edge Computing*)**: acerca el procesado y las aplicaciones al borde de la red (junto a los nodos radio), evitando el viaje a nubes centralizadas y logrando las latencias de milisegundos de los servicios en tiempo real (V2X, industria, *smart cities*).
- **Evolución por releases del 3GPP**:
    - **Release 15 (2018)**: primera especificación 5G NR.
    - **Releases 16-17**: URLLC industrial, dispositivos IoT simplificados (**RedCap**) y comunicaciones por satélite (**NTN**).
    - **Release 18 (congelada en junio de 2024)**: inaugura **5G-Advanced**, con IA/ML nativos en la red, eficiencia energética y realidad extendida; la Release 19 (2025) la completa.
    - **6G**: la UIT ya ha fijado el marco **IMT-2030** (Recomendación UIT-R M.2160, noviembre de 2023); el 3GPP prevé las primeras especificaciones 6G en la **Release 21**, hacia **2030**.
- **Marco español**:
    - **Ley 11/2022, General de Telecomunicaciones**: transpone el Código Europeo de Comunicaciones Electrónicas (Directiva (UE) 2018/1972). La **CNMC** actúa como autoridad nacional de reglamentación independiente (Título VI) y lleva el **Registro de operadores** (arts. 6.2 y 7), donde los operadores notifican su actividad; la ordenación general y el espectro corresponden al Ministerio.
    - **RD-ley 7/2022**, de requisitos de seguridad de redes y servicios 5G, desarrollado por el **RD 443/2024**, que aprueba el **Esquema Nacional de Seguridad de redes y servicios 5G (ENS5G)**: análisis nacional de riesgos, obligaciones para operadores y tratamiento de los proveedores de alto riesgo.
    - **Plan de Recuperación (Componente 15**, ~4.000 M€): financia la extensión de banda ancha ultrarrápida y 5G mediante los programas **UNICO** (banda ancha, 5G redes, sectorial 5G, I+D 6G), con despliegue en corredores de transporte y núcleos de población intermedios.

## Otras tecnologías de transmisión

Además de Wi-Fi y de la telefonía móvil, otras tecnologías inalámbricas cubren nichos específicos de alcance, consumo o entorno:

- **Comunicaciones por satélite**: enlazan estaciones terrestres a través de un satélite (señal ascendente hacia el satélite y descendente hacia tierra, en bandas distintas). Por órbita:
    - **GEO (geoestacionaria, ~36.000 km)**: el satélite parece fijo; TV por satélite y VSAT, pero latencia alta (~600 ms ida y vuelta).
    - **MEO (órbita media)**: navegación por satélite (GPS, **Galileo**) y algunas constelaciones de datos.
    - **LEO (órbita baja, <2.000 km)**: latencias de 20-50 ms; las **megaconstelaciones** de banda ancha (**Starlink**, OneWeb, Kuiper) dan cobertura global y respaldo en catástrofes (tema [75](75-redes-de-emergencia.md)).
    - **IRIS²** (Reglamento (UE) **2023/588**): la constelación europea de **conectividad segura** (~290 satélites multiórbita), orientada a comunicaciones gubernamentales resilientes; operativa prevista hacia **2030**.
- **Radioenlaces de microondas terrestres**: enlaces punto a punto con antenas parabólicas alineadas (requieren visión directa); se usan como *backhaul* de operadores y para unir sedes donde no llega la fibra.
- **Comunicaciones ópticas inalámbricas**: los infrarrojos clásicos (IrDA) han desaparecido del mercado; su relevo es **LiFi** (comunicación por luz visible o infrarroja), estandarizado como **IEEE 802.11bb (2023)**: inmune a interferencias radio y confinado físicamente a la sala, útil en entornos sensibles (hospitales, industria, defensa).
- **WiMAX (IEEE 802.16)**: banda ancha inalámbrica metropolitana (hasta ~70 Mbps y decenas de km); perdió frente a LTE y la fibra y hoy es una tecnología **legado**, residual en accesos rurales.

Como síntesis, las tecnologías inalámbricas se ordenan en un cuadrante alcance-consumo; las redes de baja potencia (cuadrante inferior derecho) se estudian en el tema [77](77-internet-de-las-cosas-y-redes-de-sensores.md):

| | Poco alcance | Mucho alcance |
| --- | --- | --- |
| **Bajo consumo** | Bluetooth/BLE, ZigBee, Z-Wave, NFC | **LPWAN**: LoRaWAN, Sigfox, NB-IoT, LTE-M (tema [77](77-internet-de-las-cosas-y-redes-de-sensores.md)) |
| **Alto consumo** | Wi-Fi | Telefonía móvil (3G/4G/5G), satélite |

## Supuesto práctico: despliegue de una red Wi-Fi corporativa

**Enunciado**: un organismo traslada su sede a un edificio de **3 plantas** de **1.200 m²**, con **80 empleados por planta** (cada uno con portátil y móvil) y un **salón de actos de 200 plazas** en la planta baja. Requisitos: acceso corporativo seguro integrado con el directorio, red de **invitados** separada, voz y videoconferencia sobre Wi-Fi con itinerancia sin cortes, y soporte futuro de sensores IoT. El edificio dispone de cableado de **categoría 6A** con PoE (tema [72](72-cableado-estructurado-y-medios-de-transmision.md)).

**Se pide**:

- a) Elegir estándar, bandas y arquitectura de gestión.
- b) Dimensionar y ubicar los puntos de acceso.
- c) Planificar canales y potencias.
- d) Diseñar la seguridad y la segmentación.
- e) Garantizar la itinerancia y la calidad de servicio.

**Resolución**:

**a) Estándar y arquitectura**

- **Wi-Fi 6 (802.11ax)**, preferiblemente **6E**: OFDMA y MU-MIMO para los entornos densos (salón de actos), TWT para el IoT futuro y la banda de **6 GHz** libre de interferencias. Wi-Fi 7 solo se justifica si el parque de clientes va a aprovecharlo.
- **Gestión centralizada**: AP gestionados por una controladora (física, virtual o en la nube): configuración y políticas únicas, **RRM** (gestión automática de canales y potencias) e itinerancia coordinada. AP alimentados por **PoE 802.3at**.

**b) Dimensionamiento y ubicación de los AP**

- **Por capacidad (oficinas)**: 80 × 2 = **160 dispositivos por planta**; con la regla práctica de **30-50 clientes activos por AP**, bastarían 4 AP. **Por cobertura**: en oficina se estima un AP por cada **100-150 m²**, luego 1.200 m² piden **8-10 AP por planta**. Manda el criterio más exigente: **9 AP por planta** como hipótesis de partida.
- **Salón de actos (alta densidad)**: 200 personas × 1,5 dispositivos ≈ **300 dispositivos**; a ~50 por AP, **6 AP** de alta densidad con celdas pequeñas (potencia baja y, si es posible, antenas direccionales o montaje distribuido entre el público).
- **Site survey**: el número y la posición finales los fija un **estudio de cobertura** predictivo verificado sobre el terreno, con objetivo de **RSSI ≥ -67 dBm** y SNR ≥ 25 dB en las zonas con voz, y un solape del **15-20 %** entre celdas para la itinerancia.

**c) Canales y potencias**

- **2,4 GHz**: solo canales **1, 6 y 11**; se desactiva la radio de 2,4 GHz en parte de los AP (evita el solapamiento cocanal) y la banda se reserva para dispositivos antiguos e IoT.
- **5 GHz**: canales de **40 MHz** en oficinas (80 MHz solo si el espectro local lo permite), aprovechando los canales **DFS**; en el salón de actos, celdas de **20-40 MHz** para multiplicar la reutilización.
- **6 GHz** (si 6E): canales de 80 MHz para los clientes compatibles.
- **Potencias**: ajustadas automáticamente por el RRM dentro de límites definidos (una celda demasiado grande rompe la itinerancia y la reutilización de canales).

**d) Seguridad y segmentación** (desarrollo en el tema [79](79-seguridad-en-las-comunicaciones.md))

- **Red corporativa**: **WPA3-Enterprise** con **802.1X** contra un servidor RADIUS integrado con el directorio, idealmente **EAP-TLS** con certificados en los dispositivos gestionados; asignación a la VLAN corporativa y **PMF (802.11w)** obligatorio.
- **Invitados**: SSID separado en VLAN propia con salida solo a internet, aislamiento entre clientes, portal cautivo y ancho de banda limitado.
- **IoT**: SSID/VLAN dedicada con WPA3-Personal o claves por dispositivo (MPSK) y filtrado hacia lo imprescindible.
- Regla general: **máximo 3-4 SSID**, porque cada SSID añade tramas de gestión que consumen capacidad radio.

**e) Itinerancia y calidad de servicio**

- **802.11k** (informe de vecinos), **802.11v** (transición dirigida por la red) y **802.11r** (transición rápida FT, con reautenticación en decenas de milisegundos) activados para la voz.
- ***Band steering*** hacia 5/6 GHz y balanceo de clientes entre AP contiguos.
- **QoS**: WMM con prioridad para voz y vídeo, coherente extremo a extremo con la QoS de la red cableada.
- **Operación**: monitorización continua desde la controladora (clientes, interferencias, AP caídos), revisión del diseño tras cambios de ocupación o mobiliario y actualización planificada del firmware.

## Fuentes {.unnumbered .unlisted}

- AUTELSI, informes *5G: Introducción y Tecnología* y *5G: Casos de uso y habilitadores* (junio de 2022), en `references/08-redes/`.
- IEEE 802.11ax-2021, 802.11be-2024 (publicado en julio de 2025) y 802.11bb-2023; certificaciones y generaciones de la Wi-Fi Alliance (consulta julio 2026).
- IEEE 802.11k-2008, 802.11r-2008 y 802.11v-2011 (itinerancia asistida), refundidas en las revisiones consolidadas del estándar 802.11.
- 3GPP (Releases 15 a 19; 5G-Advanced) y UIT-R: requisitos IMT-2020 y Recomendación UIT-R M.2160 (IMT-2030, noviembre de 2023), contrastados online en julio de 2026.
- Ley 11/2022, de 28 de junio, General de Telecomunicaciones; RD-ley 7/2022, de 29 de marzo; RD 443/2024, de 30 de abril (ENS5G), todos en BOE.
- Reglamento (UE) 2023/588 (programa de conectividad segura de la Unión, IRIS²).
