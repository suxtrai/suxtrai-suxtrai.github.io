#!/usr/bin/env python3
"""Genera las páginas estáticas de suxtrai.es.

Qué hace:
  1. Crea las páginas de servicio (/servicios/...), las legales y el sitemap.xml
     a partir de los datos de este archivo.
  2. Pre-renderiza la portada: abre index.html en un navegador sin ventana,
     copia el HTML ya montado por React y lo guarda dentro de index.html para
     que Google, Bing y los navegadores sin JavaScript vean el contenido real.

Uso (desde la raíz del repo):
    pip install playwright && playwright install chromium   # solo la primera vez
    python3 scripts/build.py              # todo
    python3 scripts/build.py --sin-prerender   # solo páginas y sitemap

Vuelve a ejecutarlo cada vez que cambies textos de la portada o de este archivo.
"""
import datetime
import hashlib
import html
import json
import re
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from contenido import ARTICULOS, BACKOFFICE, SECTORES  # noqa: E402
from visuales import resumen_html, cuerpo_con_figuras  # noqa: E402
SITE = "https://suxtrai.es"
HOY = datetime.date.today().isoformat()
UMAMI_ID = "adb6b538-9ae7-48ce-9cd4-6067065a8fb9"

# ---------------------------------------------------------------------------
# Datos del titular para las páginas legales.
# Mientras no exista la SL, el titular es una persona física (un socio).
# Cuando se constituya, cambiad estos datos por los de la sociedad.
# ---------------------------------------------------------------------------
TITULAR = {
    "nombre": "Jon Medina",
    "nif": "",        # pendiente: CIF de la SL cuando se constituya
    "domicilio": "",  # pendiente: domicilio social de la SL
    "email": "contact@suxtrai.es",
}

