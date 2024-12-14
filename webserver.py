from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MainHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        public_dir = os.path.join(os.getcwd(), 'public')
        
        if self.path == '/':
            self.path = '/index.html'
        
        self.directory = public_dir
        return super().do_GET()

class WebServer():
    def run(PORT=3000):
        server_address = ('', PORT)
        httpd = HTTPServer(server_address, MainHandler)
        print(f"Servidor está ouvindo http:localhost:{PORT}")
        
        httpd.serve_forever()

if __name__ == "__main__":
    WebServer.run()
