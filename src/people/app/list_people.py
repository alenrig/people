"""List command helper."""
from typing import List

from ..db.models import People
from ..db.queries import get_all_persons_from_db
from ..utils.data_formatter import set_in_rows_with_diff
from ..utils.table import print_table_wrapper


@print_table_wrapper
def list_people(sort_by: str) -> List[List[str]]:
    """List peoples in terminal.

    Args:
        sort_by (str): field to sort by.
    """
    order = People.last_contact if sort_by == "days" else People.surname
    people = get_all_persons_from_db(order)
    return set_in_rows_with_diff(people)
