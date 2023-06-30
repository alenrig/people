import pytest
from people.db.models import People
from peewee import SqliteDatabase


MODELS = [People]

@pytest.fixture
def test_db():
    """Setup Database"""
    _db = SqliteDatabase(":memory:")
    with _db.bind_ctx(MODELS):
        _db.create_tables(MODELS)
        try:
            yield test_db
        finally:
            _db.drop_tables(MODELS)
