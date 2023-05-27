import click

from .models import People


@click.command
@click.pass_context
def ls(ctx: click.Context):
    for man in People.select():
        print(man.name)


@click.command
@click.argument("name")
def add(name):
    People.create(name=name)
