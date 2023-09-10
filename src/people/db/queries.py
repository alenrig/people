"""DB queries module."""
import sys
from datetime import date
from typing import List, Optional, Union

from peewee import CharField, DateField

from .models import People


def add_person_to_db(
    surname: str, name: Optional[str] = None, last_contact_date: str = str(date.today())
) -> People:
    """Add person to db

    Args:
        surname (str): person surname
        name (Optional[str], optional): person name. Defaults to None.
        last_contact_date (str, optional): last contact with person.
        Defaults to str(date.today()).

    Returns:
        People: instance on People
    """
    _check_if_already_exists(surname, name)
    result: People = People.create(
        name=name, surname=surname, last_contact=last_contact_date
    )
    return result


def get_person_from_db(id: int) -> People:
    """Get person from db

    Args:
        id (int): person id.

    Returns:
        People: instance of Person
    """
    return _return_person_if_exists(id)


def get_all_persons_from_db(order: Union[CharField, DateField]) -> List[People]:
    """Get all persons from db.

    Args:
        order (Union[CharField, DateField]): order persons by surnames or dates.

    Returns:
        List[People]: list of all People instances.
    """
    return People.select().order_by(order)  # type: ignore


def update_last_contact_date(
    id: int, last_contact: date = date.today()
) -> People:
    """Update last contact date with person

    Args:
        id (int): person id.
        last_contact (date, optional): last contact date with person.
        Defaults to date.today().

    Returns:
        People: instance of People.
    """
    person = get_person_from_db(id)
    person.last_contact = last_contact  # type: ignore
    person.save()
    return person


def delete_person_from_db(id: int) -> People:
    """Delete person from db.

    Args:
        id (int): person id.
    """
    person = _return_person_if_exists(id)
    person.delete_instance()
    return person


def _check_if_already_exists(surname: str, name: Optional[str] = None) -> None:
    if People.get_or_none(People.name == name and People.surname == surname):
        sys.exit("Person already exists.")


def _return_person_if_exists(id: int) -> People:
    person: People = People.get_or_none(
        People.id == id
    )
    if not person:
        sys.exit("Person does not exists.")
    return person
