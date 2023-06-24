"""Module for CLI commands logic."""
from datetime import date
from typing import List, Optional, Union

import click
from peewee import DateField

from .__main__ import SHORT_TABLE_HEADER, TABLE_HEADER
from .models import People, CharField
from .utils.data_formatter import set_in_rows
from .utils.dates import date_formatter
from .utils.table import print_table


@click.command(name="ls")
@click.option(
    "--sort-by",
    type=click.Choice(['surname', 'days'], case_sensitive=False),
    default="surname"
)
def list_people(sort_by: str) -> None:
    """List contacts."""
    if sort_by == "surname":
        order: CharField = People.surname # type: ignore
    elif sort_by == "days":
        order: DateField = People.last_contact # type: ignore
    people: List[List[Union[str, DateField]]] = set_in_rows(
        People.select().order_by(order)  # type: ignore
    )
    print_table(TABLE_HEADER, people)


@click.command
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=str(date.today()),
    help="date in dd.mm.YYYY format. Default today.",
)
def add(
    surname: str,
    name: Optional[str],
    last_contact: str = str(date.today()),
) -> None:
    """Add new person to contacts."""
    last_contact_date: date = date_formatter(last_contact)
    if name:
        person: People = People.create(
            name=name, surname=surname, last_contact=last_contact_date
        )
    else:
        person = People.create(surname=surname, last_contact=last_contact_date)
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)


@click.command
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
def remove(name: str, surname: str):
    """Remove person from contacts.

    Args:
        name (str): person first name
    """
    People.get(People.name == name and People.surname == surname).delete_instance()


@click.command
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
def contact(name: str, surname: str):
    """Set last contact with person to today."""
    person: People = People.get(People.name == name and People.surname == surname)
    person.last_contact = date.today()  # type: ignore
    person.save()
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)
