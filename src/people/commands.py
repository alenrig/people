"""Module for CLI commands logic."""
import click

from .models import People


@click.command(name="ls")
def list_people() -> None:
    """List all people in contacts."""
    for man in People.select():
        print(man.name)


@click.command
@click.argument("name")
def add(name: str) -> None:
    """Add new person in contacts.

    Args:
        name (str): first name of a person
    """
    People.create(name=name)
