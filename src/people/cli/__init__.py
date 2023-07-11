"""CLI Module."""

from .commands import add_command, contact_command, list_people_command, remove_command
from .groups import people


def setup_commands() -> None:
    """Setup CLI commands."""
    commands = [add_command, contact_command, list_people_command, remove_command]
    for command in commands:
        people.add_command(command)
