import pytest

from pyflix.mediatheque import TvShow, Episode

def test_tvshow_creation():
    tv = TvShow("Les 100")
    assert tv.name == "Les 100"
    assert len(tv.episodes) == 0

def test_add_first_episode():
    tv = TvShow("Les 100")

    tv.add_episode("First", 2, 1, 90, 2005)

    assert len(tv.episodes) == 1

def test_duplicate_episode_must_raise():
    tv = TvShow("Les 100")

    tv.add_episode("First", 2, 1, 90, 2005)
    with pytest.raises(ValueError):
        tv.add_episode("First", 2, 1, 90, 2005)

def test_episodes_are_equal():
    ep1 = Episode("First", 2, 1, 90, 2005)
    ep2 = Episode("First", 2, 1, 90, 2005)

    assert ep1 == ep2