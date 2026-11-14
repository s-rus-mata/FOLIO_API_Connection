
from pathlib import Path
import shutil
import argparse

# Ruta del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Template
MAIN_TEMPLATE = PROJECT_ROOT / "scripts" / "templates" / "main.py"

# Carpeta desde la que se ejecuta el script
TARGET_DIR = Path.cwd()


def create_main(filename):
    # Asegurar que el archivo tenga extensión .py
    if not filename.endswith(".py"):
        filename += ".py"

    target_main = TARGET_DIR / filename

    if not MAIN_TEMPLATE.exists():
        print(f"❌ No se encuentra el template: {MAIN_TEMPLATE}")
        return

    if target_main.exists():
        print(f"⚠️ Ya existe {filename} en: {TARGET_DIR}")
        return

    shutil.copy2(MAIN_TEMPLATE, target_main)
    print(f"✅ {filename} creado en: {target_main}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crea un archivo Python a partir del template main.py"
    )
    parser.add_argument(
        "filename",
        help="Nombre del archivo que se quiere crear (por ejemplo, coso.py)"
    )

    args = parser.parse_args()
    create_main(args.filename)
