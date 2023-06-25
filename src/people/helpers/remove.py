from ..db.models import People
from ..db.queries import delete_person_from_db
from typing import Optional


def remove(surname: str, name: Optional[str]) -> None:
    delete_person_from_db(surname, name)
