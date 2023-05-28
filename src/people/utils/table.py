"""Module for print data in pretty table."""
from typing import List

from prettytable import PrettyTable


class TableCreationError(Exception):
    """Exception for wrong header and data lengths"""

    def __str__(self) -> str:
        return "Несоответствие количества заголовков и столбцов данных."


def print_table(header: List[str], data: List[List[str]]) -> None:
    """Print data in pretty table.

    Args:
        header (List[str]): table headers;
        data (List[List[str]]): list with lists of table rows.
    """
    _check_args(header, data)
    table = _create_table(header, data)
    print(table)


def _check_args(header: List[str], data: List[List[str]]) -> None:
    """Check inputs for table creation.

    Args:
        header (List[str]): table headers;
        data (List[List[str]]): list with lists of table rows.

    Raises:
        TableCreationError
    """
    try:
        assert len(header) == len(data)
    except AssertionError as exc:
        raise TableCreationError from exc


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
