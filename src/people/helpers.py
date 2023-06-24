from peewee import CharField, DateField
from .__main__ import SHORT_TABLE_HEADER, TABLE_HEADER
from .models import People
from typing import List, Union, Optional
from datetime import date
from .utils.data_formatter import set_in_rows
from .utils.dates import date_formatter
from .utils.table import print_table


def list_people(sort_by: str) -> None:
    if sort_by == "surname":
        order: CharField = People.surname  # type: ignore
    elif sort_by == "days":
        order: DateField = People.last_contact  # type: ignore
    people: List[List[Union[str, DateField]]] = set_in_rows(
        People.select().order_by(order)  # type: ignore
    )
    print_table(TABLE_HEADER, people)


def add(
    surname: str,
    name: Optional[str],
    last_contact: str = str(date.today()),
) -> None:
    last_contact_date: date = date_formatter(last_contact)
    if name:
        person: People = People.create(
            name=name, surname=surname, last_contact=last_contact_date
        )
    else:
        person = People.create(surname=surname, last_contact=last_contact_date)
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)


def remove(name: str, surname: str) -> None:
    People.get(People.name == name and People.surname == surname).delete_instance()


def contact(name: str, surname: str) -> None:
    person: People = People.get(People.name == name and People.surname == surname)
    person.last_contact = date.today()  # type: ignore
    person.save()
    people: List[List[Union[str, DateField]]] = set_in_rows([person], passed_days=False)
    print_table(SHORT_TABLE_HEADER, people)
