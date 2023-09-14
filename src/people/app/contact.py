"""Contact command helper."""
from datetime import date

from people.db.models import People

from ..db.queries import update_last_contact_date
from ..utils.dates import date_formatter


def contact_person(index: int, last_contact: str) -> People:
    """Update person last contact date.

    Args:
        index (int): person id.
        last_contact (str): last contact date with person.
    """
    last_contact_date: date = date_formatter(last_contact)
    return update_last_contact_date(index, last_contact_date)
