import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VAULT_PATH = "."  # raiz do vault
RAW_PATH = "raw"
SCHEMA_FILE = "schema.md"
MODEL = "deepseek/deepseek-chat"

PROMPT = """Leia os arquivos indicados e o schema.md.
Crie as páginas wiki apropriadas nas pastas corretas conforme o schema.md:
- Pessoas em wiki/people/
- Obras em wiki/works/
- Conceitos abstratos em wiki/concepts/
- Movimentos e épocas em wiki/periods/
- Resumo da fonte em wiki/sources/
Adicione backlinks entre todas as páginas relacionadas."""

class RawFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if not event.src_path.endswith(".md"):
            return

        filepath = event.src_path.replace("\\", "/")
        print(f"\n📄 Novo arquivo detectado: {filepath}")
        print("⏳ Aguardando 3 segundos para garantir que o arquivo foi salvo...")
        time.sleep(3)

        print("🤖 Iniciando Aider...")
        command = [
            "aider",
            "--model", MODEL,
            "--no-git",
            "--yes",
            "--message", f"/add {filepath}\n/add {SCHEMA_FILE}\n{PROMPT}",
        ]

        subprocess.run(command, cwd=VAULT_PATH)
        print(f"✅ Processamento concluído para {filepath}")

if __name__ == "__main__":
    print("👀 Monitorando a pasta raw/ — pode começar a clicar!")
    print("Pressione Ctrl+C para parar.\n")

    observer = Observer()
    observer.schedule(RawFolderHandler(), path=RAW_PATH, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()