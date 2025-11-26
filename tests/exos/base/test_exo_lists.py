import pytest
from exos.base.exo_lists import duration_for

def test_duration_for_empty_colletion():
    assert duration_for([], 3) == 0


def test_duration_for_some_colletion():
    medias = ["first", "second", "third"]
    assert duration_for(medias, 10) == 30
