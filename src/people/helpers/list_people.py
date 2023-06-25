from typing import List, Union

from peewee import CharField, DateField

from ..__main__ import TABLE_HEADER
from ..db.models import People
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
    people: List[List[Union[str, DateField]]] = set_in_rows(
        People.select().order_by(order)  # type: ignore
    )
    return people
