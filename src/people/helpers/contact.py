from datetime import date
from typing import List, Optional, Union

from peewee import DateField

from ..configs import SHORT_TABLE_HEADER
from ..db.queries import update_last_contact_date
from ..utils.data_formatter import set_in_rows
from ..utils.dates import date_formatter
from ..utils.table import print_table


def contact(
    surname: str,
    name: Optional[str] = None,
    last_contact: str = f"{date.today().day}.{date.today().month}.{date.today().year}",
) -> None:
    people = _contact(surname, name, last_contact)
    print_table(SHORT_TABLE_HEADER, people)


def _contact(
    surname: str, name: Optional[str], last_contact: str
) -> List[List[Union[str, DateField]]]:
    last_contact_date: date = date_formatter(last_contact)
    person = update_last_contact_date(surname, name, last_contact_date)
    return set_in_rows([person], passed_days=False)
