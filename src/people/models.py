"""Module for ORM modules."""

from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase("people.db")


class BaseModel(Model):
    """Parent class for tables ORM.

    Args:
        Model
    """
    class Meta:
        database = db


class People(BaseModel):
    """DB Table for people representation.

    Args:
        BaseModel: parent class with meta definition.
    """
    name = CharField()
