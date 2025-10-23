import pytest
from exos.pyflix.mediatheque import TvShow

def test_new_show():
    show = TvShow("Dr. who")
    assert show.name == "Dr. Who"
    assert show.episodes == []

@pytest.fixture
def show():
    return TvShow("Dr. Who")

def test_add_one_episode(show):
    show.add_episode("Rose", 1, 1)
    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Rose"

def test_add_one_episode_with_duration(show):
    show.add_episode("Rose", 1, 1, 54)
    assert len(show.episodes) == 1
    assert show.episodes[0].duration == 54

def test_add_one_episode_with_year(show):
    show.add_episode("Rose", 1, 1, 54, 2006)
    assert len(show.episodes) == 1
    assert show.episodes[0].year == 2006

def test_duplicate_episode_must_raise(show):
    show.add_episode("Rose", 1, 1, 54, 2006)
    with pytest.raises(ValueError):
        show.add_episode("Rose", 1, 1, 54, 2006)
