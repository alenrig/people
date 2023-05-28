"""Module for CLI commands logic."""
from datetime import date

import click

from .models import People
from .utils.date_formatter import date_formatter
from .utils.table import print_table


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    data = [
        [f"{man.first_name} {man.last_name}", man.last_contacted]
        for man in People.select()
    ]
    print_table(["Name", "Last Contacted"], data)


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.option("-d", "--date", default=date.today, help="Last contacted date")
def add(first_name: str, last_name: str, date: str) -> None:
    date = date_formatter(date)
    People.create(first_name=first_name, last_name=last_name, last_contacted=date)


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
