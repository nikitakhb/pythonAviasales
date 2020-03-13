import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

from store import SingletonStore


class ServerHTTPRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.store = SingletonStore()
        self.route_map = {
            "GET": {
                '/get': self.get_word
            },
            "POST": {
                '/load': self.load_list,
            },
        }
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        self.route_map['GET'].get(path, self.default)()
        return

    def do_POST(self):
        path = urlparse(self.path).path
        self.route_map['POST'].get(path, self.default)()

    def response(self, status: int = 200, data: str = ''):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data.encode())

    def load_list(self):
        post_body = self.rfile.read(int(self.headers['Content-Length']))
        test_data = json.loads(post_body)
        if isinstance(test_data, list):
            self.store.set_list(test_data)
            self.response()
        else:
            self.response(400, 'It is Not list words! Bad Request!')

    def get_word(self):
        word = parse_qs(urlparse(self.path).query).get('word', None)
        if word:
            data = self.store.get_anagrams(word[0])
            self.response(data=json.dumps(data))
        else:
            self.response(400, 'Bad Request')

    def default(self):
        self.response(404, '404 Page Not Found')


