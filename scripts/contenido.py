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
        "title": "IA para empresas de construcción y reformas: albaranes, facturas y presupuestos",
        "meta": "Automatizamos el back office de constructoras y empresas de reformas: albaranes de materiales por obra, cruce con facturas y presupuestos desde mediciones.",
        "h1": "IA para empresas de construcción y reformas",
        "lead": "Albaranes de almacén que se pierden entre obras, facturas de proveedor que nadie cruza y presupuestos que salen tarde. Automatizamos esa parte para que la oficina vaya al ritmo de las obras.",
        "card": "Albaranes por obra, cruce con facturas y presupuestos desde mediciones.",
        "faq": [
            ("¿Se pueden imputar los albaranes a cada obra?", "Sí. Al leer el albarán se identifica la obra (por referencia, dirección o pedido) y el coste queda asignado, así podéis ver el gasto real de cada obra sin esperar al cierre."),
            ("¿Sirve para presupuestos de reforma muy distintos entre sí?", "Sí. Se parte de las notas de la visita o de una medición y se generan las partidas con vuestras tarifas. Siempre lo revisa alguien antes de enviarlo."),
        ],
        "cuerpo": """
<section><div class="inner">
<p class="eyebrow">Lo que pasa hoy</p>
<h2>Muchas obras, muchos proveedores, mucho papel</h2>
<p>En una empresa de construcción o reformas llegan cada semana decenas de albaranes de almacenes de materiales, alquiler de maquinaria y subcontratas. A menudo viajan en la furgoneta, se fotografían con el móvil o se quedan en la obra.</p>
<p>A fin de mes llegan las facturas y toca comprobar, una a una, que lo facturado coincide con lo entregado y con el precio pactado. Como es tan pesado, se hace por encima, y así se pagan materiales que no llegaron o precios que no eran los acordados. Y saber cuánto lleva gastado cada obra se convierte en un trabajo de días.</p>
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
""",
    },
    {
        "slug": "transporte-gruas",
        "nav": "Transporte y grúas",
        "title": "IA para empresas de transporte y grúas: partes de servicio y facturación automática",
        "meta": "Automatizamos la facturación de empresas de transporte y grúas de asistencia: partes de servicio, kilómetros, esperas y peajes convertidos en facturas sin teclear.",
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
        "title": "IA para talleres y empresas de mantenimiento: órdenes de trabajo, recambios y facturas",
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
        "title": "IA para distribuidores y mayoristas: pedidos por correo al ERP y facturas de proveedor",
        "meta": "Automatizamos el back office de distribuidores y mayoristas: pedidos de clientes que llegan por correo pasan solos al ERP y las facturas de proveedor se cruzan con lo recibido.",
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
        "title": "Cómo comprobar albaranes contra facturas de proveedor sin hacerlo a mano",
        "meta": "Guía práctica para cruzar albaranes con facturas de proveedor: errores habituales, cómo hacerlo bien en Excel y cuándo compensa automatizarlo con IA.",
        "h1": "Cómo comprobar albaranes contra facturas de proveedor sin hacerlo a mano",
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
<p>El problema es el tiempo: con muchos proveedores, registrar y comparar se convierte en horas cada semana, y es justo lo primero que se deja de hacer cuando hay prisa.</p>
<h2>Cuándo compensa automatizarlo</h2>
<p>Compensa cuando recibís muchos albaranes al mes, de varios proveedores y en formatos distintos (PDF, papel, foto), o cuando necesitáis saber el coste real de cada obra o trabajo sin esperar al cierre.</p>
<p>Con IA el proceso es el mismo de la lista anterior, pero sin teclear: los albaranes y las facturas se leen al llegar, sea cual sea el formato; se cruzan entre sí y con los precios pactados, y solo se os enseñan las diferencias, con el documento original al lado para decidir. Lo que cuadra pasa directamente a contabilidad.</p>
<p>Si queréis ver cómo funcionaría con vuestros documentos, lo explicamos en <a href="/servicios/automatizacion-facturas-albaranes/">automatización de facturas y albaranes</a>.</p>
""",
    },
    {
        "slug": "ocr-o-ia-para-leer-facturas",
        "fecha": "2026-11-23",
        "title": "OCR o IA para leer facturas: qué diferencia hay y cuál necesita tu empresa",
        "meta": "Diferencias entre el OCR tradicional y la lectura de facturas con inteligencia artificial: plantillas, formatos distintos, errores y cuándo conviene cada uno.",
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
<p>Y si el objetivo no es solo leer, sino cruzar facturas con albaranes y pedidos, la IA es casi imprescindible. Lo contamos en <a href="/blog/cruzar-albaranes-con-facturas/">cómo comprobar albaranes contra facturas</a>.</p>
""",
    },
    {
        "slug": "tareas-administrativas-automatizar-pyme",
        "fecha": "2026-11-23",
        "title": "7 tareas administrativas que una pyme puede automatizar con IA",
        "meta": "Las tareas de back office que más tiempo quitan en una pyme y que hoy se pueden automatizar con IA: facturas, albaranes, presupuestos, pedidos, correos e informes.",
        "h1": "7 tareas administrativas que una pyme puede automatizar con IA",
        "resumen": "De la lectura de facturas a los informes semanales: dónde está el tiempo de la oficina y qué parte se puede automatizar ya.",
        "cuerpo": """
<p>No hace falta un gran proyecto para notar la IA en la oficina. Las mejores primeras automatizaciones son tareas pequeñas, repetitivas y que hoy dependen de que alguien teclee datos. Estas son siete de las más habituales en pymes.</p>
<h2>1. Registrar facturas de proveedor</h2>
<p>Leer cada factura y pasar proveedor, fecha, importes e IVA al programa de contabilidad. Es la tarea más fácil de automatizar y la que antes se nota. <a href="/blog/ocr-o-ia-para-leer-facturas/">Aquí explicamos la diferencia entre OCR e IA</a> para hacerlo.</p>
<h2>2. Cruzar albaranes con facturas</h2>
<p>Comprobar que lo facturado coincide con lo entregado y con el precio pactado. Automatizado, solo revisáis las diferencias. <a href="/blog/cruzar-albaranes-con-facturas/">Guía completa</a>.</p>
<h2>3. Preparar presupuestos</h2>
<p>Convertir las notas de una visita, una medición o la petición de un cliente en un presupuesto con vuestras partidas y tarifas. Un borrador en minutos que alguien revisa y envía.</p>
<h2>4. Facturar trabajos y servicios</h2>
<p>Pasar partes de trabajo, horas, kilómetros o materiales a factura sin volver a teclearlos, y detectar lo que se ha hecho y no se ha facturado.</p>
<h2>5. Dar de alta pedidos que llegan por correo</h2>
<p>Leer pedidos en PDF, Excel o en el propio correo y darlos de alta en el ERP sin intervención, con aviso cuando algo no está claro.</p>
<h2>6. Clasificar correos y documentos</h2>
<p>Enviar cada documento a su carpeta, su responsable o su flujo de trabajo: facturas a contabilidad, pedidos a almacén, consultas a quien corresponda.</p>
<h2>7. Informes semanales</h2>
<p>Compras del mes, coste por obra, trabajos pendientes de facturar o presupuestos sin respuesta, generados solos cada lunes en lugar de montarlos a mano.</p>
<h2>Por dónde empezar</h2>
<p>Elegid la tarea que más horas os quita y que siga siempre los mismos pasos. Automatizad solo esa, medid el resultado y después pasad a la siguiente. En el <a href="/automatizacion-back-office/">back office con IA</a> explicamos cómo lo planteamos, y el diagnóstico inicial es gratuito.</p>
""",
    },
]
