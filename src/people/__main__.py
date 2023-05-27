import click


@click.group
@click.pass_context
def people(ctx: click.Context, **options):
    ctx.ensure_object(dict)
    ctx.obj = options


if __name__ == "__main__":
    people()
