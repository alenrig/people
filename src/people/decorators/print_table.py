"""Module for print table wrapper."""
from ..configs import SHORT_TABLE_HEADER, TABLE_HEADER
from ..utils.table import print_table


def print_table_wrapper(func):
    """Print pretty table after comand execution.

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
