"""Package entrypoint."""
from .cli import setup_commands
from .cli.groups import people
from .configs import setup_configs
from .db.models import setup_db


def main():
    """Start app."""
    setup_configs()
    setup_commands()
    setup_db()
    people()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
