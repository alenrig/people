"""Remove from storage command helper."""
from typing import Optional

from people.db.models import People

from ..db.queries import delete_person_from_db


def remove_person(id: int) -> People:
    """Remove person from storage.

    Args:
        id (int): person id.
    """
    return delete_person_from_db(id)
