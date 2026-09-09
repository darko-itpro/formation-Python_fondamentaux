from pyflix.media_utils import is_viewed

def test_is_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode) is True

def test_is_not_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode) is False

def test_is_viewed_as_count():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": 4}
    assert is_viewed(episode) is True

def test_is_not_viewed_as_count():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}
    assert is_viewed(episode) is False

def test_is_not_viewed_without_viewed():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "year": 2025}
    assert is_viewed(episode) is False
