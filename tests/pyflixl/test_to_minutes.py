import pytest
from exos_corrections.pyflixl import to_minutes

def test_basic_convert():
    value = 5
    expected = 300

    assert to_minutes(value) == expected

def test_hours_as_str():
    value = "20"
    expected = 1200

    assert to_minutes(value) == expected

def test_hours_and_minutes():
    hours = 2
    minutes = 24

    assert to_minutes(hours, minutes) == 144

def test_hours_and_minutes_as_str():
    hours = 2
    minutes = "24"

    assert to_minutes(hours, minutes) == 144

def test_negative_values_must_raise():
    hours = -2
    minutes = "24"

    with pytest.raises(ValueError):
        to_minutes(hours, minutes)
