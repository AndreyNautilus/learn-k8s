import argparse
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import logging

logging.getLogger().setLevel(logging.INFO)


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        page_line = [
            self.server.page_message,
            self.path,
            datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        ]
        self.wfile.write(" - ".join(page_line).encode("utf-8"))
        
    def do_POST(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, nargs='?', default=8000)
    parser.add_argument("--message", type=str, default="Hello, world!")
    args = parser.parse_args()

    if not args.message:
        raise RuntimeError("Message cannot be empty")

    logging.info(f"Message: {args.message}")

    httpd = ThreadingHTTPServer(('', args.port), SimpleHandler)
    httpd.page_message = args.message
    
    logging.info(f"Start serving on port {args.port} ...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
