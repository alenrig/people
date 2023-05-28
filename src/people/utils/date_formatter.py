from datetime import date, datetime

from dateutil import parser


def date_formatter(date: str) -> str:
    dt = parser.parse(date)
    return f"{dt.year}-{dt.month}-{dt.day}"
