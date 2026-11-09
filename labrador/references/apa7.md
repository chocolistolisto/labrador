# Normas APA 7 aplicadas al informe

Resumen práctico de lo que se usa en un informe de laboratorio: figuras, tablas, citas en el texto y lista de referencias. No es la norma completa; cubre los casos que aparecen en estas prácticas.

## Contenido

1. Figuras
2. Tablas
3. Citas en el texto
4. Lista de referencias
5. Formatos por tipo de fuente

---

## 1. Figuras

Todo lo que no es texto ni tabla es una figura: capturas de pantalla, fotos, diagramas, esquemas, gráficas.

**Estructura (de arriba hacia abajo):**

1. **Número:** "Figura 1", en negrita.
2. **Título:** en la línea siguiente, en cursiva, con mayúscula inicial y sin punto final. Describe qué muestra, no lo interpreta. Por ejemplo, *Extremos del cable UTP terminados con conectores RJ45 bajo el estándar T568B*.
3. **La imagen.**
4. **Nota:** debajo, empieza con *Nota*. en cursiva y continúa en redonda. Explica lo que hace falta para leer la figura e indica el origen:
   - Si es propia: "…Elaboración propia."
   - Si se tomó de una fuente: "Tomado de *Título del recurso*, por Autor, año, Editor o sitio." Esta es la única cita permitida fuera del marco teórico, y la fuente también va en Referencias.
   - Si se adaptó: "Adaptado de…".

**Reglas:**

- Se numeran en el orden de aparición, en todo el documento (no por sección).
- Se mencionan en el texto antes de aparecer: "como se observa en la Figura 3", "(ver Figura 3)". En el texto se escriben con mayúscula inicial.
- Una figura nunca aparece sin que el texto la mencione y la explique.
- Las capturas deben ser legibles. Si en la captura importa un campo específico, la nota dice dónde está ("el campo Header Checksum aparece resaltado en el panel de bytes").

## 2. Tablas

**Estructura:** igual que las figuras. "Tabla 1" en negrita, título en cursiva en la línea siguiente, la tabla, y la *Nota*. debajo.

**Formato de la tabla:** encabezados en la primera fila, líneas horizontales arriba y abajo del encabezado y al final de la tabla, sin líneas verticales. Los valores numéricos alineados y con las mismas unidades en toda la columna (las unidades van en el encabezado: "Latencia (ms)").

**Cuándo usar tabla y no texto:** cuando hay más de tres o cuatro valores comparables (resultados pin a pin, mediciones repetidas, configuración de varios equipos).

## 3. Citas en el texto

Solo en el marco teórico (y en la nota de una figura tomada de una fuente).

**Formas básicas:**

| Caso | Entre paréntesis | Narrativa |
|---|---|---|
| Un autor | (Postel, 1981) | Postel (1981) señala que… |
| Dos autores | (Deering & Hinden, 2017) | Deering y Hinden (2017)… |
| Tres o más | (Bezprozvannych et al., 2021) | Bezprozvannych et al. (2021)… |
| Autor institucional | (Cisco, s.f.) | Según Cisco (s.f.)… |
| Sin fecha | (Wireshark Foundation, s.f.) | |
| Con sección | (Postel, 1981a, sección 3.1) | |
| Dos fuentes | (Fluke Networks, 2014; Petrovitch, 2025) | |

**Mismo autor y mismo año:** se agregan letras en el orden en que aparecen en la lista de referencias: (Postel, 1981a), (Postel, 1981b). Sin fecha: (Cisco, s.f.-a), (Cisco, s.f.-b).

**Cita textual:** entre comillas angulares «…», exacta (palabra por palabra, en el idioma original), seguida de la cita y, si está en otro idioma, de la explicación en español. Debe ser breve: una frase o un fragmento, y como máximo una por fuente. Si se omite parte del texto, se marca con […].

**Paráfrasis:** se expresa la idea con palabras propias y se cita igual. La mayoría del marco teórico va así.

**Dónde va la cita:** al final de la idea que respalda, antes del punto. Si un párrafo entero viene de una sola fuente, no hace falta citarla en cada oración: basta al inicio o en la primera afirmación y de nuevo si se mezcla con otra fuente.

## 4. Lista de referencias

- Título "Referencias", centrado y en negrita, en página nueva.
- Orden alfabético por el apellido del primer autor o el nombre de la institución.
- Sangría francesa (1,27 cm), sin viñetas ni números.
- Solo la fuente y su enlace o DOI. Sin notas, sin "consultado el…", sin comentarios sobre cómo se encontró.
- Toda cita del texto está en la lista, y toda entrada de la lista se cita en el texto.
- Los títulos de obras independientes (libros, normas, RFC, páginas web, informes) van en cursiva. Los títulos de artículos dentro de una revista no; en ese caso va en cursiva el nombre de la revista y el volumen.

## 5. Formatos por tipo de fuente

En el JSON del script, la cursiva se marca con `*asteriscos*`.

**RFC (IETF):**
> Postel, J. (1981). *Internet Protocol* (RFC 791). Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc791

**Norma técnica:**
> IEEE. (2018). *IEEE standard for Ethernet* (IEEE Std 802.3-2018). Institute of Electrical and Electronics Engineers. https://standards.ieee.org/ieee/802.3/7071/

**Documentación técnica de un fabricante (página web sin fecha):**
> Cisco. (s.f.). *Use the traceroute command on operating systems*. https://www.cisco.com/c/en/us/support/docs/ip/ip-routed-protocols/22826-traceroute.html

**Documentación con sitio o colección (cuando el sitio no es el mismo autor):**
> Microsoft. (s.f.). *ping*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping

**Página web con autor y fecha:**
> Petrovitch, J. (2025, 3 de abril). *T568A vs T568B: Breaking down Ethernet wiring standards*. NetAlly. https://www.netally.com/tech-tips/t568a-vs-t568b/

**Página de manual (man page):**
> Kerrisk, M. (s.f.). *ping(8) — Linux manual page*. https://man7.org/linux/man-pages/man8/ping.8.html

**Artículo de revista:**
> Bezprozvannych, G., Kostiukov, I., & Pushkar, O. (2021). Synthesis of constructive-technological decisions of regulation of working capacitance of cables of industrial networks. *Electrical Engineering & Electromechanics*, (1), 44–49. https://doi.org/10.20998/2074-272X.2021.1.07

**Libro:**
> Tanenbaum, A. S., Feamster, N., & Wetherall, D. J. (2021). *Computer networks* (6.ª ed.). Pearson.

**Ley o norma colombiana:**
> Congreso de la República de Colombia. (2009). *Ley 1273 de 2009*. https://www.cancilleria.gov.co/normograma/compilacion/docs/ley_1273_2009.htm

**Guía o manual de usuario:**
> Wireshark Foundation. (s.f.). *Wireshark user's guide*. https://www.wireshark.org/docs/wsug_html_chunked/

**Detalles frecuentes:**

- "s.f." cuando la página no tiene fecha visible. No se inventa el año.
- En español: "y" en el texto narrativo y "&" dentro de paréntesis y en la lista de referencias.
- Si el autor y el sitio son el mismo (Cisco en cisco.com), el sitio no se repite.
- Los enlaces se escriben completos, sin "Recuperado de" (APA 7 ya no lo usa salvo en contenido que cambia con el tiempo).
