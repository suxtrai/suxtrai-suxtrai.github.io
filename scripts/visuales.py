"""Elementos visuales de cada artículo del blog: resumen, figuras y avisos.

Las figuras se definen en figuras.py. Aquí se decide qué lleva cada artículo y dónde.
La posición se indica con el título del h2 ANTES del cual se inserta el bloque
(«^» = antes del primer h2, «$» = al final del artículo).
"""
import re
from html import escape as E

from figuras import FIGURAS


def aviso(tipo, titulo, texto):
    clase = {"idea": "idea", "cuidado": "cuidado", "nota": ""}[tipo]
    return f'<div class="callout {clase}"><p class="t">{E(titulo)}</p><p>{texto}</p></div>'


RESUMEN = {
    "cruzar-albaranes-con-facturas": [
        "El albarán prueba lo que llegó y la factura fija lo que se cobra: entre uno y otro aparecen diferencias más a menudo de lo que parece.",
        "Los fallos típicos son el precio distinto al pactado, más cantidad de la recibida, albaranes facturados dos veces y portes no acordados.",
        "Se puede empezar con una hoja de cálculo; cuando hay mucho volumen y formatos distintos, compensa automatizar la lectura y el cruce.",
    ],
    "ocr-o-ia-para-leer-facturas": [
        "El OCR lee el texto de una factura; la IA lo interpreta, que es lo que evita tener a alguien corrigiendo datos.",
        "Con pocos proveedores y PDF siempre iguales, un OCR con plantillas puede bastar. Con formatos variados o fotos, la IA ahorra mantenimiento.",
        "Lo decisivo es qué hace el sistema cuando duda: lo bueno es que lo marque para revisión, no que lo dé por bueno.",
    ],
    "tareas-administrativas-automatizar-pyme": [
        "Las mejores primeras automatizaciones son pequeñas, repetitivas y hoy dependen de que alguien teclee datos.",
        "Siete candidatas habituales: desde registrar facturas de proveedor hasta los informes semanales.",
        "Empezad por una sola, la que más horas os quita y siempre sigue los mismos pasos; medid y pasad a la siguiente.",
    ],
    "control-costes-por-obra": [
        "Comparad presupuesto y gasto real, partida por partida, mientras la obra sigue en marcha y todavía se puede corregir.",
        "El albarán da el gasto semanas antes que la factura: registradlo el día que llega y usad la factura para cerrar.",
        "Con un código de obra único, una revisión semanal y un umbral de desviación ya tenéis un método que funciona.",
    ],
    "imputar-albaranes-a-obra": [
        "Un albarán sin obra es un gasto sin dueño: se paga, pero no se sabe a quién cargarlo.",
        "Lo que mejor funciona: un código de obra único, foto del albarán el mismo día y registro al recibirlo, no a fin de mes.",
        "Lo que no se puede asignar va a una bandeja de pendientes con una persona responsable, nunca a «varios».",
    ],
    "presupuesto-reforma-desde-visita": [
        "Un presupuesto rápido empieza con buenas notas en la visita: mediciones, fotos, alcance, calidades y condicionantes.",
        "Organizadlo por capítulos y partidas con unidad, cantidad, precio e importe, e indicad también lo que no está incluido.",
        "Con un tarifario propio, la IA puede dejar un borrador en minutos; una persona lo revisa y lo envía.",
    ],
    "software-albaranes-constructoras": [
        "Antes de comparar productos, decidid qué problema os duele más: el coste de cada obra, comprobar facturas o dejar de teclear.",
        "Mirad siete cosas: captura, lectura, imputación a obra, cruce con la factura, integración, revisión de excepciones y datos.",
        "Con poco volumen una hoja de cálculo basta: no siempre hace falta IA.",
    ],
    "plantilla-excel-cruce-albaranes-facturas": [
        "Una plantilla de Excel gratuita que compara albaranes con facturas y colorea el estado de cada línea.",
        "Solo hay que registrar los documentos: las diferencias, lo pendiente de facturar y el resumen se calculan solos.",
        "Se queda corta cuando hay mucho volumen, porque alguien tiene que teclear cada documento.",
    ],
    "comprobar-factura-proveedor-antes-de-pagar": [
        "Diez comprobaciones en tres bloques: datos formales, lo recibido y lo pactado, y cálculos y controles.",
        "Las comprobaciones 4 a 9 son mecánicas (cantidades, precios, descuentos, portes, importes y duplicados) y se pueden automatizar.",
        "Para dudas sobre si una factura es válida a efectos fiscales, lo mejor es consultar con vuestra gestoría.",
    ],
}

