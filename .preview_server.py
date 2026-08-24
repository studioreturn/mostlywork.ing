import http.server
import pathlib

ROOT = pathlib.Path(__file__).parent

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            data = (ROOT / "index.md").read_bytes()
            content_type = "text/markdown; charset=utf-8"
        elif self.path == "/favicon.ico":
            data = (ROOT / "favicon.ico").read_bytes()
            content_type = "image/vnd.microsoft.icon"
        else:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = http.server.HTTPServer(("127.0.0.1", 4175), Handler)
    print("Serving at http://127.0.0.1:4175")
    server.serve_forever()