# ---------------------------------------------------------------------------
# Servicios
# ---------------------------------------------------------------------------
SERVICIOS = [
    {
        "slug": "automatizacion-facturas-albaranes",
        "nav": "Facturas y albaranes",
        "title": "Automatización de facturas y albaranes con IA",
        "meta": "Leemos automáticamente las facturas y albaranes de proveedores, los cruzamos y os avisamos solo de lo que no cuadra. Para pymes de Bizkaia y toda España.",
        "h1": "Automatización de facturas y albaranes",
        "lead": "Leemos automáticamente las facturas y albaranes de vuestros proveedores, los cruzamos entre sí y os avisamos solo de lo que no cuadra. Dejáis de revisar papeles uno a uno.",
        "card": "Lectura automática de facturas y albaranes de proveedor y cruce entre ambos para detectar diferencias.",
        "problema": [
            "En muchas empresas alguien comprueba a mano que lo que factura cada proveedor coincide con lo que realmente se entregó. Albarán por albarán, línea por línea.",
            "Como lleva tantas horas, se acaba haciendo tarde, por encima o solo cuando algo huele raro. Y ahí se escapan precios que no son los pactados, cantidades que no cuadran, portes cobrados dos veces o albaranes que nunca se llegan a facturar.",
        ],
        "hacemos": [
            "Lectura de facturas y albaranes en PDF, foto, escáner o correo electrónico.",
            "Extracción de proveedor, fecha, número, líneas, cantidades, precios, descuentos e IVA.",
            "Cruce automático entre albarán, factura y, si lo tenéis, pedido.",
            "Avisos de diferencias: precios distintos a los pactados, cantidades, duplicados y albaranes sin facturar.",
            "Exportación a vuestro programa de contabilidad, ERP o Excel.",
            "Revisión humana solo de las excepciones, con el documento original al lado.",
        ],
        "pasos": [
            ("Recogida", "Los documentos llegan como hasta ahora: por correo, escaneados o con una foto desde el móvil."),
            ("Lectura", "La IA extrae los datos de cada documento, aunque cada proveedor use un formato distinto."),
            ("Cruce", "Se comparan albaranes, facturas y pedidos, y se marcan las diferencias."),
            ("Revisión", "Veis en un panel solo lo que no cuadra y decidís. Lo correcto pasa directamente a contabilidad."),
        ],
        "para": "Empresas que reciben muchos albaranes de proveedores: obra y reforma, rehabilitación, instaladores, transporte y logística, talleres, distribución y hostelería.",
        "faq": [
            ("¿Tenemos que cambiar de programa de contabilidad?", "No. Nos adaptamos a lo que ya usáis y le pasamos los datos revisados: por integración directa, por importación o en una hoja de cálculo."),
            ("¿Y si un documento está mal escaneado o es una foto torcida?", "Se lee igualmente en la mayoría de casos. Cuando la lectura no es fiable, el documento se marca para que lo revise una persona en lugar de darlo por bueno."),
            ("¿Funciona con facturas electrónicas?", "Sí. Si un proveedor ya os envía la factura en formato electrónico, se leen directamente sus datos y el cruce es todavía más fiable."),
            ("¿Cuánto tarda en estar funcionando?", "Normalmente en dos a cuatro semanas hay un prototipo funcionando con vuestros documentos reales. La puesta en producción depende de las integraciones que haga falta."),
        ],
        "relacionado": "presupuestos-facturas-automaticos",
    },
    {
        "slug": "presupuestos-facturas-automaticos",
        "nav": "Presupuestos y facturación",
        "title": "Presupuestos y facturas automáticos con IA",
        "meta": "Generamos presupuestos y facturas a partir de los datos de vuestro trabajo: partes, servicios realizados y tarifas, sin volver a teclearlos.",
        "h1": "Presupuestos y facturas automáticos",
        "lead": "Convertimos los datos de vuestro trabajo (partes, servicios realizados, mediciones y tarifas) en presupuestos y facturas listos para revisar y enviar. Sin volver a teclear nada.",
        "card": "Presupuestos y facturas creados a partir de los datos de vuestro trabajo, sin pasarlos a mano.",
        "problema": [
            "La información de cada trabajo está repartida: partes en papel, mensajes de WhatsApp, notas del móvil, hojas de cálculo. Pasarla después a un presupuesto o a una factura lleva horas.",
            "Además, en ese paso se pierden cosas: horas extra, desplazamientos o materiales que nunca se llegan a facturar, y presupuestos que salen tarde y se enfrían.",
        ],
        "hacemos": [
            "Presupuestos a partir de una descripción, una medición o las notas de una visita, con vuestras tarifas y plantillas.",
            "Facturas a partir de partes de trabajo o servicios realizados.",
            "Comprobación de que todo lo hecho se factura: horas, kilómetros, esperas, materiales.",
            "Documentos con vuestra imagen y vuestras condiciones.",
            "Conexión con vuestro programa de facturación para no duplicar datos.",
            "Seguimiento de presupuestos enviados y pendientes de respuesta.",
        ],
        "pasos": [
            ("Datos del trabajo", "El equipo registra el trabajo como le resulte más fácil: un formulario, una foto del parte o un mensaje."),
            ("Borrador automático", "Se genera el presupuesto o la factura con vuestras tarifas, conceptos y condiciones."),
            ("Revisión", "Alguien de la oficina lo revisa y lo ajusta si hace falta. Un minuto en lugar de media hora."),
            ("Envío y seguimiento", "Se emite desde vuestro programa y queda registrado para el seguimiento."),
        ],
        "para": "Empresas que facturan muchos trabajos o servicios distintos: reformas, instaladores, servicios técnicos, grúas y transporte, talleres y mantenimiento.",
        "faq": [
            ("¿Sustituye a nuestro programa de facturación?", "No. Lo alimenta. Las facturas se siguen emitiendo desde vuestro programa, que es el que debe cumplir los requisitos legales; nosotros preparamos los datos para que no tengáis que teclearlos."),
            ("¿Podemos revisar todo antes de enviarlo?", "Sí, siempre. El sistema prepara el borrador y una persona decide. Podéis automatizar más pasos cuando tengáis confianza en él."),
            ("¿Sirve si cada presupuesto es distinto?", "Sí. Precisamente la IA permite partir de descripciones libres o notas de una visita y convertirlas en partidas con vuestras tarifas."),
        ],
        "relacionado": "automatizacion-facturas-albaranes",
    },
    {
        "slug": "asistente-ia-documentacion",
        "nav": "Asistente sobre documentación",
        "title": "Asistente de IA sobre vuestra documentación (RAG)",
        "meta": "Un asistente que responde con vuestros contratos, manuales y procedimientos, citando siempre el documento de origen y respetando permisos.",
        "h1": "Asistente de IA sobre vuestra documentación",
        "lead": "Un buscador inteligente que responde a las preguntas del equipo usando vuestros contratos, manuales, procedimientos y normativa interna. Citando siempre de dónde sale cada respuesta.",
        "card": "Un buscador inteligente que responde con vuestros manuales, contratos y procedimientos, citando la fuente.",
        "problema": [
            "La información existe, pero está repartida entre carpetas, correos y documentos que nadie encuentra. Las mismas preguntas se repiten y siempre se las hacen a las mismas personas.",
            "Los chats de IA genéricos no conocen vuestra documentación y, cuando no saben algo, a veces se lo inventan.",
        ],
        "hacemos": [
            "Ingesta de PDF, Office, correo, wikis y bases de datos.",
            "Respuestas con cita al documento y apartado de origen.",
            "Permisos por usuario y departamento: cada persona solo recupera lo que ya puede ver.",
            "Evaluación de precisión con preguntas reales antes de abrirlo a todo el equipo.",
            "Despliegue en vuestra infraestructura si los datos no pueden salir de ella.",
        ],
        "pasos": [
            ("Selección", "Elegimos con vosotros qué documentación entra y quién puede consultarla."),
            ("Indexado", "Preparamos los documentos para que el asistente los encuentre por significado, no solo por palabras."),
            ("Evaluación", "Lo probamos con preguntas reales del equipo y medimos cuántas responde bien."),
            ("Puesta en marcha", "Lo integramos donde trabajáis (web interna, Teams, correo) y lo vamos mejorando."),
        ],
        "para": "Despachos, ingenierías, departamentos de calidad, atención al cliente y cualquier equipo que consulte mucha documentación interna.",
        "faq": [
            ("¿Se usan nuestros documentos para entrenar modelos?", "No. Trabajamos con proveedores que no usan vuestros datos para entrenar, y si hace falta se despliega todo dentro de vuestra red."),
            ("¿Qué pasa si no encuentra la respuesta?", "Lo dice. Está configurado para responder solo con lo que hay en vuestra documentación y señalar cuándo no lo encuentra."),
        ],
        "relacionado": "desarrollo-ia-a-medida",
    },
    {
        "slug": "formacion-ia-empresas",
        "nav": "Formación en IA",
        "title": "Formación en inteligencia artificial para empresas",
        "meta": "Talleres prácticos de IA con los casos reales de vuestro equipo, para usarla con criterio y saber dónde no usarla. En Bizkaia, presencial o en remoto.",
        "h1": "Formación en IA para equipos",
        "lead": "Sesiones prácticas con los casos de vuestro día a día, para que el equipo use la IA con criterio, gane tiempo de verdad y sepa dónde no usarla.",
        "card": "Talleres prácticos con vuestros propios casos para que el equipo use la IA en su día a día.",
        "problema": [
            "Casi todo el mundo ha probado ChatGPT, pero pocos equipos lo usan de forma sistemática y segura. Unos no se atreven, otros pegan datos de clientes donde no deberían.",
            "Los cursos genéricos enseñan ejemplos que no tienen nada que ver con vuestro trabajo.",
        ],
        "hacemos": [
            "Taller inicial de 4 horas, presencial o en remoto.",
            "Ejercicios con vuestros propios documentos y tareas, no con ejemplos genéricos.",
            "Guía interna de uso: qué herramientas, para qué y qué datos no se pueden meter.",
            "Seguimiento unas semanas después para resolver dudas y medir el uso.",
        ],
        "pasos": [
            ("Preparación", "Hablamos con el equipo para conocer sus tareas y elegir los casos del taller."),
            ("Taller", "Práctica guiada con esos casos y con las herramientas que vais a usar."),
            ("Guía", "Os dejamos por escrito las reglas de uso y los ejemplos que mejor han funcionado."),
            ("Seguimiento", "Revisamos al cabo de unas semanas qué se está usando y qué ajustar."),
        ],
        "para": "Equipos de administración, comerciales, dirección y oficina técnica de cualquier sector.",
        "faq": [
            ("¿Hace falta saber programar?", "No. La formación está pensada para personas que no son técnicas."),
            ("¿Se puede bonificar?", "Depende de cómo se organice. Si os interesa, lo vemos con vuestra gestoría antes de cerrar fechas."),
        ],
        "relacionado": "asesoramiento-ia",
    },
    {
        "slug": "asesoramiento-ia",
        "nav": "Asesoramiento",
        "title": "Asesoramiento en inteligencia artificial para empresas",
        "meta": "Qué automatizar primero, cuánto cuesta y qué riesgos tiene. Un plan priorizado antes de escribir una línea de código. Diagnóstico inicial sin coste.",
        "h1": "Asesoramiento en IA",
        "lead": "Qué automatizar primero, qué coste tiene, qué se puede hacer con los datos que ya tenéis y qué riesgos implica. Un plan priorizado antes de escribir una línea de código.",
        "card": "Un plan priorizado de qué automatizar, con coste y riesgos, antes de invertir.",
        "problema": [
            "Todo el mundo habla de IA, pero es difícil saber qué tiene sentido para vuestra empresa, cuánto cuesta y por dónde empezar.",
            "Empezar por el proyecto equivocado sale caro y quema la confianza del equipo.",
        ],
        "hacemos": [
            "Auditoría de procesos y datos.",
            "Lista de casos ordenada por impacto y esfuerzo.",
            "Estimación de coste y ahorro por caso.",
            "Revisión de riesgos, protección de datos y cumplimiento.",
            "Acompañamiento en la elección de proveedores y herramientas, aunque no trabajéis con nosotros.",
        ],
        "pasos": [
            ("Diagnóstico", "Una sesión con vosotros para entender procesos y datos. Sin coste."),
            ("Análisis", "Revisamos dónde se va el tiempo y qué datos hay disponibles."),
            ("Plan", "Os entregamos los casos priorizados con coste, plazo y riesgos."),
            ("Decisión", "Decidís qué hacer, con nosotros o con quien queráis."),
        ],
        "para": "Direcciones y gerencias de pymes que quieren aprovechar la IA sin tirar dinero.",
        "faq": [
            ("¿Y si no hay nada que compense automatizar?", "Os lo decimos. Preferimos eso a vender un proyecto que no se va a amortizar."),
        ],
        "relacionado": "desarrollo-ia-a-medida",
    },
    {
        "slug": "desarrollo-ia-a-medida",
        "nav": "Desarrollo a medida",
        "title": "Desarrollo de soluciones de IA a medida",
        "meta": "Del prototipo al sistema en producción: interfaz, integraciones, despliegue, monitorización y mantenimiento. Cloud u on-premise.",
        "h1": "Desarrollo de IA a medida, hasta producción",
        "lead": "Del prototipo al sistema funcionando cada día: interfaz, integraciones con vuestras herramientas, despliegue, monitorización y mantenimiento posterior.",
        "card": "Del prototipo al sistema en producción, integrado con vuestras herramientas.",
        "problema": [
            "Muchas pruebas con IA se quedan en una demo que nadie usa porque no está conectada con el ERP, el correo o las herramientas reales del equipo.",
        ],
        "hacemos": [
            "Interfaz web o integración en las herramientas que ya usáis.",
            "Conexión con ERP, CRM, correo y hojas de cálculo.",
            "Despliegue en la nube o en vuestros servidores.",
            "Monitorización, alertas y métricas de uso.",
            "Mantenimiento y evolución, o documentación y formación para que lo lleve vuestro equipo.",
        ],
        "pasos": [
            ("Prototipo", "Un caso funcionando con vuestros datos reales, medido contra el proceso actual."),
            ("Integración", "Lo conectamos con vuestros sistemas y definimos permisos."),
            ("Despliegue", "Puesta en producción con monitorización y formación a quien lo va a usar."),
            ("Mejora", "Revisamos métricas, ajustamos y pasamos al siguiente caso."),
        ],
        "para": "Empresas con un proceso claro que quieren llevarlo a producción con garantías.",
        "faq": [
            ("¿Con qué tecnologías trabajáis?", "Elegimos según el caso: modelos comerciales o abiertos, bases de datos vectoriales, Python, APIs e integraciones, en la nube o en vuestra infraestructura."),
            ("¿Quién lo mantiene después?", "Podemos quedarnos con el mantenimiento o dejarlo documentado y formar a vuestro equipo técnico."),
        ],
        "relacionado": "automatizacion-facturas-albaranes",
    },
]
POR_SLUG = {s["slug"]: s for s in SERVICIOS}

