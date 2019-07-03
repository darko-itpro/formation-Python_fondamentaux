#!/usr/bin/env python

from training.projects.mediamanager import mediamodel as media
import pytest


def test_create_empty_tvshow():
    my_show = media.TvShow("my show")
    assert my_show.name == "my show"
    assert len(my_show.get_episodes()) == 0
    assert len(my_show.episodes) == 0


@pytest.fixture()
def empty_show():
    return media.TvShow("My Show")


@pytest.fixture()
def show_with_few_episodes_same_season():
    my_show = media.TvShow("My Show")
    my_show.add_episode("First", 1, 1)
    my_show.add_episode("Second", 2, 1)
    my_show.add_episode("Fifth", 5, 1)


def test_add_one_episode(empty_show):
    empty_show.add_episode("episode", 1, 1)
    assert len(empty_show.episodes) == 1


def test_add_several_episodes(empty_show):
    empty_show.add_episode("episode 1", 1, 1)
    empty_show.add_episode("episode 2", 2, 1)
    empty_show.add_episode("episode 3", 3, 1)
    empty_show.add_episode("episode 4", 4, 1)
    empty_show.add_episode("episode 5", 5, 1)
    assert len(empty_show.episodes) == 5


def test_cannot_add_duplicate(empty_show):
    empty_show.add_episode("episode 1", 1, 1)
    empty_show.add_episode("episode 2", 2, 1)
    empty_show.add_episode("episode 3", 3, 1)

    with pytest.raises(ValueError):
        empty_show.add_episode("Duplicate", 2, 1)

