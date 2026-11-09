#!/usr/bin/env python3
"""
LABrador: genera un informe de laboratorio en Word (.docx) con formato APA 7
a partir de un archivo JSON.

Uso:
    python generar_informe.py informe.json salida.docx

La estructura del JSON está documentada en assets/ejemplo_informe.json.

Marcado en los textos:
    **negrita**   *cursiva*
    {fig:id}  -> "Figura N"     {tab:id} -> "Tabla N"

Requiere python-docx (pip install python-docx).
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

try:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:
    sys.exit("Falta python-docx. Instálalo con: pip install python-docx")


FORMATO_POR_DEFECTO = {
    "fuente": "Times New Roman",
    "tamano": 12,
    "interlineado": 1.15,
    "espacio_despues": 8,
    "alineacion": "justificado",      # justificado | izquierda
    "sangria_primera_linea_cm": 0,
    "margen_cm": 2.54,
    "papel": "carta",                 # carta | a4
    "titulos_con_dos_puntos": True,   # "Introducción:" como en los informes de referencia
    "numerar_paginas": True,
    "referencias_en_pagina_nueva": True,
    "ancho_figura_cm": 15,
}

ALINEACIONES = {
    "justificado": WD_ALIGN_PARAGRAPH.JUSTIFY,
    "izquierda": WD_ALIGN_PARAGRAPH.LEFT,
    "centrado": WD_ALIGN_PARAGRAPH.CENTER,
}

PATRON_REF = re.compile(r"\{(fig|tab):([A-Za-z0-9_\-]+)\}")
PATRON_MARCADO = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")

avisos = []


# ---------------------------------------------------------------- utilidades

def avisar(mensaje):
    avisos.append(mensaje)


def clave_orden(texto):
    """Orden alfabético ignorando tildes, mayúsculas y el marcado de cursiva."""
    limpio = texto.replace("*", "")
    sin_tildes = unicodedata.normalize("NFKD", limpio)
    sin_tildes = "".join(c for c in sin_tildes if not unicodedata.combining(c))
    return sin_tildes.casefold()


def bloques_de(seccion):
    """Devuelve los bloques de una sección; acepta cadenas como párrafos."""
    for bloque in seccion.get("bloques", []):
        yield {"tipo": "parrafo", "texto": bloque} if isinstance(bloque, str) else bloque


def todas_las_secciones(datos):
    yield from datos.get("secciones", [])
    yield from datos.get("anexos", [])


# --------------------------------------------------- numeración de figuras

def numerar(datos):
    numeros = {"fig": {}, "tab": {}}
    contador = {"fig": 0, "tab": 0}
    for seccion in todas_las_secciones(datos):
        for bloque in bloques_de(seccion):
            tipo = {"figura": "fig", "tabla": "tab"}.get(bloque.get("tipo"))
            if not tipo:
                continue
            contador[tipo] += 1
            ident = bloque.get("id") or f"{tipo}{contador[tipo]}"
            if ident in numeros[tipo]:
                avisar(f"El id '{ident}' está repetido; se usará la primera aparición.")
                continue
            numeros[tipo][ident] = contador[tipo]
            bloque["_numero"] = contador[tipo]
    return numeros


def resolver_referencias(texto, numeros):
    def reemplazo(m):
        tipo, ident = m.group(1), m.group(2)
        n = numeros[tipo].get(ident)
        nombre = "Figura" if tipo == "fig" else "Tabla"
        if n is None:
            avisar(f"Referencia a {tipo}:{ident} sin figura o tabla con ese id.")
            return f"{nombre} [?]"
        return f"{nombre} {n}"
    return PATRON_REF.sub(reemplazo, texto)


# ------------------------------------------------------------ formato base

def configurar_documento(doc, fmt):
    estilo = doc.styles["Normal"]
    estilo.font.name = fmt["fuente"]
    estilo.font.size = Pt(fmt["tamano"])
    estilo.element.rPr.rFonts.set(qn("w:eastAsia"), fmt["fuente"])
    pf = estilo.paragraph_format
    pf.line_spacing = fmt["interlineado"]
    pf.space_after = Pt(fmt["espacio_despues"])
    pf.space_before = Pt(0)

    for nombre, alineacion in (("Heading 1", WD_ALIGN_PARAGRAPH.CENTER),
                               ("Heading 2", WD_ALIGN_PARAGRAPH.LEFT)):
        h = doc.styles[nombre]
        h.font.name = fmt["fuente"]
        h.font.size = Pt(fmt["tamano"])
        h.font.bold = True
        h.font.italic = False
        h.font.color.rgb = RGBColor(0, 0, 0)
        rpr = h.element.get_or_add_rPr()
        fuentes = rpr.find(qn("w:rFonts"))
        if fuentes is None:
            fuentes = OxmlElement("w:rFonts")
            rpr.append(fuentes)
        for atributo in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            fuentes.set(qn(atributo), fmt["fuente"])
        for atributo in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            fuentes.attrib.pop(qn(atributo), None)
        h.paragraph_format.alignment = alineacion
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(12)
        h.paragraph_format.keep_with_next = True

    seccion = doc.sections[0]
    if fmt["papel"] == "a4":
        seccion.page_width, seccion.page_height = Cm(21), Cm(29.7)
    else:
        seccion.page_width, seccion.page_height = Cm(21.59), Cm(27.94)
    margen = Cm(fmt["margen_cm"])
    seccion.left_margin = seccion.right_margin = margen
    seccion.top_margin = seccion.bottom_margin = margen

    if fmt["numerar_paginas"]:
        agregar_numero_pagina(seccion)


def agregar_numero_pagina(seccion):
    p = seccion.header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run()
    for tipo, texto in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipo:
            campo = OxmlElement("w:fldChar")
            campo.set(qn("w:fldCharType"), tipo)
            run._r.append(campo)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = texto
            run._r.append(instr)


def escribir_marcado(parrafo, texto, numeros, cursiva_base=False):
    """Agrega texto con **negrita** y *cursiva* a un párrafo."""
    texto = resolver_referencias(texto, numeros)
    for trozo in PATRON_MARCADO.split(texto):
        if not trozo:
            continue
        if trozo.startswith("**") and trozo.endswith("**") and len(trozo) > 4:
            run = parrafo.add_run(trozo[2:-2])
            run.bold = True
            run.italic = cursiva_base or None
        elif trozo.startswith("*") and trozo.endswith("*") and len(trozo) > 2:
            run = parrafo.add_run(trozo[1:-1])
            run.italic = not cursiva_base
        else:
            run = parrafo.add_run(trozo)
            run.italic = cursiva_base or None


def parrafo_texto(doc, texto, fmt, numeros, alineacion=None, sangria=True):
    p = doc.add_paragraph()
    p.alignment = alineacion or ALINEACIONES.get(fmt["alineacion"], WD_ALIGN_PARAGRAPH.JUSTIFY)
    if sangria and fmt["sangria_primera_linea_cm"]:
        p.paragraph_format.first_line_indent = Cm(fmt["sangria_primera_linea_cm"])
    escribir_marcado(p, texto, numeros)
    return p


def borde_celda(celda, **lados):
    """lados: top/bottom/left/right = 'single' | 'nil'"""
    tcPr = celda._tc.get_or_add_tcPr()
    bordes = tcPr.find(qn("w:tcBorders"))
    if bordes is None:
        bordes = OxmlElement("w:tcBorders")
        tcPr.append(bordes)
    for lado, valor in lados.items():
        elem = OxmlElement(f"w:{lado}")
        elem.set(qn("w:val"), valor)
        if valor != "nil":
            elem.set(qn("w:sz"), "8")
            elem.set(qn("w:color"), "000000")
        bordes.append(elem)


def quitar_bordes_tabla(tabla):
    tblPr = tabla._tbl.tblPr
    bordes = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        elem = OxmlElement(f"w:{lado}")
        elem.set(qn("w:val"), "nil")
        bordes.append(elem)
    tblPr.append(bordes)


def compactar(parrafo, despues=0):
    parrafo.paragraph_format.space_after = Pt(despues)
    parrafo.paragraph_format.space_before = Pt(0)
    parrafo.paragraph_format.line_spacing = 1.0


# ------------------------------------------------------------------ bloques

def rotulo(doc, etiqueta, numero, titulo, numeros):
    """'Figura N' en negrita y el título en cursiva, como en APA 7."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_after = Pt(2)
    p.add_run(f"{etiqueta} {numero}").bold = True
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_after = Pt(6)
    escribir_marcado(p, titulo or f"[COMPLETAR: título de la {etiqueta.lower()}]", numeros, cursiva_base=True)


