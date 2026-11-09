---
name: labrador
description: Redacta informes de laboratorio académicos en español (redes, electrónica, física, química, sistemas y cualquier otra práctica) con la estructura Introducción, Marco teórico, Materiales y métodos, Procedimiento, Resultados y Conclusiones, figuras y tablas en APA 7 y un marco teórico con fuentes verificables. Úsala siempre que alguien pida un informe, reporte o entregable de una práctica o laboratorio, quiera convertir la guía del laboratorio, sus capturas, mediciones o notas en un informe, o pida corregir o completar un informe de laboratorio existente, aunque no mencione la skill, APA ni el nombre de las secciones.
---

# LABrador: informes de laboratorio

LABrador convierte lo que pasó en una práctica de laboratorio (la guía, las capturas, las mediciones, las notas) en un informe académico con una estructura fija, redactado en prosa y con un marco teórico respaldado por fuentes reales. La estructura base es deliberadamente corta: si la persona necesita apartados extra (diagrama de red, anexos, portada, objetivos, etc.), los pide en el prompt y se agregan en su lugar.

## Flujo de trabajo

1. **Reunir los insumos.** Lee todo lo que la persona adjuntó antes de escribir. Lo que hace falta:
   - Asignatura y tema o título del laboratorio.
   - La guía, enunciado o lista de puntos que pidió el docente. Define qué va en Resultados.
   - La evidencia: capturas, mediciones, salidas de consola, valores calculados, fotos, tablas de datos.
   - Las condiciones reales: equipos, direcciones, versiones de software, herramientas usadas.
   - Fuentes que la persona quiera usar (opcional).
   - Apartados extra o formato particular que pida el docente (opcional).

   Si faltan datos de resultados, pregúntalos todos juntos en un solo mensaje. Un informe de laboratorio vale por lo que se midió y se observó; inventar una medición, una dirección IP, un valor o una captura lo convierte en un documento falso que la persona va a entregar con su nombre. Si no hay forma de preguntar, deja marcadores visibles `[COMPLETAR: qué falta]` en lugar de rellenar.

2. **Planear el informe.** Antes de redactar, define: las secciones (base + extras pedidos), los puntos o pruebas de Resultados según la guía, y qué figuras y tablas van en cada sección. Cada imagen que la persona entregó debe tener un lugar y un número.

3. **Conseguir y validar las fuentes del marco teórico.** Sigue `references/fuentes.md`. Si la persona dio fuentes, se validan primero; luego se completa con búsqueda. Solo se cita lo que se pudo abrir y leer.

4. **Redactar sección por sección.** Sigue `references/secciones.md`, que explica qué va en cada sección, con ejemplos buenos y malos tomados de informes reales.

5. **Revisar con la lista de verificación** (al final de este archivo).

6. **Entregar** en el formato que se pida (ver "Entrega").

## Estructura base

El orden es fijo. Los apartados opcionales solo aparecen si la persona los pide, en la posición indicada.

| Orden | Sección | Notas |
|---|---|---|
| (opcional) | Portada | Solo si se pide. Muchos grupos la hacen a mano. |
| 1 | Introducción | Breve: contexto, qué se hizo y qué recoge el informe. |
| 2 | Marco teórico | Prosa continua, conectada y referenciada. Única sección con citas. |
| 3 | Materiales y métodos | Equipos, software y herramientas; luego el método en prosa. |
| 4 | Procedimiento | Lo que se hizo, en orden, en prosa. |
| (opcional) | Diagrama de red, montaje, circuito… | Va entre Procedimiento y Resultados. |
| 5 | Resultados | Organizados por los puntos, pruebas o escenarios de la guía. |
| 6 | Conclusiones | Párrafos separados, sin numerar ni viñetas. |
| 7 | Referencias | APA 7, orden alfabético. |
| (opcional) | Anexos | Después de Referencias, como Anexo A, Anexo B… |

Si la persona pide otro apartado no listado (por ejemplo, Objetivos o Análisis de resultados separado), ubícalo donde tenga sentido lógico y menciónalo en una línea al entregar.

## Reglas que aplican a todo el informe

