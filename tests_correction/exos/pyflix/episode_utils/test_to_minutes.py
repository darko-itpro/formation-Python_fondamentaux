from exos_correction.pyflix.episode_utils import to_minutes


def test_some_hours():
    assert to_minutes(3) == 180

def test_zero_hours():
    assert to_minutes(0) == 0

def test_hours_as_str():
    assert to_minutes('4') == 240

def test_with_minutes():
    assert to_minutes(3, 12) == 192

def test_with_minutes_as_str():
    assert to_minutes(3, '12') == 192
