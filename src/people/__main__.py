"""Package entrypoint."""
from .cli import setup_commands
from .cli.groups import people
from .config import get_configs


def main():
    """Package entrypoint function."""
    get_configs()
    setup_commands()
    people()  # pylint: disable=E1120


if __name__ == "__main__":
    main()
