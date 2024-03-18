import sys
from typing import Any

from rich import print
from rich.prompt import Confirm
from typer import Abort, Typer, Exit


class Cli:
    app = Typer(
        add_completion=True,
        context_settings={"help_option_names": ["-h", "--help"]},
        help="",
        no_args_is_help=True,
        rich_markup_mode="rich",
    )
    group_defaults = dict(
        help="No help text provided, add it with: Cli.group(help='my help text')",
        no_args_is_help=True,
        rich_markup_mode="rich",
    )

    @staticmethod
    def root() -> Typer:
        """Return the root typer instance

        Commands decorated with this instance will show up at the cli root
        """
        return Cli.app

    @staticmethod
    def group(*args, **kwargs) -> Typer:
        """ Create a new Typer instance.

        This defines a sub-parser.
        Commands decorated with this object will appear as sub commands (once added to the root instance)
        The module name will be used as the top level 'grouping' command
        """
        kwargs2 = Cli.group_defaults
        kwargs2.update(kwargs)
        return Typer(*args, **kwargs2)

    @staticmethod
    def exit(message: Any, code: int=1):
        """Return an Exception that exits the CLI. Should be raised by the caller

        Usage:
        ```
        raise Cli.exit('something bad')
        ```

        Raising the exception where the function is called instead of here has multiple benefits
         - Gives a more accurate traceback (when needed)
         - The caller can chain other exceptions using `raise Cli.exit() from e`
         - Linters (like pylint) can more easily detect program flow, thus report less false errors
        """
        print(f'[bold red]Error:[/bold red] {message}', file=sys.stderr)
        return Exit(code=code)

    @staticmethod
    def done(message: Any):
        print(f'[bold green]Done:[/bold green] {message}')

    @staticmethod
    def confirm(message: Any, return_val: Any = False):
        """Check with the user if its okay to continue.

        This is useful if a non critical error happens, the user may want to fix something before
        continuing or it may be fine to just go ahead anyway.

        This gives the user an oppurtunity to make that decision before potentially doing something
        destructive.

        The `return_val` param provides a way to bind a default value to the original variable before
        the failed operation happened.

        Example usage:
        ```
        try:
            result = operation_that_may_fail()
            assert result is True
        except ThingFailed:
            result = Cli.confirm('The thing failed', return_val=False)
        ```
        """
        ans = Confirm.ask(f'[bold yellow]Warning:[/bold yellow] {message}\nContinue?')
        if not ans:
            raise Abort()
        return return_val
