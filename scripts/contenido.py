"""Textos de las páginas de back office, sectores y blog.

Cada página lleva su HTML en "cuerpo". Usa solo etiquetas sencillas: h2, h3, p, ul/li,
strong y enlaces internos. build.py se encarga de la cabecera, el pie y los datos estructurados.
"""

# ---------------------------------------------------------------------------
# Página pilar
# ---------------------------------------------------------------------------
BACKOFFICE = {
    "path": "/automatizacion-back-office/",
    "title": "Automatización del back office con IA para pymes",
    "meta": "Facturas, albaranes, presupuestos, pedidos y documentación: automatizamos el trabajo administrativo de las pymes con IA, conectada a vuestras herramientas.",
    "h1": "Automatización del back office con IA para pymes",
    "lead": "Facturas de proveedor, albaranes, presupuestos, pedidos que llegan por correo, documentación que nadie encuentra. El trabajo administrativo que no se ve pero se come horas cada semana. Lo automatizamos con IA y lo conectamos con las herramientas que ya usáis.",
    "faq": [
        ("¿Qué es exactamente el back office?", "Es todo el trabajo administrativo que sostiene la empresa sin estar de cara al cliente: compras, facturación, revisión de albaranes, presupuestos, archivo de documentos, conciliaciones e informes."),
        ("¿Hace falta cambiar de ERP o de programa de contabilidad?", "No. La IA se coloca delante de vuestras herramientas: lee, ordena y prepara los datos, y se los pasa a vuestro ERP, a contabilidad o a una hoja de cálculo."),
        ("¿La IA lo hace todo sola?", "Hace el trabajo repetitivo y marca lo dudoso. Las decisiones y las excepciones las sigue viendo una persona, pero solo esas, no todos los documentos."),
        ("¿Por dónde se empieza?", "Por un diagnóstico gratuito de 30 minutos: vemos qué tareas os quitan más tiempo y cuál conviene automatizar primero."),
    ],
    "cuerpo": """
<section><div class="inner">
<p class="eyebrow">El problema</p>
<h2>Horas de oficina que no aportan nada</h2>
<p>En casi todas las pymes hay una o varias personas dedicadas a pasar datos de un sitio a otro: del PDF del proveedor al programa de contabilidad, del parte de trabajo a la factura, del correo del cliente al pedido. Es trabajo necesario, pero no aporta valor y es donde se cuelan los errores.</p>
<p>Además, como lleva tanto tiempo, lo importante se hace tarde: los albaranes se revisan a fin de mes (o nunca), los presupuestos salen días después de la visita y hay trabajos que se olvidan de facturar.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué automatizamos</p>
<h2>Las tareas que más tiempo se comen</h2>
<div class="grid">
<a class="card" href="/servicios/automatizacion-facturas-albaranes/"><h3>Facturas y albaranes de proveedor</h3><p>Lectura automática y cruce entre albarán, factura y pedido. Solo revisáis lo que no cuadra.</p><span class="more">Ver servicio →</span></a>
<a class="card" href="/servicios/presupuestos-facturas-automaticos/"><h3>Presupuestos y facturación</h3><p>Presupuestos y facturas a partir de partes, mediciones y servicios realizados, con vuestras tarifas.</p><span class="more">Ver servicio →</span></a>
<div class="card"><h3>Pedidos que llegan por correo</h3><p>Pedidos de clientes en PDF, Excel o texto del correo que pasan solos a vuestro ERP, listos para servir.</p></div>
<div class="card"><h3>Clasificación de correos y documentos</h3><p>Cada documento a su carpeta, a su responsable o a su flujo, sin que nadie lo tenga que leer primero.</p></div>
<div class="card"><h3>Informes que se hacen solos</h3><p>Resúmenes de compras, márgenes por obra o trabajos pendientes de facturar, generados cada semana.</p></div>
<a class="card" href="/servicios/asistente-ia-documentacion/"><h3>Documentación interna</h3><p>Un asistente que responde con vuestros procedimientos, contratos y manuales, citando la fuente.</p><span class="more">Ver servicio →</span></a>
</div>
</div></section>
<section><div class="inner">
<p class="eyebrow">Cómo lo hacemos</p>
<h2>IA para lo repetitivo, personas para las excepciones</h2>
<ul class="checks">
<li><strong>Sin cambiar vuestra forma de trabajar.</strong> Los documentos siguen llegando por correo, escáner o foto del móvil.</li>
<li><strong>Lectura con IA, no con plantillas.</strong> Entiende formatos distintos de cada proveedor sin configurar uno a uno.</li>
<li><strong>Revisión solo de lo dudoso.</strong> Lo que cuadra pasa solo; lo que no, se os muestra con el documento original al lado.</li>
<li><strong>Conectado a lo que ya usáis.</strong> ERP, programa de contabilidad, hojas de cálculo o correo.</li>
<li><strong>Por fases.</strong> Empezamos por la tarea que más compensa y medimos el resultado antes de seguir.</li>
</ul>
</div></section>
<section><div class="inner">
<p class="eyebrow">Por sectores</p>
<h2>Cómo se aplica en vuestro sector</h2>
<div class="grid">
<a class="card" href="/sectores/construccion-reformas/"><h3>Construcción y reformas</h3><p>Albaranes de materiales por obra, costes imputados y presupuestos desde mediciones.</p><span class="more">Ver sector →</span></a>
<a class="card" href="/sectores/transporte-gruas/"><h3>Transporte y grúas</h3><p>Partes de servicio, kilómetros y esperas convertidos en facturas sin teclear.</p><span class="more">Ver sector →</span></a>
<a class="card" href="/sectores/talleres-mantenimiento/"><h3>Talleres y mantenimiento</h3><p>Órdenes de trabajo, recambios y presupuestos de reparación al día.</p><span class="more">Ver sector →</span></a>
<a class="card" href="/sectores/distribucion-mayoristas/"><h3>Distribución y mayoristas</h3><p>Pedidos por correo al ERP y facturas de proveedor cruzadas con lo recibido.</p><span class="more">Ver sector →</span></a>
</div>
</div></section>
""",
}

