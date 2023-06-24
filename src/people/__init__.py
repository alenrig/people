"""Package init module."""

from .__main__ import people
from .commands import add, contact, list_people, remove
from .models import People

People.create_table()
commands = [add, list_people, remove, contact]
for command in commands:
    people.add_command(command)
