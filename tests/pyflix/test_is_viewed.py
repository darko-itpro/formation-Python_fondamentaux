from exos_correction.pyflix.episode_utils import is_viewed

def test_episode_viewed():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode) is True

def test_episode_not_viewed():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode) is False

def test_episode_not_viewed_without_viewed():
    episode = {"title": "The Conjugal Configuration", "duration": 20}
    assert is_viewed(episode) is False