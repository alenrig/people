from datetime import date
from typing import List, Optional, Union

from peewee import DateField

from ..__main__ import SHORT_TABLE_HEADER
from ..db.queries import add_person_to_db
from ..utils.data_formatter import set_in_rows
from ..utils.dates import date_formatter
from ..utils.table import print_table


def add(
    surname: str,
    name: Optional[str],
    last_contact: str = str(date.today()),
) -> None:
    people = _add(surname=surname, name=name, last_contact=last_contact)
    print_table(SHORT_TABLE_HEADER, people)


def _add(
    surname: str,
    name: Optional[str],
    last_contact: str = str(date.today()),
) -> List[List[Union[str, DateField]]]:
    last_contact_date: date = date_formatter(last_contact)
    person = add_person_to_db(surname, name, str(last_contact_date))
    return set_in_rows([person], passed_days=False)
