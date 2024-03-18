from typing import List

from {{ cookiecutter.pkg_name }} import Cli

# Using a new Typer instance will include the commands defined
# here as sub-commands grouped by the module name.
app = Cli.group(help="Text functions")


# These are example sub-commands, replace these with your own
@app.command()
def echo(args: List[str]):
    """ Echo the given arguments to stdout """
    print(*args)


@app.command()
def reverse(args: List[str]):
    """ Reverse a string """
    print(" ".join(args)[::-1])
