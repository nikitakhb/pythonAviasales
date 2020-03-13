from http.server import HTTPServer

from handlers import ServerHTTPRequestHandler


def run(server_class=HTTPServer,
        handler_class=ServerHTTPRequestHandler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        print('Start web server')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(' shutting down the web server')
        httpd.socket.close()
