"""Module for CLI commands logic."""
from datetime import date
from typing import List, Optional, Union

import click
from peewee import DateField

from .__main__ import SHORT_TABLE_HEADER, TABLE_HEADER
from .models import People
from .utils.data_formatter import set_in_rows
from .utils.dates import date_formatter
from .utils.table import print_table


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    people: List[List[Union[str, DateField]]] = set_in_rows(
        People.select().order_by(People.last_name)
    )
    print_table(TABLE_HEADER, people)


@click.command
@click.argument("last_name", type=str)
@click.argument("first_name", type=str, required=False)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=str(date.today()),
    help="date in dd.mm.YYYY format. Default today.",
)
def add(
    last_name: str,
    first_name: Optional[str],
    last_contact: str = str(date.today()),
) -> None:
    """Add new person to contacts."""
    last_contact_date: date = date_formatter(last_contact)
    if first_name:
        person: People = People.create(
            first_name=first_name, last_name=last_name, last_contact=last_contact_date
        )
    else:
        person = People.create(last_name=last_name, last_contact=last_contact_date)
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)


@click.command
@click.argument("last_name", type=str)
@click.argument("first_name", type=str, required=False)
def remove(first_name: str, last_name: str):
    """Remove person from contacts.

    Args:
        name (str): person first name
    """
    People.get(
        People.first_name == first_name and People.last_name == last_name
    ).delete_instance()


@click.command
@click.argument("last_name", type=str)
@click.argument("first_name", type=str, required=False)
def contact(first_name: str, last_name: str):
    """Set last contact with person to today."""
    person: People = People.get(
        People.first_name == first_name and People.last_name == last_name
    )
    person.last_contact = date.today()  # type: ignore
    person.save()
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)
