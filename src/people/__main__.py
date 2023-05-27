"""Package entrypoint."""

import click


@click.group
@click.pass_context
def people(ctx: click.Context, **options):
    """Entry CLI.

    Args:
        ctx (click.Context)
    """
    ctx.ensure_object(dict)
    ctx.obj = options


def main():
    """Package entrypoint function."""
    people()  # pylint: disable=E1120


if __name__ == "__main__":
    main()
