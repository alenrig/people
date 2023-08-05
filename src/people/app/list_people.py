"""List command helper."""
from typing import List

from ..db.models import People
from ..db.queries import get_all_persons_from_db


def list_people(sort_by: str) -> List[People]:
    """List peoples in terminal.

    Args:
        sort_by (str): field to sort by.
    """
    order = People.last_contact if sort_by == "days" else People.surname
    return get_all_persons_from_db(order)
