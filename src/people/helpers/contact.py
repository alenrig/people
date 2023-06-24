from datetime import date
from typing import List, Union

from peewee import DateField

from ..__main__ import SHORT_TABLE_HEADER
from ..models import People
from ..utils.data_formatter import set_in_rows
from ..utils.table import print_table


def contact(name: str, surname: str) -> None:
    people = _contact(name=name, surname=surname)
    print_table(SHORT_TABLE_HEADER, people)


def _contact(name: str, surname: str) -> List[List[Union[str, DateField]]]:
    person: People = People.get(People.name == name and People.surname == surname)
    person.last_contact = date.today()  # type: ignore
    person.save()
    return set_in_rows([person], passed_days=False)
