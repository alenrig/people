from datetime import date

import pytest

from people.utils import dates
from people.utils import date_formatter


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
    
    def test_set_in_rows(self, test_db):
        pass

    @pytest.mark.parametrize(
        "surname, name, expected",
        [
            ("surname", "name", "surname name"),
            ("surname", None, "surname")
        ]
    )
    def test_set_full_name(self, surname, name, expected):
        assert date_formatter._set_full_name(surname, name) == expected
