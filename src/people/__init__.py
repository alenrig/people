"""Package init module."""

from .__main__ import people
from .db.models import People

# isort: off
from .commands import add_command, contact_command, list_people_command, remove_command

People.create_table()
commands = [add_command, list_people_command, remove_command, contact_command]
for command in commands:
    people.add_command(command)
