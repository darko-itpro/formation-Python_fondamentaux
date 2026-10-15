import pytest
from pyflix.mediatheque import TvShow

def test_create_show():
    show = TvShow("One Piece")
    assert show.name == 'One Piece'
    assert show.episodes == []
    
@pytest.fixture
def show():
    return TvShow("One Piece")

def test_add_first_episode(show):
    show.add_episode("Grand Line", 2, 1)
    assert len(show.episodes) == 1

def test_duplicate_episode_must_raise(show):
    show.add_episode("Grand Line", 2, 1)
    with pytest.raises(ValueError):
        show.add_episode("Grand Line", 2, 1)