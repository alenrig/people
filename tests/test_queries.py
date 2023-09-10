from people.db.queries import add_person_to_db, delete_person_from_db, get_person_from_db, update_last_contact_date
from datetime import date
import pytest


@pytest.mark.parametrize(
    "surname, name, last_contact_date, expected",
    [
        ("surname", "name", "27.06.2023", ("surname", "name", "27.06.2023")),
        ("surname", None, "11.11.2011", ("surname", None, "11.11.2011")),
    ]
)
def test_add_person_to_db_with_dates(test_db, surname, name, last_contact_date, expected):
    result = add_person_to_db(surname, name, last_contact_date)
    assert result.surname == expected[0]
    assert result.name == expected[1]
    assert result.last_contact == expected[2]


@pytest.mark.parametrize(
    "surname, name, expected",
    [
        ("surname", "name", ("surname", "name", str(date.today())))
    ]
)
def test_add_person_to_db(test_db, surname, name, expected):
    person = add_person_to_db(surname, name)
    assert person.surname == expected[0]
    assert person.name == expected[1]
    assert person.last_contact == expected[2]


@pytest.mark.parametrize(
    "surname, name",
    [
        ("surname1", "name1"),
    ]
)
def test_reading_person_to_db(test_db, surname, name):
    add_person_to_db(surname, name)
    with pytest.raises(SystemExit):
        add_person_to_db(surname, name)


@pytest.mark.parametrize(
    "surname, name",
    [
        ("surname1", "name1"),
        ("surname2", None),
    ]
)
def test_delete_person_from_db(test_db, surname, name):
    add_person_to_db(surname, name)
    delete_person_from_db(1)
    with pytest.raises(SystemExit):
        delete_person_from_db(1)


@pytest.mark.parametrize(
    "surname, name, expected",
    [
        ("surname1", "name1", ("surname1", "name1")),
        ("surname2", None, ("surname2", None))
    ]
)
def test_get_person_from_db(test_db, surname, name, expected):
    add_person_to_db(surname, name)
    result = get_person_from_db(1)
    assert result.surname == expected[0]
    assert result.name == expected[1]


def test_get_non_existing_person(test_db):
    with pytest.raises(SystemExit):
        get_person_from_db(1)


@pytest.mark.parametrize(
    "surname, name, last_contact_date, contact_date, expected",
    [
        ("surname", "name", "27.06.2023", date.today(), date.today()),
        ("surname", None, "11.11.2011", date.today(), date.today()),
        ("surname", "name", "01.01.1970", "02.01.1970", "02.01.1970")
    ]
)
def test_update_last_contact_date(test_db, surname, name, last_contact_date, contact_date, expected):
    add_person_to_db(surname, name, last_contact_date)
    result = update_last_contact_date(1, contact_date)
    assert result.last_contact == expected
