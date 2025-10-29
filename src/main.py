from compress_subfolders import compress_subfolders
import click

@click.command()
@click.argument("path")
def compressor(path):
    """Compress all subfolders in the given path."""
    compress_subfolders(path)

if __name__ == "__main__":
    compressor()
