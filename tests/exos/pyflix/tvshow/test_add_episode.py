import pytest

from exos.pyflix.mediatheque import TvShow


@pytest.fixture
def tvshow():
    return TvShow("Dr. Who")


@pytest.fixture
def episode_as_list():
    return ["Rose", 1, 1]


@pytest.fixture
def show_with_3_episodes(tvshow, episode_as_list):
    tvshow.add_episode(*episode_as_list)
    tvshow.add_episode("Daleks", 1, 2)
    tvshow.add_episode("New Earth", 2, 3)


def test_add_first_episode(tvshow):
    tvshow.add_episode("Rose", 1, 1)
    assert len(tvshow.episodes) == 1
    assert tvshow.episodes[0].title == "Rose"


def test_add_second_episode(tvshow):
    tvshow.add_episode("Rose", 1, 1)
    tvshow.add_episode("Daleks", 1, 2)
    assert len(tvshow.episodes) == 2
    assert tvshow.episodes[0].title == "Rose"
    assert tvshow.episodes[1].title == "Daleks"

def test_duplicate_episode(tvshow, episode_as_list, show_with_3_episodes):
    with pytest.raises(ValueError):
        tvshow.add_episode(*episode_as_list)
