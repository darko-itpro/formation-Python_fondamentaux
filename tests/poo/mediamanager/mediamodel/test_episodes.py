#!/usr/bin/env python 

from training.projects.mediamanager import mediamodel as media
import pytest


def test_episode_creation_with_all_fields():
    episode = media.Episode("First", 1, 2)
    assert episode.title == "First"
    assert episode.number == 1
    assert episode.season_number == 2


def test_episode_number_should_be_positive():
    with pytest.raises(ValueError) as e:
        media.Episode("First Episode", -1, 2)

    assert e.match("Episode number")  # Test que le message correspond à l'erreur attendue


def test_episode_season_should_be_positive():
    with pytest.raises(ValueError) as e:
        media.Episode("First Episode", 1, -1)

    assert e.match("Episode season number")  # Test que le message correspond à l'erreur attendue


def test_type_for_number_should_be_a_number():
    with pytest.raises(TypeError):
        media.Episode("First", "1", 1)


def test_type_for_season_number_should_be_a_number():
    with pytest.raises(TypeError):
        media.Episode("First", 1, "1")



def test_episode_should_be_immuable():
    episode = media.Episode("First", 1, 2)
    with pytest.raises(AttributeError):
        episode.title = "new title"
    with pytest.raises(AttributeError):
        episode.number = 2
    with pytest.raises(AttributeError):
        episode.title = 1


def test_how_episodes_should_be_equals():
    first_episode = media.Episode("First", 1, 2)
    other_first_episode = media.Episode("Other", 1, 2)
    assert first_episode == other_first_episode

    assert first_episode != 1
