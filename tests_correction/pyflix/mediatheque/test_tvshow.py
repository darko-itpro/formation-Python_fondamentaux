import pytest

from exos_correction.pyflix.mediatheque import TvShow

def test_create_new_show():
    show = TvShow("green arrow")
    assert len(show.episodes) == 0
    assert show.name == 'Green Arrow'

@pytest.fixture
def empty_show():
    return TvShow('green arrow')

@pytest.fixture
def show_with_3_episodes(empty_show):
    show = empty_show
    show.add_episode("The isle", 1, 1)
    show.add_episode("The isle", 2, 1)
    show.add_episode("The isle", 1, 2)

    return show

def test_add_first_episode(empty_show):
    empty_show.add_episode("The isle", 1, 1)
    assert len(empty_show.episodes) == 1

def test_add_duplicate_episode(show_with_3_episodes):
    show = show_with_3_episodes
    with pytest.raises(ValueError):
        show.add_episode("The isle", 1, 2)
