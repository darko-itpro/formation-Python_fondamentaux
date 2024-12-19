import pytest
from exos.pyflix.mediatheque import TvShow

def test_tvshow_creation():
    myshow = TvShow('Arcane')
    assert myshow.name == "Arcane"
    assert len(myshow.episodes) == 0

@pytest.fixture
def show_without_episodes():
    return TvShow('Arcane')

@pytest.fixture
def show_with_3_episodes(show_without_episodes):
    show_without_episodes.add_episode("title1", 1, 1)
    show_without_episodes.add_episode("title2", 1, 2)
    show_without_episodes.add_episode("title3", 2, 2)

    return show_without_episodes


def test_add_first_episode(show_without_episodes):
    myshow = show_without_episodes
    myshow.add_episode("Title", 1, 1)
    assert len(myshow.episodes) == 1

def test_add_first_episode_with_all_data(show_without_episodes):
    myshow = show_without_episodes
    myshow.add_episode("Title", 1, 1, 67, 1899)
    assert len(myshow.episodes) == 1

def test_duplicate_episode_must_raise(show_with_3_episodes):
    myshow = show_with_3_episodes

    myshow.add_episode("test dup", 4, 4)
    with pytest.raises(ValueError):
        myshow.add_episode("test dup", 4, 4)