"""Module for CLI commands logic."""
import click

from .models import People
from .utils.table import print_table


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    data = [[man.first_name, man.last_name] for man in People.select()]
    print_table(["First Name", "Last Name"], data)


@click.command
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
def add(first_name: str, last_name: str) -> None:
    """Add new person in contacts.

    Args:
        name (str): person first name
    """
    People.create(first_name=first_name, last_name=last_name)


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
