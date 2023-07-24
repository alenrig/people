"""Add command helper."""
from datetime import date
from typing import List, Optional, Union

from peewee import DateField

from ..db.queries import add_person_to_db
from ..utils.table import print_table_wrapper
from ..utils.data_formatter import set_in_rows
from ..utils.dates import date_formatter


@print_table_wrapper
def add(
    surname: str,
    name: Optional[str],
    last_contact: str,
) -> List[List[Union[str, DateField]]]:
    """Add person to storage and print on terminal caller.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
        last_contact (str): person last contact date.
    """
    last_contact_date: date = date_formatter(last_contact)
    person = add_person_to_db(surname, name, str(last_contact_date))
    return set_in_rows([person], passed_days=False)
