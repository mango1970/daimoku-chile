# Avances — Daimoku Chile

Actualizado: 2026-11-15

## Estado actual

- Repositorio en `main`, sin remoto configurado. Último commit local: `0a1b2b2` («Añade el icono definitivo a la landing y la app»).
- Los cambios de reposo de esta sesión quedan sin commit hasta que se soliciten.
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

- Revisión de git: rama `main`, sin remoto. El último commit local es `0a1b2b2`.
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
- Icono corregido:
  - El SVG corregido, con la hoja central, se conserva en `design/icon-source.svg`; la versión con margen para maskable está en `design/icon-maskable.svg`.
  - `dist/assets/icon.svg` quedó cuadrado, con fondo blanco y margen; los PNG se regeneraron desde esa versión.
  - El icono se muestra en el encabezado de la landing, en la marca de la app y en el pie, con un aumento del 50 % respecto del tamaño anterior.
  - Se separaron iconos `any` (192/512) y `maskable` (192/512) en el manifest.
  - PNG de 180, 192, 512 y maskable de 192/512; URLs con `?v=4` y precache actualizado.
- Mapa en móvil:
  - En vista completa el SVG permite desplazar la página con el dedo.
  - Con zoom se activa `pannable` y el arrastre mueve el mapa.
  - «Chile completo» devuelve el desplazamiento normal.
- Reposo y continuidad:
  - Se mide el salto con `Date.now()` aunque la página siga visible.
  - Huecos de 8 a 60 s se suman automáticamente con Deshacer.
  - Huecos de 60 s o más muestran un aviso para confirmar si la práctica continuó; el tope es de 6 h.
  - Se atienden `visibilitychange`, `pagehide`, `pageshow`, `freeze`, `resume` y `focus`; el cierre del aviso no deja bloqueado el siguiente.
- Créditos de autoría en el pie de la landing y de la app.
- Vercel:
  - `vercel.json` con `outputDirectory: "dist"` y `trailingSlash`.
  - Caché: HTML y JS/CSS con revalidación, `sw.js` sin caché, manifest con su MIME, fotos con caché larga y assets/descargas con caché moderada.
  - Seguridad: `nosniff`, `Referrer-Policy`, `Permissions-Policy` y `X-Frame-Options`.
- Documentación actualizada: README, LEEME, DETALLES-TECNICOS y este archivo.
- Versiones actualizadas: `app.js?v=13`, `exports.js?v=12`, `landing.css?v=10`, `style.css?v=14`, `map-controls.js?v=11`, caché `daimoku-chile-v19-map-scroll`.

## Verificación Fase 0

Ejecutada contra `http://127.0.0.1:8765` con Chromium headless:

- Sintaxis: `node --check` correcto en `app.js`, `exports.js`, `map-controls.js`, `landing.js`, `sw.js`, `chile-map.js` y `photos.js`.
- Landing: carga correcta, 0 errores de consola, 0 solicitudes fallidas, 7 enlaces a `/app/`, créditos y metadatos iOS presentes.
- App: carga correcta, 0 errores de consola, 0 solicitudes fallidas, mapa con 1.000 celdas.
- Importación:
  - Fusión de prueba: 2 sesiones, 1.500 daimoku, 1 intención y 1 recorrido archivado.
  - Segunda importación del mismo archivo: sin duplicados (2 sesiones, 1.500 daimoku).
  - Reemplazo de prueba: 1 sesión y 250 daimoku; se solicitó la descarga de la copia de seguridad previa.
  - Archivo no reconocido: rechazado con el aviso «El archivo no parece un respaldo de Daimoku Chile».
- Offline: tras la primera carga, la app se recargó sin conexión con el mapa de 1.000 celdas y el service worker controlando la página.
- Mapa táctil simulado:
  - Vista completa: `touch-action:pan-y`; el deslizamiento sobre el mapa desplazó la página 471 px.
  - Zoom: `touch-action:none` y `pannable`; el arrastre cambió el `viewBox` y no desplazó la página.
  - «Chile completo»: volvió a `pan-y` y el siguiente deslizamiento desplazó 349 px.
- Reposo simulado:
  - Hueco visible de 30 s: suma automática de 50 daimoku con Deshacer.
  - Hueco visible de 2 min: aviso con 200 daimoku; al confirmar suma 201 (incluye el segundo en curso).
  - Al rechazar el aviso: no suma.
  - Hueco oculto de 15 s: suma automática de 25 daimoku con Deshacer.
  - Cierre del aviso de reposo sin decidir: un nuevo reposo vuelve a preguntar.
- Iconos: manifest con iconos `any` y `maskable`, todos con respuesta 200; favicon SVG cuadrado con respuesta 200; 180/192/512 y maskables con dimensiones correctas; logo visible en landing y app con la hoja central.
- Service worker: registro activo en `/sw.js` y caché `daimoku-chile-v19-map-scroll`.
- `vercel.json`: JSON válido.
- Pendiente: probar en Android e iPhone reales, con instalación, micrófono, PDF, descargas y actualización del service worker.

## Pendientes conocidos

- Desplegar en Vercel y probar la URL de producción.
- Probar instalación, micrófono, PDF y descargas en Android e iPhone reales.
- Probar reposo real del PC, bloqueo de pantalla y scroll táctil sobre el mapa en un teléfono real.
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

- `landing.css`: `v=10`; `landing.js` / `chile-map.js` / `photos.js`: `v=8`.
- `style.css`: `v=14`.
- `map-controls.js`: `v=11`.
- `exports.js`: `v=12`; `app.js`: `v=13`.
- Iconos y manifest: `?v=4`.
- Caché del service worker: `daimoku-chile-v19-map-scroll`.

Estas versiones se actualizan al cierre de cada sesión.
