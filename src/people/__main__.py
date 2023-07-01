"""Package entrypoint."""
from .cli import setup_commands
from .cli.groups import people
from .configs import setup_configs
from .db.models import setup_db


def main():
    setup_configs()
    setup_commands()
    setup_db()
    people()


if __name__ == "__main__":
    main()
