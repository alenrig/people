import pytest
from people.utils import table

@pytest.mark.parametrize(
        "header, data",
        [
            (["col1", "col2"], [["b"]])
        ] 
)
def test_check_table_args_exception(header, data):
    with pytest.raises(table.TableCreationError):
        table._check_args(header, data)
