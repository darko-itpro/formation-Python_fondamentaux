import pytest
from pip._internal.commands import show

from exos.pyflix.mediatheque import TvShow

def test_create_show():
    show = TvShow("my show")
    assert show.name == "my show"
    assert len(show.episodes) == 0

def test_add_one_episode():
    show = TvShow("my show")
    show.add_episode("title", 1, 1)

    assert len(show.episodes) == 1
    assert show.episodes[0].title == "title"

def test_duplicate_episode_must_raise():
    show = TvShow("my show")
    show.add_episode("title", 1, 1)

    with pytest.raises(ValueError):
        show.add_episode("title", 1, 1)