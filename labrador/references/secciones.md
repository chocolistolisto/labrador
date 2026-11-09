# Guía de redacción por sección

Esta guía explica qué va en cada sección del informe, cómo se escribe y qué errores evitar. Los ejemplos vienen de informes de laboratorio reales de Redes de Datos (ponchado de cables, análisis de tráfico con Wireshark y generación de tramas), pero las mismas reglas sirven para cualquier asignatura.

## Contenido

1. Introducción
2. Marco teórico
3. Materiales y métodos
4. Procedimiento
5. Apartados opcionales (diagrama, montaje, portada, anexos)
6. Resultados
7. Conclusiones
8. Referencias

---

## 1. Introducción

**Propósito:** ubicar al lector en el tema y decirle qué se hizo y qué va a encontrar. No es un resumen de resultados ni un marco teórico corto.

**Extensión:** dos a cuatro párrafos.

**Contenido, en este orden aproximado:**

1. El tema y por qué importa, en una o dos oraciones de contexto.
2. Qué se hizo en la práctica y con qué propósito (qué se quería comprobar o entender).
3. Cómo se organizó la práctica, si tuvo varias actividades o etapas.
4. Qué recoge el informe. Puede cerrar anticipando las secciones siguientes.

**Sin citas.** La introducción presenta el tema; el respaldo teórico llega en la sección siguiente.

**Ejemplo de buena apertura:** "El presente informe documenta la práctica de laboratorio dedicada a la generación e inyección manual de tramas en una red de área local. A diferencia de las prácticas anteriores, en las que el tráfico se producía con herramientas estándar como ping, en esta ocasión se construyó una trama Ethernet byte a byte…"

Funciona porque en dos oraciones dice qué se hizo y en qué se diferencia de lo anterior.

**Evitar:**

- Abrir con frases vacías del tipo "En la actualidad, la tecnología avanza a pasos agigantados…".
- Anticipar resultados concretos ("se encontró que el MTU es 1500 bytes"). Eso va en Resultados.
- Explicar teoría a fondo. Si un párrafo de la introducción necesita una cita, pertenece al marco teórico.

---

## 2. Marco teórico

**Propósito:** dar al lector todo el fundamento necesario para entender por qué los resultados salieron como salieron. La pregunta guía es: *¿qué tiene que saber alguien para interpretar cada resultado de este informe?* Si un concepto no se usa después, sobra. Si un resultado depende de un concepto que no está aquí, falta.

**Forma:** párrafos seguidos, sin viñetas, sin enumeraciones, sin listas de definiciones. Cada párrafo retoma algo del anterior y avanza. El texto se lee como una explicación continua, no como un glosario.

**Orden recomendado:** de lo general a lo particular, o siguiendo el orden en que los conceptos aparecen en la práctica. En redes suele funcionar ir por capas, de abajo hacia arriba. Al final del marco teórico pueden ir el marco normativo o las contramedidas, si la práctica lo amerita.

**Conectar los párrafos.** La transición es lo que convierte una colección de definiciones en un marco teórico. Algunas formas:

- Retomar el último concepto: "…la dirección MAC de origen y la de destino. Los switches son los dispositivos que operan en esta capa y basan sus decisiones en…"
- Mostrar la consecuencia: "Ahora bien, todo cambio en los encabezados obliga a recalcular las sumas de verificación…"
- Conectar con la práctica: "Este mecanismo de aprendizaje y expiración es precisamente el que puede manipularse al inyectar tramas con una dirección de origen falsificada."

La última técnica es la más valiosa: cerrar un párrafo diciendo por qué ese concepto importa para lo que se hizo.

**Citas:** todo lo que se afirme y no sea conocimiento común de la asignatura lleva cita. El formato está en `apa7.md`. Combina paráfrasis con citas textuales breves:

- La mayor parte del texto va **parafraseado** con su cita: "…el switch aprende la dirección MAC de origen y la asocia con el puerto por el que llegó la trama (Cisco, s.f.-b)."
- Cuando la redacción exacta importa (una definición normativa, un valor que fija un estándar), usa una **cita textual corta** entre comillas angulares, en su idioma original si es una fuente en inglés, y explícala en español justo después: «Type: 8 for echo message; 0 for echo reply message» (Postel, 1981b), es decir, el tipo 8 identifica la solicitud de eco y el 0 su respuesta.
- Las citas textuales deben ser breves (una frase o un fragmento) y como máximo una por fuente. Un marco teórico armado de citas largas pegadas no demuestra comprensión.
- Cuando la fuente tiene secciones (RFC, normas, manuales), indica la sección: (Postel, 1981a, sección 3.1).

