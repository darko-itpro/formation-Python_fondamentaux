import pytest
from exos.pyflix.mediatheque import TvShow

def test_create_tvshow():
    tv = TvShow("My Show")

    assert tv.title == "My Show"
    assert len(tv.episodes) == 0






@pytest.fixture
def tvshow():
    return TvShow("My Show")

@pytest.fixture
def add_one_episode(tvshow):
    tvshow.add_episode("title 1", 1, 1)

@pytest.fixture
def add_three_episode(tvshow):
    tvshow.add_episode("title 1", 1, 1)
    tvshow.add_episode("title 2", 1, 2)
    tvshow.add_episode("title 3", 2, 1)


def test_add_first_episode(tvshow):
    tvshow.add_episode("title 1", 1, 1)
    assert len(tvshow.episodes) == 1
    assert tvshow.episodes[0].title == "title 1"


def test_add_second_episode(tvshow, add_one_episode):
    tvshow.add_episode("title other", 2, 2)
    assert len(tvshow.episodes) == 2


def test_duplicate_episode_must_raise(tvshow):
    tvshow.add_episode("title 1", 1, 1)
    with pytest.raises(ValueError):
        tvshow.add_episode("title 1", 1, 1)

