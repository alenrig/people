"""Module for CLI commands logic."""
import click

from .models import People


@click.command(name="ls")
def list_people() -> None:
    """List contacts."""
    for man in People.select():
        print(man.name)


@click.command
@click.argument("name")
def add(name: str) -> None:
    """Add new person in contacts.

    Args:
        name (str): person first name
    """
    People.create(name=name)


@click.command
@click.argument("name")
def remove(name: str):
    """Remove person from contacts.

    Args:
        name (str): person first name
    """
    People.get(People.name == name).delete_instance()
