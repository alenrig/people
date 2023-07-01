"""Reformat data for table usages."""
from typing import List, Optional, Union

from peewee import DateField

from ..db.models import People
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
                _set_full_name(person.surname, person.name),
                person.last_contact,
                str(get_date_diff(person.last_contact)),
            ]
            for person in persons
        ]
    return [
        [_set_full_name(person.surname, person.name), person.last_contact]
        for person in persons
    ]


def _set_full_name(surname: str, name: Optional[str]) -> str:
    return f'{surname} {name if name is not None else ""}'.strip()
