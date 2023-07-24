"""Reformat data for table usages."""
from typing import List

from ..db.models import People
from .dates import get_date_diff


def set_in_rows(persons: List[People], passed_days: bool = True) -> List[List[str]]:
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
                str(person.last_contact),
                str(get_date_diff(person.last_contact)),
            ]
            for person in persons
        ]
    return [
        [_set_full_name(person.surname, person.name), str(person.last_contact)]
        for person in persons
    ]


def set_in_rows_with_diff(persons: List[People]) -> List[List[str]]:
    return [
        [
            _set_full_name(person),
            str(person.last_contact),
            str(get_date_diff(person.last_contact)),
        ]
        for person in persons
    ]


def set_in_rows_without_diff(persons: List[People]) -> List[List[str]]:
    return [[_set_full_name(person), str(person.last_contact)] for person in persons]


def _set_full_name(person: People) -> str:
    return f"{person.surname} {person.name if person.name is not None else ''}".strip()
