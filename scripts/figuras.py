"""Ilustraciones SVG propias de los artículos del blog.

Todas son dibujos originales (no hay imágenes de terceros) y llevan texto real
dentro del SVG, de modo que los buscadores y los lectores de pantalla lo leen.
Los importes y los datos que aparecen son ficticios y siempre se indican como tales.
"""
from html import escape as E

INK, INK2, BLUE, BLUE2, BLUE3 = "#14171a", "#3d444c", "#10699f", "#2f9be0", "#5fb6ea"
LINE, CARD, MUTED = "#d6d6d6", "#e8e8e8", "#5f6770"
RED, REDBG, AMBER, AMBERBG, GREEN, GREENBG = "#b3261e", "#fbe9e7", "#9a6200", "#fff4d9", "#1a7f3c", "#e3f3e7"


def svg(nombre, w, h, interior, etiqueta):
    marcadores = "".join(
        f'<marker id="a{c}-{nombre}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M0 0L10 5L0 10z" fill="{col}"/></marker>'
        for c, col in (("b", BLUE), ("g", MUTED), ("r", RED), ("v", GREEN)))
    return (f'<svg viewBox="-10 -10 {w + 20} {h + 20}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{E(etiqueta)}">'
            f'<defs>{marcadores}</defs>{interior}</svg>')


def fig(nombre, w, h, interior, etiqueta, pie):
    return f'<figure class="fig">{svg(nombre, w, h, interior, etiqueta)}<figcaption>{pie}</figcaption></figure>'


