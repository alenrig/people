"""Remove from storage command helper."""
from typing import List, Optional, Union

from peewee import DateField

from ..db.queries import delete_person_from_db
from ..decorators.print_table import print_table_wrapper
from ..utils.data_formatter import set_in_rows


@print_table_wrapper
def remove(surname: str, name: Optional[str]) -> List[List[Union[str, DateField]]]:
    """Remove person from storage.

    Args:
        surname (str): person surname.
        name (Optional[str]): person name.
    """
    person = delete_person_from_db(surname, name)
    return set_in_rows([person])
