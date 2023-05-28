import pytest
from people.utils import table

@pytest.mark.parametrize(
        "header, data",
        [
            (1,2),
            ("a", "b")
        ] 
)
def test_check_table_args(header, data):
    assert table._check_args(header, data) == 2
