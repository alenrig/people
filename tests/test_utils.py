from datetime import date

import pytest

from people.utils import dates
from people.utils import data_formatter
from people.db import queries


class TestDates:

    def test_get_date_diff(self):
        assert dates.get_date_diff(date.today()) == 0

    @pytest.mark.parametrize(
        "inputted_date, result",
        [
            ("14.05.2023", date(2023, 5, 14)),
            ("01.01.2023", date(2023, 1, 1))
        ]
    )
    def test_date_formatter(self, inputted_date, result):
        assert dates.date_formatter(inputted_date) == result


class TestDataFormatter:
    
    @pytest.mark.parametrize(
        "surname, name, last_contact, passed_days, expected",
        [
            ("surname", "name", "11.11.2011", False, [['surname name', '11.11.2011']]),
            ("surname", None, "01.01.1970", False, [['surname', '01.01.1970']]),
            ("surname", "name", date.today(), False, [["surname name", str(date.today())]]),
            ("surname", "name", date.today(), True, [["surname name", str(date.today()), '0']])
        ]
    )
    def test_set_in_rows(self, test_db, surname, name, last_contact, passed_days, expected):
        people = queries.add_person_to_db(surname, name, last_contact)
        assert data_formatter.set_in_rows([people], passed_days=passed_days) == expected


    @pytest.mark.parametrize(
        "surname, name, expected",
        [
            ("surname", "name", "surname name"),
            ("surname", None, "surname")
        ]
    )
    def test_set_full_name(self, surname, name, expected):
        assert data_formatter._set_full_name(surname, name) == expected
