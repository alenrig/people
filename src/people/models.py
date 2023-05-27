from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase('people.db')

class People(Model):
    name = CharField()

    class Meta:
        database = db
