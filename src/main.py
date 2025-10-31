from compress_subfolders import compress_subfolders
from pathlib import Path
import click

@click.command()
@click.argument("path")
def compressor(path):
    """Compress all subfolders in the given path."""
    path = Path(path)
    subfolders = [f for f in path.iterdir() if f.is_dir()]
    
    print(f"Compressing subfolders in {path.name}")

    # Progress bar
    with click.progressbar(subfolders, label="Compressing...") as bar:
        for folder in bar:
            print(f" Compressing {folder.name}...")

if __name__ == "__main__":
    compressor()