**Subtítulos internos:** por defecto no. Si la práctica abarca muchos temas distintos (por ejemplo, siete actividades con protocolos diferentes) y el marco teórico pasa de unas cuatro páginas, se pueden usar subtítulos de nivel 2 para orientar al lector. Bajo cada subtítulo se sigue escribiendo en prosa conectada.

**Figuras en el marco teórico:** son útiles para estructuras (formato de una trama, cabecera de un protocolo, esquema de colores, diagrama de secuencia). Si la figura es de una fuente, la nota dice de dónde se tomó; si se elaboró para el informe, la nota dice "Elaboración propia".

**Evitar:**

- Viñetas, listas numeradas o párrafos de una sola oración.
- Párrafos que empiezan con "X es…" uno tras otro, sin transición.
- Teoría que no se usa en ningún resultado.
- Citas a fuentes que no se abrieron (ver `fuentes.md`).

---

## 3. Materiales y métodos

**Propósito:** que otra persona pueda saber con qué se trabajó y bajo qué condiciones.

**Forma:** esta es la sección donde sí se usa lista. Primero, un párrafo corto de contexto (dónde se hizo, cuántos equipos, cómo estaban conectados). Después, la lista de materiales con viñetas, cada uno con este patrón:

> **Nombre del material o equipo:** qué es, características relevantes (versión, categoría, sistema operativo, dirección IP, MAC…) y para qué se usó en la práctica.

Por último, uno o dos párrafos de **método**: la estrategia general (por ejemplo "se siguió una secuencia de captura, construcción, verificación e inyección") y las decisiones tomadas con su justificación ("se eligió T568B en ambos extremos porque el cable conectaría un equipo a un punto de red, por lo que no se requería un cable cruzado").

**Detalles que suelen faltar:** versiones del software, modo del adaptador de red de la máquina virtual (puente o NAT), categoría del cable, quién proporcionó el instrumento de medida, segmento de red. Si son relevantes para interpretar resultados y la persona no los dio, pregúntalos o márcalos con `[COMPLETAR]`.

**Sin citas.** Si un material necesita justificación teórica (por ejemplo, por qué Cat 5e es suficiente), esa justificación va en el marco teórico y aquí solo se aplica.

---

## 4. Procedimiento

**Propósito:** contar lo que se hizo, en el orden en que se hizo, con suficiente detalle para repetirlo.

**Forma:** prosa en pasado impersonal, en orden cronológico. Un párrafo por etapa. Los conectores de secuencia ayudan ("Inicialmente…", "A continuación…", "Una vez verificada la trama…", "Por último…").

**Incluye:** los comandos o parámetros usados (en el texto o en un bloque de código si son largos), los valores que se configuraron, las verificaciones intermedias y cualquier precaución que indicó el docente.

**Figuras en el procedimiento:** se pueden usar para mostrar un paso (la ventana de configuración, el montaje), pero la evidencia de lo obtenido va en Resultados. Si una práctica es muy corta, procedimiento y resultados pueden compartir figuras, pero sin repetir la misma.

**Sin citas y sin interpretación.** "Se ejecutó ping con la bandera -f y 1472 bytes de datos" es procedimiento; "lo que demuestra que el MTU es 1500 bytes" es resultado.

---

## 5. Apartados opcionales

Solo se incluyen si la persona los pide.

- **Diagrama de red, montaje o circuito:** va entre Procedimiento y Resultados. Un párrafo que describe la topología (equipos, direcciones, conexiones, punto de captura) y la figura con el diagrama. Si la persona no tiene el diagrama, deja la figura como marcador con la descripción de lo que debe mostrar.
- **Portada:** asignatura, título del laboratorio, integrantes, docente, universidad, programa y fecha. Los datos los da la persona; no se adivinan.
- **Objetivos:** si se piden, van después de la Introducción: un objetivo general y, si aplica, objetivos específicos. Es el único caso, además de materiales, en que se acepta una lista.
- **Anexos:** después de Referencias, cada uno en página nueva como "Anexo A. Título". Para capturas complementarias, código completo o tablas de datos largas. El texto del informe debe mencionar cada anexo.

