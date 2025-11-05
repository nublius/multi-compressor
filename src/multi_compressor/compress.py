import shutil
from pathlib import Path

def compress_folder_to_zip(input_folder_path):
    folder = Path(input_folder_path)
    parent_dir = folder.parent

    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist or is not a directory")
        return

    archive_base_name = parent_dir / folder.name
    archive_format = "zip"

    try:
        shutil.make_archive(base_name=archive_base_name, format=archive_format, root_dir=folder)
        return archive_base_name.with_suffix(".zip")
    except exception as e:
        print("Compression failed:", e)



