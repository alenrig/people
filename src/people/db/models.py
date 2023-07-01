"""Module for ORM modules."""
from datetime import date
from os import path

from peewee import CharField, DateField, Model, SqliteDatabase

from ..configs import config

dbpath = f"{config['main']['config_dir']}/{config['database']['file']}"
db = SqliteDatabase(dbpath)


def setup_db():
    if not _is_db_created(dbpath):
        _create_tables()


def _is_db_created(dbpath: str) -> bool:
    return path.isfile(dbpath)


def _create_tables():
    db.create_tables([People])


class BaseModel(Model):
    """Parent class for tables ORM."""

    class Meta:  # pylint: disable=R0903
        """Class for meta information defining."""

        database = db


class People(BaseModel):
    """Table for people representation.

    Args:
        BaseModel: parent class with meta definition.
    """

    name = CharField(null=True)
    surname = CharField()
    last_contact = DateField(default=date.today())
