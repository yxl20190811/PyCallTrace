import http.server
import socketserver
import os

PORT = 8080
DIR = r"C:\hh\svn\PyCallTrace"

os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.html': 'text/html; charset=utf-8',
    '.log': 'text/plain; charset=utf-8',
    '.py': 'text/plain; charset=utf-8',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器已启动: http://localhost:{PORT}/log_analyzer.html")
    print(f"按 Ctrl+C 停止服务器")
    httpd.serve_forever()
