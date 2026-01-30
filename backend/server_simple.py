import http.server
import socketserver
import json
import sys
import os

# Add tools to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.converter import JavaToPlaywrightConverter

PORT = 8000
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)

    def do_POST(self):
        if self.path == "/api/convert":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                source_code = data.get('source_code', '')
                
                converter = JavaToPlaywrightConverter(source_code)
                converted_code = converter.convert()
                
                response = {
                    "status": "success",
                    "conversion_result": {
                        "converted_code": converted_code,
                        "logs": ["Conversion successful"]
                    }
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)

if __name__ == "__main__":
    print(f"Starting legacy server at http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
