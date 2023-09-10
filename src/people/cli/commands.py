"""Module for CLI commands logic."""

import click

from people.utils.presenter import set_in_rows_with_diff, set_in_rows_without_diff
from people.utils.view import print_table

from ..app import add_person, contact_person, list_people, remove_person
from ..configs import SHORT_TABLE_HEADER, TABLE_HEADER, TODAY_DATE


@click.command(name="ls")
@click.option(
    "--sort-by",
    "-s",
    type=click.Choice(["id", "surname", "days"], case_sensitive=False),
    default="id",
)
def list_people_command(sort_by: str) -> None:
    """List contacts"""
    peoples = list_people(sort_by=sort_by)
    presented_peoples = set_in_rows_with_diff(peoples)
    print_table(TABLE_HEADER, presented_peoples)


@click.command(name="add")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=TODAY_DATE,
    help="date in dd.mm.YYYY format. Default today.",
)
def add_command(surname, name, last_contact) -> None:
    """Add new person to contacts"""
    person = add_person(surname, name, last_contact)
    presented_person = set_in_rows_without_diff([person])
    print_table(SHORT_TABLE_HEADER, presented_person)


@click.command(name="remove")
@click.argument("id", type=int)
def remove_command(id) -> None:
    """Remove person from contacts"""
    person = remove_person(id)
    presented_person = set_in_rows_without_diff([person])
    print_table(SHORT_TABLE_HEADER, presented_person)


@click.command(name="contact")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
@click.option(
    "-l",
    "--last_contact",
    type=str,
    default=TODAY_DATE,
    help="date in dd.mm.YYYY format. Default today.",
)
def contact_command(surname, name, last_contact) -> None:
    """Change person last contact date"""
    person = contact_person(surname, name, last_contact)
    presented_person = set_in_rows_without_diff([person])
    print_table(SHORT_TABLE_HEADER, presented_person)
