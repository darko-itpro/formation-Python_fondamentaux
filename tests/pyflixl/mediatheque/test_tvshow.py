import pytest
from exos.pyflix2.mediatheque import TvShow

def test_show_creation():
    show = TvShow("rings of power")
    assert show.name == "Rings Of Power"
    assert len(show.episodes) == 0

@pytest.fixture
def empty_show():
    return TvShow("Rings of Power")

@pytest.fixture
def show_with_3_episodes(empty_show):
    empty_show.add_episode("Galadriel", 1, 1)
    empty_show.add_episode("The Stranger", 2, 1)
    empty_show.add_episode("More Rings", 1, 2)
    return empty_show

def test_add_first_episode(empty_show):
    empty_show.add_episode("Galadriel", 1, 1)
    assert len(empty_show.episodes) == 1
    assert empty_show.episodes[0].title == "Galadriel"

def test_add_to_show_with_episodes(show_with_3_episodes):
    show_with_3_episodes.add_episode("Khazad Dum", 2, 2)
    assert len(show_with_3_episodes.episodes) == 4

def test_duplicate_episode_must_raise(show_with_3_episodes):
    with pytest.raises(ValueError):
        show_with_3_episodes.add_episode("More rings", 1, 2)
