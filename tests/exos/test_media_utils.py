from exos.base.media_utils import is_viewed

def test_episode_is_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode) is True

def test_episode_is_not_viewed_as_bool():
    episode = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode) is False