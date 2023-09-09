"""CLI Module."""

from .commands import add_command, contact_command, list_people_command, remove_command
from .groups import people


def setup_commands() -> None:
    """Setup CLI commands."""
    cli_commands = [add_command, contact_command, list_people_command, remove_command]
    for command in cli_commands:
        people.add_command(command)