E = html.escape

LOGO = ('<a class="logo" href="/" aria-label="SuxtrAI, inicio">'
        '<img src="/assets/isotipo.svg" alt="" width="30" height="32">'
        '<span>suxtr<span>AI</span></span></a>')


def pagina(path, title, meta, cuerpo, schema=None, indexar=True, og_type="website", og_image=None):
    canonical = SITE + path
    if len(title) > 60 and title.endswith(" | SuxtrAI"):
        title = title[: -len(" | SuxtrAI")]
    ld = ""
    for s in (schema or []):
        ld += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    footer_svc = "".join(f'<a href="/servicios/{s["slug"]}/">{E(s["nav"])}</a>' for s in SERVICIOS)
    footer_sec = "".join(f'<a href="/sectores/{s["slug"]}/">{E(s["nav"])}</a>' for s in SECTORES)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(meta)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{'index, follow' if indexar else 'noindex, follow'}">
<meta name="theme-color" content="#14171a">
<link rel="icon" href="/favicon.ico?v=2" sizes="any">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=2">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=2">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="SuxtrAI">
<meta property="og:locale" content="es_ES">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(meta)}">
<meta property="og:image" content="{SITE}{og_image or '/assets/og-suxtrai.jpg'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=3">
{ld}<script defer src="https://cloud.umami.is/script.js" data-website-id="{UMAMI_ID}" data-domains="suxtrai.es,www.suxtrai.es"></script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="site-header"><div class="bar">
{LOGO}
<nav class="site-nav" aria-label="Principal">
<a href="/automatizacion-back-office/" class="hide-sm">Back office con IA</a>
<a href="/servicios/" class="hide-sm">Servicios</a>
<a href="/sectores/" class="hide-sm">Sectores</a>
<a href="/blog/" class="hide-sm">Blog</a>
<a href="/#contacto" class="cta" data-umami-event="cta-hablemos">Hablemos</a>
</nav>
</div></header>
<main id="contenido">
{cuerpo}
</main>
<footer class="site-footer">
<div class="cols">
<div>{LOGO}<p style="margin:14px 0 0;max-width:34ch">Automatización del back office con IA: facturas, albaranes y presupuestos sin teclear. Desde Bilbao para toda España.</p></div>
<div><p class="fh">Servicios</p>{footer_svc}</div>
<div><p class="fh">Back office</p><a href="/automatizacion-back-office/">Back office con IA</a>{footer_sec}<a href="/blog/">Blog</a></div>
<div><p class="fh">Empresa</p><a href="/#metodo">Cómo trabajamos</a><a href="/#equipo">Equipo</a><a href="/#faq">Preguntas frecuentes</a></div>
<div><p class="fh">Contacto</p><a href="mailto:contact@suxtrai.es">contact@suxtrai.es</a><a href="/#contacto">Formulario</a><a href="https://www.linkedin.com/company/suxtrai/" rel="noopener" target="_blank">LinkedIn</a><span>Bizkaia · España</span></div>
</div>
<div class="legal-bar"><span>© {datetime.date.today().year} SuxtrAI</span><span><a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Privacidad</a></span></div>
</footer>
</body>
</html>
"""


def cta(titulo="¿Lo vemos con vuestro caso?", texto="Treinta minutos bastan para saber si hay algo que merezca la pena automatizar. Si no lo hay, os lo diremos. La primera sesión no tiene coste."):
    return f"""<section class="cta-band"><div class="inner">