# ---------------------------------------------------------------------------
# Sectores
# ---------------------------------------------------------------------------
SECTORES = [
    {
        "slug": "construccion-reformas",
        "nav": "Construcción y reformas",
        "title": "Albaranes y facturas con IA para constructoras y reformas",
        "meta": "Automatizamos albaranes y facturas de proveedor en constructoras y empresas de reformas: coste real por obra, cruce con lo pactado y presupuestos desde la visita.",
        "h1": "Automatización de albaranes y facturas para constructoras y reformas",
        "lead": "Albaranes que se pierden entre obras, facturas de proveedor que nadie cruza y presupuestos que salen tarde. Automatizamos esa parte para que la oficina vaya al ritmo de las obras y sepáis cuánto cuesta cada una mientras se hace.",
        "card": "Albaranes por obra, cruce con facturas y presupuestos desde mediciones.",
        "faq": [
            ("¿Se pueden imputar los albaranes a cada obra?", "Sí. Al leer el albarán se identifica la obra (por referencia, dirección de entrega o pedido) y el coste queda asignado. Si el albarán no trae datos suficientes, el sistema no adivina: lo deja en una bandeja para que alguien lo asigne."),
            ("¿Sirve para presupuestos de reforma muy distintos entre sí?", "Sí. Se parte de las notas de la visita o de una medición y se generan las partidas con vuestras tarifas. Siempre lo revisa alguien antes de enviarlo."),
            ("¿Los encargados tienen que aprender una herramienta nueva?", "No necesariamente. Los albaranes pueden seguir llegando como hoy: una foto desde el móvil, un PDF por correo o papel escaneado en la oficina."),
            ("¿Funciona con facturas de subcontratas y de alquiler de maquinaria?", "Sí. Son documentos con otro formato, pero el planteamiento es el mismo: se leen, se asignan a la obra y se comparan con lo pactado."),
            ("¿Tenemos que cambiar de programa de gestión o de contabilidad?", "No. Nos adaptamos al que uséis. Los datos revisados se pasan por integración, por importación o en una hoja de cálculo."),
            ("¿Cuánto cuesta?", "No publicamos tarifas porque cada solución se construye a medida. Trabajamos por fases cerradas: el alcance y la propuesta de cada fase se definen con vosotros antes de empezar. El diagnóstico inicial sirve para concretarlo."),
            ("¿Cuánto tarda en verse algo funcionando?", "Normalmente entre dos y cuatro semanas hay un prototipo con vuestros documentos reales. La puesta en producción depende de las integraciones que haga falta."),
            ("¿Qué pasa con los precios pactados con cada proveedor?", "Son información confidencial y se tratan como tal: firmamos acuerdo de confidencialidad, trabajamos con proveedores que no usan vuestros datos para entrenar modelos y, si hace falta, se despliega en vuestra infraestructura."),
        ],
        "cuerpo": """
<section><div class="inner">
<p class="eyebrow">Lo que pasa hoy</p>
<h2>Muchas obras, muchos proveedores, mucho papel</h2>
<p>En una empresa de construcción, reformas o rehabilitación llegan cada semana decenas de albaranes de almacenes de materiales, alquiler de maquinaria y subcontratas. A menudo viajan en la furgoneta, se fotografían con el móvil o se quedan en la obra.</p>
<p>A fin de mes llegan las facturas y toca comprobar, una a una, que lo facturado coincide con lo entregado y con el precio pactado. Como es tan pesado, se hace por encima, y así se pagan materiales que no llegaron o precios que no eran los acordados. Y saber cuánto lleva gastado cada obra se convierte en un trabajo de días.</p>
<p>El resultado es que el margen de una obra se conoce cuando ya está terminada, justo cuando ya no se puede corregir nada.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Dónde se escapa el dinero</p>
<h2>Los descuadres de siempre</h2>
<div class="grid">
<div class="card"><h3>Precios que no son los pactados</h3><p>La factura aplica la tarifa general en lugar del precio acordado o de un descuento. Con decenas de líneas por factura, nadie lo ve.</p></div>
<div class="card"><h3>Material que no llegó o llegó a medias</h3><p>Se factura el pedido completo y a la obra llegó una parte. Sin el albarán delante, se paga igual.</p></div>
<div class="card"><h3>Albaranes que nunca se facturan</h3><p>No es dinero perdido, pero el coste de la obra queda incompleto y el margen que creéis tener no es el real.</p></div>
<div class="card"><h3>Portes y recargos no acordados</h3><p>Aparecen en la factura sin que nadie los pactara. Son pequeños, pero se repiten en cada pedido.</p></div>
<div class="card"><h3>Facturas duplicadas</h3><p>El mismo albarán en dos facturas, o la misma factura recibida dos veces por correo.</p></div>
<div class="card"><h3>Gasto sin obra asignada</h3><p>Cuando el albarán no dice a qué obra va, el gasto acaba en «varios» y el coste real de cada obra se conoce tarde.</p></div>
</div>
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué automatizamos</p>
<h2>Qué cambia con IA</h2>
<ul class="checks">
<li>Los albaranes se leen al llegar (foto, PDF o correo) y se asignan a su obra.</li>
<li>Las facturas de proveedor se cruzan automáticamente con sus albaranes y con los precios pactados.</li>
<li>Avisos de diferencias: cantidades, precios, portes, albaranes sin facturar o facturas duplicadas.</li>
<li>Coste acumulado por obra actualizado cada día, no a fin de mes.</li>
<li>Presupuestos de reforma a partir de las notas de la visita o de una medición, con vuestras partidas y tarifas.</li>
</ul>
<p>Más detalle en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a> y <a href="/servicios/presupuestos-facturas-automaticos/">presupuestos y facturas automáticos</a>.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Cómo funciona</p>
<h2>Así queda el día a día en la oficina</h2>
<div class="grid">
<div class="card"><span class="num">01</span><h3>Llega el albarán</h3><p>El encargado hace una foto, el almacén lo manda por correo o llega en PDF. Cada uno sigue trabajando como hasta ahora.</p></div>
<div class="card"><span class="num">02</span><h3>Se lee y se asigna</h3><p>La IA extrae proveedor, líneas, cantidades y precios, e identifica la obra por referencia, dirección o pedido. Si duda, lo marca.</p></div>
<div class="card"><span class="num">03</span><h3>Se cruza con la factura</h3><p>Cuando llega la factura se compara con sus albaranes y con los precios pactados. Solo se señalan las diferencias.</p></div>
<div class="card"><span class="num">04</span><h3>Veis el coste de cada obra</h3><p>El gasto por obra se actualiza según llegan los documentos. Lo correcto pasa a contabilidad; lo dudoso lo revisa una persona.</p></div>
</div>
</div></section>
<section><div class="inner">
<p class="eyebrow">Documentos</p>
<h2>Qué documentos leemos</h2>
<ul class="checks">
<li><strong>Albaranes de materiales</strong> en foto del móvil, PDF o papel escaneado, con o sin anotaciones a mano.</li>
<li><strong>Facturas de proveedores</strong>, de subcontratas y de alquiler de maquinaria.</li>
<li><strong>Tarifas o precios pactados</strong> con cada proveedor, para compararlos con lo facturado.</li>
<li><strong>Notas de visita y mediciones</strong>, para preparar presupuestos de reforma.</li>
</ul>
</div></section>
<section><div class="inner">
<p class="eyebrow">Por dónde empezar</p>
<h2>Un proveedor, unas cuantas obras</h2>
<p>No hace falta cambiarlo todo. Lo habitual es empezar por uno o dos proveedores con mucho volumen y varias obras en marcha: en dos a cuatro semanas hay un prototipo funcionando con vuestros documentos reales, y se mide frente a cómo lo hacéis hoy.</p>
<p>Si compensa, se amplía a más proveedores y obras. Si no, lo sabéis pronto y con poco gasto. Podéis ver cómo encaja en el conjunto del <a href="/automatizacion-back-office/">back office con IA</a>.</p>
</div></section>
""",
    },
    {
        "slug": "transporte-gruas",
        "nav": "Transporte y grúas",
        "title": "IA para transporte y grúas: facturación automática",
        "meta": "Facturación automática para transporte y grúas de asistencia: partes, kilómetros, esperas y peajes convertidos en facturas sin teclear.",
        "h1": "IA para empresas de transporte y grúas",
        "lead": "Cada servicio genera un parte con kilómetros, horas de espera, peajes y suplementos. Pasarlo a factura a mano lleva horas y siempre se escapa algo. Lo automatizamos.",
        "card": "Partes de servicio, kilómetros y esperas convertidos en facturas sin teclear.",
        "faq": [
            ("¿Funciona con las tarifas de cada aseguradora o cliente?", "Sí. Cada cliente tiene sus tarifas y condiciones, y el sistema aplica las que tocan a cada servicio. Lo que no encaja se marca para revisarlo."),
            ("¿Los conductores tienen que cambiar cómo rellenan el parte?", "No necesariamente. Se puede leer el parte tal y como se hace hoy, aunque sea en papel y con una foto. Si queréis, también se puede pasar a un formulario en el móvil."),
        ],
        "cuerpo": """
<section><div class="inner">
<p class="eyebrow">Lo que pasa hoy</p>
<h2>Cada servicio es una factura distinta</h2>
<p>En el transporte y la asistencia en carretera cada servicio es diferente: salida, kilómetros con y sin carga, horas de espera, peajes, trabajo nocturno o en festivo, suplementos. Y cada cliente o aseguradora tiene sus propias tarifas y su forma de recibir la factura.</p>
<p>Todo eso suele estar en partes en papel, en mensajes o en una hoja de cálculo. Convertirlo en facturas lleva horas en la oficina y es fácil olvidarse de un suplemento o de una espera, que es dinero que no se cobra.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué automatizamos</p>
<h2>Qué cambia con IA</h2>
<ul class="checks">
<li>Lectura del parte de servicio, aunque sea una foto del papel.</li>
<li>Cálculo de cada línea con las tarifas de ese cliente: kilómetros, esperas, peajes y suplementos.</li>
<li>Factura preparada en vuestro programa de facturación, lista para revisar y enviar.</li>
<li>Avisos de servicios realizados que aún no se han facturado.</li>
<li>Lectura de facturas de proveedores (combustible, talleres, peajes) y cruce con lo esperado.</li>
</ul>
<p>Más detalle en <a href="/servicios/presupuestos-facturas-automaticos/">presupuestos y facturas automáticos</a>.</p>
</div></section>
""",
    },
    {
        "slug": "talleres-mantenimiento",
        "nav": "Talleres y mantenimiento",
        "title": "IA para talleres: órdenes de trabajo y facturas",
        "meta": "Automatizamos el back office de talleres y empresas de mantenimiento: órdenes de trabajo, facturas de recambios y presupuestos de reparación sin teclear.",
        "h1": "IA para talleres y empresas de mantenimiento",
        "lead": "Órdenes de trabajo, recambios que llegan con su albarán, presupuestos de reparación y facturas al cliente. Automatizamos la parte administrativa para que el taller no dependa de la oficina.",
        "card": "Órdenes de trabajo, recambios y presupuestos de reparación al día.",
        "faq": [
            ("¿Se integra con nuestro programa de gestión del taller?", "En la mayoría de casos sí, por integración directa o por importación. Lo vemos en el diagnóstico con vuestro programa concreto."),
            ("¿Y si un recambio llega sin pedido?", "Se marca como incidencia para que alguien decida si se acepta, se devuelve o se asigna a una orden de trabajo."),
        ],
        "cuerpo": """
<section><div class="inner">
<p class="eyebrow">Lo que pasa hoy</p>
<h2>El taller trabaja, la oficina se atasca</h2>
<p>En un taller o una empresa de mantenimiento cada reparación mueve papel: la orden de trabajo, los recambios pedidos a varios proveedores con sus albaranes, las horas de cada técnico, el presupuesto que hay que aprobar y la factura final.</p>
<p>Cuando todo eso se pasa a mano, las facturas de recambios no se comprueban contra lo pedido, hay horas que no se cargan a la orden y los presupuestos tardan en salir.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué automatizamos</p>
<h2>Qué cambia con IA</h2>
<ul class="checks">
<li>Lectura de albaranes y facturas de recambios y cruce con los pedidos y las órdenes de trabajo.</li>
<li>Presupuestos de reparación a partir del diagnóstico del técnico, con vuestros precios de mano de obra y recambios.</li>
<li>Facturas al cliente preparadas a partir de la orden de trabajo cerrada.</li>
<li>Avisos de órdenes terminadas pendientes de facturar.</li>
</ul>
<p>Más detalle en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
</div></section>
""",
    },
    {
        "slug": "distribucion-mayoristas",
        "nav": "Distribución y mayoristas",
        "title": "IA para distribuidores: pedidos y facturas automáticos",
        "meta": "Para distribuidores y mayoristas: pedidos que llegan por correo pasan solos al ERP y las facturas de proveedor se cruzan con lo recibido.",
        "h1": "IA para distribuidores y mayoristas",
        "lead": "Pedidos de clientes en PDF, Excel o en el cuerpo del correo, y facturas de proveedores que hay que cruzar con lo recibido. Automatizamos las dos puntas para que el almacén no espere a la oficina.",
        "card": "Pedidos por correo al ERP y facturas de proveedor cruzadas con lo recibido.",
        "faq": [
            ("¿Entiende pedidos escritos de forma libre?", "Sí. La IA reconoce los productos aunque el cliente use su propia descripción o su referencia, y pregunta cuando no está segura."),
            ("¿Qué pasa con los precios especiales de cada cliente?", "Se aplican las tarifas que tengáis en el ERP para cada cliente; si un pedido trae un precio distinto, se marca para revisar."),
        ],
        "cuerpo": """
<section><div class="inner">
<p class="eyebrow">Lo que pasa hoy</p>
<h2>Teclear pedidos y comprobar facturas</h2>
<p>En la distribución el volumen está en los detalles: decenas de pedidos al día que llegan cada uno en un formato, y facturas de proveedores que hay que comprobar contra lo que realmente entró en el almacén.</p>
<p>Teclear los pedidos en el ERP retrasa la preparación y provoca errores de referencia o de cantidad. Y comprobar las facturas de compra se suele dejar para cuando hay tiempo.</p>
</div></section>
<section><div class="inner">
<p class="eyebrow">Qué automatizamos</p>
<h2>Qué cambia con IA</h2>
<ul class="checks">
<li>Lectura de pedidos de clientes desde el correo (PDF, Excel o texto) y alta automática en el ERP.</li>
<li>Reconocimiento de productos por descripción o referencia del cliente.</li>
<li>Facturas de proveedor cruzadas con pedidos de compra y entradas de almacén.</li>
<li>Avisos de precios distintos a la tarifa, faltas y duplicados.</li>
</ul>
<p>Más detalle en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
</div></section>
""",
    },
]

# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------
ARTICULOS = [
    {
        "slug": "cruzar-albaranes-con-facturas",
        "fecha": "2026-11-23",
        "modificado": "2026-11-27",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas", "distribucion-mayoristas", "talleres-mantenimiento"]},
        "title": "Cómo cruzar albaranes con facturas sin hacerlo a mano",
        "meta": "Guía práctica para cruzar albaranes con facturas de proveedor: errores habituales, cómo hacerlo bien en Excel y cuándo compensa automatizarlo con IA.",
        "h1": "Cómo cruzar albaranes con facturas de proveedor sin hacerlo a mano",
        "resumen": "Por qué conviene cruzar albaranes con facturas, qué errores se detectan, cómo organizarlo en una hoja de cálculo y cuándo compensa automatizarlo.",
        "cuerpo": """
<p>Comprobar que lo que factura cada proveedor coincide con lo que realmente se recibió es una de esas tareas que todas las empresas saben que deberían hacer y casi ninguna hace bien. No por descuido, sino porque hacerlo a mano lleva muchísimo tiempo.</p>
<h2>Por qué merece la pena cruzar albaranes y facturas</h2>
<p>El albarán es la prueba de lo que se entregó; la factura, lo que se cobra. Entre uno y otro aparecen diferencias con más frecuencia de lo que parece, casi siempre sin mala intención: un error al teclear, una tarifa antigua, un porte que se cobra dos veces. Si nadie compara, esas diferencias se pagan.</p>
<h2>Los errores más habituales</h2>
<ul>
<li><strong>Precio distinto al pactado:</strong> la factura aplica la tarifa general en lugar del precio acordado o el descuento.</li>
<li><strong>Cantidades:</strong> se factura más material del que consta en el albarán, o se factura un pedido completo que llegó a medias.</li>
<li><strong>Albaranes facturados dos veces</strong> en facturas distintas.</li>
<li><strong>Portes y recargos</strong> que no estaban acordados.</li>
<li><strong>Albaranes que nunca se facturan:</strong> no es dinero perdido, pero sí descuadres en el coste real de cada trabajo u obra.</li>
</ul>
<h2>Cómo hacerlo bien a mano</h2>
<p>Si todavía no queréis automatizar nada, una hoja de cálculo bien organizada ya ayuda mucho:</p>
<ol>
<li>Registrad cada albarán al recibirlo, no a fin de mes: proveedor, número, fecha, obra o pedido y líneas con cantidad.</li>
<li>Al llegar la factura, marcad qué albaranes incluye y comparad línea a línea cantidades y precios con la tarifa pactada.</li>
<li>Dejad una columna de estado (cuadra, diferencia, pendiente) y otra de comentario para reclamar.</li>
<li>Una vez al mes, filtrad los albaranes sin facturar y los facturados dos veces.</li>
</ol>
<p>Para empezar rápido, tenéis una <a href="/blog/plantilla-excel-cruce-albaranes-facturas/">plantilla de Excel para cruzar albaranes con facturas</a> que hace las comparaciones y marca las diferencias. Y si queréis un repaso más amplio antes de pagar, la <a href="/blog/comprobar-factura-proveedor-antes-de-pagar/">lista de comprobaciones para una factura de proveedor</a>.</p>
<p>El problema es el tiempo: con muchos proveedores, registrar y comparar se convierte en horas cada semana, y es justo lo primero que se deja de hacer cuando hay prisa.</p>
<h2>Cuándo compensa automatizarlo</h2>
<p>Compensa cuando recibís muchos albaranes al mes, de varios proveedores y en formatos distintos (PDF, papel, foto), o cuando necesitáis saber el coste real de cada obra o trabajo sin esperar al cierre.</p>
<p>Con IA el proceso es el mismo de la lista anterior, pero sin teclear: los albaranes y las facturas se leen al llegar, sea cual sea el formato; se cruzan entre sí y con los precios pactados, y solo se os enseñan las diferencias, con el documento original al lado para decidir. Lo que cuadra pasa directamente a contabilidad.</p>
<p>Si trabajáis en obra o reformas, el siguiente paso es <a href="/blog/imputar-albaranes-a-obra/">imputar cada albarán a su obra</a> y <a href="/blog/control-costes-por-obra/">controlar el coste de cada obra</a>. Y si queréis ver cómo funcionaría con vuestros documentos, lo explicamos en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
""",
    },
    {
        "slug": "ocr-o-ia-para-leer-facturas",
        "fecha": "2026-11-23",
        "modificado": "2026-11-27",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas"]},
        "title": "OCR o IA para leer facturas: diferencias",
        "meta": "Diferencias entre el OCR tradicional y la lectura de facturas con IA: plantillas, formatos distintos, errores y cuándo conviene cada uno.",
        "h1": "OCR o IA para leer facturas: qué diferencia hay",
        "resumen": "El OCR convierte la imagen en texto; la IA entiende qué es cada dato. Cuándo basta con uno y cuándo hace falta la otra.",
        "cuerpo": """
<p>Cuando una empresa quiere dejar de teclear facturas, la primera palabra que aparece es OCR. Pero leer el texto de una factura no es lo mismo que entenderla, y esa diferencia es la que explica por qué muchas implantaciones de OCR acaban con alguien corrigiendo datos igualmente.</p>
<h2>Qué hace el OCR</h2>
<p>El reconocimiento óptico de caracteres (OCR) convierte una imagen o un PDF escaneado en texto. Es una tecnología madura y muy fiable para eso: sabe qué letras y números hay en la página.</p>
<p>Lo que no sabe es qué significa cada cosa. Para extraer el número de factura, la fecha o el total, el OCR tradicional necesita reglas o plantillas: «el total está abajo a la derecha, después de la palabra TOTAL». Funciona bien con pocos proveedores que siempre envían el mismo formato.</p>
<h2>Qué añade la IA</h2>
<p>Los modelos de IA actuales no se limitan a leer el texto: interpretan el documento como lo haría una persona. Reconocen cuál es el proveedor, qué líneas son conceptos y cuáles descuentos, dónde está la base imponible aunque cada proveedor la llame de forma distinta, o que un número escrito a mano en un albarán es una cantidad.</p>
<ul>
<li><strong>Sin plantillas por proveedor:</strong> un proveedor nuevo o un cambio de formato no rompe nada.</li>
<li><strong>Documentos difíciles:</strong> fotos torcidas, albaranes con anotaciones a mano, tablas con muchas líneas.</li>
<li><strong>Contexto:</strong> puede comprobar que las líneas suman el total o que el IVA es coherente, y avisar cuando algo no cuadra.</li>
</ul>
<h2>¿Y los errores?</h2>
<p>Ningún sistema acierta el cien por cien. La diferencia está en qué hace cuando duda. Un buen sistema con IA indica su nivel de confianza en cada dato y manda a revisión humana solo lo dudoso, en lugar de dar por bueno un dato mal leído.</p>
<h2>Cuál necesita tu empresa</h2>
<p>Si recibís pocas facturas, siempre de los mismos proveedores y en PDF digital, un OCR con plantillas puede ser suficiente. Si tenéis muchos proveedores, formatos variados, albaranes en papel o fotos desde la obra, la IA os ahorrará el mantenimiento de plantillas y gran parte de la corrección manual.</p>
<p>Y si el objetivo no es solo leer, sino cruzar facturas con albaranes y pedidos, la IA es casi imprescindible. Lo contamos en <a href="/blog/cruzar-albaranes-con-facturas/">cómo cruzar albaranes con facturas</a>. Y si estáis eligiendo herramienta, <a href="/blog/software-albaranes-constructoras/">qué mirar antes de elegir un software de albaranes</a>.</p>
""",
    },
    {
        "slug": "tareas-administrativas-automatizar-pyme",
        "fecha": "2026-11-23",
        "modificado": "2026-11-27",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes", "presupuestos-facturas-automaticos"], "sectores": ["construccion-reformas"]},
        "title": "7 tareas administrativas que una pyme puede automatizar",
        "meta": "Las tareas de back office que más tiempo quitan en una pyme y que ya se pueden automatizar con IA: facturas, albaranes, presupuestos y pedidos.",
        "h1": "7 tareas administrativas que una pyme puede automatizar con IA",
        "resumen": "De la lectura de facturas a los informes semanales: dónde está el tiempo de la oficina y qué parte se puede automatizar ya.",
        "cuerpo": """
<p>No hace falta un gran proyecto para notar la IA en la oficina. Las mejores primeras automatizaciones son tareas pequeñas, repetitivas y que hoy dependen de que alguien teclee datos. Estas son siete de las más habituales en pymes.</p>
<h2>1. Registrar facturas de proveedor</h2>
<p>Leer cada factura y pasar proveedor, fecha, importes e IVA al programa de contabilidad. Es la tarea más fácil de automatizar y la que antes se nota. <a href="/blog/ocr-o-ia-para-leer-facturas/">Aquí explicamos la diferencia entre OCR e IA</a> para hacerlo.</p>
<h2>2. Cruzar albaranes con facturas</h2>
<p>Comprobar que lo facturado coincide con lo entregado y con el precio pactado. Automatizado, solo revisáis las diferencias. <a href="/blog/cruzar-albaranes-con-facturas/">Guía completa</a> y <a href="/blog/plantilla-excel-cruce-albaranes-facturas/">plantilla de Excel</a> para empezar.</p>
<h2>3. Preparar presupuestos</h2>
<p>Convertir las notas de una visita, una medición o la petición de un cliente en un presupuesto con vuestras partidas y tarifas. Un borrador en minutos que alguien revisa y envía. En reformas, <a href="/blog/presupuesto-reforma-desde-visita/">cómo preparar el presupuesto a partir de la visita</a>.</p>
<h2>4. Facturar trabajos y servicios</h2>
<p>Pasar partes de trabajo, horas, kilómetros o materiales a factura sin volver a teclearlos, y detectar lo que se ha hecho y no se ha facturado.</p>
<h2>5. Dar de alta pedidos que llegan por correo</h2>
<p>Leer pedidos en PDF, Excel o en el propio correo y darlos de alta en el ERP sin intervención, con aviso cuando algo no está claro.</p>
<h2>6. Clasificar correos y documentos</h2>
<p>Enviar cada documento a su carpeta, su responsable o su flujo de trabajo: facturas a contabilidad, pedidos a almacén, consultas a quien corresponda.</p>
<h2>7. Informes semanales</h2>
<p>Compras del mes, coste por obra, trabajos pendientes de facturar o presupuestos sin respuesta, generados solos cada lunes en lugar de montarlos a mano. Para obras, mirad <a href="/blog/control-costes-por-obra/">control de costes por obra</a>.</p>
<h2>Por dónde empezar</h2>
<p>Elegid la tarea que más horas os quita y que siga siempre los mismos pasos. Automatizad solo esa, medid el resultado y después pasad a la siguiente. En el <a href="/automatizacion-back-office/">back office con IA</a> explicamos cómo lo planteamos, y el diagnóstico inicial es gratuito.</p>
""",
    },
    {
        "slug": "control-costes-por-obra",
        "fecha": "2026-11-27",
        "title": "Control de costes por obra: cómo saber lo que llevas gastado",
        "meta": "Cómo controlar el coste real de cada obra: qué datos registrar, dónde se descuadra casi siempre y cómo tener el gasto al día sin esperar al cierre de mes.",
        "h1": "Control de costes por obra: cómo saber lo que llevas gastado sin esperar al cierre",
        "resumen": "El presupuesto de obra solo sirve si se compara con el gasto real a tiempo. Qué registrar, dónde se descuadra y cómo no depender del cierre de mes.",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas"]},
        "cuerpo": """
<p>En muchas constructoras y empresas de reformas, saber si una obra ha dado dinero es algo que se descubre al terminarla. Para entonces ya no hay nada que corregir. El control de costes consiste justo en lo contrario: comparar lo presupuestado con lo gastado mientras la obra sigue en marcha, a tiempo de actuar.</p>
<h2>Qué hay que comparar</h2>
<p>La comparación útil es entre el presupuesto y el gasto real, y cuanto más desglosada, mejor. Con un solo total por obra solo sabréis que os habéis pasado, no en qué. Lo habitual es separar por capítulos o partidas y, dentro de cada una, por tipo de gasto:</p>
<ul>
<li><strong>Materiales</strong>, que llegan con un albarán.</li>
<li><strong>Subcontratas</strong>, que se certifican o facturan por trabajo hecho.</li>
<li><strong>Maquinaria y medios auxiliares</strong>, normalmente alquilados.</li>
<li><strong>Mano de obra propia</strong>, a partir de los partes de horas.</li>
</ul>
<h2>De dónde sale el gasto real</h2>
<p>La fuente más temprana del gasto de materiales no es la factura, sino el albarán. El albarán llega el día que se entrega el material; la factura puede tardar semanas. Si esperáis a la factura para registrar el gasto, siempre iréis con retraso.</p>
<p>Por eso conviene registrar los albaranes al recibirlos y usar las facturas para confirmar y cerrar, no para descubrir el gasto. Lo explicamos con más detalle en <a href="/blog/imputar-albaranes-a-obra/">cómo imputar los albaranes a cada obra</a>.</p>
<h2>Dónde se descuadra casi siempre</h2>
<ul>
<li><strong>Gasto sin obra asignada.</strong> Albaranes que no dicen a qué obra van y acaban en un cajón o en «varios».</li>
<li><strong>Registro a fin de mes.</strong> Los documentos se acumulan y se pasan todos juntos, cuando ya es tarde para reaccionar.</li>
<li><strong>Facturas que llegan tarde.</strong> El gasto existe, pero no consta hasta que llega el papel.</li>
<li><strong>Cambios del cliente sin presupuestar.</strong> Se hace el trabajo adicional, se gasta el material y no se refleja ni en el presupuesto ni en la facturación.</li>
<li><strong>Precios distintos a los pactados.</strong> El coste real es mayor que el previsto sin que nadie lo note. Es el problema que tratamos en <a href="/blog/cruzar-albaranes-con-facturas/">cómo cruzar albaranes con facturas</a>.</li>
</ul>
<h2>Un método sencillo para empezar</h2>
<ol>
<li>Dad a cada obra un código corto y único, y pedid a los proveedores que lo incluyan en pedidos y albaranes.</li>
<li>Registrad cada albarán el día que llega, con su obra y, si podéis, su partida.</li>
<li>Una vez por semana, comparad el gasto acumulado de cada obra con su presupuesto, partida por partida.</li>
<li>Fijad un umbral de desviación (por ejemplo, un 10 % sobre lo previsto en una partida) a partir del cual se revisa qué ha pasado.</li>
<li>Cuando llegue la factura, cruzadla con sus albaranes antes de pagarla.</li>
<li>Al cerrar la obra, anotad las desviaciones y su causa para ajustar los próximos presupuestos.</li>
</ol>
<h2>Dónde ayuda la automatización</h2>
<p>El método funciona, pero depende de que alguien registre cada albarán y cada factura a tiempo, y es lo primero que se abandona cuando hay mucha obra en marcha. La parte que más se puede automatizar es justo esa: leer los albaranes al llegar (aunque sean una foto desde la obra), asignarlos a su obra, cruzarlos con la factura y mostrar el coste acumulado actualizado.</p>
<p>Si queréis ver cómo se aplicaría en vuestra empresa, lo contamos en <a href="/sectores/construccion-reformas/">automatización de albaranes y facturas para constructoras y reformas</a>.</p>
""",
    },
    {
        "slug": "imputar-albaranes-a-obra",
        "fecha": "2026-11-27",
        "title": "Imputar albaranes a obra: método y errores habituales",
        "meta": "Cómo asignar cada albarán de materiales a su obra y partida: referencia de obra, quién lo anota, errores habituales y cómo automatizarlo cuando hay mucho volumen.",
        "h1": "Cómo imputar los albaranes a cada obra: método y errores habituales",
        "resumen": "Un albarán sin obra es un gasto sin dueño. Cómo conseguir que cada albarán llegue con su obra asignada y qué hacer con los que no la traen.",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas"]},
        "cuerpo": """
<p>Imputar un albarán es asignar su coste a la obra (y, si se puede, a la partida) a la que corresponde. Parece un trámite menor, pero de él depende que el coste de cada obra sea fiable. Un albarán sin obra es un gasto sin dueño: se paga, pero no se sabe a quién cargarlo.</p>
<h2>Por qué falla la imputación</h2>
<ul>
<li><strong>El albarán no dice la obra.</strong> El proveedor solo pone el nombre de la empresa, y quien recogió el material dijo de palabra para qué obra era.</li>
<li><strong>Llega tarde a la oficina.</strong> Los albaranes viajan en la furgoneta, en la cartera del encargado o en una carpeta de la obra, y llegan juntos al final de la semana o del mes.</li>
<li><strong>Está ilegible.</strong> Una foto torcida, un papel arrugado o una anotación a mano que nadie entiende pasadas unas semanas.</li>
<li><strong>El material sirve para varias obras.</strong> Un pedido grande que se reparte entre dos o tres obras y que nadie divide.</li>
<li><strong>La dirección de entrega no coincide.</strong> El material se entrega en el almacén, en casa del encargado o en una dirección que no es la de la obra.</li>
</ul>
<h2>Cómo imputar bien</h2>
<ol>
<li><strong>Un código de obra corto y único</strong> (por ejemplo, el año y un número correlativo). Comunicádselo a los proveedores y pedid que figure en el pedido y en el albarán.</li>
<li><strong>Quien pide o recoge el material anota la obra</strong>, en el momento. Es mucho más fácil que averiguarlo semanas después.</li>
<li><strong>Foto del albarán el mismo día</strong>, con el papel plano y bien iluminado, y enviada a un único sitio (un correo o una carpeta compartida).</li>
<li><strong>La oficina registra el albarán al recibirlo</strong>, no a fin de mes, con su obra y su partida.</li>
<li><strong>Los repartos se dividen</strong> por unidades o por porcentajes, y se anota el criterio.</li>
<li><strong>Se revisa cada semana</strong> la lista de albaranes sin obra asignada, antes de que se acumulen.</li>
</ol>
<h2>Qué hacer con los albaranes sin obra</h2>
<p>Lo peor es dejarlos en «varios» y esperar a que alguien se acuerde. Conviene tener una bandeja de «pendientes de asignar» con una persona responsable, y revisarla con una frecuencia fija. Una pista habitual para resolverlos es la dirección de entrega, la fecha o el número de pedido: casi siempre alguien sabe a qué obra correspondía.</p>
<h2>Cómo ayuda la IA</h2>
<p>La lectura automática del albarán extrae proveedor, líneas, cantidades y precios, y busca en el documento los datos que indican la obra: la referencia, la dirección de entrega o el número de pedido. Cuando los encuentra, propone la obra; cuando no está seguro, no inventa: lo deja marcado para que una persona lo asigne con el documento original delante.</p>
<p>Así el coste de cada obra se mantiene al día sin que nadie tenga que teclear cada albarán. Y con el gasto asignado, el siguiente paso es <a href="/blog/control-costes-por-obra/">controlar los costes por obra</a> y <a href="/blog/cruzar-albaranes-con-facturas/">cruzar los albaranes con las facturas</a> antes de pagarlas. Si queréis verlo aplicado a vuestro caso, lo explicamos en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
""",
    },
    {
        "slug": "presupuesto-reforma-desde-visita",
        "fecha": "2026-11-27",
        "title": "Presupuesto de reforma: cómo hacerlo rápido tras la visita",
        "meta": "Cómo preparar presupuestos de reforma más rápido: qué anotar en la visita, cómo estructurar las partidas y cuándo ayuda la IA a convertir las notas en presupuesto.",
        "h1": "Presupuesto de reforma: cómo prepararlo rápido a partir de la visita",
        "resumen": "Qué anotar en la visita, cómo estructurar las partidas y dónde se pierde el tiempo al pasar las notas a presupuesto, y cómo acortarlo.",
        "relacion": {"servicios": ["presupuestos-facturas-automaticos"], "sectores": ["construccion-reformas"]},
        "cuerpo": """
<p>En una reforma, el cliente suele pedir varios presupuestos y se queda, en buena medida, con el que le llega antes y con más claridad. Pero cada reforma es distinta y preparar el presupuesto lleva horas: hay que pasar las notas de la visita a partidas, ponerles precio y maquetarlo todo. Estas son algunas ideas para acortar ese camino.</p>
<h2>Qué conviene anotar en la visita</h2>
<p>Un presupuesto rápido empieza con unas buenas notas. Si faltan datos, hay que volver a llamar al cliente o volver a la obra.</p>
<ul>
<li><strong>Mediciones:</strong> metros cuadrados, metros lineales y unidades de cada espacio a reformar.</li>
<li><strong>Fotos</strong> del estado actual y de cualquier detalle que condicione el trabajo.</li>
<li><strong>Alcance:</strong> qué entra y qué no, dicho en voz alta con el cliente y anotado.</li>
<li><strong>Calidades y materiales</strong> que ha elegido el cliente, o los que le habéis propuesto.</li>
<li><strong>Condicionantes:</strong> acceso, escaleras, ascensor, horarios, permisos o normas de la comunidad.</li>
<li><strong>Plazos</strong> que espera el cliente.</li>
</ul>
<h2>Estructurar el presupuesto por partidas</h2>
<p>Un presupuesto claro se organiza por capítulos (demolición, albañilería, fontanería, electricidad, alicatados, carpintería, pintura…) y, dentro de cada uno, por partidas con unidad, cantidad, precio unitario e importe. Conviene incluir también lo que no está incluido, el plazo estimado y las condiciones de pago.</p>
<p>Cuanto más desglosado, más fácil es defenderlo ante el cliente y, después, comparar lo presupuestado con lo gastado de verdad (<a href="/blog/control-costes-por-obra/">control de costes por obra</a>).</p>
<h2>Dónde se pierde el tiempo</h2>
<ul>
<li><strong>Pasar las notas a partidas.</strong> Interpretar la libreta o el audio de la visita y convertirlo en conceptos presupuestables.</li>
<li><strong>Buscar precios.</strong> Si no hay un tarifario propio actualizado, cada partida es una búsqueda.</li>
<li><strong>Maquetar.</strong> Poner el presupuesto en la plantilla de la empresa, con su imagen y sus condiciones.</li>
<li><strong>Revisar.</strong> Comprobar que no falta nada y que las sumas cuadran.</li>
</ul>
<h2>Mantened un tarifario propio</h2>
<p>La base de un presupuesto rápido es un tarifario de partidas con vuestro precio unitario, revisado cada cierto tiempo con los precios reales de proveedores y subcontratas. Con él, presupuestar es medir y multiplicar; sin él, es empezar de cero cada vez.</p>
<h2>Dónde ayuda la IA</h2>
<p>La IA es especialmente útil en el primer paso: convertir las notas de la visita, una medición o incluso un audio en un borrador de partidas, usando vuestro tarifario y vuestra plantilla. Propone; no decide. Una persona del equipo revisa el borrador, ajusta lo que haga falta y lo envía.</p>
<p>No sustituye vuestro criterio sobre qué hace falta en una reforma, pero sí el tiempo de tecleo y de maquetación. Lo contamos en <a href="/servicios/presupuestos-facturas-automaticos/">presupuestos y facturas automáticos</a>, y el contexto del sector en <a href="/sectores/construccion-reformas/">constructoras y reformas</a>.</p>
""",
    },
    {
        "slug": "software-albaranes-constructoras",
        "fecha": "2026-11-27",
        "title": "Software de albaranes para constructoras: qué mirar",
        "meta": "Criterios para elegir un software de albaranes en una constructora o empresa de reformas: captura, imputación a obra, cruce con facturas e integración.",
        "h1": "Software para gestionar albaranes en una constructora: qué mirar antes de elegir",
        "resumen": "Hay muchas herramientas y no todas resuelven el mismo problema. Los criterios para comparar y las preguntas que conviene hacer antes de contratar.",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas"]},
        "cuerpo": """
<p>«Software de albaranes» puede significar cosas muy distintas: un módulo de compras dentro de un programa de gestión de obra, una aplicación que lee documentos, una hoja de cálculo bien montada o un sistema con IA. Antes de comparar productos conviene tener claro qué problema se quiere resolver.</p>
<h2>Primero, qué problema queréis resolver</h2>
<ul>
<li><strong>Saber el coste real de cada obra</strong> mientras se hace.</li>
<li><strong>Comprobar las facturas de proveedor</strong> contra lo que llegó y contra los precios pactados.</li>
<li><strong>Dejar de teclear</strong> albaranes y facturas a mano.</li>
</ul>
<p>Muchas herramientas resuelven bien una de las tres y regular las otras. Saber cuál os duele más evita pagar por funciones que no vais a usar.</p>
<h2>Criterios para comparar</h2>
<ol>
<li><strong>Captura.</strong> ¿Se puede hacer una foto desde la obra? ¿Acepta PDF por correo? ¿Y papel escaneado con anotaciones a mano?</li>
<li><strong>Lectura.</strong> ¿Necesita una plantilla por proveedor o entiende formatos distintos? Si tenéis muchos proveedores, esto marca la diferencia: lo explicamos en <a href="/blog/ocr-o-ia-para-leer-facturas/">OCR o IA para leer facturas</a>.</li>
<li><strong>Imputación a obra y partida.</strong> ¿Asigna el albarán a su obra, o solo lo archiva?</li>
<li><strong>Cruce con la factura.</strong> ¿Compara cantidades y precios con los albaranes y con lo pactado, y avisa de las diferencias?</li>
<li><strong>Integración.</strong> ¿Se conecta con vuestro programa de contabilidad o de gestión, o al menos exporta a Excel?</li>
<li><strong>Revisión de excepciones.</strong> ¿Qué ocurre cuando duda? Lo ideal es que lo marque y os enseñe el documento original al lado, no que lo dé por bueno.</li>
<li><strong>Datos.</strong> ¿Dónde se guardan, quién puede verlos y si se pueden exportar si algún día cambiáis de herramienta?</li>
</ol>
<h2>Opciones habituales y cuándo encajan</h2>
<ul>
<li><strong>Hoja de cálculo.</strong> Suficiente con pocos proveedores y poco volumen. Barata, pero depende de que alguien teclee todo. Tenéis una <a href="/blog/plantilla-excel-cruce-albaranes-facturas/">plantilla de Excel para cruzar albaranes con facturas</a> para empezar.</li>
<li><strong>Programa de gestión de obra o ERP con módulo de compras.</strong> Buena opción si ya lo tenéis y lo usáis bien; el reto suele ser alimentarlo con los datos de los albaranes.</li>
<li><strong>Herramientas de OCR con plantillas.</strong> Funcionan cuando los formatos son pocos y estables.</li>
<li><strong>Lectura con IA a medida.</strong> Encaja cuando hay muchos proveedores, formatos variados o fotos desde la obra, y cuando se quiere el cruce con facturas y la imputación a obra. Requiere un proyecto, pero se adapta a vuestro caso.</li>
</ul>
<p>No siempre hace falta IA. Si recibís veinte albaranes al mes de tres proveedores, una buena hoja de cálculo os puede bastar.</p>
<h2>Preguntas para hacer antes de contratar</h2>
<ul>
<li>¿Puedo probarlo con mis documentos reales, no con los de la demo?</li>
<li>¿Qué pasa con un albarán mal escaneado o con un proveedor nuevo?</li>
<li>¿Cuánto tarda en estar funcionando y qué tengo que preparar yo?</li>
<li>¿Quién lo mantiene después y cuánto cuesta?</li>
<li>¿Puedo llevarme mis datos si decido cambiar?</li>
</ul>
<p>Si queréis ver cómo lo planteamos nosotros para empresas del sector, está en <a href="/sectores/construccion-reformas/">automatización de albaranes y facturas para constructoras y reformas</a>.</p>
""",
    },
    {
        "slug": "plantilla-excel-cruce-albaranes-facturas",
        "fecha": "2026-11-27",
        "title": "Plantilla Excel para cruzar albaranes y facturas",
        "meta": "Plantilla de Excel para comprobar facturas de proveedor contra albaranes: cantidades, precios pactados, diferencias y albaranes sin facturar. Descarga directa.",
        "h1": "Plantilla de Excel para cruzar albaranes con facturas de proveedor",
        "resumen": "Una hoja de cálculo lista para registrar albaranes, compararlos con las facturas y ver qué no cuadra. Cómo usarla y cuándo se queda corta.",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas", "distribucion-mayoristas"]},
        "cuerpo": """
<p>Si queréis empezar a comprobar las facturas de proveedor contra los albaranes sin cambiar de herramienta, una hoja de cálculo bien organizada ya recorre buena parte del camino. Hemos preparado una plantilla de Excel que hace las comparaciones por vosotros: solo hay que registrar los documentos.</p>
<p><a class="btn btn-dark" href="/assets/plantilla-cruce-albaranes-facturas.xlsx" download data-umami-event="descarga-plantilla-cruce">Descargar la plantilla (Excel)</a></p>
<h2>Qué incluye</h2>
<ul>
<li><strong>Albaranes:</strong> una línea por cada línea de albarán, con proveedor, obra, concepto, cantidad recibida y precio pactado. A su derecha, columnas calculadas que muestran cuánto se ha facturado, la diferencia y el estado.</li>
<li><strong>Facturas:</strong> una línea por cada línea de factura, indicando a qué albarán corresponde.</li>
<li><strong>Resumen:</strong> cuántas líneas cuadran, cuántas tienen diferencias, cuántas están sin facturar y el importe pendiente.</li>
<li><strong>Instrucciones:</strong> los pasos y los estados posibles.</li>
</ul>
<p>El estado de cada línea puede ser: cuadra, sin facturar, precio distinto, facturado de menos o facturado de más (o duplicado). Se colorea solo, para localizar las diferencias de un vistazo. Los errores que detecta son los que describimos en <a href="/blog/cruzar-albaranes-con-facturas/">cómo cruzar albaranes con facturas sin hacerlo a mano</a>.</p>
<h2>Cómo usarla</h2>
<ol>
<li>Descargad el archivo y borrad las filas de ejemplo (el proveedor «Ejemplo S.L.»), sin tocar las columnas en gris.</li>
<li>Cuando llegue un albarán, anotad cada línea en la hoja «Albaranes» con el precio pactado con ese proveedor.</li>
<li>Cuando llegue una factura, anotad cada línea en la hoja «Facturas», con el número del albarán al que corresponde y el concepto escrito igual que en el albarán.</li>
<li>Revisad la columna «Estado» y la hoja «Resumen». Reclamad al proveedor lo que no cuadre.</li>
<li>Al cerrar el mes, filtrad por «Sin facturar» para ver qué albaranes están pendientes.</li>
</ol>
<h2>Dónde se queda corta</h2>
<p>La plantilla compara bien, pero no lee: alguien tiene que teclear cada albarán y cada factura. Con pocos proveedores y poco volumen es razonable. Cuando se acumulan muchos documentos, en formatos distintos y con fotos desde la obra, el tecleo es lo primero que se deja de hacer, y con él, el control.</p>
<p>Ahí es donde compensa automatizar la lectura y el cruce. Lo explicamos en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>, y para elegir herramienta, en <a href="/blog/software-albaranes-constructoras/">software de albaranes para constructoras: qué mirar</a>.</p>
""",
    },
    {
        "slug": "comprobar-factura-proveedor-antes-de-pagar",
        "fecha": "2026-11-27",
        "title": "Qué comprobar en una factura de proveedor antes de pagar",
        "meta": "Lista de verificación para revisar facturas de proveedor antes de pagarlas: datos formales, albarán, precio pactado, cantidades, IVA, duplicados y vencimiento.",
        "h1": "Qué comprobar en una factura de proveedor antes de pagarla: lista de verificación",
        "resumen": "Diez comprobaciones, de los datos formales al cruce con el albarán, para no pagar de más. Y cuáles se pueden automatizar.",
        "relacion": {"servicios": ["automatizacion-facturas-albaranes"], "sectores": ["construccion-reformas", "distribucion-mayoristas"]},
        "cuerpo": """
<p>Pagar una factura sin revisarla es pagar lo que el proveedor diga. Revisarla a fondo lleva tiempo, así que casi siempre se hace por encima. Esta lista ayuda a ordenar la revisión: qué mirar, en qué orden y qué parte se puede automatizar.</p>
<h2>Comprobaciones formales</h2>
<ol>
<li><strong>Datos del emisor y del destinatario.</strong> Razón social y NIF correctos, y a nombre de vuestra empresa actual. Una factura con datos erróneos puede dar problemas después.</li>
<li><strong>Número y fecha.</strong> Que el número sea coherente con la serie del proveedor y que no lo hayáis recibido ya.</li>
<li><strong>Descripción de lo facturado.</strong> Conceptos claros, que permitan saber qué se compra y para qué.</li>
</ol>
<p>Los requisitos formales de una factura los regula el Reglamento de facturación (Real Decreto 1619/2012). Ante cualquier duda sobre si una factura es válida a efectos fiscales, lo mejor es consultarlo con vuestra gestoría.</p>
<h2>Comprobaciones contra lo recibido y lo pactado</h2>
<ol start="4">
<li><strong>Cantidades frente al albarán.</strong> Que no se facture más de lo entregado, ni un pedido completo cuando llegó una parte.</li>
<li><strong>Precios frente a lo pactado.</strong> Que se apliquen la tarifa y el descuento acordados, no el precio general.</li>
<li><strong>Descuentos.</strong> Que aparezcan los que corresponden por volumen o por pago anticipado.</li>
<li><strong>Portes y recargos.</strong> Que solo figuren los acordados.</li>
</ol>
<h2>Comprobaciones de cálculo y de control</h2>
<ol start="8">
<li><strong>Importes.</strong> Que las líneas sumen la base imponible, que el tipo de IVA sea el que toca y que la cuota y el total estén bien calculados.</li>
<li><strong>Duplicados.</strong> Que el mismo albarán no aparezca en otra factura y que no hayáis recibido la misma factura dos veces por correo.</li>
<li><strong>Vencimiento y forma de pago.</strong> Que coincidan con lo acordado con el proveedor.</li>
</ol>
<h2>Qué se puede automatizar</h2>
<p>Las comprobaciones 4 a 9 son mecánicas: comparar cantidades y precios con el albarán y con la tarifa, sumar líneas y detectar duplicados. Son justo las que más tiempo llevan y las que antes se dejan de hacer. Un sistema de lectura con IA extrae los datos de cada factura, los cruza con sus albaranes y solo os enseña las diferencias, con el documento original al lado.</p>
<p>Las primeras (datos formales y vencimiento) siguen requiriendo criterio, pero se revisan mucho más rápido cuando lo demás ya viene comprobado.</p>
<p>Si queréis empezar con una hoja de cálculo, tenéis la <a href="/blog/plantilla-excel-cruce-albaranes-facturas/">plantilla de Excel para cruzar albaranes con facturas</a>. Y para ver el método completo, <a href="/blog/cruzar-albaranes-con-facturas/">cómo cruzar albaranes con facturas sin hacerlo a mano</a>. Si lo queréis automatizado, está en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
""",
    },
]
