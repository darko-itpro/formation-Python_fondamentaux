import pytest
from exos_correction.pyflix.episode_utils import to_minutes

def test_to_minutes_0_hours():
    assert to_minutes(0) == 0

def test_to_minutes_some_hours():
    assert to_minutes(3) == 180

def test_to_minutes_as_str():
    assert to_minutes("3") == 180

def test_to_minutes_with_hours():
    assert to_minutes(3, 12) == 192

def test_negative_hours_must_raise():
    with pytest.raises(ValueError):
        to_minutes(-3)
