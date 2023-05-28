"""Module for working with dates."""
from dateutil import parser
from datetime import datetime, date


def date_formatter(inputted_date: str) -> date:
    """Formate date in YYYY-mm-dd format.

    Args:
        date (str): datetime in any format.

    Returns:
        str: date in YYYY-mm-dd format.
    """
    return parser.parse(inputted_date, dayfirst=True).date()


def get_date_diff(last_contact_date: date):
    delta = date.today() - last_contact_date
    return delta.days
