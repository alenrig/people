"""Module for working with dates."""
from dateutil import parser


def date_formatter(date: str) -> str:
    """Formate date in YYYY-mm-dd format.

    Args:
        date (str): datetime in any format.

    Returns:
        str: date in YYYY-mm-dd format.
    """
    parsed_date = parser.parse(date)
    return f"{parsed_date.year}-{parsed_date.month}-{parsed_date.day}"
