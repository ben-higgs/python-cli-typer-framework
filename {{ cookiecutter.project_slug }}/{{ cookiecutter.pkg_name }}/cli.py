"""
This module defines the main CLI setup.

It looks in the 'commands' directory and auto-imports commands,

Making a command module
- Command modules must contain an 'app' attribute that is a typer instance.
- The typer instance determines where the command will be placed in the command hirearchy
- Top level commands are defined by using the `Cli.root()` method
- Grouped commands are defined by using the `Cli.group()` method

```
from {{ cookiecutter.pkg_name }} import Cli

app = Cli.root()
# OR
app = Cli.group(help='Group help text')
```

Define commands within the module by simply decorating command functions with `@app.command()`
e.g.
```
@app.command()
def my_command(...):
    ...
```

Any arguments defined to this function will be used as cli parameters. See the typer docs for details
"""
import importlib
from pathlib import Path

from rich import print
from typer import Option

from {{ cookiecutter.pkg_name }} import Cli
from {{ cookiecutter.pkg_name }} import config

app = Cli.root()


def module_import(module):
    def module_name(module) -> str:
        return Path(module.__file__).stem

    # If the module has its own `app` then it is a subcommand
    # else the module contains commands that should be added to the top level app
    if module.app is not app:
        app.add_typer(module.app, name=module_name(module))

    return module


def is_command(path: Path):
    return path.stem not in ["__init__", "base"]


COMMANDS_DIR = Path(__file__).parent / "commands"
MODULES = [
    importlib.import_module(f"aetools.commands.{path.stem}")
    for path in COMMANDS_DIR.glob('**/*.py')
    if is_command(path)
]
COMMANDS = [
    module_import(module)
    for module in MODULES
    if hasattr(module, "app")
]


def _command_tree() -> dict[str, list]:
    """Gather the command tree hirearchy"""
    tree = {"root": [command.callback.__name__ for command in app.registered_commands]}
    for group in app.registered_groups:
        if not group.name:
            continue
        tree[group.name] = [
            command.callback.__name__
            for command in group.typer_instance.registered_commands
        ]

    return tree


@app.command()
def tree():
    """Print the command tree hirearchy"""
    for group, cmds in _command_tree().items():
        print(group)
        for cmd in cmds:
            print(' ', cmd)


@app.callback()
def main(
    verbose: int = Option(
        0,
        '-v', '--verbose',
        count=True,
        help='The verbosity level, (use multiple times to increment)'
    ),
):
    """The main CLI callback. This is where global options and config are managed"""
    config.VERBOSE = verbose


if __name__ == '__main__':
    app()
