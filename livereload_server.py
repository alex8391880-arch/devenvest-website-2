from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = time.time()
    
    def on_modified(self, event):
        if event.src_path.endswith(('.html', '.css', '.js', '.jpg', '.png')):
            print(f"Изменен файл: {event.src_path}")
            self.last_modified = time.time()

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Сервер запущен на http://localhost:8000")
print("Автоматическое обновление при изменении файлов")

event_handler = ReloadHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()

try:
    server = HTTPServer(('', 8000), MyHTTPRequestHandler)
    server.serve_forever()
except KeyboardInterrupt:
    observer.stop()
    print("\nСервер остановлен")
observer.join()
