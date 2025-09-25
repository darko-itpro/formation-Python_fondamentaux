import pytest

from exos.pyflix.mediatheque import TvShow

def test_new_show_name():
    show = TvShow("Title")
    assert show.name == "Title"

def test_new_show_have_empty_episodes_list():
    show = TvShow("Title")
    assert len(show.episodes) == 0
