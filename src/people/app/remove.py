"""Remove from storage command helper."""

from people.db.models import People

from ..db.queries import delete_person_from_db


def remove_person(index: int) -> People:
    """Remove person from storage.

    Args:
        index (int): person id.
    """
    return delete_person_from_db(index)
