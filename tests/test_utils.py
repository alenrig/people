from people.utils.dates import get_date_diff
from datetime import date
from dateutil import parser
import pytest


class TestDates:

    def test_get_date_diff(self):
        assert get_date_diff(date.today()) == 0
