"""Module for CLI commands logic."""
from datetime import date

import click

from .__main__ import TABLE_HEADER
from .models import People
from .utils.date_formatter import date_formatter, get_date_diff
from .utils.table import print_table


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    data = [
       [f"{man.first_name} {man.last_name}", man.last_contacted, get_date_diff(man.last_contacted)]
        for man in People.select()
    ]
    print_table(["Name", "Last Contacted", "Days Passed"], data)


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.option(
    "-l",
    "--last_contacted_date",
    type=str,
    default=str(date.today()),
    help="date in dd.mm.YYYY format. Default today.",
)
def add(
    first_name: str,
    last_name: str,
    last_contacted_date: str = str(date.today()),
) -> None:
    """Add new person using FIRST_NAME and LAST_NAME."""
    last_contacted_date = date_formatter(last_contacted_date)
    man = People.create(
        first_name=first_name, last_name=last_name, last_contacted=last_contacted_date
    )
    data = [[f"{man.first_name} {man.last_name}", man.last_contacted]]
    print_table(TABLE_HEADER, data)


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
def remove(first_name: str, last_name: str):
    """Remove person from contacts.

    Args:
        name (str): person first name
    """
    People.get(
        People.first_name == first_name and People.last_name == last_name
    ).delete_instance()
