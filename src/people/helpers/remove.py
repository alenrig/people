from ..models import People


def remove(name: str, surname: str) -> None:
    People.get(People.name == name and People.surname == surname).delete_instance()
