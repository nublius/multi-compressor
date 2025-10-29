from src.compress import compress_folder_to_zip
from pathlib import Path

def compress_subfolders(dir):
    main_dir = Path(dir)

    if not main_dir.exists() or not main_dir.is_dir():
        print("Folder does not exist or is not a directory")
        return

    has_subfolders = False
    for subfolder in main_dir.iterdir():
        if subfolder.is_dir():
            has_subfolders = True
            compress_folder_to_zip(subfolder)

    if not has_subfolders:
        print("No subfolders found in", main_dir)

