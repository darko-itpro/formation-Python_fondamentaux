import pytest

from exo_corrections.base.episodes_utils import to_minutes

def test_to_minutes():
    assert to_minutes(2) == 120

def test_hours_as_str_to_minutes():
    assert to_minutes("2") == 120

def test_with_minutes():
    assert to_minutes(2, 14) == 134

def test_with_minutes_as_str():
    assert to_minutes(2, "14") == 134

def test_negative_hours_must_raise():

    with pytest.raises(ValueError):
        to_minutes(-1)
