import pytest
from exos_correction.media_utils import to_minutes

def test_to_minutes_with_hours():
    assert to_minutes(2) == 120

def test_to_monutes_0_hour():
    assert to_minutes(0) == 0

def test_to_minutes_with_hours_as_str():
    assert to_minutes('2') == 120

def test_to_minutes_with_hours_and_minutes():
    assert to_minutes(2, 14) == 134

def test_to_minutes_with_hours_and_minutes_as_str():
    assert to_minutes('2', '14') == 134

def test_to_minutes_str_hours_must_be_numbers():
    with pytest.raises(ValueError):
        to_minutes("cinq")
