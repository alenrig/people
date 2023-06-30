from people.db.queries import add_person_to_db, delete_person_from_db, get_person_from_db
import pytest

@pytest.mark.parametrize(
    "surname, name, last_contact_date, expected",
    [
        ("surname1", "name1", "27.06.2023", ("surname1", "name1", "27.06.2023")),
        ("surname2", None, "11.11.2011", ("surname2", None, "11.11.2011"))
    ]
)
def test_add_person_to_db(test_db, surname, name, last_contact_date, expected):
    result = add_person_to_db(surname, name, last_contact_date)
    assert result.surname == expected[0]
    assert result.name == expected[1]
    assert result.last_contact == expected[2]


@pytest.mark.parametrize(
    "surname, name",
    [
        ("surname1", "name1"),
    ]
)
def test_readding_person_to_db(test_db, surname, name):
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
    delete_person_from_db(surname, name)
    with pytest.raises(SystemExit):
        delete_person_from_db(surname, name)

@pytest.mark.parametrize(
    "surname, name, expected",
    [
        ("surname1", "name1", ("surname1", "name1")),
        ("surname2", None, ("surname2", None))
    ]
)
def test_get_person_from_db(test_db, surname, name, expected):
    add_person_to_db(surname, name)
    result = get_person_from_db(surname, name)
    assert result.surname == expected[0]
    assert result.name == expected[1]


def test_get_nonexisting_person(test_db):
    with pytest.raises(SystemExit):
        get_person_from_db("surname", "name")
