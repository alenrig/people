"""Module for CLI commands logic."""
from datetime import date

import click

from .__main__ import SHORT_TABLE_HEADER, TABLE_HEADER
from .models import CharField, People
from .utils.data_formatter import set_in_rows
from .utils.dates import date_formatter
from .utils.table import print_table


@click.command(name="ls")
@click.option(
    "--sort-by",
    type=click.Choice(["surname", "days"], case_sensitive=False),
    default="surname",
)
def list_people_command(*args, **kwargs) -> None:
    list_people(*args, **kwargs)


@click.command(name="add")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=str(date.today()),
    help="date in dd.mm.YYYY format. Default today.",
)
def add_command(*args, **kwargs) -> None:
    """Add new person to contacts."""
    add(*args, **kwargs)


@click.command(name="remove")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
def remove_command(*args, **kwargs) -> None:
    remove(*args, **kwargs)


@click.command(name="contact")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
def contact_command(*args, **kwargs) -> None:
    contact(*args, **kwargs)
