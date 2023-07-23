"""List command helper."""
from typing import List, Union

from peewee import DateField

from ..db.models import People
from ..db.queries import get_all_persons_from_db
from ..decorators.print_table import print_table_wrapper
from ..utils.data_formatter import set_in_rows


@print_table_wrapper
def list_people(sort_by: str) -> List[List[Union[str, DateField]]]:
    """List peoples in terminal.

    Args:
        sort_by (str): field to sort by.
    """
    order = People.last_contact if sort_by == "days" else People.surname
    people = get_all_persons_from_db(order)
    return set_in_rows(people)