<h2>{E(titulo)}</h2>
<p>{E(texto)}</p>
<p><a class="btn btn-light" href="/#contacto" data-umami-event="cta-servicio">Contadnos vuestro caso</a></p>
</div></section>"""


def breadcrumbs(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
            for i, (n, u) in enumerate(items)
        ],
    }


def pagina_servicio(s):
    path = f"/servicios/{s['slug']}/"
    rel = POR_SLUG[s["relacionado"]]
    otros = [x for x in SERVICIOS if x["slug"] not in (s["slug"], rel["slug"])][:2]
    problema = "".join(f"<p>{E(p)}</p>" for p in s["problema"])
    hacemos = "".join(f"<li>{E(x)}</li>" for x in s["hacemos"])
    pasos = "".join(
        f'<div class="card"><span class="num">{i + 1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>'
        for i, (t, d) in enumerate(s["pasos"]))
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in s["faq"])
    relacionados = "".join(
        f'<a class="card" href="/servicios/{x["slug"]}/"><h3>{E(x["h1"])}</h3><p>{E(x["card"])}</p><span class="more">Ver servicio →</span></a>'
        for x in [rel] + otros)
    cuerpo = f"""<div class="page-hero"><div class="inner">
<div class="crumbs"><a href="/">Inicio</a> / <a href="/servicios/">Servicios</a> / {E(s['nav'])}</div>
<h1>{E(s['h1'])}</h1>
<p class="lead">{E(s['lead'])}</p>
<div class="actions"><a class="btn btn-light" href="/#contacto" data-umami-event="cta-servicio">Diagnóstico gratuito</a><a class="btn btn-ghost" href="#como">Cómo funciona</a></div>
</div></div>
<section><div class="inner">
<p class="eyebrow">El problema</p>
<h2>Lo que pasa hoy</h2>
{problema}
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué hacemos</p>
<h2>Qué incluye</h2>
<ul class="checks">{hacemos}</ul>
</div></section>
<section id="como"><div class="inner">
<p class="eyebrow">Cómo funciona</p>
<h2>En cuatro pasos</h2>
<div class="grid">{pasos}</div>
</div></section>
<section><div class="inner">
<p class="eyebrow">Para quién</p>
<h2>Para qué empresas es</h2>
<p>{E(s['para'])}</p>
<p>Trabajamos desde Bizkaia con empresas de toda España, en remoto y presencial cuando el proyecto lo pide.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Preguntas frecuentes</p>
<h2>Dudas habituales</h2>
{faq}
</div></section>
{cta()}
{bloque_guias(guias_de("servicios", s["slug"]))}
<section><div class="inner">
<p class="eyebrow">También os puede interesar</p>
<div class="grid">{relacionados}</div>
</div></section>"""
    schema = [
        {
            "@context": "https://schema.org", "@type": "Service",
            "name": s["title"], "description": s["meta"], "url": SITE + path,
            "serviceType": s["h1"],
            "provider": {"@type": "Organization", "name": "SuxtrAI", "url": SITE + "/"},
            "areaServed": [{"@type": "AdministrativeArea", "name": "Bizkaia"}, {"@type": "Country", "name": "España"}],
        },
        breadcrumbs([("Inicio", "/"), ("Servicios", "/servicios/"), (s["nav"], path)]),
        {
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]],
        },
    ]
    return path, pagina(path, f"{s['title']} | SuxtrAI", s["meta"], cuerpo, schema)


def pagina_servicios():
    path = "/servicios/"
    cards = "".join(
        f'<a class="card" href="/servicios/{s["slug"]}/"><span class="num">/{i + 1:02d}</span><h3>{E(s["h1"])}</h3><p>{E(s["card"])}</p><span class="more">Ver servicio →</span></a>'
        for i, s in enumerate(SERVICIOS))
    cuerpo = f"""<div class="page-hero"><div class="inner">
<div class="crumbs"><a href="/">Inicio</a> / Servicios</div>
<h1>Servicios de inteligencia artificial para empresas</h1>
<p class="lead">Nos especializamos en quitar papeleo administrativo: facturas, albaranes y presupuestos. Y además montamos asistentes sobre vuestra documentación, formamos equipos y desarrollamos soluciones a medida.</p>
</div></div>
<section><div class="inner">
<p class="eyebrow">Qué hacemos</p>
<h2>Seis formas de ayudaros</h2>
<p>Se combinan según el caso. Si no tenéis claro cuál encaja, empezad por el diagnóstico gratuito.</p>
<div class="grid">{cards}</div>
</div></section>
{cta()}"""
    schema = [breadcrumbs([("Inicio", "/"), ("Servicios", path)])]
    return path, pagina(path, "Servicios de IA para el back office de pymes | SuxtrAI",
                        "Automatización de facturas, albaranes y presupuestos, asistentes de IA sobre vuestra documentación, formación, asesoramiento y desarrollo a medida.",
                        cuerpo, schema)


def fila(k, v):
    # las filas sin dato no se muestran
    return f"<tr><th>{E(k)}</th><td>{v}</td></tr>" if v else ""


def pagina_aviso_legal():
    path = "/aviso-legal/"
    t = TITULAR
    cuerpo = f"""<div class="page-hero"><div class="inner"><div class="crumbs"><a href="/">Inicio</a> / Aviso legal</div><h1>Aviso legal</h1></div></div>
