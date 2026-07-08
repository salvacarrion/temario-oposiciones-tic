# Temario de Oposiciones TIC

[![Deploy](https://github.com/salvacarrion/temario-oposiciones-tic/actions/workflows/deploy.yml/badge.svg)](https://github.com/salvacarrion/temario-oposiciones-tic/actions/workflows/deploy.yml)
[![Licencia: CC BY-NC 4.0](https://img.shields.io/badge/licencia-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.es)
[![Web: MkDocs Material](https://img.shields.io/badge/web-MkDocs%20Material-526CFE.svg)](https://squidfunk.github.io/mkdocs-material/)
[![PDF: Quarto](https://img.shields.io/badge/PDF-Quarto-75AADB.svg)](https://quarto.org)

Temario **libre y gratuito**, de elaboración propia, para oposiciones de informática (cuerpos TIC, grupos A1/A2) de las administraciones públicas españolas. Un solo contenido, dos formatos: libro web y PDF.

📖 **[Leer el libro](https://salvacarrion.github.io/temario-oposiciones-tic/)** · ⬇️ **[Descargar el PDF](https://salvacarrion.github.io/temario-oposiciones-tic/temario-oposiciones-tic.pdf)**

## Origen

Este temario es la evolución del que elaboré en 2022 para aprobar las [pruebas selectivas de acceso al **Cuerpo Superior Técnico de Ingeniería en Informática de la Administración de la Generalitat Valenciana (A1-06)**, convocatoria 5/22](https://sede.gva.es/es/detall-ocupacio-publica?id_emp=84659&id_info=info_basica), en las que obtuve la plaza n.º 495, con [nombramiento como personal funcionario de carrera el 27 de septiembre de 2024 (DOGV 02/10/2024)](https://dogv.gva.es/datos/2024/10/02/pdf/2024_10012_es.pdf). Previamente ya me había presentado a otros procesos selectivos en diferentes administraciones (sanidad, universidades, administración local) por lo que este temario también incluye temas de otras oposiciones. Por tanto, aunque sigue de forma muy exhaustiva el programa de la GVA, no es ni un temario oficial ni un temario cerrado de ningún cuerpo en concreto, sino una base común para preparar gran parte de las oposiciones TIC.

Lo que aquí se publica es la versión limpia, ampliada y actualizada de aquel temario original, que era esquemático, y de elaboración manual. He actualizado el contenido tanto en la parte general como en la específica, homogeneizado el formato y añadido a cada tema sus fuentes y las fechas del texto consolidado de cada norma. Para la redacción me he apoyado en el uso de la IA a fin de mejorar la claridad de las explicaciones, cuidando la literalidad de la parte normativa. Además, la revisión de cada tema incluye una verificación exhaustiva contra la legislación vigente con **Claude Code (Fable 5)** en modo «Ultracode» (xhigh + workflow), una segunda y tercera comprobación con otros modelos (**GPT-5.5** y **Gemini 3.5**) para descartar discrepancias y alucinaciones. Finalmente, a todo esto se suma una verificación final y manual por mi parte.

Todo el contenido es de elaboración propia, a partir de fuentes públicas: normativa consolidada (BOE/DOGV), guías y estándares oficiales, y otros recursos de acceso libre. El objetivo es ofrecer una referencia **clara, estructurada y gratuita** a quien esté preparando oposiciones de informática o similares.

En **julio de 2026** decidí publicarlo, revisarlo y actualizarlo para que otras personas puedan aprovecharlo. Al publicarse como proyecto **open source**, la idea es que pueda corregirse, mejorarse y mantenerse entre todos.

## ¿Qué oposiciones cubre?

El grueso del temario es común a la mayoría de cuerpos TIC de nivel A1/A2: Administración de la Generalitat Valenciana, sanidad, universidades, administración local y otras administraciones públicas. No cubre de forma exhaustiva el programa de ninguna convocatoria concreta (tampoco el de la GVA), pero el solapamiento con todas ellas es muy alto. Solo los temas específicos valencianos habría que sustituirlos por los del ámbito correspondiente.

Los **11 bloques** actuales:

1. Marco jurídico y administrativo
2. Sociedad digital y gestión TIC
3. Ingeniería del software
4. Seguridad de la información
5. Datos, IA y tecnologías emergentes
6. Sistemas e infraestructuras
7. Protección de datos y administración electrónica
8. Desarrollo web y de aplicaciones
9. Interoperabilidad y confianza digital
10. Redes y comunicaciones
11. Administración de la Generalitat

## Contribuir

¡Toda ayuda es bienvenida! Este material lo mantengo en mi tiempo libre y seguro que contiene erratas o normativa que ha cambiado. Si ves algo mejorable, abre una [*issue*](https://github.com/salvacarrion/temario-oposiciones-tic/issues) o envía directamente un *pull request* (cada página del libro tiene enlaces de edición y de reporte de errores). En temas legales, cita la fuente (BOE/DOGV consolidado) para que la corrección sea verificable.

Si el material te ha resultado útil y quieres apoyarlo, puedes invitarme a un café en [ko-fi.com/salvacarrion](https://ko-fi.com/salvacarrion). ☕

## Cómo se construye

El contenido está escrito en markdown, un fichero por tema en [`src/`](src/). A partir de esa única fuente se generan las dos versiones del libro:

| Formato | Herramienta | Configuración |
| --- | --- | --- |
| Web | [MkDocs](https://www.mkdocs.org) + tema [Material](https://squidfunk.github.io/mkdocs-material/) | [`mkdocs.yml`](mkdocs.yml) |
| PDF | [Quarto](https://quarto.org) | [`_quarto.yml`](_quarto.yml) |

Cada push a `main` regenera el PDF, construye la web y publica ambos en GitHub Pages mediante [GitHub Actions](.github/workflows/deploy.yml).

### Desarrollo local

```bash
# Web: vista previa con recarga automática en http://127.0.0.1:8000
pip install mkdocs-material
mkdocs serve

# PDF (requiere Quarto con TinyTeX)
quarto render --to pdf
```

## Licencia

[**CC BY-NC 4.0**](LICENSE.md): puedes compartir y adaptar el material dando crédito al autor y **sin fines comerciales**.

**Aviso**: este es un temario personal, no un material oficial. Aunque he procurado la máxima precisión, no puedo garantizar la ausencia de errores ni que la normativa citada siga vigente; contrasta siempre con las fuentes oficiales (BOE/DOGV) antes del examen.