INSERTAR = {
    "cruzar-albaranes-con-facturas": [
        ("^", "cruce_tres"),
        ("Cómo hacerlo bien a mano", "albaran_vs_factura"),
    ],
    "ocr-o-ia-para-leer-facturas": [
        ("^", "ocr_vs_ia"),
        ("Cuál necesita tu empresa", aviso("cuidado", "Una pregunta para cualquier proveedor",
                                           "¿Qué hace vuestro sistema cuando duda de un dato? Si la respuesta es «lo da por bueno», habrá errores que nadie verá hasta que sea tarde.")),
        ("Cuál necesita tu empresa", "tabla_ocr_ia"),
    ],
    "tareas-administrativas-automatizar-pyme": [
        ("^", "siete_tareas"),
        ("Por dónde empezar", "esfuerzo_impacto"),
    ],
    "control-costes-por-obra": [
        ("De dónde sale el gasto real", "presupuesto_vs_real"),
        ("Dónde se descuadra casi siempre", "albaran_antes_que_factura"),
        ("Dónde ayuda la automatización", aviso("idea", "La regla de oro",
                                                "El gasto existe el día que llega el albarán, no el día que llega la factura. Todo el método parte de ahí.")),
    ],
    "imputar-albaranes-a-obra": [
        ("Qué hacer con los albaranes sin obra", "albaran_anotado"),
        ("Cómo ayuda la IA", "decision_imputacion"),
    ],
    "presupuesto-reforma-desde-visita": [
        ("^", "flujo_presupuesto"),
        ("Dónde se pierde el tiempo", "tabla_presupuesto"),
        ("Dónde ayuda la IA", aviso("cuidado", "Propone, no decide",
                                    "Un borrador automático no se envía sin revisar: una persona del equipo confirma partidas, mediciones y condiciones antes de que llegue al cliente.")),
    ],
    "software-albaranes-constructoras": [
        ("Preguntas para hacer antes de contratar", "tabla_opciones"),
        ("Preguntas para hacer antes de contratar", "si_entonces"),
        ("Preguntas para hacer antes de contratar", aviso("idea", "Probadlo con vuestros documentos",
                                                          "Una demo con documentos de ejemplo siempre sale bien. Pedid probar con vuestros albaranes reales, incluidos los peores.")),
    ],
    "plantilla-excel-cruce-albaranes-facturas": [
        ("^", "kpis_plantilla"),
        ("Cómo usarla", "hoja_albaranes"),
    ],
    "comprobar-factura-proveedor-antes-de-pagar": [
        ("^", "factura_hotspots"),
        ("Qué se puede automatizar", aviso("idea", "Si solo vais a hacer tres",
                                           "Comparad cantidades con el albarán, el precio con lo pactado y buscad duplicados. Es donde más dinero se escapa.")),
    ],
}


def resumen_html(slug):
    puntos = RESUMEN.get(slug)
    if not puntos:
        return ""
    return '<div class="tldr"><p class="label">En resumen</p><ul>' + "".join(f"<li>{E(p)}</li>" for p in puntos) + "</ul></div>"


def cuerpo_con_figuras(slug, cuerpo):
    for ancla, bloque in INSERTAR.get(slug, []):
        html = FIGURAS[bloque]() if bloque in FIGURAS else bloque
        if ancla == "$":
            cuerpo = cuerpo + html
            continue
        if ancla == "^":
            m = re.search(r"<h2>", cuerpo)
        else:
            m = re.search(r"<h2>" + re.escape(ancla) + r"</h2>", cuerpo)
        assert m, f"{slug}: no se encuentra el apartado «{ancla}»"
        cuerpo = cuerpo[:m.start()] + html + "\n" + cuerpo[m.start():]
    return cuerpo
