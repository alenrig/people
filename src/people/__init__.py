"""Package init module."""

from .commands import add, list_people, remove
from .__main__ import people
from .models import People

People.create_table()
commands = [add, list_people, remove]
for command in commands:
    people.add_command(command)