- **Español formal e impersonal.** "Se configuró", "se observó", "se obtuvo". Pasado para lo que se hizo en la práctica; presente para la teoría ("el switch asocia la dirección MAC con el puerto…").
- **Solo el marco teórico lleva citas.** Introducción, procedimiento, resultados y conclusiones se apoyan en lo que se explicó en el marco teórico, sin volver a citar. La excepción son las figuras tomadas de una fuente, que siempre indican el origen en la nota.
- **Prosa, no listas.** Las viñetas solo se usan para la lista de materiales. Los resultados pueden ir agrupados por los puntos de la guía (con su número y título), pero dentro de cada punto se escribe en párrafos.
- **Figuras y tablas en APA 7.** Se numeran en el orden en que aparecen, se mencionan en el texto antes de aparecer ("como se observa en la Figura 3") y llevan título y nota. Los detalles están en `references/apa7.md`.
- **Las siglas se definen la primera vez.** "Unidad máxima de transmisión (MTU)" y después solo "MTU".
- **Los números se explican.** Cada valor que aparezca en resultados debe interpretarse: qué significa, por qué dio eso y cómo se relaciona con la teoría.

## Las conclusiones y su pregunta implícita

Cada conclusión es un párrafo que responde a algo aprendido o comprobado en la práctica. Antes de escribir cada una, hazte esta pregunta (no aparece en el informe, es solo el criterio para redactarla):

> ¿Fue necesario desarrollar este laboratorio para llegar a esta conclusión?

Si la respuesta es sí, la conclusión sirve: está anclada en algo que se midió, se observó o se comprobó, y normalmente menciona ese dato. Si la respuesta es no, porque se podría haber escrito leyendo solo la teoría, la conclusión está mal: reescríbela apoyándola en la evidencia de la práctica, o elimínala.

- No pasa la prueba: "Ethernet es el estándar más usado en las redes de área local."
- Sí pasa: "La falla de continuidad en los pines 4, 5, 7 y 8 no se manifestó en la prueba funcional, porque Fast Ethernet solo usa los pares de los pines 1, 2, 3 y 6; verificar únicamente que el cable 'navegue' no basta como criterio de aceptación."

`references/secciones.md` tiene más ejemplos y la forma de ordenar los párrafos.

## Entrega

**Por defecto, un archivo Word (.docx).** Arma un JSON con el contenido siguiendo la estructura de `assets/ejemplo_informe.json` y genera el documento:

```bash
python scripts/generar_informe.py informe.json salida.docx
```

El script aplica el formato (márgenes, fuente, interlineado, títulos, numeración de páginas), numera solo las figuras y tablas y reemplaza las referencias internas `{fig:id}` y `{tab:id}` por "Figura N" y "Tabla N". Así no hay que llevar la cuenta a mano ni se descuadra si se agrega una figura en medio. Las imágenes van por ruta; si alguna falta, el script deja un recuadro con `[Insertar imagen: …]` en vez de fallar. Revisa los avisos que imprime. Si la persona necesita otro formato de documento (márgenes, fuente, interlineado), ajústalo en el bloque `formato` del JSON.

Después de generar el archivo, si hay forma de convertirlo a PDF o imagen (por ejemplo con LibreOffice), revisa visualmente al menos las páginas con figuras y tablas.

**Si la persona pide el texto en el chat**, entrega el informe en Markdown con los mismos títulos, las mismas reglas de redacción, y las figuras y tablas indicadas con su número, título y nota en el lugar donde irían.

Al entregar, di en pocas líneas qué quedó pendiente (marcadores `[COMPLETAR]`, imágenes por insertar, fuentes de la persona que se descartaron y por qué). No repitas el contenido del informe.

## Lista de verificación final

- [ ] Las secciones están en el orden base, más los extras pedidos y nada más.
- [ ] No hay ningún dato inventado; lo que falta quedó como `[COMPLETAR: …]`.
- [ ] El marco teórico es prosa continua, sin viñetas, y cada párrafo se conecta con el anterior.
- [ ] Cada afirmación teórica tiene su cita, y cada cita está en Referencias (y al revés).
- [ ] Ninguna sección fuera del marco teórico tiene citas (salvo la nota de una figura tomada de una fuente).
- [ ] Todas las fuentes se abrieron y respaldan lo que se les atribuye; las citas textuales son exactas.
- [ ] Cada figura y tabla tiene número, título, nota, y se menciona en el texto antes de aparecer.
- [ ] Resultados cubre todos los puntos de la guía, y cada valor está interpretado.
- [ ] Cada conclusión pasa la pregunta implícita y ninguna está numerada ni en viñetas.
- [ ] Referencias en APA 7, en orden alfabético, solo con la fuente y su enlace.
