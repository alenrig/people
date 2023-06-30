import contextlib
import sys
from datetime import date
from typing import List, Optional, Union

from peewee import CharField, DateField, DoesNotExist

from .models import People


def add_person_to_db(
    surname: str, name: Optional[str] = None, last_contact_date: str = str(date.today())
) -> People:
    _check_if_already_exists(surname, name)
    result: People = People.create(
        name=name, surname=surname, last_contact=last_contact_date
    )
    return result


def get_person_from_db(surname: str, name: Optional[str] = None) -> People:
    return _return_person_if_exists(surname, name)


def get_all_persons_from_db(order: Union[CharField, DateField]) -> List[People]:
    return People.select().order_by(order)  # type: ignore


def update_last_contact_date(
    surname: str, name: Optional[str] = None, last_contact: date = date.today()
) -> People:
    person = get_person_from_db(surname, name)
    person.last_contact = last_contact  # type: ignore
    person.save()
    return person


def delete_person_from_db(surname: str, name: Optional[str] = None) -> None:
    person = _return_person_if_exists(surname, name)
    person.delete_instance()


def _check_if_already_exists(surname: str, name: Optional[str] = None) -> None:
    people = None
    with contextlib.suppress(DoesNotExist):
        people = People.get(People.name == name and People.surname == surname)
    if people:
        sys.exit("Person already exists.")


def _return_person_if_exists(surname: str, name: Optional[str] = None) -> People:
    try:
        person: People = People.get(People.name == name and People.surname == surname)
    except DoesNotExist:
        sys.exit("Person does not exists.")
    else:
        return person
