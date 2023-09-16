from datetime import date

import pytest

from people.db import queries
from people.utils import dates, presenter


class TestDates:
    # noinspection PyTypeChecker
    def test_get_date_diff(self):
        assert dates.get_date_diff(date.today()) == 0

    @pytest.mark.parametrize(
        "inputted_date, result",
        [("14.05.2023", date(2023, 5, 14)), ("01.01.2023", date(2023, 1, 1))],
    )
    def test_date_formatter(self, inputted_date, result):
        assert dates.date_formatter(inputted_date) == result


class TestPresenter:
    @pytest.mark.parametrize(
        "surname, name, last_contact, expected",
        [
            ("surname", "name", "11.11.2011", [["1", "surname name", "11.11.2011"]]),
            ("surname", None, "01.01.1970", [["1", "surname", "01.01.1970"]]),
            (
                "surname",
                "name",
                date.today(),
                [["1", "surname name", str(date.today())]],
            ),
        ],
    )
    def test_set_in_rows_without_diff(
        self, test_db, surname, name, last_contact, expected
    ):
        people = queries.add_person_to_db(surname, name, last_contact)
        assert presenter.set_in_rows_without_diff([people]) == expected

    # noinspection PyTypeChecker
    @pytest.mark.parametrize(
        "surname, name, last_contact, expected",
        [
            (
                "surname",
                "name",
                date.today(),
                [["1", "surname name", str(date.today()), "0"]],
            )
        ],
    )
    def test_set_in_rows_with_diff(
        self, test_db, surname, name, last_contact, expected
    ):
        people = queries.add_person_to_db(surname, name, last_contact)
        assert presenter.set_in_rows_with_diff([people]) == expected

    @pytest.mark.parametrize(
        "surname, name, expected",
        [("surname", "name", "surname name"), ("surname", None, "surname")],
    )
    def test_set_full_name(self, test_db, surname, name, expected):
        people = queries.add_person_to_db(surname, name)
        assert presenter._set_full_name(people) == expected
