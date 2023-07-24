"""Contact command helper."""
from datetime import date
from typing import List, Optional, Union

from peewee import DateField

from ..db.queries import update_last_contact_date
from ..utils.data_formatter import set_in_rows
from ..utils.dates import date_formatter
from ..utils.table import print_table_wrapper


@print_table_wrapper
def contact(
    surname: str, name: Optional[str], last_contact: str
) -> List[List[Union[str, DateField]]]:
    """Update person last contact date.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
        last_contact (str): last contact date with person.
    """
    last_contact_date: date = date_formatter(last_contact)
    person = update_last_contact_date(surname, name, last_contact_date)
    return set_in_rows([person], passed_days=False)
