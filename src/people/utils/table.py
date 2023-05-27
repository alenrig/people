from prettytable import PrettyTable


class TableCreationError(Exception):

    def __str__(self) -> str:
        return "Несоответствие количества заголовков и столбцов данных."


def print_table(header, data) -> None:
    _check_args(header, data)
    table = _create_table(header, data)
    print(table)


def _check_args(header, data):
    try:
        assert len(header) == len(data)
    except AssertionError:
        TableCreationError


def _create_table(header, data) -> PrettyTable:
    table = PrettyTable()
    table.field_names = header
    table.add_rows(data)
    return table
