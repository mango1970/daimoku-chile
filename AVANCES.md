# Avances — Daimoku Chile

Actualizado: 2026-11-15

## Estado actual

- Repositorio en `main`, sin remoto configurado. Último commit local: `3051e94` («Corrige tildes en la exportación CSV»).
- Antes de esta sesión el árbol estaba limpio. Los cambios de hoy quedan sin commit hasta que se solicite.
- Producto: landing en `/`, PWA en `/app/`, mapa de 1.000 cuadros, exportaciones CSV/PDF/JSON, service worker, modo offline e importación de respaldo.
- El sitio es estático: se publica el contenido de `dist/` tal cual, sin compilación.
- Fase 0 ejecutada en navegador local. No sustituye las pruebas en teléfonos reales.

## Decisiones tomadas

- Alojamiento: Vercel, manteniendo landing y PWA en el mismo origen. La landing enlaza a `/app/` y desde ahí se instala la PWA.
- Datos: importación de respaldo JSON desde Bitácora, con validación y opciones de fusión o reemplazo.
- iOS: no es prioritario, pero se añadieron metas de instalación, icono de 180 px y precache.
- Analítica: no se incorpora; se mantiene la privacidad y el procesamiento local.
- Créditos: Mauricio Núñez y `contacto@mauricionunez.cl` visibles en la landing y en la app.

## Hecho en esta sesión

- Revisión de git: rama `main`, árbol limpio al inicio, sin remoto. El último commit local es `3051e94`.
- Importación JSON en Bitácora:
  - Botón «Importar respaldo» y lector de archivos `.json`.
  - Validación de sesiones, fechas, duraciones, modos, intenciones y recorridos archivados.
  - Límites de tamaño y cantidad; los registros inválidos se omiten y se informan.
  - «Fusionar» conserva lo actual y añade registros con id nuevo; es idempotente al repetir el mismo archivo.
  - «Reemplazar» pide confirmación y descarga antes un respaldo de seguridad de los datos actuales.
  - El JSON exportado incluye `schemaVersion: 1`; se aceptan respaldos anteriores.
  - Se endurecieron los ids importados y el escape de comillas en atributos.
- iOS:
  - Metas `apple-mobile-web-app-capable`, `apple-mobile-web-app-title`, `apple-mobile-web-app-status-bar-style` y `mobile-web-app-capable`.
  - Icono `dist/assets/icon-180.png` y enlaces `apple-touch-icon` de 180 y 192.
  - Icono de 180 agregado al precache del service worker.
- Créditos de autoría en el pie de la landing y de la app.
- Vercel:
  - `vercel.json` con `outputDirectory: "dist"` y `trailingSlash`.
  - Caché: HTML y JS/CSS con revalidación, `sw.js` sin caché, manifest con su MIME, fotos con caché larga y assets/descargas con caché moderada.
  - Seguridad: `nosniff`, `Referrer-Policy`, `Permissions-Policy` y `X-Frame-Options`.
- Documentación actualizada: README, LEEME, DETALLES-TECNICOS y este archivo.
- Versiones actualizadas: `app.js?v=12`, `exports.js?v=12`, caché `daimoku-chile-v13-import`.

## Verificación Fase 0

Ejecutada contra `http://127.0.0.1:8765` con Chromium headless:

- Sintaxis: `node --check` correcto en `app.js`, `exports.js`, `map-controls.js`, `landing.js`, `sw.js`, `chile-map.js` y `photos.js`.
- Landing: carga correcta, 0 errores de consola, 0 solicitudes fallidas, 7 enlaces a `/app/`, creditos y metadatos iOS presentes.
- App: carga correcta, 0 errores de consola, 0 solicitudes fallidas, mapa con 1.000 celdas.
- Importación:
  - Fusión de prueba: 2 sesiones, 1.500 daimoku, 1 intención y 1 recorrido archivado.
  - Segunda importación del mismo archivo: sin duplicados (2 sesiones, 1.500 daimoku).
  - Reemplazo de prueba: 1 sesión y 250 daimoku; se solicitó la descarga de la copia de seguridad previa.
  - Archivo no reconocido: rechazado con el aviso «El archivo no parece un respaldo de Daimoku Chile».
- Offline: tras la primera carga, la app se recargó sin conexión con el mapa de 1.000 celdas y el service worker controlando la página.
- Service worker: registro activo en `/sw.js` y caché `daimoku-chile-v13-import`.
- `vercel.json`: JSON válido.
- Pendiente: probar en Android e iPhone reales, con instalación, micrófono, PDF, descargas y actualización del service worker.

## Pendientes conocidos

- Desplegar en Vercel y probar la URL de producción.
- Probar instalación, micrófono, PDF y descargas en Android e iPhone reales.
- Validar el conteo por voz con recitación real.
- Actualizar la URL canónica, `og:image`, README, LEEME y guía PDF cuando exista el dominio definitivo.
- Opcional: autoalojar las fuentes de Google, añadir `robots.txt`, `sitemap.xml`, favicon `.ico` y CSP.
- Probar la importación con un respaldo real generado por la versión publicada.

## Publicación en Vercel

1. Importar el repositorio en Vercel.
2. Framework Preset: Other. Build Command: vacío. Output Directory: `dist`.
3. El archivo `vercel.json` de la raíz fija `dist` como salida y los headers de caché y seguridad.
4. Tras cada cambio, actualizar los parámetros `?v=` afectados y el nombre de caché de `dist/sw.js`.

## Versiones y caché

- `landing.css` / `landing.js` / `chile-map.js` / `photos.js`: `v=8`.
- `style.css`: `v=11`.
- `map-controls.js`: `v=10`.
- `exports.js` / `app.js`: `v=12`.
- Caché del service worker: `daimoku-chile-v13-import`.

Estas versiones se actualizan al cierre de cada sesión.