---

## 6. Resultados

**Propósito:** mostrar lo que se obtuvo y explicarlo. Es la sección más importante del informe.

**Organización:** sigue la estructura de la guía del laboratorio. Si la guía tiene puntos numerados, cada punto es un apartado con su número y su enunciado (por ejemplo, "4. Halle el valor del MTU de la red usando ping y Wireshark"). Si hubo pruebas o escenarios, se presentan como **Prueba 1. Verificación funcional de conectividad.**, con el título en negrita al inicio del párrafo. Si la práctica fue un único experimento, puede ir en párrafos sin subdivisión.

**Dentro de cada punto, el ciclo es:**

1. Qué se hizo para obtener el resultado (una oración, sin repetir todo el procedimiento).
2. La evidencia: figura o tabla, mencionada antes de aparecer.
3. El dato concreto, leído de la evidencia ("la trama alcanzó 98 bytes: 14 de Ethernet, 20 de IPv4, 8 de ICMP y 56 de datos").
4. La interpretación: por qué salió así, en relación con lo explicado en el marco teórico (sin volver a citar).

**Cálculos:** se muestran paso a paso cuando la guía los pide (sumas de verificación, conversiones, errores porcentuales), con los valores intermedios, y se comparan contra el valor que reporta la herramienta.

**Resultados inesperados:** son de lo más valioso del informe. Si algo falló o contradijo lo esperado (cuatro pines sin continuidad, una traza que se detuvo en el primer salto), se reporta tal cual y se explica la causa más probable. No se maquilla.

**Evitar:**

- Capturas sin texto que las explique.
- Valores sin interpretación.
- Inventar datos que no aparecen en la evidencia.
- Citas: la explicación se apoya en lo que ya dijo el marco teórico.

---

## 7. Conclusiones

**Forma:** varios párrafos, cada uno con una conclusión distinta. Sin numeración ("Conclusión 1"), sin viñetas, sin subtítulos. Normalmente salen entre cuatro y seis, según la práctica.

**La pregunta implícita.** Antes de escribir cada conclusión, verifica: *¿fue necesario desarrollar este laboratorio para llegar a esta conclusión?* La pregunta no se escribe en el informe; es el criterio para redactar.

- Si **sí**: la conclusión nace de algo que se midió, se observó, se calculó o falló en la práctica, y suele mencionar el dato.
- Si **no**: la conclusión es teoría reciclada o una obviedad. Reescríbela apoyándola en la evidencia o elimínala.

| No pasa la prueba | Sí pasa la prueba |
|---|---|
| "Wireshark es una herramienta muy útil para analizar redes." | "Obtener a mano los valores CB8F y 4D4A y verlos coincidir con los de Wireshark confirmó que el complemento a uno de 16 bits es la operación concreta que valida cada paquete, no una abstracción del RFC." |
| "Es importante seguir los estándares de cableado." | "Respetar el orden T568B fue condición necesaria pero no suficiente: la secuencia de colores era correcta en ambos extremos y aun así cuatro pines fallaron por la terminación mecánica." |
| "La seguridad en redes es fundamental." | "La captura de las credenciales en texto plano sobre HTTP mostró que basta con acceso al medio y un analizador para leerlas, lo que justifica exigir TLS en cualquier servicio con autenticación." |

**Orden sugerido de los párrafos:**

1. Lo técnico central: el objetivo principal de la práctica, comprobado con el dato.
2. Hallazgos específicos: un párrafo por resultado relevante, sobre todo los inesperados.
3. Implicaciones prácticas, de seguridad o éticas, solo si surgieron de la práctica.
4. Oportunidades de mejora o limitaciones, si las hubo ("como oportunidad de mejora para futuras prácticas…").
5. Opcional: un cierre que integre todo ("En conjunto, el laboratorio…").

**Sin citas** y sin información nueva que no haya aparecido en Resultados.

---

## 8. Referencias

Título "Referencias", en página nueva. Entradas en APA 7, en orden alfabético por el primer autor, con sangría francesa y sin viñetas. Cada entrada lleva solo la fuente y su enlace (o DOI), sin notas, comentarios ni marcas de cómo se encontró. El formato de cada tipo de fuente está en `apa7.md`.
