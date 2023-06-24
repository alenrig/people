from datetime import date
from typing import List, Optional, Union

from peewee import DateField

from ..__main__ import SHORT_TABLE_HEADER
from ..models import People
from ..utils.data_formatter import set_in_rows
from ..utils.dates import date_formatter
from ..utils.table import print_table


def remove(name: str, surname: str) -> None:
    People.get(People.name == name and People.surname == surname).delete_instance()
