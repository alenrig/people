"""Package entrypoint."""
from .cli import setup_commands
from .cli.groups import people
from .configs import setup_configs


def main():
    setup_configs()
    setup_commands()
    people()


if __name__ == "__main__":
    main()
