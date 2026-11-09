<p align="center">
  <img src="docs/img/banner.png" alt="LABrador: le das tu práctica, te trae el informe" width="100%">
</p>

<p align="center">
  <b>Skill para Claude que redacta informes de laboratorio académicos en español</b>,<br>
  con estructura fija, figuras y tablas en APA 7 y un marco teórico respaldado por fuentes verificables.
</p>

---

## ¿Qué hace?

- Arma el informe con la estructura base: **Introducción, Marco teórico, Materiales y métodos, Procedimiento, Resultados, Conclusiones y Referencias.**
- Redacta el marco teórico en **prosa continua** (sin viñetas), con párrafos conectados entre sí y citas en APA 7.
- **Busca fuentes confiables** (RFC, normas IEEE, documentación oficial, artículos con DOI) y **valida las que tú le des**: si alguna no es confiable o no dice lo que se le atribuye, la reemplaza y te avisa.
- Numera y formatea **figuras y tablas en APA 7** (número, título, nota).
- Organiza los **resultados** según los puntos o pruebas de la guía y explica cada valor.
- Escribe **conclusiones** que realmente salen de la práctica: cada una debe pasar la pregunta *"¿fue necesario hacer el laboratorio para llegar a esto?"*.
- **No inventa datos.** Si falta una medición o una captura, pregunta o deja un marcador `[COMPLETAR]`.
- Entrega un **Word (.docx)** listo para exportar a PDF, o el texto en el chat si lo prefieres.

Los apartados extra (portada, diagrama de red, objetivos, anexos) solo se agregan si los pides en el prompt.

## Estructura del repositorio

```
labrador/
├── SKILL.md                     # Flujo de trabajo y reglas principales
├── references/
│   ├── secciones.md             # Cómo se redacta cada sección, con ejemplos
│   ├── apa7.md                  # Figuras, tablas, citas y referencias en APA 7
│   └── fuentes.md               # Cómo buscar y validar fuentes
├── scripts/
│   └── generar_informe.py       # Genera el .docx a partir de un JSON
└── assets/
    └── ejemplo_informe.json     # Ejemplo de entrada para el generador
```

## Instalación

**En Claude (web o app):** descarga `labrador.skill` desde [Releases](https://github.com/chocolistolisto/labrador/releases) y súbelo en la sección de Skills de tu configuración.

**En Claude Code:** copia la carpeta `labrador/` a tu directorio de skills:

```bash
git clone https://github.com/chocolistolisto/labrador.git
cp -r labrador/labrador ~/.claude/skills/
```

El generador de Word necesita Python 3 y `python-docx` (`pip install python-docx`).

## Uso

No hace falta nombrar la skill: basta con pedir el informe. Por ejemplo:

> Hazme el informe del laboratorio de Física sobre el péndulo simple. Te adjunto la guía, la tabla con los periodos que medimos para cinco longitudes distintas y la foto del montaje. Agrega portada y un anexo con los cálculos. Somos Ana Pérez y Luis Gómez, docente Carlos Ruiz.

Funciona igual para cualquier materia. Por ejemplo:

> Necesito el informe de la práctica de Química: titulación ácido-base de vinagre con NaOH. Te paso los volúmenes gastados en las tres repeticiones y las fotos del viraje del indicador.

Mientras más evidencia le des (fotos, tablas de datos, mediciones, capturas), mejor queda la sección de resultados.

### Generar el Word a mano

Si ya tienes el contenido en JSON (con la estructura de `assets/ejemplo_informe.json`):

```bash
python labrador/scripts/generar_informe.py informe.json informe.docx
```

En los textos puedes usar `**negrita**`, `*cursiva*` y referencias `{fig:id}` / `{tab:id}`, que el script convierte en "Figura N" y "Tabla N" automáticamente.

## Autores

- **Santiago Pinzón Vásquez** — [@Chocax](https://github.com/Chocax)
- **Laura Gabriela Díaz Amaya** — [@Diganme-Gaby](https://github.com/Diganme-Gaby)

## Licencia

[MIT](LICENSE)
