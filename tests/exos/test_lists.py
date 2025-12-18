import pytest
from exos.base.exo_lists import duration

def test_duration_of_season():
    season = ["first", "second", "third"]
    season_duration = duration(season, 10)
    assert season_duration == 30

def test_negative_duration_must_raise():
    with pytest.raises(ValueError):
        duration([], -1)