def nota(doc, texto, numeros):
    if not texto:
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(12)
    p.add_run("Nota").italic = True
    p.add_run(". ")
    escribir_marcado(p, texto, numeros)


def bloque_figura(doc, bloque, fmt, numeros, base):
    numero = bloque.get("_numero", "?")
    rotulo(doc, "Figura", numero, bloque.get("titulo"), numeros)
    ancho = Cm(bloque.get("ancho_cm", fmt["ancho_figura_cm"]))
    ruta = bloque.get("imagen")
    ruta_completa = (base / ruta) if ruta and not Path(ruta).is_absolute() else (Path(ruta) if ruta else None)

    if ruta_completa and ruta_completa.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = True
        compactar(p)
        try:
            p.add_run().add_picture(str(ruta_completa), width=ancho)
        except Exception as error:  # imagen dañada o formato no soportado
            avisar(f"Figura {numero}: no se pudo insertar '{ruta}' ({error}).")
            marcador_imagen(doc, bloque, ancho)
    else:
        if ruta:
            avisar(f"Figura {numero}: no se encontró la imagen '{ruta}'; se dejó un recuadro.")
        else:
            avisar(f"Figura {numero}: sin imagen; se dejó un recuadro para insertarla.")
        marcador_imagen(doc, bloque, ancho)
    nota(doc, bloque.get("nota"), numeros)


