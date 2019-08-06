"""Toml Sort CLI"""

import click

from . import sort_toml


@click.command()
@click.option(
    "-o",
    "--output",
    type=click.File("w"),
    default="-",
    show_default=True,
    help="The output filepath. Choose stdout with '-'.",
)
@click.argument("filename", type=click.File("r"))
def cli(output, filename) -> None:
    """Sort toml file FILENAME, saving results to a file, or stdout (default)

    FILENAME a filepath or standard input (-)

    Examples:

        Read from stdin, write to stdout:

            cat input.toml | toml-sort -

        Read from file on disk, write to file on disk:

            toml-sort -o output.toml input.toml

        Read from file on disk, write to stdout

            toml-sort input.toml
    """
    toml_content = filename.read()
    sorted_toml = sort_toml(toml_content)
    output.write(sorted_toml)
