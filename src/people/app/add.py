"""Add command helper."""
from datetime import date
from typing import Optional

from people.db.models import People

from ..db.queries import add_person_to_db
from ..utils.dates import date_formatter


def add_person(
    surname: str,
    name: Optional[str],
    last_contact: str,
) -> People:
    """Add person to storage and print on terminal caller.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
        last_contact (str): person last contact date.
    """
    last_contact_date: date = date_formatter(last_contact)
    return add_person_to_db(surname, name, str(last_contact_date))
