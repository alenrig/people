from datetime import datetime, date
from dateutil import parser


def date_formatter(string: str) -> date:
    dt = parser.parse(string)
    return datetime.strptime(f"{dt.year}-{dt.month}-{dt.day}", '%Y-%m-%d').date()
