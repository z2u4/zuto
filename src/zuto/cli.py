import click
from . import Zuto
import os

@click.command()
@click.option("-p", "--path", type=click.Path(exists=True), help="Path to the tasks folder")
def cli(path):
    if not path:
        path = os.getcwd()

    zuto = Zuto(path)
    zuto.start()

if __name__ == "__main__":
    cli()

