import pytest
from exos_correction.pyflix.mediatheque import TvShow

def test_tvshow_create():
    show = TvShow("Dr. who")
    assert show.name == "Dr. Who"
    assert len(show.episodes) == 0

@pytest.fixture
def empty_show():
    return TvShow("Dr. Who")

def test_add_one_episode(empty_show):
    show = empty_show
    show.add_episode("Rose", 1, 1, 51, 2006)
    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Rose"

@pytest.fixture
def show_with_3_episodes(empty_show):
    show = empty_show
    show.add_episode("Rose", 1, 1, 51, 2006)
    show.add_episode("Daleks", 2, 1, 51, 2006)
    show.add_episode("Gallifrey", 3, 2, 51, 2006)
    return show

def test_duplicate_episode_must_raise(show_with_3_episodes):
    show = show_with_3_episodes
    with pytest.raises(ValueError):
        show.add_episode("Rose", 1, 1, 51, 2006)
