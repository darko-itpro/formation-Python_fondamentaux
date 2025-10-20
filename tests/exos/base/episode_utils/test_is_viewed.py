from exos.base.episode_utils import is_viewed

def test_episode_viewed():
    episode = ["The new Project", 1, 98, True]
    assert is_viewed(episode) is True

def test_episode_not_viewed():
    episode = ['Installing the softwares', 2, 42, False]
    assert is_viewed(episode) is False