<section class="legal"><div class="inner">
<p class="updated">Última actualización: {HOY}</p>
<h2>1. Datos identificativos</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<table>
{fila("Titular", E(t["nombre"]))}
{fila("NIF", E(t["nif"]))}
{fila("Domicilio", E(t["domicilio"]))}
{fila("Correo electrónico", f'<a href="mailto:{t["email"]}">{t["email"]}</a>')}
{fila("Sitio web", "suxtrai.es")}
</table>
<p>SuxtrAI es el nombre comercial del proyecto. Mientras se completa su constitución como sociedad, el titular del sitio es la persona indicada arriba.</p>
<h2>2. Objeto</h2>
<p>Este sitio web informa sobre los servicios de inteligencia artificial que ofrece SuxtrAI y permite contactar con nosotros. Acceder y navegar por él implica aceptar las condiciones de este aviso legal.</p>
<h2>3. Condiciones de uso</h2>
<p>Quien utiliza el sitio se compromete a hacerlo de forma lícita y a no emplearlo para actividades que dañen los derechos de terceros o el funcionamiento del sitio.</p>
<h2>4. Propiedad intelectual e industrial</h2>
<p>Los textos, diseños, logotipos, imágenes y código de este sitio pertenecen a su titular o se usan con autorización. No se permite su reproducción, distribución o transformación sin permiso expreso, salvo para uso personal y privado.</p>
<h2>5. Responsabilidad</h2>
<p>Procuramos que la información sea correcta y esté actualizada, pero no garantizamos la ausencia de errores ni la disponibilidad continua del sitio. La información publicada es orientativa y no constituye una oferta vinculante; cada proyecto se concreta en una propuesta específica.</p>
<h2>6. Enlaces</h2>
<p>Los enlaces a sitios de terceros (por ejemplo, redes sociales) se ofrecen como referencia. No somos responsables de sus contenidos ni de sus políticas.</p>
<h2>7. Protección de datos</h2>
<p>El tratamiento de los datos personales que nos facilites se explica en la <a href="/privacidad/">política de privacidad</a>.</p>
<h2>8. Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales que correspondan conforme a la ley; cuando la otra parte sea consumidora, los de su domicilio.</p>
</div></section>"""
    return path, pagina(path, "Aviso legal | SuxtrAI", "Aviso legal e información del titular del sitio web suxtrai.es.", cuerpo)


def pagina_privacidad():
    path = "/privacidad/"
    t = TITULAR
    cuerpo = f"""<div class="page-hero"><div class="inner"><div class="crumbs"><a href="/">Inicio</a> / Privacidad</div><h1>Política de privacidad</h1></div></div>
<section class="legal"><div class="inner">
<p class="updated">Última actualización: {HOY}</p>
<p>Esta política explica qué datos personales tratamos cuando usas suxtrai.es o nos escribes, para qué los usamos y qué derechos tienes, conforme al Reglamento (UE) 2016/679 (RGPD) y a la Ley Orgánica 3/2018 (LOPDGDD).</p>
<h2>1. Responsable del tratamiento</h2>
<table>
{fila("Responsable", E(t["nombre"]) + " (SuxtrAI)")}
{fila("NIF", E(t["nif"]))}
{fila("Domicilio", E(t["domicilio"]))}
{fila("Contacto", f'<a href="mailto:{t["email"]}">{t["email"]}</a>')}
</table>
<h2>2. Qué datos tratamos y para qué</h2>
<table>
<tr><th>Formulario de contacto</th><td>Nombre y empresa, correo electrónico, el mensaje que nos escribas y los intereses que marques. Los usamos para responder a tu consulta y, si lo pides, preparar una propuesta.</td></tr>
<tr><th>Correo electrónico</th><td>Los datos que incluyas al escribirnos a {t["email"]}, con la misma finalidad.</td></tr>
<tr><th>Estadísticas de visitas</th><td>Usamos Umami, una herramienta de analítica que no utiliza cookies ni guarda tu dirección IP. Solo obtenemos datos agregados y anónimos (páginas vistas, país, tipo de dispositivo, clics en botones) para mejorar la web.</td></tr>
</table>
<p>No tomamos decisiones automatizadas ni elaboramos perfiles con tus datos.</p>
<h2>3. Base legal</h2>
<p>Tratamos los datos del formulario y del correo con tu consentimiento, que das al enviarlos (art. 6.1.a RGPD), y para aplicar a petición tuya medidas previas a un posible contrato (art. 6.1.b RGPD). Puedes retirar tu consentimiento cuando quieras escribiéndonos.</p>
<h2>4. Cuánto tiempo los conservamos</h2>
<p>El tiempo necesario para atender tu consulta. Si no llegamos a colaborar, los eliminamos como máximo doce meses después del último contacto. Si eres cliente, los conservamos mientras dure la relación y, después, durante los plazos que exige la ley.</p>
<h2>5. Destinatarios</h2>
<p>No cedemos tus datos a terceros salvo obligación legal. Para que la web funcione usamos proveedores que tratan datos por nuestra cuenta, con contratos que les obligan a protegerlos:</p>
<ul>
<li><strong>Web3Forms</strong>: envía a nuestro correo los mensajes del formulario.</li>
<li><strong>Proveedor de correo electrónico</strong> de suxtrai.es: recibe y guarda los mensajes.</li>
<li><strong>GitHub Pages</strong>: aloja la web.</li>
<li><strong>Umami</strong>: estadísticas anónimas de visitas.</li>
<li><strong>Google Fonts</strong>: sirve las tipografías de la web; al cargarlas, tu navegador se conecta con servidores de Google, que reciben tu dirección IP.</li>
</ul>
<p>Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia se ampara en decisiones de adecuación de la Comisión Europea (como el Marco de Privacidad de Datos UE-EE. UU.) o en cláusulas contractuales tipo.</p>
<h2>6. Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación del tratamiento y portabilidad escribiendo a <a href="mailto:{t["email"]}">{t["email"]}</a>. Si consideras que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener" target="_blank">www.aepd.es</a>).</p>
<h2>7. Cookies</h2>
<p>Esta web no usa cookies propias ni de terceros con fines de análisis o publicidad, por eso no te mostramos un aviso de cookies. Si en el futuro añadimos alguna que lo requiera, te pediremos el consentimiento antes.</p>
<h2>8. Cambios</h2>
<p>Podemos actualizar esta política. La fecha de la última actualización aparece al principio.</p>
</div></section>"""
    return path, pagina(path, "Política de privacidad | SuxtrAI", "Cómo trata SuxtrAI los datos personales de quienes visitan suxtrai.es o nos escriben.", cuerpo)


ORG = {"@type": "Organization", "name": "SuxtrAI", "url": SITE + "/", "@id": SITE + "/#org"}
# Autor de los artículos del blog (aparece en la firma y en los datos estructurados).
AUTOR = {"@type": "Person", "name": "Jon Medina", "url": SITE + "/#equipo", "worksFor": {"@id": SITE + "/#org"}}
POR_SLUG_SECTOR = {s["slug"]: s for s in SECTORES}


def portada(slug):
    """Ruta de la portada del artículo (assets/blog/<slug>.jpg); cadena vacía si todavía no se ha generado."""
    return f"/assets/blog/{slug}.jpg" if (ROOT / "assets" / "blog" / f"{slug}.jpg").exists() else ""


def miniatura(a):
    p = portada(a["slug"])
    return f'<img class="thumb" src="{p}" alt="" width="1200" height="630" loading="lazy" decoding="async">' if p else ""


def tarjeta_articulo(a, num=""):
    n = f'<span class="num">{num}</span>' if num else ""
    return (f'<a class="card" href="/blog/{a["slug"]}/">{miniatura(a)}{n}<h3>{E(a["h1"])}</h3>'
            f'<p>{E(a["resumen"])}</p><span class="more">Leer →</span></a>')


def guias_de(tipo, slug):
    """Artículos del blog relacionados con un servicio o un sector (según el campo 'relacion')."""
    return [a for a in sorted(ARTICULOS, key=lambda x: x["fecha"], reverse=True)
            if slug in a.get("relacion", {}).get(tipo, [])]


def bloque_guias(arts, titulo="Guías relacionadas"):
    if not arts:
        return ""
    cards = "".join(
        tarjeta_articulo(a) for a in arts)
    return f'''<section><div class="inner">
<p class="eyebrow">Guías</p>
<h2>{E(titulo)}</h2>
<div class="grid">{cards}</div>
</div></section>'''


def hero(crumbs, h1, lead, acciones=True):
    migas = " / ".join(f'<a href="{u}">{E(n)}</a>' if u else E(n) for n, u in crumbs)
    botones = ('<div class="actions"><a class="btn btn-light" href="/#contacto" data-umami-event="cta-servicio">Diagnóstico gratuito</a></div>' if acciones else "")
    return f"""<div class="page-hero"><div class="inner">
