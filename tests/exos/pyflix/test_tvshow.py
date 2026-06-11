import pytest
from exos.pyflix.mediatheque import TvShow, Episode, DuplicateEpisodeError

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

def test_duplicate_must_raise(show):
    show.add_episode("Grand Line", 1, 1)
    with pytest.raises(DuplicateEpisodeError):
        show.add_episode("Grand Line", 1, 1)

def test_episodes_are_equal(show):
    ep1 = Episode("Grand Line", 1, 1)
    ep2 = Episode("Grand Line", 1, 1)
    assert ep1 == ep2