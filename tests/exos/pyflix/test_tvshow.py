import pytest
from exos.pyflix.mediatheque import TvShow

def test_create_show():
    show = TvShow('One Piece')

    assert show.name == "One Piece"
    assert show.episodes == []

@pytest.fixture
def show():
    return TvShow('One Piece')

def test_add_one_episode(show):
    show.add_episode("Grand Line", 2, 1)
    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Grand Line"

def test_add_several_episodes(show):
    show.add_episode("Gold Rodgers", 1, 1)
    show.add_episode("Grand Line", 2, 1)
    assert len(show.episodes) == 2
    assert show.episodes[1].title == "Grand Line"
