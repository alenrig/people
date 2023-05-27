"""Module for ORM modules."""

from dataclasses import dataclass

from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase("people.db")


class BaseModel(Model):
    """Parent class for tables ORM."""

    @dataclass
    class Meta:
        """Class for meta information defining."""

        database = db


@dataclass
class People(BaseModel):
    """Table for people representation.

    Args:
        BaseModel: parent class with meta definition.
    """

    name = CharField()
