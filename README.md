# suxtrai.es

Landing page oficial de **SuxtrAI** — soluciones de IA a medida (RAG, automatización, formación). Bilbao.

Publicada con GitHub Pages en https://suxtrai.es

## Estructura
- `index.html` — la landing (exportada de Claude Design, con SEO añadido)
- `support.js` — runtime que renderiza la página
- `vendor/` — React, ReactDOM y Babel servidos desde el propio repo
- `assets/` — imágenes, logo, favicon e imagen para redes (og)
- `robots.txt`, `sitemap.xml` — indexación en Google

## Cómo contribuir
1. Crea una rama: `git checkout -b mi-cambio`
2. Haz tus cambios y pruébalos en local: `python3 -m http.server 8000` → http://localhost:8000
3. Abre un Pull Request y pide revisión a otro socio.

- `manifest.webmanifest`, `404.html`, `favicon.ico`: icono de pestaña/instalación y página de error con el isotipo.
- `assets/isotipo.svg`, `favicon.svg`, `icon-*.png`, `apple-touch-icon.png`, `og-suxtrai.jpg`: isotipo en vectorial y derivados.
