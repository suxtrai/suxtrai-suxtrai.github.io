"""Genera las portadas de los artículos (assets/blog/<slug>.jpg, 1200×630).

Se usan como miniatura en el blog y como imagen al compartir el enlace (og:image).
Es un paso manual: python3 scripts/imagenes.py  (necesita Playwright con Chromium).
Después, ejecutad scripts/build.py para que las páginas las enlacen.
"""
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from contenido import ARTICULOS  # noqa: E402

# Etiqueta y motivo de cada artículo
META = {
    "cruzar-albaranes-con-facturas": ("FACTURAS Y ALBARANES", "cruce"),
    "ocr-o-ia-para-leer-facturas": ("LECTURA DE DOCUMENTOS", "ojo"),
    "tareas-administrativas-automatizar-pyme": ("BACK OFFICE", "lista"),
    "control-costes-por-obra": ("CONSTRUCCIÓN Y REFORMAS", "barras"),
    "imputar-albaranes-a-obra": ("CONSTRUCCIÓN Y REFORMAS", "pin"),
    "presupuesto-reforma-desde-visita": ("CONSTRUCCIÓN Y REFORMAS", "presupuesto"),
    "software-albaranes-constructoras": ("CONSTRUCCIÓN Y REFORMAS", "matriz"),
    "plantilla-excel-cruce-albaranes-facturas": ("PLANTILLA GRATUITA", "hoja"),
    "comprobar-factura-proveedor-antes-de-pagar": ("FACTURAS DE PROVEEDOR", "check"),
}
C = "#5fb6ea"
DOC = f'<rect x="40" y="20" width="200" height="260" rx="6" fill="none" stroke="{C}" stroke-width="5"/>'
MOTIVOS = {
    "cruce": f'<g fill="none" stroke="{C}" stroke-width="5"><rect x="10" y="40" width="120" height="160" rx="6"/><rect x="150" y="80" width="120" height="160" rx="6"/>'
             f'<path d="M30 80h80M30 110h80M30 140h50M170 120h80M170 150h80M170 180h50" stroke-linecap="round"/><path d="M130 120l20 0M142 112l8 8-8 8" stroke-linecap="round"/></g>',
    "ojo": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><path d="M10 150C60 60 220 60 270 150 220 240 60 240 10 150z"/><circle cx="140" cy="150" r="44"/><circle cx="140" cy="150" r="14" fill="{C}"/></g>',
    "lista": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><path d="M20 50l14 14 26-28M20 120l14 14 26-28M20 190l14 14 26-28"/><path d="M90 52h170M90 122h170M90 192h170"/></g>',
    "barras": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><path d="M20 250h250M20 250V30"/><rect x="50" y="150" width="40" height="100"/><rect x="110" y="90" width="40" height="160"/><rect x="170" y="190" width="40" height="60"/><path d="M30 120h240" stroke-dasharray="8 8"/></g>',
    "pin": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><path d="M140 270C80 200 50 160 50 120a90 90 0 0 1 180 0c0 40-30 80-90 150z"/><circle cx="140" cy="120" r="30"/></g>',
    "presupuesto": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><rect x="30" y="20" width="220" height="260" rx="6"/><path d="M60 70h100M60 110h160M60 150h160M60 190h160M180 240h40"/></g>',
    "matriz": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><rect x="20" y="30" width="250" height="230" rx="6"/><path d="M20 88h250M20 146h250M20 204h250M100 30v230M185 30v230"/><circle cx="60" cy="117" r="8" fill="{C}"/><circle cx="142" cy="175" r="8" fill="{C}"/><circle cx="228" cy="233" r="8" fill="{C}"/></g>',
    "hoja": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round"><rect x="20" y="30" width="250" height="230" rx="6"/><path d="M20 80h250M20 130h250M20 180h250M110 30v230"/><rect x="116" y="136" width="148" height="38" fill="{C}" opacity=".35" stroke="none"/></g>',
    "check": f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><rect x="40" y="20" width="200" height="260" rx="6"/><path d="M70 90l16 16 30-34M70 160l16 16 30-34M70 230l16 16 30-34M140 92h70M140 162h70M140 232h70"/></g>',
}


def pagina(a):
    etiqueta, motivo = META[a["slug"]]
    titulo = a["h1"]
    tam = 62 if len(titulo) <= 48 else 54 if len(titulo) <= 66 else 48
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0}}
body{{width:1200px;height:630px;background:#14171a;font-family:'Inter Tight','Inter',Helvetica,Arial,sans-serif;color:#fff;position:relative;overflow:hidden}}
.glow{{position:absolute;right:-180px;top:-220px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(47,155,224,.42),rgba(16,105,159,.16) 45%,transparent 70%)}}
.motivo{{position:absolute;right:70px;top:150px;width:360px;height:360px;opacity:.95}}
.etq{{position:absolute;left:72px;top:68px;font-family:'IBM Plex Mono',monospace;font-size:22px;letter-spacing:.2em;color:#5fb6ea}}
h1{{position:absolute;left:72px;top:150px;width:700px;font-size:{tam}px;line-height:1.08;letter-spacing:-.03em;font-weight:800}}
.marca{{position:absolute;left:72px;bottom:60px;font-size:34px;font-weight:800;letter-spacing:-.03em}}
.marca i{{display:inline-block;width:14px;height:14px;background:#2f9be0;margin-right:12px;border-radius:2px}}
.web{{position:absolute;right:72px;bottom:66px;font-size:24px;color:#9aa3ad}}
</style></head><body><div class="glow"></div>
<svg class="motivo" viewBox="0 0 280 300">{MOTIVOS[motivo]}</svg>
<div class="etq">{escape(etiqueta)}</div><h1>{escape(titulo)}</h1>
<div class="marca"><i></i>SuxtrAI</div><div class="web">suxtrai.es/blog</div></body></html>"""


def main():
    from playwright.sync_api import sync_playwright
    salida = ROOT / "assets" / "blog"
    salida.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for a in ARTICULOS:
            pg.set_content(pagina(a), wait_until="load")
            destino = salida / f"{a['slug']}.jpg"
            pg.screenshot(path=str(destino), type="jpeg", quality=82)
            print(f"  ✓ {destino.name} ({destino.stat().st_size // 1024} KB)")
        b.close()


if __name__ == "__main__":
    main()
