"""Contact command helper."""
from datetime import date
from typing import Optional

from people.db.models import People

from ..db.queries import update_last_contact_date
from ..utils.dates import date_formatter


def contact_person(surname: str, name: Optional[str], last_contact: str) -> People:
    """Update person last contact date.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
        last_contact (str): last contact date with person.
    """
    last_contact_date: date = date_formatter(last_contact)
    return update_last_contact_date(surname, name, last_contact_date)
