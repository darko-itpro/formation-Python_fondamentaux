import pytest
from exos.base.episode_utils import is_viewed

def test_episode_viewed():
    episode_viewed = ["The new Project", 1, 98, True]
    assert is_viewed(episode_viewed) is True


def test_episode_not_viewed():
    episode_not_viewed = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode_not_viewed) is False

def test_episode_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, 7]
    assert is_viewed(episode) is True

def test_episode_not_viewed_as_count():
    episode = ['Installing the softwares', 2, 42, 0]
    assert is_viewed(episode) is False

def test_episode_without_viewed():
    episode = ['Installing the softwares', 2, 42]
    assert is_viewed(episode) is False

