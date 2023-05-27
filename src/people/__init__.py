"""Package init module."""

from .commands import add, list_people
from .__main__ import people
from .models import People

People.create_table()
commands = [add, list_people]
for command in commands:
    people.add_command(command)
