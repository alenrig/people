"""Reformat data for table usages."""
from typing import List, Union

from peewee import CharField, DateField

from ..models import People
from .dates import get_date_diff


def set_in_rows(
    persons: List[People], passed_days: bool = True
) -> List[List[Union[str, DateField]]]:
    """Format persons data in table rows.

    Args:
        persons (List[People]): list of people to format;
        passed_days (bool, optional): add passed days tile. Defaults to True.

    Returns:
        List[List[str]]: list of rows for PrettyTable
    """
    if passed_days:
        return [
            [
                _set_full_name(person.name, person.last_name),
                person.last_contact,
                str(get_date_diff(person.last_contact)),
            ]
            for person in persons
        ]
    return [
        [_set_full_name(person.name, person.last_name), person.last_contact]
        for person in persons
    ]


def _set_full_name(name: CharField, last_name: CharField) -> str:
    return f'{last_name} {name if name is not None else ""}'.strip()
