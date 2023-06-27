from people.db.queries import add_person_to_db, delete_person_from_db
import pytest

@pytest.mark.parametrize(
    "surname, name, last_contact_date, expected",
    [
        ("surname1", "name1", "27.06.2023", ("surname1", "name1", "27.06.2023")),
        ("surname2", "name2", "11.11.2011", ("surname2", "name2", "11.11.2011"))
    ]
)
def test_add_person_to_db(test_db, surname, name, last_contact_date, expected):
    result = add_person_to_db(surname, name, last_contact_date)
    assert result.surname == expected[0]
