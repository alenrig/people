import click


@click.group
@click.pass_context
def people(ctx: click.Context, **options):
    """Track down then you contact someone last time."""
    ctx.ensure_object(dict)
    ctx.obj = options
