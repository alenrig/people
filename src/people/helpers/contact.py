from datetime import date
from typing import List, Union

from peewee import DateField

from ..__main__ import SHORT_TABLE_HEADER
from ..db.models import People
from ..utils.data_formatter import set_in_rows
from ..utils.table import print_table
from ..db.queries import get_person_from_db, update_last_contact_date


def contact(name: str, surname: str) -> None:
    people = _contact(name=name, surname=surname)
    print_table(SHORT_TABLE_HEADER, people)


def _contact(name: str, surname: str) -> List[List[Union[str, DateField]]]:
    person = get_person_from_db(surname, name)
    person = update_last_contact_date(person)
    return set_in_rows([person], passed_days=False)
