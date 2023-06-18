"""Module for working with dates."""
from datetime import date

from dateutil import parser
from peewee import DateField


def date_formatter(inputted_date: str) -> date:
    """Formate date in YYYY-mm-dd format.

    Args:
        date (str): datetime in any format.

    Returns:
        str: date in YYYY-mm-dd format.
    """
    return parser.parse(inputted_date, dayfirst=True).date()


def get_date_diff(last_contact_date: DateField) -> int:
    """Get different between last contact day and today.

    Args:
        last_contact_date (date): date of last contact with person.

    Returns:
        int: different between last contact day and today in days.
    """
    delta = date.today() - last_contact_date
    return delta.days  # type: ignore
