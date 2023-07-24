"""Module for CLI commands logic."""

import click

from ..app import add, contact, list_people, remove
from ..configs import TODAY_DATE


@click.command(name="ls")
@click.option(
    "--sort-by",
    "-s",
    type=click.Choice(["surname", "days"], case_sensitive=False),
    default="surname",
)
def list_people_command(*args, **kwargs) -> None:
    """List contacts"""
    list_people(*args, **kwargs)


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
def add_command(*args, **kwargs) -> None:
    """Add new person to contacts"""
    add(*args, **kwargs)


@click.command(name="remove")
@click.argument("surname", type=str)
@click.argument("name", type=str, required=False)
def remove_command(*args, **kwargs) -> None:
    """Remove person from contacts"""
    remove(*args, **kwargs)


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
def contact_command(*args, **kwargs) -> None:
    """Change person last contact date"""
    contact(*args, **kwargs)
