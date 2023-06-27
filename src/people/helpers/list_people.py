from typing import List, Union

from peewee import CharField, DateField

from ..configs import TABLE_HEADER
from ..db.models import People
from ..db.queries import get_all_persons_from_db
from ..utils.data_formatter import set_in_rows
from ..utils.table import print_table


def list_people(sort_by: str) -> None:
    people = _list_people(sort_by=sort_by)
    print_table(TABLE_HEADER, people)


def _list_people(sort_by: str) -> List[List[Union[str, DateField]]]:
    if sort_by == "surname":
        order: CharField = People.surname  # type: ignore
    elif sort_by == "days":
        order: DateField = People.last_contact  # type: ignore
    _people = get_all_persons_from_db(order)  # type: ignore
    return set_in_rows(_people)
