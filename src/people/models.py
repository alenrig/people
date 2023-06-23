"""Module for ORM modules."""
from peewee import CharField, Model, SqliteDatabase, DateField

db = SqliteDatabase("people.db")


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

    first_name = CharField(null=True)
    last_name = CharField()
    last_contact = DateField()
