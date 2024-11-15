import pytest
from exos_correction.base.exo_lists import episodes_duration

def test_negative_duration_must_raise():
    with pytest.raises(ValueError):
        episodes_duration([], -2)
