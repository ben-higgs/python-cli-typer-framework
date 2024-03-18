import requests

from {{ cookiecutter.pkg_name }} import Cli

# Using the root Typer instance will include the commands
# defined in this module to the top level cli
app = Cli.root()


# This is an example command, replace this with your own
@app.command()
def quote(qty: int=1):
    """ Display a random quote """
    res = requests.get("https://api.quotable.io/quotes/random", params={"limit": qty})
    res.raise_for_status()
    body = res.json()
    for i, quote in enumerate(body):
        print('"', quote["content"], '"', sep="")
        print("  -", quote["author"])
        if i < len(body) -1: print()
