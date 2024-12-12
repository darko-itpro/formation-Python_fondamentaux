import pytest
from exo_corrections.pyflix.mediatheque import TvShow, Episode

def test_create_show():
    show = TvShow('arcane')
    assert len(show.episodes) == 0
    assert show.name == "Arcane"

@pytest.fixture
def empty_tvshow():
    return TvShow('Arcane')

def test_add_first_episode(empty_tvshow):
    empty_tvshow.add_episode("title", 1, 2)
    assert len(empty_tvshow.episodes) == 1

@pytest.fixture
def show_3_episodes(empty_tvshow):
    empty_tvshow.add_episode("title 1", 1, 1, 24)
    empty_tvshow.add_episode("title 2", 1, 2, 24)
    empty_tvshow.add_episode("title 3", 2, 1, 24)
    return empty_tvshow

def test_duplicate_episode_must_raise(show_3_episodes):
    show_3_episodes.add_episode("new title", 2, 3)
    with pytest.raises(ValueError):
        show_3_episodes.add_episode("new title", 2, 3)

def test_episodes_are_equal():
    ep1 = Episode("title", 1, 2)
    ep2 = Episode("title", 1, 2)
    assert ep1 == ep2