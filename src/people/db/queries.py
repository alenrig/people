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


def get_person_from_db(surname: str, name: Optional[str] = None) -> People:
    try:
        result: People = People.get(People.name == name and People.surname == surname)
    except DoesNotExist as e:
        sys.exit("Person does not exists.")
    return result


def update_last_contact_date(person: People, last_contact: date = date.today()) -> People:
    person.last_contact = last_contact  # type: ignore
    person.save()
    return person


def _is_already_exists(surname: str, name: Optional[str] = None) -> None:
    people = None
    with contextlib.suppress(DoesNotExist):
        people = People.get(People.name == name and People.surname == surname)
    if people:
        sys.exit("Person already exists.")
