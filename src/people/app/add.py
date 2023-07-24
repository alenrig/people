"""Add command helper."""
from datetime import date
from typing import List, Optional

from ..db.queries import add_person_to_db
from ..utils.data_formatter import set_in_rows_without_diff
from ..utils.dates import date_formatter
from ..utils.table import print_table_wrapper


@print_table_wrapper
def add(
    surname: str,
    name: Optional[str],
    last_contact: str,
) -> List[List[str]]:
    """Add person to storage and print on terminal caller.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
        last_contact (str): person last contact date.
    """
    last_contact_date: date = date_formatter(last_contact)
    person = add_person_to_db(surname, name, str(last_contact_date))
    return set_in_rows_without_diff([person])
