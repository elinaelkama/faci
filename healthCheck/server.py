import threading
import http.server
from decouple import config
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')


def __startServer(stopEvent):
    PORT = config('PORT', cast=int)
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Health server running on port {PORT}...")
        httpd.timeout = 1
        while not stopEvent.is_set():
            httpd.handle_request()


stopEvent = threading.Event()


def start():
    serverThread = threading.Thread(target=__startServer, args=(stopEvent,))
    serverThread.start()


def stop():
    stopEvent.set()
