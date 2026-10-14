import pytest
from exos.exo_list import episodes_duration

def test_negative_value_must_raise():
    with pytest.raises(ValueError):
        episodes_duration([], -1)
