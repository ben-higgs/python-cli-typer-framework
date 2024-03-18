# Python Typer CLI Framework

This is a [CookieCutter](https://www.cookiecutter.io/) template for a CLI app framework using [Typer](https://typer.tiangolo.com/)

# Setup CookieCutter

Install cookiecutter with [pipx](https://pypa.github.io/pipx/), or use plain [pip](https://pip.pypa.io/en/stable/) if you like to live dangerously

```bash
pipx install cookiecutter
```

# Create a cli app from this template

```bash
# 1. Create the repo
cookiecutter gh:ben.higgs/python-typer-cli-framework
<<cookiecutter config questions>>

# 2. Init the repo
cd my-cli-project
make venv
. .venv/bin/activate

# 3. Your CLI tool is ready to go!
my-cli-project --help
```

cookiecutter will interactively ask for info about the app & create all the neccesary files for you, you can also provide a config file using `--config-file` if you have a predefined config
