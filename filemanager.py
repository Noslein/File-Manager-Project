from pathlib import Path
import shutil


download_dir = Path.home() / "Downloads"

CATEGORIES = {
    "Texts": [".txt", ".doc", ".docx", ".pdf", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
}


def create_category_folders(directory):
    # Creates the category folders if they do not exist.
    for category in CATEGORIES:
        (directory / category).mkdir(exist_ok=True)


def get_category(extension):
    # Returns the category corresponding to a file extension.
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(directory):
    # Organizes files in the directory according to their extensions.
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return

    create_category_folders(directory)
    (directory / "Others").mkdir(exist_ok=True)

    for file in directory.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix.lower())
        destination = directory / category / file.name

        shutil.move(file, destination)
        print(f"Moved: {file.name} -> {category}")


organize_files(download_dir)