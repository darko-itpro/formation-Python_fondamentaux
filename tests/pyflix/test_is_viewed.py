import pytest
from pyflix.media_utils import is_viewed

test_data = [
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": True}, True),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 5}, True),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": False}, False),
    ({"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}, False),
    ({"title": "The Conjugal Configuration", "duration": 20}, False),
    ({"title": "The Conjugal Configuration", "duration": 20, "year":2018}, False),
]

# Test paramétré

@pytest.mark.parametrize("episode, expected", test_data)
def test_is_viewed(episode, expected):
    assert is_viewed(episode) is expected





# Manière de faire de base
def test_is_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode) is True

def test_is_viewed_as_int():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": 5}
    assert is_viewed(episode) is True


def test_is_not_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode) is False

def test_is_not_viewed_as_int():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}
    assert is_viewed(episode) is False

def test_is_not_viewed_without_viewed():
    episode = {"title": "The Conjugal Configuration", "duration": 20}
    assert is_viewed(episode) is False

def test_is_not_viewed_without_viewed_with_year():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "year":2018}
    assert is_viewed(episode) is False