def marcador_imagen(doc, bloque, ancho):
    tabla = doc.add_table(rows=1, cols=1)
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    celda = tabla.cell(0, 0)
    celda.width = ancho
    borde_celda(celda, top="single", bottom="single", left="single", right="single")
    p = celda.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    descripcion = bloque.get("descripcion_imagen") or bloque.get("titulo") or "imagen"
    run = p.add_run(f"\n[Insertar imagen: {descripcion.replace('*', '')}]\n")
    run.italic = True
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)


def bloque_tabla(doc, bloque, fmt, numeros, base):
    numero = bloque.get("_numero", "?")
    rotulo(doc, "Tabla", numero, bloque.get("titulo"), numeros)
    encabezados = bloque.get("encabezados", [])
    filas = bloque.get("filas", [])
    columnas = max([len(encabezados)] + [len(f) for f in filas] or [1])

    tabla = doc.add_table(rows=1 + len(filas), cols=columnas)
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    quitar_bordes_tabla(tabla)

    for j in range(columnas):
        celda = tabla.cell(0, j)
        texto = str(encabezados[j]) if j < len(encabezados) else ""
        p = celda.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        compactar(p)
        run = p.add_run(texto.replace("*", ""))
        run.bold = True
        borde_celda(celda, top="single", bottom="single")

    for i, fila in enumerate(filas, start=1):
        for j in range(columnas):
            celda = tabla.cell(i, j)
            texto = str(fila[j]) if j < len(fila) else ""
            p = celda.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            compactar(p)
            escribir_marcado(p, texto, numeros)
            if i == len(filas):
                borde_celda(celda, bottom="single")
    nota(doc, bloque.get("nota"), numeros)


def bloque_lista(doc, bloque, fmt, numeros, base):
    estilo = "List Number" if bloque.get("numerada") else "List Bullet"
    for item in bloque.get("items", []):
        p = doc.add_paragraph(style=estilo)
        p.alignment = ALINEACIONES.get(fmt["alineacion"], WD_ALIGN_PARAGRAPH.JUSTIFY)
        p.paragraph_format.space_after = Pt(4)
        escribir_marcado(p, item, numeros)


def bloque_codigo(doc, bloque, fmt, numeros, base):
    tabla = doc.add_table(rows=1, cols=1)
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    celda = tabla.cell(0, 0)
    borde_celda(celda, top="single", bottom="single", left="single", right="single")
    lineas = bloque.get("texto", "").split("\n")
    p = celda.paragraphs[0]
    compactar(p)
    for k, linea in enumerate(lineas):
        run = p.add_run(linea)
        run.font.name = "Consolas"
        run._element.rPr.rFonts.set(qn("w:eastAsia"), "Consolas")
        run.font.size = Pt(fmt["tamano"] - 2)
        if k < len(lineas) - 1:
            run.add_break()
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def bloque_marcador(doc, bloque, fmt, numeros, base):
    p = doc.add_paragraph()
    run = p.add_run(f"[COMPLETAR: {bloque.get('texto', '')}]")
    run.bold = True
    run.font.highlight_color = 7  # amarillo
    avisar(f"Marcador pendiente: {bloque.get('texto', '')}")


def bloque_subtitulo(doc, bloque, fmt, numeros, base):
    doc.add_heading(resolver_referencias(bloque.get("texto", ""), numeros).replace("*", ""), level=2)


def bloque_parrafo(doc, bloque, fmt, numeros, base):
    texto = bloque.get("texto", "")
    if "[COMPLETAR" in texto:
        avisar(f"Texto con marcador pendiente: {texto[:60]}…")
    parrafo_texto(doc, texto, fmt, numeros)


