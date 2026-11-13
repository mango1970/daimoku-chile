# Daimoku Chile

PWA independiente que acompaña una práctica personal de recitación y la convierte en un recorrido de norte a sur por Chile. Cada 1.000 daimoku ilumina un cuadro del mapa; la meta es un millón (1.000 cuadros).

Sitio estático de HTML, CSS y JavaScript: sin compilación, sin backend y sin cuentas. Los datos quedan en el navegador del dispositivo.

Versión alojada: https://daimoku-chile-viaje.mauro1970.chatgpt.site

## Uso local

Requiere Python 3 (solo para servir archivos; no hay dependencias).

- Windows: doble clic en `INICIAR.cmd`.
- macOS y Linux: `python3 iniciar.py`.
- Manual: `python -m http.server 8765 --bind 127.0.0.1 --directory dist` y abrir http://127.0.0.1:8765/

La portada está en `/` y la práctica en `/app/`. No abras `dist/index.html` como archivo: el micrófono y la instalación de la PWA necesitan localhost o HTTPS.

## Estructura

```
.
├── dist/                  # sitio completo; se publica tal cual
│   ├── index.html         # portada
│   ├── landing.css/js
│   ├── app/index.html     # aplicación
│   ├── app.js             # sesión, conteo, estaciones y temas
│   ├── map-controls.js    # cámara del mapa
│   ├── exports.js         # CSV, PDF, reconocimiento y respaldo JSON
│   ├── sw.js              # service worker
│   ├── assets/            # mapa, fotografías, iconos y créditos
│   ├── downloads/         # guía rápida en PDF
│   └── vendor/            # jsPDF 4.2.1 (MIT)
├── iniciar.py             # servidor local
├── INICIAR.cmd            # lanzador para Windows
├── LEEME.txt              # instrucciones para quien usa la app
├── DETALLES-TECNICOS.md   # decisiones de implementación
├── .gitattributes
└── .gitignore
```

## Funciones

- Tres modos de conteo: voz (estima por actividad sonora), cronómetro y manual.
- Calibración del ritmo personal y umbral de sensibilidad.
- Mapa de 1.000 cuadros sobre el contorno de Chile, con zoom, arrastre y seguimiento del avance.
- Siete estaciones culturales con fotografías y reflexiones originales.
- Exportación CSV, bitácora en PDF, reconocimiento con mapa y respaldo JSON.
- PWA instalable y uso sin conexión tras la primera carga.
- Temas claro, semioscuro y oscuro, con preferencia persistente.
- Continuidad de sesión: si sales de la app o se apaga la pantalla, el tiempo ausente se suma al volver y puede deshacerse.

## Datos y privacidad

- El audio se procesa en el dispositivo: no se graba ni se transmite.
- Sesiones e intenciones viven en `localStorage` (`daimoku-chile-v1`). Sin cuentas ni sincronización entre dispositivos.
- El respaldo JSON se descarga desde Bitácora. La importación automática está pendiente.
- Borrar los datos del sitio elimina el avance; borrar solo la caché no.

## Publicación

Sube el contenido de `dist/` a la raíz de un alojamiento HTTPS. Tras cambiar archivos, actualiza el parámetro `?v=` en `dist/app/index.html` y el nombre de caché en `dist/sw.js`.

## Desarrollo

No hay paso de compilación: `dist/` es a la vez código fuente y artefacto publicable. Si en el futuro se incorpora un compilador, el código debería moverse a `src/` y `dist/` pasar a ser salida generada. Al modificar archivos, recuerda actualizar el `?v=` correspondiente y el nombre de caché del service worker.

## Licencia

MIT — ver `LICENSE`. Cubre el código del proyecto. Las fotografías, el contorno de Natural Earth y jsPDF conservan las licencias indicadas en «Créditos y aviso».

## Créditos y aviso

- Contorno de Chile: Natural Earth (dominio público).
- Fotografías: Wikimedia Commons; autores y licencias en `dist/assets/photo-credits.json`.
- jsPDF 4.2.1 (MIT) en `dist/vendor/`.
- Proyecto independiente, sin afiliación ni aval de SGI. El conteo por voz es estimado y no reconoce palabras.
