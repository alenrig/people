"""Reformat data for table usages."""
from ..models import People
from .dates import get_date_diff
from typing import List


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
                f"{person.first_name} {person.last_name}",
                person.last_contact,
                str(get_date_diff(person.last_contact)),
            ]
            for person in persons
        ]
    return [
        [f"{person.first_name} {person.last_name}", person.last_contact]
        for person in persons
    ]
