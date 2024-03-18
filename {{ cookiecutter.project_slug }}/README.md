# {{ cookiecutter.project_name }}

# Setup

This repo demonstrates how to make a command tree with [Typer](https://typer.tiangolo.com/) that is dynamic and simple to extend.

## Structure

There is a root cli object defined at `{{ cookiecutter.pkg_name }}/__init__.py:Cli.app`
This contains all the top level commands and command groups.

The `commands` directory contains all the cli commands, grouped by module. Each module can either be a collection of top-level commands or a command group containing sub-commands.
These are all automatically detected at runtime. Simply add new modules to this directory to extend the cli (see below).

The only requirement is that all modules must contain an `app` attribute which is a `Typer` instance
 
Some commands are defined in `cli.py` but for design reasons these should be limited to meta or operational commands such as `list`, `help`, `install` etc...

## Extend

### New Single Command

To add a new top level command:
- Create a new module in the `commands` directory
- Fetch the root typer app
- Decorate your new function(s) with it

```shell
touch {{ cookiecutter.pkg_name }}/commands/foo.py
```

then

```python
# foo.py
from {{ cookiecutter.pkg_name }} import Cli

app = Cli.root()

@app.command()
def bar(name: str, qty: int=1):
    """the bar command help text"""
    ...
```

Notes about function params:
- Adding default values to parameters will make the param optional
- You can use Typer's `Argument` and `Option` classes for more control over params
- See the [typer arguments docs](https://typer.tiangolo.com/tutorial/commands/arguments/) for more info

Notes about help text:
- Adding type hints and docstrings to the functions will add help text to the cli `--help` info
- See the [typer help docs](https://typer.tiangolo.com/tutorial/commands/help/) for more info

All functions defined in this way will show up as root commands
i.e can be called like `$ cli bar`

### New Command Group

To add a new group of commands:
- Create a new module in the `commands` directory
- Create a new Cli group
- Decorate your new function(s) with it

```shell
touch {{ cookiecutter.pkg_name }}/commands/foo.py
```

then

```python
# foo.py
from {{ cookiecutter.pkg_name }} import Cli

app = Cli.group(help="My function group")

@app.command()
def bar(a: int, b: int):
    """the bar command help"""
    ...

@app.command()
def baz(a: int, b: int):
    """the baz command help"""
    ...
```

Things to note:
- The command group name will be the name of the module
- These commands will be nested in a group
    - i.e The above functions can be called like `$ cli foo bar` and `$ cli foo baz`
