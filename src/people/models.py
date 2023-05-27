from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase("people.db")


class BaseModel(Model):
    class Meta:
        database = db


class People(BaseModel):
    name = CharField()
