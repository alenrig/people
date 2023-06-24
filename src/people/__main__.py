"""Package entrypoint."""

import click

SHORT_TABLE_HEADER = ["Name", "Last Contacted"]
TABLE_HEADER = ["Name", "Last Contact", "Days Passed"]


@click.group
@click.pass_context
def people(ctx: click.Context, **options):
    """Track down then you contact someone last time."""
    ctx.ensure_object(dict)
    ctx.obj = options


def main():
    """Package entrypoint function."""
    people()  # pylint: disable=E1120


if __name__ == "__main__":
    main()
