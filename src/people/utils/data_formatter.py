"""Reformat data for table usages."""
from typing import List

from ..db.models import People
from .dates import get_date_diff


def set_in_rows_with_diff(persons: List[People]) -> List[List[str]]:
    """Format persons data in table rows with date diff.

    Args:
        persons (List[People]): list of people to format;

    Returns:
        List[List[str]]: list of rows for PrettyTable
    """
    return [
        [
            _set_full_name(person),
            str(person.last_contact),
            str(get_date_diff(person.last_contact)),
        ]
        for person in persons
    ]


def set_in_rows_without_diff(persons: List[People]) -> List[List[str]]:
    """Format persons data in table rows without date diff.

    Args:
        persons (List[People]): list of people to format;

    Returns:
        List[List[str]]: list of rows for PrettyTable
    """
    return [[_set_full_name(person), str(person.last_contact)] for person in persons]


def _set_full_name(person: People) -> str:
    return f"{person.surname} {person.name if person.name is not None else ''}".strip()