<div class="crumbs">{migas}</div>
<h1>{E(h1)}</h1>
<p class="lead">{E(lead)}</p>
{botones}
</div></div>"""


def bloque_faq(faq):
    items = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faq)
    return f"""<section><div class="inner">
<p class="eyebrow">Preguntas frecuentes</p>
<h2>Dudas habituales</h2>
{items}
</div></section>"""


def schema_faq(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def pagina_backoffice():
    b = BACKOFFICE
    cuerpo = hero([("Inicio", "/"), ("Back office con IA", None)], b["h1"], b["lead"]) + b["cuerpo"] + bloque_faq(b["faq"]) + cta()
    schema = [
        {"@context": "https://schema.org", "@type": "Service", "name": b["title"], "description": b["meta"],
         "url": SITE + b["path"], "serviceType": "Automatización del back office", "provider": ORG,
         "areaServed": [{"@type": "AdministrativeArea", "name": "Bizkaia"}, {"@type": "Country", "name": "España"}]},
        breadcrumbs([("Inicio", "/"), ("Back office con IA", b["path"])]),
        schema_faq(b["faq"]),
    ]
    return b["path"], pagina(b["path"], f'{b["title"]} | SuxtrAI', b["meta"], cuerpo, schema)


def pagina_sectores():
    path = "/sectores/"
    cards = "".join(
        f'<a class="card" href="/sectores/{s["slug"]}/"><h3>{E(s["nav"])}</h3><p>{E(s["card"])}</p><span class="more">Ver sector →</span></a>'
        for s in SECTORES)
    cuerpo = hero([("Inicio", "/"), ("Sectores", None)], "Automatización del back office por sectores",
                  "El papeleo cambia según el sector, pero el problema es el mismo: horas pasando datos a mano. Así lo aplicamos en cada uno.") + f"""
<section><div class="inner">
<p class="eyebrow">Sectores</p>
<h2>Elige el tuyo</h2>
<div class="grid">{cards}</div>
<p style="margin-top:24px">¿No está tu sector? El método es el mismo para cualquier empresa con mucho papeleo. <a href="/automatizacion-back-office/">Ver cómo automatizamos el back office</a>.</p>
</div></section>""" + cta()
    return path, pagina(path, "IA para el back office por sectores | SuxtrAI",
                        "Cómo automatizamos facturas, albaranes, pedidos y presupuestos en construcción y reformas, transporte y grúas, talleres y distribución.",
                        cuerpo, [breadcrumbs([("Inicio", "/"), ("Sectores", path)])])


def pagina_sector(s):
    path = f"/sectores/{s['slug']}/"
    otros = "".join(
        f'<a class="card" href="/sectores/{x["slug"]}/"><h3>{E(x["nav"])}</h3><p>{E(x["card"])}</p><span class="more">Ver sector →</span></a>'
        for x in SECTORES if x["slug"] != s["slug"])
    cuerpo = (hero([("Inicio", "/"), ("Sectores", "/sectores/"), (s["nav"], None)], s["h1"], s["lead"])
              + s["cuerpo"] + bloque_guias(guias_de("sectores", s["slug"]), "Guías para " + s["nav"].lower())
              + bloque_faq(s["faq"]) + cta()
              + f'<section><div class="inner"><p class="eyebrow">Otros sectores</p><div class="grid">{otros}</div></div></section>')
    schema = [
        {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "description": s["meta"], "url": SITE + path,
         "serviceType": "Automatización del back office", "provider": ORG, "audience": {"@type": "BusinessAudience", "name": s["nav"]},
         "areaServed": [{"@type": "AdministrativeArea", "name": "Bizkaia"}, {"@type": "Country", "name": "España"}]},
        breadcrumbs([("Inicio", "/"), ("Sectores", "/sectores/"), (s["nav"], path)]),
        schema_faq(s["faq"]),
    ]
    return path, pagina(path, f"{s['title']} | SuxtrAI", s["meta"], cuerpo, schema)


def fecha_es(iso):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    a, m, d = iso.split("-")
    return f"{int(d)} de {meses[int(m) - 1]} de {a}"


def pagina_blog():
    path = "/blog/"
    items = "".join(
        tarjeta_articulo(a, fecha_es(a["fecha"])) for a in sorted(ARTICULOS, key=lambda x: x["fecha"], reverse=True))
    cuerpo = hero([("Inicio", "/"), ("Blog", None)], "Blog: automatización del back office",
                  "Guías prácticas para quitar papeleo en la oficina: facturas, albaranes, presupuestos y cómo aplicar la IA sin complicaciones.", acciones=False) + f"""