def bloque_salto(doc, bloque, fmt, numeros, base):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


MANEJADORES = {
    "parrafo": bloque_parrafo,
    "subtitulo": bloque_subtitulo,
    "lista": bloque_lista,
    "figura": bloque_figura,
    "tabla": bloque_tabla,
    "codigo": bloque_codigo,
    "marcador": bloque_marcador,
    "salto_pagina": bloque_salto,
}


# ------------------------------------------------------------------ partes

def portada(doc, datos, fmt):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(120)
    centro = WD_ALIGN_PARAGRAPH.CENTER
    lineas = []
    if datos.get("titulo"):
        lineas.append((datos["titulo"], True))
    if datos.get("asignatura"):
        lineas.append((datos["asignatura"], False))
    lineas.append(("", False))
    for integrante in datos.get("integrantes", []):
        lineas.append((integrante, False))
    lineas.append(("", False))
    for clave in ("docente", "programa", "universidad", "fecha"):
        if datos.get(clave):
            lineas.append((datos[clave], False))
    for texto, negrita in lineas:
        q = doc.add_paragraph()
        q.alignment = centro
        q.paragraph_format.space_after = Pt(4)
        q.add_run(texto).bold = negrita
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def titulo_seccion(doc, texto, fmt, nueva_pagina=False):
    if nueva_pagina:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    texto = texto.strip().rstrip(":")
    if fmt["titulos_con_dos_puntos"]:
        texto += ":"
    doc.add_heading(texto, level=1)


def referencias(doc, lista, fmt, ordenar=True):
    if not lista:
        avisar("El informe no tiene referencias.")
        return
    if fmt["referencias_en_pagina_nueva"]:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    doc.add_heading("Referencias", level=1)
    for entrada in (sorted(lista, key=clave_orden) if ordenar else lista):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-1.27)
        escribir_marcado(p, entrada, {"fig": {}, "tab": {}})


def anexos(doc, lista, fmt, numeros, base):
    for i, anexo in enumerate(lista):
        letra = chr(ord("A") + i)
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        doc.add_heading(f"Anexo {letra}. {anexo.get('titulo', '').strip()}".rstrip(". "), level=1)
        for bloque in bloques_de(anexo):
            MANEJADORES.get(bloque.get("tipo"), bloque_parrafo)(doc, bloque, fmt, numeros, base)


def limpiar_parrafo_inicial(doc):
    """python-docx deja un párrafo vacío al inicio del cuerpo; se elimina."""
    cuerpo = doc.element.body
    primero = cuerpo[0]
    if primero.tag == qn("w:p") and not "".join(primero.itertext()).strip():
        cuerpo.remove(primero)


# -------------------------------------------------------------------- main

def generar(ruta_json, ruta_salida):
    ruta_json = Path(ruta_json)
    with open(ruta_json, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    fmt = {**FORMATO_POR_DEFECTO, **datos.get("formato", {})}
    base = ruta_json.parent
    numeros = numerar(datos)

    doc = Document()
    configurar_documento(doc, fmt)
    limpiar_parrafo_inicial(doc)

    if datos.get("portada"):
        portada(doc, datos["portada"], fmt)

    for seccion in datos.get("secciones", []):
        titulo_seccion(doc, seccion.get("titulo", "Sección"), fmt, seccion.get("pagina_nueva", False))
        for bloque in bloques_de(seccion):
            manejador = MANEJADORES.get(bloque.get("tipo"))
            if manejador is None:
                avisar(f"Tipo de bloque desconocido '{bloque.get('tipo')}'; se trató como párrafo.")
                manejador = bloque_parrafo
            manejador(doc, bloque, fmt, numeros, base)

    referencias(doc, datos.get("referencias", []), fmt, datos.get("ordenar_referencias", True))
    anexos(doc, datos.get("anexos", []), fmt, numeros, base)

    doc.save(ruta_salida)
    return numeros


def main():
    parser = argparse.ArgumentParser(description="Genera un informe de laboratorio .docx (APA 7) desde JSON.")
    parser.add_argument("json", help="Archivo JSON con el contenido del informe")
    parser.add_argument("salida", help="Ruta del .docx a generar")
    args = parser.parse_args()

    numeros = generar(args.json, args.salida)
    print(f"Informe generado: {args.salida}")
    print(f"Figuras: {len(numeros['fig'])} | Tablas: {len(numeros['tab'])}")
    if avisos:
        print("\nAvisos:")
        for aviso in avisos:
            print(f"  - {aviso}")


if __name__ == "__main__":
    main()
