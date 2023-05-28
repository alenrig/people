"""Module for CLI commands logic."""
from datetime import date

import click

from .__main__ import TABLE_HEADER, SHORT_TABLE_HEADER
from .models import People
from .utils.dates import date_formatter, get_date_diff
from .utils.table import print_table


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    data = [
        [
            f"{person.first_name} {person.last_name}",
            person.last_contact,
            get_date_diff(person.last_contact),
        ]
        for person in People.select()
    ]
    print_table(TABLE_HEADER, data)


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=str(date.today()),
    help="date in dd.mm.YYYY format. Default today.",
)
def add(
    first_name: str,
    last_name: str,
    last_contact: str = str(date.today()),
) -> None:
    """Add new person to contacts."""
    last_contact_date = date_formatter(last_contact)
    person = People.create(
        first_name=first_name, last_name=last_name, last_contact=last_contact_date
    )
    data = [[f"{person.first_name} {person.last_name}", str(person.last_contact)]]
    print_table(SHORT_TABLE_HEADER, data)


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


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
def contact(first_name: str, last_name: str):
    """Set last contact with person to today."""
    person = People.get(
        People.first_name == first_name and People.last_name == last_name
    )
    person.last_contact = date.today()
    person.save()
    data = [[f"{person.first_name} {person.last_name}", str(person.last_contact)]]
    print_table(SHORT_TABLE_HEADER, data)
