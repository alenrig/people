from .commands import ls
from .main import people
from .models import People

People.create_table()
commands = [ls]
for command in commands:
    people.add_command(command)