def t(x, y, s, size=16, weight=400, fill=INK, anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{E(s)}</text>'


def tl(x, y, lineas, size=16, weight=400, fill=INK, anchor="middle", lh=None):
    lh = lh or round(size * 1.28)
    return "".join(t(x, y + i * lh, s, size, weight, fill, anchor) for i, s in enumerate(lineas))


def r(x, y, w, h, fill="#fff", stroke=LINE, rx=0, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def ln(x1, y1, x2, y2, col=LINE, sw=1.5, dash=None, marca=None, nombre=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#a{marca}-{nombre})"' if marca else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{d}{m}/>'


def badge(cx, cy, n, relleno=True, rad=13):
    fondo, texto = (BLUE, "#fff") if relleno else ("#fff", BLUE)
    return (f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="{fondo}" stroke="{BLUE}" stroke-width="2"/>'
            + t(cx, cy + 5, str(n), 14, 700, texto, "middle"))


# ───────────────────────── cruzar-albaranes-con-facturas ─────────────────────────

def cruce_tres():
    n = "cruce3"
    cols = [("Pedido", ["Lo que pedisteis", "y a qué precio"], BLUE),
            ("Albarán", ["Lo que llegó", "(prueba de entrega)"], BLUE2),
            ("Factura", ["Lo que os cobran", "y lo que pagaréis"], INK)]
    x0 = [10, 215, 420]
    s = ""
    for (nombre, sub, col), x in zip(cols, x0):
        s += r(x, 20, 170, 140, "#fff", LINE)
        s += r(x, 20, 170, 44, col, col)
        s += t(x + 85, 50, nombre, 22, 700, "#fff", "middle")
        s += r(x + 52, 82, 66, 52, "#f3f6f9", LINE) + "".join(ln(x + 62, 94 + i * 12, x + 108 - (i % 2) * 14, 94 + i * 12, "#9aa3ad", 3) for i in range(4))
    # subtítulos bajo el icono
    for (nombre, sub, col), x in zip(cols, x0):
        s += tl(x + 85, 178, sub, 16, 400, INK2)
    s += ln(182, 92, 212, 92, MUTED, 2, marca="g", nombre=n) + ln(387, 92, 417, 92, MUTED, 2, marca="g", nombre=n)
    for x in x0:
        s += ln(x + 85, 212, x + 85, 232, MUTED, 2)
    s += ln(95, 232, 505, 232, MUTED, 2)
    s += r(150, 250, 300, 38, BLUE, BLUE, 19) + t(300, 275, "¿Coinciden cantidades y precios?", 17, 600, "#fff", "middle")
    s += ln(300, 232, 300, 250, MUTED, 2)
    return fig(n, 600, 300, s, "Esquema del cruce a tres bandas: pedido, albarán y factura deben coincidir en cantidades y precios",
               "El cruce compara tres documentos: lo que se pidió (con el precio pactado), lo que llegó y lo que se factura.")


def albaran_vs_factura():
    n = "avf"
    s = ""
    # albarán
    s += r(10, 10, 270, 190, "#fff", LINE) + r(10, 10, 270, 40, INK, INK)
    s += t(24, 36, "ALBARÁN A-1001", 17, 700, "#fff") + t(266, 36, "lo recibido", 15, 400, BLUE3, "end")
    filas_a = [("Cemento 25 kg", "20", "5,20"), ("Arena lavada", "2 m³", "28,00")]
    s += t(24, 76, "Concepto", 14, 600, MUTED) + t(200, 76, "Cant.", 14, 600, MUTED, "end") + t(262, 76, "Precio", 14, 600, MUTED, "end")
    for i, (c, q, p) in enumerate(filas_a):
        y = 108 + i * 40
        s += t(24, y, c, 17) + t(200, y, q, 17, 400, INK, "end") + t(262, y, p, 17, 400, INK, "end")
    # factura
    s += r(320, 10, 270, 190, "#fff", LINE) + r(320, 10, 270, 40, BLUE, BLUE)
    s += t(334, 36, "FACTURA F-5532", 17, 700, "#fff") + t(576, 36, "lo cobrado", 15, 400, "#dbeeff", "end")
    s += t(334, 76, "Concepto", 14, 600, MUTED) + t(510, 76, "Cant.", 14, 600, MUTED, "end") + t(572, 76, "Precio", 14, 600, MUTED, "end")
    filas_f = [("Cemento 25 kg", "20", "5,90", 1, "precio"), ("Arena lavada", "3 m³", "28,00", 2, "cant"), ("Porte", "1", "45,00", 3, "porte")]
    for i, (c, q, p, k, tipo) in enumerate(filas_f):
        y = 108 + i * 40
        s += r(326, y - 24, 258, 34, REDBG, RED, 0, 1)
        s += t(334, y, c, 17) + t(510, y, q, 17, tipo == "cant" and 700 or 400, RED if tipo == "cant" else INK, "end") + t(572, y, p, 17, tipo != "cant" and 700 or 400, RED if tipo != "cant" else INK, "end")
        s += badge(300, y - 7, k, True, 12).replace(BLUE, RED)
    # leyenda
    leyenda = ["Precio distinto al pactado", "Más cantidad de la que llegó", "Porte que nadie había acordado"]
    for i, txt in enumerate(leyenda):
        y = 238 + i * 32
        s += badge(26, y - 5, i + 1, True, 12).replace(BLUE, RED) + t(48, y, txt, 17)
    s += t(590, 290, "Datos ficticios, solo ilustrativos", 14, 400, MUTED, "end")
    return fig(n, 600, 310, s, "Comparación entre un albarán y una factura con tres diferencias marcadas",
               "Tres diferencias típicas que solo aparecen al comparar línea a línea (ejemplo ilustrativo con datos inventados).")


# ───────────────────────── ocr-o-ia-para-leer-facturas ─────────────────────────

def ocr_vs_ia():
    n = "ocria"
    s = ""
    def carril(y, titulo, cajas, col, fondo, nota, colnota):
        o = t(0, y - 8, titulo, 15, 600, col, "start", 'letter-spacing=".08em"')
        for i, txt in enumerate(cajas):
            x = i * 154
            o += r(x, y, 124, 64, fondo, col, 0, 1.5) + tl(x + 62, y + 28 - (len(txt) - 1) * 9, txt, 16, 600, INK)
            if i < len(cajas) - 1:
                o += ln(x + 126, y + 32, x + 150, y + 32, col, 2, marca="g" if col == MUTED else "b", nombre=n)
        o += t(0, y + 94, nota, 16, 600, colnota)
        return o
    s += carril(34, "OCR CON PLANTILLAS", [["Imagen", "o PDF"], ["Texto", "sin interpretar"], ["Reglas por", "proveedor"], ["Campos", "extraídos"]], MUTED, "#f4f4f4",
                "Si el proveedor cambia el formato, hay que rehacer la regla", RED)
    s += carril(182, "IA QUE ENTIENDE EL DOCUMENTO", [["Imagen", "o PDF"], ["Interpreta el", "documento"], ["Campos +", "confianza"], ["Revisión", "solo si duda"]], BLUE, "#eaf4fb",
                "Un formato nuevo no rompe nada: se lee como lo haría una persona", GREEN)
    return fig(n, 600, 300, s, "Comparación del recorrido de un documento con OCR con plantillas y con IA",
               "Cómo recorre una factura cada enfoque. La diferencia está en el paso del medio: aplicar reglas fijas o interpretar el documento.")


def tabla_ocr_ia():
    filas = [
        ("Proveedor nuevo", "Hace falta crear una plantilla", "Se lee sin preparar nada"),
        ("Cambio de formato", "Puede dejar de funcionar", "Se adapta"),
        ("Foto torcida o anotaciones a mano", "Suele fallar", "Los maneja mejor"),
        ("Distinguir descuentos, portes y líneas", "Solo si la plantilla lo prevé", "Los interpreta por contexto"),
        ("Comprobar que las líneas suman el total", "No", "Sí"),
        ("Qué hace cuando duda", "Normalmente, nada: da el dato por bueno", "Lo marca para revisión"),
        ("Encaja mejor cuando…", "Pocos proveedores, siempre el mismo PDF", "Muchos proveedores, formatos variados, fotos"),
    ]
    cuerpo = "".join(f"<tr><th scope=\"row\">{E(a)}</th><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in filas)
    return (f'<figure class="fig"><div class="tablewrap"><table class="cmp"><thead><tr><th></th><th>OCR con plantillas</th><th>IA que interpreta el documento</th></tr></thead>'
            f'<tbody>{cuerpo}</tbody></table></div><figcaption>Comparación general entre los dos enfoques. Productos concretos pueden variar.</figcaption></figure>')


# ───────────────────────── tareas-administrativas-automatizar-pyme ─────────────────────────

def siete_tareas():
    tareas = ["Registrar facturas de proveedor", "Cruzar albaranes con facturas", "Preparar presupuestos", "Facturar trabajos y servicios",
              "Dar de alta pedidos por correo", "Clasificar correos y documentos", "Informes semanales"]
    li = "".join(f"<li><b>{i+1:02d}</b>{E(x)}</li>" for i, x in enumerate(tareas))
    li += '<li class="last"><b>EMPEZAR</b>Por una sola: la que más horas os quita</li>'
    return f'<ul class="tiles" aria-label="Las siete tareas">{li}</ul>'


def esfuerzo_impacto():
    n = "matriz"
    X0, X1, Y0, Y1 = 70, 580, 20, 330
    s = r(X0, Y0, X1 - X0, Y1 - Y0, "#fff", LINE)
    xm, ym = (X0 + X1) // 2, (Y0 + Y1) // 2
    s += r(X0, Y0, xm - X0, ym - Y0, GREENBG, "none")
    s += ln(xm, Y0, xm, Y1, LINE, 1.5, "5 5") + ln(X0, ym, X1, ym, LINE, 1.5, "5 5")
    s += t(X0 + 10, Y0 + 24, "Empezar por aquí", 16, 700, GREEN)
    s += t(X1 - 10, Y0 + 24, "Con retorno, pero más trabajo", 15, 600, MUTED, "end")
    s += t(X0 + 10, Y1 - 12, "Pequeños extras", 15, 600, MUTED)
    s += t(X1 - 10, Y1 - 12, "Para más adelante", 15, 600, MUTED, "end")
    s += t((X0 + X1) // 2, 366, "Esfuerzo de ponerlo en marcha  →", 16, 600, INK2, "middle")
    s += f'<text transform="translate(26 {(Y0+Y1)//2}) rotate(-90)" font-size="16" font-weight="600" fill="{INK2}" text-anchor="middle">Horas que ahorra  →</text>'
    puntos = [(1, .16, .84), (2, .40, .93), (3, .72, .80), (4, .46, .68), (5, .63, .40), (6, .22, .28), (7, .28, .58)]
    for k, ex, im in puntos:
        cx, cy = X0 + ex * (X1 - X0), Y1 - im * (Y1 - Y0)
        s += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="17" fill="{BLUE}"/>' + t(f"{cx:.0f}", f"{cy+6:.0f}", str(k), 17, 700, "#fff", "middle")
    return fig(n, 600, 380, s, "Matriz orientativa de esfuerzo frente a ahorro de horas para siete tareas administrativas",
               "Valoración orientativa de SuxtrAI; en cada empresa cambia. 1 Facturas de proveedor · 2 Cruce de albaranes · 3 Presupuestos · 4 Facturar trabajos · 5 Pedidos por correo · 6 Clasificar documentos · 7 Informes.")


# ───────────────────────── control-costes-por-obra ─────────────────────────

def presupuesto_vs_real():
    n = "barras"
    datos = [("Demolición", 92), ("Albañilería", 118), ("Fontanería", 70), ("Electricidad", 104), ("Alicatados", 85)]
    X0, ESC = 150, 3.0   # 0..140 % -> 420 px
    s = ""
    x100, x110 = X0 + 100 * ESC, X0 + 110 * ESC
    s += ln(x100, 38, x100, 296, INK, 1.5, "4 4") + t(x100 - 6, 28, "Presupuesto", 15, 600, INK, "end")
    s += ln(x110, 38, x110, 296, AMBER, 1.5, "4 4") + t(x110 + 6, 28, "+10 %", 15, 600, AMBER, "start")
    for i, (nom, v) in enumerate(datos):
        y = 58 + i * 48
        mal = v > 110
        s += t(X0 - 14, y + 20, nom, 17, 400, INK, "end")
        s += r(X0, y, 140 * ESC, 28, "#f1f1f1", "none")
        s += r(X0, y, v * ESC, 28, RED if mal else BLUE, "none")
        s += t(X0 + v * ESC - 8 if v * ESC > 70 else X0 + v * ESC + 8, y + 20, f"{v} %", 16, 700, "#fff" if v * ESC > 70 else INK,
               "end" if v * ESC > 70 else "start")
    s += t(X0, 322, "Gasto acumulado respecto a lo presupuestado en cada partida", 15, 400, MUTED)
    return fig(n, 600, 336, s, "Gráfico de barras: gasto acumulado frente a presupuesto por partida, con una partida por encima del umbral",
               "Ejemplo ilustrativo con datos inventados. Al comparar por partidas se ve enseguida cuál se ha desviado más del umbral fijado (aquí, un 10 %).")


def albaran_antes_que_factura():
    n = "linea"
    s = ln(40, 112, 570, 112, MUTED, 3, marca="g", nombre=n)
    nodos = [(60, "Pedido", ""), (200, "Albarán", "día de entrega"), (440, "Factura", "semanas después"), (540, "Pago", "")]
    for x, nom, sub in nodos:
        col = BLUE if nom == "Albarán" else INK
        s += f'<circle cx="{x}" cy="112" r="12" fill="{col}"/>' + t(x, 84, nom, 19, 700, col, "middle")
        if sub:
            s += t(x, 56, sub, 15, 400, MUTED, "middle")
    s += ln(200, 152, 438, 152, RED, 3, marca="r", nombre=n) + t(200, 180, "Gasto invisible si esperáis a la factura", 17, 600, RED)
    s += ln(200, 208, 568, 208, GREEN, 3, marca="v", nombre=n) + t(200, 236, "Con el albarán registrado, el gasto consta", 17, 600, GREEN)
    return fig(n, 600, 250, s, "Línea de tiempo: el albarán llega semanas antes que la factura",
               "El material se recibe el día del albarán; la factura llega después. Registrar el gasto al recibir el albarán permite reaccionar a tiempo.")


# ───────────────────────── imputar-albaranes-a-obra ─────────────────────────

def albaran_anotado():
    n = "alba"
    s = r(10, 10, 400, 370, "#fff", LINE)
    s += r(10, 10, 400, 46, INK, INK) + t(26, 40, "ALBARÁN Nº A-1001", 19, 700, "#fff") + t(394, 40, "Materiales Ejemplo S.L.", 14, 400, BLUE3, "end")
    campos = [(4, 94, "Fecha:", "02/11/2026"), (2, 134, "Pedido nº:", "P-0457"), (1, 174, "Ref. obra:", "2026-014"), (3, 214, "Entregar en:", "C/ Ejemplo 12, Leioa")]
    for k, y, et, val in campos:
        s += r(22, y - 24, 340, 34, "#eaf4fb", BLUE, 0, 1.5, "4 3")
        s += t(32, y, et, 16, 400, MUTED) + t(140, y, val, 17, 600)
        s += badge(386, y - 7, k)
    s += t(26, 266, "Concepto", 14, 600, MUTED) + t(300, 266, "Cant.", 14, 600, MUTED, "end") + t(394, 266, "Precio", 14, 600, MUTED, "end")
    s += ln(22, 274, 398, 274, LINE)
    for i, (c, q, p) in enumerate([("Cemento 25 kg", "40", "5,20"), ("Mortero cola", "20", "7,80"), ("Arena lavada", "2 m³", "28,00")]):
        y = 302 + i * 28
        s += t(26, y, c, 16) + t(300, y, q, 16, 400, INK, "end") + t(394, y, p, 16, 400, INK, "end")
    leyenda = [(1, ["Referencia", "de obra"]), (2, ["Número de", "pedido"]), (3, ["Dirección", "de entrega"]), (4, ["Fecha", "de entrega"])]
    s += t(432, 38, "Dónde buscar la obra", 15, 700, BLUE)
    for i, (k, lineas) in enumerate(leyenda):
        y = 90 + i * 62
        s += badge(448, y, k) + tl(472, y - 4, lineas, 16, 400, INK, "start")
    s += t(436, 350, "Datos ficticios, solo", 14, 400, MUTED) + t(436, 368, "ilustrativos", 14, 400, MUTED)
    return fig(n, 600, 390, s, "Albarán de ejemplo con los cuatro datos que ayudan a saber a qué obra pertenece",
               "Los datos que permiten asignar un albarán a su obra suelen estar en el propio documento, si se sabe dónde mirar.")


def decision_imputacion():
    n = "imputa"
    s = ""
    pasos = [("¿Trae la referencia de obra?", "Se asigna a esa obra"),
             ("¿El nº de pedido es de una obra conocida?", "Se asigna a la obra del pedido"),
             ("¿La dirección de entrega es una obra?", "Se propone esa obra")]
    for i, (q, a) in enumerate(pasos):
        y = 10 + i * 96
        s += r(0, y, 270, 64, "#fff", BLUE, 0, 2) + tl(135, y + 28 - (1 if len(q) > 32 else 0) * 0, [q] if len(q) <= 32 else [q[:q.rfind(" ", 0, 30)], q[q.rfind(" ", 0, 30) + 1:]], 16, 600, INK)
        s += ln(272, y + 32, 328, y + 32, GREEN, 2.5, marca="v", nombre=n) + t(300, y + 24, "Sí", 15, 700, GREEN, "middle")
        s += r(330, y, 270, 64, GREENBG, GREEN, 0, 1.5) + tl(465, y + 36, [a], 16, 600, INK)
        s += ln(135, y + 66, 135, y + 94, MUTED, 2.5, marca="g", nombre=n) + t(147, y + 86, "No", 15, 700, MUTED)
    y = 298
    s += r(0, y, 270, 64, AMBERBG, AMBER, 0, 2) + tl(135, y + 28, ["Pendiente de asignar"], 16, 700, INK) + tl(135, y + 48, ["una persona decide"], 15, 400, INK2)
    return fig(n, 600, 372, s, "Árbol de decisión para asignar un albarán a una obra",
               "Orden habitual para resolver un albarán: de la pista más fiable a la menos. Si ninguna funciona, no se adivina.")


# ───────────────────────── presupuesto-reforma-desde-visita ─────────────────────────

def tabla_presupuesto():
    filas = [
        ("cap", "1 · Demolición", "", "", "", "366,00"),
        ("", "Picado de alicatado", "m²", "18", "12,00", "216,00"),
        ("", "Retirada de escombros", "ud", "1", "150,00", "150,00"),
        ("cap", "2 · Albañilería", "", "", "", "180,00"),
        ("", "Tabique de ladrillo hueco", "m²", "6", "30,00", "180,00"),
        ("cap", "3 · Alicatados", "", "", "", "630,00"),
        ("", "Alicatado de paredes del baño", "m²", "18", "35,00", "630,00"),
    ]
    out = ""
    for tipo, c, u, q, p, imp in filas:
        if tipo == "cap":
            out += f'<tr class="cap"><th scope="row" colspan="4">{E(c)}</th><td class="num"><b>{imp}</b></td></tr>'
        else:
            out += f'<tr><td>{E(c)}</td><td>{u}</td><td class="num">{q}</td><td class="num">{p}</td><td class="num">{imp}</td></tr>'
    return ('<figure class="fig"><div class="tablewrap"><table class="cmp"><thead><tr><th>Partida</th><th>Ud.</th><th class="num">Cant.</th><th class="num">Precio (€)</th><th class="num">Importe (€)</th></tr></thead>'
            f'<tbody>{out}</tbody><tfoot><tr><td colspan="5"><b>No incluye:</b> mobiliario y sanitarios · <b>Plazo:</b> a indicar · <b>Pago:</b> a indicar</td></tr></tfoot></table></div>'
            '<figcaption>Estructura de ejemplo. Los importes son ficticios y no sirven como precios de referencia.</figcaption></figure>')


def flujo_presupuesto():
    pasos = [("La visita", "Notas, mediciones, fotos y alcance"), ("El borrador", "Partidas con vuestro tarifario"),
             ("La revisión", "Una persona ajusta y completa"), ("El envío", "PDF con vuestra plantilla")]
    return '<ol class="flow">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in pasos) + "</ol>"


# ───────────────────────── software-albaranes-constructoras ─────────────────────────

def tabla_opciones():
    cab = ["Opción", "Foto desde obra", "Lee formatos distintos", "Imputa a obra", "Cruza con factura"]
    filas = [
        ("Hoja de cálculo", ("no", "No"), ("no", "No: se teclea"), ("med", "A mano"), ("med", "Con plantilla")),
        ("Gestión de obra / ERP", ("med", "Según producto"), ("med", "Según producto"), ("si", "Sí"), ("med", "Parcial")),
        ("OCR con plantillas", ("med", "A veces"), ("med", "Con plantilla"), ("no", "No"), ("no", "No")),
        ("IA a medida", ("si", "Sí"), ("si", "Sí"), ("si", "Sí"), ("si", "Sí")),
    ]
    cuerpo = "".join(
        f"<tr><th scope=\"row\">{E(n)}</th>" + "".join(f'<td><span class="{c}">{E(tx)}</span></td>' for c, tx in cols) + "</tr>"
        for n, *cols in filas)
    return (f'<figure class="fig"><div class="tablewrap"><table class="cmp"><thead><tr>{"".join(f"<th>{E(x)}</th>" for x in cab)}</tr></thead><tbody>{cuerpo}</tbody></table></div>'
            '<figcaption>Valoración general por tipo de herramienta. Cada producto concreto puede variar: probadlo con vuestros documentos.</figcaption></figure>')


def si_entonces():
    filas = [("Pocos albaranes al mes y pocos proveedores", "Una hoja de cálculo bien montada"),
             ("Muchos albaranes, pero formatos estables", "Vuestro ERP o un OCR con plantillas"),
             ("Muchos proveedores, formatos variados o fotos desde la obra", "Lectura con IA a medida")]
    return '<ul class="sino">' + "".join(f'<li><span>{E(a)}</span><i>→</i><span class="r">{E(b)}</span></li>' for a, b in filas) + "</ul>"


# ───────────────────────── plantilla-excel-cruce-albaranes-facturas ─────────────────────────

def hoja_albaranes():
    cab = ["Nº albarán", "Concepto", "Recibido", "Facturado", "Diferencia (€)", "Estado"]
    filas = [
        ("A-1001", "Cemento 25 kg", "40", "40", "0,00", "ok", "Cuadra"),
        ("A-1001", "Mortero cola", "20", "20", "12,00", "mal", "Precio distinto"),
        ("A-1002", "Arena lavada", "3", "—", "—", "pend", "Sin facturar"),
        ("A-1003", "Tubo PVC", "10", "8", "−18,40", "mal", "Facturado de menos"),
        ("A-1004", "Tablero DM", "6", "12", "61,50", "mal", "Facturado de más o duplicado"),
    ]
    cuerpo = "".join(
        f'<tr><td>{a}</td><td>{E(b)}</td><td class="num">{c}</td><td class="num">{d}</td><td class="num">{e}</td><td class="est-{k}">{E(f)}</td></tr>'
        for a, b, c, d, e, k, f in filas)
    return (f'<figure class="fig"><div class="tablewrap"><table class="cmp"><caption>Hoja «Albaranes» (vista ilustrativa con datos inventados)</caption><thead><tr>{"".join(f"<th>{E(x)}</th>" for x in cab)}</tr></thead>'
            f'<tbody>{cuerpo}</tbody></table></div></figure>')


def kpis_plantilla():
    datos = [("4", "hojas: instrucciones, albaranes, facturas y resumen"), ("5", "estados que se colorean solos"), ("500", "líneas de albarán preparadas"), ("1.000", "líneas de factura preparadas")]
    return '<div class="kpis">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in datos) + "</div>"


# ───────────────────────── comprobar-factura-proveedor-antes-de-pagar ─────────────────────────

def factura_hotspots():
    n = "factura"
    s = r(40, 10, 520, 396, "#fff", LINE) + r(40, 10, 520, 8, BLUE, BLUE)
    s += t(56, 46, "Materiales Ejemplo S.L.", 18, 700) + t(56, 68, "NIF B-00000000", 15, 400, MUTED)
    s += t(56, 94, "Facturar a: Vuestra Empresa S.L. · NIF B-11111111", 16, 400, INK2)
    s += badge(20, 70, 1, False)
    s += t(544, 46, "FACTURA F-5532", 18, 700, BLUE, "end") + t(544, 68, "Fecha: 30/11/2026", 15, 400, MUTED, "end")
    s += badge(580, 56, 2, False)
    # cabecera de tabla con los números encima de cada columna
    s += r(52, 134, 496, 34, "#f3f6f9", LINE)
    for nm, x, a in [("Concepto", 64, "start"), ("Albarán", 250, "start"), ("Cant.", 400, "end"), ("Precio", 470, "end"), ("Importe", 538, "end")]:
        s += t(x, 157, nm, 15, 600, MUTED, a)
    s += badge(102, 122, 3, False, 11) + badge(278, 122, 9, True, 11) + badge(374, 122, 4, True, 11) + badge(444, 122, 5, True, 11)
    filas = [("Cemento 25 kg", "A-1001", "40", "5,20", "208,00"), ("Mortero cola", "A-1001", "20", "7,80", "156,00"),
             ("Descuento 3 %", "", "", "", "−10,92"), ("Porte", "", "1", "45,00", "45,00")]
    for i, (c, a, q, p, imp) in enumerate(filas):
        y = 192 + i * 32
        s += t(64, y, c, 16) + t(250, y, a, 16) + t(400, y, q, 16, 400, INK, "end") + t(470, y, p, 16, 400, INK, "end") + t(538, y, imp, 16, 400, INK, "end")
        s += ln(52, y + 10, 548, y + 10, "#ececec")
    s += badge(20, 252, 6, True) + badge(20, 284, 7, True)
    s += r(330, 314, 218, 80, "#f3f6f9", LINE)
    for i, (a, v) in enumerate([("Base imponible", "398,08"), ("IVA 21 %", "83,60"), ("TOTAL", "481,68")]):
        y = 336 + i * 24
        w = 700 if i == 2 else 400
        s += t(344, y, a, 16, w) + t(538, y, v, 16, w, INK, "end")
    s += badge(580, 354, 8, True)
    s += t(64, 346, "Vencimiento: 30 días", 16, 400, INK2) + t(64, 370, "Forma de pago: transferencia", 16, 400, INK2)
    s += badge(20, 358, 10, False)
    # leyenda
    s += f'<circle cx="22" cy="432" r="10" fill="{BLUE}"/>' + t(40, 438, "Automatizable (4 a 9)", 15, 400, INK2)
    s += f'<circle cx="250" cy="432" r="10" fill="#fff" stroke="{BLUE}" stroke-width="2"/>' + t(268, 438, "Requiere criterio (1 a 3 y 10)", 15, 400, INK2)
    s += t(590, 466, "Datos ficticios, solo ilustrativos", 14, 400, MUTED, "end")
    return fig(n, 600, 476, s, "Factura de ejemplo con diez puntos de comprobación numerados antes de pagar",
               "Los diez puntos de la lista sobre una factura inventada. Los de relleno azul (4 a 9) son mecánicos y se pueden automatizar.")


FIGURAS = {
    "cruce_tres": cruce_tres, "albaran_vs_factura": albaran_vs_factura, "ocr_vs_ia": ocr_vs_ia, "tabla_ocr_ia": tabla_ocr_ia,
    "siete_tareas": siete_tareas, "esfuerzo_impacto": esfuerzo_impacto, "presupuesto_vs_real": presupuesto_vs_real,
    "albaran_antes_que_factura": albaran_antes_que_factura, "albaran_anotado": albaran_anotado, "decision_imputacion": decision_imputacion,
    "tabla_presupuesto": tabla_presupuesto, "flujo_presupuesto": flujo_presupuesto, "tabla_opciones": tabla_opciones, "si_entonces": si_entonces,
    "hoja_albaranes": hoja_albaranes, "kpis_plantilla": kpis_plantilla, "factura_hotspots": factura_hotspots,
}
