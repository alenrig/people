from typing import List, Optional, Union

from peewee import DateField

from ..configs import SHORT_TABLE_HEADER
from ..db.models import People
from ..db.queries import get_person_from_db, update_last_contact_date
from ..utils.data_formatter import set_in_rows
from ..utils.table import print_table


def contact(surname: str, name: Optional[str] = None) -> None:
    people = _contact(surname, name)
    print_table(SHORT_TABLE_HEADER, people)


def _contact(surname: str, name: Optional[str]) -> List[List[Union[str, DateField]]]:
    person = update_last_contact_date(surname, name)
    return set_in_rows([person], passed_days=False)
