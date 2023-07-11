"""Remove from storage command helper."""
from typing import Optional

from ..db.queries import delete_person_from_db


def remove(surname: str, name: Optional[str]) -> None:
    """Remove person from storage.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
    """
    delete_person_from_db(surname, name)
