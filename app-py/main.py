import argparse
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"do_GET: {self.path}")
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"{self.server.page_message} {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}".encode("utf-8"))
        else:
            self.send_error(404)
        
    def do_POST(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, nargs='?', default=8000)
    parser.add_argument("--message", type=str, default="Hello, world!")
    args = parser.parse_args()

    if not args.message:
        raise RuntimeError("Message cannot be empty")

    print(f"Message: {args.message}")

    httpd = ThreadingHTTPServer(('', args.port), SimpleHandler)
    httpd.page_message = args.message
    
    print(f"Start serving on port {args.port} ...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
