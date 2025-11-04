from compress_subfolders import compress_subfolders
from pathlib import Path
import click

@click.command()
@click.argument("path")
def compressor(path):
    """Compress all subfolders in the given path."""

    click.echo(f"You are about to compress all subfolders in: {path}")

    if not click.confirm("Do you want to continue?", default=False):
        click.echo("Operation cancelled.")
        return

    path = Path(path)
    subfolders = [f for f in path.iterdir() if f.is_dir()]
    
    print(f"Compressing subfolders in {path.name}")

    # Progress bar
    with click.progressbar(subfolders, label="Compressing...") as bar:
        for folder in bar:
            print(f" Compressing {folder.name}...")

    click.echo("Compression complete!")

if __name__ == "__main__":
    compressor()
