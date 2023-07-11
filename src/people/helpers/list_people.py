"""List command helper."""
from typing import List, Union

from peewee import DateField

from ..configs import TABLE_HEADER
from ..db.models import People
from ..db.queries import get_all_persons_from_db
from ..utils.data_formatter import set_in_rows
from ..utils.table import print_table


def list_people(sort_by: str) -> None:
    """List peoples in terminal.

    Args:
        sort_by (str): field to sort by.
    """
    people = _list_people(sort_by=sort_by)
    print_table(TABLE_HEADER, people)


def _list_people(sort_by: str) -> List[List[Union[str, DateField]]]:
    order = People.last_contact if sort_by == "days" else People.surname
    people = get_all_persons_from_db(order)
    return set_in_rows(people)
