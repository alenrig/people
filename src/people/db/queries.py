import contextlib
import sys
from datetime import date
from typing import Optional

from peewee import DoesNotExist

from .models import People


def add_person_to_db(
    surname: str, name: Optional[str] = None, last_contact_date: str = str(date.today())
) -> People:
    _is_already_exists(surname, name)
    result: People = People.create(
        name=name, surname=surname, last_contact=last_contact_date
    )
    return result


def _is_already_exists(surname: str, name: Optional[str] = None):
    people = None
    with contextlib.suppress(DoesNotExist):
        people = People.get(People.name == name and People.surname == surname)
    if people:
        sys.exit("Person already exists.")
