from typing import Optional

from ..db.queries import delete_person_from_db


def remove(surname: str, name: Optional[str]) -> None:
    delete_person_from_db(surname, name)
