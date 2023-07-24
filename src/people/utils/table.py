"""Module for print data in pretty table."""
from typing import List

from prettytable import PrettyTable

from ..configs import SHORT_TABLE_HEADER, TABLE_HEADER


def print_table(header: List[str], data: List[List[str]]) -> None:
    """Print data in pretty table.

    Args:
        header (List[str]): table headers;
        data (List[List[str]]): list with lists of table rows.
    """
    table = _create_table(header, data)
    print(table)


def _create_table(header: List[str], data: List[List[str]]) -> PrettyTable:
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


def print_table_wrapper(func):
    """Print pretty table after command execution.

    Args:
        func (__func__): command of people cli to run.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            print_table(TABLE_HEADER, result)
        except (AssertionError, ValueError):
            print_table(SHORT_TABLE_HEADER, result)

    return wrapper
