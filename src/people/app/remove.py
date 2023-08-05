"""Remove from storage command helper."""
from typing import Optional

from people.db.models import People

from ..db.queries import delete_person_from_db


def remove_person(surname: str, name: Optional[str]) -> People:
    """Remove person from storage.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
    """
    return delete_person_from_db(surname, name)
