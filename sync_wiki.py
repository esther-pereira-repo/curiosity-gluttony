
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

SCHEMA_PATH = "schema.md"
RAW_DIR = "raw"
WIKI_DIR = "wiki"

class RawFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if not event.src_path.endswith(".md"):
            return

        raw_file = event.src_path
        filename = os.path.basename(raw_file)
        wiki_file = os.path.join(WIKI_DIR, filename)

        print(f"Arquivo atualizado: {filename}. Sincronizando com a wiki...")

        prompt = f"Leia o arquivo {raw_file} e o schema em {SCHEMA_PATH}. Crie ou atualize o arquivo {wiki_file} seguindo as regras do schema."

        subprocess.run(["aider", "--message", prompt, raw_file, SCHEMA_PATH, wiki_file])

if __name__ == "__main__":
    event_handler = RawFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=RAW_DIR, recursive=False)
    observer.start()
    print("Monitorando a pasta raw... (Ctrl+C para parar)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
