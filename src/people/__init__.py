from .commands import add, ls
from .__main__ import people
from .models import People

People.create_table()
commands = [add,ls]
for command in commands:
    people.add_command(command)
