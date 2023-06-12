from people.utils import dates 
from datetime import date
from dateutil import parser
import pytest


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
