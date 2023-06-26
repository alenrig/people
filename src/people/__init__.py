"""Package init module."""
import configparser
import contextlib
import os

from .__main__ import people
from .db.models import People

# isort: off
from .commands import add_command, contact_command, list_people_command, remove_command

config = configparser.ConfigParser()
configdir = f"{os.getenv('HOME')}/.config/people"
configpath = f"{configdir}/config.ini"
if not os.path.isfile(configpath):
    with contextlib.suppress(OSError):
        os.makedirs(configdir)
    config.add_section("main")
    config.set("main", "config_dir", configdir)
    config.add_section("database")
    config.set("database", "file", "people.db")
    with open(configpath, "w") as file:
        config.write(file)

People.create_table()
commands = [add_command, list_people_command, remove_command, contact_command]
for command in commands:
    people.add_command(command)
