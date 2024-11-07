from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World! This is a simple HTTP server.")

if __name__ == "__main__":
    server_address = ("", 80)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 80...")
    httpd.serve_forever()

