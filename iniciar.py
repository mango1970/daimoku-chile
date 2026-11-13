from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Timer
import webbrowser

directory = Path(__file__).resolve().parent / "dist"
handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
server = None
for port in range(8765, 8776):
    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), handler)
        break
    except OSError:
        continue
if server is None:
    raise SystemExit("No se encontro un puerto disponible entre 8765 y 8775.")
url = f"http://127.0.0.1:{server.server_port}/"
print("DAIMOKU CHILE")
print(f"Abre {url} en tu navegador.")
print("Mantén esta ventana abierta. Para cerrar: Ctrl+C.")
Timer(0.7, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
