# Daimoku Chile

PWA independiente para acompañar una práctica personal y completar un mapa geográfico de Chile hacia una meta de un millón de daimoku.

- 1.000 cuadros, 1.000 daimoku por cuadro, de norte a sur.
- Voz: estima tiempo con actividad sonora y aplica un ritmo personal calibrado. No reconoce frases y puede incluir ruido o conversaciones.
- Cronómetro: estima por tiempo con el mismo ritmo personal.
- Manual: permite registrar un conteo conocido.
- Revisión antes de guardar, bitácora exportable, intenciones privadas y siete estaciones culturales con reflexiones originales.
- Datos en localStorage; sin cuentas ni sincronización entre dispositivos. No graba ni transmite audio.
- Manifest, iconos PNG y service worker para instalación y uso sin conexión después de la primera carga.
- Al ocultarse la app se libera el micrófono; al volver, el tiempo ausente se suma con el ritmo personal (exacto en cronómetro, estimado en voz) y el aviso permite deshacerlo. La pantalla encendida es opcional (WakeLock): con ella, el modo voz sigue midiendo sin interrupciones. El navegador requiere HTTPS y permiso para el micrófono.

Abrir la versión de vista previa: https://daimoku-chile-viaje.mauro1970.chatgpt.site

Para servir localmente: ejecutar `python -m http.server 8765 --bind 127.0.0.1 --directory dist` desde esta carpeta y abrir http://127.0.0.1:8765/. No abrir index.html directamente como archivo para probar el micrófono o la PWA.

No se ha verificado una tasa oficial universal de Soka Gakkai. Esta aplicación no está afiliada ni avalada por SGI. DAIMOKU PRO se consultó como referencia de cronómetro, metas y registros; su ficha de Google Play identifica a Hiromi Fujita como desarrollador, sin confirmar aval institucional.

Fuentes:
https://www.sokaglobal.org/resources/videos/how-to-chant.html
https://www.sokaglobal.org/resources/sg-charter.html
https://play.google.com/store/apps/details?id=com.daimokupro.DAIMOKUPRO

Verificación: sintaxis JS, pruebas de 1.000 celdas, avance al millón, límites visuales, persistencia y escape de intenciones; prueba en navegador de registro manual, cronómetro calibrado, revisión de sesión y pantalla móvil. Pendiente validación acústica con recitación real y prueba de instalación en teléfonos reales.

Actualización: contorno de Natural Earth (dominio público), islas ampliadas, mapa visible al inicio en móvil y en Mi viaje; modos Claro, Semioscuro y Oscuro, con preferencia persistente.

Cámara del mapa: la app abre con el país completo a la vista. "Seguir avance" lleva al frente del recorrido —el último cuadro encendido, o el primero si aún no hay ninguno— y el zoom sigue apuntando a esa zona mientras no se arrastre el mapa. Al completar un cuadro, la vista salta sola al frente. Estados de cámara: inicio (vista completa), seguimiento, mapa completo y control manual.

Continuidad de sesión: al ocultarse la página no se pausa la sesión; se guarda la marca `hiddenAt`, se libera el micrófono y se escribe el borrador. Al volver se suma el hueco real (tope de 6 h) a `elapsed` y `activeSeconds`, se recalcula el conteo y se ofrece "Deshacer". Si el AudioContext se suspende o el micrófono se desconecta, el botón principal pasa a "Reactivar micrófono" y, mientras tanto, el tiempo se acredita con el ritmo personal. El WakeLock es opcional (interruptor en el modal de ritmo, por defecto activo); se vuelve a solicitar al volver a la página y se escucha su evento `release`. `updateSession()` y `refreshMilestone()` solo escriben en el DOM cuando el valor cambia, y el borrador se guarda cada 5 s reales.

Fotografías regionales: siete imágenes reales de Wikimedia Commons, con autores y licencias en dist/assets/photo-credits.json y dentro de la aplicación. Formato WebP, encuadre responsivo y precarga sin conexión mediante service worker.

Importación de respaldo: Bitácora permite leer un JSON exportado por la app. Se validan sesiones, fechas, duraciones, modos, intenciones y recorridos archivados; los registros inválidos se omiten y se informa cuántos. «Fusionar» conserva los datos actuales y añade los registros cuyo id no exista; «Reemplazar» sustituye todo y descarga antes un respaldo de seguridad. El archivo incluye `schemaVersion: 1` y se aceptan también respaldos anteriores.

iOS: la landing y la app incluyen metas de aplicación web, icono de 180 px y el icono de 192 px. La instalación sigue siendo manual desde Safari («Compartir > Añadir a pantalla de inicio»); queda pendiente probar micrófono, descargas y uso offline en un iPhone real.

Publicación: `vercel.json` fija `dist` como salida, `trailingSlash`, cabeceras de caché para HTML, service worker, manifest y assets, y cabeceras de seguridad (`nosniff`, `Referrer-Policy`, `Permissions-Policy` y `X-Frame-Options`). La CSP queda pendiente porque el HTML usa scripts y estilos inline.

Actualización de lanzamiento: landing en /; práctica en /app/; compatibilidad con enlaces anteriores y PWA instalada; PDF de guía descargable. Zoom, arrastre y seguimiento, cuadros completos superpuestos al contorno y tricolor. CSV, PDF de bitácora, reconocimiento con mapa y sesiones. Reinicio al millón condicionado a confirmación de reconocimiento guardado, con archivo atómico del recorrido anterior. Los datos siguen en la misma clave y origen. jsPDF 4.2.1 se distribuye localmente con su licencia MIT.
