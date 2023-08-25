"""Package entrypoint."""
from people.cli import setup_commands
from people.cli.groups import people
from people.configs import setup_configs
from people.db.models import  setup_db


def main():
    """Start app."""
    setup_configs()
    setup_commands()
    setup_db()
    people()  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    main()
