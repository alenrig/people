"""Module for print data in pretty table."""
from typing import List, Union

from peewee import DateField
from prettytable import PrettyTable


def print_table(header: List[str], data: List[List[Union[str, DateField]]]) -> None:
    """Print data in pretty table.

    Args:
        header (List[str]): table headers;
        data (List[List[str]]): list with lists of table rows.
    """
    table = _create_table(header, data)
    print(table)


def _create_table(
    header: List[str], data: List[List[Union[str, DateField]]]
) -> PrettyTable:
    """Create PrettyTable object.

    Args:
        header (List[str]): table headers;
        data (List[List[str]]): list with lists of table rows.

    Returns:
        PrettyTable
    """
    table = PrettyTable()
    table.field_names = header
    table.add_rows(data)
    return table