<section><div class="inner"><div class="grid">{items}</div></div></section>""" + cta()
    return path, pagina(path, "Blog de automatización del back office con IA | SuxtrAI",
                        "Guías prácticas sobre facturas, albaranes, presupuestos y automatización administrativa con IA para pymes.",
                        cuerpo, [breadcrumbs([("Inicio", "/"), ("Blog", path)])])


def pagina_articulo(a):
    path = f"/blog/{a['slug']}/"
    # "Sigue leyendo": los tres artículos más afines (comparten servicio o sector); a igualdad, los más recientes
    def afinidad(x):
        rx, ra = x.get("relacion", {}), a.get("relacion", {})
        return -sum(len(set(rx.get(k, [])) & set(ra.get(k, []))) for k in ("servicios", "sectores"))
    resto = sorted([x for x in ARTICULOS if x["slug"] != a["slug"]], key=lambda x: x["fecha"], reverse=True)
    otros = "".join(
        tarjeta_articulo(x) for x in sorted(resto, key=afinidad)[:3])
    modificado = a.get("modificado", a["fecha"])
    actualizado = f" · Actualizado el {fecha_es(modificado)}" if modificado != a["fecha"] else ""
    r = a.get("relacion", {})
    rel_cards = "".join(
        f'<a class="card" href="/servicios/{sl}/"><span class="num">Servicio</span><h3>{E(POR_SLUG[sl]["h1"])}</h3><p>{E(POR_SLUG[sl]["card"])}</p><span class="more">Ver servicio →</span></a>'
        for sl in r.get("servicios", [])
    ) + "".join(
        f'<a class="card" href="/sectores/{sl}/"><span class="num">Sector</span><h3>{E(POR_SLUG_SECTOR[sl]["nav"])}</h3><p>{E(POR_SLUG_SECTOR[sl]["card"])}</p><span class="more">Ver sector →</span></a>'
        for sl in r.get("sectores", []))
    bloque_rel = (f'<section><div class="inner"><p class="eyebrow">Para aplicarlo</p><div class="grid">{rel_cards}</div></div></section>'
                  if rel_cards else "")
    cuerpo = f"""<div class="page-hero"><div class="inner">
