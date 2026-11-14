from pathlib import Path
import shutil
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "input",
    "output",
]

MAIN_TEMPLATE = PROJECT_ROOT / "scripts" / "templates" / "main.py"


def create_folders_for_work(folder_name: str) -> None:
    iteration_path = PROJECT_ROOT / folder_name
    iteration_path.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (iteration_path / folder).mkdir(exist_ok=True)

    destination = iteration_path / "main.py"

    if not destination.exists():
        shutil.copy2(MAIN_TEMPLATE, destination)


def create_folders() -> None:
    args = sys.argv[1:]

    if not args:
        print(
            "Creating folder structure 'input - ouput - main.py'\n"
            f"\n{'*' * 79}\n"
            "To provide other folder name, use:\n"
            "\tpython create_folder_structure.py 01_report 02_test\n"
            f"{'*' * 79}"
        )
        create_folders_for_work("01_issue")
    else:
        for iteration in args:
            print(
                f"Creating folder structure for iteration "
                f"'{iteration}'...",
                end=" ",
            )
            create_folders_for_work(iteration)
            print("Done!")


if __name__ == "__main__":
    create_folders()