<div class="crumbs"><a href="/">Inicio</a> / <a href="/blog/">Blog</a></div>
<h1>{E(a['h1'])}</h1>
<p class="lead">{E(a['resumen'])}</p>
<p class="updated" style="color:#9aa3ad;margin-top:18px">Por {AUTOR["name"]} · Publicado el {fecha_es(a['fecha'])}{actualizado}</p>
</div></div>
<section class="article"><div class="inner">
{resumen_html(a['slug'])}
{cuerpo_con_figuras(a['slug'], a['cuerpo'])}
</div></section>
{bloque_rel}
{cta("¿Queréis automatizarlo?", "Os enseñamos cómo funcionaría con vuestros propios documentos. La primera sesión, de 30 minutos, no tiene coste.")}
<section><div class="inner"><p class="eyebrow">Sigue leyendo</p><div class="grid">{otros}</div></div></section>"""
    schema = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["h1"], "description": a["meta"],
         "datePublished": a["fecha"], "dateModified": modificado, "inLanguage": "es",
         "mainEntityOfPage": SITE + path, "image": SITE + (portada(a["slug"]) or "/assets/og-suxtrai.jpg"),
         "author": AUTOR, "publisher": {**ORG, "logo": {"@type": "ImageObject", "url": SITE + "/assets/suxtrai-logo.jpg"}}},
        breadcrumbs([("Inicio", "/"), ("Blog", "/blog/"), (a["h1"], path)]),
    ]
    return path, pagina(path, f"{a['title']} | SuxtrAI", a["meta"], cuerpo, schema, og_type="article", og_image=portada(a["slug"]) or None)


def llms_txt():
    lineas = [
        "# SuxtrAI",
        "",
        "> Automatización del back office de pymes con inteligencia artificial: lectura de facturas y albaranes de proveedor, cruce con pedidos, presupuestos y facturación sin teclear, asistentes sobre documentación interna y formación. Con sede en Bizkaia (Bilbao) y clientes en toda España. Contacto: contact@suxtrai.es. Diagnóstico inicial de 30 minutos sin coste.",
        "",
        "## Páginas principales",
        f"- [Back office con IA]({SITE}{BACKOFFICE['path']}): qué tareas administrativas automatizamos y cómo",
        f"- [Servicios]({SITE}/servicios/): todos los servicios",
    ]
    lineas += [f"- [{s['h1']}]({SITE}/servicios/{s['slug']}/): {s['card']}" for s in SERVICIOS]
    lineas += ["", "## Sectores"] + [f"- [{s['nav']}]({SITE}/sectores/{s['slug']}/): {s['card']}" for s in SECTORES]
    lineas += ["", "## Guías"] + [f"- [{a['h1']}]({SITE}/blog/{a['slug']}/): {a['resumen']}" for a in ARTICULOS]
    lineas += ["", "## Opcional", f"- [Aviso legal]({SITE}/aviso-legal/)", f"- [Privacidad]({SITE}/privacidad/)", ""]
    (ROOT / "llms.txt").write_text("\n".join(lineas), encoding="utf-8")
    print("  ✓ llms.txt")


LASTMOD = Path(__file__).resolve().parent / "lastmod.json"
HUELLAS = {}


def huella(texto):
    """Resumen del contenido sin los datos que cambian solos (fecha de actualización, año del pie)."""
    texto = re.sub(r"Última actualización: \d{4}-\d{2}-\d{2}", "", texto)
    texto = re.sub(r"© \d{4}", "", texto)
    texto = re.sub(r"site\.css\?v=\d+", "site.css?v=2", texto)  # subir la versión del CSS no cuenta como cambio de contenido
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:16]


def escribir(path, contenido):
    HUELLAS[path] = huella(contenido)
    destino = ROOT / path.strip("/") / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(contenido, encoding="utf-8")
    print("  ✓", path)


def sitemap(paths):
    prio = {"/": "1.0", "/automatizacion-back-office/": "0.9", "/servicios/": "0.9", "/sectores/": "0.8", "/blog/": "0.7"}
    # lastmod: solo se actualiza la fecha de las páginas cuyo contenido ha cambiado desde la última vez.
    # La portada se compara sin el bloque pre-renderizado (que se regenera en cada ejecución).
    previo = json.loads(LASTMOD.read_text(encoding="utf-8")) if LASTMOD.exists() else {}
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    home = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN) + r"\n?", "", home, flags=re.S)
    HUELLAS["/"] = huella(home)
    estado = {}
    urls = []
    for p in paths:
        ant = previo.get(p)
        lm = ant["lastmod"] if ant and ant["huella"] == HUELLAS[p] else HOY
        estado[p] = {"huella": HUELLAS[p], "lastmod": lm}
        pr = prio.get(p, "0.3" if p in ("/aviso-legal/", "/privacidad/") else "0.8")
        urls.append(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{lm}</lastmod>\n    <priority>{pr}</priority>\n  </url>")
    LASTMOD.write_text(json.dumps(estado, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    print("  ✓ sitemap.xml")


# ---------------------------------------------------------------------------
# Pre-renderizado de la portada
# ---------------------------------------------------------------------------
INICIO = "<!-- PRERENDER:INICIO (generado por scripts/build.py, no editar a mano) -->"
FIN = "<!-- PRERENDER:FIN -->"
# ids que se conservan para que funcionen los enlaces internos (#contacto...) sin JavaScript
ANCLAS = {"top", "servicios", "calculadora", "metodo", "porque", "equipo", "faq", "contacto"}

JS_EXTRAER = """() => {
  const root = document.getElementById('dc-root');
  const c = root.cloneNode(true);
  c.querySelectorAll('video, canvas, iframe, script').forEach(e => e.remove());
  const escrito = c.querySelector('#suxtr-hero-type');
  if (escrito) escrito.textContent = 'Inteligencia artificial a\\u00a0medida.';
  const cursor = c.querySelector('#suxtr-hero-cursor');
  if (cursor) cursor.remove();
  c.querySelectorAll('[id]').forEach(e => { if (!ANCLAS.includes(e.id)) e.removeAttribute('id'); });
  c.querySelectorAll('[aria-live]').forEach(e => e.removeAttribute('aria-live'));
  const estilos = [...document.head.querySelectorAll('style')]
    .map(s => s.textContent)
    .filter(t => t.includes('scroll-behavior'))
    .join('\\n');
  return { html: c.innerHTML, css: estilos };
}"""


TPL_ABRE = '<script type="text/x-dc-template" id="suxtr-tpl">'
TPL_CARGA = ("<script>(function(){var t=document.getElementById('suxtr-tpl');if(!t)return;"
             "var d=document.createElement('div');d.innerHTML=t.textContent;t.replaceWith(d.firstElementChild)})();</script>")


def envolver_plantilla(src):
    """Mete la plantilla <x-dc> dentro de un <script> para que los buscadores no la lean
    como texto duplicado (ya tienen la copia pre-renderizada). Un script la restaura
    antes de que arranque support.js (que va con defer)."""
    if TPL_ABRE in src:
        return src
    i = src.index("<x-dc>")
    j = src.index("</x-dc>") + len("</x-dc>")
    plantilla = src[i:j]
    assert "</script" not in plantilla.lower() and "<!--" not in plantilla
    return src[:i] + TPL_ABRE + plantilla + "</script>\n" + TPL_CARGA + src[j:]


def servidor():
    class Silencioso(SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = partial(Silencioso, directory=str(ROOT))
    srv = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def prerender():
    from playwright.sync_api import sync_playwright
    idx = ROOT / "index.html"
    src = idx.read_text(encoding="utf-8")
    # quitar el pre-renderizado anterior antes de volver a generarlo
    src = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN) + r"\n?", "", src, flags=re.S)
    src = envolver_plantilla(src)
    idx.write_text(src, encoding="utf-8")

    srv = servidor()
    url = f"http://127.0.0.1:{srv.server_address[1]}/index.html"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.route("**/cloud.umami.is/**", lambda r: r.abort())
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_selector("#dc-root #contacto", timeout=20000)
        # recorrer la página para que se muestren las secciones que aparecen al hacer scroll
        alto = pg.evaluate("document.body.scrollHeight")
        for y in range(0, alto + 900, 450):
            pg.evaluate(f"window.scrollTo(0, {y})")
            pg.wait_for_timeout(120)
        pg.wait_for_timeout(1500)
        pg.evaluate("window.scrollTo(0, 0)")
        pg.wait_for_timeout(300)
        datos = pg.evaluate(JS_EXTRAER.replace("ANCLAS", json.dumps(sorted(ANCLAS))))
        b.close()
    srv.shutdown()

    contenido = datos["html"]
    bloque = (
        f"{INICIO}\n"
        f'<style>x-dc{{display:none!important}}</style>\n'
        f'<div id="suxtr-prerender">\n<style>{datos["css"]}</style>\n{contenido}\n</div>\n'
        # en cuanto la web real crea #dc-root se quita la copia, antes de que se pinte nada (sin saltos de diseño)
        "<script>(function(){var p=document.getElementById('suxtr-prerender');if(!p)return;"
        "var o=new MutationObserver(function(){if(document.getElementById('dc-root')){o.disconnect();p.remove();}});"
        "o.observe(document.body,{childList:true,subtree:true})})();</script>\n"
        f"{FIN}\n"
    )
    src = envolver_plantilla(src)
    src = src.replace(TPL_ABRE, bloque + TPL_ABRE, 1)
    idx.write_text(src, encoding="utf-8")
    print(f"  ✓ portada pre-renderizada ({len(contenido) // 1024} KB de HTML)")


def main():
    print("Generando páginas…")
    paths = ["/"]
    generadores = ([pagina_backoffice, pagina_servicios] + [partial(pagina_servicio, s) for s in SERVICIOS]
                   + [pagina_sectores] + [partial(pagina_sector, s) for s in SECTORES]
                   + [pagina_blog] + [partial(pagina_articulo, a) for a in ARTICULOS]
                   + [pagina_aviso_legal, pagina_privacidad])
    for fn in generadores:
        path, contenido = fn()
        escribir(path, contenido)
        paths.append(path)
    sitemap(paths)
    llms_txt()
    if "--sin-prerender" not in sys.argv:
        print("Pre-renderizando la portada…")
        prerender()
    pendientes = [k for k, v in TITULAR.items() if not v]
    if pendientes:
        print("\nAviso: faltan datos del titular en scripts/build.py:", ", ".join(pendientes))


if __name__ == "__main__":
    main()
